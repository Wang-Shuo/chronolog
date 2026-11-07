---
card_id: elevenlabs-2026-09-14-dab1d0
date: '2026-09-14'
description: 'ElevenLabs · 2026-09-14 · Voice and Audio: Real-time server events add
  `queue_status`. Its required `queue_status_event.status` accepts `waiting`, `admitted`…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2989
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: e7949645a08c0f75a8477d0a200afe512616913e2fd717330e4343057e04a195
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-09-14-dab1d0
  comparison: ''
  date: '2026-09-14'
  description: 'ElevenLabs — ElevenLabs updates — 2026-09-14: Real-time server events
    add `queue_status`. Its required `queue_status_event.status` accepts `waiting`,
    `admitted` or `timed_out`; `timed_out` precedes WebSocket close code `4300`. Hold
    audio continues to arrive as regular `audio` events.'
  evidence:
  - quote: Real-time server events add `queue_status`. Its required `queue_status_event.status`
      accepts `waiting`, `admitted` or `timed_out`; `timed_out` precedes WebSocket
      close code `4300`. Hold audio continues to arrive as regular `audio` events.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: The `LLM` enum adds `gemini-3.8-flash`, including conversation initiation
      overrides.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: Conversation system tool result unions add `start_procedure_success`, `start_procedure_error`,
      `end_procedure_success` and `end_procedure_error`.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  - quote: '`FeaturesUsageCommonModel` adds optional `freeform_procedure` and `structured_procedure`
      feature statuses.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/14
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-09-14-2026-09-14-583c2a71
  source_type: elevenlabs_changelog
  theme: voice
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Qoder/2026-09-12-real-time-voice-improved-connection-stability-reducing-the-likelihood-of-unexpec|Real-time
  voice: Improved connection stability, reducing the likelihood…]]'
- '[[Changes/ElevenLabs/2026-09-14-packages|Packages]]'
- '[[Changes/ElevenLabs/2026-09-14-elevenagents-bdb11f|ElevenAgents]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-09-14-2026-09-14-583c2a71|elevenlabs-2026-09-14-2026-09-14-583c2a71]]'
source_type: elevenlabs_changelog
theme: voice
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-09-14 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/9/14) · from [[Releases/ElevenLabs/elevenlabs-2026-09-14-2026-09-14-583c2a71|ElevenLabs updates — 2026-09-14]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Real-time server events add `queue_status`. Its required `queue_status_event.status` accepts `waiting`, `admitted` or `timed_out`; `timed_out` precedes WebSocket close code `4300`. Hold audio continues to arrive as regular `audio` events.
>
> The `LLM` enum adds `gemini-3.8-flash`, including conversation initiation overrides.
>
> Conversation system tool result unions add `start_procedure_success`, `start_procedure_error`, `end_procedure_success` and `end_procedure_error`.
>
> `FeaturesUsageCommonModel` adds optional `freeform_procedure` and `structured_procedure` feature statuses.
>
> Source: https://elevenlabs.io/docs/changelog/2026/9/14
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-09-14-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-09-14-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-14-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-09-14-ios-sdk|iOS SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-09-14-javascript-sdk|JavaScript SDK]] · Model Support
- [[Changes/ElevenLabs/2026-09-14-python-sdk|Python SDK]] · Model Support
- [[Changes/ElevenLabs/2026-09-14-elevenagents-bdb11f|ElevenAgents]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-14-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-09-14-elevenagents-d9e798|ElevenAgents]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-09-12 · Qoder · [[Changes/Qoder/2026-09-12-real-time-voice-improved-connection-stability-reducing-the-likelihood-of-unexpec|Real-time voice: Improved connection stability, reducing the likelihood…]]
- Later: 2026-09-16 · Synthesia · [[Changes/Synthesia/2026-09-16-create-up-to-20-seconds-of-b-roll-with-natively-synced-audio-and-drop-polished-c|Generate B-roll with Flux 3 from Black Forest Labs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-09-14-dab1d0&body=Card%3A%20Changes%2FElevenLabs%2F2026-09-14-elevenagents-dab1d0.md%0ACard%20ID%3A%20elevenlabs-2026-09-14-dab1d0%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F9%2F14%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->