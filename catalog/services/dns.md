# Dns

- slug: `dns`  |  module: `dns-module`

## Fields

- **`product-name`** (text)

- **`Zone`** (select)
  - options: Zone 1, Zone 2, Zone 3, Zone 4, US Gov Zone 1

- **`SKU`** (select)
  - options: DNS, DNS Private Resolver, DNS Security Policy

- **`Type`** (select)
  - depends on: `dnsSku`
  - disappears when: `dnsSku` = *DNS Private Resolver*, `dnsSku` = *DNS Security Policy*
  - options: Public, Private

- **`Hosted DNS zones`** (number)
  - depends on: `dnsSku`, `type`
  - disappears when: `dnsSku` = *DNS Private Resolver*, `dnsSku` = *DNS Security Policy*

- **`DNS queries (millions)`** (number)
  - depends on: `dnsSku`, `type`
  - disappears when: `dnsSku` = *DNS Private Resolver*, `dnsSku` = *DNS Security Policy*

- **`Number of Inbound endpoints`** (number)
  - depends on: `dnsSku`
  - only exists when: `dnsSku` = *DNS Private Resolver*

- **`Number of Outbound endpoints`** (number)
  - depends on: `dnsSku`
  - only exists when: `dnsSku` = *DNS Private Resolver*

- **`Number of rulesets`** (number)
  - depends on: `dnsSku`
  - only exists when: `dnsSku` = *DNS Private Resolver*

- **`x1 million queries`** (number)
  - depends on: `dnsSku`
  - only exists when: `dnsSku` = *DNS Security Policy*

- **`x1,000 domains`** (number)
  - depends on: `dnsSku`
  - only exists when: `dnsSku` = *DNS Security Policy*

## Example component

```json
{
  "product": "Dns",
  "name": "my-dns",
  "fields": {
    "Zone": "Zone 1",
    "SKU": "DNS",
    "Type": "Public",
    "Hosted DNS zones": 1,
    "DNS queries (millions)": 1
  }
}
```
