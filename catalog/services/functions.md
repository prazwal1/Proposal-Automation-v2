# Functions

- slug: `functions`  |  module: `functions-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Consumption, Flex Consumption, Premium

- **`Memory size (MB)`** (select)
  - depends on: `tier`
  - disappears when: `tier` = *Consumption*, `tier` = *Premium*
  - options: 512, 2048, 4096

- **`x10 On Demand executions per month`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Consumption*, `tier` = *Premium*

- **`Active On Demand execution seconds per instance per month`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Consumption*, `tier` = *Premium*

- **`Number of instances`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Consumption*, `tier` = *Premium*

- **`Memory size`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Consumption*
  - options: 128, 256, 384, 512, 640, 768, 896, 1024, 1152, 1280, 1408, 1536

- **`Execution time (in milliseconds)`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Consumption*

- **`Executions per month`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Consumption*

- **`Instance`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*
  - options: EP1: 1 Cores(s), 3.5 GB RAM, 250 GB Storage, EP2: 2 Cores(s), 7 GB RAM, 250 GB Storage, EP3: 4 Cores(s), 14 GB RAM, 250 GB Storage

- **`Instances`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*

- **`Hours`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*

- **`preWarmedCountHoursFactor`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*
  - options: Hours, Days, Month

- **`additionalUnitsCount`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*

- **`additionalUnitsCountHours`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*

- **`additionalUnitsCountHoursFactor`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*
  - options: Hours, Days, Month

- **`billingOption`** (radio)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year reserved (~17% savings)), `sv-three-year` (3 year reserved (~17% savings))

## Example component

```json
{
  "product": "Functions",
  "name": "my-functions",
  "fields": {
    "Region": "Central US",
    "Tier": "Consumption",
    "Memory size (MB)": "512",
    "x10 On Demand executions per month": 1,
    "Active On Demand execution seconds per instance per month": 1
  }
}
```
