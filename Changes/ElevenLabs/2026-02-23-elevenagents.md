---
card_id: elevenlabs-2026-02-23-8ad570
date: '2026-02-23'
description: 'ElevenLabs · 2026-02-23 · Agent Mode: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
  [Update…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 963
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: cc9c5817b8dfca38c737e816391746fc3329525e5e17b738464833ce8ae9cc71
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-02-23-8ad570
  comparison: ''
  confidence: low
  date: '2026-02-23'
  description: 'ElevenLabs — ElevenLabs updates — 2026-02-23: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
    [Update agent](https://elevenlabs.io/docs/api-reference/agents/update), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get)'
  evidence:
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Update agent](https://elevenlabs.io/docs/api-reference/agents/update), [Get
      agent](https://elevenlabs.io/docs/api-reference/agents/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Added `coaching_settings` field for agent training configuration
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Added `conversation_history_redaction` in `platform_settings.privacy` with
      configurable entity types
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: 'Added new guardrails: `focus` and `prompt_injection` in `platform_settings.guardrails`'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Removed `alignment` guardrail from `platform_settings.guardrails`
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Added `qwen3_embedding_4b` as an embedding model option in RAG configuration
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Updated numeric field descriptions for better clarity on ranges and defaults
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '[Create MCP server](https://elevenlabs.io/docs/api-reference/mcp/create),
      [Update MCP server](https://elevenlabs.io/docs/api-reference/mcp/update), [Get
      MCP server](https://elevenlabs.io/docs/api-reference/mcp/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Added `auth_connection` field (optional) to enable OAuth and advanced authentication
      methods
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Added `secret_token` field to PATCH endpoint for backward compatibility
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Auth connection takes precedence over `secret_token` when both are provided
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '[Create MCP tool config](https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/create),
      [Update MCP tool config](https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/update),
      [Get MCP tool config](https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Added `input_overrides` field - allows overriding tool input parameters
      with constants, dynamic variables, or LLM-generated values
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '[Create RAG index](https://elevenlabs.io/docs/api-reference/knowledge-base/compute-rag-index),
      [Delete RAG index](https://elevenlabs.io/docs/api-reference/knowledge-base/delete-rag-index)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Added `qwen3_embedding_4b` to the `embedding_model` enum
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '[Get conversations](https://elevenlabs.io/docs/api-reference/conversations/get-conversations)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Deprecated `search` query parameter (use the new dedicated search endpoints
      instead)
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '[Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Added `hiding_reason` field to indicate why a conversation might be hidden
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Extended conversation transcript entries to support `file_input` metadata
      with new `ChatSourceMedium` type (audio, text, image, file)
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '[Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation),
      [Simulate conversation stream](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation-stream)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Updated all nested configuration fields with improved descriptions and
      validation ranges
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '[Get agent branches](https://elevenlabs.io/docs/api-reference/agents/branches/get),
      [Update agent branch](https://elevenlabs.io/docs/api-reference/agents/branches/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Updated `current_live_percentage` field description for clarity
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: '[Get ElevenAgents settings](https://elevenlabs.io/docs/api-reference/workspace/get),
      [Update ElevenAgents settings](https://elevenlabs.io/docs/api-reference/workspace/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  - quote: Updated `rag_retention_period_days` field with improved description
    source_release: https://elevenlabs.io/docs/changelog/2026/2/23
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-02-23-2026-02-23-19067983
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-02-19-3-agent-mode-changes-in-v0-0-412|3 Agent
  Mode changes in v0.0.412]]'
- '[[Changes/Claude Code/2026-02-20-2-agent-mode-changes-in-v2-1-50|2 Agent Mode changes
  in v2.1.50]]'
- '[[Changes/Replit/2026-02-20-production-deployment-logs-access|Production deployment
  logs access]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-02-23-2026-02-23-19067983|elevenlabs-2026-02-23-2026-02-23-19067983]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-02-23 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/2/23) · from [[Releases/ElevenLabs/elevenlabs-2026-02-23-2026-02-23-19067983|ElevenLabs updates — 2026-02-23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get)
>
> Added `coaching_settings` field for agent training configuration
>
> Added `conversation_history_redaction` in `platform_settings.privacy` with configurable entity types
>
> Added new guardrails: `focus` and `prompt_injection` in `platform_settings.guardrails`
>
> Removed `alignment` guardrail from `platform_settings.guardrails`
>
> Added `qwen3_embedding_4b` as an embedding model option in RAG configuration
>
> Updated numeric field descriptions for better clarity on ranges and defaults
>
> [Create MCP server](https://elevenlabs.io/docs/api-reference/mcp/create), [Update MCP server](https://elevenlabs.io/docs/api-reference/mcp/update), [Get MCP server](https://elevenlabs.io/docs/api-reference/mcp/get)
>
> Added `auth_connection` field (optional) to enable OAuth and advanced authentication methods
>
> Added `secret_token` field to PATCH endpoint for backward compatibility
>
> Auth connection takes precedence over `secret_token` when both are provided
>
> [Create MCP tool config](https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/create), [Update MCP tool config](https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/update), [Get MCP tool config](https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/get)
>
> Added `input_overrides` field - allows overriding tool input parameters with constants, dynamic variables, or LLM-generated values
>
> [Create RAG index](https://elevenlabs.io/docs/api-reference/knowledge-base/compute-rag-index), [Delete RAG index](https://elevenlabs.io/docs/api-reference/knowledge-base/delete-rag-index)
>
> Added `qwen3_embedding_4b` to the `embedding_model` enum
>
> [Get conversations](https://elevenlabs.io/docs/api-reference/conversations/get-conversations)
>
> Deprecated `search` query parameter (use the new dedicated search endpoints instead)
>
> [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)
>
> Added `hiding_reason` field to indicate why a conversation might be hidden
>
> Extended conversation transcript entries to support `file_input` metadata with new `ChatSourceMedium` type (audio, text, image, file)
>
> [Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation), [Simulate conversation stream](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation-stream)
>
> Updated all nested configuration fields with improved descriptions and validation ranges
>
> [Get agent branches](https://elevenlabs.io/docs/api-reference/agents/branches/get), [Update agent branch](https://elevenlabs.io/docs/api-reference/agents/branches/update)
>
> Updated `current_live_percentage` field description for clarity
>
> [Get ElevenAgents settings](https://elevenlabs.io/docs/api-reference/workspace/get), [Update ElevenAgents settings](https://elevenlabs.io/docs/api-reference/workspace/update)
>
> Updated `rag_retention_period_days` field with improved description
>
> Source: https://elevenlabs.io/docs/changelog/2026/2/23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-02-23-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-23-text-to-voice|Text to Voice]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-23-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-02-23-workspaces|Workspaces]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-02-23-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-02-23-music|Music]] · Collaboration
- [[Changes/ElevenLabs/2026-02-23-removed-endpoints|Removed Endpoints]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-23-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-23-elevenagents-f6efef|ElevenAgents]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-02-20 · Replit · [[Changes/Replit/2026-02-20-production-deployment-logs-access|Production deployment logs access]]
- Later: 2026-02-23 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-23-2-agent-mode-changes-in-v0-0-415|2 Agent Mode changes in v0.0.415]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-02-23-8ad570&body=Card%3A%20Changes%2FElevenLabs%2F2026-02-23-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-02-23-8ad570%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F2%2F23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->