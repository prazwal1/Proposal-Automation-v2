# Cosmos Db

- slug: `cosmos-db`  |  module: `cosmos-db-module`

## Fields

- **`product-name`** (text)

- **`Api Choice`** (select)
  - options: Azure Cosmos DB for NoSQL (formerly Core), Azure Cosmos DB for PostgreSQL (NEW), Azure Cosmos DB for MongoDB (RU), Azure Cosmos DB for MongoDB (vCore), Azure Cosmos DB for Apache Cassandra, Azure Cosmos DB for Apache Gremlin, Azure Cosmos DB for Table, Azure Cosmos DB Garnet Cache

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Database Operations`** (select)
  - depends on: `apiChoice`
  - disappears when: `apiChoice` = *Azure Cosmos DB for PostgreSQL (NEW)*, `apiChoice` = *Azure Cosmos DB for MongoDB (vCore)*, `apiChoice` = *Azure Cosmos DB Garnet Cache*
  - options: Standard provisioned throughput (manual), Autoscale provisioned throughput, Serverless

- **`Service Tier`** (select)
  - depends on: `apiChoice`, `databaseOperation`
  - disappears when: `apiChoice` = *Azure Cosmos DB for PostgreSQL (NEW)*, `apiChoice` = *Azure Cosmos DB for MongoDB (RU)*, `apiChoice` = *Azure Cosmos DB for MongoDB (vCore)*, `apiChoice` = *Azure Cosmos DB for Apache Cassandra*, `apiChoice` = *Azure Cosmos DB for Apache Gremlin*, `apiChoice` = *Azure Cosmos DB for Table*
  - options: General Purpose, Business Critical

- **`Write Capability`** (select)
  - depends on: `apiChoice`, `databaseOperation`, `serviceTier`
  - disappears when: `apiChoice` = *Azure Cosmos DB for PostgreSQL (NEW)*, `apiChoice` = *Azure Cosmos DB for MongoDB (RU)*, `apiChoice` = *Azure Cosmos DB for MongoDB (vCore)*, `apiChoice` = *Azure Cosmos DB for Apache Cassandra*, `apiChoice` = *Azure Cosmos DB for Apache Gremlin*, `apiChoice` = *Azure Cosmos DB for Table*
  - options: Multi Region Write, Per Partition Automatic Failover
  - when `serviceTier` = *General Purpose*: Single Write

- **`RUs`** (number)
  - depends on: `apiChoice`, `databaseOperation`
  - disappears when: `apiChoice` = *Azure Cosmos DB for PostgreSQL (NEW)*, `apiChoice` = *Azure Cosmos DB for MongoDB (vCore)*, `apiChoice` = *Azure Cosmos DB Garnet Cache*, `databaseOperation` = *Serverless*

- **`Hours`** (number)
  - depends on: `apiChoice`

- **`hoursFactor`** (select)
  - depends on: `apiChoice`
  - options: Hours, Days, Month

- **`Preferred Write Region`** (select)
  - depends on: `apiChoice`, `databaseOperation`, `serviceTier`, `writeCapability`
  - disappears when: `apiChoice` = *Azure Cosmos DB for PostgreSQL (NEW)*, `apiChoice` = *Azure Cosmos DB for MongoDB (RU)*, `apiChoice` = *Azure Cosmos DB for MongoDB (vCore)*, `apiChoice` = *Azure Cosmos DB for Apache Cassandra*, `apiChoice` = *Azure Cosmos DB for Apache Gremlin*, `apiChoice` = *Azure Cosmos DB for Table*
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`GB`** (number)
  - depends on: `apiChoice`
  - disappears when: `apiChoice` = *Azure Cosmos DB for PostgreSQL (NEW)*, `apiChoice` = *Azure Cosmos DB for MongoDB (vCore)*, `apiChoice` = *Azure Cosmos DB Garnet Cache*

- **`Backup Type`** (select)
  - depends on: `apiChoice`, `databaseOperation`
  - disappears when: `apiChoice` = *Azure Cosmos DB for PostgreSQL (NEW)*, `apiChoice` = *Azure Cosmos DB for MongoDB (vCore)*, `apiChoice` = *Azure Cosmos DB Garnet Cache*
  - options: Periodic, Continuous (7-day), Continuous (30-day)
  - when `apiChoice` = *Azure Cosmos DB for Apache Cassandra*: Periodic
  - when `apiChoice` = *Azure Cosmos DB for Apache Gremlin*: Periodic
  - when `apiChoice` = *Azure Cosmos DB for Table*: Periodic
  - when `databaseOperation` = *Serverless*: Periodic

- **`Backup Copies`** (number)
  - depends on: `apiChoice`, `backupType`
  - disappears when: `apiChoice` = *Azure Cosmos DB for PostgreSQL (NEW)*, `apiChoice` = *Azure Cosmos DB for MongoDB (vCore)*, `apiChoice` = *Azure Cosmos DB Garnet Cache*, `backupType` = *Continuous (7-day)*, `backupType` = *Continuous (30-day)*

- **`Tier`** (select)
  - depends on: `apiChoice`
  - only exists when: `apiChoice` = *Azure Cosmos DB for PostgreSQL (NEW)*
  - options: Single Node, Multi Node

- **`Compute`** (select)
  - depends on: `apiChoice`
  - only exists when: `apiChoice` = *Azure Cosmos DB for PostgreSQL (NEW)*
  - options: 1 vCore Burstable, 2 GiB RAM, 2 vCore Burstable, 4 GiB RAM, 2 vCore, 8 GiB RAM, 4 vCore, 16 GiB RAM, 8 vCore, 32 GiB RAM, 16 vCore, 64 GiB RAM, 32 vCore, 128 GiB RAM, 64 vCore, 256 GiB RAM

- **`Size`** (select)
  - depends on: `apiChoice`
  - only exists when: `apiChoice` = *Azure Cosmos DB for PostgreSQL (NEW)*
  - options: 128 GiB General Purpose Storage, 256 GiB General Purpose Storage, 512 GiB General Purpose Storage, 1 TiB General Purpose Storage, 2 TiB General Purpose Storage

- **`Write Regions`** (select)
  - depends on: `apiChoice`
  - only exists when: `apiChoice` = *Azure Cosmos DB for MongoDB (RU)*, `apiChoice` = *Azure Cosmos DB for Apache Cassandra*, `apiChoice` = *Azure Cosmos DB for Apache Gremlin*, `apiChoice` = *Azure Cosmos DB for Table*, `databaseOperation` = *Serverless*
  - options: Single Region Write (Single-Master), Multiple Region Write (Multi-Master)

- **`Write Region`** (select)
  - depends on: `apiChoice`, `databaseOperation`
  - only exists when: `apiChoice` = *Azure Cosmos DB for MongoDB (RU)*, `apiChoice` = *Azure Cosmos DB for Apache Cassandra*, `apiChoice` = *Azure Cosmos DB for Apache Gremlin*, `apiChoice` = *Azure Cosmos DB for Table*, `serviceTier` = *General Purpose*
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`SKU`** (select)
  - depends on: `apiChoice`
  - only exists when: `apiChoice` = *Azure Cosmos DB Garnet Cache*
  - options: D2, 2 vCores per node, 8 GiB per node, $0.1259/vCore hour, D4, 4 vCores per node, 16 GiB per node, $0.2518/vCore hour, D8, 8 vCores per node, 32 GiB per node, $0.5037/vCore hour, D16, 16 vCores per node, 64 GiB per node, $1.0074/vCore hour, D32, 32 vCores per node, 128 GiB per node, $2.0147/vCore hour, D48, 48 vCores per node, 192 GiB per node, $3.0221/vCore hour, D64, 64 vCores per node, 256 GiB per node, $4.0294/vCore hour, D96, 96 vCores per node, 384 GiB per node, $6.0442/vCore hour, D128, 128 vCores per node, 512 GiB per node, $8.0589/vCore hour, D192, 192 vCores per node, 768 GiB per node, $12.0883/vCore hour

- **`Shards`** (number)
  - depends on: `apiChoice`
  - only exists when: `apiChoice` = *Azure Cosmos DB Garnet Cache*

- **`Replication Factor`** (number)
  - depends on: `apiChoice`
  - only exists when: `apiChoice` = *Azure Cosmos DB Garnet Cache*

- **`DISK SIZE`** (select)
  - depends on: `apiChoice`
  - only exists when: `apiChoice` = *Azure Cosmos DB Garnet Cache*
  - options: P6, 64 GiB disk

- **`Average % Utilization`** (number)
  - depends on: `databaseOperation`
  - only exists when: `databaseOperation` = *Autoscale provisioned throughput*

- **`x1 million RUs`** (number)
  - depends on: `databaseOperation`
  - only exists when: `databaseOperation` = *Serverless*

- **`Primary Write Region`** (select)
  - depends on: `writeCapability`
  - only exists when: `writeCapability` = *Multi Region Write*
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`billingOption`** (radio)
  - depends on: `apiChoice`
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved capacity), `three-year` (3 year reserved capacity)

- **`singleNodeBillingOption`** (radio)
  - depends on: `apiChoice`
  - only exists when: `apiChoice` = *Azure Cosmos DB for PostgreSQL (NEW)*
  - choices: `one-year` (1 year reserved (~0% savings)), `three-year` (3 year reserved (~17% savings))

## Example component

```json
{
  "product": "Cosmos Db",
  "name": "my-cosmos-db",
  "fields": {
    "Api Choice": "Azure Cosmos DB for NoSQL (formerly Core)",
    "Region": "Central US",
    "Database Operations": "Standard provisioned throughput (manual)",
    "Service Tier": "General Purpose",
    "Write Capability": "Multi Region Write"
  }
}
```
