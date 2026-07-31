---
card_id: claude-code-2026-07-03-d5e33d
date: '2026-07-03'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1174
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-29-security-claude-mcp-list-get-no-longer-spawn-mcp-json-servers-that-a-repo-self-a|claude-code-2026-06-29-697a1f]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: cfececd57e796229d279caae1a4e19827af09129654f76fa75d255aeb61614b0
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-24-improved-sandbox-network-permission-dialog-hosts-you-allow-with-yes-are-now-reme|claude-code-2026-06-24-b762ff]]'
- '[[Changes/Claude Code/2026-06-26-fixed-external-plugins-enabled-only-by-project-claude-settings-json-not-requirin|claude-code-2026-06-26-0a16aa]]'
- '[[Changes/Claude Code/2026-06-29-security-claude-mcp-list-get-no-longer-spawn-mcp-json-servers-that-a-repo-self-a|claude-code-2026-06-29-697a1f]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-03-v2-1-200-github-348415228-64d6d68d|claude-code-2026-07-03-v2-1-200-github-348415228-64d6d68d]]'
theme: safety-privacy
type: change
---

# Changed the "default" permission mode to "Manual" across the CLI, `--help`, VS C

<!-- chronolog:begin region="description" -->
Changed the "default" permission mode to "Manual" across the CLI, `--help`, VS Code, and JetBrains; `--permission-mode manual` and `"defaultMode": "manual"` are accepted alongside `default`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Changed the "default" permission mode to "Manual" across the CLI, `--help`, VS Code, and JetBrains; `--permission-mode manual` and `"defaultMode": "manual"` are accepted alongside `default`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.200
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-29-security-claude-mcp-list-get-no-longer-spawn-mcp-json-servers-that-a-repo-self-a|claude-code-2026-06-29-697a1f]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1174
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes