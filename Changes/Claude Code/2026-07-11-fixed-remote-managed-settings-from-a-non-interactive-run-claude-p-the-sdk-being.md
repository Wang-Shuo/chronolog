---
card_id: claude-code-2026-07-11-aad6e5
date: '2026-07-11'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1182
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-11-fixed-compound-commands-with-cd-prompting-for-permission-when-the-only-output-re|claude-code-2026-07-11-4ef412]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: c51760c006d0db512de0db02c4fd4e4104fc642f6f20da083d6c07d7df3d23af
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-07-09-if-you-already-use-the-codex-app-update-it-as-usual-to-move-to-the-new-chatgpt-d|chatgpt-2026-07-09-6457ba]]'
- '[[Changes/ChatGPT/2026-07-09-on-desktop-work-can-use-local-files-and-desktop-apps-with-your-permission-the-bu|chatgpt-2026-07-09-6ac3cb]]'
- '[[Changes/Claude Code/2026-07-11-fixed-compound-commands-with-cd-prompting-for-permission-when-the-only-output-re|claude-code-2026-07-11-4ef412]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-11-v2-1-207-github-352355755-d77b8e91|claude-code-2026-07-11-v2-1-207-github-352355755-d77b8e91]]'
theme: safety-privacy
type: change
---

# Fixed remote managed settings from a non-interactive run (`claude -p`, the SDK)

<!-- chronolog:begin region="description" -->
Fixed remote managed settings from a non-interactive run (`claude -p`, the SDK) being permanently recorded as consented without ever showing the security consent dialog
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed remote managed settings from a non-interactive run (`claude -p`, the SDK) being permanently recorded as consented without ever showing the security consent dialog
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.207
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-11-fixed-compound-commands-with-cd-prompting-for-permission-when-the-only-output-re|claude-code-2026-07-11-4ef412]]
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