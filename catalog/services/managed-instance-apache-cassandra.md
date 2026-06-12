# Managed Instance Apache Cassandra

- slug: `managed-instance-apache-cassandra`  |  module: `managed-instance-apache-cassandra-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (50): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`VM SKU`** (select)
  - options (41): D2as v5: 2 vCPUs, 8 GB RAM, D4as v5: 4 vCPUs, 16 GB RAM, D8as v5: 8 vCPUs, 32 GB RAM, D16as v5: 16 vCPUs, 64 GB RAM, D32as v5: 32 vCPUs, 128 GB RAM, D2s v5: 2 vCPUs, 8 GB RAM, D4s v5: 4 vCPUs, 16 GB RAM, D8s v5: 8 vCPUs, 32 GB RAM, D16s v5: 16 vCPUs, 64 GB RAM, D32s v5: 32 vCPUs, 128 GB RAM, D16s v4: 16 vCPUs, 64 GB RAM, D2s v4: 2 vCPUs, 8 GB RAM, D4s v4: 4 vCPUs, 16 GB RAM, D8s v4: 8 vCPUs, 32 GB RAM, D32s v4: 32 vCPUs, 128 GB RAM, ...

- **`VM SKUs`** (number)

- **`Hours`** (number)
  - depends on: `computeInstancesHoursFactor`
  - disappears when: `computeInstancesHoursFactor` = *Days*

- **`computeInstancesHoursFactor`** (select)
  - depends on: `computeInstancesHoursFactor`
  - disappears when: `computeInstancesHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Disks`** (number)

- **`Days`** (number)
  - depends on: `computeInstancesHoursFactor`
  - only exists when: `computeInstancesHoursFactor` = *Days*

- **`Days (computeInstancesHoursFactor)`** (select)
  - depends on: `computeInstancesHoursFactor`
  - only exists when: `computeInstancesHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Managed Instance Apache Cassandra",
  "name": "my-managed-instance-apache-cassandra",
  "fields": {
    "Region": "Central US",
    "VM SKU": "D2as v5: 2 vCPUs, 8 GB RAM",
    "VM SKUs": 1,
    "Hours": 1,
    "computeInstancesHoursFactor": "Hours"
  }
}
```
