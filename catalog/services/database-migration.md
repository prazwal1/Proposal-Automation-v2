# Database Migration

- slug: `database-migration`  |  module: `database-migration-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (39): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, UK South, UK West, UAE Central, UAE North, Korea Central, Korea South, Japan East, ...

- **`Pricing Tier`** (select)
  - options: Standard, Premium

- **`Instance`** (select)
  - depends on: `pricingTier`
  - disappears when: `pricingTier` = *Standard*
  - options: 4 vCore

- **`Instances`** (number)
  - depends on: `pricingTier`
  - disappears when: `pricingTier` = *Standard*

- **`Hours`** (number)
  - depends on: `pricingTier`, `hoursFactor`
  - disappears when: `pricingTier` = *Standard*, `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `pricingTier`, `hoursFactor`
  - disappears when: `pricingTier` = *Standard*, `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Database Migration",
  "name": "my-database-migration",
  "fields": {
    "Region": "Central US",
    "Pricing Tier": "Standard",
    "Instance": "4 vCore",
    "Instances": 1,
    "Hours": 1
  }
}
```
