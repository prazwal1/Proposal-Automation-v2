# Automation

- slug: `automation`  |  module: `automation-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (52): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Capability`** (select)
  - options: Configuration Management (Azure nodes), Configuration Management (non-Azure nodes), Process Automation, Update Management (Azure and non-Azure nodes)

- **`Nodes`** (number)
  - depends on: `capability`

- **`Additional nodes`** (number)
  - depends on: `capability`
  - only exists when: `capability` = *Configuration Management (non-Azure nodes)*

- **`Additional minutes`** (number)
  - depends on: `capability`
  - only exists when: `capability` = *Process Automation*

- **`Watchers`** (number)
  - depends on: `capability`
  - only exists when: `capability` = *Process Automation*

- **`Hours`** (number)
  - depends on: `capability`
  - only exists when: `capability` = *Process Automation*

- **`watchersHoursFactor`** (select)
  - depends on: `capability`
  - only exists when: `capability` = *Process Automation*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Automation",
  "name": "my-automation",
  "fields": {
    "Region": "Central US",
    "Capability": "Configuration Management (Azure nodes)",
    "Nodes": 1
  }
}
```
