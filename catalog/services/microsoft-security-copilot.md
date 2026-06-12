# Microsoft Security Copilot

- slug: `microsoft-security-copilot`  |  module: `microsoft-security-copilot-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options: East US, UK South, West Europe, Australia East

- **`Security compute units per hour`** (number)

- **`Hours`** (number)
  - depends on: `computeHoursFactor`
  - disappears when: `computeHoursFactor` = *Days*

- **`computeHoursFactor`** (select)
  - depends on: `computeHoursFactor`
  - disappears when: `computeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`overageComputeUnits`** (number)

- **`overageComputeHours`** (number)
  - depends on: `overageComputeHoursFactor`
  - disappears when: `overageComputeHoursFactor` = *Days*

- **`overageComputeHoursFactor`** (select)
  - depends on: `overageComputeHoursFactor`
  - disappears when: `overageComputeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `computeHoursFactor`
  - only exists when: `computeHoursFactor` = *Days*

- **`Days (computeHoursFactor)`** (select)
  - depends on: `computeHoursFactor`
  - only exists when: `computeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (overageComputeHours)`** (number)
  - depends on: `overageComputeHoursFactor`
  - only exists when: `overageComputeHoursFactor` = *Days*

- **`Days (overageComputeHoursFactor)`** (select)
  - depends on: `overageComputeHoursFactor`
  - only exists when: `overageComputeHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Microsoft Security Copilot",
  "name": "my-microsoft-security-copilot",
  "fields": {
    "Region": "East US",
    "Security compute units per hour": 1,
    "Hours": 1,
    "computeHoursFactor": "Hours",
    "overageComputeUnits": 1
  }
}
```
