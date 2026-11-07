---
card_id: elevenlabs-2026-05-25-e7876f
date: '2026-05-25'
description: 'ElevenLabs · 2026-05-25 · Agent Mode: **Text behavior overrides**: Added
  `text_behavior_overrides`, a per-`ConversationInitiationSource` map of…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1054
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: a73787353a9282dc3723287417ae5a6897004a1bcdebb59c4b09e27048ff23d5
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-05-25-e7876f
  comparison: ''
  confidence: low
  date: '2026-05-25'
  description: 'ElevenLabs — ElevenLabs updates — 2026-05-25: **Text behavior overrides**:
    Added `text_behavior_overrides`, a per-`ConversationInitiationSource` map of `BehaviorOverride`
    objects with optional `verbosity`, `output_format` and `interaction_budget` fields
    for channel-specific agent behavior.'
  evidence:
  - quote: '**Text behavior overrides**: Added `text_behavior_overrides`, a per-`ConversationInitiationSource`
      map of `BehaviorOverride` objects with optional `verbosity`, `output_format`
      and `interaction_budget` fields for channel-specific agent behavior.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/25
  - quote: '**Integration sources**: Added Intercom, Telegram and Freshdesk.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/25
  - quote: '**OTLP conversation traces**: [Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get)
      now accepts an optional `format` query parameter. Set `format=otlp_traces` to
      return OTLP-compatible trace data alongside the standard conversation payload.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/25
  - quote: '**ASR keyword overrides**: Added `ASRConversationalConfigOverride` and
      `ASRConversationalConfigOverrideConfig` schemas with optional `keywords` arrays,
      wired into conversation config client override models.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/25
  - quote: '**Webhook auth metadata**: Webhook tool configuration schemas now expose
      optional `auth_resolved_params` (string array) documenting URL placeholders
      resolved from the auth connection.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/25
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-05-25-2026-05-25-1b6f860f
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Replit/2026-05-22-agent-settings-stay-yours-in-shared-projects|Agent
  settings stay yours in shared projects]]'
- '[[Changes/Replit/2026-05-22-agent|Agent]]'
- '[[Changes/GitHub Copilot CLI/2026-05-23-custom-agents-support-opt-in-deferred-tool-loading-via-deferred-tool-loading-in|Custom
  agents support opt-in deferred tool loading via deferred-tool-loading…]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-05-25-2026-05-25-1b6f860f|elevenlabs-2026-05-25-2026-05-25-1b6f860f]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-05-25 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/5/25) · from [[Releases/ElevenLabs/elevenlabs-2026-05-25-2026-05-25-1b6f860f|ElevenLabs updates — 2026-05-25]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Text behavior overrides**: Added `text_behavior_overrides`, a per-`ConversationInitiationSource` map of `BehaviorOverride` objects with optional `verbosity`, `output_format` and `interaction_budget` fields for channel-specific agent behavior.
>
> **Integration sources**: Added Intercom, Telegram and Freshdesk.
>
> **OTLP conversation traces**: [Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get) now accepts an optional `format` query parameter. Set `format=otlp_traces` to return OTLP-compatible trace data alongside the standard conversation payload.
>
> **ASR keyword overrides**: Added `ASRConversationalConfigOverride` and `ASRConversationalConfigOverrideConfig` schemas with optional `keywords` arrays, wired into conversation config client override models.
>
> **Webhook auth metadata**: Webhook tool configuration schemas now expose optional `auth_resolved_params` (string array) documenting URL placeholders resolved from the auth connection.
>
> Source: https://elevenlabs.io/docs/changelog/2026/5/25
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-05-25-elevencreative-studio|ElevenCreative Studio]] · Voice and Audio
- [[Changes/ElevenLabs/2026-05-25-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-05-25-elevencreative-studio-17d8d4|ElevenCreative Studio]] · Voice and Audio
- [[Changes/ElevenLabs/2026-05-25-music|Music]] · Automation and Scheduling
- [[Changes/ElevenLabs/2026-05-25-music-5f1ccf|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-05-25-javascript-sdk|JavaScript SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-05-25-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-05-25-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-05-25-introducing-speech-engine|Introducing Speech Engine]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-05-23 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-23-custom-agents-support-opt-in-deferred-tool-loading-via-deferred-tool-loading-in|Custom agents support opt-in deferred tool loading via deferred-tool-loading…]]
- Later: 2026-05-26 · AnythingLLM · [[Changes/AnythingLLM/2026-05-26-10-agent-mode-changes-in-v1-13-0|10 Agent Mode changes in v1.13.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-05-25-e7876f&body=Card%3A%20Changes%2FElevenLabs%2F2026-05-25-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-05-25-e7876f%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F5%2F25%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->