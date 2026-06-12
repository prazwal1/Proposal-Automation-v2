# Energy Data Services

- slug: `energy-data-services`  |  module: `energy-data-services-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (16): East US, South Central US, West Central US, West US 2, UAE North, Sweden Central, Qatar Central, Malaysia West, Indonesia Central, Central India, North Europe, West Europe, Brazil South, Australia East, Southeast Asia, ...

- **`Tier`** (select)
  - options: Standard, Developer

- **`Instances`** (number)

- **`Hours`** (number)
  - depends on: `baseInstanceHoursFactor`
  - disappears when: `baseInstanceHoursFactor` = *Days*

- **`baseInstanceHoursFactor`** (select)
  - depends on: `baseInstanceHoursFactor`
  - disappears when: `baseInstanceHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Additional partitions per instance`** (number)

- **`additionalDataPartitionHours`** (number)
  - depends on: `additionalDataPartitionHoursFactor`
  - disappears when: `additionalDataPartitionHoursFactor` = *Days*

- **`additionalDataPartitionHoursFactor`** (select)
  - depends on: `additionalDataPartitionHoursFactor`
  - disappears when: `additionalDataPartitionHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `baseInstanceHoursFactor`
  - only exists when: `baseInstanceHoursFactor` = *Days*

- **`Days (baseInstanceHoursFactor)`** (select)
  - depends on: `baseInstanceHoursFactor`
  - only exists when: `baseInstanceHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days (additionalDataPartitionHours)`** (number)
  - depends on: `additionalDataPartitionHoursFactor`
  - only exists when: `additionalDataPartitionHoursFactor` = *Days*

- **`Days (additionalDataPartitionHoursFactor)`** (select)
  - depends on: `additionalDataPartitionHoursFactor`
  - only exists when: `additionalDataPartitionHoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Energy Data Services",
  "name": "my-energy-data-services",
  "fields": {
    "Region": "East US",
    "Tier": "Standard",
    "Instances": 1,
    "Hours": 1,
    "baseInstanceHoursFactor": "Hours"
  }
}
```
