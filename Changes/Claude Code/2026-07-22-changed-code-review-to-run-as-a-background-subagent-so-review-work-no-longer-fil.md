---
card_id: claude-code-2026-07-22-9535c3
date: '2026-07-22'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1222
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-21-improved-footer-pr-badge-links-to-be-clickable-hyperlinks-even-when-terminal-sup|claude-code-2026-07-21-7c3261]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 5b601750bfca62cccb6c88d45ee51b1f56282d2e3d9e7f97ec5cb6ecfad9fc30
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-10-added-directory-path-suggestions-to-cd-matching-add-dir-behavior|claude-code-2026-07-10-e508b3]]'
- '[[Changes/Claude Code/2026-07-19-claude-no-longer-runs-the-verify-and-code-review-skills-on-its-own-invoke-them-w|claude-code-2026-07-19-3944a0]]'
- '[[Changes/Claude Code/2026-07-21-improved-footer-pr-badge-links-to-be-clickable-hyperlinks-even-when-terminal-sup|claude-code-2026-07-21-7c3261]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4|claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4]]'
theme: developer-workflow
type: change
---

# Changed `/code-review` to run as a background subagent, so review work no longer

<!-- chronolog:begin region="description" -->
Changed `/code-review` to run as a background subagent, so review work no longer fills your conversation and keeps stacked slash commands as its review target
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Changed `/code-review` to run as a background subagent, so review work no longer fills your conversation and keeps stacked slash commands as its review target
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.218
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-21-improved-footer-pr-badge-links-to-be-clickable-hyperlinks-even-when-terminal-sup|claude-code-2026-07-21-7c3261]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1222
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes