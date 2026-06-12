# Machine Learning Service

- slug: `machine-learning-service`  |  module: `machine-learning-service-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Category`** (select)
  - options: All, Compute optimized, General purpose, GPU, High performance compute, Memory optimized

- **`Instance Series`** (select)
  - depends on: `category`
  - options (18): All, Dds v4-series, D-series, Dsv2-series, Dsv3-series, Dv2-series, Dv3-series, Ea v4-series, Ev3-series, Fsv2-series, HC-series, M-series, NC_T4_v3-series, NC-series, NCsv3-series, ...
  - when `category` = *Compute optimized*: All, Fsv2-series
  - when `category` = *General purpose*: All, Dds v4-series, D-series, Dsv2-series, Dsv3-series, Dv2-series, Dv3-series
  - when `category` = *GPU*: All, NC_T4_v3-series, NC-series, NCsv3-series, NDm A100 v4-series, NV-series, NVv3-series
  - when `category` = *High performance compute*: All, HC-series
  - when `category` = *Memory optimized*: All, D-series, Dsv2-series, Dv2-series, Ea v4-series, Ev3-series, M-series

- **`Instance: (Need help finding the right VM?)`** (text)

- **`Instances`** (number)

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
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~31% savings)), `sv-three-year` (3 year savings plan (~53% savings)), `one-year` (1 year reserved (~35% savings)), `three-year` (3 year reserved)

## Example component

```json
{
  "product": "Machine Learning Service",
  "name": "my-machine-learning-service",
  "fields": {
    "Region": "Central US",
    "Category": "All",
    "Instance Series": "All",
    "Instances": 1,
    "Hours": 1
  }
}
```
