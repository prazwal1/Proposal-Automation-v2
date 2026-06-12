# Service Bus

- slug: `service-bus`  |  module: `service-bus-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Basic, Standard, Premium

- **`x 1 million operations`** (number)
  - depends on: `tier`

- **`Hours`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*, `tier` = *Premium*

- **`messagingOperationsHoursFactor`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*, `tier` = *Premium*
  - options: Hours, Days, Month

- **`Brokered Connections`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`Listeners`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`Overage GB`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`x 100 relay hours`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`x 10,000 messages`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`Daily message units`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*
  - options: 0, 1, 2, 4, 8, 16

- **`Number of Partitions`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*
  - options: 1, 2, 4

## Example component

```json
{
  "product": "Service Bus",
  "name": "my-service-bus",
  "fields": {
    "Region": "Central US",
    "Tier": "Basic",
    "x 1 million operations": 1
  }
}
```
