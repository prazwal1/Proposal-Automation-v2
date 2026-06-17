# Kubernetes Service

- slug: `kubernetes-service`  |  module: `kubernetes-service-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Standard, Automatic

- **`Options`** (select)
  - depends on: `kubernetesServiceOfferTier`
  - disappears when: `kubernetesServiceOfferTier` = *Automatic*
  - options: No SLA (free, non-production), SLA, SLA and Long Term Support

- **`Clusters`** (number)

- **`Operating system`** (select)
  - options: Linux, Windows

- **`Category`** (select)
  - depends on: `kubernetesServiceOfferTier`
  - options: All, Compute optimized, General purpose, GPU, High performance compute, Memory optimized, Storage optimized
  - when `kubernetesServiceOfferTier` = *Automatic*: Compute optimized, General purpose, GPU, High performance compute, Memory optimized, Storage optimized

- **`Instance Series`** (select)
  - depends on: `kubernetesServiceOfferTier`, `operatingSystem`, `category`
  - options (72): All, A-series, Av2 Standard, Basv2-series, Bpsv2-series, Bs-series, Bsv2-series, Constrained vCPUs capable, Da v4-series, Dadsv5-series, Das v4-series, Dasv5-series, DCadsv5-series, DCasv5-series, DCdsv3-series, ...
  - when `kubernetesServiceOfferTier` = *Automatic*: All, A-series, Av2 Standard, Basv2-series, Bpsv2-series, Bs-series, Bsv2-series, Da v4-series, Dadsv5-series, Das v4-series, Dasv5-series, DCadsv5-series, DCasv5-series, DCdsv3-series, DCsv2-series, DCsv3-series, Dd v4-series, Dds v4-series, Ddsv5-series, Ddv5-series, Dldsv5-series, Dplsv5-Series, Dpsv5-Series, D-series, ...
  - when `operatingSystem` = *Windows*: All, A-series, Av2 Standard, Basv2-series, Bs-series, Bsv2-series, Da v4-series, Dadsv5-series, Das v4-series, Dasv5-series, DCadsv5-series, DCasv5-series, DCdsv3-series, DCsv2-series, DCsv3-series, Dd v4-series, Dds v4-series, Ddsv5-series, Ddv5-series, Dldsv5-series, D-series, DS-series, Dsv2-series, Dsv3-series, ...
  - when `category` = *Compute optimized*: All, F-series, Fs-series, Fsv2-series
  - when `category` = *GPU*: All, NC_T4_v3-series, NCsv3-series, NVv3-series
  - when `category` = *High performance compute*: All, H-series
  - when `category` = *Memory optimized*: All, Constrained vCPUs capable, D-series, DS-series, Dsv2-series, Dv2-series, Ea v4-series, Eadsv5-series, Eas v4-series, Easv5-series, Ebdsv5-series, Ebsv5-series, Ed v4-series, Eds v4-series, Edsv5-series, Edv5-series, Epsv5-Series, Esv3-series, Esv4-series, Esv5-series, Ev3-series, Ev4-series, Ev5-series, G-series, ...

- **`Instance: (Need help finding the right VM?)`** (text)

- **`Virtual Machines`** (number)

- **`Hours`** (number)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`managedDiskTier`** (select)
  - depends on: `category`
  - options: Standard HDD, Standard SSD
  - when `category` = *GPU*: Standard HDD, Standard SSD, Premium SSD
  - when `category` = *Memory optimized*: Standard HDD, Standard SSD, Premium SSD
  - when `category` = *Storage optimized*: Standard HDD, Standard SSD, Premium SSD

- **`Disk size`** (select)
  - depends on: `managedDiskTier`
  - options: S4 - 32 GB, S6 - 64 GB, S10 - 128 GB, S15 - 256 GB, S20 - 512 GB, S30 - 1024 GB, S40 - 2048 GB, S50 - 4096 GB, S60 - 8192 GB, S70 - 16384 GB, S80 - 32767 GB
  - when `managedDiskTier` = *Standard SSD*: E1 - 4 GB, E2 - 8 GB, E3 - 16 GB, E4 - 32 GB, E6 - 64 GB, E10 - 128 GB, E15 - 256 GB, E20 - 512 GB, E30 - 1024 GB, E40 - 2048 GB, E50 - 4096 GB, E60 - 8192 GB, E70 - 16384 GB, E80 - 32767 GB

- **`Disks`** (number)

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`computeBillingOption`** (radio)
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~31% discount)), `sv-three-year` (3 year savings plan (~53% discount)), `one-year` (1 year reserved (~32% discount)), `three-year` (3 year reserved (~57% discount))

- **`osBillingOption`** (radio)
  - depends on: `operatingSystem`
  - only exists when: `operatingSystem` = *Windows*
  - choices: `payg` (License included), `ahb` (Azure Hybrid Benefit)

## Example component

```json
{
  "product": "Kubernetes Service",
  "name": "my-kubernetes-service",
  "fields": {
    "Region": "Central US",
    "Tier": "Standard",
    "Options": "No SLA (free, non-production)",
    "Clusters": 1,
    "Operating system": "Linux"
  }
}
```
