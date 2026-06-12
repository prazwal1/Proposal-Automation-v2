# App Configuration

- slug: `app-configuration`  |  module: `app-configuration-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Free, Standard

- **`Day(s)`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`Number of replicas`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`replicaDays`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`Overage requests (in 10,000 units)`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

## Example component

```json
{
  "product": "App Configuration",
  "name": "my-app-configuration",
  "fields": {
    "Region": "Central US",
    "Tier": "Free"
  }
}
```
