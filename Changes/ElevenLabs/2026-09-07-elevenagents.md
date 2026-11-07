---
card_id: elevenlabs-2026-09-07-5fe86f
date: '2026-09-07'
description: 'ElevenLabs · 2026-09-07 · Agent Mode: **Workspace-wide conversation
  tickets**: Added [List workspace…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1159
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 1a33b069c00caff26d4dec35bfe360513eabf2b74f632388a455deae2ef38e67
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-09-07-5fe86f
  comparison: ''
  date: '2026-09-07'
  description: 'ElevenLabs — ElevenLabs updates — 2026-09-07: **Workspace-wide conversation
    tickets**: Added [List workspace tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list-for-workspace)
    to retrieve conversation triage tickets across accessible agents. Filter by status
    or assignee and use cursor pagination to retrieve up to 100 tickets per page.'
  evidence:
  - quote: '**Workspace-wide conversation tickets**: Added [List workspace tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list-for-workspace)
      to retrieve conversation triage tickets across accessible agents. Filter by
      status or assignee and use cursor pagination to retrieve up to 100 tickets per
      page.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: '**Dynamic variable conversation filters**: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
      and [Text search conversation messages](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search)
      now accept repeatable `dynamic_variable_params` filters. Use `name:op:value`
      with `eq`, `gt`, `gte`, `lt` or `lte`; comparison operators require numeric
      values.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: '**Twilio answering machine detection**: Outbound telephony and batch call
      configurations now support optional `twilio_machine_detection`. Choose `enable`
      for an early human-or-machine verdict or `detect_message_end` to wait for a
      voicemail greeting to finish. Results arrive through the new `answering_machine_detection`
      webhook event.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: '**Data collection value constraints**: Data collection properties can
      now use `allowed_values` to name a dynamic variable containing the permitted
      values. The previous `allowed_values_dynamic_variable` field is deprecated.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: '**Agent metadata**: [List agent branches](https://elevenlabs.io/docs/api-reference/agents/branches/list)
      responses now indicate when a draft was created and whether it predates the
      branch tip. Agent and Speech Engine summaries now require `voice_id`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: '**Knowledge base source URLs**: Agent RAG query chunks now include required
      nullable `source_url`, containing the tracked URL for URL documents.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  - quote: '**Agent response attachments**: `agent_response` WebSocket events now
      include optional `attachments`. Each attachment requires `url` and `name` and
      can include `mime_type`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/9/7
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-09-07-2026-09-07-cf030a1d
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-05-swarm-is-now-available-to-eligible-agents-without-a-separate-enablement-step-so|Swarm
  is now available to eligible agents without a separate enablement step…]]'
- '[[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode
  changes in v2026.9.2]]'
- '[[Changes/ElevenLabs/2026-09-07-javascript-sdk|JavaScript SDK]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-09-07-2026-09-07-cf030a1d|elevenlabs-2026-09-07-2026-09-07-cf030a1d]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-09-07 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/9/7) · from [[Releases/ElevenLabs/elevenlabs-2026-09-07-2026-09-07-cf030a1d|ElevenLabs updates — 2026-09-07]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Workspace-wide conversation tickets**: Added [List workspace tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list-for-workspace) to retrieve conversation triage tickets across accessible agents. Filter by status or assignee and use cursor pagination to retrieve up to 100 tickets per page.
>
> **Dynamic variable conversation filters**: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list) and [Text search conversation messages](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search) now accept repeatable `dynamic_variable_params` filters. Use `name:op:value` with `eq`, `gt`, `gte`, `lt` or `lte`; comparison operators require numeric values.
>
> **Twilio answering machine detection**: Outbound telephony and batch call configurations now support optional `twilio_machine_detection`. Choose `enable` for an early human-or-machine verdict or `detect_message_end` to wait for a voicemail greeting to finish. Results arrive through the new `answering_machine_detection` webhook event.
>
> **Data collection value constraints**: Data collection properties can now use `allowed_values` to name a dynamic variable containing the permitted values. The previous `allowed_values_dynamic_variable` field is deprecated.
>
> **Agent metadata**: [List agent branches](https://elevenlabs.io/docs/api-reference/agents/branches/list) responses now indicate when a draft was created and whether it predates the branch tip. Agent and Speech Engine summaries now require `voice_id`.
>
> **Knowledge base source URLs**: Agent RAG query chunks now include required nullable `source_url`, containing the tracked URL for URL documents.
>
> **Agent response attachments**: `agent_response` WebSocket events now include optional `attachments`. Each attachment requires `url` and `name` and can include `mime_type`.
>
> Source: https://elevenlabs.io/docs/changelog/2026/9/7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-09-07-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-09-07-javascript-sdk|JavaScript SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-09-07-elevenlabs-cli|ElevenLabs CLI]] · Developer Workflow
- [[Changes/ElevenLabs/2026-09-07-workspaces|Workspaces]] · Voice and Audio
- [[Changes/ElevenLabs/2026-09-07-python-sdk|Python SDK]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-05 · OpenClaw · [[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode changes in v2026.9.2]]
- Later: 2026-09-08 · Claude Code · [[Changes/Claude Code/2026-09-08-improved-workflows-agent-detail-tool-calls-are-marked-running-failed-or-done-the|Improved /workflows agent detail]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-09-07-5fe86f&body=Card%3A%20Changes%2FElevenLabs%2F2026-09-07-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-09-07-5fe86f%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F9%2F7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->