# Confidential Ledger

- slug: `confidential-ledger`  |  module: `confidential-ledger-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (18): East US, North Central US, South Central US, West US, UK South, UK West, UAE North, Sweden Central, Japan East, Italy North, Central India, Germany West Central, North Europe, West Europe, Canada Central, ...

- **`Tier`** (select)
  - options: P1

- **`Instances`** (number)

- **`Hours`** (number)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`GB`** (number)
  - depends on: `storageFactor`
  - disappears when: `storageFactor` = *TB*

- **`storageFactor`** (select)
  - depends on: `storageFactor`
  - disappears when: `storageFactor` = *TB*
  - options: GB, TB

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`TB`** (number)
  - depends on: `storageFactor`
  - only exists when: `storageFactor` = *TB*

- **`TB (storageFactor)`** (select)
  - depends on: `storageFactor`
  - only exists when: `storageFactor` = *TB*
  - options: GB, TB

## Example component

```json
{
  "product": "Confidential Ledger",
  "name": "my-confidential-ledger",
  "fields": {
    "Region": "East US",
    "Tier": "P1",
    "Instances": 1,
    "Hours": 1,
    "hoursFactor": "Hours"
  }
}
```
