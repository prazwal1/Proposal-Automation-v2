# Azure Sql Database

- slug: `azure-sql-database`  |  module: `azure-sql-database-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Type`** (select)
  - options: Elastic Pool, Single Database

- **`Purchase Model`** (select)
  - options: vCore, DTU

- **`Service Tier`** (select)
  - depends on: `purchaseModel`
  - options: General Purpose, Business Critical, Hyperscale

- **`Compute Tier`** (select)
  - depends on: `type`
  - only exists when: `vcoreTier` = *Hyperscale*
  - disappears when: `type` = *Elastic Pool*
  - options: Provisioned, Serverless

- **`Hardware Type`** (select)
  - depends on: `type`, `purchaseModel`, `vcoreTier`, `computeTier`
  - disappears when: `purchaseModel` = *DTU*
  - options: Standard-series (Gen 5), Fsv2-series, DC-series
  - when `type` = *Elastic Pool*: Standard-series (Gen 5), DC-series
  - when `vcoreTier` = *Hyperscale*: Standard-series (Gen 5), Premium-series, Premium-series, memory optimized, DC-series
  - when `computeTier` = *Serverless*: Standard-series (Gen 5)

- **`Instance`** (select)
  - depends on: `type`, `purchaseModel`, `vcoreTier`, `computeTier`, `generation`
  - disappears when: `purchaseModel` = *DTU*, `computeTier` = *Serverless*
  - options: 2 vCore, 4 vCore, 6 vCore, 8 vCore, 10 vCore, 12 vCore, 14 vCore, 16 vCore, 18 vCore, 20 vCore, 24 vCore, 32 vCore, 40 vCore, 80 vCore, 128 vCore
  - when `type` = *Elastic Pool*: 4 vCore, 6 vCore, 8 vCore, 10 vCore, 12 vCore, 14 vCore, 16 vCore, 18 vCore, 20 vCore, 24 vCore, ...
  - when `vcoreTier` = *Hyperscale*: 2 vCore, 4 vCore, 6 vCore, 8 vCore, 10 vCore, 12 vCore, 14 vCore, 16 vCore, 18 vCore, 20 vCore, ...
  - when `generation` = *Fsv2-series*: 8 vCore, 10 vCore, 12 vCore, 14 vCore, 16 vCore, 18 vCore, 20 vCore, 24 vCore, 32 vCore, 36 vCore, ...
  - when `generation` = *DC-series*: 2 vCore, 4 vCore, 6 vCore, 8 vCore, 10 vCore, 12 vCore, 14 vCore, 16 vCore, 18 vCore, 20 vCore, ...

- **`Disaster Recovery`** (select)
  - depends on: `type`, `purchaseModel`, `vcoreTier`, `computeTier`
  - disappears when: `type` = *Elastic Pool*, `purchaseModel` = *DTU*, `vcoreTier` = *Hyperscale*, `computeTier` = *Serverless*
  - options: Primary or Geo replica, Standby replica

- **`Redundancy`** (select)
  - depends on: `type`, `generation`
  - only exists when: `vcoreTier` = *Hyperscale*
  - disappears when: `type` = *Elastic Pool*, `generation` = *Fsv2-series*, `generation` = *DC-series*
  - options: Locally Redundant, Zone Redundant

- **`Databases`** (number)
  - depends on: `type`, `computeTier`
  - disappears when: `type` = *Elastic Pool*, `computeTier` = *Serverless*

- **`Hours`** (number)
  - depends on: `computeTier`, `hoursFactor`
  - disappears when: `computeTier` = *Serverless*, `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `computeTier`, `hoursFactor`
  - disappears when: `computeTier` = *Serverless*, `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`GB`** (number)
  - depends on: `type`, `vcoreTier`

- **`redundancy`** (select)
  - options: LRS, ZRS, RA-GRS, RA-GZRS

- **`backupStorageSize`** (number)
  - depends on: `purchaseModel`
  - disappears when: `purchaseModel` = *DTU*

- **`ltrDatabaseSize`** (number)
  - depends on: `ltrDatabaseSizeFactor`
  - disappears when: `ltrDatabaseSizeFactor` = *TB*

- **`ltrDatabaseSizeFactor`** (select)
  - depends on: `ltrDatabaseSizeFactor`
  - disappears when: `ltrDatabaseSizeFactor` = *TB*
  - options: GB, TB

- **`Number of weeks`** (number)

- **`Number of months`** (number)

- **`Number of years`** (number)

- **`Pools`** (number)
  - depends on: `type`
  - only exists when: `type` = *Elastic Pool*

- **`Performance level`** (select)
  - depends on: `purchaseModel`
  - only exists when: `purchaseModel` = *DTU*
  - options: B: 5 DTUs, 2 GB included storage per DB

- **`High availability replicas per database`** (number)
  - depends on: `vcoreTier`
  - only exists when: `vcoreTier` = *Hyperscale*

- **`singleHyperscaleReplicaHours`** (number)
  - depends on: `vcoreTier`
  - only exists when: `vcoreTier` = *Hyperscale*

- **`singleHyperscaleReplicaHoursFactor`** (select)
  - depends on: `vcoreTier`
  - only exists when: `vcoreTier` = *Hyperscale*
  - options: Hours, Days, Month

- **`Named replicas per database`** (number)
  - depends on: `vcoreTier`
  - only exists when: `vcoreTier` = *Hyperscale*

- **`namedReplicaHours`** (number)
  - depends on: `vcoreTier`
  - only exists when: `vcoreTier` = *Hyperscale*

- **`namedReplicaHoursFactor`** (select)
  - depends on: `vcoreTier`
  - only exists when: `vcoreTier` = *Hyperscale*
  - options: Hours, Days, Month

- **`singleHyperscaleStorageUnitsFactor`** (select)
  - depends on: `vcoreTier`
  - only exists when: `vcoreTier` = *Hyperscale*
  - options: GB, TB

- **`Maximum vCores`** (select)
  - depends on: `computeTier`
  - only exists when: `computeTier` = *Serverless*
  - options: 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 32, 40, 80

- **`Minimum vCores`** (select)
  - depends on: `computeTier`
  - only exists when: `computeTier` = *Serverless*
  - options: 0.5, 0.75, 1

- **`CPU Used (vCores)`** (number)
  - depends on: `computeTier`
  - only exists when: `computeTier` = *Serverless*

- **`Memory used (GB)`** (number)
  - depends on: `computeTier`
  - only exists when: `computeTier` = *Serverless*

- **`Duration (in seconds, max 2,678,400 seconds (744 hours))`** (number)
  - depends on: `computeTier`
  - only exists when: `computeTier` = *Serverless*

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
  - depends on: `purchaseModel`
  - disappears when: `purchaseModel` = *DTU*
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~24% discount)), `sv-three-year` (3 year savings plan), `one-year` (1 year reserved), `three-year` (3 year reserved)

- **`softwareBillingOption`** (radio)
  - depends on: `purchaseModel`, `vcoreTier`, `computeTier`
  - disappears when: `purchaseModel` = *DTU*, `vcoreTier` = *Hyperscale*, `computeTier` = *Serverless*
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan), `ahb` (Azure Hybrid Benefit), `failover-rights` (Failover rights, standby replica)

## Example component

```json
{
  "product": "Azure Sql Database",
  "name": "my-azure-sql-database",
  "fields": {
    "Region": "Central US",
    "Type": "Elastic Pool",
    "Purchase Model": "vCore",
    "Service Tier": "General Purpose",
    "Hardware Type": "Standard-series (Gen 5)"
  }
}
```
