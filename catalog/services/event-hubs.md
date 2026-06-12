# Event Hubs

- slug: `event-hubs`  |  module: `event-hubs-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Basic, Standard, Premium, Dedicated

- **`Throughput units`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Premium*, `tier` = *Dedicated*

- **`Hours`** (number)
  - depends on: `tier`

- **`hoursFactor`** (select)
  - depends on: `tier`
  - options: Hours, Days, Month

- **`Million Events per month`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Premium*, `tier` = *Dedicated*

- **`Processing Units`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*
  - options: 1, 2, 4, 8, 16

- **`Overage GB/month`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*

- **`Capacity Units`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Dedicated*
  - options: 1, 2, 4, 8, 12, 16, 20

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Event Hubs",
  "name": "my-event-hubs",
  "fields": {
    "Region": "Central US",
    "Tier": "Basic",
    "Throughput units": 1,
    "Hours": 1,
    "hoursFactor": "Hours"
  }
}
```
