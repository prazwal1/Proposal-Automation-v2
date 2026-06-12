# Data Factory

- slug: `data-factory`  |  module: `data-factory-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (59): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Type`** (select)
  - options: Azure Data Factory V1, Azure Data Factory V2

- **`Service type`** (select)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Data Factory V1*
  - options: Data Pipeline, SQL Server Integration Services

- **`Activity Runs (in thousands)`** (number) — section: *Orchestration and Execution* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Data Factory V1*

- **`Data integration unit hours`** (number) — section: *Orchestration and Execution* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Data Factory V1*

- **`Pipeline activity execution hours`** (number) — section: *Orchestration and Execution* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Data Factory V1*

- **`External Pipeline activity execution hours`** (number) — section: *Orchestration and Execution* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Data Factory V1*

- **`Instance`** (select) — section: *Cluster Configuration* (opened automatically)
  - depends on: `tier`, `serviceType`
  - disappears when: `tier` = *Azure Data Factory V1*
  - options: 8 vCores, 16 vCores, 32 vCores, 48 vCores, 80 vCores, 144 vCores, 272 vCores

- **`Instances`** (number) — section: *Cluster Configuration* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Data Factory V1*

- **`Hours`** (number) — section: *Cluster Configuration* (opened automatically)
  - depends on: `tier`, `serviceType`
  - disappears when: `tier` = *Azure Data Factory V1*

- **`generalPurposeHoursFactor`** (select) — section: *Cluster Configuration* (opened automatically)
  - depends on: `tier`, `serviceType`
  - disappears when: `tier` = *Azure Data Factory V1*
  - options: Hours, Days, Month

- **`memoryOptimizedInstance`** (select) — section: *Cluster Configuration* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Data Factory V1*
  - options: 8 vCores, 16 vCores, 32 vCores, 48 vCores, 80 vCores, 144 vCores, 272 vCores

- **`Entity units (50,000 entities)`** (number) — section: *Operations* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Data Factory V1*

- **`monitoringOperations`** (number) — section: *Operations* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Data Factory V1*

- **`Low frequency activities`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Azure Data Factory V1*

- **`High frequency activities`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Azure Data Factory V1*

- **`Re-run activities (in thousands)`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Azure Data Factory V1*

- **`Data Movement (Hours)`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Azure Data Factory V1*

- **`onPremisesLowFrequency`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Azure Data Factory V1*

- **`onPremisesHighFrequency`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Azure Data Factory V1*

- **`onPremisesReruns`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Azure Data Factory V1*

- **`onPremisesDataMovement`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Azure Data Factory V1*

- **`Tier`** (select)
  - depends on: `serviceType`
  - only exists when: `serviceType` = *SQL Server Integration Services*
  - options: Standard, Enterprise

- **`Virtual machines`** (number)
  - depends on: `serviceType`
  - only exists when: `serviceType` = *SQL Server Integration Services*

- **`generalPurposeBillingOption`** (radio) — section: *Cluster Configuration* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Azure Data Factory V1*
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved (~25% savings)), `three-year` (3 year reserved (~35% savings))

## Example component

```json
{
  "product": "Data Factory",
  "name": "my-data-factory",
  "fields": {
    "Region": "Central US",
    "Type": "Azure Data Factory V1",
    "Service type": "Data Pipeline"
  }
}
```
