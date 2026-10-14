---
card_id: claude-code-2026-07-02-ebe592
date: '2026-07-02'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1295
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: b532567b8bc0250f8b2f17a097baf43a3d54b402f99b46d06efe7bf4c3c6a073
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-02-ebe592
  comparison: ''
  date: '2026-07-02'
  description: 'Claude Code — v2.1.199: `CLAUDE_CODE_RETRY_WATCHDOG` now raises the
    default retry count for non-capacity transient errors to 300 and lifts the cap
    of 15 on `CLAUDE_CODE_MAX_RETRIES`'
  evidence:
  - quote: '`CLAUDE_CODE_RETRY_WATCHDOG` now raises the default retry count for non-capacity
      transient errors to 300 and lifts the cap of 15 on `CLAUDE_CODE_MAX_RETRIES`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.199
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: claude-code-retry-watchdog-now-raises-the-default-retry-count-for-non-capacity-t
  source_release: claude-code-2026-07-02-v2-1-199-github-348195313-a8a76d9f
  source_type: github_releases
  theme: reliability-performance
  theme_matches: []
  theme_resolution: manual-backfill-review-v1
  title: '`CLAUDE_CODE_RETRY_WATCHDOG` now raises the default retry count for non-capacity'
  type: change
related_changes:
- '[[Changes/Cursor/2026-06-17-your-environment-is-captured-in-a-reusable-snapshot-so-future-cloud-agents-start|cursor-2026-06-17-efeb40]]'
- '[[Changes/Claude Code/2026-06-20-the-stream-stall-hint-now-reads-waiting-for-api-response-will-retry-in-instead-o|claude-code-2026-06-20-ef4f72]]'
- '[[Changes/Claude Code/2026-07-02-transient-server-rate-limit-errors-429s-unrelated-to-your-usage-limit-are-now-re|claude-code-2026-07-02-964eea]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-02-v2-1-199-github-348195313-a8a76d9f|claude-code-2026-07-02-v2-1-199-github-348195313-a8a76d9f]]'
source_type: github_releases
theme: reliability-performance
title: CLAUDE_CODE_RETRY_WATCHDOG now raises the default retry count for non-capacity
type: change
---

# `CLAUDE_CODE_RETRY_WATCHDOG` now raises the default retry count for non-capacity

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.199: `CLAUDE_CODE_RETRY_WATCHDOG` now raises the default retry count for non-capacity transient errors to 300 and lifts the cap of 15 on `CLAUDE_CODE_MAX_RETRIES`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `CLAUDE_CODE_RETRY_WATCHDOG` now raises the default retry count for non-capacity transient errors to 300 and lifts the cap of 15 on `CLAUDE_CODE_MAX_RETRIES`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.199
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1295
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes