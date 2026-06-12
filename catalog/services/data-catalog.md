# Data Catalog

- slug: `data-catalog`  |  module: `data-catalog-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options: East US, North Central US, West Central US, West US, Japan East, Japan West, Italy North, North Europe, West Europe, US Gov Arizona, US Gov Texas, US Gov Virginia, Australia East, East Asia, Southeast Asia

- **`Tier`** (select)
  - options: Free, Standard

- **`Users`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

## Example component

```json
{
  "product": "Data Catalog",
  "name": "my-data-catalog",
  "fields": {
    "Region": "East US",
    "Tier": "Free"
  }
}
```
