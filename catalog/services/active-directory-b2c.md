# Active Directory B2c

- slug: `active-directory-b2c`  |  module: `active-directory-b2c-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (49): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Premium P1, Premium P2

- **`Monthly Active Users`** (number)

- **`SMS/Phone Events`** (number)

## Example component

```json
{
  "product": "Active Directory B2c",
  "name": "my-active-directory-b2c",
  "fields": {
    "Region": "Central US",
    "Tier": "Premium P1",
    "Monthly Active Users": 1,
    "SMS/Phone Events": 1
  }
}
```
