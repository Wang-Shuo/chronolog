---
card_id: claude-code-2026-04-15-980a64
date: '2026-04-15'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  lag_days: 1077
  role: follower
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-14-added-recap-feature-to-provide-context-when-returning-to-a-session-configurable|claude-code-2026-04-14-705fd6]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 056419f8c3b2a4604f2daebf514a15e6d9833a228b0d6d39905dbe6003893b9f
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-09-added-exclude-dynamic-system-prompt-sections-flag-to-print-mode-for-improved-cro|claude-code-2026-04-09-ea27a8]]'
- '[[Changes/Claude Code/2026-04-14-added-enable-prompt-caching-1h-env-var-to-opt-into-1-hour-prompt-cache-ttl-on-ap|claude-code-2026-04-14-4bb7a3]]'
- '[[Changes/Claude Code/2026-04-14-added-recap-feature-to-provide-context-when-returning-to-a-session-configurable|claude-code-2026-04-14-705fd6]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-15-v2-1-110-github-309583669-83ce1e59|claude-code-2026-04-15-v2-1-110-github-309583669-83ce1e59]]'
theme: context-window
type: change
---

# Added option to show Claude's last response as commented context in the `Ctrl+G`

<!-- chronolog:begin region="description" -->
Added option to show Claude's last response as commented context in the `Ctrl+G` external editor (enable via `/config`)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added option to show Claude's last response as commented context in the `Ctrl+G` external editor (enable via `/config`)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.110
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-14-added-recap-feature-to-provide-context-when-returning-to-a-session-configurable|claude-code-2026-04-14-705fd6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 1077
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes