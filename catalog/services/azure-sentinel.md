# Azure Sentinel

- slug: `azure-sentinel`  |  module: `azure-sentinel-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Ingestion Size Estimation Type`** (select)
  - options: Daily Logs Ingested, Events Per Second

- **`Per day (GB)`** (number)
  - depends on: `ingestionSizeEstimationType`
  - disappears when: `ingestionSizeEstimationType` = *Events Per Second*

- **`dailyDataLakeTierLogsIngested`** (number)
  - depends on: `ingestionSizeEstimationType`
  - disappears when: `ingestionSizeEstimationType` = *Events Per Second*

- **`Analytics retention (months)`** (number) — section: *Storage* (opened automatically)

- **`Total retention (months)`** (number) — section: *Storage* (opened automatically)

- **`Data lake retention (months)`** (number) — section: *Storage* (opened automatically)

- **`Hours`** (number) — section: *Advanced Data Insights* (opened automatically)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select) — section: *Advanced Data Insights* (opened automatically)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Total number of queries (per Month)`** (number) — section: *Data Lake Query* (opened automatically)

- **`Data scanned per query (GB)`** (number) — section: *Data Lake Query* (opened automatically)

- **`searchJobsTotalQueries`** (number) — section: *Data Lake Query* (opened automatically)

- **`searchJobsDataScanned`** (number) — section: *Data Lake Query* (opened automatically)

- **`Security compute units per hour`** (number) — section: *Entity Analyzer* (opened automatically)

- **`provisionedSecurityComputeHours`** (number) — section: *Entity Analyzer* (opened automatically)
  - depends on: `provisionedSecurityComputeHoursFactor`
  - disappears when: `provisionedSecurityComputeHoursFactor` = *Days*

- **`provisionedSecurityComputeHoursFactor`** (select) — section: *Entity Analyzer* (opened automatically)
  - depends on: `provisionedSecurityComputeHoursFactor`
  - disappears when: `provisionedSecurityComputeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`overageSecurityComputeUnits`** (number) — section: *Entity Analyzer* (opened automatically)

- **`overageSecurityComputeHours`** (number) — section: *Entity Analyzer* (opened automatically)
  - depends on: `overageSecurityComputeHoursFactor`
  - disappears when: `overageSecurityComputeHoursFactor` = *Days*

- **`overageSecurityComputeHoursFactor`** (select) — section: *Entity Analyzer* (opened automatically)
  - depends on: `overageSecurityComputeHoursFactor`
  - disappears when: `overageSecurityComputeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`graphHours`** (number) — section: *Graph* (opened automatically)
  - depends on: `graphHoursFactor`
  - disappears when: `graphHoursFactor` = *Days*

- **`graphHoursFactor`** (select) — section: *Graph* (opened automatically)
  - depends on: `graphHoursFactor`
  - disappears when: `graphHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Events per second`** (number)
  - depends on: `ingestionSizeEstimationType`
  - only exists when: `ingestionSizeEstimationType` = *Events Per Second*

- **`Average event size (bytes)`** (number)
  - depends on: `ingestionSizeEstimationType`
  - only exists when: `ingestionSizeEstimationType` = *Events Per Second*

- **`eventsDataLakeTierLogsPerSecond`** (number)
  - depends on: `ingestionSizeEstimationType`
  - only exists when: `ingestionSizeEstimationType` = *Events Per Second*

- **`eventsDataLakeTierLogsEventSize`** (number)
  - depends on: `ingestionSizeEstimationType`
  - only exists when: `ingestionSizeEstimationType` = *Events Per Second*

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (provisionedSecurityComputeHours)`** (number)
  - depends on: `provisionedSecurityComputeHoursFactor`
  - only exists when: `provisionedSecurityComputeHoursFactor` = *Days*

- **`Days (provisionedSecurityComputeHoursFactor)`** (select)
  - depends on: `provisionedSecurityComputeHoursFactor`
  - only exists when: `provisionedSecurityComputeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (overageSecurityComputeHours)`** (number)
  - depends on: `overageSecurityComputeHoursFactor`
  - only exists when: `overageSecurityComputeHoursFactor` = *Days*

- **`Days (overageSecurityComputeHoursFactor)`** (select)
  - depends on: `overageSecurityComputeHoursFactor`
  - only exists when: `overageSecurityComputeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (graphHours)`** (number)
  - depends on: `graphHoursFactor`
  - only exists when: `graphHoursFactor` = *Days*

- **`Days (graphHoursFactor)`** (select)
  - depends on: `graphHoursFactor`
  - only exists when: `graphHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Azure Sentinel",
  "name": "my-azure-sentinel",
  "fields": {
    "Region": "Central US",
    "Ingestion Size Estimation Type": "Daily Logs Ingested",
    "Per day (GB)": 1,
    "dailyDataLakeTierLogsIngested": 1
  }
}
```
