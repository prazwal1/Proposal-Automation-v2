# Mysql

- slug: `mysql`  |  module: `mysql-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Deployment Option`** (select)
  - options: Flexible Server

- **`Tier`** (select)
  - options: Burstable, General Purpose, Memory Optimized

- **`Instance Series`** (select)
  - depends on: `tier`
  - disappears when: `tier` = *Burstable*
  - options: Ddsv6 - Series, Ddsv4 - Series
  - when `tier` = *Memory Optimized*: Edsv6 - Series, Edsv4 - Series

- **`Instance`** (select)
  - depends on: `tier`, `computeInstanceSeries`
  - disappears when: `tier` = *Burstable*
  - options: D2ds v4, 2 vCore, D4ds v4, 4 vCore, D8ds v4, 8 vCore, D16ds v4, 16 vCore, D32ds v4, 32 vCore, D48ds v4, 48 vCore, D64ds v4, 64 vCore, D96ds v4, 96 vCore
  - when `tier` = *Memory Optimized*: E2ds v4, 2 vCore, E4ds v4, 4 vCore, E8ds v4, 8 vCore, E16ds v4, 16 vCore, E32ds v4, 32 vCore, E48ds v4, 48 vCore, E64ds v4, 64 vCore, E80ds v4, 80 vCore, E96ds v4, 96 vCore
  - when `computeInstanceSeries` = *Ddsv6 - Series*: D2ds v6, 2 vCore, D4ds v6, 4 vCore, D8ds v6, 8 vCore, D16ds v6, 16 vCore, D32ds v6, 32 vCore, D48ds v6, 48 vCore, D64ds v6, 64 vCore, D96ds v6, 96 vCore

- **`Servers`** (number)

- **`Hours`** (number)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`GiB`** (number)

- **`Option`** (select)
  - options: Paid IO, Additional IOPS

- **`Redundancy`** (select)
  - depends on: `iopsOption`
  - disappears when: `iopsOption` = *Additional IOPS*
  - options: LRS, ZRS

- **`x1 million IOPS`** (number)
  - depends on: `iopsOption`
  - disappears when: `iopsOption` = *Additional IOPS*

- **`backupUnits`** (number)
  - depends on: `backupUnitsFactor`
  - disappears when: `backupUnitsFactor` = *TiB*

- **`backupUnitsFactor`** (select)
  - depends on: `backupUnitsFactor`
  - disappears when: `backupUnitsFactor` = *TiB*
  - options: GiB, TiB

- **`Compute`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Burstable*
  - options: B1MS, 2 vCore, B2S, 1 vCore, B2MS2, 1 vCore, B4MS, 1 vCore, B8MS, 1 vCore, B12MS, 1 vCore, B16MS, 1 vCore, B20MS, 1 vCore

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Additional IOPS`** (number)
  - depends on: `iopsOption`
  - only exists when: `iopsOption` = *Additional IOPS*

- **`TiB`** (number)
  - depends on: `backupUnitsFactor`
  - only exists when: `backupUnitsFactor` = *TiB*

- **`TiB (backupUnitsFactor)`** (select)
  - depends on: `backupUnitsFactor`
  - only exists when: `backupUnitsFactor` = *TiB*
  - options: GiB, TiB

- **`flexibleServerBillingOption`** (radio)
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~20% savings)), `sv-three-year` (3 year savings plan), `one-year` (1 year reserved (~40% savings)), `three-year` (3 year reserved (~60% savings))

## Example component

```json
{
  "product": "Mysql",
  "name": "my-mysql",
  "fields": {
    "Region": "Central US",
    "Deployment Option": "Flexible Server",
    "Tier": "Burstable",
    "Instance Series": "Ddsv6 - Series",
    "Instance": "D2ds v4, 2 vCore"
  }
}
```
