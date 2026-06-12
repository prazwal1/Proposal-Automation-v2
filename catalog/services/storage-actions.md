# Storage Actions

- slug: `storage-actions`  |  module: `storage-actions-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (56): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Task assignment execution runs`** (number)

- **`x1 million Blobs scanned per run`** (number)

- **`x1 million average operations per Blob per run`** (number)

## Example component

```json
{
  "product": "Storage Actions",
  "name": "my-storage-actions",
  "fields": {
    "Region": "Central US",
    "Task assignment execution runs": 1,
    "x1 million Blobs scanned per run": 1,
    "x1 million average operations per Blob per run": 1
  }
}
```
