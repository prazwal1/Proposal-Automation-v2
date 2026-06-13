"""Validate an estimate config against the learned schemas — no browser.

Checks, per component:
  - the product resolves to a learned schema
  - every field key matches a learned control
  - select values match an option in the baseline state OR in a recorded
    option_variant (in which case the gating field must be set compatibly)
  - fields that only exist in certain states have their gating field set
  - radio values match a known choice

Exit code 0 = config should build; 1 = problems found.

Usage:
  uv run validate.py myconfig.json [--schemas schemas] [--v1]
"""
import argparse
import json
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from azcalc.adapter import assessment_to_config
from azcalc.engine import GenericEngine, norm


def _tokens(s):
    return set(re.findall(r"[a-z0-9]+", str(s).lower()))


def option_matches(value, options):
    v = norm(value)
    for o in options or []:
        if v and (v == norm(o.get("text") or "") or v == norm(o.get("value") or "")):
            return True
    for o in options or []:
        t = norm(o.get("text") or "")
        if v and (v in t or (t and t in v)):
            return True
    # token-subset, mirroring the engine's _set_select fallback so the
    # validator accepts exactly what the build will resolve (e.g. config value
    # 'SQL Server Standard' vs the Windows option 'SQL Standard')
    vt = _tokens(value)
    for o in options or []:
        ot = _tokens(o.get("text") or "")
        if ot and vt and (ot <= vt or vt <= ot):
            return True
    return False


def _cond_satisfied(when, comp_fields, engine, schema, strict=False):
    """Is a single {field, value, text} condition met by this component?"""
    want_field = norm(when.get("field") or "")
    want_vals = {norm(when.get("value") or ""), norm(when.get("text") or "")}
    want_vals.discard("")
    for key, value in comp_fields.items():
        try:
            f = engine._match_field(schema, key, value)
        except KeyError:
            continue
        names = {norm(f.get("clean_name") or ""), norm(f.get("name") or ""),
                 norm(f.get("label") or ""), norm(f.get("id") or "")}
        if want_field in names:
            v = norm(value)
            if v in want_vals:
                return True
            if not strict and any(v in w or w in v for w in want_vals):
                return True
    return False


def when_satisfied(when, comp_fields, engine, schema, strict=False):
    """Is the gating condition met in this component?

    A `when` may carry an `and` list of extra conditions (a field that depends
    on a *combination* of choices, e.g. SQL Server License for Ubuntu needs
    both Type=SQL Server and OS=Linux) — every part must hold.

    strict=True requires exact (normalized) equality — used for absent_when,
    where substring leniency causes false positives ('Azure VMs' must not
    satisfy 'SAP HANA in Azure VMs', 'Premium SSD' must not satisfy
    'Premium SSD v2').
    """
    if not _cond_satisfied(when, comp_fields, engine, schema, strict):
        return False
    for extra in when.get("and") or []:
        if not _cond_satisfied(extra, comp_fields, engine, schema, strict):
            return False
    return True


def validate(config, schema_dir="schemas"):
    engine = GenericEngine.offline(schema_dir)
    errors, warnings = [], []

    for ci, comp in enumerate(config.get("components", [])):
        where = f"components[{ci}] ({comp.get('name') or comp.get('product')})"
        try:
            schema = engine.store.resolve(comp)
        except KeyError as e:
            errors.append(f"{where}: {e}")
            continue

        comp_fields = dict(comp.get("fields", {}))
        for key, value in comp_fields.items():
            try:
                f = engine._match_field(schema, key, value)
            except KeyError as e:
                errors.append(f"{where}: field '{key}': {str(e)[:200]}")
                continue

            # state-gated absence: this field vanishes in a state the
            # config itself selects
            for when in f.get("absent_when") or []:
                if when_satisfied(when, comp_fields, engine, schema, strict=True):
                    errors.append(
                        f"{where}: '{key}' does not exist when "
                        f"{when['field']} = {when.get('text') or when.get('value')} "
                        "(which this component sets) — use the state-specific "
                        "field instead (see catalog)"
                    )
                    break

            # state-gated existence
            for when in f.get("present_when") or []:
                if when_satisfied(when, comp_fields, engine, schema):
                    break
            else:
                if f.get("present_when"):
                    conds = ", ".join(
                        f"{c['field']}={c.get('text') or c.get('value')}"
                        for c in f["present_when"][:4]
                    )
                    errors.append(
                        f"{where}: '{key}' only exists when one of [{conds}] — "
                        "set that field in this component too"
                    )

            if f["control"] == "select":
                if option_matches(value, f.get("options")):
                    continue
                hit = None
                for var in f.get("option_variants") or []:
                    if option_matches(value, var.get("options")):
                        hit = var
                        break
                if hit is None:
                    sample = [o["text"] for o in (f.get("options") or [])[:6]]
                    if f.get("option_variants") or f.get("depends_on"):
                        # options vary by state and not every state was observed
                        # during learning (e.g. SKUs gated by the chosen instance)
                        warnings.append(
                            f"{where}: '{key}' = '{value}' not seen in any learned "
                            f"state — options depend on {f.get('depends_on')}; "
                            "will be resolved against the live page"
                        )
                    else:
                        errors.append(
                            f"{where}: '{key}' = '{value}' matches no known option. "
                            f"Baseline options start: {sample}"
                        )
                elif not when_satisfied(hit["when"], comp_fields, engine, schema):
                    w = hit["when"]
                    warnings.append(
                        f"{where}: '{key}' = '{value}' is only available when "
                        f"{w['field']} = {w.get('text') or w.get('value')} — "
                        "make sure that field is set accordingly"
                    )
            elif f["control"] == "radio":
                v = norm(value)
                ok = (
                    v == norm(f.get("radio_value") or "")
                    or v == norm(f.get("label") or "")
                    or v in norm(f.get("label") or "")
                )
                if not ok:
                    warnings.append(
                        f"{where}: radio '{key}' = '{value}' did not exactly match "
                        f"choice '{f.get('radio_value')}' ({f.get('label')}) — "
                        "engine will pick the closest radio in the group"
                    )

    return errors, warnings


def main():
    ap = argparse.ArgumentParser(description="Offline estimate config validator")
    ap.add_argument("config")
    ap.add_argument("--schemas", default="schemas")
    ap.add_argument("--v1", action="store_true", help="config is a v1 assessment JSON")
    args = ap.parse_args()

    with open(args.config, encoding="utf-8") as fh:
        config = json.load(fh)
    if args.v1 or "vms" in config:
        config = assessment_to_config(config)

    errors, warnings = validate(config, args.schemas)
    for w in warnings:
        print(f"⚠️  {w}")
    for e in errors:
        print(f"❌ {e}")
    n = len(config.get("components", []))
    if errors:
        print(f"\n{n} components — {len(errors)} errors, {len(warnings)} warnings")
        sys.exit(1)
    print(f"\n✅ {n} components valid ({len(warnings)} warnings)")


if __name__ == "__main__":
    main()
