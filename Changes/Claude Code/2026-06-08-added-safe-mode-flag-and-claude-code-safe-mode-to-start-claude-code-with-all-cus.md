---
card_id: claude-code-2026-06-08-55bad2
date: '2026-06-08'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1149
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-06-hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla|claude-code-2026-06-06-931934]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 34859454cc9e9f9f09328c2e25380bda8ef5963274831ac66d8616eaa418e650
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-06-03-teams-are-the-operating-unit-for-a-department-region-or-subsidiary-this-is-what|cursor-2026-06-03-df00e8]]'
- '[[Changes/Cursor/2026-06-04-you-can-now-hand-the-local-agent-your-own-tools-by-passing-function-definitions|cursor-2026-06-04-020531]]'
- '[[Changes/Claude Code/2026-06-06-hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla|claude-code-2026-06-06-931934]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-08-v2-1-169-github-336158564-d513d69d|claude-code-2026-06-08-v2-1-169-github-336158564-d513d69d]]'
theme: safety-privacy
type: change
---

# Added `--safe-mode` flag (and `CLAUDE_CODE_SAFE_MODE`) to start Claude Code with

<!-- chronolog:begin region="description" -->
Added `--safe-mode` flag (and `CLAUDE_CODE_SAFE_MODE`) to start Claude Code with all customizations (CLAUDE.md, plugins, skills, hooks, MCP servers) disabled for troubleshooting
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `--safe-mode` flag (and `CLAUDE_CODE_SAFE_MODE`) to start Claude Code with all customizations (CLAUDE.md, plugins, skills, hooks, MCP servers) disabled for troubleshooting
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.169
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-06-hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla|claude-code-2026-06-06-931934]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1149
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes