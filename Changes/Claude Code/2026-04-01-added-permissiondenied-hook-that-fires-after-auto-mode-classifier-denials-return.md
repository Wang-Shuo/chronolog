---
card_id: claude-code-2026-04-01-e43a95
date: '2026-04-01'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  lag_days: 1000
  role: follower
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-26-added-taskcreated-hook-that-fires-when-a-task-is-created-via-taskcreate|claude-code-2026-03-26-484bd3]]'
extractor_version: fallback-v2
impact: significant
machine_hash: ab0f94445049eb55f7b175069ab4dc35b0e65828a2b141201d92203e9581b25d
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-03-25-try-it-out-today-by-enabling-self-hosted-cloud-agents-in-your-cursor-dashboard-r|cursor-2026-03-25-8c41d9]]'
- '[[Changes/Cursor/2026-03-25-cursor-now-supports-self-hosted-cloud-agents-that-keep-your-code-and-tool-execut|cursor-2026-03-25-ef9cb1]]'
- '[[Changes/Claude Code/2026-03-26-added-taskcreated-hook-that-fires-when-a-task-is-created-via-taskcreate|claude-code-2026-03-26-484bd3]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|claude-code-2026-04-01-v2-1-89-github-303967782-358023f0]]'
theme: agent-mode
type: change
---

# Added `PermissionDenied` hook that fires after auto mode classifier denials — re

<!-- chronolog:begin region="description" -->
Added `PermissionDenied` hook that fires after auto mode classifier denials — return `{retry: true}` to tell the model it can retry
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `PermissionDenied` hook that fires after auto mode classifier denials — return `{retry: true}` to tell the model it can retry
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-26-added-taskcreated-hook-that-fires-when-a-task-is-created-via-taskcreate|claude-code-2026-03-26-484bd3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1000
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes