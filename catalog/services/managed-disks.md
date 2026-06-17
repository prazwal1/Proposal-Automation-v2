# Managed Disks

- slug: `managed-disks`  |  module: `managed-disks-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Tier`** (select)
  - options: Standard HDD, Standard SSD, Premium SSD, Premium SSD v2, Ultra Disk

- **`Disk size`** (select)
  - depends on: `tier`
  - disappears when: `tier` = *Premium SSD v2*
  - options: S4: 32 GiB, 500 Provisioned IOPS, 60 Provisioned MB/s, S6: 64 GiB, 500 Provisioned IOPS, 60 Provisioned MB/s, S10: 128 GiB, 500 Provisioned IOPS, 60 Provisioned MB/s, S15: 256 GiB, 500 Provisioned IOPS, 60 Provisioned MB/s, S20: 512 GiB, 500 Provisioned IOPS, 60 Provisioned MB/s, S30: 1,024 GiB, 500 Provisioned IOPS, 60 Provisioned MB/s, S40: 2,048 GiB, 500 Provisioned IOPS, 60 Provisioned MB/s, S50: 4,096 GiB, 500 Provisioned IOPS, 60 Provisioned MB/s, S60: 8,192 GiB, 1,300 Provisioned IOPS, 300 Provisioned MB/s, S70: 16,384 GiB, 2,000 Provisioned IOPS, 500 Provisioned MB/s, S80: 32,767 GiB, 2,000 Provisioned IOPS, 500 Provisioned MB/s
  - when `tier` = *Standard SSD*: E1: 4 GiB, 500 Provisioned IOPS, 100 Provisioned MB/s, E2: 8 GiB, 500 Provisioned IOPS, 100 Provisioned MB/s, E3: 16 GiB, 500 Provisioned IOPS, 100 Provisioned MB/s, E4: 32 GiB, 500 Provisioned IOPS, 100 Provisioned MB/s, E6: 64 GiB, 500 Provisioned IOPS, 100 Provisioned MB/s, E10: 128 GiB, 500 Provisioned IOPS, 100 Provisioned MB/s, E15: 256 GiB, 500 Provisioned IOPS, 100 Provisioned MB/s, E20: 512 GiB, 500 Provisioned IOPS, 100 Provisioned MB/s, E30: 1,024 GiB, 500 Provisioned IOPS, 100 Provisioned MB/s, E40: 2,048 GiB, 500 Provisioned IOPS, 100 Provisioned MB/s, E50: 4,096 GiB, 500 Provisioned IOPS, 100 Provisioned MB/s, E60: 8,192 GiB, 2,000 Provisioned IOPS, 400 Provisioned MB/s, E70: 16,384 GiB, 4,000 Provisioned IOPS, 600 Provisioned MB/s, E80: 32,767 GiB, 6,000 Provisioned IOPS, 750 Provisioned MB/s
  - when `tier` = *Premium SSD*: P1: 4 GiB, 120 Provisioned IOPS, 25 Provisioned MB/s, P2: 8 GiB, 120 Provisioned IOPS, 25 Provisioned MB/s, P3: 16 GiB, 120 Provisioned IOPS, 25 Provisioned MB/s, P4: 32 GiB, 120 Provisioned IOPS, 25 Provisioned MB/s, P6: 64 GiB, 240 Provisioned IOPS, 50 Provisioned MB/s, P10: 128 GiB, 500 Provisioned IOPS, 100 Provisioned MB/s, P15: 256 GiB, 1,100 Provisioned IOPS, 125 Provisioned MB/s, P20: 512 GiB, 2,300 Provisioned IOPS, 150 Provisioned MB/s, P30: 1,024 GiB, 5,000 Provisioned IOPS, 200 Provisioned MB/s, P40: 2,048 GiB, 7,500 Provisioned IOPS, 250 Provisioned MB/s, P50: 4,096 GiB, 7,500 Provisioned IOPS, 250 Provisioned MB/s, P60: 8,192 GiB, 16,000 Provisioned IOPS, 500 Provisioned MB/s, P70: 16,384 GiB, 18,000 Provisioned IOPS, 750 Provisioned MB/s, P80: 32,767 GiB, 20,000 Provisioned IOPS, 900 Provisioned MB/s

- **`Disks`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Premium SSD v2*

- **`Transaction units (10,000 transactions)`** (number)
  - depends on: `tier`
  - disappears when: `tier` = *Premium SSD*, `tier` = *Premium SSD v2*, `tier` = *Ultra Disk*

- **`Redundancy`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Standard SSD*, `tier` = *Premium SSD*
  - options: LRS, ZRS

- **`Disk Size (GiB)`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Premium SSD v2*

- **`Number of Disks`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Premium SSD v2*

- **`Hours`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Premium SSD v2*

- **`storageV2HoursFactor`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Premium SSD v2*
  - options: Hours, Days, Month

- **`Number of IOPS`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Premium SSD v2*

- **`MB/s`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Premium SSD v2*

- **`managedDiskBillingOption`** (radio)
  - depends on: `tier`
  - only exists when: `tier` = *Premium SSD*
  - choices: `payg` (Pay as you go), `one-year` (1 year reserved)

## Example component

```json
{
  "product": "Managed Disks",
  "name": "my-managed-disks",
  "fields": {
    "Region": "Central US",
    "Tier": "Standard HDD",
    "Disk size": "S4: 32 GiB, 500 Provisioned IOPS, 60 Provisioned MB/s",
    "Disks": 1,
    "Transaction units (10,000 transactions)": 1
  }
}
```
