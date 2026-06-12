# Purview

- slug: `purview`  |  module: `purview-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (52): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Offer`** (select)
  - options: Data Security, Data Compliance, Data Governance​, Data Map (Classic)

- **`Assets`** (number)
  - depends on: `purviewOfferType`
  - disappears when: `purviewOfferType` = *Data Compliance*

- **`Days`** (number)
  - depends on: `purviewOfferType`

- **`informationAssetsHoursFactor`** (select)
  - depends on: `purviewOfferType`
  - options: Days, Month

- **`User Activities`** (number)
  - depends on: `purviewOfferType`
  - disappears when: `purviewOfferType` = *Data Compliance*, `purviewOfferType` = *Data Governance​*, `purviewOfferType` = *Data Map (Classic)*

- **`Requests per day`** (number)
  - depends on: `purviewOfferType`
  - disappears when: `purviewOfferType` = *Data Compliance*, `purviewOfferType` = *Data Governance​*, `purviewOfferType` = *Data Map (Classic)*

- **`requestsAssetsHours`** (number)
  - depends on: `purviewOfferType`, `requestsAssetsHoursFactor`
  - disappears when: `purviewOfferType` = *Data Compliance*, `purviewOfferType` = *Data Governance​*, `purviewOfferType` = *Data Map (Classic)*, `requestsAssetsHoursFactor` = *Month*

- **`requestsAssetsHoursFactor`** (select)
  - depends on: `purviewOfferType`, `requestsAssetsHoursFactor`
  - disappears when: `purviewOfferType` = *Data Compliance*, `purviewOfferType` = *Data Governance​*, `purviewOfferType` = *Data Map (Classic)*, `requestsAssetsHoursFactor` = *Month*
  - options: Days, Month

- **`GBs`** (number)
  - depends on: `purviewOfferType`
  - disappears when: `purviewOfferType` = *Data Compliance*, `purviewOfferType` = *Data Governance​*, `purviewOfferType` = *Data Map (Classic)*

- **`securityHours`** (number)
  - depends on: `purviewOfferType`, `securityHoursFactor`
  - disappears when: `purviewOfferType` = *Data Compliance*, `purviewOfferType` = *Data Governance​*, `purviewOfferType` = *Data Map (Classic)*, `securityHoursFactor` = *Month*

- **`securityHoursFactor`** (select)
  - depends on: `purviewOfferType`, `securityHoursFactor`
  - disappears when: `purviewOfferType` = *Data Compliance*, `purviewOfferType` = *Data Governance​*, `purviewOfferType` = *Data Map (Classic)*, `securityHoursFactor` = *Month*
  - options: Days, Month

- **`1 Compute Unit`** (number)
  - depends on: `purviewOfferType`
  - disappears when: `purviewOfferType` = *Data Compliance*, `purviewOfferType` = *Data Governance​*, `purviewOfferType` = *Data Map (Classic)*

- **`Hours`** (number)
  - depends on: `purviewOfferType`
  - disappears when: `purviewOfferType` = *Data Compliance*, `purviewOfferType` = *Data Governance​*

- **`investigationHoursFactor`** (select)
  - depends on: `purviewOfferType`
  - disappears when: `purviewOfferType` = *Data Compliance*, `purviewOfferType` = *Data Governance​*
  - options: Hours

- **`x 10,000 assets`** (number)
  - depends on: `purviewOfferType`
  - disappears when: `purviewOfferType` = *Data Compliance*, `purviewOfferType` = *Data Governance​*, `purviewOfferType` = *Data Map (Classic)*

- **`x 1,000 assets`** (number)
  - depends on: `purviewOfferType`
  - only exists when: `purviewOfferType` = *Data Compliance*

- **`auditAssets`** (number)
  - depends on: `purviewOfferType`
  - only exists when: `purviewOfferType` = *Data Compliance*

- **`x 1 text record`** (number)
  - depends on: `purviewOfferType`
  - only exists when: `purviewOfferType` = *Data Compliance*

- **`communicationCompliancePremium`** (number)
  - depends on: `purviewOfferType`
  - only exists when: `purviewOfferType` = *Data Compliance*

- **`SKU (Data Quality)​`** (select)
  - depends on: `purviewOfferType`
  - only exists when: `purviewOfferType` = *Data Governance​*
  - options: Basic, Standard, Advanced

- **`Units`** (number)
  - depends on: `purviewOfferType`
  - only exists when: `purviewOfferType` = *Data Governance​*

- **`SKU (Controls and Reports)​`** (select)
  - depends on: `purviewOfferType`
  - only exists when: `purviewOfferType` = *Data Governance​*
  - options: Basic

- **`enterpriseSKUControlsReportsUnits`** (number)
  - depends on: `purviewOfferType`
  - only exists when: `purviewOfferType` = *Data Governance​*

- **`Minutes`** (number)
  - depends on: `purviewOfferType`
  - only exists when: `purviewOfferType` = *Data Map (Classic)*

- **`otherDataSourcesHoursFactor`** (select)
  - depends on: `purviewOfferType`
  - only exists when: `purviewOfferType` = *Data Map (Classic)*
  - options: Minutes, Hours

- **`Total vCores across all scans`** (number)
  - depends on: `purviewOfferType`
  - only exists when: `purviewOfferType` = *Data Map (Classic)*

- **`Capacity Units`** (number)
  - depends on: `purviewOfferType`
  - only exists when: `purviewOfferType` = *Data Map (Classic)*

- **`Service`** (select)
  - depends on: `purviewOfferType`
  - only exists when: `purviewOfferType` = *Data Map (Classic)*
  - options: C0, C1, D0

- **`DevOps policies`** (number)
  - depends on: `purviewOfferType`
  - only exists when: `purviewOfferType` = *Data Map (Classic)*

- **`API calls`** (number)
  - depends on: `purviewOfferType`
  - only exists when: `purviewOfferType` = *Data Map (Classic)*

- **`Month`** (number)
  - depends on: `informationAssetsHoursFactor`
  - only exists when: `informationAssetsHoursFactor` = *Month*

- **`Month (informationAssetsHoursFactor)`** (select)
  - depends on: `informationAssetsHoursFactor`
  - only exists when: `informationAssetsHoursFactor` = *Month*
  - options: Days, Month

- **`Month (requestsAssetsHours)`** (number)
  - depends on: `requestsAssetsHoursFactor`
  - only exists when: `requestsAssetsHoursFactor` = *Month*

- **`Month (requestsAssetsHoursFactor)`** (select)
  - depends on: `requestsAssetsHoursFactor`
  - only exists when: `requestsAssetsHoursFactor` = *Month*
  - options: Days, Month

- **`Month (securityHours)`** (number)
  - depends on: `securityHoursFactor`
  - only exists when: `securityHoursFactor` = *Month*

- **`Month (securityHoursFactor)`** (select)
  - depends on: `securityHoursFactor`
  - only exists when: `securityHoursFactor` = *Month*
  - options: Days, Month

## Example component

```json
{
  "product": "Purview",
  "name": "my-purview",
  "fields": {
    "Region": "Central US",
    "Offer": "Data Security",
    "Assets": 1,
    "Days": 1,
    "informationAssetsHoursFactor": "Days"
  }
}
```
