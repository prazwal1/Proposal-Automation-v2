# Defender Easm

- slug: `defender-easm`  |  module: `defender-easm-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (28): Central US, East US, East US 2, North Central US, South Central US, West US, West US 2, West US 3, UK South, UAE North, Switzerland North, Sweden Central, Norway East, New Zealand North, Malaysia West, ...

- **`IP Addresses`** (number)

- **`Days per month`** (number)

- **`Domains`** (number)

- **`daysPerMonthDomains`** (number)

- **`Hosts`** (number)

- **`daysPerMonthHosts`** (number)

## Example component

```json
{
  "product": "Defender Easm",
  "name": "my-defender-easm",
  "fields": {
    "Region": "Central US",
    "IP Addresses": 1,
    "Days per month": 1,
    "Domains": 1,
    "daysPerMonthDomains": 1
  }
}
```
