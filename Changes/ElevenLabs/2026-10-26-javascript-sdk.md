---
card_id: elevenlabs-2026-10-26-a6c1bb
date: '2026-10-26'
description: 'ElevenLabs · 2026-10-26 · Voice and Audio: [v2.75.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.75.0)
  - `client.speechToSpeech.convert` and…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1204
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 00e30d7ed08c3825d317a9d72d64d062cb970f26b981149f9970993bb4ed7ee5
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-10-26-a6c1bb
  comparison: ''
  date: '2026-10-26'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-26: [v2.75.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.75.0)
    - `client.speechToSpeech.convert` and `client.speechToSpeech.stream` now call
    `POST /v1/voice-changer/{voice_id}` and its `/stream` path. Added `client.environmentVariables.delete`,
    `client.conversationalAi.tests.invocations.update` for renaming a test invocation,
    and an optional `name` on `client.conversationalAi.agents.runTests`. Also adds
    `serviceTier` on the LLM usage calculators, `excludePatterns` on knowledge base
    crawl jobs, `expiresAtUnix` on service account API keys, `cloneStrength` in voice
    settings, `startProcedureIds` in conversation initiation client data and the widget
    `mobileFullscreen` setting. The legacy dubbing `list`, `create`, `get` and `delete`
    methods are marked deprecated, and the branch rebase request type `BranchesRebaseRequest`
    is renamed to `BodyRebaseABranchOntoMainV1ConvaiAgentsAgentIdBranchesBranchIdRebasePost`.'
  evidence:
  - quote: '[v2.75.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.75.0)
      - `client.speechToSpeech.convert` and `client.speechToSpeech.stream` now call
      `POST /v1/voice-changer/{voice_id}` and its `/stream` path. Added `client.environmentVariables.delete`,
      `client.conversationalAi.tests.invocations.update` for renaming a test invocation,
      and an optional `name` on `client.conversationalAi.agents.runTests`. Also adds
      `serviceTier` on the LLM usage calculators, `excludePatterns` on knowledge base
      crawl jobs, `expiresAtUnix` on service account API keys, `cloneStrength` in
      voice settings, `startProcedureIds` in conversation initiation client data and
      the widget `mobileFullscreen` setting. The legacy dubbing `list`, `create`,
      `get` and `delete` methods are marked deprecated, and the branch rebase request
      type `BranchesRebaseRequest` is renamed to `BodyRebaseABranchOntoMainV1ConvaiAgentsAgentIdBranchesBranchIdRebasePost`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: javascript-sdk
  source_release: elevenlabs-2026-10-26-2026-10-26-ca7c552d
  source_type: elevenlabs_changelog
  theme: voice
  theme_matches:
  - matched_terms:
    - voice
    score: 110
    theme: voice
  - matched_terms:
    - agents
    score: 50
    theme: agent-mode
  - matched_terms:
    - llm
    score: 50
    theme: model-support
  title: JavaScript SDK
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-10-26-voice-changer|Voice Changer]]'
- '[[Changes/ElevenLabs/2026-10-26-packages|Packages]]'
- '[[Changes/ElevenLabs/2026-10-26-14-voice-and-audio-changes-in-elevenlabs-updates-2026-10-26|14
  Voice and Audio changes in ElevenLabs updates — 2026-10-26]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-26-2026-10-26-ca7c552d|elevenlabs-2026-10-26-2026-10-26-ca7c552d]]'
source_type: elevenlabs_changelog
theme: voice
title: JavaScript SDK
type: change
---

<!-- chronolog:begin region="header" -->
# JavaScript SDK

**ElevenLabs** · 2026-10-26 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/26) · from [[Releases/ElevenLabs/elevenlabs-2026-10-26-2026-10-26-ca7c552d|ElevenLabs updates — 2026-10-26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [v2.75.0](https://github.com/elevenlabs/elevenlabs-js/releases/tag/v2.75.0) - `client.speechToSpeech.convert` and `client.speechToSpeech.stream` now call `POST /v1/voice-changer/{voice_id}` and its `/stream` path. Added `client.environmentVariables.delete`, `client.conversationalAi.tests.invocations.update` for renaming a test invocation, and an optional `name` on `client.conversationalAi.agents.runTests`. Also adds `serviceTier` on the LLM usage calculators, `excludePatterns` on knowledge base crawl jobs, `expiresAtUnix` on service account API keys, `cloneStrength` in voice settings, `startProcedureIds` in conversation initiation client data and the widget `mobileFullscreen` setting. The legacy dubbing `list`, `create`, `get` and `delete` methods are marked deprecated, and the branch rebase request type `BranchesRebaseRequest` is renamed to `BodyRebaseABranchOntoMainV1ConvaiAgentsAgentIdBranchesBranchIdRebasePost`.
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-26-2-apps-and-integrations-changes-in-elevenlabs-updates-2026-10-26|2 Apps and Integrations changes in ElevenLabs updates — 2026-10-26]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-26-python-sdk|Python SDK]] · Voice and Audio
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

- Earlier: 2026-10-25 · Open WebUI · [[Changes/Open WebUI/2026-10-25-4-voice-and-audio-changes-in-v0-12-4|4 Voice and Audio changes in v0.12.4]]
- Later: 2026-10-27 · Ollama · [[Changes/Ollama/2026-10-27-3-voice-and-audio-changes-in-v0-40-12|3 Voice and Audio changes in v0.40.12]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-26-a6c1bb&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-26-javascript-sdk.md%0ACard%20ID%3A%20elevenlabs-2026-10-26-a6c1bb%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->