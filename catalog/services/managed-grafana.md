# Managed Grafana

- slug: `managed-grafana`  |  module: `managed-grafana-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (32): Central US, East US, East US 2, South Central US, West Central US, West US, West US 2, West US 3, UK South, UAE North, Switzerland North, Sweden Central, Norway East, Korea Central, Japan East, ...

- **`Pricing Plan`** (select)
  - options: Standard, Essential

- **`Hours`** (number)
  - depends on: `pricingPlan`, `nodeHoursFactor`
  - disappears when: `pricingPlan` = *Essential*, `nodeHoursFactor` = *Days*

- **`nodeHoursFactor`** (select)
  - depends on: `pricingPlan`, `nodeHoursFactor`
  - disappears when: `pricingPlan` = *Essential*, `nodeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Active Users`** (number)

- **`Days`** (number)
  - depends on: `nodeHoursFactor`
  - only exists when: `nodeHoursFactor` = *Days*

- **`Days (nodeHoursFactor)`** (select)
  - depends on: `nodeHoursFactor`
  - only exists when: `nodeHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Managed Grafana",
  "name": "my-managed-grafana",
  "fields": {
    "Region": "Central US",
    "Pricing Plan": "Standard",
    "Hours": 1,
    "nodeHoursFactor": "Hours",
    "Active Users": 1
  }
}
```
