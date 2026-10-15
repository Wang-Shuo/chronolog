---
card_id: claude-code-2026-06-20-ef4f72
date: '2026-06-20'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1283
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 8438fcb40439b99d83f9425debce88fe5e7347cfdcb15bcc84ee8a75a11fcda7
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-20-ef4f72
  comparison: ''
  date: '2026-06-20'
  description: 'Claude Code — v2.1.185: The stream-stall hint now reads "Waiting for
    API response · will retry in …" instead of "No response from API · Retrying in
    …", and triggers after 20s of silence instead of 10s'
  evidence:
  - quote: The stream-stall hint now reads "Waiting for API response · will retry
      in …" instead of "No response from API · Retrying in …", and triggers after
      20s of silence instead of 10s
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.185
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: the-stream-stall-hint-now-reads-waiting-for-api-response-will-retry-in-instead-o
  source_release: claude-code-2026-06-20-v2-1-185-github-342367004-9ddb0cf9
  source_type: github_releases
  theme: reliability-performance
  theme_matches: []
  theme_resolution: manual-backfill-review-v1
  title: The stream-stall hint now reads "Waiting for API response · will retry in
    …" instead…
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-06-17-all-tasks-are-faster-and-more-reliable|chatgpt-2026-06-17-281370]]'
- '[[Changes/Claude Code/2026-06-17-improved-auto-retry-api-connection-drops-mid-thinking-now-automatically-retry-in|claude-code-2026-06-17-acfb36]]'
- '[[Changes/Cursor/2026-06-17-your-environment-is-captured-in-a-reusable-snapshot-so-future-cloud-agents-start|cursor-2026-06-17-efeb40]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-20-v2-1-185-github-342367004-9ddb0cf9|claude-code-2026-06-20-v2-1-185-github-342367004-9ddb0cf9]]'
source_type: github_releases
theme: reliability-performance
title: The stream-stall hint now reads "Waiting for API response · will retry in …"
  instead…
type: change
---

# The stream-stall hint now reads "Waiting for API response · will retry in …" instead…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.185: The stream-stall hint now reads "Waiting for API response · will retry in …" instead of "No response from API · Retrying in …", and triggers after 20s of silence instead of 10s
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> The stream-stall hint now reads "Waiting for API response · will retry in …" instead of "No response from API · Retrying in …", and triggers after 20s of silence instead of 10s
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.185
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
- Lag Days: 1283
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes