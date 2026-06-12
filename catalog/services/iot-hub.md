# Iot Hub

- slug: `iot-hub`  |  module: `iot-hub-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (51): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Basic, Standard

- **`Edition`** (select)
  - depends on: `tier`
  - options: Free: 500 devices, 8,000 msgs/day, S1: Unlimited devices, 400,000 msgs/day, S2: Unlimited devices, 6,000,000 msgs/day, S3: Unlimited devices, 300,000,000 msgs/day
  - when `tier` = *Basic*: B1: Unlimited devices, 400,000 msgs/day, B2: Unlimited devices, 6,000,000 msgs/day, B3: Unlimited devices, 300,000,000 msgs/day

- **`IoT Hub Units`** (number)

## Example component

```json
{
  "product": "Iot Hub",
  "name": "my-iot-hub",
  "fields": {
    "Region": "Central US",
    "Tier": "Basic",
    "Edition": "Free: 500 devices, 8,000 msgs/day",
    "IoT Hub Units": 1
  }
}
```
