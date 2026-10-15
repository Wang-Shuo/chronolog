---
card_id: claude-code-2026-03-26-33b65d
date: '2026-03-26'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1197
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 990965cf4205aca1ec353a0d4e97c39766932d5fb8bd1ef80c79cec08c37f43b
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-26-33b65d
  comparison: ''
  date: '2026-03-26'
  description: 'Claude Code — v2.1.84: Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var
    to configure the streaming idle watchdog threshold (default 90s)'
  evidence:
  - quote: Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming
      idle watchdog threshold (default 90s)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-claude-stream-idle-timeout-ms-env-var-to-configure-the-streaming-idle-watc
  source_release: claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa
  source_type: github_releases
  theme: reliability-performance
  theme_matches: []
  theme_resolution: manual-backfill-review-v1
  title: Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming
    idle…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-18-improved-startup-memory-usage-by-18mb-across-all-scenarios|claude-code-2026-03-18-545a2b]]'
- '[[Changes/Claude Code/2026-03-18-improved-non-streaming-api-fallback-with-a-2-minute-per-attempt-timeout-preventi|claude-code-2026-03-18-f2102f]]'
- '[[Changes/Cursor/2026-03-19-composer-2-is-now-available-in-cursor-frontier-level-coding-performance-with-str|cursor-2026-03-19-780a40]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa]]'
source_type: github_releases
theme: reliability-performance
title: Added CLAUDE_STREAM_IDLE_TIMEOUT_MS env var to configure the streaming idle…
type: change
---

# Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming idle…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.84: Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming idle watchdog threshold (default 90s)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming idle watchdog threshold (default 90s)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
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
- Lag Days: 1197
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes