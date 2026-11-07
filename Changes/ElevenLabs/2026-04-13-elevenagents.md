---
card_id: elevenlabs-2026-04-13-ccb0fb
date: '2026-04-13'
description: 'ElevenLabs · 2026-04-13 · Agent Mode: **Conversation topic discovery**:
  A new [conversation topics](https://elevenlabs.io/docs/api-reference/conversations/get)…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1012
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 8a00de4f4e016cfb2309d88974736cb0719ee043b5d43e86e62b5f2863b158a8
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-04-13-ccb0fb
  comparison: ''
  confidence: low
  date: '2026-04-13'
  description: 'ElevenLabs — ElevenLabs updates — 2026-04-13: **Conversation topic
    discovery**: A new [conversation topics](https://elevenlabs.io/docs/api-reference/conversations/get)
    endpoint (`GET /v1/convai/agents/{agent_id}/topics`) returns the latest topic
    discovery results for a given agent, surfacing recurring themes across conversations.
    The [list conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
    endpoint now accepts a `topic_ids` query parameter to filter conversations by
    discovered topic.'
  evidence:
  - quote: '**Conversation topic discovery**: A new [conversation topics](https://elevenlabs.io/docs/api-reference/conversations/get)
      endpoint (`GET /v1/convai/agents/{agent_id}/topics`) returns the latest topic
      discovery results for a given agent, surfacing recurring themes across conversations.
      The [list conversations](https://elevenlabs.io/docs/api-reference/conversations/list)
      endpoint now accepts a `topic_ids` query parameter to filter conversations by
      discovered topic.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/13
  - quote: '**Knowledge base content search**: A new [search knowledge base](https://elevenlabs.io/docs/api-reference/knowledge-base/search)
      endpoint (`GET /v1/convai/knowledge-base/search`) provides fuzzy text search
      over knowledge base document content. Results include highlighted snippets with
      `SearchHighlightSegment` objects and support cursor-based pagination with configurable
      page sizes (up to 100, default 30). Filter by document type with the optional
      `types` parameter.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/13
  - quote: '**Flexible branch merging**: The [merge branch](https://elevenlabs.io/docs/api-reference/agents/branches/merge)
      endpoint no longer restricts merges to the main branch -- any branch can now
      be used as a merge target. A new optional `force` boolean parameter overrides
      timestamp-based conflict resolution when set to `true`. Branch metadata responses
      now include `parent_branch_id` and `merged_from_version_id` for better lineage
      tracking.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/13
  - quote: '**Secret dependency management**: A new [get secret dependencies](https://elevenlabs.io/docs/api-reference/workspace/secrets/get-dependencies)
      endpoint (`GET /v1/convai/secrets/{secret_id}/dependencies/{resource_type}`)
      returns paginated dependency lookups filtered by resource type (`tools`, `agents`,
      or `phone_numbers`). The [list secrets](https://elevenlabs.io/docs/api-reference/workspace/secrets/list)
      endpoint now accepts a `dependency_limit` query parameter to control how many
      dependencies are previewed per secret, with `agents_has_more`, `tools_has_more`,
      and `phone_numbers_has_more` flags indicating when additional dependents exist
      beyond the preview.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/13
  - quote: '**New LLM options**: Added `gemini-3.1-pro-preview` to the list of available
      LLM providers for agent configuration.'
    source_release: https://elevenlabs.io/docs/changelog/2026/4/13
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-04-13-2026-04-13-a9d3ca3b
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-13-this-release-introduces-improvements-to-our-agents-window-interface-as-part-of-c|Cursor
  introduces improvements to our Agents Window interface as part of Cursor 3]]'
- '[[Changes/Cursor/2026-04-13-branch-selection-in-empty-state|Branch selection in
  empty state]]'
- '[[Changes/Cursor/2026-04-13-3-agent-mode-changes-in-3-1|3 Agent Mode changes in
  3.1]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-04-13-2026-04-13-a9d3ca3b|elevenlabs-2026-04-13-2026-04-13-a9d3ca3b]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-04-13 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/4/13) · from [[Releases/ElevenLabs/elevenlabs-2026-04-13-2026-04-13-a9d3ca3b|ElevenLabs updates — 2026-04-13]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Conversation topic discovery**: A new [conversation topics](https://elevenlabs.io/docs/api-reference/conversations/get) endpoint (`GET /v1/convai/agents/{agent_id}/topics`) returns the latest topic discovery results for a given agent, surfacing recurring themes across conversations. The [list conversations](https://elevenlabs.io/docs/api-reference/conversations/list) endpoint now accepts a `topic_ids` query parameter to filter conversations by discovered topic.
>
> **Knowledge base content search**: A new [search knowledge base](https://elevenlabs.io/docs/api-reference/knowledge-base/search) endpoint (`GET /v1/convai/knowledge-base/search`) provides fuzzy text search over knowledge base document content. Results include highlighted snippets with `SearchHighlightSegment` objects and support cursor-based pagination with configurable page sizes (up to 100, default 30). Filter by document type with the optional `types` parameter.
>
> **Flexible branch merging**: The [merge branch](https://elevenlabs.io/docs/api-reference/agents/branches/merge) endpoint no longer restricts merges to the main branch -- any branch can now be used as a merge target. A new optional `force` boolean parameter overrides timestamp-based conflict resolution when set to `true`. Branch metadata responses now include `parent_branch_id` and `merged_from_version_id` for better lineage tracking.
>
> **Secret dependency management**: A new [get secret dependencies](https://elevenlabs.io/docs/api-reference/workspace/secrets/get-dependencies) endpoint (`GET /v1/convai/secrets/{secret_id}/dependencies/{resource_type}`) returns paginated dependency lookups filtered by resource type (`tools`, `agents`, or `phone_numbers`). The [list secrets](https://elevenlabs.io/docs/api-reference/workspace/secrets/list) endpoint now accepts a `dependency_limit` query parameter to control how many dependencies are previewed per secret, with `agents_has_more`, `tools_has_more`, and `phone_numbers_has_more` flags indicating when additional dependents exist beyond the preview.
>
> **New LLM options**: Added `gemini-3.1-pro-preview` to the list of available LLM providers for agent configuration.
>
> Source: https://elevenlabs.io/docs/changelog/2026/4/13
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-04-13-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-13-python-sdk|Python SDK]] · Model Support
- [[Changes/ElevenLabs/2026-04-13-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-13-javascript-sdk|JavaScript SDK]] · Model Support
- [[Changes/ElevenLabs/2026-04-13-swift-sdk|Swift SDK]] · Voice and Audio
- [[Changes/ElevenLabs/2026-04-13-sdk-releases|SDK Releases]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-13 · Cursor · [[Changes/Cursor/2026-04-13-3-agent-mode-changes-in-3-1|3 Agent Mode changes in 3.1]]
- Later: 2026-04-14 · Cursor · [[Changes/Cursor/2026-04-14-ask-a-quick-side-question-without-derailing-the-agent-s-main-task-btw-allows-you|/btw support in CLI]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-04-13-ccb0fb&body=Card%3A%20Changes%2FElevenLabs%2F2026-04-13-elevenagents.md%0ACard%20ID%3A%20elevenlabs-2026-04-13-ccb0fb%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F4%2F13%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->