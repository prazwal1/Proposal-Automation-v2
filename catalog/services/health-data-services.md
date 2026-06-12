# Health Data Services

- slug: `health-data-services`  |  module: `health-data-services-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (25): East US, East US 2, North Central US, South Central US, West Central US, West US 2, West US 3, UK South, UK West, Switzerland North, Sweden Central, Qatar Central, Korea Central, Japan East, Central India, ...

- **`API`** (select)
  - options: Azure API for FHIR, Azure Health Data Services

- **`GB`** (number)
  - depends on: `api`

- **`structuredStorageFactorHealthcare`** (select)
  - depends on: `api`
  - options: GB, TB

- **`blobStorage`** (number)
  - depends on: `api`, `blobStorageFactor`
  - disappears when: `api` = *Azure API for FHIR*, `blobStorageFactor` = *TB*

- **`blobStorageFactor`** (select)
  - depends on: `api`, `blobStorageFactor`
  - disappears when: `api` = *Azure API for FHIR*, `blobStorageFactor` = *TB*
  - options: GB, TB

- **`x100K requests`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`Size of each request (KB)`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`Requests per month`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`transformCcdaSize`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`transformCcdaOperations`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`transformJsonSize`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`transformJsonOperations`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`transformMedicalSize`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`transformMedicalOperations`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`Size of each resource (KB)`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`Resource per month`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`structuredDeidentificationSize`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`structuredDeidentificationOperations`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`Size of each image (KB)`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`Images per month`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`exportBatch`** (number)
  - depends on: `api`, `exportBatchFactor`
  - disappears when: `api` = *Azure API for FHIR*, `exportBatchFactor` = *TB*

- **`exportBatchFactor`** (select)
  - depends on: `api`, `exportBatchFactor`
  - disappears when: `api` = *Azure API for FHIR*, `exportBatchFactor` = *TB*
  - options: GB, TB

- **`x1 million events`** (number)
  - depends on: `api`
  - disappears when: `api` = *Azure API for FHIR*

- **`Hours`** (number)
  - depends on: `api`
  - only exists when: `api` = *Azure API for FHIR*

- **`serviceRuntimeHoursFactor`** (select)
  - depends on: `api`
  - only exists when: `api` = *Azure API for FHIR*
  - options: Hours, Days, Month

- **`x 100 RU/sec`** (number)
  - depends on: `api`
  - only exists when: `api` = *Azure API for FHIR*

- **`provisionedRUsHours`** (number)
  - depends on: `api`
  - only exists when: `api` = *Azure API for FHIR*

- **`provisionedRUsHoursFactor`** (select)
  - depends on: `api`
  - only exists when: `api` = *Azure API for FHIR*
  - options: Hours, Days, Month

- **`TB`** (number)
  - depends on: `structuredStorageFactorHealthcare`
  - only exists when: `structuredStorageFactorHealthcare` = *TB*

- **`TB (structuredStorageFactorHealthcare)`** (select)
  - depends on: `structuredStorageFactorHealthcare`
  - only exists when: `structuredStorageFactorHealthcare` = *TB*
  - options: GB, TB

- **`TB (blobStorage)`** (number)
  - depends on: `blobStorageFactor`
  - only exists when: `blobStorageFactor` = *TB*

- **`TB (blobStorageFactor)`** (select)
  - depends on: `blobStorageFactor`
  - only exists when: `blobStorageFactor` = *TB*
  - options: GB, TB

- **`TB (exportBatch)`** (number)
  - depends on: `exportBatchFactor`
  - only exists when: `exportBatchFactor` = *TB*

- **`TB (exportBatchFactor)`** (select)
  - depends on: `exportBatchFactor`
  - only exists when: `exportBatchFactor` = *TB*
  - options: GB, TB

## Example component

```json
{
  "product": "Health Data Services",
  "name": "my-health-data-services",
  "fields": {
    "Region": "East US",
    "API": "Azure API for FHIR",
    "GB": 1,
    "structuredStorageFactorHealthcare": "GB",
    "blobStorage": 1
  }
}
```
