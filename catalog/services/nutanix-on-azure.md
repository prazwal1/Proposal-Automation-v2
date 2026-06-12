# Nutanix On Azure

- slug: `nutanix-on-azure`  |  module: `nutanix-on-azure-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (19): East US, East US 2, North Central US, South Central US, West US 2, West US 3, UK South, UAE North, Qatar Central, Japan East, Central India, South India, Germany West Central, North Europe, West Europe, ...

- **`Instance`** (select)
  - options: AN36: 36 Cores(s), 576 GB RAM, 18.6 TB All Flash Capacity, AN64: 64 Cores(s), 1 TB RAM, 38.4 TB All Flash Capacity (all NVMe)

- **`Nodes`** (number)

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

- **`billingOption`** (radio)
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved (~36% discount)), `three-year` (3 year reserved (~58% discount))

## Example component

```json
{
  "product": "Nutanix On Azure",
  "name": "my-nutanix-on-azure",
  "fields": {
    "Region": "East US",
    "Instance": "AN36: 36 Cores(s), 576 GB RAM, 18.6 TB All Flash Capacity",
    "Nodes": 1,
    "Hours": 1,
    "hoursFactor": "Hours"
  }
}
```
