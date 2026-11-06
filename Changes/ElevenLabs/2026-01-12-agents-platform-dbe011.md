---
card_id: elevenlabs-2026-01-12-dbe011
date: '2026-01-12'
description: 'ElevenLabs · 2026-01-12 · Agent Mode: **Timezone support for batch call
  scheduling**: You can now select a timezone when scheduling batch calls. The scheduled…'
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
impact: significant
kind: launch
machine_hash: cd404461f35f17edbe54f7aa53835e1fc38c0b492361e1ab279b8ef802d4f61f
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-01-12-dbe011
  comparison: ''
  confidence: low
  date: '2026-01-12'
  description: 'ElevenLabs — ElevenLabs updates — 2026-01-12: **Timezone support for
    batch call scheduling**: You can now select a timezone when scheduling batch calls.
    The scheduled time is converted to UTC based on your chosen timezone. Your browser''s
    timezone is automatically selected by default, and validation prevents scheduling
    calls for times that have already passed in the selected timezone. This makes
    it easier to schedule outbound calls for the right time in your recipients'' time
    zones.'
  evidence:
  - quote: '**Timezone support for batch call scheduling**: You can now select a timezone
      when scheduling batch calls. The scheduled time is converted to UTC based on
      your chosen timezone. Your browser''s timezone is automatically selected by
      default, and validation prevents scheduling calls for times that have already
      passed in the selected timezone. This makes it easier to schedule outbound calls
      for the right time in your recipients'' time zones.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: '**Knowledge Base source file URL**: Added a new endpoint to retrieve the
      original source file URL for knowledge base documents, enabling direct access
      to uploaded files.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: '**LLM fallback cascade timeout**: Added `cascade_timeout_seconds` configuration
      option for agent backup LLM configs, allowing control over how long to wait
      before cascading to the next LLM. Default is 8 seconds with an allowed range
      of 2-15 seconds.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: '**Soft timeout LLM-generated messages**: Added `use_llm_generated_message`
      option to soft timeout configuration. When enabled, the agent will generate
      a contextual message using the LLM instead of using a predefined message when
      soft timeout triggers.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: '**Knowledge Base folder navigation**: Knowledge Base document responses
      now include `folder_path` field showing the path segments from root to parent
      folder, making it easier to understand document hierarchy.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  - quote: '**Conversation filtering by initiation source**: The Get Conversations
      endpoint now supports filtering by `conversation_initiation_source` query parameter.'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/12
  extractor_version: fallback-v5
  impact: significant
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
- '[[Changes/Ollama/2026-01-10-ollama-run-experimental-cli-will-now-open-a-new-ollama-cli-that-includes-an-agen|ollama
  run --experimental CLI will now open a new Ollama CLI that includes…]]'
- '[[Changes/Claude Code/2026-01-11-added-claude-code-disable-background-tasks-environment-variable-to-disable-all-b|Added
  CLAUDE_CODE_DISABLE_BACKGROUND_TASKS environment variable to disable all…]]'
- '[[Changes/ElevenLabs/2026-01-12-agents-platform|Agents Platform]]'
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
> **Timezone support for batch call scheduling**: You can now select a timezone when scheduling batch calls. The scheduled time is converted to UTC based on your chosen timezone. Your browser's timezone is automatically selected by default, and validation prevents scheduling calls for times that have already passed in the selected timezone. This makes it easier to schedule outbound calls for the right time in your recipients' time zones.
>
> **Knowledge Base source file URL**: Added a new endpoint to retrieve the original source file URL for knowledge base documents, enabling direct access to uploaded files.
>
> **LLM fallback cascade timeout**: Added `cascade_timeout_seconds` configuration option for agent backup LLM configs, allowing control over how long to wait before cascading to the next LLM. Default is 8 seconds with an allowed range of 2-15 seconds.
>
> **Soft timeout LLM-generated messages**: Added `use_llm_generated_message` option to soft timeout configuration. When enabled, the agent will generate a contextual message using the LLM instead of using a predefined message when soft timeout triggers.
>
> **Knowledge Base folder navigation**: Knowledge Base document responses now include `folder_path` field showing the path segments from root to parent folder, making it easier to understand document hierarchy.
>
> **Conversation filtering by initiation source**: The Get Conversations endpoint now supports filtering by `conversation_initiation_source` query parameter.
>
> Source: https://elevenlabs.io/docs/changelog/2026/1/12
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-01-12-scribe-v2|Scribe v2]] · Model Support
- [[Changes/ElevenLabs/2026-01-12-knowledge-base|Knowledge Base]] · Files and Data
- [[Changes/ElevenLabs/2026-01-12-agents-platform|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-12-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-12-speech-to-text-995b34|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-12-mcp-server|MCP Server]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-01-12-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-01-12-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-12-javascript-sdk|JavaScript SDK]] · Voice and Audio
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
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-01-12-dbe011&body=Card%3A%20Changes%2FElevenLabs%2F2026-01-12-agents-platform-dbe011.md%0ACard%20ID%3A%20elevenlabs-2026-01-12-dbe011%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F1%2F12%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->