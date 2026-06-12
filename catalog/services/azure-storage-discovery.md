# Azure Storage Discovery

- slug: `azure-storage-discovery`  |  module: `azure-storage-discovery-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (53): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Pricing Plan`** (select)
  - options: Standard

- **`storageAccountAnalyzed`** (number)

- **`In million objects`** (number)

## Example component

```json
{
  "product": "Azure Storage Discovery",
  "name": "my-azure-storage-discovery",
  "fields": {
    "Region": "Central US",
    "Pricing Plan": "Standard",
    "storageAccountAnalyzed": 1,
    "In million objects": 1
  }
}
```
