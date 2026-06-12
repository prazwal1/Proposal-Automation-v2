# Azure Calculator v2 — Self-Learning Selector Mapper

A self-learning Selenium agent for the [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/).
Instead of hand-writing page objects per product (v1: `framework/vm_page.py`,
`backup_page.py`, ...), v2 **learns the page by itself**:

1. **Discover** — enumerates every product card in the picker
   (`button[data-testid$='-picker-item']`), across all categories.
2. **Learn** — adds each product, attaches a **MutationObserver** to the new
   module and waits for the DOM to settle, then extracts *every* control
   (selects + options, text/number inputs, radios, checkboxes, collapsible
   toggles) with a robust CSS selector scoped to the module.
3. **Explore** — clicks every collapsed section (e.g. "Managed Disks" inside
   a VM module), watches the mutations in real time, and diffs the control
   list to record which fields are *revealed by* which toggle.
4. **Play** — the page is reactive, so the learner *interacts* with it:
   it selects **every option of every driving dropdown**, waits for the DOM
   to settle, re-extracts, and records the observed differences:
   - `option_variants` — another field's option list changes per state
     (e.g. Managed Disk `Disk size` flips S10 → E10 → P10 SKUs per `Tier`)
   - `present_when` / `absent_when` — fields that only exist in some states
     (e.g. `License` appears for SQL Server, `storageV2*` fields appear for
     Premium SSD v2, AHB radios vanish on Linux)
   - `selector_variants` — a control whose name/selector itself changes per
     state (captured by label+control identity matching)
   - `depends_on` — the dependency edges between fields
5. **Persist** — writes one JSON schema per product to `schemas/<slug>.json`
   plus a master `schemas/index.json`. The crawl is resumable: already-learned
   products are skipped unless `--force`.
6. **Replay** — `build.py` reads a plain JSON estimate config, matches your
   field names fuzzily against the learned schemas, applies fields in
   on-page order (so dependencies like instance → disk tier → SKU resolve
   naturally), and drives the calculator for **any** learned product.

## Setup

```powershell
cd v2
uv sync
```

## Learn the calculator

```powershell
uv run learn.py --list                                          # see all products (153 discovered)
uv run learn.py --products "Virtual Machines,Managed Disks,Backup"
uv run learn.py --all --headless                                # full crawl (slow, 150+ products)
uv run learn.py --all --max 20                                  # partial crawl
uv run learn.py --all --no-interact                             # skip option sweep (faster, shallower)
uv run learn.py --all --max-options 20                          # sweep bigger dropdowns too
```

Inspect what was learned:

```powershell
uv run python inspect_schema.py schemas/virtual-machines.json   # all fields + selectors
uv run python inspect_variants.py schemas/managed-disks.json    # state dependencies
uv run python test_order.py                                     # offline config→schema match check
```

Output: `schemas/virtual-machines.json`, `schemas/index.json`, failures (if
any) in `schemas/_failures.json`. Re-running resumes where it left off.

### Schema example (excerpt)

```json
{
  "product": "Virtual Machines",
  "picker_testid": "virtual-machines-picker-item",
  "module_testid": "virtual-machines-module",
  "fields": [
    {
      "control": "select",
      "label": "Operating system",
      "name": "operatingSystem",
      "selector": "select[aria-label=\"Operating system\"]",
      "options": [{"value": "linux", "text": "Linux"}, {"value": "windows", "text": "Windows"}],
      "revealed_by": null
    },
    {
      "control": "select",
      "label": "Disk size",
      "name": "managedDiskType",
      "selector": "select[aria-label=\"Disk size\"][name=\"managedDiskType\"]",
      "revealed_by": "Managed Disks",
      "depends_on": ["managedDiskTier"],
      "options": [{"value": "s4", "text": "S4: 32 GiB, ..."}],
      "option_variants": [
        {"when": {"field": "managedDiskTier", "text": "Premium SSD"},
         "options": [{"value": "p10", "text": "P10: 128 GiB, ..."}]}
      ]
    }
  ],
  "toggles": [ { "label": "Managed Disks", "aria_expanded": "false" } ]
}
```

## Configuration catalog (reference for AI agents)

`catalog.py` turns the learned schemas into a reference an AI agent (or a
human) can use to author correct, compatible configs:

```powershell
uv run catalog.py            # regenerates catalog/ from schemas/
```

- `catalog/AGENT_GUIDE.md` — the rules for writing configs (field keys,
  option matching, dependency handling, radio groups)
- `catalog/INDEX.md` — all services with field counts
- `catalog/services/<slug>.md` — per-service page: every field, every option,
  state-dependencies ("only exists when…", "options change when…"), plus a
  ready-made example component
- `catalog/catalog.json` — the same, machine-readable

Validate any config offline (no browser) before building:

```powershell
uv run validate.py configs/examples/three-tier-web.json
```

The validator checks product resolution, field keys, select values against
baseline options *and* learned state-variants, and catches configs that set
a field which doesn't exist in the state the config itself selects (e.g.
`Instances` on an Application Gateway `Standard V2`).

## Deployment examples

Ready-made architectures in `configs/examples/` (all validated, and
`three-tier-web` verified live end-to-end):

| Config | Components |
|---|---|
| `three-tier-web.json` | App Service (P1V3) + VM API tier (3-yr reserved, Premium OS disk) + Azure SQL DB (vCore GP, 1-yr) + App Gateway V2 + Backup + Bandwidth |
| `hub-spoke-vpn.json` | VPN Gateway (VpnGw2) + Azure Firewall + Bastion + VNet peering + DNS + spoke VMs |
| `data-platform.json` | PostgreSQL Flexible Server + SQL DB Hyperscale + Blob storage + Backup + Site Recovery + Monitor |

```powershell
uv run build.py configs/examples/three-tier-web.json --export
```

## Build an estimate

Generic config (any product you have learned):

```powershell
uv run build.py configs/example_estimate.json --export
```

Old v1 assessment JSONs from `../data/` work too (auto-detected by the
`"vms"` key, or force with `--v1`):

```powershell
uv run build.py "../data/assesment.json" --reservation 3 --export
```

Field keys in configs are matched fuzzily (case/punctuation-insensitive)
against each field's label, aria-label, and `name` attribute, with aliases
for the v1 vocabulary (`os` → Operating system, `instance` → size,
`quantity` → Virtual machines). If a field lives behind a collapsed section,
the engine opens that section automatically (`revealed_by`).

## Layout

```
v2/
├── learn.py              # CLI: discover + learn schemas
├── build.py              # CLI: build estimate from JSON config
├── catalog.py            # CLI: generate the AI-agent config catalog
├── validate.py           # CLI: validate a config offline (no browser)
├── inspect_schema.py     # print a learned schema as a table
├── inspect_variants.py   # print learned state-dependencies
├── test_order.py         # offline config→schema matching check
├── configs/
│   └── examples/         # three-tier-web, hub-spoke-vpn, data-platform
├── schemas/              # learned selector schemas (generated, 152 services)
├── catalog/              # generated reference docs (generated)
└── azcalc/
    ├── driver.py         # Chrome setup (standalone from v1)
    ├── js_snippets.py    # MutationObserver + DOM field extraction JS
    ├── learner.py        # SchemaLearner agent (crawl/sweep/persist)
    ├── engine.py         # GenericEngine (replay schemas from configs)
    └── adapter.py        # v1 assessment JSON → generic config
```

## Notes / limits

- Coverage: 152 of 153 discovered products learned. **Dev Box** cannot be
  learned — the calculator itself renders an error in its module (site bug);
  the learner reports this explicitly in `schemas/_failures.json`.

- Microsoft changes the calculator DOM occasionally; when something breaks,
  just re-run `learn.py --force` for the affected product — no code changes.
- Toggle exploration clicks only buttons with `aria-expanded="false"` inside
  the module, so it never touches other estimate rows.
- Some products have cascading dropdowns (options depend on earlier picks).
  The schema stores the options visible at learn time; the engine matches
  partially at run time, so normal flows work, but exotic combinations may
  need field order in your config to follow the on-page order (configs are
  applied top-to-bottom).
