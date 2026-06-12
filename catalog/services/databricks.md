# Databricks

- slug: `databricks`  |  module: `databricks-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Workload`** (select)
  - options: All-Purpose Compute with Photon, All-Purpose Compute, Automated Serverless Compute, Spark Declarative Pipeline with Photon, Spark Declarative Pipeline, Interactive Serverless Compute, Jobs Compute with Photon, Jobs Compute, Jobs Light Compute, SQL Compute, SQL Pro Compute, Serverless SQL, Database Serverless Compute

- **`Tier`** (select)
  - options: Standard, Premium

- **`Category`** (select)
  - options: All, General purpose, GPU, Memory optimized, Storage optimized

- **`Instance Series`** (select)
  - depends on: `category`
  - options (44): All, Da v4-series, Dadsv5-series, Dadsv6-series, Das v4-series, Dasv5-series, DCasv5-series, Dd v4-series, Dds v4-series, Ddsv5-series, Ddsv6-series, Dpdsv6-series, Dpsv6-series, Dsv2-series, Dsv3-series, ...
  - when `category` = *General purpose*: All, Da v4-series, Dadsv5-series, Dadsv6-series, Das v4-series, Dasv5-series, DCasv5-series, Dd v4-series, Dds v4-series, Ddsv5-series, ...
  - when `category` = *GPU*: All, NC A100 v4-series, NC_T4_v3-series, NCads H100 v5-series, NCsv3-series, NDsrH100v5-series, NVads A10 v5-series
  - when `category` = *Memory optimized*: All, Dsv2-series, Dv2-series, Ea v4-series, Eadsv5-series, Eadsv6-series, Eas v4-series, Easv5-series, Ed v4-series, Eds v4-series, ...
  - when `category` = *Storage optimized*: All, Lasv3-series, Ls-series, Lsv3-series

- **`Instance: (Need help finding the right VM?)`** (text)

- **`Virtual machines`** (number)

- **`Hours`** (number)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`dbuHours`** (number)
  - depends on: `dbuHoursFactor`
  - disappears when: `dbuHoursFactor` = *Days*

- **`dbuHoursFactor`** (select)
  - depends on: `dbuHoursFactor`
  - disappears when: `dbuHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (dbuHours)`** (number)
  - depends on: `dbuHoursFactor`
  - only exists when: `dbuHoursFactor` = *Days*

- **`Days (dbuHoursFactor)`** (select)
  - depends on: `dbuHoursFactor`
  - only exists when: `dbuHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`computeBillingOption`** (radio)
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~31% savings)), `sv-three-year` (3 year savings plan (~53% savings)), `one-year` (1 year reserved (~39% savings)), `three-year` (3 year reserved)

## Example component

```json
{
  "product": "Databricks",
  "name": "my-databricks",
  "fields": {
    "Region": "Central US",
    "Workload": "All-Purpose Compute with Photon",
    "Tier": "Standard",
    "Category": "All",
    "Instance Series": "All"
  }
}
```
