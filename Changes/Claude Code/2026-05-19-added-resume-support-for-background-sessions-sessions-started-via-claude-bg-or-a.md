---
card_id: claude-code-2026-05-19-215520
date: '2026-05-19'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1048
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-13-added-claude-agents-cwd-path-to-scope-the-session-list-to-a-directory|claude-code-2026-05-13-31bba2]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: 4bad99f4c40322c1e952e03ede7a7ef68dcec39ca7e556f1fcf777c02b241d14
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-05-13-cloud-agents-and-automations-now-support-multi-repo-environments-building-off-ou|cursor-2026-05-13-b5c19b]]'
- '[[Changes/Cursor/2026-05-13-this-release-introduces-new-tools-for-teams-to-configure-development-environment|cursor-2026-05-13-e9f5ab]]'
- '[[Changes/Cursor/2026-05-18-composer-2-5-is-now-available-in-cursor|cursor-2026-05-18-3afa8e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-19-v2-1-144-github-324524751-1469637a|claude-code-2026-05-19-v2-1-144-github-324524751-1469637a]]'
theme: agent-mode
type: change
---

# Added `/resume` support for background sessions — sessions started via `claude -

<!-- chronolog:begin region="description" -->
Added `/resume` support for background sessions — sessions started via `claude --bg` or agent view now appear alongside interactive ones, marked with `bg`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `/resume` support for background sessions — sessions started via `claude --bg` or agent view now appear alongside interactive ones, marked with `bg`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.144
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-13-added-claude-agents-cwd-path-to-scope-the-session-list-to-a-directory|claude-code-2026-05-13-31bba2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1048
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes