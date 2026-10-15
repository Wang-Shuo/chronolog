---
card_id: claude-code-2026-06-29-697a1f
date: '2026-06-29'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1170
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 0d0827e81d09526ef4095a7d2b98af7d1dce07e57f2556c849d64d6c14e9642d
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-29-697a1f
  comparison: ''
  date: '2026-06-29'
  description: 'Claude Code — v2.1.196: Security: `claude mcp list`/`get` no longer
    spawn `.mcp.json` servers that a repo self-approved via a committed `.claude/settings.json`;
    untrusted workspaces show `⏸ Pending approval`'
  evidence:
  - quote: 'Security: `claude mcp list`/`get` no longer spawn `.mcp.json` servers
      that a repo self-approved via a committed `.claude/settings.json`; untrusted
      workspaces show `⏸ Pending approval`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.196
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: security-claude-mcp-list-get-no-longer-spawn-mcp-json-servers-that-a-repo-self-a
  source_release: claude-code-2026-06-29-v2-1-196-github-346482381-e21be272
  source_type: github_releases
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  - matched_terms:
    - security
    score: 50
    theme: safety-privacy
  theme_resolution: manual-semantic-rule-v1
  title: 'Security: `claude mcp list`/`get` no longer spawn `.mcp.json` servers that
    a repo…'
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-23-added-sandbox-credentials-setting-to-block-sandboxed-commands-from-reading-crede|claude-code-2026-06-23-3d5454]]'
- '[[Changes/Claude Code/2026-06-24-improved-sandbox-network-permission-dialog-hosts-you-allow-with-yes-are-now-reme|claude-code-2026-06-24-b762ff]]'
- '[[Changes/Claude Code/2026-06-26-fixed-external-plugins-enabled-only-by-project-claude-settings-json-not-requirin|claude-code-2026-06-26-0a16aa]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-29-v2-1-196-github-346482381-e21be272|claude-code-2026-06-29-v2-1-196-github-346482381-e21be272]]'
source_type: github_releases
theme: safety-privacy
title: 'Security: claude mcp list/get no longer spawn .mcp.json servers that a repo…'
type: change
---

# Security: `claude mcp list`/`get` no longer spawn `.mcp.json` servers that a repo…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.196: Security: `claude mcp list`/`get` no longer spawn `.mcp.json` servers that a repo self-approved via a committed `.claude/settings.json`; untrusted workspaces show `⏸ Pending approval`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Security: `claude mcp list`/`get` no longer spawn `.mcp.json` servers that a repo self-approved via a committed `.claude/settings.json`; untrusted workspaces show `⏸ Pending approval`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.196
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1170
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes