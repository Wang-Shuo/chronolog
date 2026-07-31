---
card_id: claude-code-2026-02-03-a84e37
date: '2026-02-03'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1053
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-01-30-added-tool-call-failures-and-denials-to-debug-logs|claude-code-2026-01-30-aab171]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 7a5b92146f31ab8e846e3a2b26c23ff185aa84b142879905167c05e1f2d453fb
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-01-29-changed-bash-commands-to-show-timeout-duration-alongside-elapsed-time|claude-code-2026-01-29-e261ae]]'
- '[[Changes/Claude Code/2026-01-30-sessions-are-now-automatically-linked-to-prs-when-created-via-gh-pr-create|claude-code-2026-01-30-59b443]]'
- '[[Changes/Claude Code/2026-01-30-added-tool-call-failures-and-denials-to-debug-logs|claude-code-2026-01-30-aab171]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2|claude-code-2026-02-03-v2-1-30-github-282673902-7b2e46f2]]'
theme: developer-workflow
type: change
---

# Added support for additional `git log` and `git show` flags in read-only mode (e

<!-- chronolog:begin region="description" -->
Added support for additional `git log` and `git show` flags in read-only mode (e.g., `--topo-order`, `--cherry-pick`, `--format`, `--raw`)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added support for additional `git log` and `git show` flags in read-only mode (e.g., `--topo-order`, `--cherry-pick`, `--format`, `--raw`)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.30
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-01-30-added-tool-call-failures-and-denials-to-debug-logs|claude-code-2026-01-30-aab171]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1053
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes