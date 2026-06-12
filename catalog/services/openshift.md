# Openshift

- slug: `openshift`  |  module: `openshift-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Version`** (select)
  - options: Red Hat OpenShift 4

- **`Category`** (select)
  - options: All, Compute optimized, General purpose, GPU, Memory optimized, Storage optimized

- **`Instance Series`** (select)
  - depends on: `workerNodeCategory`
  - options (20): All, Das v4-series, Dasv5-series, Dsv3-series, Dsv4-series, Dsv5-series, Eas v4-series, Easv5-series, Eds v4-series, Edsv5-series, Esv3-series, Esv4-series, Esv5-series, Fsv2-series, Ls-series, ...
  - when `workerNodeCategory` = *Compute optimized*: All, Fsv2-series
  - when `workerNodeCategory` = *General purpose*: All, Das v4-series, Dasv5-series, Dsv3-series, Dsv4-series, Dsv5-series
  - when `workerNodeCategory` = *GPU*: All, NC_T4_v3-series, NCsv3-series
  - when `workerNodeCategory` = *Memory optimized*: All, Eas v4-series, Easv5-series, Eds v4-series, Edsv5-series, Esv3-series, Esv4-series, Esv5-series, M-series
  - when `workerNodeCategory` = *Storage optimized*: All, Ls-series, Lsv2-series, Lsv3-series

- **`Instance: (Need help finding the right VM?)`** (text)

- **`Worker Nodes`** (number)

- **`Hours`** (number)
  - depends on: `workerNodeHoursFactor`
  - disappears when: `workerNodeHoursFactor` = *Days*

- **`workerNodeHoursFactor`** (select)
  - depends on: `workerNodeHoursFactor`
  - disappears when: `workerNodeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Disk size`** (select)
  - options: P10: 128 GiB, 500 IOPS, 100 MB/sec, P15: 256 GiB, 1100 IOPS, 125 MB/sec, P20: 512 GiB, 2300 IOPS, 150 MB/sec, P30: 1024 GiB, 5000 IOPS, 200 MB/sec, P40: 2048 GiB, 7500 IOPS, 250 MB/sec, P60: 8192 GiB, 16000 IOPS, 500 MB/sec, P70: 16384 GiB, 18000 IOPS, 750 MB/sec, P80: 32767 GiB, 20000 IOPS, 900 MB/sec

- **`masterNodesCategory`** (select)
  - options: All, Compute optimized, General purpose, Memory optimized

- **`masterNodesInstanceSeries`** (select)
  - depends on: `masterNodesCategory`
  - options: All, Das v4-series, Dasv5-series, Dsv3-series, Dsv4-series, Dsv5-series, Eas v4-series, Easv5-series, Eds v4-series, Edsv5-series, Esv3-series, Esv4-series, Esv5-series, Fsv2-series, M-series
  - when `masterNodesCategory` = *Compute optimized*: All, Fsv2-series
  - when `masterNodesCategory` = *General purpose*: All, Das v4-series, Dasv5-series, Dsv3-series, Dsv4-series, Dsv5-series
  - when `masterNodesCategory` = *Memory optimized*: All, Eas v4-series, Easv5-series, Eds v4-series, Edsv5-series, Esv3-series, Esv4-series, Esv5-series, M-series

- **`masterNodesSize`** (text)

- **`masterNodesHours`** (number)
  - depends on: `masterNodesHoursFactor`
  - disappears when: `masterNodesHoursFactor` = *Days*

- **`masterNodesHoursFactor`** (select)
  - depends on: `masterNodesHoursFactor`
  - disappears when: `masterNodesHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`disk5Size`** (select)
  - options: P30: 1024 GiB, 5000 IOPS, 200 MB/sec

- **`Days`** (number)
  - depends on: `workerNodeHoursFactor`
  - only exists when: `workerNodeHoursFactor` = *Days*

- **`Days (workerNodeHoursFactor)`** (select)
  - depends on: `workerNodeHoursFactor`
  - only exists when: `workerNodeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (masterNodesHours)`** (number)
  - depends on: `masterNodesHoursFactor`
  - only exists when: `masterNodesHoursFactor` = *Days*

- **`Days (masterNodesHoursFactor)`** (select)
  - depends on: `masterNodesHoursFactor`
  - only exists when: `masterNodesHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`workerNodeBillingOption`** (radio)
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved (~33% savings)), `three-year` (3 year reserved (~56% savings))

- **`workerNodeVMBillingOption`** (radio)
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved (~40% savings)), `three-year` (3 year reserved (~62% savings))

- **`masterNodesBillingOption`** (radio)
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved (~40% savings)), `three-year` (3 year reserved (~62% savings))

## Example component

```json
{
  "product": "Openshift",
  "name": "my-openshift",
  "fields": {
    "Region": "Central US",
    "Version": "Red Hat OpenShift 4",
    "Category": "All",
    "Instance Series": "All",
    "Worker Nodes": 1
  }
}
```
