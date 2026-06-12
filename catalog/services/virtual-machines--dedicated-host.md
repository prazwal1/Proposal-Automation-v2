# Dedicated Host

- slug: `virtual-machines--dedicated-host`  |  module: `virtual-machines\dedicated-host-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`VM series`** (select)
  - options (40): Dadsv5, Dasv4, Dasv5, Dcadsv5, Dcasv5, Dcdsv3, Dcsv2, Dcsv3, Ddsv4, Ddsv5, Dsv3, Dsv4, Dsv5, Eadsv5, Easv4, ...

- **`Host type`** (select)
  - options: Type 3, Type 4

- **`Host`** (number)

- **`Hours`** (number)
  - depends on: `hostHoursFactor`
  - disappears when: `hostHoursFactor` = *Days*

- **`hostHoursFactor`** (select)
  - depends on: `hostHoursFactor`
  - disappears when: `hostHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Software`** (select) — section: *Software licenses* (opened automatically)
  - options (20): Windows OS, Biztalk Enterprise, Biztalk Standard, RHEL for SAP Business Applications, SUSE Linux Enterprise for HPC + 24x7 Support, SUSE Linux Enterprise for SAP Applications + 24x7 Support, SUSE Linux Enterprise + 24x7 Support, SQL Server Enterprise, SQL Server Linux Enterprise, SQL Server Linux Standard, SQL Server Linux Web, SQL Server Enterprise Red Hat Enterprise Linux, SQL Server Standard Red Hat Enterprise Linux, SQL Server Web Red Hat Enterprise Linux, SQL Server Enterprise SLES, ...

- **`vCPU`** (select) — section: *Software licenses* (opened automatically)
  - options (18): 2 vCPU, 4 vCPU, 8 vCPU, 12 vCPU, 16 vCPU, 20 vCPU, 24 vCPU, 32 vCPU, 48 vCPU, 64 vCPU, 72 vCPU, 80 vCPU, 96 vCPU, 128 vCPU, 208 vCPU, ...

- **`softwareHours-0`** (number) — section: *Software licenses* (opened automatically)
  - depends on: `softwareHoursFactor-0`
  - disappears when: `softwareHoursFactor-0` = *Days*

- **`softwareHoursFactor-0`** (select) — section: *Software licenses* (opened automatically)
  - depends on: `softwareHoursFactor-0`
  - disappears when: `softwareHoursFactor-0` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `hostHoursFactor`
  - only exists when: `hostHoursFactor` = *Days*

- **`Days (hostHoursFactor)`** (select)
  - depends on: `hostHoursFactor`
  - only exists when: `hostHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (softwareHours-0)`** (number)
  - depends on: `softwareHoursFactor-0`
  - only exists when: `softwareHoursFactor-0` = *Days*

- **`Days (softwareHoursFactor-0)`** (select)
  - depends on: `softwareHoursFactor-0`
  - only exists when: `softwareHoursFactor-0` = *Days*
  - options: Hours, Days, Month

- **`billingOption`** (radio)
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~31% savings)), `sv-three-year` (3 year savings plan (~53% savings)), `one-year` (1 year reserved (~41% savings)), `three-year` (3 year reserved (~62% savings))

## Example component

```json
{
  "product": "Dedicated Host",
  "name": "my-virtual-machines--dedicated-host",
  "fields": {
    "Region": "Central US",
    "VM series": "Dadsv5",
    "Host type": "Type 3",
    "Host": 1,
    "Hours": 1
  }
}
```
