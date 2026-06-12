# Container Apps

- slug: `container-apps`  |  module: `container-apps-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (59): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Plan Type`** (select)
  - options: Consumption, Dedicated, Dedicated – GPU enabled, Dynamic Sessions

- **`x1 million total requests per month`** (number)
  - depends on: `planType`
  - disappears when: `planType` = *Dedicated*, `planType` = *Dedicated – GPU enabled*, `planType` = *Dynamic Sessions*

- **`Concurrent requests per container app`** (number)
  - depends on: `planType`
  - disappears when: `planType` = *Dedicated*, `planType` = *Dedicated – GPU enabled*, `planType` = *Dynamic Sessions*

- **`Execution time per request (ms)`** (number)
  - depends on: `planType`
  - disappears when: `planType` = *Dedicated*, `planType` = *Dedicated – GPU enabled*, `planType` = *Dynamic Sessions*

- **`vCPU`** (select)
  - depends on: `planType`
  - disappears when: `planType` = *Dedicated*, `planType` = *Dedicated – GPU enabled*, `planType` = *Dynamic Sessions*
  - options (16): 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, ...

- **`Memory`** (select)
  - depends on: `planType`
  - disappears when: `planType` = *Dedicated*, `planType` = *Dedicated – GPU enabled*, `planType` = *Dynamic Sessions*
  - options: 1 GiB, 2 GiB, 3 GiB, 4 GiB, 5 GiB, 6 GiB, 7 GiB, 8 GiB

- **`workload`** (select)
  - depends on: `planType`
  - only exists when: `planType` = *Dedicated*
  - options: D4, 4 vCPU, 16 GiB RAM, $0.31, D8, 8 vCPU, 32 GiB RAM, $0.62, D16, 16 vCPU, 64 GiB RAM, $1.23, D32, 32 vCPU, 128 GiB RAM, $2.46, E4, 4 vCPU, 32 GiB RAM, $0.39, E8, 8 vCPU, 64 GiB RAM, $0.78, E16, 16 vCPU, 128 GiB RAM, $1.55, E32, 32 vCPU, 256 GiB RAM, $3.10

- **`Instances`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Dedicated*, `planType` = *Dedicated – GPU enabled*

- **`Hours`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Dedicated*, `planType` = *Dedicated – GPU enabled*

- **`dedicatedInstanceHoursFactor`** (select)
  - depends on: `planType`
  - only exists when: `planType` = *Dedicated*, `planType` = *Dedicated – GPU enabled*
  - options: Hours, Days, Month

- **`Sessions`** (number)
  - depends on: `planType`
  - only exists when: `planType` = *Dynamic Sessions*

- **`requestBillingOption`** (radio)
  - depends on: `planType`
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~15% discount)), `sv-three-year` (3 year savings plan (~17% discount))

- **`resourceBillingOption`** (radio)
  - depends on: `planType`
  - disappears when: `planType` = *Dedicated*, `planType` = *Dedicated – GPU enabled*, `planType` = *Dynamic Sessions*
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~15% discount)), `sv-three-year` (3 year savings plan (~17% discount))

## Example component

```json
{
  "product": "Container Apps",
  "name": "my-container-apps",
  "fields": {
    "Region": "Central US",
    "Plan Type": "Consumption",
    "x1 million total requests per month": 1,
    "Concurrent requests per container app": 1,
    "Execution time per request (ms)": 1
  }
}
```
