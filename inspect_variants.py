"""Print learned state-dependencies (variants) from a schema."""
import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

path = sys.argv[1] if len(sys.argv) > 1 else "schemas/managed-disks.json"
s = json.load(open(path, encoding="utf-8"))
print(f"== {s['product']} ==")
for f in s["fields"]:
    bits = []
    if f.get("depends_on"):
        bits.append(f"depends_on={f['depends_on']}")
    if f.get("option_variants"):
        bits.append(f"{len(f['option_variants'])} option_variants")
    if f.get("selector_variants"):
        bits.append(f"{len(f['selector_variants'])} selector_variants")
    if f.get("present_when"):
        bits.append(
            "present_when=" + str([(c["field"], c["text"]) for c in f["present_when"]][:3])
        )
    if f.get("absent_when"):
        bits.append(
            "absent_when=" + str([(c["field"], c["text"]) for c in f["absent_when"]][:3])
        )
    if bits:
        print(f"  {f.get('label')!r} (name={f.get('name')}): " + "; ".join(bits))
        for v in (f.get("option_variants") or [])[:4]:
            opts = [o["text"] for o in v["options"]][:6]
            print(f"      when {v['when']['field']}={v['when']['text']!r}: {opts} ...")
        if f.get("options"):
            print(f"      baseline: {[o['text'] for o in f['options']][:6]} ...")
