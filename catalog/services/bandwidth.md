# Bandwidth

- slug: `bandwidth`  |  module: `bandwidth-module`

## Fields

- **`product-name`** (text)

- **`Data Transfer Type`** (select)
  - options: Inter Region, Internet Egress

- **`Source Region`** (select)
  - options (59): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Destination Region`** (select)
  - depends on: `dataTransferType`
  - disappears when: `dataTransferType` = *Internet Egress*
  - options (58): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, Sweden Central, ...

- **`GB`** (number)
  - depends on: `dataTransferType`

- **`Routed Via`** (select)
  - depends on: `dataTransferType`
  - only exists when: `dataTransferType` = *Internet Egress*
  - options: Microsoft Global Network, Public Internet

## Example component

```json
{
  "product": "Bandwidth",
  "name": "my-bandwidth",
  "fields": {
    "Data Transfer Type": "Inter Region",
    "Source Region": "Central US",
    "Destination Region": "Central US",
    "GB": 1
  }
}
```
