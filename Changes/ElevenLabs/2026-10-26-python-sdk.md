---
card_id: elevenlabs-2026-10-26-043ef8
date: '2026-10-26'
description: 'ElevenLabs · 2026-10-26 · Voice and Audio: [v2.75.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.75.0)
  - Added the `callback_disconnect`…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 3031
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 6dc0fb45d6f82b277d7f09957a7fae73431f7c1d95b12425f65875e15db5bd64
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-10-26-043ef8
  comparison: ''
  confidence: low
  date: '2026-10-26'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-26: [v2.75.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.75.0)
    - Added the `callback_disconnect` option to `Conversation` and `AsyncConversation`.
    It receives a `DisconnectionDetails` with a `reason` of `"user"`, `"agent"` or
    `"error"`, plus the WebSocket close code and reason when available, and replaces
    the deprecated `callback_end_session`. The regenerated client moves `client.speech_to_speech`
    to the `/v1/voice-changer` paths and adds `client.environment_variables.delete`,
    `client.conversational_ai.tests.invocations.update` and the same new parameters
    as JavaScript SDK v2.75.0.'
  evidence:
  - quote: '[v2.75.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.75.0)
      - Added the `callback_disconnect` option to `Conversation` and `AsyncConversation`.
      It receives a `DisconnectionDetails` with a `reason` of `"user"`, `"agent"`
      or `"error"`, plus the WebSocket close code and reason when available, and replaces
      the deprecated `callback_end_session`. The regenerated client moves `client.speech_to_speech`
      to the `/v1/voice-changer` paths and adds `client.environment_variables.delete`,
      `client.conversational_ai.tests.invocations.update` and the same new parameters
      as JavaScript SDK v2.75.0.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: python-sdk
  source_release: elevenlabs-2026-10-26-2026-10-26-ca7c552d
  source_type: elevenlabs_changelog
  theme: voice
  theme_matches:
  - matched_terms:
    - voice
    score: 110
    theme: voice
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  title: Python SDK
  type: change
related_changes:
- '[[Changes/Ollama/2026-10-24-ollama-can-now-generate-speech-https-docs-ollama-com-capabilities-speech-on-maco|Ollama
  can now generate speech((source link) on macOS]]'
- '[[Changes/Open WebUI/2026-10-25-4-voice-and-audio-changes-in-v0-12-4|4 Voice and
  Audio changes in v0.12.4]]'
- '[[Changes/AnythingLLM/2026-10-26-support-mov-files-for-transcription-by-shatfield4-in-https-github-com-mintplex-l|Support
  .mov files for transcription]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-26-2026-10-26-ca7c552d|elevenlabs-2026-10-26-2026-10-26-ca7c552d]]'
source_type: elevenlabs_changelog
theme: voice
title: Python SDK
type: change
---

<!-- chronolog:begin region="header" -->
# Python SDK

**ElevenLabs** · 2026-10-26 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/26) · from [[Releases/ElevenLabs/elevenlabs-2026-10-26-2026-10-26-ca7c552d|ElevenLabs updates — 2026-10-26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [v2.75.0](https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.75.0) - Added the `callback_disconnect` option to `Conversation` and `AsyncConversation`. It receives a `DisconnectionDetails` with a `reason` of `"user"`, `"agent"` or `"error"`, plus the WebSocket close code and reason when available, and replaces the deprecated `callback_end_session`. The regenerated client moves `client.speech_to_speech` to the `/v1/voice-changer` paths and adds `client.environment_variables.delete`, `client.conversational_ai.tests.invocations.update` and the same new parameters as JavaScript SDK v2.75.0.
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-26-2-apps-and-integrations-changes-in-elevenlabs-updates-2026-10-26|2 Apps and Integrations changes in ElevenLabs updates — 2026-10-26]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-26-knowledge-base-crawl-exclusions|Knowledge base crawl exclusions]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-26-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-26-clone-strength-for-v4-voices|Clone strength for v4 voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-android-sdk|Android SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-10-26-2-pricing-model-changes-in-elevenlabs-updates-2026-10-26|2 Pricing Model changes in ElevenLabs updates — 2026-10-26]] · Pricing Model
- [[Changes/ElevenLabs/2026-10-26-transcript-downloads-the-dubbing-project-menu-can-download-target-language-trans|Transcript downloads: The dubbing project menu can download target language…]] · Interface Experience
- [[Changes/ElevenLabs/2026-10-26-video-to-music-studio-s-video-to-music-workflow-uses-music-v2-5-by-default|Video to music: Studio's video to music workflow uses Music v2.5 by default]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-26-2-editor-experience-changes-in-elevenlabs-updates-2026-10-26|2 Editor Experience changes in ElevenLabs updates — 2026-10-26]] · Editor Experience
- [[Changes/ElevenLabs/2026-10-26-dubbing|Dubbing]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-voice-changer|Voice Changer]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-2-mobile-and-desktop-changes-in-elevenlabs-updates-2026-10-26|2 Mobile and Desktop changes in ElevenLabs updates — 2026-10-26]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-10-26-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-14-voice-and-audio-changes-in-elevenlabs-updates-2026-10-26|14 Voice and Audio changes in ElevenLabs updates — 2026-10-26]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-26-voice-cloning-permissions-members-without-the-create-instant-voice-clone-or-crea|Voice cloning permissions]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-10-26-9-agent-mode-changes-in-elevenlabs-updates-2026-10-26|9 Agent Mode changes in ElevenLabs updates — 2026-10-26]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-26-fast-llm-service-tier|Fast LLM service tier]] · Model Support
- [[Changes/ElevenLabs/2026-10-26-3-model-support-changes-in-elevenlabs-updates-2026-10-26|3 Model Support changes in ElevenLabs updates — 2026-10-26]] · Model Support
- [[Changes/ElevenLabs/2026-10-26-elevenlabs-cli|ElevenLabs CLI]] · Account and Access
- [[Changes/ElevenLabs/2026-10-26-oauth-scope-oauth-clients-can-request-the-realtime-translation-scope|OAuth scope: OAuth clients can request the realtime_translation scope]] · Account and Access
- [[Changes/ElevenLabs/2026-10-26-9-other-changes-in-elevenlabs-updates-2026-10-26|9 other changes in ElevenLabs updates — 2026-10-26]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-10-26 · AnythingLLM · [[Changes/AnythingLLM/2026-10-26-support-mov-files-for-transcription-by-shatfield4-in-https-github-com-mintplex-l|Support .mov files for transcription]]
- Later: 2026-10-26 · Superwhisper · [[Changes/Superwhisper/2026-10-26-resolve-spoken-self-corrections-in-message-preset|Resolve spoken self-corrections in Message preset]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-26-043ef8&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-26-python-sdk.md%0ACard%20ID%3A%20elevenlabs-2026-10-26-043ef8%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->