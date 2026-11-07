---
card_id: elevenlabs-2026-05-18-ddcb34
date: '2026-05-18'
description: 'ElevenLabs · 2026-05-18 · Agent Mode: **Agent version metadata**: Added
  an API endpoint to retrieve metadata for a specific agent version. The response…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1047
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 135a37df9a92aae8d8180326d5874549762da27f17388f26086812da3191b673
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-05-18-ddcb34
  comparison: ''
  confidence: low
  date: '2026-05-18'
  description: 'ElevenLabs — ElevenLabs updates — 2026-05-18: **Agent version metadata**:
    Added an API endpoint to retrieve metadata for a specific agent version. The response
    includes the version ID, agent ID, branch ID, description, sequence number, commit
    timestamp, parents and access information.'
  evidence:
  - quote: '**Agent version metadata**: Added an API endpoint to retrieve metadata
      for a specific agent version. The response includes the version ID, agent ID,
      branch ID, description, sequence number, commit timestamp, parents and access
      information.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/18
  - quote: '**Conversation filtering**: Added a `text_only` filter to conversation
      list and message text search endpoints so developers can narrow results to text-only
      conversations.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/18
  - quote: '**Procedure loading**: Added `load_procedure` as a system tool configuration
      with `ProcedureAtVersion`, and added `skills` to `ProcedureCompilerMode`. `ProcedureSettings.compiler_mode`
      now defaults to `skills`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/18
  - quote: '**Agent configuration updates**: Added `gemini-3.1-flash-lite` and `qwen35-397b-a17b`
      as LLM options, added `genesys_bot_connector` as a conversation initiation source,
      added `auto_resolve_after_inactive_minutes` to alerting settings, and added
      `attributes_to_headers` to SIP trunk configuration.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/18
  - quote: '**Custom LLM temperature**: Agent prompt temperature can now be set to
      `null` to omit the temperature field from downstream LLM requests.'
    source_release: https://elevenlabs.io/docs/changelog/2026/5/18
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-05-18-2026-05-18-640aaf83
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-18-9-agent-mode-changes-in-rust-v0-131-0|9 Agent Mode
  changes in rust-v0.131.0]]'
- '[[Changes/Cursor/2026-05-18-composer-2-5-is-now-available-in-cursor|Composer 2.5
  is now available in Cursor]]'
- '[[Changes/ElevenLabs/2026-05-18-elevenagents|ElevenAgents]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-05-18-2026-05-18-640aaf83|elevenlabs-2026-05-18-2026-05-18-640aaf83]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-05-18 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/5/18) · from [[Releases/ElevenLabs/elevenlabs-2026-05-18-2026-05-18-640aaf83|ElevenLabs updates — 2026-05-18]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Agent version metadata**: Added an API endpoint to retrieve metadata for a specific agent version. The response includes the version ID, agent ID, branch ID, description, sequence number, commit timestamp, parents and access information.
>
> **Conversation filtering**: Added a `text_only` filter to conversation list and message text search endpoints so developers can narrow results to text-only conversations.
>
> **Procedure loading**: Added `load_procedure` as a system tool configuration with `ProcedureAtVersion`, and added `skills` to `ProcedureCompilerMode`. `ProcedureSettings.compiler_mode` now defaults to `skills`.
>
> **Agent configuration updates**: Added `gemini-3.1-flash-lite` and `qwen35-397b-a17b` as LLM options, added `genesys_bot_connector` as a conversation initiation source, added `auto_resolve_after_inactive_minutes` to alerting settings, and added `attributes_to_headers` to SIP trunk configuration.
>
> **Custom LLM temperature**: Agent prompt temperature can now be set to `null` to omit the temperature field from downstream LLM requests.
>
> Source: https://elevenlabs.io/docs/changelog/2026/5/18
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-05-18-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-05-18-ios-sdk|iOS SDK]] · Mobile and Desktop
- [[Changes/ElevenLabs/2026-05-18-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-05-18-voice-isolator|Voice Isolator]] · Voice and Audio
- [[Changes/ElevenLabs/2026-05-18-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-05-18-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-05-18-voice-isolator-f9327f|Voice Isolator]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-05-18 · Cursor · [[Changes/Cursor/2026-05-18-composer-2-5-is-now-available-in-cursor|Composer 2.5 is now available in Cursor]]
- Later: 2026-05-18 · Lovable · [[Changes/Lovable/2026-05-18-build-and-plan-mode-switch|Build and Plan mode switch]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-05-18-ddcb34&body=Card%3A%20Changes%2FElevenLabs%2F2026-05-18-elevenagents-ddcb34.md%0ACard%20ID%3A%20elevenlabs-2026-05-18-ddcb34%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F5%2F18%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->