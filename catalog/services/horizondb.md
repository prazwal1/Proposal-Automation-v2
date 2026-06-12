# Horizondb

- slug: `horizondb`  |  module: `horizondb-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (59): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Number Of Replicas`** (number)

- **`Cores/Replica`** (select)
  - options: 2, 4, 8, 16, 20, 32, 48, 64, 96, 128, 192

- **`Hours`** (number)
  - depends on: `computeHoursFactor`
  - disappears when: `computeHoursFactor` = *Days*

- **`computeHoursFactor`** (select)
  - depends on: `computeHoursFactor`
  - disappears when: `computeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`GB`** (number)
  - depends on: `storageUnits`
  - disappears when: `storageUnits` = *TB*

- **`storageUnits`** (select)
  - depends on: `storageUnits`
  - disappears when: `storageUnits` = *TB*
  - options: GB, TB

- **`backupStorageCount`** (number)
  - depends on: `backupStorageUnits`
  - disappears when: `backupStorageUnits` = *TB*

- **`backupStorageUnits`** (select)
  - depends on: `backupStorageUnits`
  - disappears when: `backupStorageUnits` = *TB*
  - options: GB, TB

- **`Days`** (number)
  - depends on: `computeHoursFactor`
  - only exists when: `computeHoursFactor` = *Days*

- **`Days (computeHoursFactor)`** (select)
  - depends on: `computeHoursFactor`
  - only exists when: `computeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`TB`** (number)
  - depends on: `storageUnits`
  - only exists when: `storageUnits` = *TB*

- **`TB (storageUnits)`** (select)
  - depends on: `storageUnits`
  - only exists when: `storageUnits` = *TB*
  - options: GB, TB

- **`TB (backupStorageCount)`** (number)
  - depends on: `backupStorageUnits`
  - only exists when: `backupStorageUnits` = *TB*

- **`TB (backupStorageUnits)`** (select)
  - depends on: `backupStorageUnits`
  - only exists when: `backupStorageUnits` = *TB*
  - options: GB, TB

## Example component

```json
{
  "product": "Horizondb",
  "name": "my-horizondb",
  "fields": {
    "Region": "Central US",
    "Number Of Replicas": 1,
    "Cores/Replica": "2",
    "Hours": 1,
    "computeHoursFactor": "Hours"
  }
}
```
