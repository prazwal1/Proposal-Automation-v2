# Time Series Insights

- slug: `time-series-insights`  |  module: `time-series-insights-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (23): Central US, East US, East US 2, South Central US, West Central US, West US, West US 2, UK South, UK West, Sweden Central, Norway East, Japan West, Central India, Germany North, Germany West Central, ...

- **`Tier`** (select)
  - options: S1: 1,000,000 msgs/day, S2: 10,000,000 msgs/day

- **`Units`** (number)

## Example component

```json
{
  "product": "Time Series Insights",
  "name": "my-time-series-insights",
  "fields": {
    "Region": "Central US",
    "Tier": "S1: 1,000,000 msgs/day",
    "Units": 1
  }
}
```
