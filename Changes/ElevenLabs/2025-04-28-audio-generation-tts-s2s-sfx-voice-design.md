---
card_id: elevenlabs-2025-04-28-812f79
date: '2025-04-28'
description: 'ElevenLabs · 2025-04-28 · Voice and Audio: Updated endpoints to support
  new `output_format` option `pcm_48000`:'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 658
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: affbabff0cc9f43813859898222b987434eb3772f733d7c28b2124bf88167377
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2025-04-28-812f79
  comparison: ''
  confidence: low
  date: '2025-04-28'
  description: 'ElevenLabs — ElevenLabs updates — 2025-04-28: Updated endpoints to
    support new `output_format` option `pcm_48000`:'
  evidence:
  - quote: 'Updated endpoints to support new `output_format` option `pcm_48000`:'
    source_release: https://elevenlabs.io/docs/changelog/2025/4/28
  - quote: '[Text to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech/convert)
      (`POST /v1/text-to-speech/{voice_id}`)'
    source_release: https://elevenlabs.io/docs/changelog/2025/4/28
  - quote: '[Text to Speech with Timestamps](https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps)
      (`POST /v1/text-to-speech/{voice_id}/with-timestamps`)'
    source_release: https://elevenlabs.io/docs/changelog/2025/4/28
  - quote: '[Text to Speech Stream](https://elevenlabs.io/docs/api-reference/text-to-speech/stream)
      (`POST /v1/text-to-speech/{voice_id}/stream`)'
    source_release: https://elevenlabs.io/docs/changelog/2025/4/28
  - quote: '[Text to Speech Stream with Timestamps](https://elevenlabs.io/docs/api-reference/text-to-speech/stream-with-timestamps)
      (`POST /v1/text-to-speech/{voice_id}/stream/with-timestamps`)'
    source_release: https://elevenlabs.io/docs/changelog/2025/4/28
  - quote: '[Speech to Speech](https://elevenlabs.io/docs/api-reference/speech-to-speech/convert)
      (`POST /v1/speech-to-speech/{voice_id}`)'
    source_release: https://elevenlabs.io/docs/changelog/2025/4/28
  - quote: '[Speech to Speech Stream](https://elevenlabs.io/docs/api-reference/speech-to-speech/stream)
      (`POST /v1/speech-to-speech/{voice_id}/stream`)'
    source_release: https://elevenlabs.io/docs/changelog/2025/4/28
  - quote: '[Sound Generation](https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert)
      (`POST /v1/sound-generation`)'
    source_release: https://elevenlabs.io/docs/changelog/2025/4/28
  - quote: '[Create Voice Previews](https://elevenlabs.io/docs/api-reference/legacy/voices/create-previews)
      (`POST /v1/text-to-voice/create-previews`)'
    source_release: https://elevenlabs.io/docs/changelog/2025/4/28
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: audio-generation-tts-s2s-sfx-voice-design
  source_release: elevenlabs-2025-04-28-2025-04-28-49480de5
  source_type: elevenlabs_changelog
  theme: voice
  title: Audio Generation (TTS, S2S, SFX, Voice Design)
  type: change
related_changes:
- '[[Changes/ElevenLabs/2025-04-21-speech-to-text|Speech to Text]]'
- '[[Changes/ElevenLabs/2025-04-21-professional-voice-cloning-pvc|Professional Voice
  Cloning (PVC)]]'
- '[[Changes/ElevenLabs/2025-04-21-speech-to-text-e79d25|Speech to Text]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2025-04-28-2025-04-28-49480de5|elevenlabs-2025-04-28-2025-04-28-49480de5]]'
source_type: elevenlabs_changelog
theme: voice
title: Audio Generation (TTS, S2S, SFX, Voice Design)
type: change
---

<!-- chronolog:begin region="header" -->
# Audio Generation (TTS, S2S, SFX, Voice Design)

**ElevenLabs** · 2025-04-28 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2025/4/28) · from [[Releases/ElevenLabs/elevenlabs-2025-04-28-2025-04-28-49480de5|ElevenLabs updates — 2025-04-28]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Updated endpoints to support new `output_format` option `pcm_48000`:
>
> [Text to Speech](https://elevenlabs.io/docs/api-reference/text-to-speech/convert) (`POST /v1/text-to-speech/{voice_id}`)
>
> [Text to Speech with Timestamps](https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps) (`POST /v1/text-to-speech/{voice_id}/with-timestamps`)
>
> [Text to Speech Stream](https://elevenlabs.io/docs/api-reference/text-to-speech/stream) (`POST /v1/text-to-speech/{voice_id}/stream`)
>
> [Text to Speech Stream with Timestamps](https://elevenlabs.io/docs/api-reference/text-to-speech/stream-with-timestamps) (`POST /v1/text-to-speech/{voice_id}/stream/with-timestamps`)
>
> [Speech to Speech](https://elevenlabs.io/docs/api-reference/speech-to-speech/convert) (`POST /v1/speech-to-speech/{voice_id}`)
>
> [Speech to Speech Stream](https://elevenlabs.io/docs/api-reference/speech-to-speech/stream) (`POST /v1/speech-to-speech/{voice_id}/stream`)
>
> [Sound Generation](https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert) (`POST /v1/sound-generation`)
>
> [Create Voice Previews](https://elevenlabs.io/docs/api-reference/legacy/voices/create-previews) (`POST /v1/text-to-voice/create-previews`)
>
> Source: https://elevenlabs.io/docs/changelog/2025/4/28
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2025-04-28-new-endpoints|New Endpoints]] · Agent Mode
- [[Changes/ElevenLabs/2025-04-28-agents-platform|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2025-04-28-agents-platform-4b369f|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2025-04-28-agents-platform-6b1e4d|Agents Platform]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2025-04-21 · ElevenLabs · [[Changes/ElevenLabs/2025-04-21-speech-to-text-e79d25|Speech to Text]]
- Later: 2025-05-01 · ChatGPT · [[Changes/ChatGPT/2025-05-01-launched-on-april-1-as-a-one-month-surprise-our-monday-personality-available-in|Sunsetting Monday GPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2025-04-28-812f79&body=Card%3A%20Changes%2FElevenLabs%2F2025-04-28-audio-generation-tts-s2s-sfx-voice-design.md%0ACard%20ID%3A%20elevenlabs-2025-04-28-812f79%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2025%2F4%2F28%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->