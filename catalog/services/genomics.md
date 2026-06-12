# Genomics

- slug: `genomics`  |  module: `genomics-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options: East US, East US 2, South Central US, West US, West US 2, UK South, UK West, North Europe, West Europe, Canada Central, Canada East, Australia East, Australia Southeast, East Asia, Southeast Asia

- **`Gigabases processed per genome`** (number)

- **`Number of genomes processed in a month`** (number)

## Example component

```json
{
  "product": "Genomics",
  "name": "my-genomics",
  "fields": {
    "Region": "East US",
    "Gigabases processed per genome": 1,
    "Number of genomes processed in a month": 1
  }
}
```
