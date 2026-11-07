---
card_id: elevenlabs-2026-03-09-26c43c
date: '2026-03-09'
description: 'ElevenLabs · 2026-03-09 · Model Support: **New LLM options**: Added
  [claude-sonnet-4-6](https://www.anthropic.com/claude/sonnet) and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1155
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 4bd69b189fdabe27809d89725bc80afebf329de605756313361b54081da5e3a2
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-03-09-26c43c
  comparison: ''
  confidence: low
  date: '2026-03-09'
  description: 'ElevenLabs — ElevenLabs updates — 2026-03-09: **New LLM options**:
    Added [claude-sonnet-4-6](https://www.anthropic.com/claude/sonnet) and `gemini-3.1-flash-lite-preview`
    as supported LLM providers for agent conversation configuration.'
  evidence:
  - quote: '**New LLM options**: Added [claude-sonnet-4-6](https://www.anthropic.com/claude/sonnet)
      and `gemini-3.1-flash-lite-preview` as supported LLM providers for agent conversation
      configuration.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/9
  - quote: '**Guardrail execution mode**: Custom guardrails now support a configurable
      `execution_mode` field with the `GuardrailExecutionMode` enum, and have separate
      input and output schema definitions. This allows more precise control over when
      guardrail logic runs and which message direction it applies to.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/9
  - quote: '**Guardrail triggered client event**: Added `guardrail_triggered` to the
      `ClientEvent` enum, enabling agent workflows and client-side handlers to respond
      when a guardrail fires during a conversation.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/9
  - quote: '**Batch calling concurrency**: Added `target_concurrency_limit` field
      to the [submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create)
      request body, allowing you to control the target number of concurrent calls
      for a given batch.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/9
  - quote: '**Agent testing type filter**: The [list agent tests](https://elevenlabs.io/docs/api-reference/tests/list)
      endpoint now accepts a `types` query parameter to filter results by test type.
      The `include_folders` query parameter is deprecated in favor of the new `types`
      filter.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/9
  - quote: '**Telephony call configuration**: Added `telephony_call_config` to outbound
      call request schemas for [Twilio](https://elevenlabs.io/docs/api-reference/twilio/outbound-call)
      and [SIP trunk](https://elevenlabs.io/docs/api-reference/sip-trunk/outbound-call)
      calls, with a default `ringing_timeout_secs` of 60 seconds.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/9
  - quote: '**WhatsApp audio message responses**: Added `enable_audio_message_response`
      to WhatsApp account configuration, enabling agents to send audio messages in
      addition to text in WhatsApp conversations.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/9
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-03-09-2026-03-09-ae721d55
  source_type: elevenlabs_changelog
  theme: model-support
  theme_matches:
  - matched_terms:
    - claude sonnet
    - gemini
    - llm
    - sonnet
    score: 210
    theme: model-support
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  theme_resolution: manual-semantic-rule-v2
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/OpenCode/2026-03-07-desktop-model-sticks-to-session-after-being-changed|Desktop
  Model sticks to session after being changed]]'
- '[[Changes/Codex CLI/2026-03-08-13617-update-models-json-aibrahim-oai|♯13617 Update
  models.json @aibrahim-oai]]'
- '[[Changes/Open WebUI/2026-03-08-9-model-support-changes-in-v0-8-9|9 Model Support
  changes in v0.8.9]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-03-09-2026-03-09-ae721d55|elevenlabs-2026-03-09-2026-03-09-ae721d55]]'
source_type: elevenlabs_changelog
theme: model-support
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-03-09 · [[Themes/model-support|Model Support]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/3/9) · from [[Releases/ElevenLabs/elevenlabs-2026-03-09-2026-03-09-ae721d55|ElevenLabs updates — 2026-03-09]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **New LLM options**: Added [claude-sonnet-4-6](https://www.anthropic.com/claude/sonnet) and `gemini-3.1-flash-lite-preview` as supported LLM providers for agent conversation configuration.
>
> **Guardrail execution mode**: Custom guardrails now support a configurable `execution_mode` field with the `GuardrailExecutionMode` enum, and have separate input and output schema definitions. This allows more precise control over when guardrail logic runs and which message direction it applies to.
>
> **Guardrail triggered client event**: Added `guardrail_triggered` to the `ClientEvent` enum, enabling agent workflows and client-side handlers to respond when a guardrail fires during a conversation.
>
> **Batch calling concurrency**: Added `target_concurrency_limit` field to the [submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create) request body, allowing you to control the target number of concurrent calls for a given batch.
>
> **Agent testing type filter**: The [list agent tests](https://elevenlabs.io/docs/api-reference/tests/list) endpoint now accepts a `types` query parameter to filter results by test type. The `include_folders` query parameter is deprecated in favor of the new `types` filter.
>
> **Telephony call configuration**: Added `telephony_call_config` to outbound call request schemas for [Twilio](https://elevenlabs.io/docs/api-reference/twilio/outbound-call) and [SIP trunk](https://elevenlabs.io/docs/api-reference/sip-trunk/outbound-call) calls, with a default `ringing_timeout_secs` of 60 seconds.
>
> **WhatsApp audio message responses**: Added `enable_audio_message_response` to WhatsApp account configuration, enabling agents to send audio messages in addition to text in WhatsApp conversations.
>
> Source: https://elevenlabs.io/docs/changelog/2026/3/9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-03-09-python-sdk|Python SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-03-09-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-03-09-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-03-09-elevenagents-63860d|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-03-09-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-09-saml-sso-for-ios-and-android-enterprise-customers-using-saml-based-identity-prov|SAML SSO for iOS and Android]] · Account and Access
- [[Changes/ElevenLabs/2026-03-09-elevencreative-studio|ElevenCreative Studio]] · Agent Mode
- [[Changes/ElevenLabs/2026-03-09-packages|Packages]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-03-09-audio-native|Audio Native]] · Voice and Audio
- [[Changes/ElevenLabs/2026-03-09-javascript-sdk|JavaScript SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-03-09-music|Music]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-09-elevencreative-studio-cd704d|ElevenCreative Studio]] · Editor Experience
- [[Changes/ElevenLabs/2026-03-09-speech-to-text-dec5c9|Speech to Text]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-03-08 · Open WebUI · [[Changes/Open WebUI/2026-03-08-9-model-support-changes-in-v0-8-9|9 Model Support changes in v0.8.9]]
- Later: 2026-03-09 · Google Antigravity · [[Changes/Google Antigravity/2026-03-09-added-support-for-reading-rules-from-agents-md-in-addition-to-gemini-md|Added support for reading rules from AGENTS.md in addition to GEMINI.md]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-03-09-26c43c&body=Card%3A%20Changes%2FElevenLabs%2F2026-03-09-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-03-09-26c43c%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F3%2F9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->