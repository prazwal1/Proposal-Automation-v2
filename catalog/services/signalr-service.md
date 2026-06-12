# Signalr Service

- slug: `signalr-service`  |  module: `signalr-service-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (44): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE North, Switzerland North, Switzerland West, Sweden Central, ...

- **`Tier`** (select)
  - options: Free, Standard, Premium

- **`Units`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*, `tier` = *Premium*

- **`Days`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*, `tier` = *Premium*

- **`Million messages`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*, `tier` = *Premium*

## Example component

```json
{
  "product": "Signalr Service",
  "name": "my-signalr-service",
  "fields": {
    "Region": "Central US",
    "Tier": "Free"
  }
}
```
