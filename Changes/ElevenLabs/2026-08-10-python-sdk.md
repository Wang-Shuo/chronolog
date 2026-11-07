---
card_id: elevenlabs-2026-08-10-468c2d
date: '2026-08-10'
description: 'ElevenLabs · 2026-08-10 · Voice and Audio: [v2.63.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.63.0)
  - Added realtime Speech to Text…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2954
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 159be7a96487ac343ce15835f7a041cbe327655baa868d6340619d69f5c01209
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-08-10-468c2d
  comparison: ''
  date: '2026-08-10'
  description: 'ElevenLabs — ElevenLabs updates — 2026-08-10: [v2.63.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.63.0)
    - Added realtime Speech to Text options for secondary languages, language and
    entity detection, background audio filtering, logging and single-use token authentication.
    Added final transcript, entity and invalid request events; fixed unaccepted terms
    dispatch and now rejects connections without an API key or token.'
  evidence:
  - quote: '[v2.63.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.63.0)
      - Added realtime Speech to Text options for secondary languages, language and
      entity detection, background audio filtering, logging and single-use token authentication.
      Added final transcript, entity and invalid request events; fixed unaccepted
      terms dispatch and now rejects connections without an API key or token.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/10
  - quote: '[v2.62.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.62.0)
      - Added Dubbing `update_segments` methods and `DubbingRegenerateResponse`; added
      `guardrail_types`, `custom_guardrail_names`, `include_commit_status` and MCP
      `request_meta` support. Dubbing segment updates now use request body models,
      and language target creation no longer accepts `model_id`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/10
  - quote: '[v2.61.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.61.0)
      - Added `parent_conversation_id`, analysis charging, triggered guardrail metadata,
      branch merge conflicts, DTMF input redaction and Dubbing transcript uploads.
      Removed OpenAI realtime session types and `run_subagent_*` result models.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/10
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: python-sdk
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
  title: Python SDK
  type: change
related_changes:
- '[[Changes/HeyGen/2026-08-07-video-podcast|Video podcast]]'
- '[[Changes/HeyGen/2026-08-07-avatar-look-voice-control|Avatar look & voice control]]'
- '[[Changes/HeyGen/2026-08-07-translation-layout-re-design|Translation layout re-design]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-08-10-2026-08-10-3c63678b|elevenlabs-2026-08-10-2026-08-10-3c63678b]]'
source_type: elevenlabs_changelog
theme: voice
title: Python SDK
type: change
---

<!-- chronolog:begin region="header" -->
# Python SDK

**ElevenLabs** · 2026-08-10 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/8/10) · from [[Releases/ElevenLabs/elevenlabs-2026-08-10-2026-08-10-3c63678b|ElevenLabs updates — 2026-08-10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [v2.63.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.63.0) - Added realtime Speech to Text options for secondary languages, language and entity detection, background audio filtering, logging and single-use token authentication. Added final transcript, entity and invalid request events; fixed unaccepted terms dispatch and now rejects connections without an API key or token.
>
> [v2.62.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.62.0) - Added Dubbing `update_segments` methods and `DubbingRegenerateResponse`; added `guardrail_types`, `custom_guardrail_names`, `include_commit_status` and MCP `request_meta` support. Dubbing segment updates now use request body models, and language target creation no longer accepts `model_id`.
>
> [v2.61.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.61.0) - Added `parent_conversation_id`, analysis charging, triggered guardrail metadata, branch merge conflicts, DTMF input redaction and Dubbing transcript uploads. Removed OpenAI realtime session types and `run_subagent_*` result models.
>
> Source: https://elevenlabs.io/docs/changelog/2026/8/10
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-08-10-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-08-10-dubbing-v2-api|Dubbing v2 API]] · Voice and Audio
- [[Changes/ElevenLabs/2026-08-10-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-08-10-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-08-10-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-08-10-mcp-server|MCP Server]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-08-07 · HeyGen · [[Changes/HeyGen/2026-08-07-translation-layout-re-design|Translation layout re-design]]
- Later: 2026-08-10 · Runway · [[Changes/Runway/2026-08-10-tool-mode-and-edit-studio-now-let-you-export-gen-4-5-and-aleph-2-generations-as|ProRes / PNG Sequence Export]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-08-10-468c2d&body=Card%3A%20Changes%2FElevenLabs%2F2026-08-10-python-sdk.md%0ACard%20ID%3A%20elevenlabs-2026-08-10-468c2d%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F8%2F10%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->