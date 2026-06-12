# Azure Sql

- slug: `azure-sql`  |  module: `azure-sql-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Managed Instance

- **`Service Tier`** (select)
  - options: Next Generation General Purpose, General Purpose, Business Critical

- **`Instance Type`** (select)
  - depends on: `vcoreTier`, `generation`
  - options: Single Instance, Instance Pools
  - when `vcoreTier` = *Next Generation General Purpose*: Single Instance
  - when `vcoreTier` = *Business Critical*: Single Instance
  - when `generation` = *Premium-series, memory optimized*: Single Instance

- **`Hardware Type`** (select)
  - depends on: `managedInstanceType`
  - options: Standard-series (Gen 5), Premium-series, Premium-series, memory optimized
  - when `managedInstanceType` = *Instance Pools*: Standard-series (Gen 5), Premium-series

- **`Compute`** (select)
  - depends on: `managedInstanceType`, `generation`
  - options: 4 vCore, 8 vCore, 16 vCore, 24 vCore, 32 vCore, 40 vCore, 64 vCore, 80 vCore
  - when `managedInstanceType` = *Instance Pools*: 8 vCore, 16 vCore, 24 vCore, 32 vCore, 40 vCore, 64 vCore, 80 vCore
  - when `generation` = *Premium-series, memory optimized*: 4 vCore, 8 vCore, 16 vCore, 24 vCore, 32 vCore, 40 vCore, 64 vCore

- **`Disaster Recovery`** (select)
  - options: Primary Instance, Geo-secondary replicated instance

- **`Redundancy`** (select)
  - depends on: `vcoreTier`, `managedInstanceType`
  - disappears when: `vcoreTier` = *Next Generation General Purpose*, `managedInstanceType` = *Instance Pools*
  - options: Locally Redundant, Zone Redundant

- **`Instances`** (number)

- **`Hours`** (number)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`32GB units`** (number)

- **`Backup Storage Tier`** (select)
  - depends on: `recovery`
  - disappears when: `recovery` = *Geo-secondary replicated instance*
  - options: LRS, ZRS, RA-GRS, RA-GZRS

- **`GB`** (number)
  - depends on: `recovery`
  - disappears when: `recovery` = *Geo-secondary replicated instance*

- **`ltrDatabaseSize`** (number)
  - depends on: `recovery`, `ltrDatabaseSizeFactor`
  - disappears when: `recovery` = *Geo-secondary replicated instance*, `ltrDatabaseSizeFactor` = *TB*

- **`ltrDatabaseSizeFactor`** (select)
  - depends on: `recovery`, `ltrDatabaseSizeFactor`
  - disappears when: `recovery` = *Geo-secondary replicated instance*, `ltrDatabaseSizeFactor` = *TB*
  - options: GB, TB

- **`Number of weeks`** (number)
  - depends on: `recovery`
  - disappears when: `recovery` = *Geo-secondary replicated instance*

- **`Number of months`** (number)
  - depends on: `recovery`
  - disappears when: `recovery` = *Geo-secondary replicated instance*

- **`Number of years`** (number)
  - depends on: `recovery`
  - disappears when: `recovery` = *Geo-secondary replicated instance*

- **`Additional IOPS`** (number)
  - depends on: `vcoreTier`
  - only exists when: `vcoreTier` = *Next Generation General Purpose*

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`TB`** (number)
  - depends on: `ltrDatabaseSizeFactor`
  - only exists when: `ltrDatabaseSizeFactor` = *TB*

- **`TB (ltrDatabaseSizeFactor)`** (select)
  - depends on: `ltrDatabaseSizeFactor`
  - only exists when: `ltrDatabaseSizeFactor` = *TB*
  - options: GB, TB

- **`databaseBillingOption`** (radio)
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~24% discount)), `sv-three-year` (3 year savings plan), `one-year` (1 year reserved), `three-year` (3 year reserved)

- **`softwareBillingOption`** (radio)
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan), `ahb` (Azure Hybrid Benefit), `failover-rights` (Failover rights, standby replica)

## Example component

```json
{
  "product": "Azure Sql",
  "name": "my-azure-sql",
  "fields": {
    "Region": "Central US",
    "Tier": "Managed Instance",
    "Service Tier": "Next Generation General Purpose",
    "Instance Type": "Single Instance",
    "Hardware Type": "Standard-series (Gen 5)"
  }
}
```
