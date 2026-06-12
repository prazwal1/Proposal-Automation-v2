# Site Recovery

- slug: `site-recovery`  |  module: `site-recovery-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (57): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Instances`** (number)

- **`azure`** (number)

## Example component

```json
{
  "product": "Site Recovery",
  "name": "my-site-recovery",
  "fields": {
    "Region": "Central US",
    "Instances": 1,
    "azure": 1
  }
}
```
