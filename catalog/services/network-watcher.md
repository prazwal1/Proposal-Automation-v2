# Network Watcher

- slug: `network-watcher`  |  module: `network-watcher-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (58): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Expected Usage (GB)`** (number)

- **`Expected Usage (Checks)`** (number)

- **`Expected networks connections`** (number)

- **`DNS or App Gateway servers monitored`** (number)

- **`Average logs ingested per server (GB)`** (number)

- **`Logs collected (GB)`** (number)

- **`trafficAnalyticsAcceleratedLogs`** (number)

## Example component

```json
{
  "product": "Network Watcher",
  "name": "my-network-watcher",
  "fields": {
    "Region": "Central US",
    "Expected Usage (GB)": 1,
    "Expected Usage (Checks)": 1,
    "Expected networks connections": 1,
    "DNS or App Gateway servers monitored": 1
  }
}
```
