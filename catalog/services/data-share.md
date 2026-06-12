# Data Share

- slug: `data-share`  |  module: `data-share-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (23): Central US, East US, East US 2, South Central US, West US, West US 2, UK South, UAE North, Switzerland North, Japan East, Central India, Germany West Central, France Central, North Europe, West Europe, ...

- **`dataset-snapshot(s)`** (number)

- **`vCore(s)`** (number)

- **`Hours`** (number)
  - depends on: `datasetMovementHoursFactor`
  - disappears when: `datasetMovementHoursFactor` = *Days*

- **`datasetMovementHoursFactor`** (select)
  - depends on: `datasetMovementHoursFactor`
  - disappears when: `datasetMovementHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `datasetMovementHoursFactor`
  - only exists when: `datasetMovementHoursFactor` = *Days*

- **`Days (datasetMovementHoursFactor)`** (select)
  - depends on: `datasetMovementHoursFactor`
  - only exists when: `datasetMovementHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Data Share",
  "name": "my-data-share",
  "fields": {
    "Region": "Central US",
    "dataset-snapshot(s)": 1,
    "vCore(s)": 1,
    "Hours": 1,
    "datasetMovementHoursFactor": "Hours"
  }
}
```
