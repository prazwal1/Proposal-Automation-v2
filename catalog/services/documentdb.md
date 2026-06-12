# Documentdb

- slug: `documentdb`  |  module: `documentdb-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Cluster Tier`** (select)
  - options: M10, 1 vCores per node, 2 GiB per node, $0.02/vCore hour, M20, 2 vCores per node, 4 GiB per node, $0.08/vCore hour, M25, 2 vCores per node, 8 GiB per node, $0.11/vCore hour, M30, 2 vCores per node, 8 GiB per node, $0.14/vCore hour, M40, 4 vCores per node, 16 GiB per node, $0.28/vCore hour, M50, 8 vCores per node, 32 GiB per node, $0.55/vCore hour, M60, 16 vCores per node, 64 GiB per node, $1.10/vCore hour, M80, 32 vCores per node, 128 GiB per node, $2.21/vCore hour, M200, 64 vCores per node, 256 GiB per node, $4.41/vCore hour, M200-Autoscale, Up to 64 vCores per node, Up to 256 GiB per node, Up to $6.62/vCore hour, M300, 96 vCores per node, 384 GiB per node, $6.62/vCore hour

- **`Shards`** (number)

- **`Hours`** (number)
  - depends on: `documentDBVcoreHourFactor`
  - disappears when: `documentDBVcoreHourFactor` = *Days*

- **`documentDBVcoreHourFactor`** (select)
  - depends on: `documentDBVcoreHourFactor`
  - disappears when: `documentDBVcoreHourFactor` = *Days*
  - options: Hours, Days, Month

- **`Size`** (select)
  - options: 32 GiB General Purpose Storage, 64 GiB General Purpose Storage, 128 GiB General Purpose Storage, 256 GiB General Purpose Storage, 512 GiB General Purpose Storage, 1 TiB General Purpose Storage, 2 TiB General Purpose Storage, 4 TiB General Purpose Storage, 8 TiB General Purpose Storage, 16 TiB General Purpose Storage, 32 TiB General Purpose Storage

- **`Days`** (number)
  - depends on: `documentDBVcoreHourFactor`
  - only exists when: `documentDBVcoreHourFactor` = *Days*

- **`Days (documentDBVcoreHourFactor)`** (select)
  - depends on: `documentDBVcoreHourFactor`
  - only exists when: `documentDBVcoreHourFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Documentdb",
  "name": "my-documentdb",
  "fields": {
    "Region": "Central US",
    "Cluster Tier": "M10, 1 vCores per node, 2 GiB per node, $0.02/vCore hour",
    "Shards": 1,
    "Hours": 1,
    "documentDBVcoreHourFactor": "Hours"
  }
}
```
