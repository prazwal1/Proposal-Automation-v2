# Virtual Network Manager

- slug: `virtual-network-manager`  |  module: `virtual-network-manager-module`

## Fields

- **`product-name`** (text)

- **`Deployed Configurations`** (select)
  - options: Virtual Network-based billing, Subscription-based billing

- **`Number of managed virtual networks`** (number)
  - depends on: `deployedConfiguration`
  - disappears when: `deployedConfiguration` = *Subscription-based billing*

- **`Hours`** (number)
  - depends on: `deployedConfiguration`

- **`virtualNetworkHoursFactor`** (select)
  - depends on: `deployedConfiguration`
  - options: Hours, Days, Month

- **`Reachability analysis runs`** (number)

- **`Number of managed IPs`** (number)

- **`ipsHours`** (number)
  - depends on: `ipsHoursFactor`
  - disappears when: `ipsHoursFactor` = *Days*

- **`ipsHoursFactor`** (select)
  - depends on: `ipsHoursFactor`
  - disappears when: `ipsHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Number of managed subscriptions`** (number)
  - depends on: `deployedConfiguration`
  - only exists when: `deployedConfiguration` = *Subscription-based billing*

- **`Days`** (number)
  - depends on: `virtualNetworkHoursFactor`
  - only exists when: `virtualNetworkHoursFactor` = *Days*

- **`Days (virtualNetworkHoursFactor)`** (select)
  - depends on: `virtualNetworkHoursFactor`
  - only exists when: `virtualNetworkHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (ipsHours)`** (number)
  - depends on: `ipsHoursFactor`
  - only exists when: `ipsHoursFactor` = *Days*

- **`Days (ipsHoursFactor)`** (select)
  - depends on: `ipsHoursFactor`
  - only exists when: `ipsHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Virtual Network Manager",
  "name": "my-virtual-network-manager",
  "fields": {
    "Deployed Configurations": "Virtual Network-based billing",
    "Number of managed virtual networks": 1,
    "Hours": 1,
    "virtualNetworkHoursFactor": "Hours",
    "Reachability analysis runs": 1
  }
}
```
