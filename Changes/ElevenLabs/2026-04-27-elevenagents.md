---
card_id: elevenlabs-2026-04-27-959c87
date: '2026-04-27'
description: 'ElevenLabs · 2026-04-27 · Voice and Audio: **`agent_response_complete`
  WebSocket event**: A new [`agent_response_complete` client…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1022
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: a99ce118a18f998eafed0c5e09af0ce3924f86ed4f220cd59a70f6aa7731228a
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-04-27-959c87
  comparison: ''
  confidence: low
  date: '2026-04-27'
  description: 'ElevenLabs — ElevenLabs updates — 2026-04-27: **`agent_response_complete`
    WebSocket event**: A new [`agent_response_complete` client event](https://elevenlabs.io/docs/eleven-agents/customization/events/client-events)
    fires exactly once when an agent''s response is fully delivered -- after all LLM
    generation, tool call chains, and audio playback complete. After this event, the
    agent will only produce further output if the user provides new input or a turn
    timeout triggers a new turn. The event lets clients reliably detect end of turn
    for batching messages, wake-word activation, or post-turn UI updates. Added a
    new `AGENT_RESPONSE_COMPLETE` value to the `ClientEvent` enum and a corresponding
    `AgentResponseCompleteClientEvent` response model.'
  evidence:
  - quote: '**`agent_response_complete` WebSocket event**: A new [`agent_response_complete`
      client event](https://elevenlabs.io/docs/eleven-agents/customization/events/client-events)
      fires exactly once when an agent''s response is fully delivered -- after all
      LLM generation, tool call chains, and audio playback complete. After this event,
      the agent will only produce further output if the user provides new input or
      a turn timeout triggers a new turn. The event lets clients reliably detect end
      of turn for batching messages, wake-word activation, or post-turn UI updates.
      Added a new `AGENT_RESPONSE_COMPLETE` value to the `ClientEvent` enum and a
      corresponding `AgentResponseCompleteClientEvent` response model.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '**Pre-tool speech mode**: Added a new `pre_tool_speech` field (`PreToolSpeechMode`
      enum, default `auto`) on MCP server configuration and per-tool overrides. Replaces
      the now-deprecated `force_pre_tool_speech` boolean. Values: `auto` decides whether
      the agent speaks before the tool call based on recent tool latency, `force`
      always asks the agent to speak, and `off` opts out entirely.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '**Tool dispatch respects execution mode**: Workflow tool dispatch nodes
      now correctly respect each nested tool''s `execution_mode`. If any tool in a
      dispatch node uses `POST_TOOL_SPEECH`, the workflow waits for the current turn''s
      audio to be fully exposed before executing the dispatch.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '**MCP response timeout**: Added a `response_timeout_secs` field (integer,
      default `30`, min `5`, max `120`) on MCP server configuration and per-tool overrides,
      controlling the maximum time to wait for each MCP tool call to complete.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '**Agent trust context**: Added a `trust_context` field on agent platform
      settings (`AgentTrustContext` enum: `unknown` | `low` | `high`, default `unknown`).
      `low` is for agents serving untrusted external participants, where outputs should
      be vetted and tool access scoped; `high` is for agents serving the owner where
      full tool access is appropriate; `unknown` covers agents created before this
      feature.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '**Source attribution toggle**: Added a `source_attribution` boolean (default
      `false`) on conversation config. When enabled and knowledge base content is
      present, the LLM is instructed to report which sources it used.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '**Test sharing mode filter**: The [list tests](https://elevenlabs.io/docs/api-reference/tests/list)
      endpoint now accepts a `sharing_mode` query parameter (`all` | `shared_with_me`,
      default `all`) to filter tests and folders to only those shared with the current
      user that they did not create.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '**Tool icons and execution metadata**: Added `icons` (array of `Icon`)
      and `execution` (`ToolExecution`) fields to the `Tool` schema. `Icon` includes
      `src`, `mimeType`, and `sizes` for UI display, and `ToolExecution.taskSupport`
      (`forbidden` | `optional` | `required`) declares how the tool participates in
      tasks.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '**Procedure compiler default**: The `ProcedureCompilerMode` default has
      changed from `deterministic` to `append`, and the `llm` value has been removed.
      Existing agents that explicitly set `deterministic` are unaffected.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '**RAG and knowledge base attribution metadata**: Added `used_static_kb_document_ids`
      (array of strings) on `ConversationHistoryTranscriptCommonModel` and `ConversationHistoryTranscriptResponseModel`,
      and `used_chunk_ids` on `RagRetrievalInfo`, surfacing exactly which knowledge
      base documents and RAG chunks contributed to each transcript turn.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  - quote: '**Dynamic variable refactor**: `dynamic_variables` and `dynamic_variable_placeholders`
      now reference unified `DynamicVariableValueType-Input` / `DynamicVariableValueType-Output`
      schemas (replacing the prior `DynamicVariableContainerValueType-*` schemas),
      with broader support for nested and list values. `DynamicVariableAssignment`
      gained a `preserve_native_type` field to keep typed values rather than coercing
      to strings.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/27
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-04-27-2026-04-27-7b6333fc
  source_type: elevenlabs_changelog
  theme: voice
  theme_matches:
  - matched_terms:
    - agent
    - agents
    score: 100
    theme: agent-mode
  - matched_terms:
    - llm
    - model
    score: 100
    theme: model-support
  - matched_terms:
    - audio
    score: 50
    theme: voice
  theme_resolution: manual-semantic-rule-v1
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-04-27-python-sdk|Python SDK]]'
- '[[Changes/ElevenLabs/2026-04-27-audio-isolation|Audio Isolation]]'
- '[[Changes/ElevenLabs/2026-04-27-new-endpoints|New Endpoints]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-04-27-2026-04-27-7b6333fc|elevenlabs-2026-04-27-2026-04-27-7b6333fc]]'
source_type: elevenlabs_changelog
theme: voice
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-04-27 · [[Themes/voice|Voice and Audio]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/4/27) · from [[Releases/ElevenLabs/elevenlabs-2026-04-27-2026-04-27-7b6333fc|ElevenLabs updates — 2026-04-27]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **`agent_response_complete` WebSocket event**: A new [`agent_response_complete` client event](https://elevenlabs.io/docs/eleven-agents/customization/events/client-events) fires exactly once when an agent's response is fully delivered -- after all LLM generation, tool call chains, and audio playback complete. After this event, the agent will only produce further output if the user provides new input or a turn timeout triggers a new turn. The event lets clients reliably detect end of turn for batching messages, wake-word activation, or post-turn UI updates. Added a new `AGENT_RESPONSE_COMPLETE` value to the `ClientEvent` enum and a corresponding `AgentResponseCompleteClientEvent` response model.
>
> **Pre-tool speech mode**: Added a new `pre_tool_speech` field (`PreToolSpeechMode` enum, default `auto`) on MCP server configuration and per-tool overrides. Replaces the now-deprecated `force_pre_tool_speech` boolean. Values: `auto` decides whether the agent speaks before the tool call based on recent tool latency, `force` always asks the agent to speak, and `off` opts out entirely.
>
> **Tool dispatch respects execution mode**: Workflow tool dispatch nodes now correctly respect each nested tool's `execution_mode`. If any tool in a dispatch node uses `POST_TOOL_SPEECH`, the workflow waits for the current turn's audio to be fully exposed before executing the dispatch.
>
> **MCP response timeout**: Added a `response_timeout_secs` field (integer, default `30`, min `5`, max `120`) on MCP server configuration and per-tool overrides, controlling the maximum time to wait for each MCP tool call to complete.
>
> **Agent trust context**: Added a `trust_context` field on agent platform settings (`AgentTrustContext` enum: `unknown` | `low` | `high`, default `unknown`). `low` is for agents serving untrusted external participants, where outputs should be vetted and tool access scoped; `high` is for agents serving the owner where full tool access is appropriate; `unknown` covers agents created before this feature.
>
> **Source attribution toggle**: Added a `source_attribution` boolean (default `false`) on conversation config. When enabled and knowledge base content is present, the LLM is instructed to report which sources it used.
>
> **Test sharing mode filter**: The [list tests](https://elevenlabs.io/docs/api-reference/tests/list) endpoint now accepts a `sharing_mode` query parameter (`all` | `shared_with_me`, default `all`) to filter tests and folders to only those shared with the current user that they did not create.
>
> **Tool icons and execution metadata**: Added `icons` (array of `Icon`) and `execution` (`ToolExecution`) fields to the `Tool` schema. `Icon` includes `src`, `mimeType`, and `sizes` for UI display, and `ToolExecution.taskSupport` (`forbidden` | `optional` | `required`) declares how the tool participates in tasks.
>
> **Procedure compiler default**: The `ProcedureCompilerMode` default has changed from `deterministic` to `append`, and the `llm` value has been removed. Existing agents that explicitly set `deterministic` are unaffected.
>
> **RAG and knowledge base attribution metadata**: Added `used_static_kb_document_ids` (array of strings) on `ConversationHistoryTranscriptCommonModel` and `ConversationHistoryTranscriptResponseModel`, and `used_chunk_ids` on `RagRetrievalInfo`, surfacing exactly which knowledge base documents and RAG chunks contributed to each transcript turn.
>
> **Dynamic variable refactor**: `dynamic_variables` and `dynamic_variable_placeholders` now reference unified `DynamicVariableValueType-Input` / `DynamicVariableValueType-Output` schemas (replacing the prior `DynamicVariableContainerValueType-*` schemas), with broader support for nested and list values. `DynamicVariableAssignment` gained a `preserve_native_type` field to keep typed values rather than coercing to strings.
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
- [[Changes/ElevenLabs/2026-04-27-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-27-elevenagents-e7cc6e|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-04-27-javascript-sdk|JavaScript SDK]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-04-21 · Open WebUI · [[Changes/Open WebUI/2026-04-21-4-voice-and-audio-changes-in-v0-9-0|4 Voice and Audio changes in v0.9.0]]
- Later: 2026-04-28 · Claude Code · [[Changes/Claude Code/2026-04-28-vscode-voice-dictation-now-respects-the-accessibility-voice-speechlanguage-setti|VSCode Voice dictation now respects the accessibility.voice.speechLanguage…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-04-27-959c87&body=Card%3A%20Changes%2FElevenLabs%2F2026-04-27-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-04-27-959c87%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F4%2F27%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->