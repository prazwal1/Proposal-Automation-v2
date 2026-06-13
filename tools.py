"""Plain-Python tool layer over the v2 engine — no CLI, no MCP, no printing.

Every consumer (mcp_server.py today; the agent service / REST API / bots
later) imports these functions. All paths are resolved relative to the repo
root so callers may run from any working directory.

Tools:
  list_services()                  - one-line summary of every learned service
  search_catalog(query)            - find services by name/category/field/option
  get_service_doc(slug)            - full per-service reference (markdown)
  get_config_guide()               - how to author estimate configs
  validate_config(config)          - offline validation against learned schemas
  start_build(config)              - queue a headless calculator build (async)
  check_build(job_id)              - poll a build job; returns xlsx path when done
  list_builds()                    - recent build jobs and their states
  quick_price(...)                 - ballpark prices from Azure Retail Prices API
"""
import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import uuid
from functools import lru_cache
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
SCHEMA_DIR = REPO_ROOT / "schemas"
CATALOG_DIR = REPO_ROOT / "catalog"
JOBS_DIR = REPO_ROOT / "Azure_Estimates" / "jobs"

RETAIL_PRICES_URL = "https://prices.azure.com/api/retail/prices"

# in-process handles for builds started by this process (best effort; job
# state is also persisted on disk so check_build works across restarts)
_JOBS: dict = {}


def _norm(s):
    return re.sub(r"[^a-z0-9]+", "", str(s).lower())


def _as_config(config):
    """Accept a config as dict or JSON string; apply the v1 adapter if needed."""
    if isinstance(config, str):
        config = json.loads(config)
    if not isinstance(config, dict):
        raise ValueError("config must be a JSON object")
    if "vms" in config:  # old v1 assessment format
        from azcalc.adapter import assessment_to_config
        config = assessment_to_config(config)
    return config


@lru_cache(maxsize=1)
def _catalog():
    data = json.loads((CATALOG_DIR / "catalog.json").read_text(encoding="utf-8"))
    return data["services"]


# ---------------------------------------------------------------- catalog --

def list_services():
    """All learned services: product, slug, category, field count."""
    return [
        {
            "product": s["product"],
            "slug": s["slug"],
            "category": s.get("category"),
            "fields": len(s["fields"]),
        }
        for s in _catalog()
    ]


def search_catalog(query, limit=12):
    """Rank services against the query.

    Matches product name, slug and category first; falls back to field keys
    and option texts so queries like "premium ssd" or "savings plan" hit the
    services that actually carry those controls.
    """
    q = _norm(query)
    if not q:
        return list_services()

    results = []
    for s in _catalog():
        score, why = 0, []
        name, slug, cat = _norm(s["product"]), _norm(s["slug"]), _norm(s.get("category") or "")
        if q == name or q == slug:
            score, why = 100, ["exact name"]
        elif q in name or q in slug:
            score, why = 80, ["name"]
        elif name in q:
            score, why = 60, ["name in query"]
        if q in cat:
            score, why = max(score, 40), why + ["category"]

        field_hits = []
        for f in s["fields"]:
            if q in _norm(f.get("key") or "") or q in _norm(f.get("label") or ""):
                field_hits.append(f["key"])
            else:
                for o in (f.get("options") or [])[:200]:
                    if q in _norm(o.get("text") or ""):
                        field_hits.append(f"{f['key']} → {o['text']}")
                        break
            if len(field_hits) >= 3:
                break
        if field_hits:
            score = max(score, 30)
            why.append("fields: " + "; ".join(field_hits))

        if score:
            results.append({
                "product": s["product"],
                "slug": s["slug"],
                "category": s.get("category"),
                "score": score,
                "match": ", ".join(why),
            })

    results.sort(key=lambda r: -r["score"])
    return results[:limit]


def get_service_doc(slug):
    """Markdown reference for one service: every field, option, dependency."""
    path = CATALOG_DIR / "services" / f"{slug}.md"
    if not path.exists():
        wanted = _norm(slug)
        near = [s["slug"] for s in _catalog()
                if wanted in _norm(s["slug"]) or wanted in _norm(s["product"])]
        raise KeyError(
            f"No service '{slug}'. "
            + (f"Did you mean: {', '.join(near[:8])}?" if near
               else "Use search_catalog to find the right slug.")
        )
    return path.read_text(encoding="utf-8")


def get_config_guide():
    """The config-authoring guide (format, rules, workflow)."""
    return (CATALOG_DIR / "AGENT_GUIDE.md").read_text(encoding="utf-8")


# --------------------------------------------------------------- validate --

def validate_config(config):
    """Offline validation against learned schemas. No browser, instant."""
    from validate import validate
    config = _as_config(config)
    errors, warnings = validate(config, schema_dir=str(SCHEMA_DIR))
    return {
        "ok": not errors,
        "components": len(config.get("components", [])),
        "errors": errors,
        "warnings": warnings,
    }


# ------------------------------------------------------------------ build --

def start_build(config, export=True, force=False):
    """Queue a headless calculator build; returns a job descriptor immediately.

    Validates first and refuses on errors unless force=True (a Selenium build
    takes minutes — don't waste it on a config that cannot apply).
    """
    config = _as_config(config)
    if not force:
        v = validate_config(config)
        if not v["ok"]:
            return {"started": False, "reason": "validation failed", **v}

    job_id = time.strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:6]
    job_dir = JOBS_DIR / job_id
    job_dir.mkdir(parents=True, exist_ok=True)
    config_path = job_dir / "config.json"
    config_path.write_text(json.dumps(config, indent=2), encoding="utf-8")

    cmd = [sys.executable, str(REPO_ROOT / "build.py"), str(config_path),
           "--headless", "--download", str(job_dir)]
    if export:
        cmd.append("--export")

    log = open(job_dir / "build.log", "w", encoding="utf-8")
    kwargs = {}
    if sys.platform == "win32":
        kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW
    proc = subprocess.Popen(cmd, cwd=str(REPO_ROOT), stdout=log, stderr=log,
                            stdin=subprocess.DEVNULL, **kwargs)
    _JOBS[job_id] = proc
    (job_dir / "meta.json").write_text(json.dumps({
        "pid": proc.pid,
        "started": time.strftime("%Y-%m-%d %H:%M:%S"),
        "estimate_name": config.get("estimate_name"),
        "components": len(config.get("components", [])),
        "export": export,
    }), encoding="utf-8")
    return {
        "started": True,
        "job_id": job_id,
        "note": "Builds take ~1-3 min per component. Poll check_build(job_id).",
    }


def _job_state(job_dir: Path):
    job_id = job_dir.name
    meta = {}
    meta_path = job_dir / "meta.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    xlsx = [str(p) for p in job_dir.glob("*.xlsx")]
    log_path = job_dir / "build.log"
    log_tail = ""
    if log_path.exists():
        text = log_path.read_text(encoding="utf-8", errors="replace")
        log_tail = "\n".join(text.splitlines()[-15:])

    proc = _JOBS.get(job_id)
    if proc is not None and proc.poll() is None:
        status = "running"
    elif proc is not None:
        status = "succeeded" if proc.returncode == 0 and (xlsx or not meta.get("export")) else "failed"
    elif xlsx:
        status = "succeeded"  # job from a previous process; output exists
    else:
        status = "unknown (started by a previous process; check the log tail)"

    return {
        "job_id": job_id,
        "status": status,
        "estimate_name": meta.get("estimate_name"),
        "started": meta.get("started"),
        "xlsx": xlsx,
        "log_tail": log_tail,
    }


def check_build(job_id):
    """State of one build job: running / succeeded / failed, xlsx path, log tail."""
    job_dir = JOBS_DIR / job_id
    if not job_dir.exists():
        raise KeyError(f"No build job '{job_id}'. Use list_builds().")
    return _job_state(job_dir)


def list_builds(limit=10):
    """Most recent build jobs, newest first."""
    if not JOBS_DIR.exists():
        return []
    dirs = sorted((d for d in JOBS_DIR.iterdir() if d.is_dir()),
                  key=lambda d: d.name, reverse=True)
    return [_job_state(d) for d in dirs[:limit]]


# ------------------------------------------------------------ quick price --

def quick_price(service_name=None, region=None, sku_contains=None,
                product_contains=None, price_type="Consumption", top=10):
    """Ballpark unit prices from the Azure Retail Prices API (no auth, live).

    These are list prices for sanity checks during a conversation — the
    official quotation always comes from a calculator build (start_build).
    """
    clauses = []
    if price_type:
        clauses.append(f"priceType eq '{price_type}'")
    if service_name:
        clauses.append(f"serviceName eq '{service_name}'")
    if region:
        clauses.append(f"armRegionName eq '{region}'")
    if sku_contains:
        clauses.append(f"contains(skuName, '{sku_contains}')")
    if product_contains:
        clauses.append(f"contains(productName, '{product_contains}')")
    if not clauses:
        raise ValueError("Provide at least one filter (service_name, region, "
                         "sku_contains, product_contains).")

    url = RETAIL_PRICES_URL + "?" + urllib.parse.urlencode(
        {"$filter": " and ".join(clauses)})
    req = urllib.request.Request(url, headers={"User-Agent": "azcalc-v2"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    items = [
        {
            "service": i.get("serviceName"),
            "product": i.get("productName"),
            "sku": i.get("skuName"),
            "armSku": i.get("armSkuName"),
            "meter": i.get("meterName"),
            "region": i.get("armRegionName"),
            "retailPrice": i.get("retailPrice"),
            "unit": i.get("unitOfMeasure"),
            "type": i.get("type"),
            "reservationTerm": i.get("reservationTerm"),
        }
        for i in data.get("Items", [])[:top]
    ]
    return {
        "count_returned": len(items),
        "more_available": bool(data.get("NextPageLink")),
        "hint": ("Region names are ARM names like 'southeastasia'. "
                 "serviceName examples: 'Virtual Machines', 'Storage', "
                 "'Azure Database for MySQL'."),
        "items": items,
    }
