# Active Directory

- slug: `active-directory`  |  module: `active-directory-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (57): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Users`** (number)

- **`premiumP2Users`** (number)

- **`Pricing Tiers`** (select) — section: *Microsoft Entra Domain Services* (opened automatically)
  - options: Standard, Enterprise, Premium

- **`Hours`** (number) — section: *Microsoft Entra Domain Services* (opened automatically)
  - depends on: `dsUserForestHoursFactor`
  - disappears when: `dsUserForestHoursFactor` = *Days*

- **`dsUserForestHoursFactor`** (select) — section: *Microsoft Entra Domain Services* (opened automatically)
  - depends on: `dsUserForestHoursFactor`
  - disappears when: `dsUserForestHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `dsUserForestHoursFactor`
  - only exists when: `dsUserForestHoursFactor` = *Days*

- **`Days (dsUserForestHoursFactor)`** (select)
  - depends on: `dsUserForestHoursFactor`
  - only exists when: `dsUserForestHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Active Directory",
  "name": "my-active-directory",
  "fields": {
    "Region": "Central US",
    "Users": 1,
    "premiumP2Users": 1
  }
}
```
