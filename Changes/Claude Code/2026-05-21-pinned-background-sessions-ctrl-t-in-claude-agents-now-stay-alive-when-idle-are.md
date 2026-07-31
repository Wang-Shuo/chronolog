---
card_id: claude-code-2026-05-21-608fad
date: '2026-05-21'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  lag_days: 1253
  role: follower
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-21-improved-auto-updater-retries-transient-network-failures-reports-specific-error|claude-code-2026-05-21-4e9152]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: dbd19228e1871254fdabd46b978c3086c0639204483d906f9fa8bf347bd9380a
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-21-improved-auto-updater-reliability-native-version-checks-and-downloads-now-retry|claude-code-2026-05-21-279dd2]]'
- '[[Changes/Claude Code/2026-05-21-improved-diff-rendering-performance-for-large-file-edits-4ddf04|claude-code-2026-05-21-4ddf04]]'
- '[[Changes/Claude Code/2026-05-21-improved-auto-updater-retries-transient-network-failures-reports-specific-error|claude-code-2026-05-21-4e9152]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-21-v2-1-147-github-327133263-73928fcd|claude-code-2026-05-21-v2-1-147-github-327133263-73928fcd]]'
theme: reliability-performance
type: change
---

# Pinned background sessions (`Ctrl+T` in `claude agents`) now stay alive when idl

<!-- chronolog:begin region="description" -->
Pinned background sessions (`Ctrl+T` in `claude agents`) now stay alive when idle, are restarted in place to apply Claude Code updates, and are shed under memory pressure only after non-pinned sessions
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Pinned background sessions (`Ctrl+T` in `claude agents`) now stay alive when idle, are restarted in place to apply Claude Code updates, and are shed under memory pressure only after non-pinned sessions
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.147
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-21-improved-auto-updater-retries-transient-network-failures-reports-specific-error|claude-code-2026-05-21-4e9152]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1253
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes