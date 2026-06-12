# Load Testing

- slug: `load-testing`  |  module: `load-testing-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (24): Central US, East US, East US 2, South Central US, West US 2, West US 3, UK South, Switzerland North, Sweden Central, Malaysia West, Japan East, Italy North, Israel Central, Central India, Germany West Central, ...

- **`Estimation Method`** (select)
  - options: Aggregated usage, Load test details

- **`Virtual users per test`** (number)
  - depends on: `usageType`
  - disappears when: `usageType` = *Aggregated usage*

- **`Test Duration (minutes)`** (number)
  - depends on: `usageType`
  - disappears when: `usageType` = *Aggregated usage*

- **`Test runs per month`** (number)
  - depends on: `usageType`
  - disappears when: `usageType` = *Aggregated usage*

- **`Operating system of the cloud browser`** (select)
  - options: Linux, Windows

- **`Total number of Playwright tests in the test suite`** (number)

- **`Average seconds per test`** (number)

- **`Number test runs per month`** (number)

- **`Total virtual user hours`** (number)
  - depends on: `usageType`
  - only exists when: `usageType` = *Aggregated usage*

## Example component

```json
{
  "product": "Load Testing",
  "name": "my-load-testing",
  "fields": {
    "Region": "Central US",
    "Estimation Method": "Aggregated usage",
    "Virtual users per test": 1,
    "Test Duration (minutes)": 1,
    "Test runs per month": 1
  }
}
```
