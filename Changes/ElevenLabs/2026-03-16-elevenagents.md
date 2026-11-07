---
card_id: elevenlabs-2026-03-16-77e51d
date: '2026-03-16'
description: 'ElevenLabs · 2026-03-16 · Agent Mode: **Users page is now generally
  available**: The [list users](https://elevenlabs.io/docs/api-reference/users/list)
  page…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 984
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 3e3d1dce211c181d79b9ef0718b48d8c4902cb59371c23e7eaabd446e26e1c2f
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-03-16-77e51d
  comparison: ''
  date: '2026-03-16'
  description: 'ElevenLabs — ElevenLabs updates — 2026-03-16: **Users page is now
    generally available**: The [list users](https://elevenlabs.io/docs/api-reference/users/list)
    page, which groups conversations by a user identifier, is now available to all
    workspaces. This allows you to view all users who have interacted with your agents,
    their conversation history, and contact details in a unified view.'
  evidence:
  - quote: '**Users page is now generally available**: The [list users](https://elevenlabs.io/docs/api-reference/users/list)
      page, which groups conversations by a user identifier, is now available to all
      workspaces. This allows you to view all users who have interacted with your
      agents, their conversation history, and contact details in a unified view.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/16
  - quote: '**SIP inbound headers as dynamic variables**: Custom SIP `X-` headers
      from inbound SIP trunking calls are now automatically exposed as dynamic variables
      in ElevenAgents conversations. Any custom SIP header (e.g., `X-Contact-ID`,
      `X-Campaign-ID`) passed by the caller is available in the agent prompt using
      `{{sip_contact_id}}`, `{{sip_campaign_id}}`, etc. These variables are also visible
      in the conversation history under the Phone Call tab. Reserved headers such
      as `X-Call-ID` and `X-Caller-ID` continue to map to `system__call_sid` and `system__caller_id`
      and are not overridden.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/16
  - quote: '**Conversation filtering by tool outcome**: The [list conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
      and [text search conversations](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search)
      endpoints now accept `tool_names_successful` and `tool_names_errored` query
      parameters (array of strings) to filter conversations by which tools succeeded
      or returned errors during the call.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/16
  - quote: '**User listing improvements**: The [list users](https://elevenlabs.io/docs/api-reference/users/list)
      endpoint now supports a `sort_by` query parameter accepting `last_contact_unix_secs`
      (default) or `conversation_count`, and a `branch_id` query parameter to filter
      users by agent branch.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/16
  - quote: '**Force delete tools**: The [delete tool](https://elevenlabs.io/docs/api-reference/tools/delete)
      endpoint now accepts a `force` query parameter (boolean, default `false`). When
      set to `true`, the tool is deleted even if it is used by agents, and it is automatically
      removed from all dependent agents and branches.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/16
  - quote: '**Conversation embedding retention**: The [ElevenAgents settings](https://elevenlabs.io/docs/api-reference/workspace/get)
      response now includes `conversation_embedding_retention_days`, which controls
      how long conversation embeddings are retained (maximum 365 days). A `null` value
      uses the system default of 30 days.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/16
  - quote: '**Content threshold guardrail**: Added the `ContentThresholdGuardrail`
      schema, which provides a configurable threshold-based guardrail with an `is_enabled`
      flag and a `threshold` value for content moderation.'
    source_release: https://elevenlabs.io/docs/changelog/2026/3/16
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-03-16-2026-03-16-c52d3abb
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Replit/2026-03-13-introducing-replit-agent-4|Introducing Replit Agent
  4]]'
- '[[Changes/Claude Code/2026-03-14-improved-background-agent-behavior-killing-a-background-agent-now-preserves-its|Improved
  background agent behavior]]'
- '[[Changes/Codex CLI/2026-03-16-16-agent-mode-changes-in-rust-v0-115-0|16 Agent
  Mode changes in rust-v0.115.0]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-03-16-2026-03-16-c52d3abb|elevenlabs-2026-03-16-2026-03-16-c52d3abb]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-03-16 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/3/16) · from [[Releases/ElevenLabs/elevenlabs-2026-03-16-2026-03-16-c52d3abb|ElevenLabs updates — 2026-03-16]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Users page is now generally available**: The [list users](https://elevenlabs.io/docs/api-reference/users/list) page, which groups conversations by a user identifier, is now available to all workspaces. This allows you to view all users who have interacted with your agents, their conversation history, and contact details in a unified view.
>
> **SIP inbound headers as dynamic variables**: Custom SIP `X-` headers from inbound SIP trunking calls are now automatically exposed as dynamic variables in ElevenAgents conversations. Any custom SIP header (e.g., `X-Contact-ID`, `X-Campaign-ID`) passed by the caller is available in the agent prompt using `{{sip_contact_id}}`, `{{sip_campaign_id}}`, etc. These variables are also visible in the conversation history under the Phone Call tab. Reserved headers such as `X-Call-ID` and `X-Caller-ID` continue to map to `system__call_sid` and `system__caller_id` and are not overridden.
>
> **Conversation filtering by tool outcome**: The [list conversations](https://elevenlabs.io/docs/api-reference/conversations/list) and [text search conversations](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search) endpoints now accept `tool_names_successful` and `tool_names_errored` query parameters (array of strings) to filter conversations by which tools succeeded or returned errors during the call.
>
> **User listing improvements**: The [list users](https://elevenlabs.io/docs/api-reference/users/list) endpoint now supports a `sort_by` query parameter accepting `last_contact_unix_secs` (default) or `conversation_count`, and a `branch_id` query parameter to filter users by agent branch.
>
> **Force delete tools**: The [delete tool](https://elevenlabs.io/docs/api-reference/tools/delete) endpoint now accepts a `force` query parameter (boolean, default `false`). When set to `true`, the tool is deleted even if it is used by agents, and it is automatically removed from all dependent agents and branches.
>
> **Conversation embedding retention**: The [ElevenAgents settings](https://elevenlabs.io/docs/api-reference/workspace/get) response now includes `conversation_embedding_retention_days`, which controls how long conversation embeddings are retained (maximum 365 days). A `null` value uses the system default of 30 days.
>
> **Content threshold guardrail**: Added the `ContentThresholdGuardrail` schema, which provides a configurable threshold-based guardrail with an `is_enabled` flag and a `threshold` value for content moderation.
>
> Source: https://elevenlabs.io/docs/changelog/2026/3/16
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-03-16-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-03-16-javascript-sdk|JavaScript SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-16-python-sdk|Python SDK]] · Multimodal Input
- [[Changes/ElevenLabs/2026-03-16-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-03-16-music|Music]] · Model Support
- [[Changes/ElevenLabs/2026-03-16-ios-sdk|iOS SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-03-16-elevencreative-studio|ElevenCreative Studio]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-03-16 · Codex CLI · [[Changes/Codex CLI/2026-03-16-16-agent-mode-changes-in-rust-v0-115-0|16 Agent Mode changes in rust-v0.115.0]]
- Later: 2026-03-16 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-16-5-agent-mode-changes-in-v1-0-6|5 Agent Mode changes in v1.0.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-03-16-77e51d&body=Card%3A%20Changes%2FElevenLabs%2F2026-03-16-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-03-16-77e51d%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F3%2F16%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->