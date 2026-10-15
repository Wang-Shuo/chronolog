---
card_id: claude-code-2026-10-14-0e9e30
date: '2026-10-14'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1259
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: ca469848d6adb7e65dcb19e190f1440bc37643e63f7cc4ec7768ba250174c34c
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-14-0e9e30
  comparison: ''
  date: '2026-10-14'
  description: 'Claude Code — v2.1.300: Added `cache_creation_5m_tokens` and `cache_creation_1h_tokens`
    to the OpenTelemetry `api_request` event, splitting cache writes by lifetime'
  evidence:
  - quote: Added `cache_creation_5m_tokens` and `cache_creation_1h_tokens` to the
      OpenTelemetry `api_request` event, splitting cache writes by lifetime
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-cache-creation-5m-tokens-and-cache-creation-1h-tokens-to-the-opentelemetry
  source_release: claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0
  source_type: github_releases
  theme: context-window
  title: Added `cache_creation_5m_tokens` and `cache_creation_1h_tokens` to the OpenTelem
  type: change
related_changes:
- '[[Changes/Cursor/2026-09-10-today-we-re-launching-projects-in-cursor-projects-lets-you-take-on-larger-bodies|cursor-2026-09-10-bf27c0]]'
- '[[Changes/Claude Code/2026-09-15-added-x-claude-code-request-class-x-claude-code-agent-type-x-claude-code-prev-to|claude-code-2026-09-15-d69af3]]'
- '[[Changes/Claude Code/2026-10-09-added-autocompactwindow-to-subagent-frontmatter-and-agents-definitions-so-a-suba|claude-code-2026-10-09-bc35b4]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0|claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0]]'
source_type: github_releases
theme: context-window
title: Added cache_creation_5m_tokens and cache_creation_1h_tokens to the OpenTelem
type: change
---

# Added `cache_creation_5m_tokens` and `cache_creation_1h_tokens` to the OpenTelem

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.300: Added `cache_creation_5m_tokens` and `cache_creation_1h_tokens` to the OpenTelemetry `api_request` event, splitting cache writes by lifetime
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `cache_creation_5m_tokens` and `cache_creation_1h_tokens` to the OpenTelemetry `api_request` event, splitting cache writes by lifetime
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 1259
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes