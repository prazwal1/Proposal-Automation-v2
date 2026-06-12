# Stream Analytics

- slug: `stream-analytics`  |  module: `stream-analytics-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Type`** (select)
  - options: Standard, Dedicated, Standard V2, Dedicated V2

- **`Streaming Unit(s)`** (number)

- **`Hours`** (number)
  - depends on: `streamingHoursFactor`
  - disappears when: `streamingHoursFactor` = *Days*

- **`streamingHoursFactor`** (select)
  - depends on: `streamingHoursFactor`
  - disappears when: `streamingHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Devices`** (number)

- **`Range`** (select)
  - depends on: `type`
  - only exists when: `type` = *Standard V2*
  - options: 1 or more Streaming Unit(s), Less than 1 Streaming Unit

- **`Days`** (number)
  - depends on: `streamingHoursFactor`
  - only exists when: `streamingHoursFactor` = *Days*

- **`Days (streamingHoursFactor)`** (select)
  - depends on: `streamingHoursFactor`
  - only exists when: `streamingHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Stream Analytics",
  "name": "my-stream-analytics",
  "fields": {
    "Region": "Central US",
    "Type": "Standard",
    "Streaming Unit(s)": 1,
    "Hours": 1,
    "streamingHoursFactor": "Hours"
  }
}
```
