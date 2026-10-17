---
card_id: claude-code-2026-09-25-148214
date: '2026-09-25'
description: 'Claude Code · 2026-09-25 · Developer Workflow: 3 changes in v2.1.283
  — Changed prompt suggestions in the terminal to appear less often after 20 in a
  row go…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1287
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cb829fe15a9c06002c6daffc3ec1d5fa8a6de448d8d155251f4e8dc28a47c22f
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-25-148214
  comparison: ''
  date: '2026-09-25'
  description: 'Claude Code — v2.1.283: 3 Developer Workflow changes'
  evidence:
  - quote: Changed prompt suggestions in the terminal to appear less often after 20
      in a row go unused; using one brings them back
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: 'Changed the `/workflows` run list to size itself like other lists: half
      the terminal inline, and it keeps its title on screen when the prompt shows
      below'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: 'Self-hosted runner: Changed `GIT_SSL_CAINFO` and `GIT_SSL_NO_VERIFY` under
      Anthropic-managed git: the runner''s own git always verifies Anthropic''s git
      route, and warning lines say what applies where'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-developer-workflow-changes-in-v2-1-283
  source_release: claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8
  source_type: github_releases
  theme: developer-workflow
  title: 3 Developer Workflow changes in v2.1.283
  type: change
related_changes:
- '[[Changes/Cursor/2026-09-23-rollouts|Rollouts]]'
- '[[Changes/Cursor/2026-09-23-when-a-pull-request-opens-rollouts-reads-the-diff-and-the-systems-it-touches-the|Monitoring
  plans]]'
- '[[Changes/Claude Code/2026-09-24-changed-windows-wsl-managed-settings-so-an-admin-policy-that-is-present-but-inva|Changed
  Windows/WSL managed settings so an admin policy that is present but invalid…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8|claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8]]'
source_type: github_releases
theme: developer-workflow
title: 3 Developer Workflow changes in v2.1.283
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Developer Workflow changes in v2.1.283

**Claude Code** · 2026-09-25 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.283) · from [[Releases/Claude Code/claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8|v2.1.283]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changed prompt suggestions in the terminal to appear less often after 20 in a row go unused; using one brings them back

> Changed the `/workflows` run list to size itself like other lists: half the terminal inline, and it keeps its title on screen when the prompt shows below

> Self-hosted runner: Changed `GIT_SSL_CAINFO` and `GIT_SSL_NO_VERIFY` under Anthropic-managed git: the runner's own git always verifies Anthropic's git route, and warning lines say what applies where

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-25-improved-startup-claude-p-and-claude-code-remote-no-longer-load-the-interactive|Improved startup: claude -p and Claude Code Remote no longer load the interactive…]] · Agent Mode
- [[Changes/Claude Code/2026-09-25-14-apps-and-integrations-changes-in-v2-1-283|14 Apps and Integrations changes in v2.1.283]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-25-3-safety-and-privacy-changes-in-v2-1-283|3 Safety and Privacy changes in v2.1.283]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-25-improved-prompt-audit-on-claude-code-configuration-stale-paths-stale-commands-an|Improved prompt-audit on Claude Code configuration]] · Files and Data
- [[Changes/Claude Code/2026-09-25-2-context-window-changes-in-v2-1-283|2 Context Window changes in v2.1.283]] · Context Window
- [[Changes/Claude Code/2026-09-25-2-reliability-and-performance-changes-in-v2-1-283|2 Reliability and Performance changes in v2.1.283]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-25-improved-lists-in-help-hooks-copy-chrome-memory-ide-release-notes-rewind-diff-re|Improved lists in /help, /hooks, /copy, /chrome, /memory, /ide…]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-25-2-interface-experience-changes-in-v2-1-283|2 Interface Experience changes in v2.1.283]] · Interface Experience
- [[Changes/Claude Code/2026-09-25-3-model-support-changes-in-v2-1-283|3 Model Support changes in v2.1.283]] · Model Support
- [[Changes/Claude Code/2026-09-25-9-other-changes-in-v2-1-283|9 other changes in v2.1.283]] · Other changes
- [[Changes/Claude Code/2026-09-25-added-doctor-prompt-audit-also-checkup-prompt-audit-to-audit-your-claude-md-file|Added /doctor prompt-audit (also /checkup prompt-audit) to audit your CLAUDE.md…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-24 · Claude Code · [[Changes/Claude Code/2026-09-24-changed-windows-wsl-managed-settings-so-an-admin-policy-that-is-present-but-inva|Changed Windows/WSL managed settings so an admin policy that is present but invalid…]]
- Later: 2026-09-29 · Claude Code · [[Changes/Claude Code/2026-09-29-3-developer-workflow-changes-in-v2-1-285|3 Developer Workflow changes in v2.1.285]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-25-148214&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-25-3-developer-workflow-changes-in-v2-1-283.md%0ACard%20ID%3A%20claude-code-2026-09-25-148214%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.283%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->