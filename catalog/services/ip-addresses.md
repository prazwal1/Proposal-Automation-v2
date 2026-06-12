# Ip Addresses

- slug: `ip-addresses`  |  module: `ip-addresses-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Type`** (select)
  - options: Basic (ARM), Basic (Classic), Global (ARM), Standard (ARM)

- **`Addresses`** (number)
  - depends on: `type`

- **`Hours`** (number)
  - depends on: `type`

- **`dynamicAddressHoursFactor`** (select)
  - depends on: `type`
  - options: Hours, Days, Month

- **`staticAddresses`** (number)

- **`staticAddressHours`** (number)
  - depends on: `staticAddressHoursFactor`
  - disappears when: `staticAddressHoursFactor` = *Days*

- **`staticAddressHoursFactor`** (select)
  - depends on: `staticAddressHoursFactor`
  - disappears when: `staticAddressHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `dynamicAddressHoursFactor`
  - only exists when: `dynamicAddressHoursFactor` = *Days*

- **`Days (dynamicAddressHoursFactor)`** (select)
  - depends on: `dynamicAddressHoursFactor`
  - only exists when: `dynamicAddressHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (staticAddressHours)`** (number)
  - depends on: `staticAddressHoursFactor`
  - only exists when: `staticAddressHoursFactor` = *Days*

- **`Days (staticAddressHoursFactor)`** (select)
  - depends on: `staticAddressHoursFactor`
  - only exists when: `staticAddressHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Ip Addresses",
  "name": "my-ip-addresses",
  "fields": {
    "Region": "Central US",
    "Type": "Basic (ARM)",
    "Addresses": 1,
    "Hours": 1,
    "dynamicAddressHoursFactor": "Hours"
  }
}
```
