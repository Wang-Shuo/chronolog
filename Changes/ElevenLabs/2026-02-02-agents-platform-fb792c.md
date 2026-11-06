---
card_id: elevenlabs-2026-02-02-fb792c
date: '2026-02-02'
description: 'ElevenLabs · 2026-02-02 · Agent Mode: [Update agent branch](https://elevenlabs.io/docs/api-reference/agents/branches/update)'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 942
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 69dbc3f4c7aae12cfce4e68c3d2c2d514107197f61014c6fa93832d1ab4d3961
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-02-02-fb792c
  comparison: ''
  confidence: low
  date: '2026-02-02'
  description: 'ElevenLabs — ElevenLabs updates — 2026-02-02: [Update agent branch](https://elevenlabs.io/docs/api-reference/agents/branches/update)'
  evidence:
  - quote: '[Update agent branch](https://elevenlabs.io/docs/api-reference/agents/branches/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: Added optional `name` field (string, 1-140 characters, nullable) for renaming
      branches
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: '[Get workspace secrets](https://elevenlabs.io/docs/api-reference/workspace/secrets/list)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: Added `page_size` query parameter (integer, optional, max 100) for pagination
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: Added `cursor` query parameter (string, optional) for fetching next page
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: Response now includes `next_cursor` (string) and `has_more` (boolean) fields
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create),
      [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: Added `speculative_turn` field to turn configuration
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: Added `procedure_refs` field to agent patch schema
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: Added `AlignmentGuardrail` to `GuardrailsV1` schema
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: Added `response_filter_mode` and `response_filters` to webhook overrides
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: '[Create agent test](https://elevenlabs.io/docs/api-reference/tests/create),
      [Update agent test](https://elevenlabs.io/docs/api-reference/tests/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/2/2
  - quote: Added `check_any_tool_matches` field (boolean, optional) for relaxed tool
      call matching
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
- '[[Changes/ElevenLabs/2026-02-02-python-sdk|Python SDK]]'
- '[[Changes/ElevenLabs/2026-02-02-javascript-sdk|JavaScript SDK]]'
- '[[Changes/ElevenLabs/2026-02-02-agents-platform|Agents Platform]]'
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
> [Update agent branch](https://elevenlabs.io/docs/api-reference/agents/branches/update)
>
> Added optional `name` field (string, 1-140 characters, nullable) for renaming branches
>
> [Get workspace secrets](https://elevenlabs.io/docs/api-reference/workspace/secrets/list)
>
> Added `page_size` query parameter (integer, optional, max 100) for pagination
>
> Added `cursor` query parameter (string, optional) for fetching next page
>
> Response now includes `next_cursor` (string) and `has_more` (boolean) fields
>
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
>
> Added `speculative_turn` field to turn configuration
>
> Added `procedure_refs` field to agent patch schema
>
> Added `AlignmentGuardrail` to `GuardrailsV1` schema
>
> Added `response_filter_mode` and `response_filters` to webhook overrides
>
> [Create agent test](https://elevenlabs.io/docs/api-reference/tests/create), [Update agent test](https://elevenlabs.io/docs/api-reference/tests/update)
>
> Added `check_any_tool_matches` field (boolean, optional) for relaxed tool call matching
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
- [[Changes/ElevenLabs/2026-02-02-agents-platform|Agents Platform]] · Agent Mode
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
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-02-02-fb792c&body=Card%3A%20Changes%2FElevenLabs%2F2026-02-02-agents-platform-fb792c.md%0ACard%20ID%3A%20elevenlabs-2026-02-02-fb792c%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F2%2F2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->