# Microsoft Fabric

- slug: `microsoft-fabric`  |  module: `microsoft-fabric-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`SKU`** (select)
  - options: F2, 2 Capacity units, F4, 4 Capacity units, F8, 8 Capacity units, F16, 16 Capacity units, F32, 32 Capacity units, F64, 64 Capacity units, F128, 128 Capacity units, F256, 256 Capacity units, F512, 512 Capacity units, F1024, 1024 Capacity units, F2048, 2048 Capacity units

- **`Hours`** (number)
  - depends on: `computeHoursFactor`
  - disappears when: `computeHoursFactor` = *Days*

- **`computeHoursFactor`** (select)
  - depends on: `computeHoursFactor`
  - disappears when: `computeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Hot storage type`** (select)
  - options: OneLake hot storage, OneLake BCDR hot storage

- **`GB`** (number)

- **`Cool storage type`** (select)
  - options: OneLake cool storage, OneLake BCDR cool Storage

- **`coolStorage`** (number)

- **`Cold storage type`** (select)
  - options: OneLake cold storage, OneLake BCDR cold storage

- **`coldStorage`** (number)

- **`Cache`** (select)
  - options: OneLake cache

- **`cacheStorage`** (number)

- **`Days`** (number)
  - depends on: `computeHoursFactor`
  - only exists when: `computeHoursFactor` = *Days*

- **`Days (computeHoursFactor)`** (select)
  - depends on: `computeHoursFactor`
  - only exists when: `computeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`computeBillingOption`** (radio)
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved), `three-year` (3 year reserved)

## Example component

```json
{
  "product": "Microsoft Fabric",
  "name": "my-microsoft-fabric",
  "fields": {
    "Region": "Central US",
    "SKU": "F2, 2 Capacity units",
    "Hours": 1,
    "computeHoursFactor": "Hours",
    "Hot storage type": "OneLake hot storage"
  }
}
```
