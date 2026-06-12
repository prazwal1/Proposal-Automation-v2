# Databox

- slug: `databox`  |  module: `databox-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (46): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, Switzerland North, Sweden Central, Sweden South, ...

- **`Products`** (select)
  - options: Data Box Disk, Data Box 120, Data Box 525, Data Box Gateway

- **`Order`** (number)
  - depends on: `databoxProduct`
  - disappears when: `databoxProduct` = *Data Box 120*, `databoxProduct` = *Data Box 525*, `databoxProduct` = *Data Box Gateway*

- **`Disk`** (number)
  - depends on: `databoxProduct`
  - disappears when: `databoxProduct` = *Data Box 120*, `databoxProduct` = *Data Box 525*, `databoxProduct` = *Data Box Gateway*

- **`Additional Days`** (number)
  - depends on: `databoxProduct`

- **`Unit`** (number)
  - depends on: `databoxProduct`
  - only exists when: `databoxProduct` = *Data Box 120*

## Example component

```json
{
  "product": "Databox",
  "name": "my-databox",
  "fields": {
    "Region": "Central US",
    "Products": "Data Box Disk",
    "Order": 1,
    "Disk": 1,
    "Additional Days": 1
  }
}
```
