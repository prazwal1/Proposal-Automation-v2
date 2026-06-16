# Virtual Machine Scale Sets

- slug: `virtual-machine-scale-sets`  |  module: `virtual-machine-scale-sets-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Operating System`** (select)
  - options: Linux, Windows

- **`Type`** (select)
  - depends on: `operatingSystem`
  - options: (OS Only), BizTalk, SQL Server
  - when `operatingSystem` = *Linux*: Red Hat Enterprise Linux, Red Hat Enterprise Linux with HA, RHEL for SAP Business Applications, RHEL for SAP with HA, SQL Server Red Hat Enterprise Linux, SQL Server SUSE Priority, SQL Server Ubuntu Linux, SQL Server Ubuntu Pro, SUSE Linux Enterprise, SUSE Linux Enterprise for HPC, SUSE Linux Enterprise for SAP Applications + 24x7 Support, Ubuntu, Ubuntu Advantage, Ubuntu Pro

- **`Tier`** (select)
  - options: Basic, Standard

- **`Category`** (select)
  - depends on: `tier`
  - options: All, Compute optimized, General purpose, GPU, High performance compute, Memory optimized, Storage optimized
  - when `tier` = *Basic*: All, General purpose

- **`Instance Series`** (select)
  - depends on: `operatingSystem`, `type`, `tier`, `category`
  - options (134): All, A-series, Av2 Standard, Basv2-series, Bs-series, Bsv2-series, Constrained vCPUs capable, Da v4-series, Dadsv5-series, Dadsv6-series, Dadsv7-series, Daldsv6-series, Daldsv7-series, Dalsv6-series, Dalsv7-series, ...
  - when `operatingSystem` = *Linux*: All, A-series, Av2 Standard, Basv2-series, Bpsv2-series, Bs-series, Bsv2-series, Constrained vCPUs capable, Da v4-series, Dadsv5-series, Dadsv6-series, Dadsv7-series, Daldsv6-series, Daldsv7-series, Dalsv6-series, Dalsv7-series, Das v4-series, Dasv5-series, Dasv6-series, Dasv7-series, DCadsv5-series, DCadsv6-series, DCasv5-series, DCasv6-series, ...
  - when `type` = *BizTalk*: All, A-series, Av2 Standard, Basv2-series, Bs-series, Bsv2-series, Constrained vCPUs capable, Da v4-series, Dadsv5-series, Dadsv6-series, Dadsv7-series, Daldsv6-series, Daldsv7-series, Dalsv6-series, Dalsv7-series, Das v4-series, Dasv5-series, Dasv6-series, Dasv7-series, DCadsv5-series, DCadsv6-series, DCasv5-series, DCasv6-series, DCdsv3-series, ...
  - when `type` = *SQL Server*: All, A-series, Av2 Standard, Basv2-series, Bs-series, Bsv2-series, Constrained vCPUs capable, Da v4-series, Dadsv5-series, Dadsv6-series, Dadsv7-series, Daldsv6-series, Daldsv7-series, Dalsv6-series, Dalsv7-series, Das v4-series, Dasv5-series, Dasv6-series, Dasv7-series, DCadsv5-series, DCadsv6-series, DCasv5-series, DCasv6-series, DCdsv3-series, ...
  - when `tier` = *Basic*: All, A-series
  - when `category` = *Compute optimized*: All, Fadsv7-series, Faldsv7-series, Falsv6-series, Falsv7-series, Famdsv7-series, Famsv6-series, Famsv7-series, Fasv6-series, Fasv7-series, F-series, Fs-series, Fsv2-series, FXmdsv2-series, FXmsv2-series
  - when `category` = *General purpose*: All, A-series, Av2 Standard, Basv2-series, Bs-series, Bsv2-series, Da v4-series, Dadsv5-series, Dadsv6-series, Dadsv7-series, Daldsv6-series, Daldsv7-series, Dalsv6-series, Dalsv7-series, Das v4-series, Dasv5-series, Dasv6-series, Dasv7-series, DCadsv5-series, DCadsv6-series, DCasv5-series, DCasv6-series, DCdsv3-series, DCedsv6-series, ...

- **`Instance: (Need help finding the right VM?)`** (text)

- **`Virtual Machines`** (number)

- **`Hours`** (number)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

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

- **`computeBillingOption`** (radio)
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~31% discount)), `sv-three-year` (3 year savings plan (~53% discount)), `one-year` (1 year reserved (~31% discount)), `three-year` (3 year reserved)

- **`osBillingOption`** (radio)
  - depends on: `operatingSystem`
  - disappears when: `operatingSystem` = *Linux*
  - choices: `payg` (License included), `ahb` (Azure Hybrid Benefit)

- **`softwareBillingOption`** (radio)
  - depends on: `type`
  - only exists when: `type` = *BizTalk*
  - choices: `payg` (Pay as you go)

- **`sqlSoftwareBillingOption`** (radio)
  - depends on: `type`
  - only exists when: `type` = *SQL Server*
  - choices: `payg` (License included), `ahb` (Azure Hybrid Benefit)

## Example component

```json
{
  "product": "Virtual Machine Scale Sets",
  "name": "my-virtual-machine-scale-sets",
  "fields": {
    "Region": "Central US",
    "Operating System": "Linux",
    "Type": "(OS Only)",
    "Tier": "Basic",
    "Category": "All"
  }
}
```
