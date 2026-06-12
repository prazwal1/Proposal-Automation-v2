# Update Management Center

- slug: `update-management-center`  |  module: `update-management-center-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Service Type`** (select)
  - options: Azure, Arc-enabled

- **`Servers`** (number)
  - depends on: `serviceType`
  - only exists when: `serviceType` = *Arc-enabled*

## Example component

```json
{
  "product": "Update Management Center",
  "name": "my-update-management-center",
  "fields": {
    "Region": "Central US",
    "Service Type": "Azure"
  }
}
```
