# Data Explorer

- slug: `data-explorer`  |  module: `data-explorer-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Environment`** (select)
  - options: Dev/Test, Production

- **`GB`** (number)
  - depends on: `dataCollectedUnitFactor`
  - disappears when: `dataCollectedUnitFactor` = *TB*

- **`dataCollectedUnitFactor`** (select)
  - depends on: `dataCollectedUnitFactor`
  - disappears when: `dataCollectedUnitFactor` = *TB*
  - options: GB, TB

- **`Hot Cache retention (days)`** (number)

- **`Total retention (days)`** (number)

- **`Estimated Data Compression`** (number)

- **`Hours`** (number) — section: *Engine Instances* (opened automatically)
  - depends on: `engineInstanceHoursFactor`
  - disappears when: `engineInstanceHoursFactor` = *Days*

- **`engineInstanceHoursFactor`** (select) — section: *Engine Instances* (opened automatically)
  - depends on: `engineInstanceHoursFactor`
  - disappears when: `engineInstanceHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`dataManagementHours`** (number) — section: *Data Management Instances* (opened automatically)
  - depends on: `dataManagementHoursFactor`
  - disappears when: `dataManagementHoursFactor` = *Days*

- **`dataManagementHoursFactor`** (select) — section: *Data Management Instances* (opened automatically)
  - depends on: `dataManagementHoursFactor`
  - disappears when: `dataManagementHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`TB`** (number)
  - depends on: `dataCollectedUnitFactor`
  - only exists when: `dataCollectedUnitFactor` = *TB*

- **`TB (dataCollectedUnitFactor)`** (select)
  - depends on: `dataCollectedUnitFactor`
  - only exists when: `dataCollectedUnitFactor` = *TB*
  - options: GB, TB

- **`Days`** (number)
  - depends on: `engineInstanceHoursFactor`
  - only exists when: `engineInstanceHoursFactor` = *Days*

- **`Days (engineInstanceHoursFactor)`** (select)
  - depends on: `engineInstanceHoursFactor`
  - only exists when: `engineInstanceHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (dataManagementHours)`** (number)
  - depends on: `dataManagementHoursFactor`
  - only exists when: `dataManagementHoursFactor` = *Days*

- **`Days (dataManagementHoursFactor)`** (select)
  - depends on: `dataManagementHoursFactor`
  - only exists when: `dataManagementHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`engineInstanceBillingOption`** (radio) — section: *Engine Instances* (opened automatically)
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~32% savings)), `sv-three-year` (3 year savings plan (~53% savings)), `one-year` (1 year reserved (~41% savings)), `three-year` (3 year reserved (~62% savings))

- **`dataManagementBillingOption`** (radio) — section: *Data Management Instances* (opened automatically)
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~31% savings)), `sv-three-year` (3 year savings plan (~53% savings)), `one-year` (1 year reserved (~35% savings)), `three-year` (3 year reserved)

- **`dataExplorerMarkupBillingOption`** (radio) — section: *Azure Data Explorer Markup* (opened automatically)
  - depends on: `environment`
  - disappears when: `environment` = *Dev/Test*
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved (~15% savings)), `three-year` (3 year reserved (~30% savings))

## Example component

```json
{
  "product": "Data Explorer",
  "name": "my-data-explorer",
  "fields": {
    "Region": "Central US",
    "Environment": "Dev/Test",
    "GB": 1,
    "dataCollectedUnitFactor": "GB",
    "Hot Cache retention (days)": 1
  }
}
```
