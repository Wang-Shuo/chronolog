---
card_id: elevenlabs-2026-10-19-cf18a4
date: '2026-10-19'
description: 'ElevenLabs · 2026-10-19 · Apps and Integrations: [v2.74.1](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.74.1)
  - `music.compose_detailed` now…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1306
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 2a1e436b435e610b4e40b8da363e984c51d6b32da5fba94bf000e25f4ffa89a7
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-10-19-cf18a4
  comparison: ''
  date: '2026-10-19'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-19: [v2.74.1](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.74.1)
    - `music.compose_detailed` now accepts and forwards `enable_logging`, which the
    custom wrapper previously dropped, so Zero Retention Mode works with this method.'
  evidence:
  - quote: '[v2.74.1](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.74.1)
      - `music.compose_detailed` now accepts and forwards `enable_logging`, which
      the custom wrapper previously dropped, so Zero Retention Mode works with this
      method.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '[v2.74.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.74.0)
      - Added `client.conversational_ai.realtime.create_client_secret` for the Realtime
      API and an `environments` client, with the same regenerated API changes as JavaScript
      SDK v2.74.0.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '[v2.73.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.73.0)
      - Added `create_and_wait` helpers for Flows image, video and Text to Speech
      generations and template runs, for both sync and async clients, with `wait_timeout_in_seconds`
      and `min_poll_interval_in_seconds` options and a `FlowsWaitTimeoutError` exported
      from `elevenlabs.flows_custom`. Type checkers such as pyright now resolve `client.webhooks.construct_event`,
      `client.speech_to_text.realtime`, `client.text_to_speech.convert_realtime` and
      the custom Music methods. Includes the same regenerated API changes as the JavaScript
      SDK.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '[v2.73.1](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.73.1)
      - Fixed the test suite on Python 3.13 and later, and added Python 3.13 and 3.14
      to CI.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: python-sdk
  source_release: elevenlabs-2026-10-19-2026-10-19-dd219c14
  source_type: elevenlabs_changelog
  theme: apps-integrations
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Python SDK
  type: change
related_changes:
- '[[Changes/v0/2026-10-16-integration-icons-no-longer-fail-to-load-in-project-settings|Integration
  icons no longer fail to load in project settings]]'
- '[[Changes/Claude Code/2026-10-19-8-apps-and-integrations-changes-in-v2-1-304|8
  Apps and Integrations changes in v2.1.304]]'
- '[[Changes/ElevenLabs/2026-10-19-sdk-releases|SDK releases]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-19-2026-10-19-dd219c14|elevenlabs-2026-10-19-2026-10-19-dd219c14]]'
source_type: elevenlabs_changelog
theme: apps-integrations
title: Python SDK
type: change
---

<!-- chronolog:begin region="header" -->
# Python SDK

**ElevenLabs** · 2026-10-19 · [[Themes/apps-integrations|Apps and Integrations]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/19) · from [[Releases/ElevenLabs/elevenlabs-2026-10-19-2026-10-19-dd219c14|ElevenLabs updates — 2026-10-19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [v2.74.1](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.74.1) - `music.compose_detailed` now accepts and forwards `enable_logging`, which the custom wrapper previously dropped, so Zero Retention Mode works with this method.
>
> [v2.74.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.74.0) - Added `client.conversational_ai.realtime.create_client_secret` for the Realtime API and an `environments` client, with the same regenerated API changes as JavaScript SDK v2.74.0.
>
> [v2.73.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.73.0) - Added `create_and_wait` helpers for Flows image, video and Text to Speech generations and template runs, for both sync and async clients, with `wait_timeout_in_seconds` and `min_poll_interval_in_seconds` options and a `FlowsWaitTimeoutError` exported from `elevenlabs.flows_custom`. Type checkers such as pyright now resolve `client.webhooks.construct_event`, `client.speech_to_text.realtime`, `client.text_to_speech.convert_realtime` and the custom Music methods. Includes the same regenerated API changes as the JavaScript SDK.
>
> [v2.73.1](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.73.1) - Fixed the test suite on Python 3.13 and later, and added Python 3.13 and 3.14 to CI.
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-19-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-19-music-and-sound-effects|Music and Sound Effects]] · Enterprise and Administration
- [[Changes/ElevenLabs/2026-10-19-eleven-realtime|Eleven Realtime]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-elevenagents|ElevenAgents]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-video-to-music|Video to Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-19-realtime-translation|Realtime Translation]] · Enterprise and Administration
- [[Changes/ElevenLabs/2026-10-19-javascript-sdk|JavaScript SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-elevenagents-b18b24|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-19-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-elevenagents-ee74ab|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-voices-f9aa8c|Voices]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-19 · Claude Code · [[Changes/Claude Code/2026-10-19-8-apps-and-integrations-changes-in-v2-1-304|8 Apps and Integrations changes in v2.1.304]]
- Later: 2026-10-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-19-10-apps-and-integrations-changes-in-v1-0-100|10 Apps and Integrations changes in v1.0.100]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-19-cf18a4&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-19-python-sdk.md%0ACard%20ID%3A%20elevenlabs-2026-10-19-cf18a4%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->