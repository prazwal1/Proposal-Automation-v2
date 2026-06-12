# Search

- slug: `search`  |  module: `search-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (54): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE North, Switzerland North, Switzerland West, Sweden Central, ...

- **`Tier`** (select)
  - options: Free, Basic, Standard S1, Standard S2, Standard S3, Storage Optimized L1, Storage Optimized L2

- **`Units`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Basic*, `tier` = *Standard S1*, `tier` = *Standard S2*, `tier` = *Standard S3*, `tier` = *Storage Optimized L1*, `tier` = *Storage Optimized L2*

- **`Hours`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Basic*, `tier` = *Standard S1*, `tier` = *Standard S2*, `tier` = *Standard S3*, `tier` = *Storage Optimized L1*, `tier` = *Storage Optimized L2*

- **`hoursFactor`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Basic*, `tier` = *Standard S1*, `tier` = *Standard S2*, `tier` = *Standard S3*, `tier` = *Storage Optimized L1*, `tier` = *Storage Optimized L2*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Search",
  "name": "my-search",
  "fields": {
    "Region": "Central US",
    "Tier": "Free"
  }
}
```
