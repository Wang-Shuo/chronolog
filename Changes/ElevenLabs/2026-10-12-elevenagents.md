---
card_id: elevenlabs-2026-10-12-23bdfb
date: '2026-10-12'
description: 'ElevenLabs · 2026-10-12 · Agent Mode: **Merge and search triage tickets**:
  [Merge tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/merge) folds…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1194
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 55449a3a980fd59f0d407b0e9294c6c14a0d361cbdd294806274acd4ca228cd3
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-10-12-23bdfb
  comparison: ''
  confidence: low
  date: '2026-10-12'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-12: **Merge and search triage
    tickets**: [Merge tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/merge)
    folds up to 50 open tickets from the same agent into one target ticket. Merged
    tickets keep the status `merged` and reference the target through `merged_into_ticket_id`.
    [List tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list) and
    [List workspace tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list-for-workspace)
    add a case-insensitive `search` parameter that matches ticket titles, descriptions,
    comments and turn comments, and each result includes a `search_match` excerpt
    showing where the query matched.'
  evidence:
  - quote: '**Merge and search triage tickets**: [Merge tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/merge)
      folds up to 50 open tickets from the same agent into one target ticket. Merged
      tickets keep the status `merged` and reference the target through `merged_into_ticket_id`.
      [List tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list)
      and [List workspace tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list-for-workspace)
      add a case-insensitive `search` parameter that matches ticket titles, descriptions,
      comments and turn comments, and each result includes a `search_match` excerpt
      showing where the query matched.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: '**Workflow End node outcomes**: Workflow End nodes accept an `outcome`
      of `success` (default) or `failure`, so a workflow can record whether a conversation
      ended successfully. The conversation error type adds `workflow_end_failure`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: '**Call queueing enabled for new agents**: New agents are created with
      [call queueing](https://elevenlabs.io/docs/eleven-agents/guides/call-queueing)
      enabled unless `platform_settings.queueing_config.enabled` is set explicitly.
      Existing agents keep their current setting.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: '**Post-call audio webhook retries**: When **Enable retries** is on, `post_call_audio`
      [webhooks](https://elevenlabs.io/docs/eleven-agents/workflows/post-call-webhooks)
      are retried on the same schedule as transcription webhooks. Audio payloads over
      50 MiB are not retried, and queued audio retries are capped at 400 MiB per webhook.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: '**Strict tool overrides**: The conversation override `tool_ids_strict`
      makes an overridden `tool_ids` list the complete set of tools available in the
      conversation, including tools on workflow nodes. It is ignored when set on the
      agent itself.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  - quote: '**Widget end confirmation**: The widget can ask users to confirm before
      ending a chat or call. Enable it with `end_confirmation_enabled` in the widget
      configuration or the `end-confirmation` attribute.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/12
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-10-12-2026-10-12-16e5a6a0
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-08-14-agent-mode-changes-in-rust-v0-162-0|14 Agent
  Mode changes in rust-v0.162.0]]'
- '[[Changes/Claude Code/2026-10-09-3-agent-mode-changes-in-v2-1-296|3 Agent Mode
  changes in v2.1.296]]'
- '[[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes
  in v0.12.0]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-12-2026-10-12-16e5a6a0|elevenlabs-2026-10-12-2026-10-12-16e5a6a0]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-10-12 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/12) · from [[Releases/ElevenLabs/elevenlabs-2026-10-12-2026-10-12-16e5a6a0|ElevenLabs updates — 2026-10-12]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Merge and search triage tickets**: [Merge tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/merge) folds up to 50 open tickets from the same agent into one target ticket. Merged tickets keep the status `merged` and reference the target through `merged_into_ticket_id`. [List tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list) and [List workspace tickets](https://elevenlabs.io/docs/api-reference/triage-tickets/list-for-workspace) add a case-insensitive `search` parameter that matches ticket titles, descriptions, comments and turn comments, and each result includes a `search_match` excerpt showing where the query matched.
>
> **Workflow End node outcomes**: Workflow End nodes accept an `outcome` of `success` (default) or `failure`, so a workflow can record whether a conversation ended successfully. The conversation error type adds `workflow_end_failure`.
>
> **Call queueing enabled for new agents**: New agents are created with [call queueing](https://elevenlabs.io/docs/eleven-agents/guides/call-queueing) enabled unless `platform_settings.queueing_config.enabled` is set explicitly. Existing agents keep their current setting.
>
> **Post-call audio webhook retries**: When **Enable retries** is on, `post_call_audio` [webhooks](https://elevenlabs.io/docs/eleven-agents/workflows/post-call-webhooks) are retried on the same schedule as transcription webhooks. Audio payloads over 50 MiB are not retried, and queued audio retries are capped at 400 MiB per webhook.
>
> **Strict tool overrides**: The conversation override `tool_ids_strict` makes an overridden `tool_ids` list the complete set of tools available in the conversation, including tools on workflow nodes. It is ignored when set on the agent itself.
>
> **Widget end confirmation**: The widget can ask users to confirm before ending a chat or call. Enable it with `end_confirmation_enabled` in the widget configuration or the `end-confirmation` attribute.
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/12
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-12-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-text-to-speech|Text to Speech]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-12-elevenagents-545be2|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-12-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-12-text-to-dialogue|Text to Dialogue]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-elevenlabs-cli|ElevenLabs CLI]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-audio-effects|Audio effects]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-voices-e71bd5|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-12-speech-to-text-f7d11e|Speech to Text]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-10 · Open WebUI · [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]]
- Later: 2026-10-12 · OpenHands · [[Changes/OpenHands/2026-10-12-4-agent-mode-changes-in-v1-27-0|4 Agent Mode changes in v1.27.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-12-23bdfb&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-12-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-10-12-23bdfb%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F12%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->