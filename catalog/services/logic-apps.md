# Logic Apps

- slug: `logic-apps`  |  module: `logic-apps-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Plan`** (select)
  - options: Standard, Consumption

- **`Instance`** (select)
  - depends on: `standardPlan`
  - disappears when: `standardPlan` = *Consumption*
  - options: WS1: 1 vCore, 3.5 GiB RAM, 250 GB Storage, WS2: 2 vCores, 7 GiB RAM, 250 GB Storage, WS3: 4 vCores, 14 GiB RAM, 250 GB Storage

- **`Instances`** (number)
  - depends on: `standardPlan`
  - disappears when: `standardPlan` = *Consumption*

- **`Hours`** (number)
  - depends on: `standardPlan`, `standardPlanInstanceHoursFactor`, `tier`
  - disappears when: `standardPlan` = *Consumption*, `standardPlanInstanceHoursFactor` = *Days*

- **`standardPlanInstanceHoursFactor`** (select)
  - depends on: `standardPlan`, `standardPlanInstanceHoursFactor`, `tier`
  - disappears when: `standardPlan` = *Consumption*, `standardPlanInstanceHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Standard Connector Calls per day`** (number)
  - depends on: `standardPlan`
  - disappears when: `standardPlan` = *Consumption*

- **`Day`** (number)

- **`Enterprise Connector Calls per day`** (number)
  - depends on: `standardPlan`
  - disappears when: `standardPlan` = *Consumption*

- **`enterpriseDays`** (number)

- **`Tier`** (select)
  - options: Developer, Premium

- **`Base Units`** (number)
  - depends on: `tier`

- **`baseUnitsPremiumHours`** (number)
  - depends on: `tier`, `baseUnitsPremiumHoursFactor`
  - disappears when: `tier` = *Developer*, `baseUnitsPremiumHoursFactor` = *Days*

- **`baseUnitsPremiumHoursFactor`** (select)
  - depends on: `tier`, `baseUnitsPremiumHoursFactor`
  - disappears when: `tier` = *Developer*, `baseUnitsPremiumHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Scale Units`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Developer*

- **`scaleUnitsPremiumHours`** (number)
  - depends on: `tier`, `scaleUnitsPremiumHoursFactor`
  - disappears when: `tier` = *Developer*, `scaleUnitsPremiumHoursFactor` = *Days*

- **`scaleUnitsPremiumHoursFactor`** (select)
  - depends on: `tier`, `scaleUnitsPremiumHoursFactor`
  - disappears when: `tier` = *Developer*, `scaleUnitsPremiumHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Standard Integration Accounts`** (number)

- **`standardIntegrationHours`** (number)
  - depends on: `standardIntegrationHoursFactor`
  - disappears when: `standardIntegrationHoursFactor` = *Days*

- **`standardIntegrationHoursFactor`** (select)
  - depends on: `standardIntegrationHoursFactor`
  - disappears when: `standardIntegrationHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Basic Integration Accounts`** (number)

- **`basicIntegrationHours`** (number)
  - depends on: `basicIntegrationHoursFactor`
  - disappears when: `basicIntegrationHoursFactor` = *Days*

- **`basicIntegrationHoursFactor`** (select)
  - depends on: `basicIntegrationHoursFactor`
  - disappears when: `basicIntegrationHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Action Executions per day`** (number)
  - depends on: `standardPlan`
  - only exists when: `standardPlan` = *Consumption*

- **`actionDays`** (number)
  - depends on: `standardPlan`
  - only exists when: `standardPlan` = *Consumption*

- **`GB`** (number)
  - depends on: `standardPlan`
  - only exists when: `standardPlan` = *Consumption*

- **`dataRetentionUnits`** (select)
  - depends on: `standardPlan`
  - only exists when: `standardPlan` = *Consumption*
  - options: GB, TB

- **`Standard Connector Executions per day`** (number)
  - depends on: `standardPlan`
  - only exists when: `standardPlan` = *Consumption*

- **`Enterprise Connector Executions per day`** (number)
  - depends on: `standardPlan`
  - only exists when: `standardPlan` = *Consumption*

- **`Days`** (number)
  - depends on: `standardPlanInstanceHoursFactor`
  - only exists when: `standardPlanInstanceHoursFactor` = *Days*

- **`Days (standardPlanInstanceHoursFactor)`** (select)
  - depends on: `standardPlanInstanceHoursFactor`
  - only exists when: `standardPlanInstanceHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (baseUnitsPremiumHours)`** (number)
  - depends on: `baseUnitsPremiumHoursFactor`
  - only exists when: `baseUnitsPremiumHoursFactor` = *Days*

- **`Days (baseUnitsPremiumHoursFactor)`** (select)
  - depends on: `baseUnitsPremiumHoursFactor`
  - only exists when: `baseUnitsPremiumHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (scaleUnitsPremiumHours)`** (number)
  - depends on: `scaleUnitsPremiumHoursFactor`
  - only exists when: `scaleUnitsPremiumHoursFactor` = *Days*

- **`Days (scaleUnitsPremiumHoursFactor)`** (select)
  - depends on: `scaleUnitsPremiumHoursFactor`
  - only exists when: `scaleUnitsPremiumHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (standardIntegrationHours)`** (number)
  - depends on: `standardIntegrationHoursFactor`
  - only exists when: `standardIntegrationHoursFactor` = *Days*

- **`Days (standardIntegrationHoursFactor)`** (select)
  - depends on: `standardIntegrationHoursFactor`
  - only exists when: `standardIntegrationHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (basicIntegrationHours)`** (number)
  - depends on: `basicIntegrationHoursFactor`
  - only exists when: `basicIntegrationHoursFactor` = *Days*

- **`Days (basicIntegrationHoursFactor)`** (select)
  - depends on: `basicIntegrationHoursFactor`
  - only exists when: `basicIntegrationHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Logic Apps",
  "name": "my-logic-apps",
  "fields": {
    "Region": "Central US",
    "Plan": "Standard",
    "Instance": "WS1: 1 vCore, 3.5 GiB RAM, 250 GB Storage",
    "Instances": 1,
    "Hours": 1
  }
}
```
