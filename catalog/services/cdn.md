# Cdn

- slug: `cdn`  |  module: `cdn-module`

## Fields

- **`product-name`** (text)

- **`Provider`** (select)
  - options: Microsoft (classic)

- **`GB`** (number)
  - depends on: `zoneOneStorageUnits`
  - disappears when: `zoneOneStorageUnits` = *TB*

- **`zoneOneStorageUnits`** (select)
  - depends on: `zoneOneStorageUnits`
  - disappears when: `zoneOneStorageUnits` = *TB*
  - options: GB, TB

- **`zone2`** (number)
  - depends on: `zoneTwoStorageUnits`
  - disappears when: `zoneTwoStorageUnits` = *TB*

- **`zoneTwoStorageUnits`** (select)
  - depends on: `zoneTwoStorageUnits`
  - disappears when: `zoneTwoStorageUnits` = *TB*
  - options: GB, TB

- **`zone3`** (number)
  - depends on: `zoneThreeStorageUnits`
  - disappears when: `zoneThreeStorageUnits` = *TB*

- **`zoneThreeStorageUnits`** (select)
  - depends on: `zoneThreeStorageUnits`
  - disappears when: `zoneThreeStorageUnits` = *TB*
  - options: GB, TB

- **`zone4`** (number)
  - depends on: `zoneFourStorageUnits`
  - disappears when: `zoneFourStorageUnits` = *TB*

- **`zoneFourStorageUnits`** (select)
  - depends on: `zoneFourStorageUnits`
  - disappears when: `zoneFourStorageUnits` = *TB*
  - options: GB, TB

- **`zone5`** (number)
  - depends on: `zoneFiveStorageUnits`
  - disappears when: `zoneFiveStorageUnits` = *TB*

- **`zoneFiveStorageUnits`** (select)
  - depends on: `zoneFiveStorageUnits`
  - disappears when: `zoneFiveStorageUnits` = *TB*
  - options: GB, TB

- **`TB`** (number)
  - depends on: `zoneOneStorageUnits`
  - only exists when: `zoneOneStorageUnits` = *TB*

- **`TB (zoneOneStorageUnits)`** (select)
  - depends on: `zoneOneStorageUnits`
  - only exists when: `zoneOneStorageUnits` = *TB*
  - options: GB, TB

- **`TB (zone2)`** (number)
  - depends on: `zoneTwoStorageUnits`
  - only exists when: `zoneTwoStorageUnits` = *TB*

- **`TB (zoneTwoStorageUnits)`** (select)
  - depends on: `zoneTwoStorageUnits`
  - only exists when: `zoneTwoStorageUnits` = *TB*
  - options: GB, TB

- **`TB (zone3)`** (number)
  - depends on: `zoneThreeStorageUnits`
  - only exists when: `zoneThreeStorageUnits` = *TB*

- **`TB (zoneThreeStorageUnits)`** (select)
  - depends on: `zoneThreeStorageUnits`
  - only exists when: `zoneThreeStorageUnits` = *TB*
  - options: GB, TB

- **`TB (zone4)`** (number)
  - depends on: `zoneFourStorageUnits`
  - only exists when: `zoneFourStorageUnits` = *TB*

- **`TB (zoneFourStorageUnits)`** (select)
  - depends on: `zoneFourStorageUnits`
  - only exists when: `zoneFourStorageUnits` = *TB*
  - options: GB, TB

- **`TB (zone5)`** (number)
  - depends on: `zoneFiveStorageUnits`
  - only exists when: `zoneFiveStorageUnits` = *TB*

- **`TB (zoneFiveStorageUnits)`** (select)
  - depends on: `zoneFiveStorageUnits`
  - only exists when: `zoneFiveStorageUnits` = *TB*
  - options: GB, TB

## Example component

```json
{
  "product": "Cdn",
  "name": "my-cdn",
  "fields": {
    "Provider": "Microsoft (classic)",
    "GB": 1,
    "zoneOneStorageUnits": "GB",
    "zone2": 1,
    "zoneTwoStorageUnits": "GB"
  }
}
```
