# Azure Vmware

- slug: `azure-vmware`  |  module: `azure-vmware-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (45): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE North, Switzerland North, Switzerland West, Sweden Central, ...

- **`Instance`** (select)
  - options: AV36 VCF BYOL: 36 Cores(s), 72 vCPU(s), 576 GB RAM, 18.6 TB vSAN Capacity (all NVMe) ESA, AV36P VCF BYOL: 36 Cores(s), 72 vCPU(s), 768 GB RAM, 20.7 TB vSAN Capacity (all NVMe) ESA, AV48 VCF BYOL: 48 Cores(s), 96 vCPU(s), 1 TB RAM, 25.6 TB vSAN Capacity (all NVMe) ESA, AV64 VCF BYOL: 64 Cores(s), 128 vCPU(s), 1 TB RAM, 19.2 TB vSAN Capacity (all NVMe) ESA

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
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved (~33% discount)), `three-year` (3 year reserved (~57% discount)), `five-year` (5 year reserved)

## Example component

```json
{
  "product": "Azure Vmware",
  "name": "my-azure-vmware",
  "fields": {
    "Region": "Central US",
    "Instance": "AV36 VCF BYOL: 36 Cores(s), 72 vCPU(s), 576 GB RAM, 18.6 TB vSAN Capacity (all NVMe) ESA",
    "Nodes": 1,
    "Hours": 1,
    "hoursFactor": "Hours"
  }
}
```
