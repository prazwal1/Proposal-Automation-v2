# Video Indexer

- slug: `video-indexer`  |  module: `video-indexer-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (49): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Analysis Type`** (select)
  - options: All insights, Only audio insights, Only video insights

- **`Analysis Mode`** (select)
  - depends on: `analysisType`
  - disappears when: `analysisType` = *Only audio insights*, `analysisType` = *Only video insights*
  - options: Basic, Standard, Advanced

- **`Total Minutes of content`** (number)

- **`Total content minutes`** (number)

- **`Audio Analysis Mode`** (select)
  - depends on: `analysisType`
  - only exists when: `analysisType` = *Only audio insights*
  - options: Basic, Standard, Advanced

- **`Video Analysis Mode`** (select)
  - depends on: `analysisType`
  - only exists when: `analysisType` = *Only video insights*
  - options: Basic, Standard, Advanced

## Example component

```json
{
  "product": "Video Indexer",
  "name": "my-video-indexer",
  "fields": {
    "Region": "Central US",
    "Analysis Type": "All insights",
    "Analysis Mode": "Basic",
    "Total Minutes of content": 1,
    "Total content minutes": 1
  }
}
```
