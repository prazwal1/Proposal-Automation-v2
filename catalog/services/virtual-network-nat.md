# Virtual Network Nat

- slug: `virtual-network-nat`  |  module: `virtual-network-nat-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Standard

- **`Hours`** (number)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`GB`** (number)
  - depends on: `dataProcessedUnits`
  - disappears when: `dataProcessedUnits` = *TB*

- **`dataProcessedUnits`** (select)
  - depends on: `dataProcessedUnits`
  - disappears when: `dataProcessedUnits` = *TB*
  - options: GB, TB

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`TB`** (number)
  - depends on: `dataProcessedUnits`
  - only exists when: `dataProcessedUnits` = *TB*

- **`TB (dataProcessedUnits)`** (select)
  - depends on: `dataProcessedUnits`
  - only exists when: `dataProcessedUnits` = *TB*
  - options: GB, TB

## Example component

```json
{
  "product": "Virtual Network Nat",
  "name": "my-virtual-network-nat",
  "fields": {
    "Region": "Central US",
    "Tier": "Standard",
    "Hours": 1,
    "hoursFactor": "Hours",
    "GB": 1
  }
}
```
