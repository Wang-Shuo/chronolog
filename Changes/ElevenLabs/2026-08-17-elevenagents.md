---
card_id: elevenlabs-2026-08-17-7b699a
date: '2026-08-17'
description: 'ElevenLabs · 2026-08-17 · Agent Mode: **Lightweight conversation summaries**:
  [Get conversation…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1138
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 87997a10eed6ad270267dde9eb54f3a0148292758eb5e1c461fc1bf1930381db
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-08-17-7b699a
  comparison: ''
  confidence: low
  date: '2026-08-17'
  description: 'ElevenLabs — ElevenLabs updates — 2026-08-17: **Lightweight conversation
    summaries**: [Get conversation summary](https://elevenlabs.io/docs/api-reference/conversations/get-summary)
    returns the generated title, transcript summary, call outcome and plain user or
    agent messages without loading the full transcript. The optional `max_messages`
    query parameter is an integer from 1 to 200 (default `40`); longer conversations
    set `messages_omitted` to `true`. Useful for agents that need to preserve context.'
  evidence:
  - quote: '**Lightweight conversation summaries**: [Get conversation summary](https://elevenlabs.io/docs/api-reference/conversations/get-summary)
      returns the generated title, transcript summary, call outcome and plain user
      or agent messages without loading the full transcript. The optional `max_messages`
      query parameter is an integer from 1 to 200 (default `40`); longer conversations
      set `messages_omitted` to `true`. Useful for agents that need to preserve context.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: '**Conversation topic pagination and sorting**: [Get agent conversation
      topics](https://elevenlabs.io/docs/api-reference/conversations/topics/get) adds
      optional cursor pagination and sorting. Use `page_size` (integer, 1–100), `cursor`
      (string), `sort_by` (`conversations`, `sentiment` or `success_rate`) and `sort_direction`
      (`asc` or `desc`). Responses add `has_more` and nullable `next_cursor`.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: '**Concurrency wait queues**: Agent platform settings add optional `queueing`
      (`AgentQueueingConfig`). Set `enabled` to `true` to hold callers when the agent
      reaches its concurrency limit; `wait_timeout_seconds` is an integer up to 1,800
      (default `180`).'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: '**Turn and workflow controls**: Turn configuration adds `merge_with_default_ignore_terms`
      (boolean, default `false`) to combine custom interruption terms with curated
      defaults. Soft timeouts add `disable_until_first_user_message` (boolean, default
      `false`), and workflow tool locators add optional `schema_overrides` for per-node
      parameter overrides.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  - quote: '**Background audio defaults**: `BackgroundSoundConfig.volume` now defaults
      to `0.15` instead of `0.6`, and `crossfade_loop` now defaults to `true` instead
      of `false`. Set these fields explicitly to retain the previous behavior.'
    source_release: https://elevenlabs.io/docs/changelog/2026/8/17
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-08-17-2026-08-17-6196d42b
  source_type: elevenlabs_changelog
  theme: agent-mode
  theme_matches:
  - matched_terms:
    - agent
    - agents
    score: 100
    theme: agent-mode
  - matched_terms:
    - context
    score: 50
    theme: context-window
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/v0/2026-08-14-the-paused-agent-timeout-card-shows-resuming-and-resumed-states|The
  paused-agent timeout card shows Resuming and Resumed states]]'
- '[[Changes/Claude Code/2026-08-17-removed-the-redundant-allowed-by-auto-mode-classifier-line-that-auto-mode-showed|Removed
  the redundant "Allowed by auto mode classifier" line that auto mode showed…]]'
- '[[Changes/Cursor/2026-08-17-agents-in-every-repo|Agents in every repo]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-08-17-2026-08-17-6196d42b|elevenlabs-2026-08-17-2026-08-17-6196d42b]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-08-17 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/8/17) · from [[Releases/ElevenLabs/elevenlabs-2026-08-17-2026-08-17-6196d42b|ElevenLabs updates — 2026-08-17]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Lightweight conversation summaries**: [Get conversation summary](https://elevenlabs.io/docs/api-reference/conversations/get-summary) returns the generated title, transcript summary, call outcome and plain user or agent messages without loading the full transcript. The optional `max_messages` query parameter is an integer from 1 to 200 (default `40`); longer conversations set `messages_omitted` to `true`. Useful for agents that need to preserve context.
>
> **Conversation topic pagination and sorting**: [Get agent conversation topics](https://elevenlabs.io/docs/api-reference/conversations/topics/get) adds optional cursor pagination and sorting. Use `page_size` (integer, 1–100), `cursor` (string), `sort_by` (`conversations`, `sentiment` or `success_rate`) and `sort_direction` (`asc` or `desc`). Responses add `has_more` and nullable `next_cursor`.
>
> **Concurrency wait queues**: Agent platform settings add optional `queueing` (`AgentQueueingConfig`). Set `enabled` to `true` to hold callers when the agent reaches its concurrency limit; `wait_timeout_seconds` is an integer up to 1,800 (default `180`).
>
> **Turn and workflow controls**: Turn configuration adds `merge_with_default_ignore_terms` (boolean, default `false`) to combine custom interruption terms with curated defaults. Soft timeouts add `disable_until_first_user_message` (boolean, default `false`), and workflow tool locators add optional `schema_overrides` for per-node parameter overrides.
>
> **Background audio defaults**: `BackgroundSoundConfig.volume` now defaults to `0.15` instead of `0.6`, and `crossfade_loop` now defaults to `true` instead of `false`. Set these fields explicitly to retain the previous behavior.
>
> Source: https://elevenlabs.io/docs/changelog/2026/8/17
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-08-17-python-sdk|Python SDK]] · Multimodal Input
- [[Changes/ElevenLabs/2026-08-17-elevencreative|ElevenCreative]] · Editor Experience
- [[Changes/ElevenLabs/2026-08-17-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-08-17-sdk-releases|SDK Releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-08-17-javascript-sdk|JavaScript SDK]] · Multimodal Input
- [[Changes/ElevenLabs/2026-08-17-elevencreative-fd6a14|ElevenCreative]] · Multimodal Input
- [[Changes/ElevenLabs/2026-08-17-elevenagents-fdc84e|ElevenAgents]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-17 · Cursor · [[Changes/Cursor/2026-08-17-agents-in-every-repo|Agents in every repo]]
- Later: 2026-08-17 · OpenHands · [[Changes/OpenHands/2026-08-17-docs-agents-add-a-repository-map-clarifying-what-belongs-where-by-smolpaws-in-ht|docs(agents): add a repository map clarifying what belongs where]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-08-17-7b699a&body=Card%3A%20Changes%2FElevenLabs%2F2026-08-17-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-08-17-7b699a%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F8%2F17%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->