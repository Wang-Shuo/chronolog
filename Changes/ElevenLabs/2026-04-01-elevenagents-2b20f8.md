---
card_id: elevenlabs-2026-04-01-2b20f8
date: '2026-04-01'
description: 'ElevenLabs · 2026-04-01 · Apps and Integrations: **MCP tool scoping
  in agent workflows**: Agent workflow nodes can now restrict which MCP tools a sub-agent
  is…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1105
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 3c8dd33226c99eaf7323df51d1ecd3c4db47fa1679c99cc248b1c35d43cf8ffb
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-04-01-2b20f8
  comparison: ''
  confidence: low
  date: '2026-04-01'
  description: 'ElevenLabs — ElevenLabs updates — 2026-04-01: **MCP tool scoping in
    agent workflows**: Agent workflow nodes can now restrict which MCP tools a sub-agent
    is permitted to call. When tool inheritance is disabled on a node, only the explicitly
    selected MCP tools are loaded for that sub-agent, giving teams precise control
    over tool access per workflow step.'
  evidence:
  - quote: '**MCP tool scoping in agent workflows**: Agent workflow nodes can now
      restrict which MCP tools a sub-agent is permitted to call. When tool inheritance
      is disabled on a node, only the explicitly selected MCP tools are loaded for
      that sub-agent, giving teams precise control over tool access per workflow step.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: '**Conversation file uploads**: The [create agent](https://elevenlabs.io/docs/api-reference/agents/create)
      and [update agent](https://elevenlabs.io/docs/api-reference/agents/update) endpoints
      now support a `file_input` field on `ConversationConfig`. When enabled, end
      users can attach images or PDFs in chat (requires an LLM with multimodal input
      support). Configurable with `enabled` (boolean) and `max_files_per_conversation`
      (integer).'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: '**Re-run conversation analysis**: New [run conversation analysis](https://elevenlabs.io/docs/api-reference/conversations/analysis/run-analysis)
      endpoint (`POST /v1/convai/conversations/{conversation_id}/analysis/run`) re-evaluates
      a completed conversation using the agent''s current evaluation criteria and
      data collection settings, without needing a new call.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: '**Tool response mocking for tests**: Agent simulation tests and test suite
      invocations now support a `tool_mock_config` field to control how tool calls
      are handled during testing. Use `MockingStrategy` (`all`, `selected`, `none`)
      to choose which tools are mocked and `MockNoMatchBehavior` (`call_real_tool`,
      `raise_error`) to set the fallback when no mock matches.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: '**Text search sort order**: The [text search conversations](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search)
      endpoint now accepts a `sort_by` query parameter with values `search_score`
      (default) or `created_at`, allowing you to control whether results are ordered
      by relevance or recency.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: '**mTLS auth connections**: Agent auth connections now support mutual TLS
      (`mtls`) as an `auth_type`, in addition to the existing options. New `CreateMTLSAuthRequest`
      and `MTLSAuthResponse` schemas are available for creating and retrieving mTLS-authenticated
      connections.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: '**Max duration message**: Added `max_conversation_duration_message` field
      to agent configuration. When set to a non-empty string, the agent will send
      this message to the user when the maximum conversation duration is reached.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  - quote: '**Branch and environment in conversation initiation**: Added `branch_id`
      and `environment` optional fields to the conversation initiation client data
      (`ConversationInitiationClientDataRequest`) and [submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create)
      request body, enabling routing to specific agent branches and environments.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/1
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-04-01-2026-04-01-d4336c3f
  source_type: elevenlabs_changelog
  theme: apps-integrations
  theme_matches:
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  theme_resolution: manual-semantic-rule-v1
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-03-31-5-apps-and-integrations-changes-in-v1-0-14|5
  Apps and Integrations changes in v1.0.14]]'
- '[[Changes/Claude Code/2026-04-01-3-apps-and-integrations-changes-in-v2-1-89|3 Apps
  and Integrations changes in v2.1.89]]'
- '[[Changes/Claude Code/2026-04-01-2-apps-and-integrations-changes-in-v2-1-90|2 Apps
  and Integrations changes in v2.1.90]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-04-01-2026-04-01-d4336c3f|elevenlabs-2026-04-01-2026-04-01-d4336c3f]]'
source_type: elevenlabs_changelog
theme: apps-integrations
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-04-01 · [[Themes/apps-integrations|Apps and Integrations]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/4/1) · from [[Releases/ElevenLabs/elevenlabs-2026-04-01-2026-04-01-d4336c3f|ElevenLabs updates — 2026-04-01]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **MCP tool scoping in agent workflows**: Agent workflow nodes can now restrict which MCP tools a sub-agent is permitted to call. When tool inheritance is disabled on a node, only the explicitly selected MCP tools are loaded for that sub-agent, giving teams precise control over tool access per workflow step.
>
> **Conversation file uploads**: The [create agent](https://elevenlabs.io/docs/api-reference/agents/create) and [update agent](https://elevenlabs.io/docs/api-reference/agents/update) endpoints now support a `file_input` field on `ConversationConfig`. When enabled, end users can attach images or PDFs in chat (requires an LLM with multimodal input support). Configurable with `enabled` (boolean) and `max_files_per_conversation` (integer).
>
> **Re-run conversation analysis**: New [run conversation analysis](https://elevenlabs.io/docs/api-reference/conversations/analysis/run-analysis) endpoint (`POST /v1/convai/conversations/{conversation_id}/analysis/run`) re-evaluates a completed conversation using the agent's current evaluation criteria and data collection settings, without needing a new call.
>
> **Tool response mocking for tests**: Agent simulation tests and test suite invocations now support a `tool_mock_config` field to control how tool calls are handled during testing. Use `MockingStrategy` (`all`, `selected`, `none`) to choose which tools are mocked and `MockNoMatchBehavior` (`call_real_tool`, `raise_error`) to set the fallback when no mock matches.
>
> **Text search sort order**: The [text search conversations](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search) endpoint now accepts a `sort_by` query parameter with values `search_score` (default) or `created_at`, allowing you to control whether results are ordered by relevance or recency.
>
> **mTLS auth connections**: Agent auth connections now support mutual TLS (`mtls`) as an `auth_type`, in addition to the existing options. New `CreateMTLSAuthRequest` and `MTLSAuthResponse` schemas are available for creating and retrieving mTLS-authenticated connections.
>
> **Max duration message**: Added `max_conversation_duration_message` field to agent configuration. When set to a non-empty string, the agent will send this message to the user when the maximum conversation duration is reached.
>
> **Branch and environment in conversation initiation**: Added `branch_id` and `environment` optional fields to the conversation initiation client data (`ConversationInitiationClientDataRequest`) and [submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create) request body, enabling routing to specific agent branches and environments.
>
> Source: https://elevenlabs.io/docs/changelog/2026/4/1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-04-01-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-01-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-01-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-04-01-javascript-sdk|JavaScript SDK]] · Multimodal Input
- [[Changes/ElevenLabs/2026-04-01-packages|Packages]] · Agent Mode
- [[Changes/ElevenLabs/2026-04-01-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-01-voices-7b77ff|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-01-speech-to-text-8868d1|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-01-new-endpoints|New Endpoints]] · Agent Mode
- [[Changes/ElevenLabs/2026-04-01-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-04-01-sdk-releases|SDK Releases]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-01 · Claude Code · [[Changes/Claude Code/2026-04-01-2-apps-and-integrations-changes-in-v2-1-90|2 Apps and Integrations changes in v2.1.90]]
- Later: 2026-04-01 · Gemini CLI · [[Changes/Gemini CLI/2026-04-01-5-apps-and-integrations-changes-in-v0-36-0|5 Apps and Integrations changes in v0.36.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-04-01-2b20f8&body=Card%3A%20Changes%2FElevenLabs%2F2026-04-01-elevenagents-2b20f8.md%0ACard%20ID%3A%20elevenlabs-2026-04-01-2b20f8%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F4%2F1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->