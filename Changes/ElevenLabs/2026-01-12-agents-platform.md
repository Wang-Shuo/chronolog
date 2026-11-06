---
card_id: elevenlabs-2026-01-12-40435a
date: '2026-01-12'
description: 'ElevenLabs · 2026-01-12 · Agent Mode: [Submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create)'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 921
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: a84ddd08069f7bbed739936091e79fee7886c8abca392629242150915130ca80
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-01-12-40435a
  comparison: ''
  date: '2026-01-12'
  description: 'ElevenLabs — ElevenLabs updates — 2026-01-12: [Submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create)'
  evidence:
  - quote: '[Submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: Added `timezone` (string, optional) to request body for timezone-aware
      scheduling
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: Added `scheduled_time` (string, optional) as ISO string alternative to
      `scheduled_time_unix`
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: '[Get batch call](https://elevenlabs.io/docs/api-reference/batch-calling/get),
      [Cancel batch call](https://elevenlabs.io/docs/api-reference/batch-calling/cancel),
      [Retry batch call](https://elevenlabs.io/docs/api-reference/batch-calling/retry)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: Added `timezone` (string, required) to batch call response models
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Update agent](https://elevenlabs.io/docs/api-reference/agents/update), [Get
      agent](https://elevenlabs.io/docs/api-reference/agents/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: Added `cascade_timeout_seconds` (integer, default 8, range 2-15, nullable)
      to backup LLM configuration
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: Added `use_llm_generated_message` (boolean, default `false`) to soft timeout
      configuration
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: '[Get conversations](https://elevenlabs.io/docs/api-reference/conversations/get-conversations)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: Added `conversation_initiation_source` (string, optional) query parameter
      for filtering conversations by initiation source
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: '[Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation),
      [Simulate conversation stream](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation-stream)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: Updated `entity_detection` to accept `'all'`, strings, or string arrays
      instead of boolean
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2026-01-12-2026-01-12-102f5bca
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/Replit/2026-01-09-ai-command-in-shell|AI command in Shell]]'
- '[[Changes/Ollama/2026-01-10-ollama-run-experimental-cli-will-now-open-a-new-ollama-cli-that-includes-an-agen|ollama
  run --experimental CLI will now open a new Ollama CLI that includes…]]'
- '[[Changes/Claude Code/2026-01-11-added-claude-code-disable-background-tasks-environment-variable-to-disable-all-b|Added
  CLAUDE_CODE_DISABLE_BACKGROUND_TASKS environment variable to disable all…]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-01-12-2026-01-12-102f5bca|elevenlabs-2026-01-12-2026-01-12-102f5bca]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2026-01-12 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/1/12) · from [[Releases/ElevenLabs/elevenlabs-2026-01-12-2026-01-12-102f5bca|ElevenLabs updates — 2026-01-12]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create)
>
> Added `timezone` (string, optional) to request body for timezone-aware scheduling
>
> Added `scheduled_time` (string, optional) as ISO string alternative to `scheduled_time_unix`
>
> [Get batch call](https://elevenlabs.io/docs/api-reference/batch-calling/get), [Cancel batch call](https://elevenlabs.io/docs/api-reference/batch-calling/cancel), [Retry batch call](https://elevenlabs.io/docs/api-reference/batch-calling/retry)
>
> Added `timezone` (string, required) to batch call response models
>
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get)
>
> Added `cascade_timeout_seconds` (integer, default 8, range 2-15, nullable) to backup LLM configuration
>
> Added `use_llm_generated_message` (boolean, default `false`) to soft timeout configuration
>
> [Get conversations](https://elevenlabs.io/docs/api-reference/conversations/get-conversations)
>
> Added `conversation_initiation_source` (string, optional) query parameter for filtering conversations by initiation source
>
> [Simulate conversation](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation), [Simulate conversation stream](https://elevenlabs.io/docs/api-reference/agents/simulate-conversation-stream)
>
> Updated `entity_detection` to accept `'all'`, strings, or string arrays instead of boolean
>
> Source: https://elevenlabs.io/docs/changelog/2026/1/12
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-01-12-scribe-v2|Scribe v2]] · Model Support
- [[Changes/ElevenLabs/2026-01-12-knowledge-base|Knowledge Base]] · Files and Data
- [[Changes/ElevenLabs/2026-01-12-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-12-speech-to-text-995b34|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-12-mcp-server|MCP Server]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-01-12-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-01-12-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-12-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-12-agents-platform-dbe011|Agents Platform]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-01-11 · Claude Code · [[Changes/Claude Code/2026-01-11-added-claude-code-disable-background-tasks-environment-variable-to-disable-all-b|Added CLAUDE_CODE_DISABLE_BACKGROUND_TASKS environment variable to disable all…]]
- Later: 2026-01-13 · Dify · [[Changes/Dify/2026-01-13-3-agent-mode-changes-in-1-11-3|3 Agent Mode changes in 1.11.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-01-12-40435a&body=Card%3A%20Changes%2FElevenLabs%2F2026-01-12-agents-platform.md%0ACard%20ID%3A%20elevenlabs-2026-01-12-40435a%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F1%2F12%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->