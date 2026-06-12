# Azure Devops

- slug: `azure-devops`  |  module: `azure-devops-module`

## Fields

- **`product-name`** (text)

- **`Additional users`** (number)

- **`Users`** (number)

- **`Tier`** (select)
  - options: Free, Paid

- **`Additional parallel CI/CD jobs`** (number)

- **`Operating system`** (select)
  - options: macOS

- **`Machine size`** (select)
  - options: Standard, XL

- **`Number of Jobs per month`** (number)

- **`Duration of each job in minutes`** (number)

- **`GiB`** (number)
  - depends on: `artifactUnits`
  - disappears when: `artifactUnits` = *TiB*

- **`artifactUnits`** (select)
  - depends on: `artifactUnits`
  - disappears when: `artifactUnits` = *TiB*
  - options: GiB, TiB

- **`Committers`** (number)

- **`secretProtectionCommitters`** (number)

- **`Parallel CI/CD jobs`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Paid*

- **`TiB`** (number)
  - depends on: `artifactUnits`
  - only exists when: `artifactUnits` = *TiB*

- **`TiB (artifactUnits)`** (select)
  - depends on: `artifactUnits`
  - only exists when: `artifactUnits` = *TiB*
  - options: GiB, TiB

## Example component

```json
{
  "product": "Azure Devops",
  "name": "my-azure-devops",
  "fields": {
    "Additional users": 1,
    "Users": 1,
    "Tier": "Free",
    "Additional parallel CI/CD jobs": 1,
    "Operating system": "macOS"
  }
}
```
