---
card_id: elevenlabs-2026-08-10-c155da
date: '2026-08-10'
description: 'ElevenLabs · 2026-08-10 · Voice and Audio: [v2.63.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.63.0)
  - Added realtime Speech to Text options…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1127
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 968da49699be54f5b681787cc2c40fb622b42016ff6c993f38f5d058c8e9eb22
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-08-10-c155da
  comparison: ''
  date: '2026-08-10'
  description: 'ElevenLabs — ElevenLabs updates — 2026-08-10: [v2.63.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.63.0)
    - Added realtime Speech to Text options for secondary languages, language and
    entity detection, background audio filtering, logging and single-use token authentication.
    Added final transcript, entity and invalid request events; fixed unaccepted terms
    dispatch, duplicate `audio_format` parameters and inclusive VAD bounds.'
  evidence:
  - quote: '[v2.63.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.63.0)
      - Added realtime Speech to Text options for secondary languages, language and
      entity detection, background audio filtering, logging and single-use token authentication.
      Added final transcript, entity and invalid request events; fixed unaccepted
      terms dispatch, duplicate `audio_format` parameters and inclusive VAD bounds.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/10
  - quote: '[v2.62.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.62.0)
      - Added Dubbing bulk transcript update methods and `DubbingRegenerateResponse`;
      added conversation guardrail filters, agent branch commit status, agent alerting
      and MCP `requestMeta` support. Language target creation no longer accepts `modelId`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/10
  - quote: '[v2.61.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.61.0)
      - Added conversation hierarchy filtering, post-call analysis charging, triggered
      guardrail metadata, branch merge conflict details, DTMF input redaction and
      Dubbing transcript uploads. Removed exported OpenAI realtime session types and
      `run_subagent_*` tool-result variants.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/10
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: javascript-sdk
  source_release: elevenlabs-2026-08-10-2026-08-10-3c63678b
  source_type: elevenlabs_changelog
  theme: voice
  theme_matches:
  - matched_terms:
    - audio
    - speech to text
    score: 120
    theme: voice
  - matched_terms:
    - authentication
    score: 50
    theme: account-access
  title: JavaScript SDK
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-08-07-36807-extract-audio-preparation-into-a-utility-crate-copyberry|♯36807
  Extract audio preparation into a utility crate @copyberry]]'
- '[[Changes/ElevenLabs/2026-08-10-python-sdk|Python SDK]]'
- '[[Changes/ElevenLabs/2026-08-10-dubbing-v2-api|Dubbing v2 API]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-08-10-2026-08-10-3c63678b|elevenlabs-2026-08-10-2026-08-10-3c63678b]]'
source_type: elevenlabs_changelog
theme: voice
title: JavaScript SDK
type: change
---

<!-- chronolog:begin region="header" -->
# JavaScript SDK

**ElevenLabs** · 2026-08-10 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/8/10) · from [[Releases/ElevenLabs/elevenlabs-2026-08-10-2026-08-10-3c63678b|ElevenLabs updates — 2026-08-10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [v2.63.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.63.0) - Added realtime Speech to Text options for secondary languages, language and entity detection, background audio filtering, logging and single-use token authentication. Added final transcript, entity and invalid request events; fixed unaccepted terms dispatch, duplicate `audio_format` parameters and inclusive VAD bounds.
>
> [v2.62.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.62.0) - Added Dubbing bulk transcript update methods and `DubbingRegenerateResponse`; added conversation guardrail filters, agent branch commit status, agent alerting and MCP `requestMeta` support. Language target creation no longer accepts `modelId`.
>
> [v2.61.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.61.0) - Added conversation hierarchy filtering, post-call analysis charging, triggered guardrail metadata, branch merge conflict details, DTMF input redaction and Dubbing transcript uploads. Removed exported OpenAI realtime session types and `run_subagent_*` tool-result variants.
>
> Source: https://elevenlabs.io/docs/changelog/2026/8/10
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-08-10-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-08-10-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-08-10-dubbing-v2-api|Dubbing v2 API]] · Voice and Audio
- [[Changes/ElevenLabs/2026-08-10-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-08-10-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-08-10-mcp-server|MCP Server]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-08-07 · Codex CLI · [[Changes/Codex CLI/2026-08-07-36807-extract-audio-preparation-into-a-utility-crate-copyberry|♯36807 Extract audio preparation into a utility crate @copyberry]]
- Later: 2026-08-14 · ChatGPT · [[Changes/ChatGPT/2026-08-14-switch-between-typing-and-dictation-the-dictation-button-stays-available-after-y|Switch between typing and dictation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-08-10-c155da&body=Card%3A%20Changes%2FElevenLabs%2F2026-08-10-javascript-sdk.md%0ACard%20ID%3A%20elevenlabs-2026-08-10-c155da%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F8%2F10%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->