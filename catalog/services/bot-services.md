# Bot Services

- slug: `bot-services`  |  module: `bot-services-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Free, S1

- **`Messages (in thousands)`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *S1*

## Example component

```json
{
  "product": "Bot Services",
  "name": "my-bot-services",
  "fields": {
    "Region": "Central US",
    "Tier": "Free"
  }
}
```
