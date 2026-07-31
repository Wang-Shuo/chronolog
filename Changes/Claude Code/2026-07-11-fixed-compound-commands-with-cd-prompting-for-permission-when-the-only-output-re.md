---
card_id: claude-code-2026-07-11-4ef412
date: '2026-07-11'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1182
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-08-background-task-notifications-now-explicitly-state-that-no-human-input-has-occur|claude-code-2026-07-08-e5045d]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: a9f1c2ac2fd556cae50a117941c15e4b46fa382fb923229f45414f1e18c5aca1
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-08-background-task-notifications-now-explicitly-state-that-no-human-input-has-occur|claude-code-2026-07-08-e5045d]]'
- '[[Changes/ChatGPT/2026-07-09-if-you-already-use-the-codex-app-update-it-as-usual-to-move-to-the-new-chatgpt-d|chatgpt-2026-07-09-6457ba]]'
- '[[Changes/ChatGPT/2026-07-09-on-desktop-work-can-use-local-files-and-desktop-apps-with-your-permission-the-bu|chatgpt-2026-07-09-6ac3cb]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-11-v2-1-207-github-352355755-d77b8e91|claude-code-2026-07-11-v2-1-207-github-352355755-d77b8e91]]'
theme: safety-privacy
type: change
---

# Fixed compound commands with `cd` prompting for permission when the only output

<!-- chronolog:begin region="description" -->
Fixed compound commands with `cd` prompting for permission when the only output redirect was to `/dev/null`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed compound commands with `cd` prompting for permission when the only output redirect was to `/dev/null`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.207
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-08-background-task-notifications-now-explicitly-state-that-no-human-input-has-occur|claude-code-2026-07-08-e5045d]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1182
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes