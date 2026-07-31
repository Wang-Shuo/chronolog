---
card_id: claude-code-2026-04-14-eb6e81
date: '2026-04-14'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1094
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-09-added-subprocess-sandboxing-with-pid-namespace-isolation-on-linux-when-claude-co|claude-code-2026-04-09-5db0ee]]'
extractor_version: fallback-v2
impact: significant
machine_hash: d88aa8f600a844a75d3bc6676aaa0e623b0afd1cd21e7df3847926c84307089c
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-01-added-defer-permission-decision-to-pretooluse-hooks-headless-sessions-can-pause|claude-code-2026-04-01-789bcb]]'
- '[[Changes/Claude Code/2026-04-02-fixed-plan-mode-in-remote-sessions-losing-track-of-the-plan-file-after-a-contain|claude-code-2026-04-02-76e8e8]]'
- '[[Changes/Claude Code/2026-04-09-added-subprocess-sandboxing-with-pid-namespace-isolation-on-linux-when-claude-co|claude-code-2026-04-09-5db0ee]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5|claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5]]'
theme: safety-privacy
type: change
---

# The model can now discover and invoke built-in slash commands like `/init`, `/re

<!-- chronolog:begin region="description" -->
The model can now discover and invoke built-in slash commands like `/init`, `/review`, and `/security-review` via the Skill tool
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> The model can now discover and invoke built-in slash commands like `/init`, `/review`, and `/security-review` via the Skill tool
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.108
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-09-added-subprocess-sandboxing-with-pid-namespace-isolation-on-linux-when-claude-co|claude-code-2026-04-09-5db0ee]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1094
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes