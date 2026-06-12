# Form Recognizer

- slug: `form-recognizer`  |  module: `form-recognizer-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (35): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UAE North, Switzerland North, Switzerland West, Sweden Central, Spain Central, ...

- **`Payment Option`** (select)
  - options: Pay as you go, Commitment Tier

- **`Instance`** (select)
  - depends on: `formRecognizerPaymentOption`
  - options: Free, S0
  - when `formRecognizerPaymentOption` = *Commitment Tier*: Azure standard, Connected Container, Disconnected Container

- **`Feature`** (select)
  - depends on: `formRecognizerPaymentOption`
  - only exists when: `formRecognizerPaymentOption` = *Commitment Tier*
  - options: Custom, Pre-built, Read

- **`Commitment tier`** (select)
  - depends on: `formRecognizerPaymentOption`
  - only exists when: `formRecognizerPaymentOption` = *Commitment Tier*
  - options: Commitment tier $540 per 20,000 pages, Commitment tier $2,400 per 100,000 pages, Commitment tier $10,500 per 500,000 pages

- **`x 1,000 pages per month`** (number)
  - depends on: `formRecognizerPaymentOption`
  - only exists when: `formRecognizerPaymentOption` = *Commitment Tier*

- **`x1,000 Pages`** (number)
  - depends on: `formRecognizerTier`
  - only exists when: `formRecognizerTier` = *S0*

- **`formRecognizerPagesPrebuiltTransactions`** (number)
  - depends on: `formRecognizerTier`
  - only exists when: `formRecognizerTier` = *S0*

- **`customClassification`** (number)
  - depends on: `formRecognizerTier`
  - only exists when: `formRecognizerTier` = *S0*

- **`formRecognizerPagesTransactions`** (number)
  - depends on: `formRecognizerTier`
  - only exists when: `formRecognizerTier` = *S0*

- **`formRecognizerPagesAddonTransactions`** (number)
  - depends on: `formRecognizerTier`
  - only exists when: `formRecognizerTier` = *S0*

- **`formRecognizerPagesQueryTransactions`** (number)
  - depends on: `formRecognizerTier`
  - only exists when: `formRecognizerTier` = *S0*

- **`paidTraining`** (number)
  - depends on: `formRecognizerTier`
  - only exists when: `formRecognizerTier` = *S0*

- **`Minutes`** (number)
  - depends on: `formRecognizerTier`
  - only exists when: `formRecognizerTier` = *S0*

- **`paidTrainingHoursFactor`** (select)
  - depends on: `formRecognizerTier`
  - only exists when: `formRecognizerTier` = *S0*
  - options: Minutes, Hours

## Example component

```json
{
  "product": "Form Recognizer",
  "name": "my-form-recognizer",
  "fields": {
    "Region": "Central US",
    "Payment Option": "Pay as you go",
    "Instance": "Free"
  }
}
```
