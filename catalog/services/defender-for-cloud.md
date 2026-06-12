# Defender For Cloud

- slug: `defender-for-cloud`  |  module: `defender-for-cloud-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Defender for Cloud Solution Plan Type`** (select)
  - options: Cloud Security Posture Management (CSPM), Cloud Workload Protection

- **`Billable resources`** (number)
  - depends on: `planType`
  - disappears when: `planType` = *Cloud Workload Protection*

- **`Hours`** (number)
  - depends on: `planType`

- **`postureMgmtHoursFactor`** (select)
  - depends on: `planType`
  - options: Hours, Days, Month

- **`Servers`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`serversPlan2Nodes`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`vCores`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`Images`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`Nodes`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`sqlDbServers`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`Total vCores`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`Instances`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`postgresqlInstances`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`x100 RUs`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`Number of storage accounts`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`overageUnits`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`Storage scanned (GB)`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`x 1,000 total tokens`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`Estimated API monthly Transactions (in millions)`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`Plan`** (select)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*
  - options: Plan 1, Entitlement Limit: 1 Million API Calls, Plan 2, Entitlement Limit: 5 Million API Calls, Plan 3, Entitlement Limit: 50 Million API Calls, Plan 4, Entitlement Limit: 100 Million API Calls, Plan 5, Entitlement Limit: 1 Billion API Calls

- **`Vaults`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`Subscriptions`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Cloud Workload Protection*

- **`Days`** (number)
  - depends on: `postureMgmtHoursFactor`
  - only exists when: `postureMgmtHoursFactor` = *Days*

- **`Days (postureMgmtHoursFactor)`** (select)
  - depends on: `postureMgmtHoursFactor`
  - only exists when: `postureMgmtHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Defender For Cloud",
  "name": "my-defender-for-cloud",
  "fields": {
    "Region": "Central US",
    "Defender for Cloud Solution Plan Type": "Cloud Security Posture Management (CSPM)",
    "Billable resources": 1,
    "Hours": 1,
    "postureMgmtHoursFactor": "Hours"
  }
}
```
