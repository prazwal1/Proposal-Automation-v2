# Sre Agent

- slug: `sre-agent`  |  module: `sre-agent-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options: Central US, East US, East US 2, South Central US, West US 3, UK South, Sweden Central, Canada Central, Canada East, Brazil South, Australia East

- **`Number Of Agents`** (number)

- **`Hours`** (number)
  - depends on: `agentsHoursFactor`
  - disappears when: `agentsHoursFactor` = *Days*

- **`agentsHoursFactor`** (select)
  - depends on: `agentsHoursFactor`
  - disappears when: `agentsHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Tasks per day`** (number)

- **`Number of days tasks run`** (number)

- **`Runtime of each task (in seconds)`** (number)

- **`Days`** (number)
  - depends on: `agentsHoursFactor`
  - only exists when: `agentsHoursFactor` = *Days*

- **`Days (agentsHoursFactor)`** (select)
  - depends on: `agentsHoursFactor`
  - only exists when: `agentsHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Sre Agent",
  "name": "my-sre-agent",
  "fields": {
    "Region": "Central US",
    "Number Of Agents": 1,
    "Hours": 1,
    "agentsHoursFactor": "Hours",
    "Tasks per day": 1
  }
}
```
