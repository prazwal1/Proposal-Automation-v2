# Application Gateway

- slug: `application-gateway`  |  module: `application-gateway-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Basic V1, Web Application Firewall V1, Basic V2, Standard V2, Web Application Firewall V2, Application Gateway for Containers, Application Gateway for Containers with WAF

- **`Size`** (select)
  - depends on: `tier`
  - disappears when: `tier` = *Basic V2*, `tier` = *Standard V2*, `tier` = *Web Application Firewall V2*, `tier` = *Application Gateway for Containers*, `tier` = *Application Gateway for Containers with WAF*
  - options: Small, Medium, Large
  - when `tier` = *Web Application Firewall V1*: Medium, Large

- **`Instances`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Basic V2*, `tier` = *Standard V2*, `tier` = *Web Application Firewall V2*, `tier` = *Application Gateway for Containers*, `tier` = *Application Gateway for Containers with WAF*

- **`Hours`** (number)
  - depends on: `tier`

- **`hoursFactor`** (select)
  - depends on: `tier`
  - options: Hours, Days, Month

- **`GB`** (number)
  - depends on: `tier`, `processedUnits`
  - disappears when: `tier` = *Basic V2*, `tier` = *Standard V2*, `tier` = *Web Application Firewall V2*, `tier` = *Application Gateway for Containers*, `tier` = *Application Gateway for Containers with WAF*, `processedUnits` = *TB*

- **`processedUnits`** (select)
  - depends on: `tier`, `processedUnits`
  - disappears when: `tier` = *Basic V2*, `tier` = *Standard V2*, `tier` = *Web Application Firewall V2*, `tier` = *Application Gateway for Containers*, `tier` = *Application Gateway for Containers with WAF*, `processedUnits` = *TB*
  - options: GB, TB

- **`units`** (number)
  - depends on: `tier`, `storageUnits`
  - disappears when: `tier` = *Application Gateway for Containers*, `tier` = *Application Gateway for Containers with WAF*, `storageUnits` = *TB*

- **`storageUnits`** (select)
  - depends on: `tier`, `storageUnits`
  - disappears when: `tier` = *Application Gateway for Containers*, `tier` = *Application Gateway for Containers with WAF*, `storageUnits` = *TB*
  - options: GB, TB

- **`Compute unit(s)`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Basic V2*, `tier` = *Standard V2*, `tier` = *Web Application Firewall V2*

- **`Persistent Connection(s)`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Basic V2*, `tier` = *Standard V2*, `tier` = *Web Application Firewall V2*

- **`Throughput (mb/s)`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Basic V2*, `tier` = *Standard V2*, `tier` = *Web Application Firewall V2*

- **`Quantity`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Application Gateway for Containers*

- **`frontEndsInstances`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Application Gateway for Containers*

- **`associationInstances`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Application Gateway for Containers*

- **`capacityInstances`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Application Gateway for Containers*

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`TB`** (number)
  - depends on: `processedUnits`
  - only exists when: `processedUnits` = *TB*

- **`TB (processedUnits)`** (select)
  - depends on: `processedUnits`
  - only exists when: `processedUnits` = *TB*
  - options: GB, TB

- **`TB (units)`** (number)
  - depends on: `storageUnits`
  - only exists when: `storageUnits` = *TB*

- **`TB (storageUnits)`** (select)
  - depends on: `storageUnits`
  - only exists when: `storageUnits` = *TB*
  - options: GB, TB

## Example component

```json
{
  "product": "Application Gateway",
  "name": "my-application-gateway",
  "fields": {
    "Region": "Central US",
    "Tier": "Basic V1",
    "Size": "Small",
    "Instances": 1,
    "Hours": 1
  }
}
```
