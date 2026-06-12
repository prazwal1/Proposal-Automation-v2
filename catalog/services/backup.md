# Backup

- slug: `backup`  |  module: `backup-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Type`** (select)
  - options: Azure VMs, Azure Blob (non-HNS), On-premises Servers, Azure Files, SAP HANA in Azure VMs, SAP ASE in Azure VMs, SQL Server on Azure VMs, Azure PostgreSQL Servers or Flexible Servers, Kubernetes Service, Azure Data Lake Storage (HNS), Azure Cosmos DB

- **`Backup Policy Type`** (select)
  - depends on: `type`
  - disappears when: `type` = *Azure Blob (non-HNS)*, `type` = *On-premises Servers*
  - options: Standard, Enhanced

- **`VMs`** (number)
  - depends on: `type`
  - disappears when: `type` = *Azure Blob (non-HNS)*, `type` = *On-premises Servers*, `type` = *Azure Files*, `type` = *SAP HANA in Azure VMs*, `type` = *SAP ASE in Azure VMs*, `type` = *SQL Server on Azure VMs*

- **`GB`** (number)
  - depends on: `type`
  - disappears when: `type` = *Kubernetes Service*

- **`backupUnits`** (select)
  - depends on: `type`, `backupUnits`
  - disappears when: `type` = *Kubernetes Service*, `backupUnits` = *TB*
  - options: GB, TB

- **`Day(s)`** (number)
  - depends on: `type`
  - disappears when: `type` = *Azure PostgreSQL Servers or Flexible Servers*, `type` = *Kubernetes Service*

- **`Week(s)`** (number)
  - depends on: `type`

- **`Month(s)`** (number)
  - depends on: `type`

- **`Year(s)`** (number)
  - depends on: `type`

- **`restoreSnapshots`** (number)
  - depends on: `type`
  - disappears when: `type` = *Azure Blob (non-HNS)*, `type` = *On-premises Servers*, `type` = *Azure Files*

- **`Average Daily Data Churn`** (select)
  - depends on: `type`
  - disappears when: `type` = *Azure PostgreSQL Servers or Flexible Servers*, `type` = *Kubernetes Service*
  - options: Low, Moderate, High

- **`Redundancy`** (select)
  - depends on: `type`
  - options: LRS, GRS, RA-GRS, ZRS
  - when `type` = *Azure Files*: LRS, GRS, GZRS, ZRS

- **`Storage Accounts`** (number)
  - depends on: `type`
  - only exists when: `type` = *Azure Blob (non-HNS)*, `type` = *Azure Files*, `type` = *Azure Data Lake Storage (HNS)*

- **`x 10,000 operations`** (number)
  - depends on: `type`
  - only exists when: `type` = *Azure Blob (non-HNS)*, `type` = *Azure Data Lake Storage (HNS)*

- **`Servers`** (number)
  - depends on: `type`
  - only exists when: `type` = *On-premises Servers*, `type` = *SAP HANA in Azure VMs*, `type` = *SAP ASE in Azure VMs*, `type` = *SQL Server on Azure VMs*, `type` = *Azure PostgreSQL Servers or Flexible Servers*

- **`Performance Tier`** (select)
  - depends on: `type`
  - only exists when: `type` = *Azure Files*
  - options: Transaction Optimized, Premium, Hot, Cool

- **`AKS Clusters`** (number)
  - depends on: `type`
  - only exists when: `type` = *Kubernetes Service*

- **`Namespaces`** (number)
  - depends on: `type`
  - only exists when: `type` = *Kubernetes Service*

- **`Cosmos DB account`** (number)
  - depends on: `type`
  - only exists when: `type` = *Azure Cosmos DB*

- **`Schedule for hourly backup`** (select)
  - depends on: `backuppolicytype`
  - only exists when: `backuppolicytype` = *Enhanced*
  - options: 4 hours, 6 hours, 8 hours, 12 hours, 24 hours

- **`TB`** (number)
  - depends on: `backupUnits`
  - only exists when: `backupUnits` = *TB*

- **`TB (backupUnits)`** (select)
  - depends on: `backupUnits`
  - only exists when: `backupUnits` = *TB*
  - options: GB, TB

## Example component

```json
{
  "product": "Backup",
  "name": "my-backup",
  "fields": {
    "Region": "Central US",
    "Type": "Azure VMs",
    "Backup Policy Type": "Standard",
    "VMs": 1,
    "GB": 1
  }
}
```
