# Azure Dedicated Hsm

- slug: `azure-dedicated-hsm`  |  module: `azure-dedicated-hsm-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (24): East US, East US 2, South Central US, West US, West US 2, UK South, UK West, Switzerland North, Switzerland West, Japan East, Japan West, Central India, South India, North Europe, West Europe, ...

- **`HSM(s)`** (number)

- **`Hours`** (number)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Azure Dedicated Hsm",
  "name": "my-azure-dedicated-hsm",
  "fields": {
    "Region": "East US",
    "HSM(s)": 1,
    "Hours": 1,
    "hoursFactor": "Hours"
  }
}
```
