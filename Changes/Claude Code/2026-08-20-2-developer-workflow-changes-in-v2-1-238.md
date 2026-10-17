---
card_id: claude-code-2026-08-20-66355c
date: '2026-08-20'
description: 'Claude Code · 2026-08-20 · Developer Workflow: 2 changes in v2.1.238
  — Added a `keybindingFlavor` setting: set it to `"readline"` to make Ctrl+W in the
  prompt…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1251
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a1f7cf9bd04816bd593ba4d0ee7453923f835d1efac6b7e4aaa7e31c62bd851a
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-20-66355c
  comparison: ''
  date: '2026-08-20'
  description: 'Claude Code — v2.1.238: 2 Developer Workflow changes'
  evidence:
  - quote: 'Added a `keybindingFlavor` setting: set it to `"readline"` to make Ctrl+W
      in the prompt delete back to the previous whitespace, as in Bash; the default
      (`"classic"`) is unchanged'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
  - quote: Added `claude self-hosted-runner --proxy-authorization-command` / `--proxy-authorization-file`
      for egress proxies that require a freshly issued `Proxy-Authorization` header
      on every connection
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-developer-workflow-changes-in-v2-1-238
  source_release: claude-code-2026-08-20-v2-1-238-github-373927029-c96744e2
  source_type: github_releases
  theme: developer-workflow
  title: 2 Developer Workflow changes in v2.1.238
  type: change
related_changes:
- '[[Changes/Cursor/2026-08-13-build-history-and-debugging|Build history and debugging]]'
- '[[Changes/Claude Code/2026-08-14-added-gitlab-merge-request-url-support-to-the-worktree-flag-and-the-claude-agent|Added
  GitLab merge request URL support to the --worktree flag…]]'
- '[[Changes/Claude Code/2026-08-19-2-developer-workflow-changes-in-v2-1-236|2 Developer
  Workflow changes in v2.1.236]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-20-v2-1-238-github-373927029-c96744e2|claude-code-2026-08-20-v2-1-238-github-373927029-c96744e2]]'
source_type: github_releases
theme: developer-workflow
title: 2 Developer Workflow changes in v2.1.238
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Developer Workflow changes in v2.1.238

**Claude Code** · 2026-08-20 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.238) · from [[Releases/Claude Code/claude-code-2026-08-20-v2-1-238-github-373927029-c96744e2|v2.1.238]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a `keybindingFlavor` setting: set it to `"readline"` to make Ctrl+W in the prompt delete back to the previous whitespace, as in Bash; the default (`"classic"`) is unchanged

> Added `claude self-hosted-runner --proxy-authorization-command` / `--proxy-authorization-file` for egress proxies that require a freshly issued `Proxy-Authorization` header on every connection

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.238
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-20-updated-the-bundled-claude-api-skill-for-the-managed-agents-aug-19-release-web-s|Updated the bundled claude-api skill for the Managed Agents Aug 19 release]] · Memory and Personalization
- [[Changes/Claude Code/2026-08-20-6-apps-and-integrations-changes-in-v2-1-238|6 Apps and Integrations changes in v2.1.238]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-20-improved-startup-bare-claude-starts-sooner-on-macos|Improved startup: bare claude starts sooner on macOS]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-20-3-safety-and-privacy-changes-in-v2-1-238|3 Safety and Privacy changes in v2.1.238]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-20-improved-startup-responsiveness-the-automatic-update-check-now-runs-about-10-sec|Improved startup responsiveness]] · Reliability and Performance
- [[Changes/Claude Code/2026-08-20-changed-ctrl-l-and-cmd-k-in-fullscreen-to-always-just-repaint-the-double-press-c|Changed Ctrl+L and Cmd+K in fullscreen to always just repaint]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-08-19 · Claude Code · [[Changes/Claude Code/2026-08-19-2-developer-workflow-changes-in-v2-1-236|2 Developer Workflow changes in v2.1.236]]
- Later: 2026-08-21 · Claude Code · [[Changes/Claude Code/2026-08-21-2-developer-workflow-changes-in-v2-1-239|2 Developer Workflow changes in v2.1.239]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-20-66355c&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-20-2-developer-workflow-changes-in-v2-1-238.md%0ACard%20ID%3A%20claude-code-2026-08-20-66355c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.238%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->