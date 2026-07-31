---
card_id: claude-code-2026-06-29-697a1f
date: '2026-06-29'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1170
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-26-fixed-external-plugins-enabled-only-by-project-claude-settings-json-not-requirin|claude-code-2026-06-26-0a16aa]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: f33cb7a1f8fc34559d7a273573ab5693a87ee9f0ffaf502b40f5925640a5ed60
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-23-added-sandbox-credentials-setting-to-block-sandboxed-commands-from-reading-crede|claude-code-2026-06-23-3d5454]]'
- '[[Changes/Claude Code/2026-06-24-improved-sandbox-network-permission-dialog-hosts-you-allow-with-yes-are-now-reme|claude-code-2026-06-24-b762ff]]'
- '[[Changes/Claude Code/2026-06-26-fixed-external-plugins-enabled-only-by-project-claude-settings-json-not-requirin|claude-code-2026-06-26-0a16aa]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-29-v2-1-196-github-346482381-e21be272|claude-code-2026-06-29-v2-1-196-github-346482381-e21be272]]'
theme: safety-privacy
type: change
---

# Security: `claude mcp list`/`get` no longer spawn `.mcp.json` servers that a rep

<!-- chronolog:begin region="description" -->
Security: `claude mcp list`/`get` no longer spawn `.mcp.json` servers that a repo self-approved via a committed `.claude/settings.json`; untrusted workspaces show `⏸ Pending approval`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Security: `claude mcp list`/`get` no longer spawn `.mcp.json` servers that a repo self-approved via a committed `.claude/settings.json`; untrusted workspaces show `⏸ Pending approval`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.196
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-26-fixed-external-plugins-enabled-only-by-project-claude-settings-json-not-requirin|claude-code-2026-06-26-0a16aa]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1170
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes