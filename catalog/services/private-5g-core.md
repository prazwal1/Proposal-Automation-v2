# Private 5g Core

- slug: `private-5g-core`  |  module: `private-5g-core-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options: East US, UAE North, West Europe, US Gov Virginia

- **`Package`** (select)
  - options: Package G0, Package G1, Package G2, Package G5, Package G10

- **`Site(s)`** (number)

- **`Hours`** (number)
  - depends on: `additionalHoursFactor0`
  - disappears when: `additionalHoursFactor0` = *Days*

- **`additionalHoursFactor0`** (select)
  - depends on: `additionalHoursFactor0`
  - disappears when: `additionalHoursFactor0` = *Days*
  - options: Hours, Days, Month

- **`Gbps per site`** (number)

- **`throughputHours0`** (number)
  - depends on: `throughputHoursFactor0`
  - disappears when: `throughputHoursFactor0` = *Days*

- **`throughputHoursFactor0`** (select)
  - depends on: `throughputHoursFactor0`
  - disappears when: `throughputHoursFactor0` = *Days*
  - options: Hours, Days, Month

- **`Per site`** (number)
  - depends on: `package0`
  - disappears when: `package0` = *Package G5*, `package0` = *Package G10*

- **`ranHours0`** (number)
  - depends on: `package0`, `ranHoursFactor0`
  - disappears when: `package0` = *Package G5*, `package0` = *Package G10*, `ranHoursFactor0` = *Days*

- **`ranHoursFactor0`** (select)
  - depends on: `package0`, `ranHoursFactor0`
  - disappears when: `package0` = *Package G5*, `package0` = *Package G10*, `ranHoursFactor0` = *Days*
  - options: Hours, Days, Month

- **`x100 devices/hour`** (number)

- **`deviceHours`** (number)
  - depends on: `deviceHoursFactor`
  - disappears when: `deviceHoursFactor` = *Days*

- **`deviceHoursFactor`** (select)
  - depends on: `deviceHoursFactor`
  - disappears when: `deviceHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `additionalHoursFactor0`
  - only exists when: `additionalHoursFactor0` = *Days*

- **`Days (additionalHoursFactor0)`** (select)
  - depends on: `additionalHoursFactor0`
  - only exists when: `additionalHoursFactor0` = *Days*
  - options: Hours, Days, Month

- **`Days (throughputHours0)`** (number)
  - depends on: `throughputHoursFactor0`
  - only exists when: `throughputHoursFactor0` = *Days*

- **`Days (throughputHoursFactor0)`** (select)
  - depends on: `throughputHoursFactor0`
  - only exists when: `throughputHoursFactor0` = *Days*
  - options: Hours, Days, Month

- **`Days (ranHours0)`** (number)
  - depends on: `ranHoursFactor0`
  - only exists when: `ranHoursFactor0` = *Days*

- **`Days (ranHoursFactor0)`** (select)
  - depends on: `ranHoursFactor0`
  - only exists when: `ranHoursFactor0` = *Days*
  - options: Hours, Days, Month

- **`Days (deviceHours)`** (number)
  - depends on: `deviceHoursFactor`
  - only exists when: `deviceHoursFactor` = *Days*

- **`Days (deviceHoursFactor)`** (select)
  - depends on: `deviceHoursFactor`
  - only exists when: `deviceHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Private 5g Core",
  "name": "my-private-5g-core",
  "fields": {
    "Region": "East US",
    "Package": "Package G0",
    "Site(s)": 1,
    "Hours": 1,
    "additionalHoursFactor0": "Hours"
  }
}
```
