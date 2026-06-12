# Openai Service

- slug: `openai-service`  |  module: `openai-service-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (39): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE North, Switzerland North, Switzerland West, Sweden Central, ...

- **`Model type`** (select)
  - options: Language Models, Computer-Using Agent (CUA), Built-in Tools, Base Models, Fine-tuning Models, Image Models, Embedding Models, Speech Models

- **`Model`** (select)
  - depends on: `selectedModelSeries`
  - options (43): o1 Preview, o1 mini, GPT-4o-2024-08-06, GPT-4o-128K, GPT-4o-mini, GPT-3.5-Turbo-0125-16K, GPT-3.5-Turbo-Instruct-4K, GPT-4-Turbo-128K, GPT-4-Turbo-Vision-128K, GPT-4-8K, GPT-4-32K, GPT-3.5-Turbo-0301-4K, GPT-3.5-Turbo-0613-4K, GPT-3.5-Turbo-0613-16K, GPT-3.5-Turbo-1106-16K, ...

- **`Pricing Strategy`** (select)
  - depends on: `selectedModelSeries`
  - disappears when: `selectedModelSeries` = *Computer-Using Agent (CUA)*, `selectedModelSeries` = *Built-in Tools*, `selectedModelSeries` = *Base Models*, `selectedModelSeries` = *Fine-tuning Models*, `selectedModelSeries` = *Image Models*, `selectedModelSeries` = *Embedding Models*
  - options: Provisioned (PTU), Standard (On-Demand), Batch (On-Demand)

- **`Deployment type`** (select)
  - depends on: `selectedModelSeries`, `pricingStrategy`
  - disappears when: `selectedModelSeries` = *Computer-Using Agent (CUA)*, `selectedModelSeries` = *Built-in Tools*, `selectedModelSeries` = *Base Models*, `selectedModelSeries` = *Fine-tuning Models*, `selectedModelSeries` = *Image Models*, `selectedModelSeries` = *Embedding Models*
  - options: Global, Data Zone, Regional
  - when `pricingStrategy` = *Batch (On-Demand)*: Global

- **`x1,000 tokens`** (number)
  - depends on: `selectedModelSeries`
  - disappears when: `selectedModelSeries` = *Base Models*, `selectedModelSeries` = *Fine-tuning Models*, `selectedModelSeries` = *Image Models*

- **`completion`** (number)
  - depends on: `selectedModelSeries`, `pricingStrategy`
  - disappears when: `selectedModelSeries` = *Base Models*, `selectedModelSeries` = *Fine-tuning Models*, `selectedModelSeries` = *Image Models*, `selectedModelSeries` = *Embedding Models*, `selectedModelSeries` = *Speech Models*, `pricingStrategy` = *Provisioned (PTU)*

- **`x100 images`** (number)
  - depends on: `selectedModelSeries`
  - only exists when: `selectedModelSeries` = *Image Models*

- **`PTUs`** (number)
  - depends on: `pricingStrategy`
  - only exists when: `pricingStrategy` = *Provisioned (PTU)*

- **`Hours`** (number)
  - depends on: `pricingStrategy`
  - only exists when: `pricingStrategy` = *Provisioned (PTU)*

- **`pricingHoursFactor`** (select)
  - depends on: `pricingStrategy`
  - only exists when: `pricingStrategy` = *Provisioned (PTU)*
  - options: Hours, Days, Month

- **`billingOption`** (radio)
  - depends on: `pricingStrategy`
  - only exists when: `pricingStrategy` = *Provisioned (PTU)*
  - choices: `payg` (Pay as you go), `p1m` (1 month reserved), `p1y` (1 year reserved)

## Example component

```json
{
  "product": "Openai Service",
  "name": "my-openai-service",
  "fields": {
    "Region": "Central US",
    "Model type": "Language Models",
    "Model": "o1 Preview",
    "Pricing Strategy": "Provisioned (PTU)",
    "Deployment type": "Global"
  }
}
```
