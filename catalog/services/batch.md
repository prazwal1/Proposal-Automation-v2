# Batch

- slug: `batch`  |  module: `batch-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Standard

- **`Category`** (select)
  - options: All, Compute optimized, General purpose, High performance compute, Memory optimized

- **`Instance Series`** (select)
  - depends on: `cloudServicesCategory`
  - options: All, A-series, Av2 Standard, D-series, Dv2-series, Dv3-series, Ev3-series, Fsv2-series, G-series, H-series
  - when `cloudServicesCategory` = *Compute optimized*: All, Fsv2-series
  - when `cloudServicesCategory` = *General purpose*: All, A-series, Av2 Standard, D-series, Dv2-series, Dv3-series
  - when `cloudServicesCategory` = *High performance compute*: All, H-series
  - when `cloudServicesCategory` = *Memory optimized*: All, D-series, Dv2-series, Ev3-series, G-series

- **`Instance: (Need help finding the right VM?)`** (text)

- **`Instances`** (number)

- **`Hours`** (number)
  - depends on: `cloudServicesHoursFactor`
  - disappears when: `cloudServicesHoursFactor` = *Days*

- **`cloudServicesHoursFactor`** (select)
  - depends on: `cloudServicesHoursFactor`
  - disappears when: `cloudServicesHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`virtualMachinesTier`** (select)
  - options: Standard

- **`Operating system`** (select)
  - options: Linux, Windows

- **`virtualMachinesCategory`** (select)
  - options: All, Compute optimized, General purpose, GPU, High performance compute, Memory optimized, Storage optimized

- **`virtualMachinesInstanceSeries`** (select)
  - depends on: `virtualMachinesOperatingSystem`, `virtualMachinesCategory`
  - options (143): All, A-series, Av2 Standard, Basv2-series, Bs-series, Bsv2-series, Constrained vCPUs capable, Da v4-series, Dadsv5-series, Dadsv6-series, Dadsv7-series, Daldsv6-series, Daldsv7-series, Dalsv6-series, Dalsv7-series, ...
  - when `virtualMachinesOperatingSystem` = *Linux*: All, A-series, Av2 Standard, Basv2-series, Bpsv2-series, Bs-series, Bsv2-series, Constrained vCPUs capable, Da v4-series, Dadsv5-series, ...
  - when `virtualMachinesCategory` = *Compute optimized*: All, Fadsv7-series, Faldsv7-series, Falsv6-series, Falsv7-series, Famdsv7-series, Famsv6-series, Famsv7-series, Fasv6-series, Fasv7-series, ...
  - when `virtualMachinesCategory` = *General purpose*: All, A-series, Av2 Standard, Basv2-series, Bs-series, Bsv2-series, Da v4-series, Dadsv5-series, Dadsv6-series, Dadsv7-series, ...
  - when `virtualMachinesCategory` = *GPU*: All, NC A100 v4-series, NC_T4_v3-series, NCads A10 v4-series, NCads H100 v5-series, NCdsxlRTX6Kv6-series, NCldsxlRTX6Kv6-series, NC-series, NCsv2-series, NCsv3-series, ...
  - when `virtualMachinesCategory` = *High performance compute*: All, Constrained vCPUs capable, HB-series, HBv2-series, HBv3-series, HBv4-series, HC-series, H-series, HX-series
  - when `virtualMachinesCategory` = *Memory optimized*: All, Constrained vCPUs capable, D-series, DS-series, Dsv2-series, Dv2-series, Ea v4-series, Eadsv5-series, Eadsv6-series, Eadsv7-series, ...

- **`virtualMachinesSize`** (text)

- **`virtualMachinesInstances`** (number)

- **`virtualMachinesHours`** (number)
  - depends on: `virtualMachinesHoursFactor`
  - disappears when: `virtualMachinesHoursFactor` = *Days*

- **`virtualMachinesHoursFactor`** (select)
  - depends on: `virtualMachinesHoursFactor`
  - disappears when: `virtualMachinesHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `cloudServicesHoursFactor`
  - only exists when: `cloudServicesHoursFactor` = *Days*

- **`Days (cloudServicesHoursFactor)`** (select)
  - depends on: `cloudServicesHoursFactor`
  - only exists when: `cloudServicesHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (virtualMachinesHours)`** (number)
  - depends on: `virtualMachinesHoursFactor`
  - only exists when: `virtualMachinesHoursFactor` = *Days*

- **`Days (virtualMachinesHoursFactor)`** (select)
  - depends on: `virtualMachinesHoursFactor`
  - only exists when: `virtualMachinesHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`billingOption`** (radio)
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~31% discount)), `sv-three-year` (3 year savings plan (~53% discount)), `one-year` (1 year reserved (~31% discount)), `three-year` (3 year reserved (~0% discount))

- **`osBillingOption`** (radio)
  - depends on: `virtualMachinesOperatingSystem`
  - disappears when: `virtualMachinesOperatingSystem` = *Linux*
  - choices: `payg` (License included), `ahb` (Azure Hybrid Benefit)

## Example component

```json
{
  "product": "Batch",
  "name": "my-batch",
  "fields": {
    "Region": "Central US",
    "Tier": "Standard",
    "Category": "All",
    "Instance Series": "All",
    "Instances": 1
  }
}
```
