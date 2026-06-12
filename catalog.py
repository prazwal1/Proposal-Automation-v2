"""Generate the service configuration catalog from learned schemas.

The catalog is the reference an AI agent reads to author valid estimate
configs for build.py:

  catalog/catalog.json     - machine-readable: every service, every field,
                             every option, every state-dependency
  catalog/services/<slug>.md - per-service reference page
  catalog/INDEX.md         - one-line summary of all services
  catalog/AGENT_GUIDE.md   - how to write configs (rules + examples)

Usage:
  uv run catalog.py [--schemas schemas] [--out catalog]
"""
import argparse
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PRICE_RE = re.compile(r",?\s*\$[\d,.]+\s*/\s*\w+\s*$")


def clean_option(text):
    """Strip volatile price suffixes: 'P10: 128 GiB, ..., $19.71/month' -> sku part."""
    return PRICE_RE.sub("", text).strip()


def field_key(field, used_keys):
    """Pick the config key an agent should use for this field."""
    for cand in (field.get("label"), field.get("aria_label"),
                 field.get("clean_name"), field.get("name"), field.get("id")):
        if not cand:
            continue
        cand = cand.strip()
        if len(cand) > 60 or cand.lower() == "none":
            continue
        if cand not in used_keys:
            return cand
    # last resort: disambiguate with the name attribute
    base = field.get("label") or field.get("clean_name") or "field"
    return f"{base} ({field.get('name')})"


def summarize_when(conds):
    return [
        {"field": c.get("field"), "value": c.get("value"), "text": c.get("text")}
        for c in conds
    ]


def build_service_entry(schema):
    fields_out = []
    radio_groups = OrderedDict()
    used_keys = set()

    for f in schema["fields"]:
        if f["control"] == "radio":
            group = f.get("data_name_override") or f.get("clean_name") or f.get("name")
            g = radio_groups.setdefault(group, {
                "key": group,
                "control": "radio",
                "label": group,
                "choices": [],
                "depends_on": f.get("depends_on") or [],
                "present_when": summarize_when(f.get("present_when") or []),
                "absent_when": summarize_when(f.get("absent_when") or []),
                "revealed_by": f.get("revealed_by"),
            })
            g["choices"].append({
                "value": f.get("radio_value"),
                "label": f.get("label"),
            })
            continue

        key = field_key(f, used_keys)
        used_keys.add(key)
        entry = {
            "key": key,
            "control": f["control"],
            "label": f.get("label"),
            "name": f.get("name"),
            "revealed_by": f.get("revealed_by"),
            "depends_on": f.get("depends_on") or [],
        }
        if f.get("options") is not None:
            entry["options"] = [
                {"value": o["value"], "text": clean_option(o["text"])}
                for o in f["options"]
            ]
        if f.get("option_variants"):
            entry["option_variants"] = [
                {
                    "when": {"field": v["when"].get("field"),
                             "value": v["when"].get("value"),
                             "text": v["when"].get("text")},
                    "options": [
                        {"value": o["value"], "text": clean_option(o["text"])}
                        for o in v["options"]
                    ],
                }
                for v in f["option_variants"]
            ]
        if f.get("present_when"):
            entry["present_when"] = summarize_when(f["present_when"])
        if f.get("absent_when"):
            entry["absent_when"] = summarize_when(f["absent_when"])
        fields_out.append(entry)

    fields_out.extend(radio_groups.values())
    return {
        "product": schema["product"],
        "slug": schema["slug"],
        "category": schema.get("category"),
        "module_testid": schema["module_testid"],
        "learned_at": schema.get("learned_at"),
        "fields": fields_out,
    }


def example_component(entry):
    """A minimal-but-plausible component example for the docs."""
    fields = {}
    for f in entry["fields"]:
        if f["key"] in ("product-name",):
            continue
        if f.get("revealed_by") or f.get("present_when"):
            continue  # keep examples to the always-visible basics
        if f["control"] == "select" and f.get("options"):
            fields[f["key"]] = f["options"][0]["text"]
        elif f["control"] == "number":
            fields[f["key"]] = 1
        if len(fields) >= 5:
            break
    return {
        "product": entry["product"],
        "name": f"my-{entry['slug']}",
        "fields": fields,
    }


def render_md(entry):
    lines = [f"# {entry['product']}", ""]
    lines.append(f"- slug: `{entry['slug']}`  |  module: `{entry['module_testid']}`")
    lines.append("")
    lines.append("## Fields")
    lines.append("")
    for f in entry["fields"]:
        bits = [f"**`{f['key']}`** ({f['control']})"]
        if f.get("revealed_by"):
            bits.append(f"— section: *{f['revealed_by']}* (opened automatically)")
        lines.append("- " + " ".join(bits))
        if f.get("depends_on"):
            lines.append(f"  - depends on: {', '.join('`%s`' % d for d in f['depends_on'])}")
        if f.get("present_when"):
            conds = ", ".join(
                f"`{c['field']}` = *{c.get('text') or c.get('value')}*"
                for c in f["present_when"][:6]
            )
            lines.append(f"  - only exists when: {conds}")
        if f.get("absent_when"):
            conds = ", ".join(
                f"`{c['field']}` = *{c.get('text') or c.get('value')}*"
                for c in f["absent_when"][:6]
            )
            lines.append(f"  - disappears when: {conds}")
        if f["control"] == "radio":
            choices = ", ".join(
                f"`{c['value']}` ({c['label']})" for c in f.get("choices", [])
            )
            lines.append(f"  - choices: {choices}")
        if f.get("options") is not None:
            opts = [o["text"] for o in f["options"]]
            if len(opts) > 15:
                shown = ", ".join(opts[:15])
                lines.append(f"  - options ({len(opts)}): {shown}, ...")
            else:
                lines.append(f"  - options: {', '.join(opts) if opts else '(state-dependent, see variants)'}")
        for v in (f.get("option_variants") or [])[:6]:
            opts = [o["text"] for o in v["options"]]
            shown = ", ".join(opts[:10]) + (", ..." if len(opts) > 10 else "")
            lines.append(
                f"  - when `{v['when']['field']}` = *{v['when'].get('text') or v['when'].get('value')}*: {shown}"
            )
        lines.append("")
    lines.append("## Example component")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(example_component(entry), indent=2))
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


AGENT_GUIDE = """# Authoring estimate configs (guide for AI agents)

This catalog describes every service of the Azure Pricing Calculator that the
v2 engine can drive. Use it to produce config JSONs for `build.py`.

## Config format

```json
{
  "estimate_name": "My Deployment",
  "components": [
    {
      "product": "Virtual Machines",   // product name OR "slug": "virtual-machines"
      "name": "web-01",                 // display name shown in the estimate
      "fields": { "<field key>": <value>, ... }
    }
  ]
}
```

## Rules

1. **Field keys** come from each service page in `services/<slug>.md`
   (the `key` of every field). Matching is fuzzy (case/punctuation
   insensitive; label, aria-label or HTML name all work), but prefer the
   documented key.
2. **Select values**: use the option *text* (partial matches allowed, e.g.
   `"P10"` matches `"P10: 128 GiB"`). Check `options` — and if the field has
   `option_variants`, the valid options depend on another field: set that
   driver field in the same component and pick an option valid for that state.
3. **Dependent fields**: if a field lists `only exists when`, your config
   MUST also set the gating field to one of the enabling values, otherwise
   the engine cannot find the control. The engine applies fields in on-page
   order automatically, so you don't need to order keys yourself.
4. **Radio groups**: one key per group (e.g. `computeBillingOption`), value =
   choice `value` (`payg`, `one-year`, `three-year`, `sv-one-year`, ...) or
   its label text.
5. **Numbers**: plain integers. **Checkboxes**: true/false.
6. Fields marked `section: *X*` live behind a collapsible — the engine opens
   it automatically; just set the field.
7. Region-like dropdowns accept the visible region name, e.g.
   `"Southeast Asia"`.
8. Repeat a component entry to add the same product multiple times
   (e.g. one "Managed Disks" component per data disk).

## Workflow

1. Pick services from `INDEX.md`.
2. Read each service's `services/<slug>.md`.
3. Write the config; validate offline (no browser):
   `uv run validate.py myconfig.json`
4. Build it: `uv run build.py myconfig.json [--export]`
"""


def main():
    ap = argparse.ArgumentParser(description="Generate service config catalog")
    ap.add_argument("--schemas", default="schemas")
    ap.add_argument("--out", default="catalog")
    args = ap.parse_args()

    schema_dir = Path(args.schemas)
    out = Path(args.out)
    (out / "services").mkdir(parents=True, exist_ok=True)

    index = json.loads((schema_dir / "index.json").read_text(encoding="utf-8"))
    entries = []
    for slug, meta in sorted(index.items()):
        schema = json.loads(
            (schema_dir / meta["file"]).read_text(encoding="utf-8")
        )
        entry = build_service_entry(schema)
        entries.append(entry)
        (out / "services" / f"{slug}.md").write_text(
            render_md(entry), encoding="utf-8"
        )

    (out / "catalog.json").write_text(
        json.dumps({"services": entries}, indent=2), encoding="utf-8"
    )

    # INDEX.md
    lines = ["# Service catalog", "",
             f"{len(entries)} services learned from the Azure Pricing Calculator.",
             "", "| Product | slug | fields | state-dependent |", "|---|---|---|---|"]
    for e in entries:
        dep = sum(
            1 for f in e["fields"]
            if f.get("depends_on") or f.get("present_when") or f.get("option_variants")
        )
        lines.append(
            f"| {e['product']} | [`{e['slug']}`](services/{e['slug']}.md) "
            f"| {len(e['fields'])} | {dep} |"
        )
    (out / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out / "AGENT_GUIDE.md").write_text(AGENT_GUIDE, encoding="utf-8")

    print(f"📖 Catalog generated: {len(entries)} services → {out}/")


if __name__ == "__main__":
    main()
