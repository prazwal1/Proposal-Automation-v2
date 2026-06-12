# Api Management

- slug: `api-management`  |  module: `api-management-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (59): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`API Services`** (select)
  - options: API Management v2, API Management, API Center

- **`Tier`** (select)
  - depends on: `apiService`
  - options: Basic, Standard, Premium
  - when `apiService` = *API Management*: Consumption, Developer, Basic, Standard, Premium
  - when `apiService` = *API Center*: Standard, Free

- **`Units`** (number)
  - depends on: `apiService`
  - disappears when: `apiService` = *API Center*

- **`Hours`** (number)
  - depends on: `apiService`

- **`hoursFactor`** (select)
  - depends on: `apiService`
  - options: Hours, Days, Month

- **`scaleOutUnits`** (number)
  - depends on: `apiService`
  - disappears when: `apiService` = *API Management*, `apiService` = *API Center*

- **`scaleOutHours`** (number)
  - depends on: `apiService`

- **`scaleOutHoursFactor`** (select)
  - depends on: `apiService`
  - options: Hours, Days, Month

- **`x 10,000 api requests per month`** (number)
  - depends on: `apiService`, `tier`
  - disappears when: `apiService` = *API Management*, `apiService` = *API Center*, `tier` = *Premium*

- **`Gateways`** (number)
  - depends on: `apiService`
  - only exists when: `apiService` = *API Management*, `tier` = *Standard*

- **`API Centers`** (number)
  - depends on: `apiService`
  - only exists when: `apiService` = *API Center*

- **`gatewayHours`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`gatewayHoursFactor`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (scaleOutHours)`** (number)
  - depends on: `scaleOutHoursFactor`
  - only exists when: `scaleOutHoursFactor` = *Days*

- **`Days (scaleOutHoursFactor)`** (select)
  - depends on: `scaleOutHoursFactor`
  - only exists when: `scaleOutHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Api Management",
  "name": "my-api-management",
  "fields": {
    "Region": "Central US",
    "API Services": "API Management v2",
    "Tier": "Basic",
    "Units": 1,
    "Hours": 1
  }
}
```
