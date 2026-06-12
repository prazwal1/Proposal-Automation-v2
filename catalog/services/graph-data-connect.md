# Graph Data Connect

- slug: `graph-data-connect`  |  module: `graph-data-connect-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (57): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Scenario`** (select)
  - options: Ad-hoc Use​, Once Backfill And Monthly Incremental​, Monthly incremental recurring

- **`Number of users, sites, etc.`** (number)

- **`avgNumberOfEXOEmails`** (number)

- **`Average number of EXO Calendar Events per day per scope​`** (number)

- **`avgNumberOfTeamsChat`** (number)

- **`Average number of Teams Call Records per day per user​`** (number)

- **`Average number of ODSP File per day per user​`** (number)

- **`Average number of Tasks and Lists per day per user`** (number)

- **`Duration of dataset (days) per billing period`** (number)

## Example component

```json
{
  "product": "Graph Data Connect",
  "name": "my-graph-data-connect",
  "fields": {
    "Region": "Central US",
    "Scenario": "Ad-hoc Use\u200b",
    "Number of users, sites, etc.": 1,
    "avgNumberOfEXOEmails": 1,
    "Average number of EXO Calendar Events per day per scope\u200b": 1
  }
}
```
