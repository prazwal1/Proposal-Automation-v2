# Spring Apps

- slug: `spring-apps`  |  module: `spring-apps-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (59): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Plan`** (select)
  - options: Basic, Standard, Standard consumption, Enterprise

- **`vCPU(s)`** (number)
  - depends on: `plan`

- **`Memory (GB)`** (number)
  - depends on: `plan`

- **`Hours`** (number)
  - depends on: `plan`

- **`enterpriseHoursFactor`** (select)
  - depends on: `plan`
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `enterpriseHoursFactor`
  - only exists when: `enterpriseHoursFactor` = *Days*

- **`Days (enterpriseHoursFactor)`** (select)
  - depends on: `enterpriseHoursFactor`
  - only exists when: `enterpriseHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`groupBillingOption`** (radio)
  - depends on: `plan`
  - disappears when: `plan` = *Basic*, `plan` = *Standard*, `plan` = *Standard consumption*
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~20% discount)), `sv-three-year` (3 year savings plan (~47% discount))

## Example component

```json
{
  "product": "Spring Apps",
  "name": "my-spring-apps",
  "fields": {
    "Region": "Central US",
    "Plan": "Basic",
    "vCPU(s)": 1,
    "Memory (GB)": 1,
    "Hours": 1
  }
}
```
