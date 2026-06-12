# Media Services

- slug: `media-services`  |  module: `media-services-module`

## Fields

- **`product-name`** (text)

- **`Region`** (select)
  - options (49): Central US, East US, East US 2, North Central US, South Central US, West Central US, West US, West US 2, West US 3, UK South, UK West, UAE Central, UAE North, Switzerland North, Switzerland West, ...

- **`Type`** (select)
  - options: Video on Demand (VoD) Encoding, Streaming, Live Video, Content Protection

- **`Encoder type`** (select)
  - depends on: `service`
  - disappears when: `service` = *Streaming*, `service` = *Live Video*, `service` = *Content Protection*
  - options: Standard

- **`Codec Type`** (select)
  - depends on: `service`
  - disappears when: `service` = *Streaming*, `service` = *Live Video*, `service` = *Content Protection*
  - options: H.264, HEVC(H.265)

- **`Video output quality`** (select)
  - depends on: `service`, `codecType`
  - disappears when: `service` = *Streaming*, `service` = *Live Video*, `service` = *Content Protection*
  - options: SD (less than 1280×720), HD (at least 1280x720, up to 1920x1080), 4K (more than 1920x1080, up to 4096x2304)
  - when `codecType` = *HEVC(H.265)*: SD (less than 1280×720), HD (at least 1280x720, up to 1920x1080), 4K (more than 1920x1080, up to 4096x2304), 8K (more than 4096x2304, up to 8192x2608)

- **`Total Minutes Of Content`** (number)
  - depends on: `service`
  - disappears when: `service` = *Streaming*, `service` = *Live Video*, `service` = *Content Protection*

- **`Tier`** (select)
  - depends on: `service`
  - only exists when: `service` = *Streaming*
  - options: Premium streaming units, Standard streaming endpoint

- **`Live encoding type`** (select)
  - depends on: `service`
  - only exists when: `service` = *Live Video*
  - options: Live Transcriptions, Running Basic Pass-through, Running Pass-through, Running Premium Live Encoding, Running Standard Live Encoding, Standby Basic Pass-through, Standby Pass-through, Standby Premium Live Encoding, Standby Standard Live Encoding

- **`Hours`** (number)
  - depends on: `service`
  - only exists when: `service` = *Live Video*

- **`Units of 100 keys`** (number)
  - depends on: `service`
  - only exists when: `service` = *Content Protection*

- **`Units of 100 licenses`** (number)
  - depends on: `service`
  - only exists when: `service` = *Content Protection*

- **`contentProtectionWidevine`** (number)
  - depends on: `service`
  - only exists when: `service` = *Content Protection*

- **`contentProtectionFairplay`** (number)
  - depends on: `service`
  - only exists when: `service` = *Content Protection*

- **`Preset`** (select)
  - depends on: `codecType`
  - only exists when: `codecType` = *HEVC(H.265)*
  - options: Speed Optimized, Balance Optimized, Quality Optimized

- **`Frame Rate`** (select)
  - depends on: `codecType`
  - only exists when: `codecType` = *HEVC(H.265)*
  - options: <=30 frames/sec, >30 frames/sec and <=60 frames/sec, >60 frames/sec and <=120 frames/sec

## Example component

```json
{
  "product": "Media Services",
  "name": "my-media-services",
  "fields": {
    "Region": "Central US",
    "Type": "Video on Demand (VoD) Encoding",
    "Encoder type": "Standard",
    "Codec Type": "H.264",
    "Video output quality": "SD (less than 1280\u00d7720)"
  }
}
```
