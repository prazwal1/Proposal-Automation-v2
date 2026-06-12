# Ddos Protection

- slug: `ddos-protection`  |  module: `ddos-protection-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (49): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Sweden Central, Spain Central, ...

- **`Tier`** (select)
  - options: Network Protection, IP Protection

- **`Additional IP Resources`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *IP Protection*

- **`IP Resources`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *IP Protection*

- **`Hours`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *IP Protection*

- **`hoursFactor`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *IP Protection*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Ddos Protection",
  "name": "my-ddos-protection",
  "fields": {
    "Region": "Central US",
    "Tier": "Network Protection",
    "Additional IP Resources": 1
  }
}
```
