# Container Instances

- slug: `container-instances`  |  module: `container-instances-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Operating system`** (select)
  - options: Linux, Windows

- **`containerGroups`** (number)

- **`Seconds`** (number)
  - depends on: `durationUnitsFactor`
  - disappears when: `durationUnitsFactor` = *Minutes*

- **`durationUnitsFactor`** (select)
  - depends on: `durationUnitsFactor`
  - disappears when: `durationUnitsFactor` = *Minutes*
  - options: Seconds, Minutes, Hours, Days

- **`Memory`** (select)
  - options (31): 1 GB, 1.5 GB, 2 GB, 2.5 GB, 3 GB, 3.5 GB, 4 GB, 4.5 GB, 5 GB, 5.5 GB, 6 GB, 6.5 GB, 7 GB, 7.5 GB, 8 GB, ...

- **`Cores`** (select)
  - options: 1, 2, 3, 4

- **`Minutes`** (number)
  - depends on: `durationUnitsFactor`
  - only exists when: `durationUnitsFactor` = *Minutes*

- **`Minutes (durationUnitsFactor)`** (select)
  - depends on: `durationUnitsFactor`
  - only exists when: `durationUnitsFactor` = *Minutes*
  - options: Seconds, Minutes, Hours, Days

- **`billingOption`** (radio)
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~27% savings)), `sv-three-year` (3 year savings plan (~52% savings))

## Example component

```json
{
  "product": "Container Instances",
  "name": "my-container-instances",
  "fields": {
    "Region": "Central US",
    "Operating system": "Linux",
    "containerGroups": 1,
    "Seconds": 1,
    "durationUnitsFactor": "Seconds"
  }
}
```
