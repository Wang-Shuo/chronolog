---
card_id: claude-code-2026-05-07-765f8d
date: '2026-05-07'
description: 'Claude Code · 2026-05-07 · Apps and Integrations: 2 changes in v2.1.133
  — Hooks now receive the active effort level via the `effort.level` JSON input field
  and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1141
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a03660c7643de304ccb1dba3da1c41bc75aa87be35d71c0053256585b33a0c4b
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-07-765f8d
  comparison: ''
  date: '2026-05-07'
  description: 'Claude Code — v2.1.133: 2 Apps and Integrations changes'
  evidence:
  - quote: Hooks now receive the active effort level via the `effort.level` JSON input
      field and the `$CLAUDE_EFFORT` environment variable, and Bash tool commands
      can read `$CLAUDE_EFFORT`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.133
  - quote: '`claude --help` now lists `--remote-control` alongside `--remote-control-session-name-prefix`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.133
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-apps-and-integrations-changes-in-v2-1-133
  source_release: claude-code-2026-05-07-v2-1-133-github-319164825-08653677
  source_type: github_releases
  theme: apps-integrations
  title: 2 Apps and Integrations changes in v2.1.133
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-04-6-apps-and-integrations-changes-in-v2-1-128|6
  Apps and Integrations changes in v2.1.128]]'
- '[[Changes/Claude Code/2026-05-06-added-claude-code-session-id-environment-variable-to-the-bash-tool-subprocess-en|Added
  CLAUDE_CODE_SESSION_ID environment variable to the Bash tool subprocess…]]'
- '[[Changes/Claude Code/2026-05-06-3-apps-and-integrations-changes-in-v2-1-129|3
  Apps and Integrations changes in v2.1.129]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-07-v2-1-133-github-319164825-08653677|claude-code-2026-05-07-v2-1-133-github-319164825-08653677]]'
source_type: github_releases
theme: apps-integrations
title: 2 Apps and Integrations changes in v2.1.133
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Apps and Integrations changes in v2.1.133

**Claude Code** · 2026-05-07 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.133) · from [[Releases/Claude Code/claude-code-2026-05-07-v2-1-133-github-319164825-08653677|v2.1.133]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hooks now receive the active effort level via the `effort.level` JSON input field and the `$CLAUDE_EFFORT` environment variable, and Bash tool commands can read `$CLAUDE_EFFORT`

> `claude --help` now lists `--remote-control` alongside `--remote-control-session-name-prefix`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.133
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-07-improved-memory-usage-by-releasing-warm-spare-background-workers-under-memory-pr|Improved memory usage by releasing warm-spare background workers under memory pressure]] · Reliability and Performance
- [[Changes/Claude Code/2026-05-07-added-worktree-baseref-setting-fresh-head-to-choose-whether-worktree-enterworktr|Added worktree.baseRef setting (fresh  /  head) to choose whether --worktree…]] · Developer Workflow
- [[Changes/Claude Code/2026-05-07-improved-focus-mode-behavior|Improved focus mode behavior]] · Interface Experience
- [[Changes/Claude Code/2026-05-07-added-sandbox-bwrappath-and-sandbox-socatpath-managed-settings-linux-wsl-to-spec|Added sandbox.bwrapPath and sandbox.socatPath managed settings (Linux/WSL)…]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-07-added-parentsettingsbehavior-admin-tier-key-first-wins-merge-to-let-admins-opt-s|Added parentSettingsBehavior admin-tier key ('first-wins'  /  'merge') to let…]] · Enterprise and Administration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-06 · Claude Code · [[Changes/Claude Code/2026-05-06-3-apps-and-integrations-changes-in-v2-1-129|3 Apps and Integrations changes in v2.1.129]]
- Later: 2026-05-07 · Cursor · [[Changes/Cursor/2026-05-07-made-mcp-connection-behavior-more-predictable-and-added-explicit-stale-token-cle|Made MCP connection behavior more predictable, and added explicit stale token…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-07-765f8d&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-07-2-apps-and-integrations-changes-in-v2-1-133.md%0ACard%20ID%3A%20claude-code-2026-05-07-765f8d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.133%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->