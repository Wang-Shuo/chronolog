---
card_id: claude-code-2026-05-21-645cfa
date: '2026-05-21'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1050
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-19-added-elapsed-duration-to-background-subagent-completion-notifications-e-g-agent|claude-code-2026-05-19-f74413]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 2d87fb5e8b6a0919f187bcd1e2b4d7622c9876e35582c19fa953212f9c74fff1
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-19-added-elapsed-duration-to-background-subagent-completion-notifications-e-g-agent|claude-code-2026-05-19-f74413]]'
- '[[Changes/Cursor/2026-05-19-assign-work-items-to-cursor-or-mention-cursor-in-a-comment-to-kick-off-a-cloud-a|cursor-2026-05-19-269d26]]'
- '[[Changes/Cursor/2026-05-20-with-loop-cursor-can-run-a-prompt-repeatedly-on-a-local-schedule-until-a-certain|cursor-2026-05-20-8c2c28]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-21-v2-1-146-github-326230049-ea612648|claude-code-2026-05-21-v2-1-146-github-326230049-ea612648]]'
theme: agent-mode
type: change
---

# Auto mode no longer suppresses `AskUserQuestion` when the user or a skill explic

<!-- chronolog:begin region="description" -->
Auto mode no longer suppresses `AskUserQuestion` when the user or a skill explicitly relies on it
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Auto mode no longer suppresses `AskUserQuestion` when the user or a skill explicitly relies on it
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.146
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-19-added-elapsed-duration-to-background-subagent-completion-notifications-e-g-agent|claude-code-2026-05-19-f74413]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1050
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes