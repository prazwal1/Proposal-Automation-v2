# Netapp

- slug: `netapp`  |  module: `netapp-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (53): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Service Level`** (select)
  - options: Standard Storage, Premium Storage, Ultra Storage, Flexible Storage, Elastic Storage (Preview)

- **`Encryption`** (select)
  - depends on: `tier`
  - options: Single Encryption, Double Encryption

- **`Cool Access`** (select)
  - depends on: `tier`
  - options: No, Yes

- **`TiB`** (number)
  - depends on: `tier`

- **`Hours`** (number)
  - depends on: `tier`, `coolAccessStatus`

- **`standardHoursFactor`** (select)
  - depends on: `tier`, `coolAccessStatus`
  - options: Hours, Days, Month

- **`Capacity pools`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Flexible Storage*

- **`MiB/sec`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Flexible Storage*

- **`Percentage in cool access (%)`** (number)
  - depends on: `coolAccessStatus`
  - only exists when: `coolAccessStatus` = *Yes*

- **`Cool access data read/write percentage (%)`** (number)
  - depends on: `coolAccessStatus`
  - only exists when: `coolAccessStatus` = *Yes*

- **`Days`** (number)
  - depends on: `standardHoursFactor`
  - only exists when: `standardHoursFactor` = *Days*

- **`Days (standardHoursFactor)`** (select)
  - depends on: `standardHoursFactor`
  - only exists when: `standardHoursFactor` = *Days*
  - options: Hours, Days, Month

- **`standardStorageBillingOption`** (radio)
  - depends on: `tier`
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved), `three-year` (3 year reserved)

## Example component

```json
{
  "product": "Netapp",
  "name": "my-netapp",
  "fields": {
    "Region": "Central US",
    "Service Level": "Standard Storage",
    "Encryption": "Single Encryption",
    "Cool Access": "No",
    "TiB": 1
  }
}
```
