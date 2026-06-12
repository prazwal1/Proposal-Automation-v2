# Expressroute

- slug: `expressroute`  |  module: `expressroute-module`

## Fields

- **`product-name`** (text)

- **`Product`** (select)
  - options: ExpressRoute, ExpressRoute Direct, ExpressRoute Metro

- **`Zone`** (select)
  - options: Zone 1, Zone 2, Zone 3, Zone 4, US Gov Zone 1

- **`SKU`** (select)
  - depends on: `product`
  - options: Local, Standard, Premium
  - when `product` = *ExpressRoute Direct*: Premium
  - when `product` = *ExpressRoute Metro*: Premium

- **`Data plan`** (select)
  - depends on: `product`, `skuSelection`
  - disappears when: `skuSelection` = *Local*
  - options: Metered, Unlimited
  - when `product` = *ExpressRoute Metro*: Metered

- **`Circuit speed`** (select)
  - depends on: `product`, `zone`, `skuSelection`
  - options: 50 Mbps, 100 Mbps, 200 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps
  - when `zone` = *Zone 2*: 50 Mbps, 100 Mbps, 200 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps
  - when `zone` = *Zone 3*: 50 Mbps, 100 Mbps, 200 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps
  - when `zone` = *Zone 4*: 50 Mbps, 100 Mbps, 200 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps
  - when `zone` = *US Gov Zone 1*: 50 Mbps, 100 Mbps, 200 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps
  - when `skuSelection` = *Local*: 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps
  - when `skuSelection` = *Premium*: 50 Mbps, 100 Mbps, 200 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps

- **`Circuit(s)`** (number)
  - depends on: `product`

- **`GB`** (number)
  - depends on: `skuSelection`, `storageUnits`
  - disappears when: `skuSelection` = *Local*, `skuSelection` = *Premium*, `storageUnits` = *TB*

- **`storageUnits`** (select)
  - depends on: `skuSelection`, `storageUnits`
  - disappears when: `skuSelection` = *Local*, `skuSelection` = *Premium*, `storageUnits` = *TB*
  - options: GB, TB

- **`ExpressRoute Gateways`** (select)
  - options: Virtual Network Gateways, Availability Zones, Scalable Gateway

- **`Gateway Type`** (select)
  - depends on: `gatewayValue`
  - options: Standard VNet Gateway, High Performance VNet Gateway, Ultra Performance VNet Gateway
  - when `gatewayValue` = *Availability Zones*: ErGw1AZ, ErGw2AZ, ErGw3AZ
  - when `gatewayValue` = *Scalable Gateway*: ErGwScale

- **`Region`** (select)
  - options (59): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Hours`** (number)
  - depends on: `expressRouteGatewayHoursFactor`
  - disappears when: `expressRouteGatewayHoursFactor` = *Days*

- **`expressRouteGatewayHoursFactor`** (select)
  - depends on: `expressRouteGatewayHoursFactor`
  - disappears when: `expressRouteGatewayHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Port pair speed`** (select)
  - depends on: `product`
  - only exists when: `product` = *ExpressRoute Direct*
  - options: 10 Gbps, 100 Gbps, 400 Gbps

- **`TB`** (number)
  - depends on: `storageUnits`
  - only exists when: `storageUnits` = *TB*

- **`TB (storageUnits)`** (select)
  - depends on: `storageUnits`
  - only exists when: `storageUnits` = *TB*
  - options: GB, TB

- **`Gbps`** (number)
  - depends on: `gatewayValue`
  - only exists when: `gatewayValue` = *Scalable Gateway*

- **`scalableBandwidthFactor`** (select)
  - depends on: `gatewayValue`
  - only exists when: `gatewayValue` = *Scalable Gateway*
  - options: Gbps

- **`Days`** (number)
  - depends on: `expressRouteGatewayHoursFactor`
  - only exists when: `expressRouteGatewayHoursFactor` = *Days*

- **`Days (expressRouteGatewayHoursFactor)`** (select)
  - depends on: `expressRouteGatewayHoursFactor`
  - only exists when: `expressRouteGatewayHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Expressroute",
  "name": "my-expressroute",
  "fields": {
    "Product": "ExpressRoute",
    "Zone": "Zone 1",
    "SKU": "Local",
    "Data plan": "Metered",
    "Circuit speed": "50 Mbps"
  }
}
```
