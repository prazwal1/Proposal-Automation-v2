# Advanced Container Networking Services

- slug: `advanced-container-networking-services`  |  module: `advanced-container-networking-services-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (57): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`User Nodes`** (number)

- **`Hours`** (number)
  - depends on: `userNodeHoursFactor`
  - disappears when: `userNodeHoursFactor` = *Days*

- **`userNodeHoursFactor`** (select)
  - depends on: `userNodeHoursFactor`
  - disappears when: `userNodeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `userNodeHoursFactor`
  - only exists when: `userNodeHoursFactor` = *Days*

- **`Days (userNodeHoursFactor)`** (select)
  - depends on: `userNodeHoursFactor`
  - only exists when: `userNodeHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Advanced Container Networking Services",
  "name": "my-advanced-container-networking-services",
  "fields": {
    "Region": "Central US",
    "User Nodes": 1,
    "Hours": 1,
    "userNodeHoursFactor": "Hours"
  }
}
```
