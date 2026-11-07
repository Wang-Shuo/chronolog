---
card_id: elevenlabs-2026-02-02-f8a58b
date: '2026-02-02'
description: 'ElevenLabs · 2026-02-02 · Agent Mode: **Agent branch renaming**: You
  can now rename agent branches using the [Update…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 942
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: b6781229de0bf99a07215ad5ec9bae00ba28a16b94d2418ccef3e9a58f793b08
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-02-02-f8a58b
  comparison: ''
  confidence: low
  date: '2026-02-02'
  description: 'ElevenLabs — ElevenLabs updates — 2026-02-02: **Agent branch renaming**:
    You can now rename agent branches using the [Update branch](https://elevenlabs.io/docs/api-reference/agents/branches/update)
    endpoint. The new optional `name` field accepts 1-140 characters.'
  evidence:
  - quote: '**Agent branch renaming**: You can now rename agent branches using the
      [Update branch](https://elevenlabs.io/docs/api-reference/agents/branches/update)
      endpoint. The new optional `name` field accepts 1-140 characters.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: '**Alignment guardrails**: Added `AlignmentGuardrail` type to `GuardrailsV1`
      schema for enhanced conversation safety controls.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: '**Speculative turn configuration**: Added `speculative_turn` field to
      turn configuration for fine-tuning agent turn-taking behavior.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: '**Procedure references**: Agent patch requests now support `procedure_refs`
      for referencing reusable procedures.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: '**Webhook response filtering**: Added `response_filter_mode` and `response_filters`
      fields to webhook overrides, with new `ResponseFilterMode` enum for controlling
      which response data is passed through.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: '**Error details in tool events**: Added `raw_error_message` field to API
      integration webhook, system, and workflow tool event models for improved debugging.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: '**Flexible tool call matching**: Testing models now include `check_any_tool_matches`
      option to relax tool call matching requirements during agent testing.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: '**Secrets pagination**: [Get workspace secrets](https://elevenlabs.io/docs/api-reference/workspace/secrets/list)
      endpoint now supports pagination with `page_size` (max 100) and `cursor` query
      parameters, returning `next_cursor` and `has_more` in responses.'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2026-02-02-2026-02-02-2180766f
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-02-02-2-agent-mode-changes-in-rust-v0-94-0|2 Agent Mode
  changes in rust-v0.94.0]]'
- '[[Changes/ElevenLabs/2026-02-02-python-sdk|Python SDK]]'
- '[[Changes/ElevenLabs/2026-02-02-javascript-sdk|JavaScript SDK]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-02-02-2026-02-02-2180766f|elevenlabs-2026-02-02-2026-02-02-2180766f]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2026-02-02 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/2/2) · from [[Releases/ElevenLabs/elevenlabs-2026-02-02-2026-02-02-2180766f|ElevenLabs updates — 2026-02-02]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Agent branch renaming**: You can now rename agent branches using the [Update branch](https://elevenlabs.io/docs/api-reference/agents/branches/update) endpoint. The new optional `name` field accepts 1-140 characters.
>
> **Alignment guardrails**: Added `AlignmentGuardrail` type to `GuardrailsV1` schema for enhanced conversation safety controls.
>
> **Speculative turn configuration**: Added `speculative_turn` field to turn configuration for fine-tuning agent turn-taking behavior.
>
> **Procedure references**: Agent patch requests now support `procedure_refs` for referencing reusable procedures.
>
> **Webhook response filtering**: Added `response_filter_mode` and `response_filters` fields to webhook overrides, with new `ResponseFilterMode` enum for controlling which response data is passed through.
>
> **Error details in tool events**: Added `raw_error_message` field to API integration webhook, system, and workflow tool event models for improved debugging.
>
> **Flexible tool call matching**: Testing models now include `check_any_tool_matches` option to relax tool call matching requirements during agent testing.
>
> **Secrets pagination**: [Get workspace secrets](https://elevenlabs.io/docs/api-reference/workspace/secrets/list) endpoint now supports pagination with `page_size` (max 100) and `cursor` query parameters, returning `next_cursor` and `has_more` in responses.
>
> Source: https://elevenlabs.io/docs/changelog/2026/2/2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-02-02-workspaces|Workspaces]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-02-02-new-schemas|New Schemas]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-02-python-sdk|Python SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-02-02-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-02-02-eleven-v3|Eleven v3]] · Reliability and Performance
- [[Changes/ElevenLabs/2026-02-02-text-to-dialogue|Text-to-Dialogue]] · Model Support
- [[Changes/ElevenLabs/2026-02-02-widget-packages|Widget Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-02-javascript-sdk|JavaScript SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-02-02-react-and-client-sdks|React and Client SDKs]] · Voice and Audio
- [[Changes/ElevenLabs/2026-02-02-user|User]] · Model Support
- [[Changes/ElevenLabs/2026-02-02-agents-platform-fb792c|Agents Platform]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-02-02 · Codex CLI · [[Changes/Codex CLI/2026-02-02-2-agent-mode-changes-in-rust-v0-94-0|2 Agent Mode changes in rust-v0.94.0]]
- Later: 2026-02-03 · Claude Code · [[Changes/Claude Code/2026-02-03-added-token-count-tool-uses-and-duration-metrics-to-task-tool-results|Added token count, tool uses, and duration metrics to Task tool results]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-02-02-f8a58b&body=Card%3A%20Changes%2FElevenLabs%2F2026-02-02-agents-platform.md%0ACard%20ID%3A%20elevenlabs-2026-02-02-f8a58b%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F2%2F2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->