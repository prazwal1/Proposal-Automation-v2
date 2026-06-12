# Azure Elastic San

- slug: `azure-elastic-san`  |  module: `azure-elastic-san-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (46): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Redundancy`** (select)
  - options: LRS, ZRS

- **`Units`** (number)

- **`scaleUnits`** (number)

## Example component

```json
{
  "product": "Azure Elastic San",
  "name": "my-azure-elastic-san",
  "fields": {
    "Region": "Central US",
    "Redundancy": "LRS",
    "Units": 1,
    "scaleUnits": 1
  }
}
```
