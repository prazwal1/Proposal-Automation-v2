# Machine Learning Studio

- slug: `machine-learning-studio`  |  module: `machine-learning-studio-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options: East US 2, South Central US, West Central US, Japan East, West Europe, US Gov Arizona, US Gov Texas, US Gov Virginia, Southeast Asia

- **`Feature`** (select)
  - options: Workspace, API Usage - Classic Web Service, API Usage - New Web Service

- **`Tier`** (select)
  - depends on: `feature`
  - options: Free, Standard

- **`Transactions`** (number)
  - depends on: `feature`
  - only exists when: `feature` = *API Usage - Classic Web Service*

- **`Compute hours`** (number)
  - depends on: `feature`
  - only exists when: `feature` = *API Usage - Classic Web Service*

- **`Workspaces`** (number)
  - depends on: `studioTier`
  - only exists when: `studioTier` = *Standard*

- **`Experiment hours per seat`** (number)
  - depends on: `studioTier`
  - only exists when: `studioTier` = *Standard*

## Example component

```json
{
  "product": "Machine Learning Studio",
  "name": "my-machine-learning-studio",
  "fields": {
    "Region": "East US 2",
    "Feature": "Workspace",
    "Tier": "Free"
  }
}
```
