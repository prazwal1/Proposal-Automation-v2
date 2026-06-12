# Storage

- slug: `storage`  |  module: `storage-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Type`** (select)
  - options: Block Blob Storage, Table Storage, Queue Storage, Data Lake Storage Gen2, Azure Files, Page blobs (Unmanaged Disks included), Managed Disks

- **`Performance`** (select)
  - depends on: `type`, `storageAccountType`
  - disappears when: `type` = *Table Storage*, `type` = *Queue Storage*, `type` = *Data Lake Storage Gen2*, `type` = *Azure Files*, `type` = *Page blobs (Unmanaged Disks included)*, `type` = *Managed Disks*
  - options: Premium, Standard

- **`Storage Account Type`** (select)
  - depends on: `type`, `performanceTier`
  - disappears when: `type` = *Table Storage*, `type` = *Azure Files*, `type` = *Managed Disks*, `performanceTier` = *Premium*
  - options: General Purpose V2, Blob Storage, General Purpose V1
  - when `type` = *Queue Storage*: General Purpose V2, General Purpose V1
  - when `type` = *Data Lake Storage Gen2*: General Purpose V2
  - when `type` = *Page blobs (Unmanaged Disks included)*: General Purpose V2, General Purpose V1

- **`File Structure`** (select)
  - depends on: `type`, `storageAccountType`
  - disappears when: `type` = *Table Storage*, `type` = *Queue Storage*, `type` = *Azure Files*, `type` = *Page blobs (Unmanaged Disks included)*, `type` = *Managed Disks*, `storageAccountType` = *General Purpose V1*
  - options: Flat Namespace, Hierarchical Namespace

- **`Access tier`** (select)
  - depends on: `type`, `performanceTier`, `storageAccountType`
  - disappears when: `type` = *Table Storage*, `type` = *Queue Storage*, `type` = *Azure Files*, `type` = *Page blobs (Unmanaged Disks included)*, `type` = *Managed Disks*, `performanceTier` = *Premium*
  - options: Hot, Cool, Cold, Archive

- **`Redundancy`** (select)
  - depends on: `type`, `performanceTier`, `storageAccountType`, `accessTier`
  - disappears when: `type` = *Azure Files*, `type` = *Managed Disks*
  - options: LRS, ZRS, GRS, RA-GRS, GZRS, RA-GZRS
  - when `performanceTier` = *Premium*: LRS, ZRS
  - when `storageAccountType` = *Blob Storage*: LRS, ZRS, GRS, GZRS
  - when `storageAccountType` = *General Purpose V1*: LRS, ZRS, GRS, RA-GRS
  - when `accessTier` = *Archive*: LRS, GRS, RA-GRS

- **`GB`** (number)
  - depends on: `type`, `storageUnits`
  - disappears when: `type` = *Azure Files*, `type` = *Managed Disks*, `storageUnits` = *TB*

- **`storageUnits`** (select)
  - depends on: `type`, `storageUnits`
  - disappears when: `type` = *Azure Files*, `type` = *Managed Disks*, `storageUnits` = *TB*
  - options: GB, TB

- **`x 10,000 operations`** (number)
  - depends on: `type`, `storageAccountType`
  - disappears when: `type` = *Table Storage*, `type` = *Queue Storage*, `type` = *Data Lake Storage Gen2*, `type` = *Azure Files*, `type` = *Page blobs (Unmanaged Disks included)*, `type` = *Managed Disks*

- **`blobCreateContainerOperations`** (number)
  - depends on: `type`, `storageAccountType`, `fileStructure`
  - disappears when: `type` = *Table Storage*, `type` = *Queue Storage*, `type` = *Data Lake Storage Gen2*, `type` = *Azure Files*, `type` = *Page blobs (Unmanaged Disks included)*, `type` = *Managed Disks*

- **`blobReadOperations`** (number)
  - depends on: `type`, `storageAccountType`
  - disappears when: `type` = *Table Storage*, `type` = *Queue Storage*, `type` = *Data Lake Storage Gen2*, `type` = *Azure Files*, `type` = *Page blobs (Unmanaged Disks included)*, `type` = *Managed Disks*

- **`blobOtherOperations`** (number)
  - depends on: `type`, `storageAccountType`, `accessTier`
  - disappears when: `type` = *Table Storage*, `type` = *Queue Storage*, `type` = *Data Lake Storage Gen2*, `type` = *Azure Files*, `type` = *Page blobs (Unmanaged Disks included)*, `type` = *Managed Disks*

- **`blobDataRetrieval`** (number)
  - depends on: `type`, `performanceTier`, `storageAccountType`, `redundancy`
  - disappears when: `type` = *Table Storage*, `type` = *Queue Storage*, `type` = *Data Lake Storage Gen2*, `type` = *Azure Files*, `type` = *Page blobs (Unmanaged Disks included)*, `type` = *Managed Disks*

- **`blobDataRetrievalUnits`** (select)
  - depends on: `type`, `performanceTier`, `storageAccountType`, `redundancy`
  - disappears when: `type` = *Table Storage*, `type` = *Queue Storage*, `type` = *Data Lake Storage Gen2*, `type` = *Azure Files*, `type` = *Page blobs (Unmanaged Disks included)*, `type` = *Managed Disks*
  - options: GB, TB

- **`Tier`** (select)
  - depends on: `type`
  - only exists when: `type` = *Table Storage*, `type` = *Page blobs (Unmanaged Disks included)*
  - options: Standard, Account Encrypted

- **`Transaction units (10,000 transactions)`** (number)
  - depends on: `type`
  - only exists when: `type` = *Table Storage*

- **`Operations (in 10,000s)`** (number)
  - depends on: `type`
  - only exists when: `type` = *Queue Storage*

- **`queueClass2Operations`** (number)
  - depends on: `type`
  - only exists when: `type` = *Queue Storage*

- **`Write operations (in 10,000s)`** (number)
  - depends on: `type`
  - only exists when: `type` = *Page blobs (Unmanaged Disks included)*

- **`Write additional IO units (in 10,000s)`** (number)
  - depends on: `type`
  - only exists when: `type` = *Page blobs (Unmanaged Disks included)*

- **`Read operations (in 10,000s)`** (number)
  - depends on: `type`
  - only exists when: `type` = *Page blobs (Unmanaged Disks included)*

- **`Read additional IO units (in 10,000s)`** (number)
  - depends on: `type`
  - only exists when: `type` = *Page blobs (Unmanaged Disks included)*

- **`Delete operations (in 10,000s)`** (number)
  - depends on: `type`
  - only exists when: `type` = *Page blobs (Unmanaged Disks included)*

- **`x 100 operations`** (number)
  - depends on: `fileStructure`
  - only exists when: `fileStructure` = *Hierarchical Namespace*

- **`Operations`** (number)
  - depends on: `accessTier`
  - only exists when: `accessTier` = *Archive*

- **`blobArchiveRetrieval`** (number)
  - depends on: `accessTier`, `redundancy`
  - only exists when: `accessTier` = *Archive*

- **`blobArchiveRetrievalUnits`** (select)
  - depends on: `accessTier`, `redundancy`
  - only exists when: `accessTier` = *Archive*
  - options: GB, TB

- **`TB`** (number)
  - depends on: `storageUnits`
  - only exists when: `storageUnits` = *TB*

- **`TB (storageUnits)`** (select)
  - depends on: `storageUnits`
  - only exists when: `storageUnits` = *TB*
  - options: GB, TB

- **`TB (blobDataRetrieval)`** (number)
  - depends on: `blobDataRetrievalUnits`
  - only exists when: `blobDataRetrievalUnits` = *TB*

- **`TB (blobDataRetrievalUnits)`** (select)
  - depends on: `blobDataRetrievalUnits`
  - only exists when: `blobDataRetrievalUnits` = *TB*
  - options: GB, TB

- **`blobBillingOption`** (radio)
  - depends on: `type`
  - disappears when: `type` = *Table Storage*, `type` = *Queue Storage*
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved), `three-year` (3 year reserved)

## Example component

```json
{
  "product": "Storage",
  "name": "my-storage",
  "fields": {
    "Region": "Central US",
    "Type": "Block Blob Storage",
    "Performance": "Premium",
    "Storage Account Type": "General Purpose V2",
    "File Structure": "Flat Namespace"
  }
}
```
