---
card_id: claude-code-2026-06-29-a914be
date: '2026-06-29'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-windows-and-linux-support|cursor-2023-03-14-0021fe]]'
  lag_days: 1203
  role: follower
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-17-added-claude-client-presence-file-environment-variable-point-it-at-a-marker-file|claude-code-2026-06-17-197b9f]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: ccd9d4f65c712a3b3c662d55c60643c4425d0c5eeb7a90193642a508c02d2e86
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-06-17-this-release-introduces-updates-to-cloud-agents-in-the-agents-window-of-the-curs|cursor-2026-06-17-eb2180]]'
- '[[Changes/ChatGPT/2026-06-18-web-ios-and-android|chatgpt-2026-06-18-e449e0]]'
- '[[Changes/ChatGPT/2026-06-18-chatgpt-now-has-more-ways-to-help-with-common-questions-from-pronunciation-guida|chatgpt-2026-06-18-f650fa]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-29-v2-1-196-github-346482381-e21be272|claude-code-2026-06-29-v2-1-196-github-346482381-e21be272]]'
theme: mobile-desktop
type: change
---

# Improved background session reliability: long-running commands and workflows now

<!-- chronolog:begin region="description" -->
Improved background session reliability: long-running commands and workflows now survive the session's process being stopped, restarted, or updated — including on Windows, where background shells are handed off instead of being killed
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved background session reliability: long-running commands and workflows now survive the session's process being stopped, restarted, or updated — including on Windows, where background shells are handed off instead of being killed
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.196
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-17-added-claude-client-presence-file-environment-variable-point-it-at-a-marker-file|claude-code-2026-06-17-197b9f]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: mobile-desktop
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-14-windows-and-linux-support|cursor-2023-03-14-0021fe]]
- Lag Days: 1203
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes