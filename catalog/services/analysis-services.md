# Analysis Services

- slug: `analysis-services`  |  module: `analysis-services-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (22): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, UK South, Mexico Central, Japan East, West India, North Europe, West Europe, Canada Central, ...

- **`Instance`** (select)
  - options: Developer (Hours): 10 QPU, 3 GB, Basic B1 (Hours): 40 QPU, 10 GB, Basic B2 (Hours): 80 QPU, 16 GB, Standard S0 (Hours): 40 QPU, 10 GB, Standard S1 (Hours): 100 QPU, 25 GB, Standard S2 (Hours): 200 QPU, 50 GB, Standard S4 (Hours): 400 QPU, 100 GB

- **`Instances`** (number)

- **`Hours`** (number)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Analysis Services",
  "name": "my-analysis-services",
  "fields": {
    "Region": "Central US",
    "Instance": "Developer (Hours): 10 QPU, 3 GB",
    "Instances": 1,
    "Hours": 1,
    "hoursFactor": "Hours"
  }
}
```
