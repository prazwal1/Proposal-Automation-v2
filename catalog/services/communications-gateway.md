# Communications Gateway

- slug: `communications-gateway`  |  module: `communications-gateway-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (57): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Type`** (select)
  - options: Fixed Network, Mobile Network

- **`Users per month`** (number)

## Example component

```json
{
  "product": "Communications Gateway",
  "name": "my-communications-gateway",
  "fields": {
    "Region": "Central US",
    "Type": "Fixed Network",
    "Users per month": 1
  }
}
```
