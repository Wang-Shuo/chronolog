---
card_id: claude-code-2026-02-10-9fba55
date: '2026-02-10'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1031
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-02-06-fixed-a-bug-where-commands-excluded-from-sandboxing-via-sandbox-excludedcommands|claude-code-2026-02-06-1233de]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: d0f972e4c4a867f09c22e6eddb0a238019003f19e63e3b68f245c66b2e6a9c2a
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-01-29-fixed-per-user-temp-directory-isolation-to-prevent-permission-conflicts-on-share|claude-code-2026-01-29-fc6c51]]'
- '[[Changes/Claude Code/2026-01-30-permissions-now-respect-content-level-ask-over-tool-level-allow-previously-allow|claude-code-2026-01-30-3cd8a3]]'
- '[[Changes/Claude Code/2026-02-06-fixed-a-bug-where-commands-excluded-from-sandboxing-via-sandbox-excludedcommands|claude-code-2026-02-06-1233de]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-10-v2-1-38-github-284624259-26f7a748|claude-code-2026-02-10-v2-1-38-github-284624259-26f7a748]]'
theme: safety-privacy
type: change
---

# Blocked writes to `.claude/skills` directory in sandbox mode

<!-- chronolog:begin region="description" -->
Blocked writes to `.claude/skills` directory in sandbox mode
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Blocked writes to `.claude/skills` directory in sandbox mode
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.38
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-02-06-fixed-a-bug-where-commands-excluded-from-sandboxing-via-sandbox-excludedcommands|claude-code-2026-02-06-1233de]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1031
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes