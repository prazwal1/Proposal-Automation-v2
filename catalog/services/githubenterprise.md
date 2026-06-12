# Githubenterprise

- slug: `githubenterprise`  |  module: `githubenterprise-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (57): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Users`** (number)

- **`Copilot Enterprise Users`** (number)

- **`Copilot Business Users`** (number)

- **`Committers`** (number)

- **`secretProtectionCommitters`** (number)

- **`Operating system`** (select)
  - options: Linux, macOS, Windows

- **`Machine size`** (select)
  - depends on: `actionsOperatingSystem`
  - options (23): 1 core, 2 core, 4 core, 8 core, 16 core, 32 core, 64 core, 96 core, 4 core GPU, GPU B12, GPU B24, GPU B36, HP, MO64, MO160, ...
  - when `actionsOperatingSystem` = *macOS*: 3 core, XL, L, M

- **`Number of Jobs per month`** (number)

- **`Duration of each job in minutes`** (number)

- **`GB`** (number)

- **`packagesBandwidth`** (number)

- **`codespacesOperatingSystem`** (select)
  - options: Linux

- **`codespacesSize`** (select)
  - options: 2 core, 4 core, 8 core, 16 core, 32 core

- **`Number of Developers`** (number)

- **`Monthly Usage per developer (hours)`** (number)

- **`Stored Codespaces per dev`** (number)

- **`Average project size (GiB)`** (number)

- **`largeFileStorage`** (number)

- **`largeFileBandwidth`** (number)

## Example component

```json
{
  "product": "Githubenterprise",
  "name": "my-githubenterprise",
  "fields": {
    "Region": "Central US",
    "Users": 1,
    "Copilot Enterprise Users": 1,
    "Copilot Business Users": 1,
    "Committers": 1
  }
}
```
