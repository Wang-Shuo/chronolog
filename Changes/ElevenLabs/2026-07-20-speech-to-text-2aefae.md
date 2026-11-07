---
card_id: elevenlabs-2026-07-20-2aefae
date: '2026-07-20'
description: 'ElevenLabs · 2026-07-20 · Voice and Audio: **Single-use batch authentication**:
  [Convert speech to…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2933
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 346b45ccfae3030dd124c7c510ab1cbedb2483bff415f12871b89dff7bd9554a
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-07-20-2aefae
  comparison: ''
  date: '2026-07-20'
  description: 'ElevenLabs — ElevenLabs updates — 2026-07-20: **Single-use batch authentication**:
    [Convert speech to text](https://elevenlabs.io/docs/api-reference/speech-to-text/convert)
    adds optional `token` (string) as an alternative to API key or bearer authentication.
    Create the single-use token with `POST /v1/single-use-token/batch_scribe`; it
    expires after 15 minutes.'
  evidence:
  - quote: '**Single-use batch authentication**: [Convert speech to text](https://elevenlabs.io/docs/api-reference/speech-to-text/convert)
      adds optional `token` (string) as an alternative to API key or bearer authentication.
      Create the single-use token with `POST /v1/single-use-token/batch_scribe`; it
      expires after 15 minutes.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  - quote: '**Realtime client reliability**: `@elevenlabs/client` now reports microphone
      setup and malformed server errors through `RealtimeEvents.ERROR`, releases microphone
      resources after setup failures and connection closure, and drops late microphone
      frames after socket teardown.'
    source_release: https://elevenlabs.io/docs/changelog/2026/7/20
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: speech-to-text
  source_release: elevenlabs-2026-07-20-2026-07-20-b16c37ed
  source_type: elevenlabs_changelog
  theme: voice
  title: Speech to Text
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-16-add-voice-devices-to-choose-and-persist-the-microphone-for-voice-mode|Add
  /voice devices to choose and persist the microphone for voice mode]]'
- '[[Changes/Dify/2026-07-17-3-voice-and-audio-changes-in-1-16-0|3 Voice and Audio
  changes in 1.16.0]]'
- '[[Changes/ElevenLabs/2026-07-20-speech-to-text|Speech to Text]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-07-20-2026-07-20-b16c37ed|elevenlabs-2026-07-20-2026-07-20-b16c37ed]]'
source_type: elevenlabs_changelog
theme: voice
title: Speech to Text
type: change
---

<!-- chronolog:begin region="header" -->
# Speech to Text

**ElevenLabs** · 2026-07-20 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/7/20) · from [[Releases/ElevenLabs/elevenlabs-2026-07-20-2026-07-20-b16c37ed|ElevenLabs updates — 2026-07-20]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Single-use batch authentication**: [Convert speech to text](https://elevenlabs.io/docs/api-reference/speech-to-text/convert) adds optional `token` (string) as an alternative to API key or bearer authentication. Create the single-use token with `POST /v1/single-use-token/batch_scribe`; it expires after 15 minutes.
>
> **Realtime client reliability**: `@elevenlabs/client` now reports microphone setup and malformed server errors through `RealtimeEvents.ERROR`, releases microphone resources after setup failures and connection closure, and drops late microphone frames after socket teardown.
>
> Source: https://elevenlabs.io/docs/changelog/2026/7/20
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-07-20-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-07-20-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-music|Music]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-cli|CLI]] · Agent Mode
- [[Changes/ElevenLabs/2026-07-20-workspaces|Workspaces]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-07-20-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-07-20-sdk-releases|SDK Releases]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-07-17 · Dify · [[Changes/Dify/2026-07-17-3-voice-and-audio-changes-in-1-16-0|3 Voice and Audio changes in 1.16.0]]
- Later: 2026-07-21 · Codex CLI · [[Changes/Codex CLI/2026-07-21-7-voice-and-audio-changes-in-rust-v0-145-0|7 Voice and Audio changes in rust-v0.145.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-07-20-2aefae&body=Card%3A%20Changes%2FElevenLabs%2F2026-07-20-speech-to-text-2aefae.md%0ACard%20ID%3A%20elevenlabs-2026-07-20-2aefae%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F7%2F20%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->