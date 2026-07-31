---
card_id: claude-code-2026-02-06-1233de
date: '2026-02-06'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1027
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-01-30-permissions-now-respect-content-level-ask-over-tool-level-allow-previously-allow|claude-code-2026-01-30-3cd8a3]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 4f1344f52ff87c582ea8a8c6b3458b9993a03d6aa7e56b739fb910891b5e0d06
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-01-14-fixed-security-vulnerability-where-wildcard-permission-rules-could-match-compoun|claude-code-2026-01-14-a0bfb2]]'
- '[[Changes/Claude Code/2026-01-29-fixed-per-user-temp-directory-isolation-to-prevent-permission-conflicts-on-share|claude-code-2026-01-29-fc6c51]]'
- '[[Changes/Claude Code/2026-01-30-permissions-now-respect-content-level-ask-over-tool-level-allow-previously-allow|claude-code-2026-01-30-3cd8a3]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-06-v2-1-34-github-283772587-e48b5e29|claude-code-2026-02-06-v2-1-34-github-283772587-e48b5e29]]'
theme: safety-privacy
type: change
---

# Fixed a bug where commands excluded from sandboxing (via `sandbox.excludedComman

<!-- chronolog:begin region="description" -->
Fixed a bug where commands excluded from sandboxing (via `sandbox.excludedCommands` or `dangerouslyDisableSandbox`) could bypass the Bash ask permission rule when `autoAllowBashIfSandboxed` was enabled
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed a bug where commands excluded from sandboxing (via `sandbox.excludedCommands` or `dangerouslyDisableSandbox`) could bypass the Bash ask permission rule when `autoAllowBashIfSandboxed` was enabled
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.34
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-01-30-permissions-now-respect-content-level-ask-over-tool-level-allow-previously-allow|claude-code-2026-01-30-3cd8a3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1027
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes