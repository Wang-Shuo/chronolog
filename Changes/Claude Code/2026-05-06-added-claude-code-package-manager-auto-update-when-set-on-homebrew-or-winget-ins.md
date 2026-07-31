---
card_id: claude-code-2026-05-06-3f1ca0
date: '2026-05-06'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1145
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-28-opentelemetry-added-claude-code-at-mention-log-event-for-mention-resolution|claude-code-2026-04-28-33dc91]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 6051589c9f75d1410d89a27c011e73649cf483578740f8c4208d23a6051c6f7d
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-22-the-resume-command-now-offers-to-summarize-stale-large-sessions-before-re-readin|claude-code-2026-04-22-a4073c]]'
- '[[Changes/Claude Code/2026-04-23-added-prurltemplate-setting-to-point-the-footer-pr-badge-at-a-custom-code-review|claude-code-2026-04-23-cf1efd]]'
- '[[Changes/Claude Code/2026-04-28-opentelemetry-added-claude-code-at-mention-log-event-for-mention-resolution|claude-code-2026-04-28-33dc91]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-06-v2-1-129-github-317982632-ec56fc0f|claude-code-2026-05-06-v2-1-129-github-317982632-ec56fc0f]]'
theme: developer-workflow
type: change
---

# Added `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE`: when set on Homebrew or WinGet

<!-- chronolog:begin region="description" -->
Added `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE`: when set on Homebrew or WinGet installations, Claude Code runs the upgrade command in the background and prompts to restart
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE`: when set on Homebrew or WinGet installations, Claude Code runs the upgrade command in the background and prompts to restart
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.129
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-28-opentelemetry-added-claude-code-at-mention-log-event-for-mention-resolution|claude-code-2026-04-28-33dc91]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1145
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes