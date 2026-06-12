# Notification Hubs

- slug: `notification-hubs`  |  module: `notification-hubs-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (46): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE North, Switzerland North, Switzerland West, Sweden Central, ...

- **`Tier`** (select)
  - options: Free, Basic, Standard

- **`Millions`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Free*

## Example component

```json
{
  "product": "Notification Hubs",
  "name": "my-notification-hubs",
  "fields": {
    "Region": "Central US",
    "Tier": "Free",
    "Millions": 1
  }
}
```
