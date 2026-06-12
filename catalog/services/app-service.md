# App Service

- slug: `app-service`  |  module: `app-service-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Operating system`** (select)
  - options: Windows, Linux

- **`Tier`** (select)
  - depends on: `type`
  - options: Free, Shared, Basic, Standard, Premium V2, Premium V3, Premium V4, Isolated V4, Isolated V2 (Use for ASEv3), Isolated V2 (Dedicated Host)
  - when `type` = *Linux*: Free, Basic, Standard, Premium V2, Premium V3, Premium V4, Isolated V4, Isolated V2 (Use for ASEv3), Isolated V2 (Dedicated Host)

- **`Instance`** (select)
  - depends on: `type`, `tier`
  - disappears when: `tier` = *Isolated V4*, `tier` = *Isolated V2 (Use for ASEv3)*, `tier` = *Isolated V2 (Dedicated Host)*
  - options: B1: 1 Cores(s), 1.75 GB RAM, 10 GB Storage, $0.075, B2: 2 Cores(s), 3.5 GB RAM, 10 GB Storage, $0.150, B3: 4 Cores(s), 7 GB RAM, 10 GB Storage, $0.300
  - when `type` = *Linux*: B1: 1 Cores(s), 1.75 GB RAM, 10 GB Storage, $0.018, B2: 2 Cores(s), 3.5 GB RAM, 10 GB Storage, $0.036, B3: 4 Cores(s), 7 GB RAM, 10 GB Storage, $0.071
  - when `tier` = *Free*: F1: Shared Cores(s), 1 GB RAM, 1 GB Storage, $0.000
  - when `tier` = *Shared*: D1: Shared Cores(s), 1 GB RAM, 1 GB Storage, $0.013
  - when `tier` = *Standard*: S1: 1 Cores(s), 1.75 GB RAM, 50 GB Storage, $0.100, S2: 2 Cores(s), 3.5 GB RAM, 50 GB Storage, $0.200, S3: 4 Cores(s), 7 GB RAM, 50 GB Storage, $0.400
  - when `tier` = *Premium V2*: P1V2: 1 vCPU(s), 3.5 GB RAM, 250 GB Storage, $0.200, P2V2: 2 vCPU(s), 7 GB RAM, 250 GB Storage, $0.400, P3V2: 4 vCPU(s), 14 GB RAM, 250 GB Storage, $0.800
  - when `tier` = *Premium V3*: P0V3: 1 vCPU(s), 4 GB RAM, 250 GB Storage, $0.168, P1V3: 2 vCPU(s), 8 GB RAM, 250 GB Storage, $0.335, P1MV3: 2 vCPU(s), 16 GB RAM, 250 GB Storage, $0.370, P2V3: 4 vCPU(s), 16 GB RAM, 250 GB Storage, $0.670, P2MV3: 4 vCPU(s), 32 GB RAM, 250 GB Storage, $0.740, P3V3: 8 vCPU(s), 32 GB RAM, 250 GB Storage, $1.340, P3MV3: 8 vCPU(s), 64 GB RAM, 250 GB Storage, $1.480, P4MV3: 16 vCPU(s), 128 GB RAM, 250 GB Storage, $2.960, P5MV3: 32 vCPU(s), 256 GB RAM, 250 GB Storage, $5.920

- **`Instances`** (number)
  - depends on: `tier`

- **`Hours`** (number)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Connections`** (number) — section: *SSL Connections* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Free*, `tier` = *Shared*, `tier` = *Standard*, `tier` = *Premium V2*, `tier` = *Premium V3*, `tier` = *Premium V4*

- **`Domains`** (number) — section: *Custom Domain and Certificates* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Free*, `tier` = *Shared*, `tier` = *Standard*, `tier` = *Premium V2*, `tier` = *Premium V3*, `tier` = *Premium V4*

- **`Certificates`** (number) — section: *Custom Domain and Certificates* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Free*, `tier` = *Shared*, `tier` = *Standard*, `tier` = *Premium V2*, `tier` = *Premium V3*, `tier` = *Premium V4*

- **`wildcardCertificates`** (number) — section: *Custom Domain and Certificates* (opened automatically)
  - depends on: `tier`
  - disappears when: `tier` = *Free*, `tier` = *Shared*, `tier` = *Standard*, `tier` = *Premium V2*, `tier` = *Premium V3*, `tier` = *Premium V4*

- **`INSTANCE TYPE`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Isolated V4*, `tier` = *Isolated V2 (Use for ASEv3)*
  - options: I1v4: 2 vCPU(s), 8 GB RAM, 1024 GB Storage, $0.71, I1mv4: 2 vCPU(s), 16 GB RAM, 1024 GB Storage, $0.83, I2v4: 4 vCPU(s), 16 GB RAM, 1024 GB Storage, $1.43, I2mv4: 4 vCPU(s), 32 GB RAM, 1024 GB Storage, $1.65, I3v4: 8 vCPU(s), 32 GB RAM, 1024 GB Storage, $2.85, I3mv4: 8 vCPU(s), 64 GB RAM, 1024 GB Storage, $3.30, I4v4: 16 vCPU(s), 64 GB RAM, 1024 GB Storage, $5.70, I4mv4: 16 vCPU(s), 128 GB RAM, 1024 GB Storage, $6.60, I5v4: 32 vCPU(s), 128 GB RAM, 1024 GB Storage, $11.41, I5mv4: 32 vCPU(s), 256 GB RAM, 1024 GB Storage, $13.21, I6v4: 64 vCPU(s), 256 GB RAM, 1024 GB Storage, $22.82

- **`vCPU(s)`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Isolated V2 (Dedicated Host)*

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`billingOption`** (radio)
  - depends on: `tier`
  - only exists when: `tier` = *Premium V3*, `tier` = *Premium V4*, `tier` = *Isolated V4*, `tier` = *Isolated V2 (Dedicated Host)*
  - choices: `payg` (Pay as you go), `sv-one-year` (1 year savings plan (~13% discount)), `sv-three-year` (3 year savings plan (~24% discount)), `one-year` (1 year reserved (~25% discount)), `three-year` (3 year reserved (~40% discount))

## Example component

```json
{
  "product": "App Service",
  "name": "my-app-service",
  "fields": {
    "Region": "Central US",
    "Operating system": "Windows",
    "Tier": "Free",
    "Instance": "B1: 1 Cores(s), 1.75 GB RAM, 10 GB Storage, $0.075",
    "Instances": 1
  }
}
```
