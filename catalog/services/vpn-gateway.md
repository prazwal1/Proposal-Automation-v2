# Vpn Gateway

- slug: `vpn-gateway`  |  module: `vpn-gateway-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Type`** (select)
  - options: ExpressRoute Gateways, VPN Gateways

- **`Gateway Type`** (select)
  - depends on: `type`
  - options: Basic VPN, VpnGw1, VpnGw1AZ, VpnGw2, VpnGw2AZ, VpnGw3, VpnGw3AZ, VpnGw4, VpnGw4AZ, VpnGw5, VpnGw5AZ
  - when `type` = *ExpressRoute Gateways*: Standard, ErGw1AZ, High Performance, ErGw2AZ, Ultra Performance, ErGw3AZ

- **`Gateway hours`** (number)

- **`VPN Gateway type`** (select)
  - options: Inter-VNET, VPN

- **`GB`** (number)
  - depends on: `vpnType`

- **`interVnetUnits`** (select)
  - depends on: `vpnType`
  - options: GB, TB

- **`Additional S2S tunnels (beyond included amount)`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *VpnGw1*, `tier` = *VpnGw1AZ*, `tier` = *VpnGw2*, `tier` = *VpnGw2AZ*, `tier` = *VpnGw3*, `tier` = *VpnGw3AZ*

- **`Additional P2S connections (beyond included amount)`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *VpnGw1*, `tier` = *VpnGw1AZ*, `tier` = *VpnGw2*, `tier` = *VpnGw2AZ*, `tier` = *VpnGw3*, `tier` = *VpnGw3AZ*

- **`TB`** (number)
  - depends on: `interVnetUnits`
  - only exists when: `interVnetUnits` = *TB*

- **`TB (interVnetUnits)`** (select)
  - depends on: `interVnetUnits`
  - only exists when: `interVnetUnits` = *TB*
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
