# Managed Lustre

- slug: `managed-lustre`  |  module: `managed-lustre-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (46): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Sweden Central, ...

- **`Storage Type`** (select)
  - options: SSD

- **`Throughput Tier`** (select)
  - options: Lite (40 MB/s/TiB), Standard (125 MB/s), Premium (250 MB/s), Ultra (500 MB/s)

- **`TiB increments`** (number)

- **`Hours`** (number)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Managed Lustre",
  "name": "my-managed-lustre",
  "fields": {
    "Region": "Central US",
    "Storage Type": "SSD",
    "Throughput Tier": "Lite (40 MB/s/TiB)",
    "TiB increments": 1,
    "Hours": 1
  }
}
```
