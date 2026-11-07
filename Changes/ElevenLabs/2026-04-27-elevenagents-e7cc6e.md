---
card_id: elevenlabs-2026-04-27-e7cc6e
date: '2026-04-27'
description: 'ElevenLabs · 2026-04-27 · Agent Mode: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
  [Get…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1026
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: f7d3bc06dc0873e74e6c7b115c73c437a4484fa71a17cbca0e5124bc575486f2
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-04-27-e7cc6e
  comparison: ''
  confidence: low
  date: '2026-04-27'
  description: 'ElevenLabs — ElevenLabs updates — 2026-04-27: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
    [Get agent](https://elevenlabs.io/docs/api-reference/agents/get), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
  evidence:
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Get agent](https://elevenlabs.io/docs/api-reference/agents/get), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: 'Added `trust_context` field (`AgentTrustContext` enum: `unknown` | `low`
      | `high`, default `unknown`) on `AgentPlatformSettingsRequestModel`'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Added `source_attribution` field (boolean, default `false`) on `ConversationConfig`
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '[Update MCP server configuration](https://elevenlabs.io/docs/api-reference/mcp/update),
      [Create MCP server](https://elevenlabs.io/docs/api-reference/mcp/create)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: 'Added `pre_tool_speech` field (`PreToolSpeechMode` enum: `auto` | `force`
      | `off`, default `auto`)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Added `response_timeout_secs` field (integer, default `30`, min `5`, max
      `120`)
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '[Create configuration override](https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/create),
      [Update configuration override](https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Added `pre_tool_speech` field (`PreToolSpeechMode` enum, nullable, optional)
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Added `response_timeout_secs` field (integer, nullable, optional)
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Added `response_mocks` field on `MCPToolConfigOverride-Input` / `MCPToolConfigOverride-Output`
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Marked `force_pre_tool_speech` as deprecated; use `pre_tool_speech` instead
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '[List tests](https://elevenlabs.io/docs/api-reference/tests/list)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: 'Added optional `sharing_mode` query parameter (`TestSharingMode` enum:
      `all` | `shared_with_me`, default `all`)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '[Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation),
      [Stream simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation-stream)'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Refactored `dynamic_variables` and `dynamic_variable_placeholders` payloads
      to reference unified `DynamicVariableValueType-Input` / `DynamicVariableValueType-Output`
      schemas with broader nested and list value support
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '`Tool` schema'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Added `icons` field (array of `Icon`, nullable) for UI display
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Added `execution` field (`ToolExecution`, nullable) including `taskSupport`
      (`forbidden` | `optional` | `required`)
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '`ClientEvent` enum'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Added `agent_response_complete` value with new `AgentResponseCompleteClientEvent`
      response model
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '`ProcedureCompilerMode` enum'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Default changed from `deterministic` to `append`
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Removed `llm` value
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '`ConversationHistoryTranscriptCommonModel`, `ConversationHistoryTranscriptResponseModel`'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Added `used_static_kb_document_ids` field (array of strings)
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '`RagRetrievalInfo`'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Added `used_chunk_ids` field (array of strings)
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '`DynamicVariableAssignment`'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Added `preserve_native_type` field (boolean) for keeping typed values instead
      of coercing to strings
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Workflow nodes
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Added `auto_advance_after_first_response` field on relevant workflow node
      schemas
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Tool configuration documentation
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: Added `response_body_schema` field for documenting expected response shape
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-04-27-2026-04-27-7b6333fc
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/OpenCode/2026-04-26-core-sent-an-opencode-version-user-agent-header-with-http-requests|Core
  Sent an opencode/version User-Agent header with HTTP requests]]'
- '[[Changes/ElevenLabs/2026-04-27-swift-sdk|Swift SDK]]'
- '[[Changes/ElevenLabs/2026-04-27-packages|Packages]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-04-27-2026-04-27-7b6333fc|elevenlabs-2026-04-27-2026-04-27-7b6333fc]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-04-27 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/4/27) · from [[Releases/ElevenLabs/elevenlabs-2026-04-27-2026-04-27-7b6333fc|ElevenLabs updates — 2026-04-27]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
>
> Added `trust_context` field (`AgentTrustContext` enum: `unknown` | `low` | `high`, default `unknown`) on `AgentPlatformSettingsRequestModel`
>
> Added `source_attribution` field (boolean, default `false`) on `ConversationConfig`
>
> [Update MCP server configuration](https://elevenlabs.io/docs/api-reference/mcp/update), [Create MCP server](https://elevenlabs.io/docs/api-reference/mcp/create)
>
> Added `pre_tool_speech` field (`PreToolSpeechMode` enum: `auto` | `force` | `off`, default `auto`)
>
> Added `response_timeout_secs` field (integer, default `30`, min `5`, max `120`)
>
> [Create configuration override](https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/create), [Update configuration override](https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/update)
>
> Added `pre_tool_speech` field (`PreToolSpeechMode` enum, nullable, optional)
>
> Added `response_timeout_secs` field (integer, nullable, optional)
>
> Added `response_mocks` field on `MCPToolConfigOverride-Input` / `MCPToolConfigOverride-Output`
>
> Marked `force_pre_tool_speech` as deprecated; use `pre_tool_speech` instead
>
> [List tests](https://elevenlabs.io/docs/api-reference/tests/list)
>
> Added optional `sharing_mode` query parameter (`TestSharingMode` enum: `all` | `shared_with_me`, default `all`)
>
> [Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation), [Stream simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation-stream)
>
> Refactored `dynamic_variables` and `dynamic_variable_placeholders` payloads to reference unified `DynamicVariableValueType-Input` / `DynamicVariableValueType-Output` schemas with broader nested and list value support
>
> `Tool` schema
>
> Added `icons` field (array of `Icon`, nullable) for UI display
>
> Added `execution` field (`ToolExecution`, nullable) including `taskSupport` (`forbidden` | `optional` | `required`)
>
> `ClientEvent` enum
>
> Added `agent_response_complete` value with new `AgentResponseCompleteClientEvent` response model
>
> `ProcedureCompilerMode` enum
>
> Default changed from `deterministic` to `append`
>
> Removed `llm` value
>
> `ConversationHistoryTranscriptCommonModel`, `ConversationHistoryTranscriptResponseModel`
>
> Added `used_static_kb_document_ids` field (array of strings)
>
> `RagRetrievalInfo`
>
> Added `used_chunk_ids` field (array of strings)
>
> `DynamicVariableAssignment`
>
> Added `preserve_native_type` field (boolean) for keeping typed values instead of coercing to strings
>
> Workflow nodes
>
> Added `auto_advance_after_first_response` field on relevant workflow node schemas
>
> Tool configuration documentation
>
> Added `response_body_schema` field for documenting expected response shape
>
> Source: https://elevenlabs.io/docs/changelog/2026/4/27
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-04-27-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-27-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-04-27-audio-isolation|Audio Isolation]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-27-other|Other]] · Collaboration
- [[Changes/ElevenLabs/2026-04-27-swift-sdk|Swift SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-04-27-new-endpoints|New Endpoints]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-27-packages|Packages]] · Agent Mode
- [[Changes/ElevenLabs/2026-04-27-elevenagents|ElevenAgents]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-27-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-27-javascript-sdk|JavaScript SDK]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-26 · OpenCode · [[Changes/OpenCode/2026-04-26-core-sent-an-opencode-version-user-agent-header-with-http-requests|Core Sent an opencode/version User-Agent header with HTTP requests]]
- Later: 2026-04-27 · OpenCode · [[Changes/OpenCode/2026-04-27-core-added-a-configurable-default-shell-for-terminals-and-agent-shell-commands-w|Core Added a configurable default shell for terminals and agent shell commands…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-04-27-e7cc6e&body=Card%3A%20Changes%2FElevenLabs%2F2026-04-27-elevenagents-e7cc6e.md%0ACard%20ID%3A%20elevenlabs-2026-04-27-e7cc6e%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F4%2F27%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->