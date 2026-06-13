# Virtual Machines

- slug: `virtual-machines`  |  module: `virtual-machines-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Operating system`** (select)
  - options: Linux, Windows

- **`Type`** (select)
  - depends on: `operatingSystem`, `type`, `tier`, `category`
  - options: (OS Only), BizTalk, SQL Server
  - when `operatingSystem` = *Linux*: Red Hat Enterprise Linux, Red Hat Enterprise Linux with HA, RHEL for SAP Business Applications, RHEL for SAP with HA, SQL Server Red Hat Enterprise Linux, SQL Server SUSE Priority, SQL Server Ubuntu Linux, SQL Server Ubuntu Pro, SUSE Linux Enterprise, SUSE Linux Enterprise for HPC, ...

- **`Tier`** (select)
  - options: Basic, Standard

- **`Category`** (select)
  - depends on: `tier`, `operatingSystem`, `type`, `category`
  - options: All, Compute optimized, General purpose, GPU, High performance compute, Memory optimized, Storage optimized
  - when `tier` = *Basic*: All, General purpose

- **`Instance Series`** (select)
  - depends on: `operatingSystem`, `tier`, `category`, `type`
  - options (144): All, A-series, Av2 Standard, Basv2-series, Bs-series, Bsv2-series, Constrained vCPUs capable, Da v4-series, Dadsv5-series, Dadsv6-series, Dadsv7-series, Daldsv6-series, Daldsv7-series, Dalsv6-series, Dalsv7-series, ...
  - when `operatingSystem` = *Linux*: All, A-series, Av2 Standard, Basv2-series, Bpsv2-series, Bs-series, Bsv2-series, Constrained vCPUs capable, Da v4-series, Dadsv5-series, ...
  - when `tier` = *Basic*: All, A-series
  - when `category` = *Compute optimized*: All, Fadsv7-series, Faldsv7-series, Falsv6-series, Falsv7-series, Famdsv7-series, Famsv6-series, Famsv7-series, Fasv6-series, Fasv7-series, ...
  - when `category` = *General purpose*: All, A-series, Av2 Standard, Basv2-series, Bs-series, Bsv2-series, Da v4-series, Dadsv5-series, Dadsv6-series, Dadsv7-series, ...
  - when `category` = *GPU*: All, NC A100 v4-series, NC_T4_v3-series, NCads A10 v4-series, NCads H100 v5-series, NCdsxlRTX6Kv6-series, NCldsxlRTX6Kv6-series, NC-series, NCsv2-series, NCsv3-series, ...
  - when `category` = *High performance compute*: All, Constrained vCPUs capable, HB-series, HBv2-series, HBv3-series, HBv4-series, HBv5-series, HC-series, H-series, HX-series

- **`Instance: (Need help finding the right VM?)`** (text)

- **`Virtual machines`** (number)

- **`Hours`** (number)
  - depends on: `hoursFactor`, `managedDiskTier`, `operatingSystem`, `type`, `category`
  - only exists when: `hoursFactor` = *Hours* and `operatingSystem` = *Linux*, `hoursFactor` = *Hours* and `type` = *SQL Server*, `hoursFactor` = *Hours* and `category` = *Compute optimized*, `hoursFactor` = *Hours* and `category` = *GPU*, `hoursFactor` = *Hours* and `category` = *Memory optimized*
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `hoursFactor`, `managedDiskTier`, `operatingSystem`, `type`, `category`
  - only exists when: `hoursFactor` = *Hours* and `operatingSystem` = *Linux*, `hoursFactor` = *Hours* and `type` = *SQL Server*, `hoursFactor` = *Hours* and `category` = *Compute optimized*, `hoursFactor` = *Hours* and `category` = *GPU*, `hoursFactor` = *Hours* and `category` = *Memory optimized*
  - disappears when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`managedDiskTier`** (select) — section: *Managed Disks* (opened automatically)
  - depends on: `category`, `operatingSystem`, `tier`, `type`
  - options: Standard HDD, Standard SSD
  - when `category` = *Compute optimized*: Standard HDD, Standard SSD, Premium SSD, Premium SSD v2
  - when `category` = *GPU*: Standard HDD, Standard SSD, Premium SSD, Premium SSD v2
  - when `category` = *High performance compute*: Standard HDD, Standard SSD, Premium SSD, Premium SSD v2
  - when `category` = *Memory optimized*: Standard HDD, Standard SSD, Premium SSD, Premium SSD v2
  - when `category` = *Storage optimized*: Standard HDD, Standard SSD, Premium SSD, Premium SSD v2

- **`Disk size`** (select) — section: *Managed Disks* (opened automatically)
  - depends on: `managedDiskTier`, `operatingSystem`, `type`, `tier`, `category`
  - disappears when: `managedDiskTier` = *Premium SSD v2*
  - options: S4: 32 GiB, S6: 64 GiB, S10: 128 GiB, S15: 256 GiB, S20: 512 GiB, S30: 1024 GiB, S40: 2048 GiB, S50: 4096 GiB, S60: 8192 GiB, S70: 16384 GiB, S80: 32767 GiB
  - when `managedDiskTier` = *Standard SSD*: E1: 4 GiB, E2: 8 GiB, E3: 16 GiB, E4: 32 GiB, E6: 64 GiB, E10: 128 GiB, E15: 256 GiB, E20: 512 GiB, E30: 1024 GiB, E40: 2048 GiB, ...
  - when `managedDiskTier` = *Premium SSD*: P1: 4 GiB, 120 IOPS, 25 MB/sec, P2: 8 GiB, 120 IOPS, 25 MB/sec, P3: 16 GiB, 120 IOPS, 25 MB/sec, P4: 32 GiB, 120 IOPS, 25 MB/sec, P6: 64 GiB, 240 IOPS, 50 MB/sec, P10: 128 GiB, 500 IOPS, 100 MB/sec, P15: 256 GiB, 1100 IOPS, 125 MB/sec, P20: 512 GiB, 2300 IOPS, 150 MB/sec, P30: 1024 GiB, 5000 IOPS, 200 MB/sec, P40: 2048 GiB, 7500 IOPS, 250 MB/sec, ...

- **`Disks`** (number) — section: *Managed Disks* (opened automatically)
  - depends on: `managedDiskTier`, `operatingSystem`, `type`
  - disappears when: `managedDiskTier` = *Premium SSD v2*

- **`Transaction units (10,000 transactions)`** (number) — section: *Storage transactions* (opened automatically)
  - depends on: `managedDiskTier`
  - disappears when: `managedDiskTier` = *Premium SSD*, `managedDiskTier` = *Premium SSD v2*

- **`Data Transfer Type`** (select) — section: *Bandwidth* (opened automatically)
  - options: Inter Region, Internet Egress

- **`Source Region`** (select) — section: *Bandwidth* (opened automatically)
  - options (59): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Destination Region`** (select) — section: *Bandwidth* (opened automatically)
  - depends on: `dataTransferType`, `operatingSystem`, `type`, `tier`, `category`
  - disappears when: `dataTransferType` = *Internet Egress*
  - options (58): Central US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, Sweden Central, ...

- **`GB`** (number) — section: *Bandwidth* (opened automatically)
  - depends on: `dataTransferType`, `operatingSystem`, `type`, `tier`, `category`

- **`License`** (select)
  - depends on: `type`, `operatingSystem`, `tier`, `category`
  - only exists when: `type` = *BizTalk*, `type` = *SQL Server*, `type` = *SQL Server Red Hat Enterprise Linux* and `operatingSystem` = *Linux*, `type` = *SQL Server SUSE Priority* and `operatingSystem` = *Linux*, `type` = *SQL Server Ubuntu Linux* and `operatingSystem` = *Linux*, `type` = *SQL Server Ubuntu Pro* and `operatingSystem` = *Linux*
  - disappears when: `operatingSystem` = *Linux* and `type` = *BizTalk*, `operatingSystem` = *Linux* and `type` = *SQL Server*
  - options: BizTalk Enterprise, BizTalk Standard
  - when `type` = *SQL Server*: SQL Enterprise, SQL Standard, SQL Web
  - when `type` = *SQL Server Red Hat Enterprise Linux* and `operatingSystem` = *Linux*: SQL Server Enterprise Red Hat Enterprise Linux, SQL Server Standard Red Hat Enterprise Linux, SQL Server Web Red Hat Enterprise Linux
  - when `type` = *SQL Server SUSE Priority* and `operatingSystem` = *Linux*: SQL Server Enterprise SUSE Priority, SQL Server Standard SUSE Priority, SQL Server Web SUSE Priority
  - when `type` = *SQL Server Ubuntu Linux* and `operatingSystem` = *Linux*: SQL Server Enterprise Ubuntu Linux, SQL Server Standard Ubuntu Linux, SQL Server Web Ubuntu Linux
  - when `type` = *SQL Server Ubuntu Pro* and `operatingSystem` = *Linux*: SQL Server Developer Ubuntu Pro, SQL Server Enterprise Ubuntu Pro, SQL Server Standard Ubuntu Pro, SQL Server Web Ubuntu Pro
  - when `type` = *SUSE Linux Enterprise* and `operatingSystem` = *Linux*: SUSE Linux Enterprise + Patching only, SUSE Linux Enterprise + 24x7 Support

- **`Days`** (number)
  - depends on: `hoursFactor`, `operatingSystem`, `type`, `tier`, `category`
  - only exists when: `hoursFactor` = *Days*
  - disappears when: `hoursFactor` = *Hours* and `operatingSystem` = *Linux*, `hoursFactor` = *Hours* and `type` = *SQL Server*, `hoursFactor` = *Hours* and `category` = *Compute optimized*, `hoursFactor` = *Hours* and `category` = *GPU*, `hoursFactor` = *Hours* and `category` = *Memory optimized*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`, `operatingSystem`, `type`, `tier`, `category`
  - only exists when: `hoursFactor` = *Days*
  - disappears when: `hoursFactor` = *Hours* and `operatingSystem` = *Linux*, `hoursFactor` = *Hours* and `type` = *SQL Server*, `hoursFactor` = *Hours* and `category` = *Compute optimized*, `hoursFactor` = *Hours* and `category` = *GPU*, `hoursFactor` = *Hours* and `category` = *Memory optimized*
  - options: Hours, Days, Month

- **`Redundancy`** (select)
  - depends on: `managedDiskTier`, `operatingSystem`, `type`, `tier`, `category`
  - only exists when: `managedDiskTier` = *Standard SSD*, `managedDiskTier` = *Premium SSD*
  - options: LRS, ZRS

- **`Disk Size (GiB)`** (number)
  - depends on: `managedDiskTier`, `operatingSystem`, `type`
  - only exists when: `managedDiskTier` = *Premium SSD v2*

- **`Number of disks`** (number)
  - depends on: `managedDiskTier`, `operatingSystem`, `type`
  - only exists when: `managedDiskTier` = *Premium SSD v2*

- **`Number of IOPS`** (number)
  - depends on: `managedDiskTier`, `operatingSystem`, `type`
  - only exists when: `managedDiskTier` = *Premium SSD v2*

- **`MB/s`** (number)
  - depends on: `managedDiskTier`, `operatingSystem`, `type`
  - only exists when: `managedDiskTier` = *Premium SSD v2*

- **`Routed Via`** (select)
  - depends on: `dataTransferType`, `operatingSystem`, `type`, `tier`, `category`
  - only exists when: `dataTransferType` = *Internet Egress*
  - options: Microsoft Global Network, Public Internet

- **`storageV2Hours`** (number)
  - depends on: `operatingSystem`, `managedDiskTier`, `type`
  - only exists when: `managedDiskTier` = *Premium SSD v2* and `operatingSystem` = *Linux*, `managedDiskTier` = *Premium SSD v2* and `type` = *BizTalk*, `managedDiskTier` = *Premium SSD v2* and `type` = *SQL Server*

- **`storageV2HoursFactor`** (select)
  - depends on: `operatingSystem`, `managedDiskTier`, `type`
  - only exists when: `managedDiskTier` = *Premium SSD v2* and `operatingSystem` = *Linux*, `managedDiskTier` = *Premium SSD v2* and `type` = *BizTalk*, `managedDiskTier` = *Premium SSD v2* and `type` = *SQL Server*
  - options: Hours, Days, Month

- **`computeBillingOption`** (radio)
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~31% discount)), `sv-three-year` (3 year savings plan (~53% discount)), `one-year` (1 year reserved (~40% discount)), `three-year` (3 year reserved (~62% discount))

- **`osBillingOption`** (radio)
  - depends on: `operatingSystem`, `type`, `tier`, `category`
  - disappears when: `operatingSystem` = *Linux*
  - choices: `payg` (License included), `ahb` (Azure Hybrid Benefit)

- **`softwareBillingOption`** (radio)
  - depends on: `type`, `operatingSystem`, `tier`, `category`
  - only exists when: `type` = *BizTalk*, `type` = *Red Hat Enterprise Linux* and `operatingSystem` = *Linux*, `type` = *Red Hat Enterprise Linux with HA* and `operatingSystem` = *Linux*, `type` = *RHEL for SAP Business Applications* and `operatingSystem` = *Linux*, `type` = *RHEL for SAP with HA* and `operatingSystem` = *Linux*, `type` = *SQL Server Red Hat Enterprise Linux* and `operatingSystem` = *Linux*
  - disappears when: `operatingSystem` = *Linux* and `type` = *BizTalk*
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved), `three-year` (3 year reserved)

- **`sqlSoftwareBillingOption`** (radio)
  - depends on: `type`, `operatingSystem`, `tier`, `category`
  - only exists when: `type` = *SQL Server*
  - disappears when: `operatingSystem` = *Linux* and `type` = *SQL Server*
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
