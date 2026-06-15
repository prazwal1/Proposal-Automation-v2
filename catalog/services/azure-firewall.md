# Azure Firewall

- slug: `azure-firewall`  |  module: `azure-firewall-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (58): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Basic, Standard, Premium

- **`Logical firewall units`** (number)
  - depends on: `tier`, `standardHoursUnits`, `standardDataProcessedUnits`, `standardCapacityHoursUnits`

- **`Hours`** (number)
  - depends on: `tier`, `standardCapacityHoursUnits`, `standardHoursUnits`

- **`standardHoursUnits`** (select)
  - depends on: `tier`, `standardCapacityHoursUnits`, `standardHoursUnits`
  - options: Hours, Days, Month

- **`GB`** (number)
  - depends on: `tier`, `standardHoursUnits`, `standardDataProcessedUnits`, `standardCapacityHoursUnits`

- **`standardDataProcessedUnits`** (select)
  - depends on: `tier`, `standardHoursUnits`, `standardDataProcessedUnits`, `standardCapacityHoursUnits`
  - options: GB, TB

- **`With Secured Virtual Hub`** (select)
  - depends on: `tier`, `standardHoursUnits`, `standardDataProcessedUnits`, `standardCapacityHoursUnits`
  - disappears when: `tier` = *Basic*
  - options: Yes, No

- **`Number of capacity units`** (number)
  - depends on: `tier`, `standardHoursUnits`, `standardDataProcessedUnits`, `standardCapacityHoursUnits`
  - disappears when: `tier` = *Basic*

- **`standardCapacityHours`** (number)
  - depends on: `tier`, `standardCapacityHoursUnits`, `standardHoursUnits`, `standardDataProcessedUnits`
  - disappears when: `tier` = *Basic*, `tier` = *Premium*, `standardCapacityHoursUnits` = *Days*

- **`standardCapacityHoursUnits`** (select)
  - depends on: `tier`, `standardCapacityHoursUnits`, `standardHoursUnits`, `standardDataProcessedUnits`
  - disappears when: `tier` = *Basic*, `tier` = *Premium*, `standardCapacityHoursUnits` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `standardHoursUnits`, `tier`, `basicHoursUnits`, `premiumHoursUnits`, `premiumCapacityHoursUnits`, `standardDataProcessedUnits`, `standardCapacityHoursUnits`
  - only exists when: `standardHoursUnits` = *Days*

- **`Days (standardHoursUnits)`** (select)
  - depends on: `standardHoursUnits`, `tier`, `basicHoursUnits`, `premiumHoursUnits`, `premiumCapacityHoursUnits`, `standardDataProcessedUnits`, `standardCapacityHoursUnits`
  - only exists when: `standardHoursUnits` = *Days*
  - options: Hours, Days, Month

- **`TB`** (number)
  - depends on: `standardDataProcessedUnits`, `tier`, `basicDataProcessedUnits`, `premiumDataProcessedUnits`, `standardHoursUnits`, `standardCapacityHoursUnits`
  - only exists when: `standardDataProcessedUnits` = *TB*

- **`TB (standardDataProcessedUnits)`** (select)
  - depends on: `standardDataProcessedUnits`, `tier`, `basicDataProcessedUnits`, `premiumDataProcessedUnits`, `standardHoursUnits`, `standardCapacityHoursUnits`
  - only exists when: `standardDataProcessedUnits` = *TB*
  - options: GB, TB

- **`Days (standardCapacityHours)`** (number)
  - depends on: `standardCapacityHoursUnits`, `standardHoursUnits`, `tier`, `standardDataProcessedUnits`
  - only exists when: `standardCapacityHoursUnits` = *Days*
  - disappears when: `tier` = *Basic* and `standardHoursUnits` = *Hours*, `tier` = *Premium* and `standardHoursUnits` = *Hours*, `standardCapacityHoursUnits` = *Hours* and `standardHoursUnits` = *Hours*

- **`Days (standardCapacityHoursUnits)`** (select)
  - depends on: `standardCapacityHoursUnits`, `standardHoursUnits`, `tier`, `standardDataProcessedUnits`
  - only exists when: `standardCapacityHoursUnits` = *Days*
  - disappears when: `tier` = *Basic* and `standardHoursUnits` = *Hours*, `tier` = *Premium* and `standardHoursUnits` = *Hours*, `standardCapacityHoursUnits` = *Hours* and `standardHoursUnits` = *Hours*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Azure Firewall",
  "name": "my-azure-firewall",
  "fields": {
    "Region": "Central US",
    "Tier": "Basic",
    "Logical firewall units": 1,
    "Hours": 1,
    "standardHoursUnits": "Hours"
  }
}
```
