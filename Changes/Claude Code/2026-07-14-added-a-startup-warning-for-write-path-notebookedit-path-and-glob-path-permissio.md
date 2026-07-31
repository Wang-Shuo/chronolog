---
card_id: claude-code-2026-07-14-f07656
date: '2026-07-14'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1185
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-14-fixed-multi-second-per-turn-slowdowns-in-sessions-with-many-permission-deny-ask|claude-code-2026-07-14-df06b4]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 5be20600b3640e4dd7175c34076e98963d5d3de15c0f4e204216991b89bc9d3d
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-11-fixed-remote-managed-settings-from-a-non-interactive-run-claude-p-the-sdk-being|claude-code-2026-07-11-aad6e5]]'
- '[[Changes/Claude Code/2026-07-14-improved-auto-mode-the-permission-classifier-now-defaults-to-sonnet-5-for-extern|claude-code-2026-07-14-de216e]]'
- '[[Changes/Claude Code/2026-07-14-fixed-multi-second-per-turn-slowdowns-in-sessions-with-many-permission-deny-ask|claude-code-2026-07-14-df06b4]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-14-v2-1-210-github-354034085-7eba9ec7|claude-code-2026-07-14-v2-1-210-github-354034085-7eba9ec7]]'
theme: safety-privacy
type: change
---

# Added a startup warning for `Write(path)`, `NotebookEdit(path)`, and `Glob(path)

<!-- chronolog:begin region="description" -->
Added a startup warning for `Write(path)`, `NotebookEdit(path)`, and `Glob(path)` permission rules — use `Edit(path)` or `Read(path)` instead
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added a startup warning for `Write(path)`, `NotebookEdit(path)`, and `Glob(path)` permission rules — use `Edit(path)` or `Read(path)` instead
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.210
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-14-fixed-multi-second-per-turn-slowdowns-in-sessions-with-many-permission-deny-ask|claude-code-2026-07-14-df06b4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1185
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes