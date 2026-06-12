# Static

- slug: `app-service--static`  |  module: `app-service\static-module`

## Fields

- **`product-name`** (text)

- **`Tier`** (select)
  - options: Free, Standard

- **`App`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`GB`** (number)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*

- **`standardBandwidthOveragesFactor`** (select)
  - depends on: `tier`
  - only exists when: `tier` = *Standard*
  - options: GB, TB

## Example component

```json
{
  "product": "Static",
  "name": "my-app-service--static",
  "fields": {
    "Tier": "Free"
  }
}
```
