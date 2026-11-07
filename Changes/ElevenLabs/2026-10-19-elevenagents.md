---
card_id: elevenlabs-2026-10-19-6b1733
date: '2026-10-19'
description: 'ElevenLabs · 2026-10-19 · Voice and Audio: [Create realtime client secret](https://elevenlabs.io/docs/api-reference/conversations/create-client-secret)
  - `POST…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 3024
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: 3726266823e3666ae84c34f16c84d498b87d994b565ea1a32d67fcc64ce5ce66
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-10-19-6b1733
  comparison: ''
  confidence: low
  date: '2026-10-19'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-19: [Create realtime client
    secret](https://elevenlabs.io/docs/api-reference/conversations/create-client-secret)
    - `POST /v1/convai/realtime/client_secrets` - Create an ephemeral client secret
    for browser-based Realtime API sessions. Accepts an optional `session` (OpenAI-compatible
    session configuration with `model` of `eleven_realtime_v1_mini` (default) or `eleven_realtime_v1_max`,
    `instructions`, `audio`, `tools`, `turn_detection` and `max_duration_seconds`
    from 60 to 7,200, default 600) and optional `expires_after` with required `seconds`
    (integer). Returns `value` (string), `expires_at` (integer) and the echoed `session`.'
  evidence:
  - quote: '[Create realtime client secret](https://elevenlabs.io/docs/api-reference/conversations/create-client-secret)
      - `POST /v1/convai/realtime/client_secrets` - Create an ephemeral client secret
      for browser-based Realtime API sessions. Accepts an optional `session` (OpenAI-compatible
      session configuration with `model` of `eleven_realtime_v1_mini` (default) or
      `eleven_realtime_v1_max`, `instructions`, `audio`, `tools`, `turn_detection`
      and `max_duration_seconds` from 60 to 7,200, default 600) and optional `expires_after`
      with required `seconds` (integer). Returns `value` (string), `expires_at` (integer)
      and the echoed `session`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '[List environments](https://elevenlabs.io/docs/api-reference/environments/list)
      - `GET /v1/convai/environments` - List the workspace environments, including
      `production`. Each environment has `name`, nullable `updated_at_unix_secs` and
      nullable `created_by_user_id`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '[Create environment](https://elevenlabs.io/docs/api-reference/environments/create)
      - `POST /v1/convai/environments` - Create an environment with a required, unique
      `name` (string). Returns `409` if the name is taken.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '[Delete environment](https://elevenlabs.io/docs/api-reference/environments/delete)
      - `DELETE /v1/convai/environments/{environment}` - Delete an environment and
      remove its values from all environment variables. Returns `204`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-10-19-2026-10-19-dd219c14
  source_type: elevenlabs_changelog
  theme: voice
  theme_matches:
  - matched_terms:
    - model
    score: 50
    theme: model-support
  - matched_terms:
    - audio
    score: 50
    theme: voice
  theme_resolution: manual-semantic-rule-v1
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Raycast/2026-10-16-dictation-settings-are-now-organised-better-making-it-easier-to-find-exactly-wha|Dictation:
  Settings are now organised better, making it easier to find exactly what…]]'
- '[[Changes/ElevenLabs/2026-10-19-speech-to-text|Speech to Text]]'
- '[[Changes/ElevenLabs/2026-10-19-eleven-realtime|Eleven Realtime]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-19-2026-10-19-dd219c14|elevenlabs-2026-10-19-2026-10-19-dd219c14]]'
source_type: elevenlabs_changelog
theme: voice
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-10-19 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/19) · from [[Releases/ElevenLabs/elevenlabs-2026-10-19-2026-10-19-dd219c14|ElevenLabs updates — 2026-10-19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Create realtime client secret](https://elevenlabs.io/docs/api-reference/conversations/create-client-secret) - `POST /v1/convai/realtime/client_secrets` - Create an ephemeral client secret for browser-based Realtime API sessions. Accepts an optional `session` (OpenAI-compatible session configuration with `model` of `eleven_realtime_v1_mini` (default) or `eleven_realtime_v1_max`, `instructions`, `audio`, `tools`, `turn_detection` and `max_duration_seconds` from 60 to 7,200, default 600) and optional `expires_after` with required `seconds` (integer). Returns `value` (string), `expires_at` (integer) and the echoed `session`.
>
> [List environments](https://elevenlabs.io/docs/api-reference/environments/list) - `GET /v1/convai/environments` - List the workspace environments, including `production`. Each environment has `name`, nullable `updated_at_unix_secs` and nullable `created_by_user_id`.
>
> [Create environment](https://elevenlabs.io/docs/api-reference/environments/create) - `POST /v1/convai/environments` - Create an environment with a required, unique `name` (string). Returns `409` if the name is taken.
>
> [Delete environment](https://elevenlabs.io/docs/api-reference/environments/delete) - `DELETE /v1/convai/environments/{environment}` - Delete an environment and remove its values from all environment variables. Returns `204`.
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-19-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-19-music-and-sound-effects|Music and Sound Effects]] · Enterprise and Administration
- [[Changes/ElevenLabs/2026-10-19-eleven-realtime|Eleven Realtime]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-video-to-music|Video to Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-19-realtime-translation|Realtime Translation]] · Enterprise and Administration
- [[Changes/ElevenLabs/2026-10-19-javascript-sdk|JavaScript SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-elevenagents-b18b24|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-19-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-19-elevenagents-ee74ab|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-voices-f9aa8c|Voices]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-10-16 · Raycast · [[Changes/Raycast/2026-10-16-dictation-settings-are-now-organised-better-making-it-easier-to-find-exactly-wha|Dictation: Settings are now organised better, making it easier to find exactly what…]]
- Later: 2026-10-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-19-voice-dictation-no-longer-inserts-language-markers-like-en-us-into-transcript-te|Voice dictation no longer inserts language markers like en-US into transcript text]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-19-6b1733&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-19-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-10-19-6b1733%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->