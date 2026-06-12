# Artifact Signing

- slug: `artifact-signing`  |  module: `artifact-signing-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (57): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tiers`** (select)
  - options: Basic, Premium

- **`Signatures per month`** (number)

## Example component

```json
{
  "product": "Artifact Signing",
  "name": "my-artifact-signing",
  "fields": {
    "Region": "Central US",
    "Tiers": "Basic",
    "Signatures per month": 1
  }
}
```
