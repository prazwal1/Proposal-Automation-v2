# Web Pubsub

- slug: `web-pubsub`  |  module: `web-pubsub-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (55): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Free, Standard, Premium

- **`Units`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*, `tier` = *Premium*

- **`Hours`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*, `tier` = *Premium*

- **`hoursFactor`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*, `tier` = *Premium*
  - options: Hours, Days, Month

- **`x1 million KiB of Outbound Traffic`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*, `tier` = *Premium*

## Example component

```json
{
  "product": "Web Pubsub",
  "name": "my-web-pubsub",
  "fields": {
    "Region": "Central US",
    "Tier": "Free"
  }
}
```
