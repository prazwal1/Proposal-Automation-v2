# Scheduler

- slug: `scheduler`  |  module: `scheduler-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (29): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, UK South, UK West, Korea Central, Korea South, Japan East, Japan West, Central India, ...

- **`Tier`** (select)
  - options: Standard, P10 Premium, P20 Premium

- **`Units`** (number)

## Example component

```json
{
  "product": "Scheduler",
  "name": "my-scheduler",
  "fields": {
    "Region": "Central US",
    "Tier": "Standard",
    "Units": 1
  }
}
```
