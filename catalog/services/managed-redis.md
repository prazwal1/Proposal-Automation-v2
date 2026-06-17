# Managed Redis

- slug: `managed-redis`  |  module: `managed-redis-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Memory Optimized, Balanced (Memory + Compute), Compute Optimized, Flash Optimized

- **`Instance`** (select)
  - depends on: `tier`
  - options: M10:  12 GB cache, 2 vCPU, M20:  24 GB cache, 4 vCPU, M50:  60 GB cache, 8 vCPU, M100:  120 GB cache, 16 vCPU, M150:  175 GB cache, 24 vCPU, M250:  235 GB cache, 32 vCPU, M350:  360 GB cache, 48 vCPU, M500:  480 GB cache, 64 vCPU, M700:  720 GB cache, 96 vCPU, M1000:  960 GB cache, 128 vCPU, M1500:  1440 GB cache, 192 vCPU, M2000:  1920 GB cache, 256 vCPU
  - when `tier` = *Balanced (Memory + Compute)*: B0:  0.5 GB cache, 2 vCPU, B1:  1 GB cache, 2 vCPU, B3:  3 GB cache, 2 vCPU, B5:  6 GB cache, 2 vCPU, B10:  12 GB cache, 4 vCPU, B20:  24 GB cache, 8 vCPU, B50:  60 GB cache, 16 vCPU, B100:  120 GB cache, 32 vCPU, B150:  175 GB cache, 48 vCPU, B250:  235 GB cache, 64 vCPU, B350:  360 GB cache, 96 vCPU, B500:  480 GB cache, 128 vCPU, B700:  720 GB cache, 192 vCPU, B1000:  960 GB cache, 256 vCPU
  - when `tier` = *Compute Optimized*: X3:  3 GB cache, 4 vCPU, X5:  6 GB cache, 4 vCPU, X10:  12 GB cache, 8 vCPU, X20:  24 GB cache, 16 vCPU, X50:  60 GB cache, 32 vCPU, X100:  120 GB cache, 64 vCPU, X150:  175 GB cache, 96 vCPU, X250:  235 GB cache, 128 vCPU, X350:  360 GB cache, 192 vCPU, X500:  480 GB cache, 256 vCPU, X700:  720 GB cache, 320 vCPU
  - when `tier` = *Flash Optimized*: A250:  256 GB cache, 8 vCPU, A500:  525 GB cache, 16 vCPU, A700:  787 GB cache, 24 vCPU, A1000:  1050 GB cache, 32 vCPU, A1500:  1574 GB cache, 48 vCPU, A2000:  2099 GB cache, 64 vCPU, A4500:  4723 GB cache, 144 vCPU

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

- **`billingOption`** (radio)
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved), `three-year` (3 year reserved)

## Example component

```json
{
  "product": "Managed Redis",
  "name": "my-managed-redis",
  "fields": {
    "Region": "Central US",
    "Tier": "Memory Optimized",
    "Instance": "M10:  12 GB cache, 2 vCPU",
    "Instances": 1,
    "Hours": 1
  }
}
```
