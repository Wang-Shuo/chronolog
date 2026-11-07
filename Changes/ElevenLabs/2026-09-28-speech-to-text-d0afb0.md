---
card_id: elevenlabs-2026-09-28-d0afb0
date: '2026-09-28'
description: 'ElevenLabs · 2026-09-28 · Voice and Audio: [Convert speech to text](https://elevenlabs.io/docs/api-reference/speech-to-text/convert)
  - `POST /v1/speech-to-text`'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1176
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 87f9642bf5c807141091d4b2abc5f8706f5dbcc21b1ed344d35cbe5d8dfd3205
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-09-28-d0afb0
  comparison: ''
  date: '2026-09-28'
  description: 'ElevenLabs — ElevenLabs updates — 2026-09-28: [Convert speech to text](https://elevenlabs.io/docs/api-reference/speech-to-text/convert)
    - `POST /v1/speech-to-text`'
  evidence:
  - quote: '[Convert speech to text](https://elevenlabs.io/docs/api-reference/speech-to-text/convert)
      - `POST /v1/speech-to-text`'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: Added optional nullable `transcript_edit` (string), which accepts a natural-language
      edit instruction of up to 2,000 characters.
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: 'Responses add optional nullable `edited_transcript`. A successful edit
      contains required `kind: "transcript"` and `text` fields. A failed edit contains
      required `kind: "error"`, `error_type: "edit_failed"` and `message` fields.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  - quote: '[Realtime Speech to Text](https://elevenlabs.io/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime)
      accepts `transcript_edit` (string) and emits `edited_transcript` events with
      required `text` and `edited_text` fields.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/28
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: speech-to-text
  source_release: elevenlabs-2026-09-28-2026-09-28-7fc35a6b
  source_type: elevenlabs_changelog
  theme: voice
  title: Speech to Text
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-09-28-speech-to-text|Speech to Text]]'
- '[[Changes/ElevenLabs/2026-09-28-voice-design|Voice Design]]'
- '[[Changes/ElevenLabs/2026-09-28-eleven-v4-and-eleven-v4-turbo|Eleven v4 and Eleven
  v4 Turbo]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-09-28-2026-09-28-7fc35a6b|elevenlabs-2026-09-28-2026-09-28-7fc35a6b]]'
source_type: elevenlabs_changelog
theme: voice
title: Speech to Text
type: change
---

<!-- chronolog:begin region="header" -->
# Speech to Text

**ElevenLabs** · 2026-09-28 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/9/28) · from [[Releases/ElevenLabs/elevenlabs-2026-09-28-2026-09-28-7fc35a6b|ElevenLabs updates — 2026-09-28]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Convert speech to text](https://elevenlabs.io/docs/api-reference/speech-to-text/convert) - `POST /v1/speech-to-text`
>
> Added optional nullable `transcript_edit` (string), which accepts a natural-language edit instruction of up to 2,000 characters.
>
> Responses add optional nullable `edited_transcript`. A successful edit contains required `kind: "transcript"` and `text` fields. A failed edit contains required `kind: "error"`, `error_type: "edit_failed"` and `message` fields.
>
> [Realtime Speech to Text](https://elevenlabs.io/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime) accepts `transcript_edit` (string) and emits `edited_transcript` events with required `text` and `edited_text` fields.
>
> Source: https://elevenlabs.io/docs/changelog/2026/9/28
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-09-28-python-sdk|Python SDK]] · Pricing Model
- [[Changes/ElevenLabs/2026-09-28-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-09-28-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-09-28-elevenagents-4d99c8|ElevenAgents]] · Model Support
- [[Changes/ElevenLabs/2026-09-28-models|Models]] · Model Support
- [[Changes/ElevenLabs/2026-09-28-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-28-javascript-sdk|JavaScript SDK]] · Pricing Model
- [[Changes/ElevenLabs/2026-09-28-flows|Flows]] · Image Generation
- [[Changes/ElevenLabs/2026-09-28-elevenlabs-cli|ElevenLabs CLI]] · Account and Access
- [[Changes/ElevenLabs/2026-09-28-voice-design|Voice Design]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-28-eleven-v4-and-eleven-v4-turbo|Eleven v4 and Eleven v4 Turbo]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-28-flows-ffc074|Flows]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-09-28 · Codex CLI · [[Changes/Codex CLI/2026-09-28-47975-prevent-stale-voice-answers-from-reappearing-during-speech-recovery-etraut|♯47975 Prevent stale voice answers from reappearing during speech recovery @etraut-openai]]
- Later: 2026-09-29 · ChatGPT · [[Changes/ChatGPT/2026-09-29-audio-is-deleted-once-your-notes-are-ready-and-can-t-be-accessed-or-replayed-ava|Audio is deleted once your notes are ready and can’t be accessed or replayed]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-09-28-d0afb0&body=Card%3A%20Changes%2FElevenLabs%2F2026-09-28-speech-to-text-d0afb0.md%0ACard%20ID%3A%20elevenlabs-2026-09-28-d0afb0%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F9%2F28%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->