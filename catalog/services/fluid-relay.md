# Fluid Relay

- slug: `fluid-relay`  |  module: `fluid-relay-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (28): Central US, East US, East US 2, South Central US, West US 2, West US 3, UK South, UAE North, Switzerland North, Sweden Central, Poland Central, Norway East, Korea Central, Japan East, Italy North, ...

- **`Tier`** (select)
  - options: Basic, Standard

- **`Average number of users per session`** (number)

- **`Average number of operations sent per user per minute`** (number)

- **`Average session duration in minutes`** (number)

- **`Storage per session (MB)`** (number)

- **`Average number of sessions per month`** (number)

## Example component

```json
{
  "product": "Fluid Relay",
  "name": "my-fluid-relay",
  "fields": {
    "Region": "Central US",
    "Tier": "Basic",
    "Average number of users per session": 1,
    "Average number of operations sent per user per minute": 1,
    "Average session duration in minutes": 1
  }
}
```
