---
card_id: elevenlabs-2026-02-09-36003d
date: '2026-02-09'
description: 'ElevenLabs · 2026-02-09 · Agent Mode: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
  [Update…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 949
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 32f61abd6f5a5faa656b46fdbc0faee8bd6ae6cafda3c60aa312a7132b1db5f5
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-02-09-36003d
  comparison: ''
  confidence: low
  date: '2026-02-09'
  description: 'ElevenLabs — ElevenLabs updates — 2026-02-09: [Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
    [Update agent](https://elevenlabs.io/docs/api-reference/agents/update), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get)'
  evidence:
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Update agent](https://elevenlabs.io/docs/api-reference/agents/update), [Get
      agent](https://elevenlabs.io/docs/api-reference/agents/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: Added `custom` field to `GuardrailsV1` schema for custom guardrails configuration
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: Added `alignment` field to `GuardrailsV1` schema for alignment guardrails
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: Added `suggested_audio_tags` field to TTS conversational config (array
      of `SuggestedAudioTag`, max 20 items)
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: Added `eleven_v3_conversational` to `TTSConversationalModel` enum
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: '[Create tool](https://elevenlabs.io/docs/api-reference/tools/create),
      [Update tool](https://elevenlabs.io/docs/api-reference/tools/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: 'Added `tool_error_handling_mode` field to `ApiIntegrationWebhookToolConfig`
      (enum: `auto`, `summarized`, `passthrough`, `hide`, default `auto`)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  - quote: Added `sanitize` field to `DynamicVariableAssignment` (boolean, default
      `false`)
    source_release: https://elevenlabs.io/docs/changelog/2026/2/9
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2026-02-09-2026-02-09-4b81b7a2
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/Lovable/2026-02-05-new-agent-and-chat-ui|New agent and chat UI]]'
- '[[Changes/Claude Code/2026-02-06-2-agent-mode-changes-in-v2-1-33|2 Agent Mode changes
  in v2.1.33]]'
- '[[Changes/Replit/2026-02-06-agent-inbox|Agent Inbox]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-02-09-2026-02-09-4b81b7a2|elevenlabs-2026-02-09-2026-02-09-4b81b7a2]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2026-02-09 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/2/9) · from [[Releases/ElevenLabs/elevenlabs-2026-02-09-2026-02-09-4b81b7a2|ElevenLabs updates — 2026-02-09]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update), [Get agent](https://elevenlabs.io/docs/api-reference/agents/get)
>
> Added `custom` field to `GuardrailsV1` schema for custom guardrails configuration
>
> Added `alignment` field to `GuardrailsV1` schema for alignment guardrails
>
> Added `suggested_audio_tags` field to TTS conversational config (array of `SuggestedAudioTag`, max 20 items)
>
> Added `eleven_v3_conversational` to `TTSConversationalModel` enum
>
> [Create tool](https://elevenlabs.io/docs/api-reference/tools/create), [Update tool](https://elevenlabs.io/docs/api-reference/tools/update)
>
> Added `tool_error_handling_mode` field to `ApiIntegrationWebhookToolConfig` (enum: `auto`, `summarized`, `passthrough`, `hide`, default `auto`)
>
> Added `sanitize` field to `DynamicVariableAssignment` (boolean, default `false`)
>
> Source: https://elevenlabs.io/docs/changelog/2026/2/9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-02-09-user-interface|User Interface]] · Interface Experience
- [[Changes/ElevenLabs/2026-02-09-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-02-09-new-endpoints|New Endpoints]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-02-09-agents-platform-7f0c0d|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2026-02-09-javascript-sdk|JavaScript SDK]] · Model Support
- [[Changes/ElevenLabs/2026-02-09-python-sdk|Python SDK]] · Model Support
- [[Changes/ElevenLabs/2026-02-09-text-to-speech|Text to Speech]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-02-06 · Replit · [[Changes/Replit/2026-02-06-agent-inbox|Agent Inbox]]
- Later: 2026-02-10 · Gemini CLI · [[Changes/Gemini CLI/2026-02-10-4-agent-mode-changes-in-v0-28-0|4 Agent Mode changes in v0.28.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-02-09-36003d&body=Card%3A%20Changes%2FElevenLabs%2F2026-02-09-agents-platform.md%0ACard%20ID%3A%20elevenlabs-2026-02-09-36003d%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F2%2F9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->