---
card_id: claude-code-2026-04-14-705fd6
date: '2026-04-14'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  lag_days: 1076
  role: follower
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-14-added-enable-prompt-caching-1h-env-var-to-opt-into-1-hour-prompt-cache-ttl-on-ap|claude-code-2026-04-14-4bb7a3]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: fde347fcb435fd6a8a0b5f5772c3282a48691b701e714f8d1052a720b2a6a2ff
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-27-reduced-token-overhead-when-mentioning-files-with-raw-string-content-no-longer-j|claude-code-2026-03-27-09cfad]]'
- '[[Changes/Claude Code/2026-04-09-added-exclude-dynamic-system-prompt-sections-flag-to-print-mode-for-improved-cro|claude-code-2026-04-09-ea27a8]]'
- '[[Changes/Claude Code/2026-04-14-added-enable-prompt-caching-1h-env-var-to-opt-into-1-hour-prompt-cache-ttl-on-ap|claude-code-2026-04-14-4bb7a3]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5|claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5]]'
theme: context-window
type: change
---

# Added recap feature to provide context when returning to a session, configurable

<!-- chronolog:begin region="description" -->
Added recap feature to provide context when returning to a session, configurable in /config and manually invocable with /recap; force with `CLAUDE_CODE_ENABLE_AWAY_SUMMARY` if telemetry disabled.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added recap feature to provide context when returning to a session, configurable in /config and manually invocable with /recap; force with `CLAUDE_CODE_ENABLE_AWAY_SUMMARY` if telemetry disabled.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.108
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-14-added-enable-prompt-caching-1h-env-var-to-opt-into-1-hour-prompt-cache-ttl-on-ap|claude-code-2026-04-14-4bb7a3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 1076
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes