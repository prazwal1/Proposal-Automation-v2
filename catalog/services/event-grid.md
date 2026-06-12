# Event Grid

- slug: `event-grid`  |  module: `event-grid-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (57): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, Switzerland North, Switzerland West, Sweden Central, Sweden South, ...

- **`Tier`** (select)
  - options: Basic, Standard

- **`Operations per month`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Standard*

- **`Throughput Units`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`Hours`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`hoursFactor`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*
  - options: Hours, Days, Month

- **`X1 million Event Operations`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`X1 million MQTT Operations`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

## Example component

```json
{
  "product": "Event Grid",
  "name": "my-event-grid",
  "fields": {
    "Region": "Central US",
    "Tier": "Basic",
    "Operations per month": 1
  }
}
```
