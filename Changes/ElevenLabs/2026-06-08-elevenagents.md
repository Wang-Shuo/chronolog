---
card_id: elevenlabs-2026-06-08-3b2f04
date: '2026-06-08'
description: 'ElevenLabs · 2026-06-08 · Agent Mode: **Turn model configuration**:
  `TurnConfig` and `TurnConfigWorkflowOverride` add optional `turn_model` (`turn_v2`
  or…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1068
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 9e8602fdae21318825ba4811ee2ccb89250f22125c29ab759e7d54c63eb29322
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-06-08-3b2f04
  comparison: ''
  confidence: low
  date: '2026-06-08'
  description: 'ElevenLabs — ElevenLabs updates — 2026-06-08: **Turn model configuration**:
    `TurnConfig` and `TurnConfigWorkflowOverride` add optional `turn_model` (`turn_v2`
    or `turn_v3`, default `turn_v3`) to select the turn detection model version per
    agent or workflow node.'
  evidence:
  - quote: '**Turn model configuration**: `TurnConfig` and `TurnConfigWorkflowOverride`
      add optional `turn_model` (`turn_v2` or `turn_v3`, default `turn_v3`) to select
      the turn detection model version per agent or workflow node.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/8
  - quote: '**Soft timeout filler messages**: `SoftTimeoutConfig` and `SoftTimeoutConfigWorkflowOverride`
      add optional `additional_soft_timeout_messages` (array of strings, up to 7)
      and `max_soft_timeouts_per_generation` (integer, 1–8, default `1`). The primary
      `message` applies to the first timeout; subsequent timeouts use the additional
      messages or a built-in filler.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/8
  - quote: '**ASR provider default**: The default `ASRConversationalConfig.provider`
      value changes from `elevenlabs` to `scribe_realtime`. The `elevenlabs` value
      remains in the enum but is deprecated.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/8
  - quote: '**Conversation product field**: [Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get)
      response adds optional `conversation_product` (string, default `agent`) to identify
      the product that handled the conversation.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/8
  - quote: '**Knowledge base external sync**: Knowledge base file and folder response
      models add optional `external_sync_info` (Google Drive sync metadata via `ExternalFileSyncInfo`
      / `ExternalFolderSyncInfo`) and optional `is_frozen` (boolean) to indicate whether
      synced content can be edited.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/8
  - quote: '**Tool schema omit overrides**: ConvAI tool JSON schema properties add
      optional `is_omitted` (boolean) and `OmitSchemaOverride` with `source: omit`,
      allowing fields to be explicitly omitted from tool payloads.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/8
  - quote: '**Procedure guardrails**: Procedure version schemas add optional `guardrails`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/8
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-06-08-2026-06-08-4f50e6b2
  source_type: elevenlabs_changelog
  theme: agent-mode
  theme_matches:
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-06-claude-agents-typing-a-url-into-the-list-now-filters-to-the-session-whose-first|claude
  agents: typing a URL into the list now filters to the session whose first…]]'
- '[[Changes/Claude Code/2026-06-08-2-agent-mode-changes-in-v2-1-169|2 Agent Mode
  changes in v2.1.169]]'
- '[[Changes/Codex CLI/2026-06-08-8-agent-mode-changes-in-rust-v0-138-0|8 Agent Mode
  changes in rust-v0.138.0]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-06-08-2026-06-08-4f50e6b2|elevenlabs-2026-06-08-2026-06-08-4f50e6b2]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-06-08 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/6/8) · from [[Releases/ElevenLabs/elevenlabs-2026-06-08-2026-06-08-4f50e6b2|ElevenLabs updates — 2026-06-08]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Turn model configuration**: `TurnConfig` and `TurnConfigWorkflowOverride` add optional `turn_model` (`turn_v2` or `turn_v3`, default `turn_v3`) to select the turn detection model version per agent or workflow node.
>
> **Soft timeout filler messages**: `SoftTimeoutConfig` and `SoftTimeoutConfigWorkflowOverride` add optional `additional_soft_timeout_messages` (array of strings, up to 7) and `max_soft_timeouts_per_generation` (integer, 1–8, default `1`). The primary `message` applies to the first timeout; subsequent timeouts use the additional messages or a built-in filler.
>
> **ASR provider default**: The default `ASRConversationalConfig.provider` value changes from `elevenlabs` to `scribe_realtime`. The `elevenlabs` value remains in the enum but is deprecated.
>
> **Conversation product field**: [Get conversation details](https://elevenlabs.io/docs/api-reference/conversations/get) response adds optional `conversation_product` (string, default `agent`) to identify the product that handled the conversation.
>
> **Knowledge base external sync**: Knowledge base file and folder response models add optional `external_sync_info` (Google Drive sync metadata via `ExternalFileSyncInfo` / `ExternalFolderSyncInfo`) and optional `is_frozen` (boolean) to indicate whether synced content can be edited.
>
> **Tool schema omit overrides**: ConvAI tool JSON schema properties add optional `is_omitted` (boolean) and `OmitSchemaOverride` with `source: omit`, allowing fields to be explicitly omitted from tool payloads.
>
> **Procedure guardrails**: Procedure version schemas add optional `guardrails`.
>
> Source: https://elevenlabs.io/docs/changelog/2026/6/8
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-06-08-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-08-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-06-08-python-sdk|Python SDK]] · Model Support
- [[Changes/ElevenLabs/2026-06-08-text-to-dialogue|Text to Dialogue]] · Enterprise and Administration
- [[Changes/ElevenLabs/2026-06-08-text-to-speech|Text to Speech]] · Model Support
- [[Changes/ElevenLabs/2026-06-08-javascript-sdk|JavaScript SDK]] · Model Support
- [[Changes/ElevenLabs/2026-06-08-packages|Packages]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-08 · Codex CLI · [[Changes/Codex CLI/2026-06-08-8-agent-mode-changes-in-rust-v0-138-0|8 Agent Mode changes in rust-v0.138.0]]
- Later: 2026-06-08 · v0 · [[Changes/v0/2026-06-08-2-agent-mode-changes-in-changelog-update|2 Agent Mode changes in Changelog update]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-06-08-3b2f04&body=Card%3A%20Changes%2FElevenLabs%2F2026-06-08-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-06-08-3b2f04%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F6%2F8%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->