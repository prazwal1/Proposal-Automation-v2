# Monitor

- slug: `monitor`  |  module: `monitor-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Per day (GB)`** (number) — section: *Log Data Ingestion* (opened automatically)

- **`auxiliaryLogsIngestedWithProcessing`** (number) — section: *Log Data Ingestion* (opened automatically)

- **`basicLogsIngested`** (number) — section: *Log Data Ingestion* (opened automatically)

- **`dailyLogsIngested`** (number) — section: *Log Data Ingestion* (opened automatically)

- **`Interactive retention (Months)`** (number) — section: *Log Data Ingestion* (opened automatically)

- **`Retention (months)`** (number) — section: *Log Data Ingestion* (opened automatically)

- **`Amount of data restored (GB)`** (number) — section: *Log Data Ingestion* (opened automatically)

- **`Number of days data restored`** (number) — section: *Log Data Ingestion* (opened automatically)

- **`Total number of queries (day)`** (number) — section: *Log Data Ingestion* (opened automatically)

- **`Data scanned per query (GB)`** (number) — section: *Log Data Ingestion* (opened automatically)

- **`Total number of search-jobs (day)`** (number) — section: *Log Data Ingestion* (opened automatically)

- **`Data scanned per search (GB)`** (number) — section: *Log Data Ingestion* (opened automatically)

- **`Volume of data exported (GB) per day`** (number) — section: *Log Data Ingestion* (opened automatically)

- **`Volume of data processed (GB) per day`** (number) — section: *Log Data Ingestion* (opened automatically)

- **`marketplacePartners`** (number) — section: *Log Data Ingestion* (opened automatically)

- **`Number of Endpoints`** (number) — section: *SCOM Managed Instance* (opened automatically)

- **`Number of API calls`** (number) — section: *Metrics* (opened automatically)

- **`Data Volume Estimation Method`** (select) — section: *Metrics* (opened automatically)
  - options: Using default collection, Using estimated metrics volume

- **`Number of Linux nodes in each cluster`** (number) — section: *Metrics* (opened automatically)
  - depends on: `estimationMethodOption`
  - disappears when: `estimationMethodOption` = *Using estimated metrics volume*

- **`Number of Windows nodes in each cluster`** (number) — section: *Metrics* (opened automatically)
  - depends on: `estimationMethodOption`
  - disappears when: `estimationMethodOption` = *Using estimated metrics volume*

- **`Total number of containers in the cluster​`** (number) — section: *Metrics* (opened automatically)
  - depends on: `estimationMethodOption`
  - disappears when: `estimationMethodOption` = *Using estimated metrics volume*

- **`Total number of pods in the cluster`** (number) — section: *Metrics* (opened automatically)
  - depends on: `estimationMethodOption`
  - disappears when: `estimationMethodOption` = *Using estimated metrics volume*

- **`Average number of daily Dashboards users`** (number) — section: *Metrics* (opened automatically)

- **`Number of dashboards`** (number) — section: *Metrics* (opened automatically)

- **`Data samples queried per dashboard`** (number) — section: *Metrics* (opened automatically)

- **`Number of promql alerting rules`** (number) — section: *Metrics* (opened automatically)

- **`Number of promql recording rules`** (number) — section: *Metrics* (opened automatically)

- **`Number of metrics datapoints exported`** (number) — section: *Metrics* (opened automatically)

- **`Daily logs ingested (GB/day)`** (number) — section: *Application Insights* (opened automatically)

- **`Total retention (Months)`** (number) — section: *Application Insights* (opened automatically)

- **`Number of tests`** (number) — section: *Application Insights* (opened automatically)

- **`Execution Frequency`** (select) — section: *Application Insights* (opened automatically)
  - options: 5 Minutes, 10 Minutes, 15 Minutes

- **`Hours per month`** (number) — section: *Application Insights* (opened automatically)

- **`Resources monitored`** (number) — section: *Alert Rules* (opened automatically)

- **`Metric time-series monitored per resource`** (number) — section: *Alert Rules* (opened automatically)

- **`Querying Frequency`** (select) — section: *Alert Rules* (opened automatically)
  - options: 1 Minute, 5 Minutes, 10 Minutes, 15 Minutes

- **`Number of log signals monitored`** (number) — section: *Alert Rules* (opened automatically)

- **`Number of Time series per signal`** (number) — section: *Alert Rules* (opened automatically)

- **`Additional Events (in thousands)`** (number) — section: *ITSM Connector - Ticket Creation/Update* (opened automatically)

- **`Additional emails (in 100k)`** (number) — section: *Notifications* (opened automatically)

- **`Additional push notifications (in 100k)`** (number) — section: *Notifications* (opened automatically)

- **`Additional web hooks (in millions)`** (number) — section: *Notifications* (opened automatically)

- **`Number of AKS nodes in cluster`** (number)
  - depends on: `estimationMethodOption`
  - only exists when: `estimationMethodOption` = *Using estimated metrics volume*

- **`Number of Prometheus metrics per node`** (number)
  - depends on: `estimationMethodOption`
  - only exists when: `estimationMethodOption` = *Using estimated metrics volume*

- **`Metric collection interval (in seconds)`** (number)
  - depends on: `estimationMethodOption`
  - only exists when: `estimationMethodOption` = *Using estimated metrics volume*

## Example component

```json
{
  "product": "Monitor",
  "name": "my-monitor",
  "fields": {
    "Region": "Central US"
  }
}
```
