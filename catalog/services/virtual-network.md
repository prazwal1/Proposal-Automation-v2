# Virtual Network

- slug: `virtual-network`  |  module: `virtual-network-module`

## Fields

- **`product-name`** (text)

- **`VNet 1 Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`VNet 2 Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`GB`** (number)
  - depends on: `vNet1PeeringFactor`
  - disappears when: `vNet1PeeringFactor` = *TB*

- **`vNet1PeeringFactor`** (select)
  - depends on: `vNet1PeeringFactor`
  - disappears when: `vNet1PeeringFactor` = *TB*
  - options: GB, TB

- **`vNet2Peering`** (number)
  - depends on: `vNet2PeeringFactor`
  - disappears when: `vNet2PeeringFactor` = *TB*

- **`vNet2PeeringFactor`** (select)
  - depends on: `vNet2PeeringFactor`
  - disappears when: `vNet2PeeringFactor` = *TB*
  - options: GB, TB

- **`TB`** (number)
  - depends on: `vNet1PeeringFactor`
  - only exists when: `vNet1PeeringFactor` = *TB*

- **`TB (vNet1PeeringFactor)`** (select)
  - depends on: `vNet1PeeringFactor`
  - only exists when: `vNet1PeeringFactor` = *TB*
  - options: GB, TB

- **`TB (vNet2Peering)`** (number)
  - depends on: `vNet2PeeringFactor`
  - only exists when: `vNet2PeeringFactor` = *TB*

- **`TB (vNet2PeeringFactor)`** (select)
  - depends on: `vNet2PeeringFactor`
  - only exists when: `vNet2PeeringFactor` = *TB*
  - options: GB, TB

## Example component

```json
{
  "product": "Virtual Network",
  "name": "my-virtual-network",
  "fields": {
    "VNet 1 Region": "Central US",
    "VNet 2 Region": "Central US",
    "GB": 1,
    "vNet1PeeringFactor": "GB",
    "vNet2Peering": 1
  }
}
```
