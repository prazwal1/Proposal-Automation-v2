# Vpn Gateway

- slug: `vpn-gateway`  |  module: `vpn-gateway-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Type`** (select)
  - options: ExpressRoute Gateways, VPN Gateways

- **`Gateway Type`** (select)
  - depends on: `type`, `tier`, `vpnType`, `interVnetUnits`
  - options: Basic VPN, VpnGw1, VpnGw1AZ, VpnGw2, VpnGw2AZ, VpnGw3, VpnGw3AZ, VpnGw4, VpnGw4AZ, VpnGw5, VpnGw5AZ
  - when `type` = *ExpressRoute Gateways*: Standard, ErGw1AZ, High Performance, ErGw2AZ, Ultra Performance, ErGw3AZ

- **`Gateway hours`** (number)

- **`VPN Gateway type`** (select)
  - options: Inter-VNET, VPN

- **`GB`** (number)
  - depends on: `vpnType`, `type`, `interVnetUnits`, `tier`
  - only exists when: `interVnetUnits` = *GB* and `type` = *ExpressRoute Gateways*, `interVnetUnits` = *GB* and `tier` = *VpnGw1AZ*, `interVnetUnits` = *GB* and `tier` = *VpnGw2AZ*, `interVnetUnits` = *GB* and `tier` = *VpnGw3AZ*, `interVnetUnits` = *GB* and `tier` = *VpnGw4AZ*, `interVnetUnits` = *GB* and `tier` = *VpnGw5AZ*

- **`interVnetUnits`** (select)
  - depends on: `vpnType`, `type`, `interVnetUnits`, `tier`
  - only exists when: `interVnetUnits` = *GB* and `type` = *ExpressRoute Gateways*, `interVnetUnits` = *GB* and `tier` = *VpnGw1AZ*, `interVnetUnits` = *GB* and `tier` = *VpnGw2AZ*, `interVnetUnits` = *GB* and `tier` = *VpnGw3AZ*, `interVnetUnits` = *GB* and `tier` = *VpnGw4AZ*, `interVnetUnits` = *GB* and `tier` = *VpnGw5AZ*
  - options: GB, TB

- **`Additional S2S tunnels (beyond included amount)`** (number)
  - depends on: `tier`, `type`, `vpnType`, `interVnetUnits`
  - only exists when: `tier` = *VpnGw1*, `tier` = *VpnGw1AZ*, `tier` = *VpnGw2*, `tier` = *VpnGw2AZ*, `tier` = *VpnGw3*, `tier` = *VpnGw3AZ*
  - disappears when: `type` = *ExpressRoute Gateways* and `tier` = *VpnGw1*, `type` = *ExpressRoute Gateways* and `tier` = *VpnGw1AZ*, `type` = *ExpressRoute Gateways* and `tier` = *VpnGw2*, `type` = *ExpressRoute Gateways* and `tier` = *VpnGw2AZ*, `type` = *ExpressRoute Gateways* and `tier` = *VpnGw3*, `type` = *ExpressRoute Gateways* and `tier` = *VpnGw3AZ*

- **`Additional P2S connections (beyond included amount)`** (number)
  - depends on: `tier`, `type`, `vpnType`, `interVnetUnits`
  - only exists when: `tier` = *VpnGw1*, `tier` = *VpnGw1AZ*, `tier` = *VpnGw2*, `tier` = *VpnGw2AZ*, `tier` = *VpnGw3*, `tier` = *VpnGw3AZ*
  - disappears when: `type` = *ExpressRoute Gateways* and `tier` = *VpnGw1*, `type` = *ExpressRoute Gateways* and `tier` = *VpnGw1AZ*, `type` = *ExpressRoute Gateways* and `tier` = *VpnGw2*, `type` = *ExpressRoute Gateways* and `tier` = *VpnGw2AZ*, `type` = *ExpressRoute Gateways* and `tier` = *VpnGw3*, `type` = *ExpressRoute Gateways* and `tier` = *VpnGw3AZ*

- **`TB`** (number)
  - depends on: `interVnetUnits`, `type`, `vpnType`, `tier`, `bandwidthUnits`
  - only exists when: `interVnetUnits` = *TB*
  - disappears when: `vpnType` = *VPN* and `type` = *ExpressRoute Gateways*, `interVnetUnits` = *GB* and `type` = *ExpressRoute Gateways*, `vpnType` = *VPN* and `tier` = *VpnGw1AZ*, `interVnetUnits` = *GB* and `tier` = *VpnGw1AZ*, `vpnType` = *VPN* and `tier` = *VpnGw2AZ*, `interVnetUnits` = *GB* and `tier` = *VpnGw2AZ*

- **`TB (interVnetUnits)`** (select)
  - depends on: `interVnetUnits`, `type`, `vpnType`, `tier`, `bandwidthUnits`
  - only exists when: `interVnetUnits` = *TB*
  - disappears when: `vpnType` = *VPN* and `type` = *ExpressRoute Gateways*, `interVnetUnits` = *GB* and `type` = *ExpressRoute Gateways*, `vpnType` = *VPN* and `tier` = *VpnGw1AZ*, `interVnetUnits` = *GB* and `tier` = *VpnGw1AZ*, `vpnType` = *VPN* and `tier` = *VpnGw2AZ*, `interVnetUnits` = *GB* and `tier` = *VpnGw2AZ*
  - options: GB, TB

## Example component

```json
{
  "product": "Vpn Gateway",
  "name": "my-vpn-gateway",
  "fields": {
    "Region": "Central US",
    "Type": "ExpressRoute Gateways",
    "Gateway Type": "Basic VPN",
    "Gateway hours": 1,
    "VPN Gateway type": "Inter-VNET"
  }
}
```
