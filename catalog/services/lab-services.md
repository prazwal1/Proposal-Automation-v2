# Lab Services

- slug: `lab-services`  |  module: `lab-services-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (28): Central US, East US, East US 2, North Central US, South Central US, West US, West US 2, UK South, UK West, Sweden Central, Korea Central, Korea South, Japan East, Central India, South India, ...

- **`Instance`** (select)
  - options: Classroom Small: 2 Cores(s), 3.5 GB RAM, 20 Lab Units, $0.010 per hour per Lab Unit, Classroom Medium: 4 Cores(s), 7 GB RAM, 42 Lab Units, $0.010 per hour per Lab Unit, Classroom Medium (Nested Virtualization): 4 Cores(s), 16 GB RAM, 55 Lab Units, $0.010 per hour per Lab Unit, Classroom Small GPU (Compute): 6 Cores(s), 56 GB RAM, 139 Lab Units, $0.010 per hour per Lab Unit, Classroom Small GPU (Visualization): 6 Cores(s), 56 GB RAM, 160 Lab Units, $0.010 per hour per Lab Unit, Classroom Large (Nested Virtualization): 8 Cores(s), 32 GB RAM, 84 Lab Units, $0.010 per hour per Lab Unit, Classroom Large: 8 Cores(s), 16 GB RAM, 70 Lab Units, $0.010 per hour per Lab Unit, Classroom Medium GPU (Visualization): 12 Cores(s), 112 GB RAM, 408 Lab Units, $0.010 per hour per Lab Unit

- **`instances`** (number)

- **`Hours`** (number)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*

- **`hoursFactor`** (select)
  - depends on: `hoursFactor`
  - disappears when: `hoursFactor` = *Days*
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
  "product": "Lab Services",
  "name": "my-lab-services",
  "fields": {
    "Region": "Central US",
    "Instance": "Classroom Small: 2 Cores(s), 3.5 GB RAM, 20 Lab Units, $0.010 per hour per Lab Unit",
    "instances": 1,
    "Hours": 1,
    "hoursFactor": "Hours"
  }
}
```
