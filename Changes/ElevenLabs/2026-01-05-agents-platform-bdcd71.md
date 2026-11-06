---
card_id: elevenlabs-2026-01-05-bdcd71
date: '2026-01-05'
description: 'ElevenLabs · 2026-01-05 · Agent Mode: [Get agent](https://elevenlabs.io/docs/api-reference/agents/get),
  [Update…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 914
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 18a459e0eb65ee596ab4e3570f6ec533f3767a665361495757cd7def86162c5d
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-01-05-bdcd71
  comparison: ''
  confidence: low
  date: '2026-01-05'
  description: 'ElevenLabs — ElevenLabs updates — 2026-01-05: [Get agent](https://elevenlabs.io/docs/api-reference/agents/get),
    [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)'
  evidence:
  - quote: '[Get agent](https://elevenlabs.io/docs/api-reference/agents/get), [Update
      agent](https://elevenlabs.io/docs/api-reference/agents/update)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/5
  - quote: Added `version_id` (string, nullable) for agent version identification
    source_release: https://elevenlabs.io/docs/changelog/2026/1/5
  - quote: Added `branch_id` (string, nullable) for agent branch identification
    source_release: https://elevenlabs.io/docs/changelog/2026/1/5
  - quote: Added `main_branch_id` (string, nullable) for main branch reference
    source_release: https://elevenlabs.io/docs/changelog/2026/1/5
  - quote: '[Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/5
  - quote: Added `version_id` (string, nullable) with description "The ID of the agent
      version used for this conversation"
    source_release: https://elevenlabs.io/docs/changelog/2026/1/5
  - quote: '[Get batch call](https://elevenlabs.io/docs/api-reference/batch-calling/get),
      [Submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/5
  - quote: Added `total_calls_finished` (integer, default `0`) to batch call response
      models
    source_release: https://elevenlabs.io/docs/changelog/2026/1/5
  - quote: Expanded `BatchCallRecipientStatus` enum to include `dispatched` status
    source_release: https://elevenlabs.io/docs/changelog/2026/1/5
  - quote: Made `signed_url` nullable for video assets
    source_release: https://elevenlabs.io/docs/changelog/2026/1/5
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2026-01-05-2026-01-05-6c816c7e
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/Dify/2025-12-25-2-agent-mode-changes-in-1-11-2|2 Agent Mode changes in
  1.11.2]]'
- '[[Changes/GitHub Copilot CLI/2026-01-02-built-in-subagents-for-exploring-and-managing-tasks|Built-in
  subagents for exploring and managing tasks]]'
- '[[Changes/ElevenLabs/2026-01-05-agents-platform|Agents Platform]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-01-05-2026-01-05-6c816c7e|elevenlabs-2026-01-05-2026-01-05-6c816c7e]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2026-01-05 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/1/5) · from [[Releases/ElevenLabs/elevenlabs-2026-01-05-2026-01-05-6c816c7e|ElevenLabs updates — 2026-01-05]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Get agent](https://elevenlabs.io/docs/api-reference/agents/get), [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
>
> Added `version_id` (string, nullable) for agent version identification
>
> Added `branch_id` (string, nullable) for agent branch identification
>
> Added `main_branch_id` (string, nullable) for main branch reference
>
> [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)
>
> Added `version_id` (string, nullable) with description "The ID of the agent version used for this conversation"
>
> [Get batch call](https://elevenlabs.io/docs/api-reference/batch-calling/get), [Submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create)
>
> Added `total_calls_finished` (integer, default `0`) to batch call response models
>
> Expanded `BatchCallRecipientStatus` enum to include `dispatched` status
>
> Made `signed_url` nullable for video assets
>
> Source: https://elevenlabs.io/docs/changelog/2026/1/5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-01-05-python-sdk|Python SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-05-javascript-sdk|JavaScript SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-05-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-01-05-agents-platform|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-05-voices|Voices]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-01-02 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-01-02-built-in-subagents-for-exploring-and-managing-tasks|Built-in subagents for exploring and managing tasks]]
- Later: 2026-01-07 · Codex CLI · [[Changes/Codex CLI/2026-01-07-4-agent-mode-changes-in-rust-v0-79-0|4 Agent Mode changes in rust-v0.79.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-01-05-bdcd71&body=Card%3A%20Changes%2FElevenLabs%2F2026-01-05-agents-platform-bdcd71.md%0ACard%20ID%3A%20elevenlabs-2026-01-05-bdcd71%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F1%2F5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->