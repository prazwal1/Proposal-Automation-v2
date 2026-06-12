# Traffic Manager

- slug: `traffic-manager`  |  module: `traffic-manager-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Million/month`** (number)

- **`Endpoints`** (number)

- **`fastAzureChecks`** (number)

- **`externalChecks`** (number)

- **`fastExternalChecks`** (number)

- **`Million measurements`** (number)

- **`Million data points processed`** (number)

## Example component

```json
{
  "product": "Traffic Manager",
  "name": "my-traffic-manager",
  "fields": {
    "Region": "Central US",
    "Million/month": 1,
    "Endpoints": 1,
    "fastAzureChecks": 1,
    "externalChecks": 1
  }
}
```
