# Redis Cache

- slug: `redis-cache`  |  module: `redis-cache-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Basic, Standard, Premium, Enterprise, Enterprise Flash

- **`Instance`** (select)
  - depends on: `tier`
  - options: C0: 250 MB cache, C1: 1,024 MB cache, C2: 2,560 MB cache, C3: 6,144 MB cache, C4: 13,312 MB cache, C5: 26,624 MB cache, C6: 54,272 MB cache
  - when `tier` = *Standard*: C0: 250 MB cache, C1: 1,024 MB cache, C2: 2,560 MB cache, C3: 6,144 MB cache, C4: 13,312 MB cache, C5: 26,624 MB cache, C6: 54,272 MB cache
  - when `tier` = *Premium*: P1: 6,144 MB cache, P2: 13,312 MB cache, P3: 26,624 MB cache, P4: 54,272 MB cache, P5: 122,880 MB cache
  - when `tier` = *Enterprise*: E1: 1,024 MB cache, E5: 4,096 MB cache, E10: 12,288 MB cache, E20: 25,600 MB cache, E50: 51,200 MB cache, E100: 102,400 MB cache, E200: 204,800 MB cache, E400: 409,600 MB cache
  - when `tier` = *Enterprise Flash*: F300: 393,216 MB cache, F700: 732,160 MB cache, F1500: 1,489,920 MB cache

- **`Instances`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Premium*, `tier` = *Enterprise*, `tier` = *Enterprise Flash*

- **`Hours`** (number)
  - depends on: `tier`

- **`hoursFactor`** (select)
  - depends on: `tier`
  - options: Hours, Days, Month

- **`Shardper Instance`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*

- **`AdditionalReplicasper Shard`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*

- **`count`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*

- **`Scale Factor`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Enterprise*
  - options: x1 (Capacity 2), x2 (Capacity 4), x3 (Capacity 6), x4 (Capacity 8), x5 (Capacity 10), x6 (Capacity 12), x7 (Capacity 14), x8 (Capacity 16), x9 (Capacity 18), x10 (Capacity 20)

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`billingOption`** (radio)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*, `tier` = *Enterprise*, `tier` = *Enterprise Flash*
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved (~36% savings)), `three-year` (3 year reserved (~55% savings))

- **`softwareBillingOption`** (radio)
  - depends on: `tier`
  - only exists when: `tier` = *Enterprise*, `tier` = *Enterprise Flash*
  - choices: `payg` (License included)

## Example component

```json
{
  "product": "Redis Cache",
  "name": "my-redis-cache",
  "fields": {
    "Region": "Central US",
    "Tier": "Basic",
    "Instance": "C0: 250 MB cache",
    "Instances": 1,
    "Hours": 1
  }
}
```
