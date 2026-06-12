# Remote Rendering

- slug: `remote-rendering`  |  module: `remote-rendering-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options: East US, East US 2, South Central US, West US 2, UK South, Japan East, North Europe, West Europe, Australia East, Southeast Asia

- **`Tier`** (select)
  - options: Premium, Standard

- **`Device`** (number)

- **`Hours`** (number)
  - depends on: `sessionsHoursFactor`
  - disappears when: `sessionsHoursFactor` = *Days*

- **`sessionsHoursFactor`** (select)
  - depends on: `sessionsHoursFactor`
  - disappears when: `sessionsHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Conversion`** (number)

- **`Days`** (number)
  - depends on: `sessionsHoursFactor`
  - only exists when: `sessionsHoursFactor` = *Days*

- **`Days (sessionsHoursFactor)`** (select)
  - depends on: `sessionsHoursFactor`
  - only exists when: `sessionsHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Remote Rendering",
  "name": "my-remote-rendering",
  "fields": {
    "Region": "East US",
    "Tier": "Premium",
    "Device": 1,
    "Hours": 1,
    "sessionsHoursFactor": "Hours"
  }
}
```
