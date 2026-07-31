---
card_id: claude-code-2026-07-15-12d419
date: '2026-07-15'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1105
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-15-improved-background-agent-result-reporting-claude-now-reports-the-status-of-stil|claude-code-2026-07-15-05aede]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: b4e970f4389982d096e73793788c3193a237dbc4ea24d343710cda1e921befef
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-14-hardened-the-agent-tool-against-indirect-prompt-injection-via-content-a-subagent|claude-code-2026-07-14-b086cc]]'
- '[[Changes/Claude Code/2026-07-14-added-claude-code-process-wrapper-agent-view-and-the-background-service-now-hono|claude-code-2026-07-14-dfb540]]'
- '[[Changes/Claude Code/2026-07-15-improved-background-agent-result-reporting-claude-now-reports-the-status-of-stil|claude-code-2026-07-15-05aede]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-15-v2-1-211-github-354658856-71e66e57|claude-code-2026-07-15-v2-1-211-github-354658856-71e66e57]]'
theme: agent-mode
type: change
---

# Added `--forward-subagent-text` flag and `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` env

<!-- chronolog:begin region="description" -->
Added `--forward-subagent-text` flag and `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` environment variable to include subagent text and thinking in stream-json output
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `--forward-subagent-text` flag and `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` environment variable to include subagent text and thinking in stream-json output
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.211
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-15-improved-background-agent-result-reporting-claude-now-reports-the-status-of-stil|claude-code-2026-07-15-05aede]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1105
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes