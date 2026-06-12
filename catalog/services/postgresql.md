# Postgresql

- slug: `postgresql`  |  module: `postgresql-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Deployment option`** (select)
  - options: Flexible Server

- **`Tier`** (select)
  - options: Burstable, General Purpose, Memory Optimized

- **`Instance Series`** (select)
  - depends on: `tier`
  - disappears when: `tier` = *Burstable*
  - options: Dadsv5 - Series, Dsv6 - Series, Dsv3 - Series, Ddsv4 - Series, Ddsv5 - Series, Ddsv6 - Series, DCesv6 - Series, DCadsv6 - Series, DCasv5 - Series
  - when `tier` = *Memory Optimized*: Eadsv5 - Series, Esv3 - Series, Esv6 - Series, Edsv4 - Series, Edsv5 - Series, Edsv6 - Series, ECesv6 - Series, ECasv5 - Series, ECadsv6 - Series

- **`Instance`** (select)
  - depends on: `tier`, `computeInstanceSeries`
  - disappears when: `tier` = *Burstable*
  - options: D2ds v5, 2 vCore, D4ds v5, 4 vCore, D8ds v5, 8 vCore, D16ds v5, 16 vCore, D32ds v5, 32 vCore, D48ds v5, 48 vCore, D64ds v5, 64 vCore, D96ds v5, 96 vCore
  - when `tier` = *Memory Optimized*: EC2ads v6, 2 vCore, EC4ads v6, 4 vCore, EC8ads v6, 8 vCore, EC16ads v6, 16 vCore, EC32ads v6, 32 vCore, EC48ads v6, 48 vCore, EC64ads v6, 64 vCore, EC96ads v6, 96 vCore
  - when `computeInstanceSeries` = *Dadsv5 - Series*: D2ads v5, 2 vCore, D4ads v5, 4 vCore, D8ads v5, 8 vCore, D16ads v5, 16 vCore, D32ads v5, 32 vCore, D48ads v5, 48 vCore, D64ads v5, 64 vCore, D96ads v5, 96 vCore
  - when `computeInstanceSeries` = *Dsv6 - Series*: D2s v6, 2 vCore, D4s v6, 4 vCore, D8s v6, 8 vCore, D16s v6, 16 vCore, D32s v6, 32 vCore, D48s v6, 48 vCore, D64s v6, 64 vCore, D96s v6, 96 vCore, D128s v6, 128 vCore
  - when `computeInstanceSeries` = *Dsv3 - Series*: D2s v3, 2 vCore, D4s v3, 4 vCore, D8s v3, 8 vCore, D16s v3, 16 vCore, D32s v3, 32 vCore, D48s v3, 48 vCore, D64s v3, 64 vCore
  - when `computeInstanceSeries` = *Ddsv4 - Series*: D2ds v4, 2 vCore, D4ds v4, 4 vCore, D8ds v4, 8 vCore, D16ds v4, 16 vCore, D32ds v4, 32 vCore, D48ds v4, 48 vCore, D64ds v4, 64 vCore
  - when `computeInstanceSeries` = *Ddsv6 - Series*: D2ds v6, 2 vCore, D4ds v6, 4 vCore, D8ds v6, 8 vCore, D16ds v6, 16 vCore, D32ds v6, 32 vCore, D48ds v6, 48 vCore, D64ds v6, 64 vCore, D96ds v6, 96 vCore, D128ds v6, 128 vCore

- **`Servers or Nodes`** (number)

- **`Hours`** (number)
  - depends on: `singleHoursFactor`
  - disappears when: `singleHoursFactor` = *Days*

- **`singleHoursFactor`** (select)
  - depends on: `singleHoursFactor`
  - disappears when: `singleHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`premiumSsdTier`** (select)
  - options: Premium SSD, Premium SSD v2

- **`GiB`** (number)
  - depends on: `premiumSsdTier`
  - disappears when: `premiumSsdTier` = *Premium SSD v2*

- **`Provisioned IOPS`** (number)
  - depends on: `tier`, `premiumSsdTier`
  - disappears when: `tier` = *Burstable*, `premiumSsdTier` = *Premium SSD v2*

- **`Redundancy`** (select)
  - options: GRS, LRS

- **`flexibleBackupAdditionalStorageUnits`** (number)
  - depends on: `flexibleBackupAdditionalStorageFactor`
  - disappears when: `flexibleBackupAdditionalStorageFactor` = *TiB*

- **`flexibleBackupAdditionalStorageFactor`** (select)
  - depends on: `flexibleBackupAdditionalStorageFactor`
  - disappears when: `flexibleBackupAdditionalStorageFactor` = *TiB*
  - options: GiB, TiB

- **`Compute`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Burstable*
  - options: B1MS, 1 vCore(s), B2MS, 2 vCore(s), B2S, 2 vCore(s), B4MS, 4 vCore(s), B8MS, 8 vCore(s), B12MS, 12 vCore(s), B16MS, 16 vCore(s), B20MS, 20 vCore(s)

- **`Days`** (number)
  - depends on: `singleHoursFactor`
  - only exists when: `singleHoursFactor` = *Days*

- **`Days (singleHoursFactor)`** (select)
  - depends on: `singleHoursFactor`
  - only exists when: `singleHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Disk Size (GiB)`** (number)
  - depends on: `premiumSsdTier`
  - only exists when: `premiumSsdTier` = *Premium SSD v2*

- **`Additional IOPS`** (number)
  - depends on: `premiumSsdTier`
  - only exists when: `premiumSsdTier` = *Premium SSD v2*

- **`Additional throughput (MBps)`** (number)
  - depends on: `premiumSsdTier`
  - only exists when: `premiumSsdTier` = *Premium SSD v2*

- **`TiB`** (number)
  - depends on: `flexibleBackupAdditionalStorageFactor`
  - only exists when: `flexibleBackupAdditionalStorageFactor` = *TiB*

- **`TiB (flexibleBackupAdditionalStorageFactor)`** (select)
  - depends on: `flexibleBackupAdditionalStorageFactor`
  - only exists when: `flexibleBackupAdditionalStorageFactor` = *TiB*
  - options: GiB, TiB

- **`computeBillingOption`** (radio)
  - depends on: `tier`
  - disappears when: `tier` = *Burstable*
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~20% savings)), `sv-three-year` (3 year savings plan), `one-year` (1 year reserved (~40% savings)), `three-year` (3 year reserved (~60% savings))

## Example component

```json
{
  "product": "Postgresql",
  "name": "my-postgresql",
  "fields": {
    "Region": "Central US",
    "Deployment option": "Flexible Server",
    "Tier": "Burstable",
    "Instance Series": "Dadsv5 - Series",
    "Instance": "D2ds v5, 2 vCore"
  }
}
```
