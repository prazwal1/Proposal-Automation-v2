# Virtual Machines

- slug: `virtual-machines`  |  module: `virtual-machines-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Operating system`** (select)
  - options: Linux, Windows

- **`Type`** (select)
  - depends on: `operatingSystem`
  - options: (OS Only), BizTalk, SQL Server
  - when `operatingSystem` = *Linux*: Red Hat Enterprise Linux, Red Hat Enterprise Linux with HA, RHEL for SAP Business Applications, RHEL for SAP with HA, SQL Server Red Hat Enterprise Linux, SQL Server SUSE Priority, SQL Server Ubuntu Linux, SQL Server Ubuntu Pro, SUSE Linux Enterprise, SUSE Linux Enterprise for HPC, ...

- **`Tier`** (select)
  - options: Basic, Standard

- **`Category`** (select)
  - depends on: `type`, `tier`
  - options: All, Compute optimized, General purpose, GPU, High performance compute, Memory optimized, Storage optimized
  - when `type` = *BizTalk*: 
  - when `type` = *SQL Server*: 
  - when `tier` = *Basic*: All, General purpose

- **`Instance Series`** (select)
  - depends on: `operatingSystem`, `type`, `tier`, `category`
  - options (144): All, A-series, Av2 Standard, Basv2-series, Bs-series, Bsv2-series, Constrained vCPUs capable, Da v4-series, Dadsv5-series, Dadsv6-series, Dadsv7-series, Daldsv6-series, Daldsv7-series, Dalsv6-series, Dalsv7-series, ...
  - when `operatingSystem` = *Linux*: All, A-series, Av2 Standard, Basv2-series, Bpsv2-series, Bs-series, Bsv2-series, Constrained vCPUs capable, Da v4-series, Dadsv5-series, ...
  - when `type` = *BizTalk*: All
  - when `type` = *SQL Server*: All
  - when `tier` = *Basic*: All, A-series
  - when `category` = *Compute optimized*: All, Fadsv7-series, Faldsv7-series, Falsv6-series, Falsv7-series, Famdsv7-series, Famsv6-series, Famsv7-series, Fasv6-series, Fasv7-series, ...
  - when `category` = *General purpose*: All, A-series, Av2 Standard, Basv2-series, Bs-series, Bsv2-series, Da v4-series, Dadsv5-series, Dadsv6-series, Dadsv7-series, ...

- **`Instance: (Need help finding the right VM?)`** (text)
  - depends on: `type`
  - disappears when: `type` = *BizTalk*, `type` = *SQL Server*

- **`Virtual machines`** (number)

- **`Hours`** (number)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`managedDiskTier`** (select) — section: *Managed Disks* (opened automatically)
  - depends on: `category`
  - options: Standard HDD, Standard SSD
  - when `category` = *Compute optimized*: Standard HDD, Standard SSD, Premium SSD, Premium SSD v2
  - when `category` = *GPU*: Standard HDD, Standard SSD, Premium SSD, Premium SSD v2
  - when `category` = *High performance compute*: Standard HDD, Standard SSD, Premium SSD, Premium SSD v2
  - when `category` = *Memory optimized*: Standard HDD, Standard SSD, Premium SSD, Premium SSD v2
  - when `category` = *Storage optimized*: Standard HDD, Standard SSD, Premium SSD, Premium SSD v2

- **`Disk size`** (select) — section: *Managed Disks* (opened automatically)
  - depends on: `managedDiskTier`
  - options: S4: 32 GiB, S6: 64 GiB, S10: 128 GiB, S15: 256 GiB, S20: 512 GiB, S30: 1024 GiB, S40: 2048 GiB, S50: 4096 GiB, S60: 8192 GiB, S70: 16384 GiB, S80: 32767 GiB
  - when `managedDiskTier` = *Standard SSD*: E1: 4 GiB, E2: 8 GiB, E3: 16 GiB, E4: 32 GiB, E6: 64 GiB, E10: 128 GiB, E15: 256 GiB, E20: 512 GiB, E30: 1024 GiB, E40: 2048 GiB, ...

- **`Disks`** (number) — section: *Managed Disks* (opened automatically)

- **`Transaction units (10,000 transactions)`** (number) — section: *Storage transactions* (opened automatically)

- **`Data Transfer Type`** (select) — section: *Bandwidth* (opened automatically)
  - options: Inter Region, Internet Egress

- **`Source Region`** (select) — section: *Bandwidth* (opened automatically)
  - options (59): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Destination Region`** (select) — section: *Bandwidth* (opened automatically)
  - depends on: `dataTransferType`
  - disappears when: `dataTransferType` = *Internet Egress*
  - options (58): Central US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, Sweden Central, ...

- **`GB`** (number) — section: *Bandwidth* (opened automatically)
  - depends on: `dataTransferType`

- **`License`** (select)
  - depends on: `type`
  - only exists when: `type` = *BizTalk*, `type` = *SQL Server*
  - options: BizTalk Enterprise, BizTalk Standard

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Redundancy`** (select)
  - depends on: `managedDiskTier`
  - only exists when: `managedDiskTier` = *Standard SSD*
  - options: LRS, ZRS

- **`Routed Via`** (select)
  - depends on: `dataTransferType`
  - only exists when: `dataTransferType` = *Internet Egress*
  - options: Microsoft Global Network, Public Internet

- **`computeBillingOption`** (radio)
  - depends on: `type`
  - disappears when: `type` = *BizTalk*, `type` = *SQL Server*
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~31% discount)), `sv-three-year` (3 year savings plan (~53% discount)), `one-year` (1 year reserved (~40% discount)), `three-year` (3 year reserved (~62% discount))

- **`osBillingOption`** (radio)
  - depends on: `operatingSystem`, `type`
  - disappears when: `operatingSystem` = *Linux*, `type` = *BizTalk*, `type` = *SQL Server*
  - choices: `payg` (License included), `ahb` (Azure Hybrid Benefit)

## Example component

```json
{
  "product": "Virtual Machines",
  "name": "my-virtual-machines",
  "fields": {
    "Region": "Central US",
    "Operating system": "Linux",
    "Type": "(OS Only)",
    "Tier": "Basic",
    "Category": "All"
  }
}
```
