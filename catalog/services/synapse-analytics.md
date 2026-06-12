# Synapse Analytics

- slug: `synapse-analytics`  |  module: `synapse-analytics-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Performance Tier`** (select)
  - options: Compute Optimized Gen1, Compute Optimized Gen2

- **`DWU blocks`** (select)
  - depends on: `tier`
  - options (16): 100, 200, 300, 400, 500, 1000, 1500, 2000, 2500, 3000, 5000, 6000, 7500, 10000, 15000, ...
  - when `tier` = *Compute Optimized Gen1*: 100, 200, 300, 400, 500, 600, 1000, 1200, 1500, 2000, ...

- **`Hours`** (number)
  - depends on: `computeHoursFactor`
  - disappears when: `computeHoursFactor` = *Days*

- **`computeHoursFactor`** (select)
  - depends on: `computeHoursFactor`
  - disappears when: `computeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`TB`** (number)

- **`serverlessUnits`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`Node size`** (select)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*
  - options: Small (4 vCores / 32 GB), Medium (8 vCores / 64 GB), Large (16 vCores / 128 GB), XLarge (32 vCores / 256 GB), XXLarge (64 vCores / 432 GB)

- **`Instances`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`sparkMemoryOptimizedHours`** (number)
  - depends on: `tier`, `sparkMemoryOptimizedHoursFactor`
  - disappears when: `tier` = *Compute Optimized Gen1*, `sparkMemoryOptimizedHoursFactor` = *Days*

- **`sparkMemoryOptimizedHoursFactor`** (select)
  - depends on: `tier`, `sparkMemoryOptimizedHoursFactor`
  - disappears when: `tier` = *Compute Optimized Gen1*, `sparkMemoryOptimizedHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`sparkHardwareAcceleratedInstance`** (select)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*
  - options: Large (16 vCores / 112 GB), XLarge (64 vCores / 448 GB)

- **`sparkHardwareAcceleratedUnits`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`sparkHardwareAcceleratedHours`** (number)
  - depends on: `tier`, `sparkHardwareAcceleratedHoursFactor`
  - disappears when: `tier` = *Compute Optimized Gen1*, `sparkHardwareAcceleratedHoursFactor` = *Days*

- **`sparkHardwareAcceleratedHoursFactor`** (select)
  - depends on: `tier`, `sparkHardwareAcceleratedHoursFactor`
  - disappears when: `tier` = *Compute Optimized Gen1*, `sparkHardwareAcceleratedHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`GB`** (number)
  - depends on: `dataCollectedUnitFactor`
  - disappears when: `dataCollectedUnitFactor` = *TB*

- **`dataCollectedUnitFactor`** (select)
  - depends on: `dataCollectedUnitFactor`
  - disappears when: `dataCollectedUnitFactor` = *TB*
  - options: GB, TB

- **`Hot Cache retention (days)`** (number)

- **`Total retention (days)`** (number)

- **`Estimated Data Compression`** (number)

- **`engineInstanceHours`** (number) — section: *Engine vCores* (opened automatically)
  - depends on: `engineInstanceHoursFactor`
  - disappears when: `engineInstanceHoursFactor` = *Days*

- **`engineInstanceHoursFactor`** (select) — section: *Engine vCores* (opened automatically)
  - depends on: `engineInstanceHoursFactor`
  - disappears when: `engineInstanceHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`dataManagementHours`** (number) — section: *Data Management vCores* (opened automatically)
  - depends on: `dataManagementHoursFactor`
  - disappears when: `dataManagementHoursFactor` = *Days*

- **`dataManagementHoursFactor`** (select) — section: *Data Management vCores* (opened automatically)
  - depends on: `dataManagementHoursFactor`
  - disappears when: `dataManagementHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Activity Runs (X 1,000)`** (number) — section: *Azure-Hosted* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`Data Integration Unit`** (number) — section: *Azure-Hosted* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`azureHostedExecutionHours`** (number) — section: *Azure-Hosted* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`azureHostedExecutionHoursFactor`** (select) — section: *Azure-Hosted* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*
  - options: Hours, Days, Month

- **`Integration Hours`** (number) — section: *Azure-Hosted* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`azureHostedExternalIntegrationRuntimeUnits`** (number) — section: *Azure-Hosted* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`azureVnetHostedOrchestrationUnits`** (number) — section: *Azure-Hosted Managed VNET* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`azureVnetHostedExecutionUnits`** (number) — section: *Azure-Hosted Managed VNET* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`azureVnetHostedExecutionHours`** (number) — section: *Azure-Hosted Managed VNET* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`azureVnetHostedExecutionHoursFactor`** (select) — section: *Azure-Hosted Managed VNET* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*
  - options: Hours, Days, Month

- **`azureVnetHostedIntegrationRuntimeUnits`** (number) — section: *Azure-Hosted Managed VNET* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`azureVnetHostedExternalIntegrationRuntimeUnits`** (number) — section: *Azure-Hosted Managed VNET* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`selfHostedOrchestrationUnits`** (number) — section: *Self-Hosted* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`selfHostedExecutionHours`** (number) — section: *Self-Hosted* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`selfHostedExecutionHoursFactor`** (select) — section: *Self-Hosted* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*
  - options: Hours, Days, Month

- **`selfHostedIntegrationRuntimeUnits`** (number) — section: *Self-Hosted* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`selfHostedExternalIntegrationRuntimeUnits`** (number) — section: *Self-Hosted* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`Instance`** (select) — section: *Data Flows* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*
  - options: 8 vCores, 12 vCores, 20 vCores, 36 vCores, 68 vCores

- **`basicVcoreUnits`** (number) — section: *Data Flows* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`basicVcoreHours`** (number) — section: *Data Flows* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`basicVcoreHoursFactor`** (select) — section: *Data Flows* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*
  - options: Hours, Days, Month

- **`standardVcoreInstance`** (select) — section: *Data Flows* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*
  - options: 8 vCores, 12 vCores, 20 vCores, 36 vCores, 68 vCores

- **`standardVcoreUnits`** (number) — section: *Data Flows* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`standardVcoreHours`** (number) — section: *Data Flows* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*

- **`standardVcoreHoursFactor`** (select) — section: *Data Flows* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `computeHoursFactor`
  - only exists when: `computeHoursFactor` = *Days*

- **`Days (computeHoursFactor)`** (select)
  - depends on: `computeHoursFactor`
  - only exists when: `computeHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (sparkMemoryOptimizedHours)`** (number)
  - depends on: `sparkMemoryOptimizedHoursFactor`
  - only exists when: `sparkMemoryOptimizedHoursFactor` = *Days*

- **`Days (sparkMemoryOptimizedHoursFactor)`** (select)
  - depends on: `sparkMemoryOptimizedHoursFactor`
  - only exists when: `sparkMemoryOptimizedHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (sparkHardwareAcceleratedHours)`** (number)
  - depends on: `sparkHardwareAcceleratedHoursFactor`
  - only exists when: `sparkHardwareAcceleratedHoursFactor` = *Days*

- **`Days (sparkHardwareAcceleratedHoursFactor)`** (select)
  - depends on: `sparkHardwareAcceleratedHoursFactor`
  - only exists when: `sparkHardwareAcceleratedHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`dataCollectedUnit`** (number)
  - depends on: `dataCollectedUnitFactor`
  - only exists when: `dataCollectedUnitFactor` = *TB*

- **`TB (dataCollectedUnitFactor)`** (select)
  - depends on: `dataCollectedUnitFactor`
  - only exists when: `dataCollectedUnitFactor` = *TB*
  - options: GB, TB

- **`Days (engineInstanceHours)`** (number)
  - depends on: `engineInstanceHoursFactor`
  - only exists when: `engineInstanceHoursFactor` = *Days*

- **`Days (engineInstanceHoursFactor)`** (select)
  - depends on: `engineInstanceHoursFactor`
  - only exists when: `engineInstanceHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (dataManagementHours)`** (number)
  - depends on: `dataManagementHoursFactor`
  - only exists when: `dataManagementHoursFactor` = *Days*

- **`Days (dataManagementHoursFactor)`** (select)
  - depends on: `dataManagementHoursFactor`
  - only exists when: `dataManagementHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`billingOption`** (radio)
  - depends on: `tier`
  - disappears when: `tier` = *Compute Optimized Gen1*
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved (~37% savings)), `three-year` (3 year reserved (~65% savings))

## Example component

```json
{
  "product": "Synapse Analytics",
  "name": "my-synapse-analytics",
  "fields": {
    "Region": "Central US",
    "Performance Tier": "Compute Optimized Gen1",
    "DWU blocks": "100",
    "Hours": 1,
    "computeHoursFactor": "Hours"
  }
}
```
