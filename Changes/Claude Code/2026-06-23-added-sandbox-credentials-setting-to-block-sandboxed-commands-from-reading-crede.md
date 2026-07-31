---
card_id: claude-code-2026-06-23-3d5454
date: '2026-06-23'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1164
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-23-added-mouse-click-support-to-select-menus-permission-prompts-model-config-etc-in|claude-code-2026-06-23-1c0b3a]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 87b5e686e7297005bff3114564ae9ef641fcd4412f8bdc2cc69094a5eea812b6
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-17-added-sandbox-allowappleevents-opt-in-setting-that-lets-sandboxed-commands-send|claude-code-2026-06-17-5303f3]]'
- '[[Changes/ChatGPT/2026-06-18-app-permission-controls-you-can-now-choose-when-chatgpt-asks-before-using-connec|chatgpt-2026-06-18-2159f8]]'
- '[[Changes/Claude Code/2026-06-23-added-mouse-click-support-to-select-menus-permission-prompts-model-config-etc-in|claude-code-2026-06-23-1c0b3a]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-23-v2-1-187-github-343665388-744f9775|claude-code-2026-06-23-v2-1-187-github-343665388-744f9775]]'
theme: safety-privacy
type: change
---

# Added `sandbox.credentials` setting to block sandboxed commands from reading cre

<!-- chronolog:begin region="description" -->
Added `sandbox.credentials` setting to block sandboxed commands from reading credential files and secret environment variables
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `sandbox.credentials` setting to block sandboxed commands from reading credential files and secret environment variables
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.187
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-23-added-mouse-click-support-to-select-menus-permission-prompts-model-config-etc-in|claude-code-2026-06-23-1c0b3a]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1164
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes