# Authoring estimate configs (guide for AI agents)

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
