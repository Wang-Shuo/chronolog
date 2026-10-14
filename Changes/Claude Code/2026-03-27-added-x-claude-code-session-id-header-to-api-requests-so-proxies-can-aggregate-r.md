---
card_id: claude-code-2026-03-27-358253
date: '2026-03-27'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1105
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: 3dded10481888166d4422c034fe4f51e926f26eb7c9c62debf36f1d75e33aeb0
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-27-358253
  comparison: ''
  date: '2026-03-27'
  description: 'Claude Code — v2.1.86: Added `X-Claude-Code-Session-Id` header to
    API requests so proxies can aggregate requests by session without parsing the
    body'
  evidence:
  - quote: Added `X-Claude-Code-Session-Id` header to API requests so proxies can
      aggregate requests by session without parsing the body
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.86
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-x-claude-code-session-id-header-to-api-requests-so-proxies-can-aggregate-r
  source_release: claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859
  source_type: github_releases
  theme: developer-workflow
  theme_matches: []
  theme_resolution: manual-backfill-review-v1
  title: Added `X-Claude-Code-Session-Id` header to API requests so proxies can aggregate
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-20-resuming-a-session-that-was-in-a-worktree-now-switches-back-to-that-worktree|claude-code-2026-03-20-c20f4f]]'
- '[[Changes/Claude Code/2026-03-20-added-bare-flag-for-scripted-p-calls-skips-hooks-lsp-plugin-sync-and-skill-direc|claude-code-2026-03-20-d05f5d]]'
- '[[Changes/Claude Code/2026-03-26-added-worktreecreate-hook-support-for-type-http-return-the-created-worktree-path|claude-code-2026-03-26-b1182f]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859|claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859]]'
source_type: github_releases
theme: developer-workflow
title: Added X-Claude-Code-Session-Id header to API requests so proxies can aggregate
type: change
---

# Added `X-Claude-Code-Session-Id` header to API requests so proxies can aggregate

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.86: Added `X-Claude-Code-Session-Id` header to API requests so proxies can aggregate requests by session without parsing the body
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `X-Claude-Code-Session-Id` header to API requests so proxies can aggregate requests by session without parsing the body
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.86
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1105
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes