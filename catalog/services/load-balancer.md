# Load Balancer

- slug: `load-balancer`  |  module: `load-balancer-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Basic, Standard, Gateway

- **`Rules`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`GB`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`capacityFactor`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*
  - options: GB, TB

- **`Gateway hours`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Gateway*

- **`Chain hours`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Gateway*

## Example component

```json
{
  "product": "Load Balancer",
  "name": "my-load-balancer",
  "fields": {
    "Region": "Central US",
    "Tier": "Basic"
  }
}
```
