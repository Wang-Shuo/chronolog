---
card_id: claude-code-2026-03-26-cf3617
date: '2026-03-26'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1075
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-25-added-sandbox-failifunavailable-setting-to-exit-with-an-error-when-sandbox-is-en|claude-code-2026-03-25-7d730c]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 5e9f14b7adadf3d9ba38a33a8650d8e19c4c742a2ba74ecc7b5906758dff6cb8
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-20-added-channels-permission-relay-channel-servers-that-declare-the-permission-capa|claude-code-2026-03-20-35235c]]'
- '[[Changes/Claude Code/2026-03-20-fixed-unnecessary-permission-prompts-for-bash-commands-containing-dashes-in-stri|claude-code-2026-03-20-c0b999]]'
- '[[Changes/Claude Code/2026-03-25-added-sandbox-failifunavailable-setting-to-exit-with-an-error-when-sandbox-is-en|claude-code-2026-03-25-7d730c]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-85-github-302129484-6eb9dcd7|claude-code-2026-03-26-v2-1-85-github-302129484-6eb9dcd7]]'
theme: safety-privacy
type: change
---

# Added conditional `if` field for hooks using permission rule syntax (e.g., `Bash

<!-- chronolog:begin region="description" -->
Added conditional `if` field for hooks using permission rule syntax (e.g., `Bash(git *)`) to filter when they run, reducing process spawning overhead
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added conditional `if` field for hooks using permission rule syntax (e.g., `Bash(git *)`) to filter when they run, reducing process spawning overhead
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.85
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-25-added-sandbox-failifunavailable-setting-to-exit-with-an-error-when-sandbox-is-en|claude-code-2026-03-25-7d730c]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1075
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes