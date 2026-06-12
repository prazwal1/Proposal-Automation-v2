# Container Registry

- slug: `container-registry`  |  module: `container-registry-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (58): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Basic, Standard, Premium

- **`Registry`** (number)

- **`Days`** (number)

- **`GB`** (number)
  - depends on: `storageUnitsFactor`, `dataTransferType`
  - disappears when: `storageUnitsFactor` = *TB*

- **`storageUnitsFactor`** (select)
  - depends on: `storageUnitsFactor`
  - disappears when: `storageUnitsFactor` = *TB*
  - options: GB, TB

- **`CPUs`** (number)

- **`Seconds`** (number)

- **`Data Transfer Type`** (select)
  - options: Inter Region, Internet Egress

- **`Source Region`** (select)
  - options (59): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Destination Region`** (select)
  - depends on: `dataTransferType`
  - disappears when: `dataTransferType` = *Internet Egress*
  - options (58): Central US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, Sweden Central, ...

- **`interRegionUnits`** (number)
  - depends on: `dataTransferType`
  - disappears when: `dataTransferType` = *Internet Egress*

- **`Regions`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Premium*

- **`TB`** (number)
  - depends on: `storageUnitsFactor`
  - only exists when: `storageUnitsFactor` = *TB*

- **`TB (storageUnitsFactor)`** (select)
  - depends on: `storageUnitsFactor`
  - only exists when: `storageUnitsFactor` = *TB*
  - options: GB, TB

- **`Routed Via`** (select)
  - depends on: `dataTransferType`
  - only exists when: `dataTransferType` = *Internet Egress*
  - options: Microsoft Global Network, Public Internet

## Example component

```json
{
  "product": "Container Registry",
  "name": "my-container-registry",
  "fields": {
    "Region": "Central US",
    "Tier": "Basic",
    "Registry": 1,
    "Days": 1,
    "GB": 1
  }
}
```
