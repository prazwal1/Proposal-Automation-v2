# Iot Central

- slug: `iot-central`  |  module: `iot-central-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options: Central US, East US, East US 2, West Central US, West US, UK South, Sweden Central, Sweden South, Japan East, North Europe, West Europe, Australia East, Southeast Asia

- **`Tier`** (select)
  - options: Standard 0, Standard 1, Standard 2

- **`Devices`** (number)

- **`Hours`** (number)

- **`Additional messages (in millions)`** (number)

## Example component

```json
{
  "product": "Iot Central",
  "name": "my-iot-central",
  "fields": {
    "Region": "Central US",
    "Tier": "Standard 0",
    "Devices": 1,
    "Hours": 1,
    "Additional messages (in millions)": 1
  }
}
```
