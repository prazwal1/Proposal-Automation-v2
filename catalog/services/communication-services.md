# Communication Services

- slug: `communication-services`  |  module: `communication-services-module`

## Fields

- **`product-name`** (text)

- **`Country code`** (select)
  - options: United States (+1)

- **`Local`** (number)

- **`Toll-free`** (number)

- **`Line type queries`** (number)

- **`Calling minutes`** (number)

- **`minutesOutbound`** (number)

- **`Recorded minutes`** (number)

- **`recordedMinutesMixedAudioAndVideo`** (number)

- **`recordedMinutesUnMixedAudio`** (number)

- **`Number of participants`** (number)

- **`mixedAudioStreamedMinutes`** (number)

- **`Streaming minutes`** (number)

- **`Participant minutes`** (number)

- **`Number of minutes`** (number)

- **`Total chat users`** (number)

- **`Average messages sent per user`** (number)

- **`Number of Inbound messages`** (number)

- **`Number of Outbound messages`** (number)

- **`numberOfInboundMessagesConnect`** (number)

- **`numberOfOutboundMessagesConnect`** (number)

- **`Number of emails sent per month`** (number)

- **`Size of each email (MB)`** (number)

- **`Jobs Routed per Month`** (number)

- **`CALL DURATION`** (select) — section: *Call Configuration* (opened automatically)
  - options: 15 minutes, 30 minutes, 45 minutes, 1 hour, 1.5 hours, 2 hours

- **`Calls per Month`** (number) — section: *Call Configuration* (opened automatically)

- **`Participants per Call`** (number) — section: *Call Configuration* (opened automatically)

## Example component

```json
{
  "product": "Communication Services",
  "name": "my-communication-services",
  "fields": {
    "Country code": "United States (+1)",
    "Local": 1,
    "Toll-free": 1,
    "Line type queries": 1,
    "Calling minutes": 1
  }
}
```
