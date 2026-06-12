# Cloud Services

- slug: `cloud-services`  |  module: `cloud-services-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (59): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Category`** (select)
  - options: All, Compute optimized, General purpose, High performance compute, Memory optimized

- **`Instance Series`** (select)
  - depends on: `category`
  - options: All, A-series, Av2 Standard, D-series, Dv2-series, Dv3-series, Ev3-series, Fsv2-series, G-series, H-series
  - when `category` = *Compute optimized*: All, Fsv2-series
  - when `category` = *General purpose*: All, A-series, Av2 Standard, D-series, Dv2-series, Dv3-series
  - when `category` = *High performance compute*: All, H-series
  - when `category` = *Memory optimized*: All, D-series, Dv2-series, Ev3-series, G-series

- **`Instance: (Need help finding the right VM?)`** (text)

- **`Virtual machines`** (number)

- **`Hours`** (number)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`computeBillingOption`** (radio)
  - depends on: `instanceSeries`
  - disappears when: `instanceSeries` = *G-series*
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved (~21% savings)), `three-year` (3 year reserved (~31% savings))

## Example component

```json
{
  "product": "Cloud Services",
  "name": "my-cloud-services",
  "fields": {
    "Region": "Central US",
    "Category": "All",
    "Instance Series": "All",
    "Virtual machines": 1,
    "Hours": 1
  }
}
```
