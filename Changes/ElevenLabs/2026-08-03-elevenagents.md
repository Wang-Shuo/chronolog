---
card_id: elevenlabs-2026-08-03-0175de
date: '2026-08-03'
description: 'ElevenLabs · 2026-08-03 · Agent Mode: **Test-specific tool mocks**:
  Agent simulations and unit tests can now define `tool_mock_overrides`, keyed by
  tool ID, to…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1124
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 8fb6c39fe008169d98ceb57bd8a8ac227aa4e9e4b936b8a95e103fd4d71e9ca9
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-08-03-0175de
  comparison: ''
  confidence: low
  date: '2026-08-03'
  description: 'ElevenLabs — ElevenLabs updates — 2026-08-03: **Test-specific tool
    mocks**: Agent simulations and unit tests can now define `tool_mock_overrides`,
    keyed by tool ID, to replace shared mocks for one test. `ToolResponseMockConfig`
    also adds optional `is_error` (boolean, default `false`) so a mock can exercise
    tool-failure paths.'
  evidence:
  - quote: '**Test-specific tool mocks**: Agent simulations and unit tests can now
      define `tool_mock_overrides`, keyed by tool ID, to replace shared mocks for
      one test. `ToolResponseMockConfig` also adds optional `is_error` (boolean, default
      `false`) so a mock can exercise tool-failure paths.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/3
  - quote: '**Translated workflow messages**: Literal Say node messages add `text_translations`,
      a map of language keys to `TranslatedString` objects. The field is optional
      on input and required on output, so strict response validators must accept it.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/3
  - quote: '**Conversation version filters**: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
      and [Text search conversation messages](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search)
      add the optional `version_id` query parameter (string) to filter results by
      agent version.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/3
  - quote: '**Knowledge base system tool**: Agent configuration adds a `knowledge_base`
      system tool with configurable `enabled_strategies` (`SearchStrategy[]`). Agent
      knowledge base RAG queries add optional `use_agent_defaults` (boolean, default
      `true`); set it to `false` to use neutral retrieval settings while retaining
      the agent''s embedding model.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/3
  - quote: '**Agent voice activity detection**: Agent create, update, response and
      workflow-override schemas add `vad` configuration. `VADConfig` currently supports
      `background_voice_detection` (boolean, default `false`).'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/3
  - quote: '**WebSocket custom LLMs**: `CustomLLMAPIType` adds `websocket`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/3
  - quote: '**File memory controls**: Widget file-input configuration adds `max_files_in_memory`
      (integer, 1–30, default `10`). Files beyond the limit are summarized and released
      from memory; `max_files_per_conversation` must be `-1` or at least the memory
      limit.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/3
  - quote: '**DTMF input redaction**: `DTMFInputConfig` adds optional `redact_input`
      (boolean, default `false`) to replace caller keypad digits in transcripts, conversation
      logs and analysis. Digits repeated by the agent or passed to tools remain unchanged.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/3
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-08-03-2026-08-03-8b25a66a
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-30-2-agent-mode-changes-in-v1-0-76|2 Agent
  Mode changes in v1.0.76]]'
- '[[Changes/OpenHands/2026-07-30-docs-refresh-agents-md-guidance-by-all-hands-bot-in-https-github-com-openhands-o|docs:
  refresh AGENTS.md guidance]]'
- '[[Changes/Replit/2026-07-31-agent|Agent]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-08-03-2026-08-03-8b25a66a|elevenlabs-2026-08-03-2026-08-03-8b25a66a]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-08-03 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/8/3) · from [[Releases/ElevenLabs/elevenlabs-2026-08-03-2026-08-03-8b25a66a|ElevenLabs updates — 2026-08-03]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Test-specific tool mocks**: Agent simulations and unit tests can now define `tool_mock_overrides`, keyed by tool ID, to replace shared mocks for one test. `ToolResponseMockConfig` also adds optional `is_error` (boolean, default `false`) so a mock can exercise tool-failure paths.
>
> **Translated workflow messages**: Literal Say node messages add `text_translations`, a map of language keys to `TranslatedString` objects. The field is optional on input and required on output, so strict response validators must accept it.
>
> **Conversation version filters**: [List conversations](https://elevenlabs.io/docs/api-reference/conversations/list) and [Text search conversation messages](https://elevenlabs.io/docs/api-reference/conversations/messages/text-search) add the optional `version_id` query parameter (string) to filter results by agent version.
>
> **Knowledge base system tool**: Agent configuration adds a `knowledge_base` system tool with configurable `enabled_strategies` (`SearchStrategy[]`). Agent knowledge base RAG queries add optional `use_agent_defaults` (boolean, default `true`); set it to `false` to use neutral retrieval settings while retaining the agent's embedding model.
>
> **Agent voice activity detection**: Agent create, update, response and workflow-override schemas add `vad` configuration. `VADConfig` currently supports `background_voice_detection` (boolean, default `false`).
>
> **WebSocket custom LLMs**: `CustomLLMAPIType` adds `websocket`.
>
> **File memory controls**: Widget file-input configuration adds `max_files_in_memory` (integer, 1–30, default `10`). Files beyond the limit are summarized and released from memory; `max_files_per_conversation` must be `-1` or at least the memory limit.
>
> **DTMF input redaction**: `DTMFInputConfig` adds optional `redact_input` (boolean, default `false`) to replace caller keypad digits in transcripts, conversation logs and analysis. Digits repeated by the agent or passed to tools remain unchanged.
>
> Source: https://elevenlabs.io/docs/changelog/2026/8/3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-08-03-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-08-03-mcp-server|MCP Server]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-08-03-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-08-03-voices-73a8c6|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-08-03-voices-78649b|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-08-03-text-to-speech|Text to Speech]] · Voice and Audio
- [[Changes/ElevenLabs/2026-08-03-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-08-03-packages|Packages]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-07-31 · Replit · [[Changes/Replit/2026-07-31-agent|Agent]]
- Later: 2026-08-03 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-08-03-a-run-whose-prompt-is-piped-over-stdin-now-treats-its-sessionend-hook-the-same-w|A run whose prompt is piped over stdin now treats its sessionEnd hook the same way…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-08-03-0175de&body=Card%3A%20Changes%2FElevenLabs%2F2026-08-03-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-08-03-0175de%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F8%2F3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->