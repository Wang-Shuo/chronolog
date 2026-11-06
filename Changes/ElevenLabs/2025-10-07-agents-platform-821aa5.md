---
card_id: elevenlabs-2025-10-07-821aa5
date: '2025-10-07'
description: 'ElevenLabs · 2025-10-07 · Agent Mode: **Gemini 2.5 Flash Preview models**:
  Added support for `gemini-2.5-flash-preview-09-2025` and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 824
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: fdd04c1551fc6ed1d051967a5a40465c9d37a1642aae8ee580b24821585fd2a8
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2025-10-07-821aa5
  comparison: ''
  confidence: low
  date: '2025-10-07'
  description: 'ElevenLabs — ElevenLabs updates — 2025-10-07: **Gemini 2.5 Flash Preview
    models**: Added support for `gemini-2.5-flash-preview-09-2025` and `gemini-2.5-flash-lite-preview-09-2025`
    LLM models, providing access to the latest September 2025 preview versions of
    Google''s Gemini 2.5 Flash models.'
  evidence:
  - quote: '**Gemini 2.5 Flash Preview models**: Added support for `gemini-2.5-flash-preview-09-2025`
      and `gemini-2.5-flash-lite-preview-09-2025` LLM models, providing access to
      the latest September 2025 preview versions of Google''s Gemini 2.5 Flash models.'
    source_release: https://elevenlabs.io/docs/changelog/2025/10/7
  - quote: '**Claude Sonnet 4.5**: Added support for `claude-sonnet-4-5` and `claude-sonnet-4-5@20250929`
      models, enabling access to the latest Claude Sonnet 4.5 model released on September
      29, 2025.'
    source_release: https://elevenlabs.io/docs/changelog/2025/10/7
  - quote: '**Test invocations listing**: Added new `GET /v1/convai/test-invocations`
      endpoint to list all test invocations with pagination support. Includes `agent_id`
      filter, `page_size` parameter (default 30, max 100), and `cursor` for pagination.
      Response includes test run counts, pass/fail statistics, and titles.'
    source_release: https://elevenlabs.io/docs/changelog/2025/10/7
  - quote: '**Agent archiving**: Added `archived` field (boolean, default false) to
      agent platform settings, allowing agents to be archived without deletion while
      keeping them out of active agent lists.'
    source_release: https://elevenlabs.io/docs/changelog/2025/10/7
  - quote: '**MCP Server interruption control**: Added `disable_interruptions` field
      (boolean, default false) to MCP server configuration, preventing user interruptions
      during tool execution for more reliable tool completion.'
    source_release: https://elevenlabs.io/docs/changelog/2025/10/7
  - quote: '**Streaming agent responses**: Added `agent_chat_response_part` WebSocket
      event type for receiving partial agent chat responses in real-time during streaming
      conversations.'
    source_release: https://elevenlabs.io/docs/changelog/2025/10/7
  - quote: '**Workflow edge ordering**: Added `edge_order` field (array of strings)
      to all workflow node types, enabling explicit control over edge evaluation order
      for deterministic workflow execution.'
    source_release: https://elevenlabs.io/docs/changelog/2025/10/7
  - quote: '**Test suite agent tracking**: Added `agent_id` field (string, nullable)
      to test invocation responses for associating test runs with specific agents.'
    source_release: https://elevenlabs.io/docs/changelog/2025/10/7
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2025-10-07-2025-10-07-a74f7acb
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2025-10-01-improved-the-experience-of-writing-prompts-while-the-agent-is-running-up-down-ar|Improved
  the experience of writing prompts while the agent is running -- up/down…]]'
- '[[Changes/Codex CLI/2025-10-03-5-agent-mode-changes-in-rust-v0-44-0|5 Agent Mode
  changes in rust-v0.44.0]]'
- '[[Changes/ElevenLabs/2025-10-07-agents-platform|Agents Platform]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2025-10-07-2025-10-07-a74f7acb|elevenlabs-2025-10-07-2025-10-07-a74f7acb]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2025-10-07 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2025/10/7) · from [[Releases/ElevenLabs/elevenlabs-2025-10-07-2025-10-07-a74f7acb|ElevenLabs updates — 2025-10-07]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Gemini 2.5 Flash Preview models**: Added support for `gemini-2.5-flash-preview-09-2025` and `gemini-2.5-flash-lite-preview-09-2025` LLM models, providing access to the latest September 2025 preview versions of Google's Gemini 2.5 Flash models.
>
> **Claude Sonnet 4.5**: Added support for `claude-sonnet-4-5` and `claude-sonnet-4-5@20250929` models, enabling access to the latest Claude Sonnet 4.5 model released on September 29, 2025.
>
> **Test invocations listing**: Added new `GET /v1/convai/test-invocations` endpoint to list all test invocations with pagination support. Includes `agent_id` filter, `page_size` parameter (default 30, max 100), and `cursor` for pagination. Response includes test run counts, pass/fail statistics, and titles.
>
> **Agent archiving**: Added `archived` field (boolean, default false) to agent platform settings, allowing agents to be archived without deletion while keeping them out of active agent lists.
>
> **MCP Server interruption control**: Added `disable_interruptions` field (boolean, default false) to MCP server configuration, preventing user interruptions during tool execution for more reliable tool completion.
>
> **Streaming agent responses**: Added `agent_chat_response_part` WebSocket event type for receiving partial agent chat responses in real-time during streaming conversations.
>
> **Workflow edge ordering**: Added `edge_order` field (array of strings) to all workflow node types, enabling explicit control over edge evaluation order for deterministic workflow execution.
>
> **Test suite agent tracking**: Added `agent_id` field (string, nullable) to test invocation responses for associating test runs with specific agents.
>
> Source: https://elevenlabs.io/docs/changelog/2025/10/7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2025-10-07-agents-platform|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2025-10-07-javascript-sdk|JavaScript SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2025-10-07-voice-management|Voice Management]] · Voice and Audio
- [[Changes/ElevenLabs/2025-10-07-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2025-10-07-new-llm-models|New LLM Models]] · Model Support
- [[Changes/ElevenLabs/2025-10-07-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2025-10-07-voice-management-a4407c|Voice Management]] · Voice and Audio
- [[Changes/ElevenLabs/2025-10-07-agents-platform-f78196|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2025-10-07-websocket-events|WebSocket Events]] · Agent Mode
- [[Changes/ElevenLabs/2025-10-07-mcp-server|MCP Server]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2025-10-03 · Codex CLI · [[Changes/Codex CLI/2025-10-03-5-agent-mode-changes-in-rust-v0-44-0|5 Agent Mode changes in rust-v0.44.0]]
- Later: 2025-10-07 · Gemini CLI · [[Changes/Gemini CLI/2025-10-07-2-agent-mode-changes-in-v0-8-0|2 Agent Mode changes in v0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2025-10-07-821aa5&body=Card%3A%20Changes%2FElevenLabs%2F2025-10-07-agents-platform-821aa5.md%0ACard%20ID%3A%20elevenlabs-2025-10-07-821aa5%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2025%2F10%2F7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->