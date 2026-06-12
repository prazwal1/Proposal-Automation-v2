# Iot Operations

- slug: `iot-operations`  |  module: `iot-operations-module`

## Fields

- **`product-name`** (text)

- **`Node(s) on which Azure IoT Operations is deployed`** (number)

- **`Hours`** (number)
  - depends on: `nodeHoursFactor`
  - disappears when: `nodeHoursFactor` = *Days*

- **`nodeHoursFactor`** (select)
  - depends on: `nodeHoursFactor`
  - disappears when: `nodeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Number of assets`** (number)

- **`assetHours`** (number)
  - depends on: `assetHoursFactor`
  - disappears when: `assetHoursFactor` = *Days*

- **`assetHoursFactor`** (select)
  - depends on: `assetHoursFactor`
  - disappears when: `assetHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `nodeHoursFactor`
  - only exists when: `nodeHoursFactor` = *Days*

- **`Days (nodeHoursFactor)`** (select)
  - depends on: `nodeHoursFactor`
  - only exists when: `nodeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (assetHours)`** (number)
  - depends on: `assetHoursFactor`
  - only exists when: `assetHoursFactor` = *Days*

- **`Days (assetHoursFactor)`** (select)
  - depends on: `assetHoursFactor`
  - only exists when: `assetHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Iot Operations",
  "name": "my-iot-operations",
  "fields": {
    "Node(s) on which Azure IoT Operations is deployed": 1,
    "Hours": 1,
    "nodeHoursFactor": "Hours",
    "Number of assets": 1,
    "assetHours": 1
  }
}
```
