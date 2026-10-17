---
card_id: claude-code-2026-06-29-697a1f
date: '2026-06-29'
description: 'Claude Code · 2026-06-29 · Safety and Privacy: Security: `claude mcp
  list`/`get` no longer spawn `.mcp.json` servers that a repo self-approved via a
  committed…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1170
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 96d2da2bf14fd4ca539d1c0f8b549830a521ab83d050c96c659df6f0be8f11da
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
  extractor_version: fallback-v5
  impact: incremental
  kind: change
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
- '[[Changes/Claude Code/2026-06-23-2-safety-and-privacy-changes-in-v2-1-187|2 Safety
  and Privacy changes in v2.1.187]]'
- '[[Changes/Claude Code/2026-06-24-improved-sandbox-network-permission-dialog-hosts-you-allow-with-yes-are-now-reme|Improved
  sandbox network permission dialog]]'
- '[[Changes/Claude Code/2026-06-26-fixed-external-plugins-enabled-only-by-project-claude-settings-json-not-requirin|Fixed
  external plugins enabled only by project .claude/settings.json not requiring…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-29-v2-1-196-github-346482381-e21be272|claude-code-2026-06-29-v2-1-196-github-346482381-e21be272]]'
source_type: github_releases
theme: safety-privacy
title: 'Security: claude mcp list/get no longer spawn .mcp.json servers that a repo…'
type: change
---

<!-- chronolog:begin region="header" -->
# Security: `claude mcp list`/`get` no longer spawn `.mcp.json` servers that a repo…

**Claude Code** · 2026-06-29 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.196) · from [[Releases/Claude Code/claude-code-2026-06-29-v2-1-196-github-346482381-e21be272|v2.1.196]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Security: `claude mcp list`/`get` no longer spawn `.mcp.json` servers that a repo self-approved via a committed `.claude/settings.json`; untrusted workspaces show `⏸ Pending approval`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.196
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-29-2-agent-mode-changes-in-v2-1-196|2 Agent Mode changes in v2.1.196]] · Agent Mode
- [[Changes/Claude Code/2026-06-29-added-support-for-organization-default-models-admins-set-it-in-the-org-console-i|Added support for organization default models]] · Model Support
- [[Changes/Claude Code/2026-06-29-added-readable-default-names-for-sessions-at-start-making-them-easier-to-identif|Added readable default names for sessions at start, making them easier to identify…]] · Projects and Workspaces
- [[Changes/Claude Code/2026-06-29-2-developer-workflow-changes-in-v2-1-196|2 Developer Workflow changes in v2.1.196]] · Developer Workflow
- [[Changes/Claude Code/2026-06-29-remote-control-is-now-disabled-when-anthropic-base-url-points-at-a-non-anthropic|Remote Control is now disabled when ANTHROPIC_BASE_URL points at a non-Anthropic…]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-29-added-clickable-file-attachments-in-chat-cmd-ctrl-click-reveals-the-file-in-find|Added clickable file attachments in chat]] · Files and Data
- [[Changes/Claude Code/2026-06-29-improved-background-session-reliability-long-running-commands-and-workflows-now|Improved background session reliability]] · Mobile and Desktop
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-26 · Claude Code · [[Changes/Claude Code/2026-06-26-fixed-external-plugins-enabled-only-by-project-claude-settings-json-not-requirin|Fixed external plugins enabled only by project .claude/settings.json not requiring…]]
- Later: 2026-07-03 · Claude Code · [[Changes/Claude Code/2026-07-03-changed-the-default-permission-mode-to-manual-across-the-cli-help-vs-code-and-je|Changed the "default" permission mode to "Manual" across the CLI, --help, VS Code…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-29-697a1f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-29-security-claude-mcp-list-get-no-longer-spawn-mcp-json-servers-that-a-repo-self-a.md%0ACard%20ID%3A%20claude-code-2026-06-29-697a1f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.196%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->