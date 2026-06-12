# Private Link

- slug: `private-link`  |  module: `private-link-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Endpoints`** (number)

- **`Hours`** (number)
  - depends on: `privateEndpointHoursFactor`
  - disappears when: `privateEndpointHoursFactor` = *Days*

- **`privateEndpointHoursFactor`** (select)
  - depends on: `privateEndpointHoursFactor`
  - disappears when: `privateEndpointHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`GB`** (number)
  - depends on: `outboundDataFactor`
  - disappears when: `outboundDataFactor` = *TB*

- **`outboundDataFactor`** (select)
  - depends on: `outboundDataFactor`
  - disappears when: `outboundDataFactor` = *TB*
  - options: GB, TB

- **`inboundDataUnits`** (number)
  - depends on: `inboundDataFactor`
  - disappears when: `inboundDataFactor` = *TB*

- **`inboundDataFactor`** (select)
  - depends on: `inboundDataFactor`
  - disappears when: `inboundDataFactor` = *TB*
  - options: GB, TB

- **`Days`** (number)
  - depends on: `privateEndpointHoursFactor`
  - only exists when: `privateEndpointHoursFactor` = *Days*

- **`Days (privateEndpointHoursFactor)`** (select)
  - depends on: `privateEndpointHoursFactor`
  - only exists when: `privateEndpointHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`TB`** (number)
  - depends on: `outboundDataFactor`
  - only exists when: `outboundDataFactor` = *TB*

- **`TB (outboundDataFactor)`** (select)
  - depends on: `outboundDataFactor`
  - only exists when: `outboundDataFactor` = *TB*
  - options: GB, TB

- **`TB (inboundDataUnits)`** (number)
  - depends on: `inboundDataFactor`
  - only exists when: `inboundDataFactor` = *TB*

- **`TB (inboundDataFactor)`** (select)
  - depends on: `inboundDataFactor`
  - only exists when: `inboundDataFactor` = *TB*
  - options: GB, TB

## Example component

```json
{
  "product": "Private Link",
  "name": "my-private-link",
  "fields": {
    "Region": "Central US",
    "Endpoints": 1,
    "Hours": 1,
    "privateEndpointHoursFactor": "Hours",
    "GB": 1
  }
}
```
