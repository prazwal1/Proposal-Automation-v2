# Service Fabric

- slug: `service-fabric`  |  module: `service-fabric-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Deployment Option`** (select)
  - options: Service Fabric Mesh (Preview), Service Fabric Cluster

- **`Type`** (select)
  - options: Linux, Windows

- **`Category`** (select)
  - depends on: `deploymentOption`
  - disappears when: `deploymentOption` = *Service Fabric Mesh (Preview)*
  - options: All, Compute optimized, General purpose, GPU, High performance compute, Memory optimized, Storage optimized

- **`Instance Series`** (select)
  - depends on: `deploymentOption`, `type`, `scaleSet1Category`
  - disappears when: `deploymentOption` = *Service Fabric Mesh (Preview)*
  - options (143): All, A-series, Av2 Standard, Basv2-series, Bs-series, Bsv2-series, Constrained vCPUs capable, Da v4-series, Dadsv5-series, Dadsv6-series, Dadsv7-series, Daldsv6-series, Daldsv7-series, Dalsv6-series, Dalsv7-series, ...
  - when `type` = *Linux*: All, A-series, Av2 Standard, Basv2-series, Bpsv2-series, Bs-series, Bsv2-series, Constrained vCPUs capable, Da v4-series, Dadsv5-series, ...
  - when `scaleSet1Category` = *Compute optimized*: All, Fadsv7-series, Faldsv7-series, Falsv6-series, Falsv7-series, Famdsv7-series, Famsv6-series, Famsv7-series, Fasv6-series, Fasv7-series, ...
  - when `scaleSet1Category` = *General purpose*: All, A-series, Av2 Standard, Basv2-series, Bs-series, Bsv2-series, Da v4-series, Dadsv5-series, Dadsv6-series, Dadsv7-series, ...
  - when `scaleSet1Category` = *GPU*: All, NC A100 v4-series, NC_T4_v3-series, NCads A10 v4-series, NCads H100 v5-series, NCdsxlRTX6Kv6-series, NCldsxlRTX6Kv6-series, NC-series, NCsv2-series, NCsv3-series, ...
  - when `scaleSet1Category` = *High performance compute*: All, Constrained vCPUs capable, HB-series, HBv2-series, HBv3-series, HBv4-series, HC-series, H-series, HX-series
  - when `scaleSet1Category` = *Memory optimized*: All, Constrained vCPUs capable, D-series, DS-series, Dsv2-series, Dv2-series, Ea v4-series, Eadsv5-series, Eadsv6-series, Eadsv7-series, ...

- **`Instance: (Need help finding the right VM?)`** (text)
  - depends on: `deploymentOption`
  - disappears when: `deploymentOption` = *Service Fabric Mesh (Preview)*

- **`Virtual machines`** (number)
  - depends on: `deploymentOption`
  - disappears when: `deploymentOption` = *Service Fabric Mesh (Preview)*

- **`Hours`** (number)
  - depends on: `deploymentOption`

- **`scaleSet1HoursFactor`** (select)
  - depends on: `deploymentOption`
  - options: Hours, Days, Month

- **`Data redundancy`** (select)
  - depends on: `deploymentOption`
  - disappears when: `deploymentOption` = *Service Fabric Mesh (Preview)*
  - options: LRS, GRS, RA-GRS

- **`GB`** (number)
  - depends on: `deploymentOption`

- **`storageLogUnits`** (select)
  - depends on: `deploymentOption`
  - options: GB, TB

- **`Addresses`** (number)
  - depends on: `deploymentOption`
  - disappears when: `deploymentOption` = *Service Fabric Mesh (Preview)*

- **`clusterHours`** (number)
  - depends on: `deploymentOption`, `clusterHoursFactor`
  - disappears when: `deploymentOption` = *Service Fabric Mesh (Preview)*, `clusterHoursFactor` = *Days*

- **`clusterHoursFactor`** (select)
  - depends on: `deploymentOption`, `clusterHoursFactor`
  - disappears when: `deploymentOption` = *Service Fabric Mesh (Preview)*, `clusterHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`containerInstances`** (number)
  - depends on: `deploymentOption`
  - only exists when: `deploymentOption` = *Service Fabric Mesh (Preview)*

- **`Seconds`** (number)
  - depends on: `deploymentOption`
  - only exists when: `deploymentOption` = *Service Fabric Mesh (Preview)*

- **`Container memory`** (select)
  - depends on: `deploymentOption`
  - only exists when: `deploymentOption` = *Service Fabric Mesh (Preview)*
  - options: 1 GB, 2 GB, 3 GB, 4 GB, 5 GB, 6 GB, 7 GB, 8 GB

- **`Container cores`** (select)
  - depends on: `deploymentOption`
  - only exists when: `deploymentOption` = *Service Fabric Mesh (Preview)*
  - options: 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4

- **`Instances`** (number)
  - depends on: `deploymentOption`
  - only exists when: `deploymentOption` = *Service Fabric Mesh (Preview)*

- **`Number of disks`** (number)
  - depends on: `deploymentOption`
  - only exists when: `deploymentOption` = *Service Fabric Mesh (Preview)*

- **`reliableInstances`** (number)
  - depends on: `deploymentOption`
  - only exists when: `deploymentOption` = *Service Fabric Mesh (Preview)*

- **`IOPS`** (number)
  - depends on: `deploymentOption`
  - only exists when: `deploymentOption` = *Service Fabric Mesh (Preview)*

- **`Days`** (number)
  - depends on: `scaleSet1HoursFactor`
  - only exists when: `scaleSet1HoursFactor` = *Days*

- **`Days (scaleSet1HoursFactor)`** (select)
  - depends on: `scaleSet1HoursFactor`
  - only exists when: `scaleSet1HoursFactor` = *Days*
  - options: Hours, Days, Month

- **`TB`** (number)
  - depends on: `storageLogUnits`
  - only exists when: `storageLogUnits` = *TB*

- **`TB (storageLogUnits)`** (select)
  - depends on: `storageLogUnits`
  - only exists when: `storageLogUnits` = *TB*
  - options: GB, TB

- **`Days (clusterHours)`** (number)
  - depends on: `clusterHoursFactor`
  - only exists when: `clusterHoursFactor` = *Days*

- **`Days (clusterHoursFactor)`** (select)
  - depends on: `clusterHoursFactor`
  - only exists when: `clusterHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`scaleSet1ComputeBillingOption`** (radio)
  - depends on: `deploymentOption`
  - disappears when: `deploymentOption` = *Service Fabric Mesh (Preview)*
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~62% discount)), `sv-three-year` (3 year savings plan (~74% discount)), `one-year` (1 year reserved (~62% discount)), `three-year` (3 year reserved (~0% discount))

- **`scaleSet1OsBillingOption`** (radio)
  - depends on: `deploymentOption`, `type`
  - disappears when: `deploymentOption` = *Service Fabric Mesh (Preview)*, `type` = *Linux*
  - choices: `payg` (Pay as you go), `ahb` (Azure Hybrid Benefit)

## Example component

```json
{
  "product": "Service Fabric",
  "name": "my-service-fabric",
  "fields": {
    "Region": "Central US",
    "Deployment Option": "Service Fabric Mesh (Preview)",
    "Type": "Linux",
    "Category": "All",
    "Instance Series": "All"
  }
}
```
