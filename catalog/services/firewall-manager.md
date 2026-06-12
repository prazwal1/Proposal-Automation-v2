# Firewall Manager

- slug: `firewall-manager`  |  module: `firewall-manager-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (58): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Policy 1`** (text)

- **`Firewalls`** (number)

- **`Regions`** (number)

## Example component

```json
{
  "product": "Firewall Manager",
  "name": "my-firewall-manager",
  "fields": {
    "Region": "Central US",
    "Firewalls": 1,
    "Regions": 1
  }
}
```
