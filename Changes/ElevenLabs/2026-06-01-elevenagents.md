---
card_id: elevenlabs-2026-06-01-be1883
date: '2026-06-01'
description: 'ElevenLabs · 2026-06-01 · Apps and Integrations: **Exotel telephony
  integration**: Added Exotel as a first-class telephony provider alongside Twilio
  and SIP…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1166
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 8187e37021dfaa5e477f1ff88d2a7a4a8df0755e6be7a0723595944cd473b0b4
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-06-01-be1883
  comparison: ''
  confidence: low
  date: '2026-06-01'
  description: 'ElevenLabs — ElevenLabs updates — 2026-06-01: **Exotel telephony integration**:
    Added Exotel as a first-class telephony provider alongside Twilio and SIP trunking.
    New [Exotel outbound call](https://elevenlabs.io/docs/api-reference/exotel/outbound-call)
    endpoint (`POST /v1/convai/exotel/outbound-call`) initiates outbound calls via
    the Exotel Connect API with `agent_id`, `agent_phone_number_id`, `to_number`,
    optional `conversation_initiation_client_data` and optional `telephony_call_config`.
    Exotel phone number create, list, get and update schemas are available, and `exotel`
    is added to `TelephonyProvider`, conversation initiation source and transfer result
    enums.'
  evidence:
  - quote: '**Exotel telephony integration**: Added Exotel as a first-class telephony
      provider alongside Twilio and SIP trunking. New [Exotel outbound call](https://elevenlabs.io/docs/api-reference/exotel/outbound-call)
      endpoint (`POST /v1/convai/exotel/outbound-call`) initiates outbound calls via
      the Exotel Connect API with `agent_id`, `agent_phone_number_id`, `to_number`,
      optional `conversation_initiation_client_data` and optional `telephony_call_config`.
      Exotel phone number create, list, get and update schemas are available, and
      `exotel` is added to `TelephonyProvider`, conversation initiation source and
      transfer result enums.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  - quote: '**Workflow-aware agent transfers**: `AgentTransfer` now allows a nullable
      `agent_id` so transfers can stay on the current agent, adds optional `node_id`
      to start at a specific node in the destination workflow, and only requires `condition`.
      Successful `transfer_to_agent` tool results can include nullable `to_node`,
      aligning transfers with workflow-node targets.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  - quote: '**Agent test repeat runs**: [Run tests on the agent](https://elevenlabs.io/docs/api-reference/tests/run-tests)
      accepts optional `repeat_count` (integer, 1–20, default `1`) to run each test
      multiple times. When `repeat_count` is greater than 1, responses include `bucketing_status`
      and `result_groups` for grouped summaries. Unit test create, update and summary
      schemas add optional `conversation_initiation_source` so tests can simulate
      a specific channel.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  - quote: '**Conversation filtering**: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
      adds optional `workflow_node_entered_id` (string) to filter conversations that
      entered a given workflow node. [Text search conversation messages](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search)
      adds optional `topic_ids` (array of strings) to filter by topic IDs assigned
      during topic discovery.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  - quote: '**Agent versioning query parameters deprecated**: `enable_versioning`
      on [create agent](https://elevenlabs.io/docs/api-reference/agents/create) and
      `enable_versioning_if_not_enabled` on [update agent](https://elevenlabs.io/docs/api-reference/agents/update)
      are marked deprecated. All agents are versioned and these parameters are ignored.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  - quote: '**Procedure compiler mode**: Removed `append` from `ProcedureCompilerMode`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/6/1
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-06-01-2026-06-01-63e7e167
  source_type: elevenlabs_changelog
  theme: apps-integrations
  theme_matches:
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  - matched_terms:
    - integration
    score: 50
    theme: apps-integrations
  theme_resolution: manual-semantic-rule-v1
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Replit/2026-05-29-integrations|Integrations]]'
- '[[Changes/Codex CLI/2026-06-01-20-apps-and-integrations-changes-in-rust-v0-136-0|20
  Apps and Integrations changes in rust-v0.136.0]]'
- '[[Changes/ElevenLabs/2026-06-01-sdk-releases|SDK Releases]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-06-01-2026-06-01-63e7e167|elevenlabs-2026-06-01-2026-06-01-63e7e167]]'
source_type: elevenlabs_changelog
theme: apps-integrations
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-06-01 · [[Themes/apps-integrations|Apps and Integrations]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/6/1) · from [[Releases/ElevenLabs/elevenlabs-2026-06-01-2026-06-01-63e7e167|ElevenLabs updates — 2026-06-01]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Exotel telephony integration**: Added Exotel as a first-class telephony provider alongside Twilio and SIP trunking. New [Exotel outbound call](https://elevenlabs.io/docs/api-reference/exotel/outbound-call) endpoint (`POST /v1/convai/exotel/outbound-call`) initiates outbound calls via the Exotel Connect API with `agent_id`, `agent_phone_number_id`, `to_number`, optional `conversation_initiation_client_data` and optional `telephony_call_config`. Exotel phone number create, list, get and update schemas are available, and `exotel` is added to `TelephonyProvider`, conversation initiation source and transfer result enums.
>
> **Workflow-aware agent transfers**: `AgentTransfer` now allows a nullable `agent_id` so transfers can stay on the current agent, adds optional `node_id` to start at a specific node in the destination workflow, and only requires `condition`. Successful `transfer_to_agent` tool results can include nullable `to_node`, aligning transfers with workflow-node targets.
>
> **Agent test repeat runs**: [Run tests on the agent](https://elevenlabs.io/docs/api-reference/tests/run-tests) accepts optional `repeat_count` (integer, 1–20, default `1`) to run each test multiple times. When `repeat_count` is greater than 1, responses include `bucketing_status` and `result_groups` for grouped summaries. Unit test create, update and summary schemas add optional `conversation_initiation_source` so tests can simulate a specific channel.
>
> **Conversation filtering**: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list) adds optional `workflow_node_entered_id` (string) to filter conversations that entered a given workflow node. [Text search conversation messages](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search) adds optional `topic_ids` (array of strings) to filter by topic IDs assigned during topic discovery.
>
> **Agent versioning query parameters deprecated**: `enable_versioning` on [create agent](https://elevenlabs.io/docs/api-reference/agents/create) and `enable_versioning_if_not_enabled` on [update agent](https://elevenlabs.io/docs/api-reference/agents/update) are marked deprecated. All agents are versioned and these parameters are ignored.
>
> **Procedure compiler mode**: Removed `append` from `ProcedureCompilerMode`.
>
> Source: https://elevenlabs.io/docs/changelog/2026/6/1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-06-01-workspaces|Workspaces]] · Model Support
- [[Changes/ElevenLabs/2026-06-01-dubbing|Dubbing]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-01-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-06-01-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-01-speech-to-text-9a648b|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-06-01-dubbing-fad5c5|Dubbing]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-06-01 · Codex CLI · [[Changes/Codex CLI/2026-06-01-20-apps-and-integrations-changes-in-rust-v0-136-0|20 Apps and Integrations changes in rust-v0.136.0]]
- Later: 2026-06-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-01-5-apps-and-integrations-changes-in-v1-0-57|5 Apps and Integrations changes in v1.0.57]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-06-01-be1883&body=Card%3A%20Changes%2FElevenLabs%2F2026-06-01-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-06-01-be1883%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F6%2F1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->