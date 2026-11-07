---
card_id: elevenlabs-2026-01-26-4ffdec
date: '2026-01-26'
description: 'ElevenLabs · 2026-01-26 · Agent Mode: [Get tools](https://elevenlabs.io/docs/api-reference/tools/list)'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 935
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 695359e6f6ce7478d7998481428ac9f68a8bd55f40a21e0b905c86222568cbe9
product: elevenlabs
product_name: ElevenLabs
record:
  card_id: elevenlabs-2026-01-26-4ffdec
  comparison: ''
  date: '2026-01-26'
  description: 'ElevenLabs — ElevenLabs updates — 2026-01-26: [Get tools](https://elevenlabs.io/docs/api-reference/tools/list)'
  evidence:
  - quote: '[Get tools](https://elevenlabs.io/docs/api-reference/tools/list)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: Added `search` query parameter (string, optional) for filtering tools by
      name prefix
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: Added `page_size` query parameter (integer, optional, max 100, default
      30)
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: Added `show_only_owned_documents` query parameter (boolean, optional, default
      false)
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: Added `types` query parameter (array, optional) for filtering by tool type
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: Added `sort_by` query parameter (enum, optional) for sorting results
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: Added `sort_direction` query parameter (enum, optional) for sort order
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: Added `cursor` query parameter (string, optional) for pagination
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: Response now includes `next_cursor` (string) and `has_more` (boolean, required)
      fields
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: '[Create agent](https://elevenlabs.io/docs/api-reference/agents/create)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: Request schema updated with branching support
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: '[Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: Added `agent_name` (string, optional) to response model
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: '[Create agent draft](https://elevenlabs.io/docs/api-reference/agents/drafts/create)'
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  - quote: Made `tags` field optional and removed from required fields
    source_release: https://elevenlabs.io/docs/changelog/2026/1/26
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: agents-platform
  source_release: elevenlabs-2026-01-26-2026-01-26-f7dcd336
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: Agents Platform
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-01-25-2-agent-mode-changes-in-rust-v0-90-0|2 Agent Mode
  changes in rust-v0.90.0]]'
- '[[Changes/OpenCode/2026-01-25-2-agent-mode-changes-in-v1-1-35|2 Agent Mode changes
  in v1.1.35]]'
- '[[Changes/ElevenLabs/2026-01-26-python-sdk|Python SDK]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-01-26-2026-01-26-f7dcd336|elevenlabs-2026-01-26-2026-01-26-f7dcd336]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: Agents Platform
type: change
---

<!-- chronolog:begin region="header" -->
# Agents Platform

**ElevenLabs** · 2026-01-26 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/1/26) · from [[Releases/ElevenLabs/elevenlabs-2026-01-26-2026-01-26-f7dcd336|ElevenLabs updates — 2026-01-26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [Get tools](https://elevenlabs.io/docs/api-reference/tools/list)
>
> Added `search` query parameter (string, optional) for filtering tools by name prefix
>
> Added `page_size` query parameter (integer, optional, max 100, default 30)
>
> Added `show_only_owned_documents` query parameter (boolean, optional, default false)
>
> Added `types` query parameter (array, optional) for filtering by tool type
>
> Added `sort_by` query parameter (enum, optional) for sorting results
>
> Added `sort_direction` query parameter (enum, optional) for sort order
>
> Added `cursor` query parameter (string, optional) for pagination
>
> Response now includes `next_cursor` (string) and `has_more` (boolean, required) fields
>
> [Create agent](https://elevenlabs.io/docs/api-reference/agents/create)
>
> Request schema updated with branching support
>
> [Get conversation](https://elevenlabs.io/docs/api-reference/conversations/get)
>
> Added `agent_name` (string, optional) to response model
>
> [Create agent draft](https://elevenlabs.io/docs/api-reference/agents/drafts/create)
>
> Made `tags` field optional and removed from required fields
>
> Source: https://elevenlabs.io/docs/changelog/2026/1/26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-01-26-python-sdk|Python SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-26-workspaces|Workspaces]] · Safety and Privacy
- [[Changes/ElevenLabs/2026-01-26-javascript-sdk|JavaScript SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-26-new-endpoints|New Endpoints]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-26-agents-platform-89c04a|Agents Platform]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-26-knowledge-base|Knowledge Base]] · Files and Data
- [[Changes/ElevenLabs/2026-01-26-music|Music]] · Voice and Audio
- [[Changes/ElevenLabs/2026-01-26-elevencreative-studio|ElevenCreative Studio]] · Model Support
- [[Changes/ElevenLabs/2026-01-26-new-schemas|New Schemas]] · Agent Mode
- [[Changes/ElevenLabs/2026-01-26-sdk-releases|SDK Releases]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-01-25 · OpenCode · [[Changes/OpenCode/2026-01-25-2-agent-mode-changes-in-v1-1-35|2 Agent Mode changes in v1.1.35]]
- Later: 2026-01-26 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-01-26-load-local-shell-configuration-in-agent-sessions|Load local shell configuration in agent sessions]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-01-26-4ffdec&body=Card%3A%20Changes%2FElevenLabs%2F2026-01-26-agents-platform.md%0ACard%20ID%3A%20elevenlabs-2026-01-26-4ffdec%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F1%2F26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->