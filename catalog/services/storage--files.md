# Files

- slug: `storage--files`  |  module: `storage\files-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Media tier`** (select)
  - options: SSD (Premium), HDD (Standard)

- **`Redundancy`** (select)
  - depends on: `performanceTier`, `billingModel`
  - options: Local (LRS), Zone (ZRS), Geo (GRS), GeoZone (GZRS)
  - when `performanceTier` = *SSD (Premium)*: Local (LRS), Zone (ZRS)
  - when `billingModel` = *Provisioned v1*: Local (LRS), Zone (ZRS)

- **`Billing model`** (select)
  - options: Provisioned v1, Provisioned v2, Pay-as-you-go

- **`GiB`** (number)
  - depends on: `performanceTier`, `billingModel`

- **`provisionedV2StorageFactor`** (select)
  - depends on: `performanceTier`, `billingModel`
  - options: GiB, TiB

- **`Hours`** (number)
  - depends on: `performanceTier`

- **`provisionedV2StorageHoursFactor`** (select)
  - depends on: `performanceTier`
  - options: Hours, Days, Month

- **`IO/sec`** (number)
  - depends on: `performanceTier`, `billingModel`

- **`provisionedV2IopsHours`** (number)
  - depends on: `performanceTier`, `billingModel`, `provisionedV2IopsHoursFactor`
  - disappears when: `performanceTier` = *SSD (Premium)*, `billingModel` = *Provisioned v1*, `billingModel` = *Pay-as-you-go*, `provisionedV2IopsHoursFactor` = *Days*

- **`provisionedV2IopsHoursFactor`** (select)
  - depends on: `performanceTier`, `billingModel`, `provisionedV2IopsHoursFactor`
  - disappears when: `performanceTier` = *SSD (Premium)*, `billingModel` = *Provisioned v1*, `billingModel` = *Pay-as-you-go*, `provisionedV2IopsHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`MiB/sec`** (number)
  - depends on: `performanceTier`, `billingModel`

- **`provisionedV2ThroughputHours`** (number)
  - depends on: `performanceTier`, `billingModel`, `provisionedV2ThroughputHoursFactor`
  - disappears when: `performanceTier` = *SSD (Premium)*, `billingModel` = *Provisioned v1*, `billingModel` = *Pay-as-you-go*, `provisionedV2ThroughputHoursFactor` = *Days*

- **`provisionedV2ThroughputHoursFactor`** (select)
  - depends on: `performanceTier`, `billingModel`, `provisionedV2ThroughputHoursFactor`
  - disappears when: `performanceTier` = *SSD (Premium)*, `billingModel` = *Provisioned v1*, `billingModel` = *Pay-as-you-go*, `provisionedV2ThroughputHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`usedSnapshotV2StorageUnits`** (number)
  - depends on: `performanceTier`, `billingModel`, `usedSnapshotV2StorageFactor`
  - disappears when: `performanceTier` = *SSD (Premium)*, `billingModel` = *Provisioned v1*, `billingModel` = *Pay-as-you-go*, `usedSnapshotV2StorageFactor` = *TiB*

- **`usedSnapshotV2StorageFactor`** (select)
  - depends on: `performanceTier`, `billingModel`, `usedSnapshotV2StorageFactor`
  - disappears when: `performanceTier` = *SSD (Premium)*, `billingModel` = *Provisioned v1*, `billingModel` = *Pay-as-you-go*, `usedSnapshotV2StorageFactor` = *TiB*
  - options: GiB, TiB

- **`usedSnapshotV2StorageHours`** (number)
  - depends on: `performanceTier`, `billingModel`, `usedSnapshotV2StorageHoursFactor`
  - disappears when: `performanceTier` = *SSD (Premium)*, `billingModel` = *Provisioned v1*, `billingModel` = *Pay-as-you-go*, `usedSnapshotV2StorageHoursFactor` = *Days*

- **`usedSnapshotV2StorageHoursFactor`** (select)
  - depends on: `performanceTier`, `billingModel`, `usedSnapshotV2StorageHoursFactor`
  - disappears when: `performanceTier` = *SSD (Premium)*, `billingModel` = *Provisioned v1*, `billingModel` = *Pay-as-you-go*, `usedSnapshotV2StorageHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`usedSoftDeletedV2StorageUnits`** (number)
  - depends on: `performanceTier`, `billingModel`, `usedSoftDeletedV2StorageFactor`
  - disappears when: `performanceTier` = *SSD (Premium)*, `billingModel` = *Provisioned v1*, `billingModel` = *Pay-as-you-go*, `usedSoftDeletedV2StorageFactor` = *TiB*

- **`usedSoftDeletedV2StorageFactor`** (select)
  - depends on: `performanceTier`, `billingModel`, `usedSoftDeletedV2StorageFactor`
  - disappears when: `performanceTier` = *SSD (Premium)*, `billingModel` = *Provisioned v1*, `billingModel` = *Pay-as-you-go*, `usedSoftDeletedV2StorageFactor` = *TiB*
  - options: GiB, TiB

- **`usedSoftDeletedV2StorageHours`** (number)
  - depends on: `performanceTier`, `billingModel`, `usedSoftDeletedV2StorageHoursFactor`
  - disappears when: `performanceTier` = *SSD (Premium)*, `billingModel` = *Provisioned v1*, `billingModel` = *Pay-as-you-go*, `usedSoftDeletedV2StorageHoursFactor` = *Days*

- **`usedSoftDeletedV2StorageHoursFactor`** (select)
  - depends on: `performanceTier`, `billingModel`, `usedSoftDeletedV2StorageHoursFactor`
  - disappears when: `performanceTier` = *SSD (Premium)*, `billingModel` = *Provisioned v1*, `billingModel` = *Pay-as-you-go*, `usedSoftDeletedV2StorageHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Additional sync servers`** (number)
  - depends on: `performanceTier`, `billingModel`

- **`Access tier`** (select)
  - depends on: `billingModel`
  - only exists when: `billingModel` = *Pay-as-you-go*
  - options: Transaction Optimized, Hot, Cool

- **`Write Transactions (x 10,000)`** (number)
  - depends on: `billingModel`
  - only exists when: `billingModel` = *Pay-as-you-go*

- **`List Transactions (x 10,000)`** (number)
  - depends on: `billingModel`
  - only exists when: `billingModel` = *Pay-as-you-go*

- **`Read Transactions (x 10,000)`** (number)
  - depends on: `billingModel`
  - only exists when: `billingModel` = *Pay-as-you-go*

- **`All Other Operations, except for Delete (x 10,000)`** (number)
  - depends on: `billingModel`
  - only exists when: `billingModel` = *Pay-as-you-go*

- **`TiB`** (number)
  - depends on: `provisionedV2StorageFactor`
  - only exists when: `provisionedV2StorageFactor` = *TiB*

- **`TiB (provisionedV2StorageFactor)`** (select)
  - depends on: `provisionedV2StorageFactor`
  - only exists when: `provisionedV2StorageFactor` = *TiB*
  - options: GiB, TiB

- **`Days`** (number)
  - depends on: `provisionedV2StorageHoursFactor`
  - only exists when: `provisionedV2StorageHoursFactor` = *Days*

- **`Days (provisionedV2StorageHoursFactor)`** (select)
  - depends on: `provisionedV2StorageHoursFactor`
  - only exists when: `provisionedV2StorageHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (provisionedV2IopsHours)`** (number)
  - depends on: `provisionedV2IopsHoursFactor`
  - only exists when: `provisionedV2IopsHoursFactor` = *Days*

- **`Days (provisionedV2IopsHoursFactor)`** (select)
  - depends on: `provisionedV2IopsHoursFactor`
  - only exists when: `provisionedV2IopsHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (provisionedV2ThroughputHours)`** (number)
  - depends on: `provisionedV2ThroughputHoursFactor`
  - only exists when: `provisionedV2ThroughputHoursFactor` = *Days*

- **`Days (provisionedV2ThroughputHoursFactor)`** (select)
  - depends on: `provisionedV2ThroughputHoursFactor`
  - only exists when: `provisionedV2ThroughputHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`TiB (usedSnapshotV2StorageUnits)`** (number)
  - depends on: `usedSnapshotV2StorageFactor`
  - only exists when: `usedSnapshotV2StorageFactor` = *TiB*

- **`TiB (usedSnapshotV2StorageFactor)`** (select)
  - depends on: `usedSnapshotV2StorageFactor`
  - only exists when: `usedSnapshotV2StorageFactor` = *TiB*
  - options: GiB, TiB

- **`Days (usedSnapshotV2StorageHours)`** (number)
  - depends on: `usedSnapshotV2StorageHoursFactor`
  - only exists when: `usedSnapshotV2StorageHoursFactor` = *Days*

- **`Days (usedSnapshotV2StorageHoursFactor)`** (select)
  - depends on: `usedSnapshotV2StorageHoursFactor`
  - only exists when: `usedSnapshotV2StorageHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`TiB (usedSoftDeletedV2StorageUnits)`** (number)
  - depends on: `usedSoftDeletedV2StorageFactor`
  - only exists when: `usedSoftDeletedV2StorageFactor` = *TiB*

- **`TiB (usedSoftDeletedV2StorageFactor)`** (select)
  - depends on: `usedSoftDeletedV2StorageFactor`
  - only exists when: `usedSoftDeletedV2StorageFactor` = *TiB*
  - options: GiB, TiB

- **`Days (usedSoftDeletedV2StorageHours)`** (number)
  - depends on: `usedSoftDeletedV2StorageHoursFactor`
  - only exists when: `usedSoftDeletedV2StorageHoursFactor` = *Days*

- **`Days (usedSoftDeletedV2StorageHoursFactor)`** (select)
  - depends on: `usedSoftDeletedV2StorageHoursFactor`
  - only exists when: `usedSoftDeletedV2StorageHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`billingOption`** (radio)
  - depends on: `billingModel`
  - only exists when: `billingModel` = *Provisioned v1*, `billingModel` = *Pay-as-you-go*
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved), `three-year` (3 year reserved)

## Example component

```json
{
  "product": "Files",
  "name": "my-storage--files",
  "fields": {
    "Region": "Central US",
    "Media tier": "SSD (Premium)",
    "Redundancy": "Local (LRS)",
    "Billing model": "Provisioned v1",
    "GiB": 1
  }
}
```
