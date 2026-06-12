# Cognitive Services

- slug: `cognitive-services`  |  module: `cognitive-services-module`

## Fields

- **`product-name`** (text)

- **`API`** (select)
  - options: Azure AI Custom Vision, Azure AI Immersive Reader, Azure Language in Foundry Tools, Azure Speech in Foundry Tools, Azure Translator in Foundry Tools, Azure Vision in Foundry Tools, Content Safety in Foundry Control Plane, Face API, QnA Maker

- **`Region`** (select)
  - depends on: `api`
  - options (60): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...
  - when `api` = *Azure AI Custom Vision*: Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, ...
  - when `api` = *Azure AI Immersive Reader*: Central US, East US, North Central US, West US, UAE North, Switzerland North, Switzerland West, Korea Central, Japan East, Japan West, ...
  - when `api` = *Azure Vision in Foundry Tools*: Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, ...
  - when `api` = *Content Safety in Foundry Control Plane*: Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, ...
  - when `api` = *Face API*: Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, ...

- **`Payment Option`** (select)
  - depends on: `api`
  - disappears when: `api` = *Azure AI Custom Vision*, `api` = *Azure AI Immersive Reader*
  - options: Pay as you go, Commitment tiers

- **`Instance`** (select)
  - depends on: `api`, `languageServiceType`
  - options: Free:, Standard
  - when `languageServiceType` = *Commitment tiers*: Azure standard, Connected container

- **`Tier`** (select)
  - depends on: `api`
  - only exists when: `api` = *Azure AI Immersive Reader*
  - options: Standard, Education/Nonprofit

- **`x1 million characters`** (number)
  - depends on: `api`
  - only exists when: `api` = *Azure AI Immersive Reader*

- **`x1,000 transactions per month`** (number)
  - depends on: `api`
  - only exists when: `api` = *Face API*

- **`x1,000 faces stored`** (number)
  - depends on: `api`
  - only exists when: `api` = *Face API*

- **`Number of retrains`** (number)
  - depends on: `api`
  - only exists when: `api` = *Face API*

- **`x1,000 transactions`** (number)
  - depends on: `api`
  - only exists when: `api` = *Face API*

- **`faceLivelinessVerification`** (number)
  - depends on: `api`
  - only exists when: `api` = *Face API*

- **`Commitment tier`** (select)
  - depends on: `languageServiceType`
  - only exists when: `languageServiceType` = *Commitment tiers*
  - options: - Select a tier -, Commitment tier $700 per 1 million text records, Commitment tier $1,375 per 3 million text records, Commitment tier $3,500 per 10 million text records

- **`x 1,000 text records per month`** (number)
  - depends on: `languageServiceType`, `languageServiceSize`
  - only exists when: `languageServiceType` = *Commitment tiers*

- **`summarizationAzureStandardCommitmentTier`** (select)
  - depends on: `languageServiceType`
  - only exists when: `languageServiceType` = *Commitment tiers*
  - options: - Select a tier -, Commitment tier $3,300 per 3 million text records, Commitment tier $7,000 per 10 million text records

- **`summarizationAzureStandardTextRecordsOverage`** (number)
  - depends on: `languageServiceType`
  - only exists when: `languageServiceType` = *Commitment tiers*

- **`Training hours per month`** (number)
  - depends on: `languageServiceSize`
  - only exists when: `languageServiceSize` = *Standard*

- **`Endpoint hosting models per month`** (number)
  - depends on: `languageServiceSize`
  - only exists when: `languageServiceSize` = *Standard*

- **`x 1,000 text records`** (number)
  - depends on: `languageServiceSize`
  - only exists when: `languageServiceSize` = *Standard*

- **`Advanced training hours`** (number)
  - depends on: `languageServiceSize`
  - only exists when: `languageServiceSize` = *Standard*

## Example component

```json
{
  "product": "Cognitive Services",
  "name": "my-cognitive-services",
  "fields": {
    "API": "Azure AI Custom Vision",
    "Region": "Central US",
    "Payment Option": "Pay as you go",
    "Instance": "Free:"
  }
}
```
