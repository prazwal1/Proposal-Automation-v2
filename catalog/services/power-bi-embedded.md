# Power Bi Embedded

- slug: `power-bi-embedded`  |  module: `power-bi-embedded-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (40): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, Poland Central, ...

- **`Node type`** (select)
  - options: A1: 1 Virtual Core(s), 3GB RAM, $1.008, A2: 2 Virtual Core(s), 5GB RAM, $2.008, A3: 4 Virtual Core(s), 10GB RAM, $4.024, A4: 8 Virtual Core(s), 25GB RAM, $8.057, A5: 16 Virtual Core(s), 50GB RAM, $16.121, A6: 32 Virtual Core(s), 100GB RAM, $32.251, A7: 64 Virtual Core(s), 200GB RAM, $NaN, A8: 128 Virtual Core(s), 400GB RAM, $NaN

- **`Nodes`** (number)
  - depends on: `size`
  - disappears when: `size` = *A7: 64 Virtual Core(s), 200GB RAM, $NaN*, `size` = *A8: 128 Virtual Core(s), 400GB RAM, $NaN*

- **`Hours`** (number)
  - depends on: `size`, `hoursFactor`
  - disappears when: `size` = *A7: 64 Virtual Core(s), 200GB RAM, $NaN*, `size` = *A8: 128 Virtual Core(s), 400GB RAM, $NaN*, `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `size`, `hoursFactor`
  - disappears when: `size` = *A7: 64 Virtual Core(s), 200GB RAM, $NaN*, `size` = *A8: 128 Virtual Core(s), 400GB RAM, $NaN*, `hoursFactor` = *Days*
  - options: Hours, Days, Month

- **`Days`** (number)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*

- **`Days (hoursFactor)`** (select)
  - depends on: `hoursFactor`
  - only exists when: `hoursFactor` = *Days*
  - options: Hours, Days, Month

## Example component

```json
{
  "product": "Power Bi Embedded",
  "name": "my-power-bi-embedded",
  "fields": {
    "Region": "Central US",
    "Node type": "A1: 1 Virtual Core(s), 3GB RAM, $1.008",
    "Nodes": 1,
    "Hours": 1,
    "hoursFactor": "Hours"
  }
}
```
