---
card_id: elevenlabs-2026-10-26-a5741e
date: '2026-10-26'
description: 'ElevenLabs · 2026-10-26 · Voice and Audio: 14 changes in ElevenLabs
  updates — 2026-10-26 — **Realtime voice mode**: Switching an agent to Realtime voice
  mode…'
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
impact: incremental
kind: digest
machine_hash: 307ebb0c025c3bec348be70f82cf59fc8eadcfaee89272c8ea4bfd1272d4c7a8
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-10-26-a5741e
  comparison: ''
  date: '2026-10-26'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-26: 14 Voice and Audio changes'
  evidence:
  - quote: '**Realtime voice mode**: Switching an agent to Realtime voice mode in
      the dashboard now selects Eleven Realtime v1 Max. Realtime agents always run
      tool calls in parallel, so the **Parallel tool calling** toggle is removed from
      Realtime model settings. See [Realtime models](https://elevenlabs.io/docs/eleven-agents/customization/realtime-models).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Conversation cost**: Conversation charging adds `voice_surcharge_charge`,
      the credits charged as the voice actor reward for the Voice Library voices a
      conversation used. It is not included in `cost`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Guardrails**: In voice conversations, the prompt injection guardrail
      now evaluates the user turn being answered instead of the agent''s previous
      message. Conversations on asynchronous channels such as Zendesk, Intercom and
      Custom Channel that a guardrail blocks now report the guardrail as the termination
      reason.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Zero Retention Mode**: Synthetic voice detection is skipped for conversations
      in [Zero Retention Mode](https://elevenlabs.io/docs/eleven-api/resources/zero-retention-mode).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Fixes**: Text conversations end as soon as the `end_call` tool runs
      instead of waiting for the next user message. Voice agents no longer go silent
      when a turn is cancelled before any audio is sent. The soft timeout no longer
      fires right after the first message or after tool calls on Eleven v4 voices.
      Realtime agents with sub-agent, agent tool or prompt say nodes that inherit
      the LLM can be saved and published. Agent tools that use OAuth2 connections
      no longer fail with expired tokens when the provider rotates refresh tokens.
      The `nemotron-35-super-vl-nvfp4` context limit is raised from 64,000 to 131,072
      tokens.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Clone strength**: `clone_strength` (0 to 1) in Text to Speech `voice_settings`
      and Text to Dialogue `settings` controls how closely a Professional Voice Clone
      fine-tuned for a v4 model follows its samples. The recommended value for most
      use cases is 0. [Edit voice settings](https://elevenlabs.io/docs/api-reference/voices/settings/update)
      stores `clone_strength` and [Get voice settings](https://elevenlabs.io/docs/api-reference/voices/settings/get)
      returns it.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**New endpoint paths**: Voice Changer is documented at `POST /v1/voice-changer/{voice_id}`
      and `POST /v1/voice-changer/{voice_id}/stream`. The `/v1/speech-to-speech/{voice_id}`
      paths keep working but are deprecated and removed from the API reference. The
      Python and JavaScript SDKs call the new paths from v2.75.0, and the SDK method
      names are unchanged for now. In the next major SDK version, `client.speechToSpeech`
      will be deprecated in favor of `client.voiceChanger` to match the endpoint.
      See [Voice changer](https://elevenlabs.io/docs/api-reference/speech-to-speech/convert).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Group concurrency limits enforced**: The workspace group concurrency
      limits (`group_concurrency_limit`, `group_dubbing_concurrency_limit` and `group_music_concurrency_limit`)
      are enforced for Text to Speech, Voice Changer, Music and Dubbing requests.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Shorter realtime silence thresholds**: Realtime Speech to Text honors
      `vad_silence_threshold_secs` values below 0.5 seconds, which were previously
      treated as 0.5. The minimum accepted value is lowered from 0.3 to about 0.19
      seconds.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Webhook retries**: Transcription and error webhooks are retried on failure
      when the webhook''s retry setting is on. See [Speech to Text webhooks](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/webhooks).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Legacy endpoints deprecated**: The `/v1/dubbing` endpoints outside `/v1/dubbing/project`,
      including [Dub a video or an audio file](https://elevenlabs.io/docs/api-reference/dubbing/create)
      and [List dubs](https://elevenlabs.io/docs/api-reference/dubbing/list), are
      marked deprecated in the API reference.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Video clip actions**: Video clips offer voice changer and voice isolator
      actions.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Fixes**: Cantonese Professional Voice Clone samples are no longer rejected
      when language detection reports Chinese, and adding PVC samples no longer fails
      with a `500` error when language detection is unavailable.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  - quote: '**Minimum charge**: Text to Speech and Speech to Text requests priced
      below one credit are charged one credit, and refunds return exactly the credits
      that were charged.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/26
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: elevenlabs
  product_name: ElevenLabs
  slug: 14-voice-and-audio-changes-in-elevenlabs-updates-2026-10-26
  source_release: elevenlabs-2026-10-26-2026-10-26-ca7c552d
  source_type: elevenlabs_changelog
  theme: voice
  title: 14 Voice and Audio changes in ElevenLabs updates — 2026-10-26
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-10-26-dubbing|Dubbing]]'
- '[[Changes/ElevenLabs/2026-10-26-voice-changer|Voice Changer]]'
- '[[Changes/ElevenLabs/2026-10-26-packages|Packages]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-26-2026-10-26-ca7c552d|elevenlabs-2026-10-26-2026-10-26-ca7c552d]]'
source_type: elevenlabs_changelog
theme: voice
title: 14 Voice and Audio changes in ElevenLabs updates — 2026-10-26
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Voice and Audio changes in ElevenLabs updates — 2026-10-26

**ElevenLabs** · 2026-10-26 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://elevenlabs.io/docs/changelog/2026/10/26) · from [[Releases/ElevenLabs/elevenlabs-2026-10-26-2026-10-26-ca7c552d|ElevenLabs updates — 2026-10-26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Realtime voice mode**: Switching an agent to Realtime voice mode in the dashboard now selects Eleven Realtime v1 Max. Realtime agents always run tool calls in parallel, so the **Parallel tool calling** toggle is removed from Realtime model settings. See [Realtime models](https://elevenlabs.io/docs/eleven-agents/customization/realtime-models).

> **Conversation cost**: Conversation charging adds `voice_surcharge_charge`, the credits charged as the voice actor reward for the Voice Library voices a conversation used. It is not included in `cost`.

> **Guardrails**: In voice conversations, the prompt injection guardrail now evaluates the user turn being answered instead of the agent's previous message. Conversations on asynchronous channels such as Zendesk, Intercom and Custom Channel that a guardrail blocks now report the guardrail as the termination reason.

> **Zero Retention Mode**: Synthetic voice detection is skipped for conversations in [Zero Retention Mode](https://elevenlabs.io/docs/eleven-api/resources/zero-retention-mode).

> **Fixes**: Text conversations end as soon as the `end_call` tool runs instead of waiting for the next user message. Voice agents no longer go silent when a turn is cancelled before any audio is sent. The soft timeout no longer fires right after the first message or after tool calls on Eleven v4 voices. Realtime agents with sub-agent, agent tool or prompt say nodes that inherit the LLM can be saved and published. Agent tools that use OAuth2 connections no longer fail with expired tokens when the provider rotates refresh tokens. The `nemotron-35-super-vl-nvfp4` context limit is raised from 64,000 to 131,072 tokens.

> **Clone strength**: `clone_strength` (0 to 1) in Text to Speech `voice_settings` and Text to Dialogue `settings` controls how closely a Professional Voice Clone fine-tuned for a v4 model follows its samples. The recommended value for most use cases is 0. [Edit voice settings](https://elevenlabs.io/docs/api-reference/voices/settings/update) stores `clone_strength` and [Get voice settings](https://elevenlabs.io/docs/api-reference/voices/settings/get) returns it.

> **New endpoint paths**: Voice Changer is documented at `POST /v1/voice-changer/{voice_id}` and `POST /v1/voice-changer/{voice_id}/stream`. The `/v1/speech-to-speech/{voice_id}` paths keep working but are deprecated and removed from the API reference. The Python and JavaScript SDKs call the new paths from v2.75.0, and the SDK method names are unchanged for now. In the next major SDK version, `client.speechToSpeech` will be deprecated in favor of `client.voiceChanger` to match the endpoint. See [Voice changer](https://elevenlabs.io/docs/api-reference/speech-to-speech/convert).

> **Group concurrency limits enforced**: The workspace group concurrency limits (`group_concurrency_limit`, `group_dubbing_concurrency_limit` and `group_music_concurrency_limit`) are enforced for Text to Speech, Voice Changer, Music and Dubbing requests.

> **Shorter realtime silence thresholds**: Realtime Speech to Text honors `vad_silence_threshold_secs` values below 0.5 seconds, which were previously treated as 0.5. The minimum accepted value is lowered from 0.3 to about 0.19 seconds.

> **Webhook retries**: Transcription and error webhooks are retried on failure when the webhook's retry setting is on. See [Speech to Text webhooks](https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/webhooks).

> **Legacy endpoints deprecated**: The `/v1/dubbing` endpoints outside `/v1/dubbing/project`, including [Dub a video or an audio file](https://elevenlabs.io/docs/api-reference/dubbing/create) and [List dubs](https://elevenlabs.io/docs/api-reference/dubbing/list), are marked deprecated in the API reference.

> **Video clip actions**: Video clips offer voice changer and voice isolator actions.

> **Fixes**: Cantonese Professional Voice Clone samples are no longer rejected when language detection reports Chinese, and adding PVC samples no longer fails with a `500` error when language detection is unavailable.

> **Minimum charge**: Text to Speech and Speech to Text requests priced below one credit are charged one credit, and refunds return exactly the credits that were charged.

Source: https://elevenlabs.io/docs/changelog/2026/10/26
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
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-26-a5741e&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-26-14-voice-and-audio-changes-in-elevenlabs-updates-2026-10-26.md%0ACard%20ID%3A%20elevenlabs-2026-10-26-a5741e%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->