"""Quick utility: print a learned schema in a readable table."""
import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

path = sys.argv[1] if len(sys.argv) > 1 else "schemas/virtual-machines.json"
s = json.load(open(path, encoding="utf-8"))
print(f"product={s['product']}  module={s['module_testid']}  fields={len(s['fields'])}")
print("FIELDS:")
for f in s["fields"]:
    opts = f" options={len(f['options'])}" if f.get("options") else ""
    print(
        f"  {f['control']:9} label={str(f.get('label'))!r:42} name={str(f.get('name'))!r:30} "
        f"sel={str(f.get('selector'))!r} unique={f['selector_unique']} "
        f"visible={f['visible']} revealed_by={f.get('revealed_by')}{opts}"
    )
print("TOGGLES:")
for t in s["toggles"]:
    print(
        f"  label={str(t.get('label'))!r:55} aria_expanded={str(t.get('aria_expanded'))!r:8} "
        f"sel={str(t.get('selector'))!r}"
    )
