# Azure Maps

- slug: `azure-maps`  |  module: `azure-maps-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (48): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Pricing Tier`** (select)
  - options: Gen 1, Gen 2

- **`x 1,000 Map Tile Transactions`** (number)
  - depends on: `pricingTier`
  - disappears when: `pricingTier` = *Gen 1*

- **`x 1,000 Traffic Tile Transactions`** (number)
  - depends on: `pricingTier`
  - disappears when: `pricingTier` = *Gen 1*

- **`x 1,000 Weather Tile Transactions`** (number)
  - depends on: `pricingTier`
  - disappears when: `pricingTier` = *Gen 1*

- **`x 1,000 Imagery Tile Transactions`** (number)
  - depends on: `pricingTier`
  - disappears when: `pricingTier` = *Gen 1*

- **`x 1,000 Static Map Image Transactions`** (number)
  - depends on: `pricingTier`
  - disappears when: `pricingTier` = *Gen 1*

- **`x 1,000 Search Transactions`** (number)
  - depends on: `pricingTier`
  - disappears when: `pricingTier` = *Gen 1*

- **`x 1,000 Route Transactions`** (number)
  - depends on: `pricingTier`
  - disappears when: `pricingTier` = *Gen 1*

- **`x 1,000 Traffic Data Transactions`** (number)
  - depends on: `pricingTier`
  - disappears when: `pricingTier` = *Gen 1*

- **`x 1,000 Time Zone Transactions`** (number)
  - depends on: `pricingTier`
  - disappears when: `pricingTier` = *Gen 1*

- **`x 1,000 Geolocation Transactions`** (number)
  - depends on: `pricingTier`
  - disappears when: `pricingTier` = *Gen 1*

- **`x 1,000 Weather Service Transactions`** (number)
  - depends on: `pricingTier`
  - disappears when: `pricingTier` = *Gen 1*

- **`x 1,000 Spatial Operation Transactions`** (number)
  - depends on: `pricingTier`
  - disappears when: `pricingTier` = *Gen 1*

- **`x 1,000 Data Upload Transactions`** (number)
  - depends on: `pricingTier`
  - disappears when: `pricingTier` = *Gen 1*

## Example component

```json
{
  "product": "Azure Maps",
  "name": "my-azure-maps",
  "fields": {
    "Region": "Central US",
    "Pricing Tier": "Gen 1",
    "x 1,000 Map Tile Transactions": 1,
    "x 1,000 Traffic Tile Transactions": 1,
    "x 1,000 Weather Tile Transactions": 1
  }
}
```
