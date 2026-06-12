# Virtual Wan

- slug: `virtual-wan`  |  module: `virtual-wan-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (59): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Hours`** (number)
  - depends on: `standardDeploymentHoursFactor`
  - disappears when: `standardDeploymentHoursFactor` = *Days*

- **`standardDeploymentHoursFactor`** (select)
  - depends on: `standardDeploymentHoursFactor`
  - disappears when: `standardDeploymentHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Additional Routing Infrastructure Units`** (number)

- **`GB`** (number)
  - depends on: `standardDataProcessedUnits`
  - disappears when: `standardDataProcessedUnits` = *TB*

- **`standardDataProcessedUnits`** (select)
  - depends on: `standardDataProcessedUnits`
  - disappears when: `standardDataProcessedUnits` = *TB*
  - options: GB, TB

- **`s2SVPNScaleHours`** (number) — section: *Connections* (opened automatically)
  - depends on: `s2SVPNScaleHoursFactor`
  - disappears when: `s2SVPNScaleHoursFactor` = *Days*

- **`s2SVPNScaleHoursFactor`** (select) — section: *Connections* (opened automatically)
  - depends on: `s2SVPNScaleHoursFactor`
  - disappears when: `s2SVPNScaleHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`s2SVPNScaleUnits`** (number) — section: *Connections* (opened automatically)

- **`s2SVPNConnectionUnits`** (number) — section: *Connections* (opened automatically)

- **`HoursDaysMonth`** (number) — section: *Connections* (opened automatically)

- **`userVPNScaleHours`** (number) — section: *Connections* (opened automatically)
  - depends on: `userVPNScaleHoursFactor`
  - disappears when: `userVPNScaleHoursFactor` = *Days*

- **`userVPNScaleHoursFactor`** (select) — section: *Connections* (opened automatically)
  - depends on: `userVPNScaleHoursFactor`
  - disappears when: `userVPNScaleHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`userVPNConnectionUnits`** (number) — section: *Connections* (opened automatically)

- **`userVPNConnectionHours`** (number) — section: *Connections* (opened automatically)
  - depends on: `userVPNConnectionHoursFactor`
  - disappears when: `userVPNConnectionHoursFactor` = *Days*

- **`userVPNConnectionHoursFactor`** (select) — section: *Connections* (opened automatically)
  - depends on: `userVPNConnectionHoursFactor`
  - disappears when: `userVPNConnectionHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`expressRouteScaleHours`** (number) — section: *Connections* (opened automatically)
  - depends on: `expressRouteScaleHoursFactor`
  - disappears when: `expressRouteScaleHoursFactor` = *Days*

- **`expressRouteScaleHoursFactor`** (select) — section: *Connections* (opened automatically)
  - depends on: `expressRouteScaleHoursFactor`
  - disappears when: `expressRouteScaleHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`expressRouteScaleUnits`** (number) — section: *Connections* (opened automatically)

- **`expressRouteConnectionUnits`** (number) — section: *Connections* (opened automatically)

- **`Days`** (number)
  - depends on: `standardDeploymentHoursFactor`
  - only exists when: `standardDeploymentHoursFactor` = *Days*

- **`Days (standardDeploymentHoursFactor)`** (select)
  - depends on: `standardDeploymentHoursFactor`
  - only exists when: `standardDeploymentHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`TB`** (number)
  - depends on: `standardDataProcessedUnits`
  - only exists when: `standardDataProcessedUnits` = *TB*

- **`TB (standardDataProcessedUnits)`** (select)
  - depends on: `standardDataProcessedUnits`
  - only exists when: `standardDataProcessedUnits` = *TB*
  - options: GB, TB

- **`Days (s2SVPNScaleHours)`** (number)
  - depends on: `s2SVPNScaleHoursFactor`
  - only exists when: `s2SVPNScaleHoursFactor` = *Days*

- **`Days (s2SVPNScaleHoursFactor)`** (select)
  - depends on: `s2SVPNScaleHoursFactor`
  - only exists when: `s2SVPNScaleHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (userVPNScaleHours)`** (number)
  - depends on: `userVPNScaleHoursFactor`
  - only exists when: `userVPNScaleHoursFactor` = *Days*

- **`Days (userVPNScaleHoursFactor)`** (select)
  - depends on: `userVPNScaleHoursFactor`
  - only exists when: `userVPNScaleHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (userVPNConnectionHours)`** (number)
  - depends on: `userVPNConnectionHoursFactor`
  - only exists when: `userVPNConnectionHoursFactor` = *Days*

- **`Days (userVPNConnectionHoursFactor)`** (select)
  - depends on: `userVPNConnectionHoursFactor`
  - only exists when: `userVPNConnectionHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (expressRouteScaleHours)`** (number)
  - depends on: `expressRouteScaleHoursFactor`
  - only exists when: `expressRouteScaleHoursFactor` = *Days*

- **`Days (expressRouteScaleHoursFactor)`** (select)
  - depends on: `expressRouteScaleHoursFactor`
  - only exists when: `expressRouteScaleHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Virtual Wan",
  "name": "my-virtual-wan",
  "fields": {
    "Region": "Central US",
    "Hours": 1,
    "standardDeploymentHoursFactor": "Hours",
    "Additional Routing Infrastructure Units": 1,
    "GB": 1
  }
}
```
