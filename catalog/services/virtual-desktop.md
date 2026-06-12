# Virtual Desktop

- slug: `virtual-desktop`  |  module: `virtual-desktop-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Service`** (select)
  - options: Azure Virtual Desktop, Azure Virtual Desktop for Azure Stack HCI

- **`Virtual Desktop Type`** (select)
  - depends on: `serviceType`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*
  - options: Pooled, Personal

- **`Session`** (select)
  - depends on: `serviceType`, `type`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*, `type` = *Personal*
  - options: Multi-session, Single-session

- **`Workload type`** (select)
  - depends on: `serviceType`, `type`, `session`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*, `type` = *Personal*, `session` = *Single-session*
  - options: Light, Medium, Heavy, Power

- **`Scaling Options`** (select)
  - depends on: `serviceType`, `type`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*, `type` = *Personal*
  - options: Scaling Plan, Constant Availability

- **`Total named users`** (number)
  - depends on: `serviceType`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*

- **`Total usage hours`** (number)
  - depends on: `serviceType`, `scalableOption`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*, `scalableOption` = *Constant Availability*

- **`Per user, per month`** (select)
  - depends on: `serviceType`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*
  - options: Not Applicable, App Hosting, Desktop App Hosting

- **`Category`** (select)
  - depends on: `serviceType`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*
  - options: All, Compute optimized, General purpose, GPU, High performance compute, Memory optimized, Storage optimized

- **`Instance Series`** (select)
  - depends on: `serviceType`, `category`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*
  - options (141): All, A-series, Av2 Standard, Basv2-series, Bpsv2-series, Bs-series, Bsv2-series, Constrained vCPUs capable, Da v4-series, Dadsv5-series, Dadsv6-series, Dadsv7-series, Daldsv6-series, Daldsv7-series, Dalsv6-series, ...
  - when `category` = *Compute optimized*: All, Fadsv7-series, Faldsv7-series, Falsv6-series, Falsv7-series, Famdsv7-series, Famsv6-series, Famsv7-series, Fasv6-series, Fasv7-series, ...
  - when `category` = *General purpose*: All, A-series, Av2 Standard, Basv2-series, Bpsv2-series, Bs-series, Bsv2-series, Da v4-series, Dadsv5-series, Dadsv6-series, ...
  - when `category` = *GPU*: All, NC A100 v4-series, NC_T4_v3-series, NCads H100 v5-series, NCdsxlRTX6Kv6-series, NCldsxlRTX6Kv6-series, NC-series, NCsv3-series, NDm A100 v4-series, NDsrH100v5-series, ...
  - when `category` = *High performance compute*: All, Constrained vCPUs capable, HBv4-series, HC-series, HX-series
  - when `category` = *Memory optimized*: All, Constrained vCPUs capable, D-series, DS-series, Dsv2-series, Dv2-series, Ea v4-series, Eadsv5-series, Eadsv6-series, Eadsv7-series, ...
  - when `category` = *Storage optimized*: All, Laosv4-series, Lasv3-series, Lasv4-series, Ls-series, Lsv2-series, Lsv3-series, Lsv4-series

- **`Instance: (Need help finding the right VM?)`** (text)
  - depends on: `serviceType`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*

- **`Tier`** (select)
  - depends on: `serviceType`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*
  - options: Standard HDD, Standard SSD, Premium SSD

- **`Disk size`** (select)
  - depends on: `serviceType`, `managedDiskTier`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*
  - options: P10 128 GiB 500 IOPS 100 MB/sec, P15 256 GiB 1100 IOPS 125 MB/sec, P20 512 GiB 2300 IOPS 150 MB/sec, P30 1024 GiB 5000 IOPS 200 MB/sec, P40 2048 GiB 7500 IOPS 250 MB/sec, P50 4096 GiB 7500 IOPS 250 MB/sec, P60 8192 GiB 16000 IOPS 500 MB/sec, P70 16384 GiB 18000 IOPS 750 MB/sec, P80 32767 GiB 20000 IOPS 900 MB/sec
  - when `managedDiskTier` = *Standard HDD*: S10 128 GiB, S15 256 GiB, S20 512 GiB, S30 1024 GiB, S40 2048 GiB, S50 4096 GiB, S60 8192 GiB, S70 16384 GiB, S80 32767 GiB
  - when `managedDiskTier` = *Standard SSD*: E10 128 GiB, E15 256 GiB, E20 512 GiB, E30 1024 GiB, E40 2048 GiB, E50 4096 GiB, E60 8192 GiB, E70 16384 GiB, E80 32767 GiB

- **`Type`** (select)
  - depends on: `serviceType`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*
  - options: Azure NetApp Files, Premium File Storage

- **`GB`** (number)
  - depends on: `serviceType`, `fileType`, `dataAtRestFactor`, `dataTransferType`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*, `fileType` = *Azure NetApp Files*, `dataAtRestFactor` = *TB*

- **`dataAtRestFactor`** (select)
  - depends on: `serviceType`, `fileType`, `dataAtRestFactor`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*, `fileType` = *Azure NetApp Files*, `dataAtRestFactor` = *TB*
  - options: GB, TB

- **`Data Transfer Type`** (select)
  - depends on: `serviceType`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*
  - options: Inter Region, Internet Egress

- **`Source Region`** (select)
  - depends on: `serviceType`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*
  - options (59): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Destination Region`** (select)
  - depends on: `serviceType`, `dataTransferType`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*, `dataTransferType` = *Internet Egress*
  - options (58): Central US, East US, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, Sweden Central, ...

- **`interRegionUnits`** (number)
  - depends on: `serviceType`, `dataTransferType`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*, `dataTransferType` = *Internet Egress*

- **`Amount of a core required by the OS`** (number) — section: *Customize the size of the OS* (opened automatically)
  - depends on: `serviceType`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*

- **`Total virtual cores`** (number)
  - depends on: `serviceType`
  - only exists when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*

- **`Total hours/month`** (number)
  - depends on: `serviceType`
  - only exists when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*

- **`netAppFilesTier`** (select)
  - depends on: `fileType`
  - only exists when: `fileType` = *Azure NetApp Files*
  - options: Standard Storage, Premium Storage, Ultra Storage

- **`TiB`** (number)
  - depends on: `fileType`
  - only exists when: `fileType` = *Azure NetApp Files*

- **`TB`** (number)
  - depends on: `dataAtRestFactor`
  - only exists when: `dataAtRestFactor` = *TB*

- **`TB (dataAtRestFactor)`** (select)
  - depends on: `dataAtRestFactor`
  - only exists when: `dataAtRestFactor` = *TB*
  - options: GB, TB

- **`Routed Via`** (select)
  - depends on: `dataTransferType`
  - only exists when: `dataTransferType` = *Internet Egress*
  - options: Microsoft Global Network, Public Internet

- **`computeBillingOption`** (radio)
  - depends on: `serviceType`
  - disappears when: `serviceType` = *Azure Virtual Desktop for Azure Stack HCI*
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~31% savings)), `sv-three-year` (3 year savings plan (~53% savings)), `one-year` (1 year reserved (~38% savings)), `three-year` (3 year reserved (~61% savings))

## Example component

```json
{
  "product": "Virtual Desktop",
  "name": "my-virtual-desktop",
  "fields": {
    "Region": "Central US",
    "Service": "Azure Virtual Desktop",
    "Virtual Desktop Type": "Pooled",
    "Session": "Multi-session",
    "Workload type": "Light"
  }
}
```
