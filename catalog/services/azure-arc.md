# Azure Arc

- slug: `azure-arc`  |  module: `azure-arc-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Server`** (number)

- **`Service Tier`** (select)
  - options: Standard edition, Enterprise edition

- **`vCore(s)`** (number)

- **`Hours`** (number)
  - depends on: `sqlServerOnPremVCoreHoursFactor`
  - disappears when: `sqlServerOnPremVCoreHoursFactor` = *Days*

- **`sqlServerOnPremVCoreHoursFactor`** (select)
  - depends on: `sqlServerOnPremVCoreHoursFactor`
  - disappears when: `sqlServerOnPremVCoreHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`esuServer`** (select)
  - options: Windows Server 2012, SQL Server 2012, SQL Server 2014

- **`Edition`** (select)
  - depends on: `esuServer`
  - options: Datacenter, Standard
  - when `esuServer` = *SQL Server 2012*: Enterprise, Standard
  - when `esuServer` = *SQL Server 2014*: Enterprise, Standard

- **`Physical or Virtual Cores`** (number)

- **`physicalVirtualCoreHours`** (number)
  - depends on: `physicalVirtualCoreHoursFactor`
  - disappears when: `physicalVirtualCoreHoursFactor` = *Days*

- **`physicalVirtualCoreHoursFactor`** (select)
  - depends on: `physicalVirtualCoreHoursFactor`
  - disappears when: `physicalVirtualCoreHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Instance Type`** (select)
  - options: Single Instance

- **`serviceTier`** (select)
  - options: General Purpose, Business Critical

- **`onPremVCores`** (number)

- **`onPremVCoreHours`** (number)
  - depends on: `onPremVCoreHoursFactor`
  - disappears when: `onPremVCoreHoursFactor` = *Days*

- **`onPremVCoreHoursFactor`** (select)
  - depends on: `onPremVCoreHoursFactor`
  - disappears when: `onPremVCoreHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`vCPU's in the Kubernetes Cluster`** (number)

- **`Days`** (number)
  - depends on: `sqlServerOnPremVCoreHoursFactor`
  - only exists when: `sqlServerOnPremVCoreHoursFactor` = *Days*

- **`Days (sqlServerOnPremVCoreHoursFactor)`** (select)
  - depends on: `sqlServerOnPremVCoreHoursFactor`
  - only exists when: `sqlServerOnPremVCoreHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (physicalVirtualCoreHours)`** (number)
  - depends on: `physicalVirtualCoreHoursFactor`
  - only exists when: `physicalVirtualCoreHoursFactor` = *Days*

- **`Days (physicalVirtualCoreHoursFactor)`** (select)
  - depends on: `physicalVirtualCoreHoursFactor`
  - only exists when: `physicalVirtualCoreHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (onPremVCoreHours)`** (number)
  - depends on: `onPremVCoreHoursFactor`
  - only exists when: `onPremVCoreHoursFactor` = *Days*

- **`Days (onPremVCoreHoursFactor)`** (select)
  - depends on: `onPremVCoreHoursFactor`
  - only exists when: `onPremVCoreHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`computeBillingOption`** (radio)
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved (~8% savings)), `three-year` (3 year reserved (~24% savings))

- **`sqlLicenseBillingOption`** (radio)
  - choices: `payg` (License included), `ahb` (Azure Hybrid Benefit)

## Example component

```json
{
  "product": "Azure Arc",
  "name": "my-azure-arc",
  "fields": {
    "Region": "Central US",
    "Server": 1,
    "Service Tier": "Standard edition",
    "vCore(s)": 1,
    "Hours": 1
  }
}
```
