# Key Vault

- slug: `key-vault`  |  module: `key-vault-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Operations`** (number)

- **`advancedOperations`** (number)

- **`Renewals`** (number)

- **`HSM Protected Keys`** (number)

- **`advancedKeys`** (number)

- **`HSM Pools`** (number)

- **`Hours`** (number)
  - depends on: `hsmPoolsHoursFactor`
  - disappears when: `hsmPoolsHoursFactor` = *Days*

- **`hsmPoolsHoursFactor`** (select)
  - depends on: `hsmPoolsHoursFactor`
  - disappears when: `hsmPoolsHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `hsmPoolsHoursFactor`
  - only exists when: `hsmPoolsHoursFactor` = *Days*

- **`Days (hsmPoolsHoursFactor)`** (select)
  - depends on: `hsmPoolsHoursFactor`
  - only exists when: `hsmPoolsHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Key Vault",
  "name": "my-key-vault",
  "fields": {
    "Region": "Central US",
    "Operations": 1,
    "advancedOperations": 1,
    "Renewals": 1,
    "HSM Protected Keys": 1
  }
}
```
