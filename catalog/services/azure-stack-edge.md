# Azure Stack Edge

- slug: `azure-stack-edge`  |  module: `azure-stack-edge-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Hardware`** (select)
  - options: Azure Stack Edge Pro 2, Azure Stack Edge Pro, Azure Stack Edge Pro R, Azure Stack Edge Mini R

- **`Unit(s)`** (number)
  - depends on: `tier`

- **`proOneUnitTwoGpuUnits`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Stack Edge Pro 2*, `tier` = *Azure Stack Edge Pro R*, `tier` = *Azure Stack Edge Mini R*

- **`proOneUnitFpgaUnits`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Stack Edge Pro 2*, `tier` = *Azure Stack Edge Pro R*, `tier` = *Azure Stack Edge Mini R*

- **`Ship to`** (select)
  - depends on: `tier`
  - options: Americas, APAC, EMEA, US

- **`Units`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Azure Stack Edge Pro R*

- **`proROneGpuUpsUnits`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Azure Stack Edge Pro R*

## Example component

```json
{
  "product": "Azure Stack Edge",
  "name": "my-azure-stack-edge",
  "fields": {
    "Region": "Central US",
    "Hardware": "Azure Stack Edge Pro 2",
    "Unit(s)": 1,
    "proOneUnitTwoGpuUnits": 1,
    "proOneUnitFpgaUnits": 1
  }
}
```
