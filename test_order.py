"""Offline check: field matching + ordering against learned schemas (no browser)."""
import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from azcalc.engine import GenericEngine, SchemaStore


class FakeEngine(GenericEngine):
    def __init__(self, schema_dir="schemas"):
        self.store = SchemaStore(schema_dir)


eng = FakeEngine()
config = json.load(open("configs/example_estimate.json", encoding="utf-8"))
for comp in config["components"]:
    schema = eng.store.resolve(comp)
    fields = {"product-name": comp["name"], **comp["fields"]}
    print(f"== {schema['product']} ==")
    for key, value in eng._order_fields(schema, fields):
        try:
            f = eng._match_field(schema, key, value)
            idx = next(i for i, x in enumerate(schema["fields"]) if x is f)
            print(f"  {key!r:28} -> idx {idx:3} {f.get('label')!r} (name={f.get('name')})")
        except KeyError as e:
            print(f"  {key!r:28} -> NO MATCH: {str(e)[:100]}")
