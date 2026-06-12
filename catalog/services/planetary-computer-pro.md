# Planetary Computer Pro

- slug: `planetary-computer-pro`  |  module: `planetary-computer-pro-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options: East US, North Central US, UK South, West Europe, Canada Central, US Gov Virginia

- **`Compute hours`** (number)

- **`GB`** (number)
  - depends on: `geospatialStorageFactor`
  - disappears when: `geospatialStorageFactor` = *TB*

- **`geospatialStorageFactor`** (select)
  - depends on: `geospatialStorageFactor`
  - disappears when: `geospatialStorageFactor` = *TB*
  - options: GB, TB

- **`x 10,000 Geospatial data operations`** (number)

- **`transferData`** (number)
  - depends on: `transferDataFactor`
  - disappears when: `transferDataFactor` = *TB*

- **`transferDataFactor`** (select)
  - depends on: `transferDataFactor`
  - disappears when: `transferDataFactor` = *TB*
  - options: GB, TB

- **`TB`** (number)
  - depends on: `geospatialStorageFactor`
  - only exists when: `geospatialStorageFactor` = *TB*

- **`TB (geospatialStorageFactor)`** (select)
  - depends on: `geospatialStorageFactor`
  - only exists when: `geospatialStorageFactor` = *TB*
  - options: GB, TB

- **`TB (transferData)`** (number)
  - depends on: `transferDataFactor`
  - only exists when: `transferDataFactor` = *TB*

- **`TB (transferDataFactor)`** (select)
  - depends on: `transferDataFactor`
  - only exists when: `transferDataFactor` = *TB*
  - options: GB, TB

## Example component

```json
{
  "product": "Planetary Computer Pro",
  "name": "my-planetary-computer-pro",
  "fields": {
    "Region": "East US",
    "Compute hours": 1,
    "GB": 1,
    "geospatialStorageFactor": "GB",
    "x 10,000 Geospatial data operations": 1
  }
}
```
