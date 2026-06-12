# Frontdoor Standard Premium

- slug: `frontdoor-standard-premium`  |  module: `frontdoor-standard-premium-module`

## Fields

- **`product-name`** (text)

- **`Tier`** (select)
  - options: Azure Front Door (Classic), Azure Front Door Standard, Azure Front Door Premium

- **`Zone`** (select)
  - depends on: `tier`, `outboundDataTransferZones-0`
  - options: North America, Europe, Middle East and Africa, Asia Pacific (including Japan), South America, Australia, India
  - when `outboundDataTransferZones-0` = *Asia Pacific (including Japan)*: Asia Pacific (including Japan), North America, Europe, Middle East and Africa, South America, Australia, India
  - when `outboundDataTransferZones-0` = *South America*: South America, North America, Europe, Middle East and Africa, Asia Pacific (including Japan), Australia, India
  - when `outboundDataTransferZones-0` = *Australia*: Australia, North America, Europe, Middle East and Africa, Asia Pacific (including Japan), South America, India
  - when `outboundDataTransferZones-0` = *India*: India, North America, Europe, Middle East and Africa, Asia Pacific (including Japan), South America, Australia

- **`GB`** (number)
  - depends on: `tier`

- **`outboundDataTransferUnitsFactor-0`** (select)
  - depends on: `tier`
  - options: GB, TB

- **`inboundUnits`** (number)
  - depends on: `tier`, `inboundUnitsFactor`
  - disappears when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*, `inboundUnitsFactor` = *TB*

- **`inboundUnitsFactor`** (select)
  - depends on: `tier`, `inboundUnitsFactor`
  - disappears when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*, `inboundUnitsFactor` = *TB*
  - options: GB, TB

- **`Routing rules`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*

- **`Hours`** (number)
  - depends on: `tier`, `routingHoursFactor`
  - disappears when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*, `routingHoursFactor` = *Days*

- **`routingHoursFactor`** (select)
  - depends on: `tier`, `routingHoursFactor`
  - disappears when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*, `routingHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`additionalRoutingUnits`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*

- **`additionalRoutingHours`** (number)
  - depends on: `tier`, `additionalRoutingHoursFactor`
  - disappears when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*, `additionalRoutingHoursFactor` = *Days*

- **`additionalRoutingHoursFactor`** (select)
  - depends on: `tier`, `additionalRoutingHoursFactor`
  - disappears when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*, `additionalRoutingHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Domains`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*

- **`Policies`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*

- **`Rules`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*

- **`Requests processed (in millions)`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*

- **`Default Rulesets`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*

- **`managedRulesetRequests`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*

- **`x1,000 CAPTCHA sessions`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*

- **`x10,000 Requests`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Azure Front Door Standard*, `tier` = *Azure Front Door Premium*

- **`TB`** (number)
  - depends on: `outboundDataTransferUnitsFactor-0`
  - only exists when: `outboundDataTransferUnitsFactor-0` = *TB*

- **`TB (outboundDataTransferUnitsFactor-0)`** (select)
  - depends on: `outboundDataTransferUnitsFactor-0`
  - only exists when: `outboundDataTransferUnitsFactor-0` = *TB*
  - options: GB, TB

- **`TB (inboundUnits)`** (number)
  - depends on: `inboundUnitsFactor`
  - only exists when: `inboundUnitsFactor` = *TB*

- **`TB (inboundUnitsFactor)`** (select)
  - depends on: `inboundUnitsFactor`
  - only exists when: `inboundUnitsFactor` = *TB*
  - options: GB, TB

- **`Days`** (number)
  - depends on: `routingHoursFactor`
  - only exists when: `routingHoursFactor` = *Days*

- **`Days (routingHoursFactor)`** (select)
  - depends on: `routingHoursFactor`
  - only exists when: `routingHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (additionalRoutingHours)`** (number)
  - depends on: `additionalRoutingHoursFactor`
  - only exists when: `additionalRoutingHoursFactor` = *Days*

- **`Days (additionalRoutingHoursFactor)`** (select)
  - depends on: `additionalRoutingHoursFactor`
  - only exists when: `additionalRoutingHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Frontdoor Standard Premium",
  "name": "my-frontdoor-standard-premium",
  "fields": {
    "Tier": "Azure Front Door (Classic)",
    "Zone": "North America, Europe, Middle East and Africa",
    "GB": 1,
    "outboundDataTransferUnitsFactor-0": "GB",
    "inboundUnits": 1
  }
}
```
