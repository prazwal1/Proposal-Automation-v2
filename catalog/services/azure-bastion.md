# Azure Bastion

- slug: `azure-bastion`  |  module: `azure-bastion-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (58): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Basic, Standard, Premium

- **`Hours`** (number)
  - depends on: `tier`

- **`basicHoursFactor`** (select)
  - depends on: `tier`
  - options: Hours, Days, Month

- **`GB`** (number)
  - depends on: `tier`

- **`basicOutboundDataTransferFactor`** (select)
  - depends on: `tier`
  - options: GB, TB

- **`Additional Scale Units`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`Days`** (number)
  - depends on: `basicHoursFactor`
  - only exists when: `basicHoursFactor` = *Days*

- **`Days (basicHoursFactor)`** (select)
  - depends on: `basicHoursFactor`
  - only exists when: `basicHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`TB`** (number)
  - depends on: `basicOutboundDataTransferFactor`
  - only exists when: `basicOutboundDataTransferFactor` = *TB*

- **`TB (basicOutboundDataTransferFactor)`** (select)
  - depends on: `basicOutboundDataTransferFactor`
  - only exists when: `basicOutboundDataTransferFactor` = *TB*
  - options: GB, TB

## Example component

```json
{
  "product": "Azure Bastion",
  "name": "my-azure-bastion",
  "fields": {
    "Region": "Central US",
    "Tier": "Basic",
    "Hours": 1,
    "basicHoursFactor": "Hours",
    "GB": 1
  }
}
```
