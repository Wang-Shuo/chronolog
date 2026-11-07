---
card_id: claude-code-2026-09-02-bb25ae
date: '2026-09-02'
description: 'Claude Code · 2026-09-02 · Safety and Privacy: 4 changes in v2.1.259
  — Added `--permission-prompts none` for unattended headless hosts: anything that
  would…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2227
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d1c6e777675451daacafd63e123fb7307af4aaabc49f97ca8c1b74524ea0a6b9
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-02-bb25ae
  comparison: ''
  date: '2026-09-02'
  description: 'Claude Code — v2.1.259: 4 Safety and Privacy changes'
  evidence:
  - quote: 'Added `--permission-prompts none` for unattended headless hosts: anything
      that would prompt is denied automatically while the active permission mode (including
      auto mode) keeps deciding'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
  - quote: Fixed concurrent sessions silently reverting each other's `~/.claude.json`
      changes — workspace trust no longer resets and MCP/project state is no longer
      lost when running many sessions at once
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
  - quote: Fixed the file edit permission dialog sometimes showing a changed line
      cut short with no indication
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
  - quote: Fixed remote and scheduled sessions doing nothing after a connector-tool
      permission prompt was approved while the session was paused
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-safety-and-privacy-changes-in-v2-1-259
  source_release: claude-code-2026-09-02-v2-1-259-github-381579834-0f335a0f
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v2.1.259
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-01-41227-use-compatible-powershell-for-elevated-windows-sandbox-commands-copyberry|♯41227
  Use compatible PowerShell for elevated Windows sandbox commands @copyberry]]'
- '[[Changes/OpenClaw/2026-09-01-7-safety-and-privacy-changes-in-v2026-8-2|7 Safety
  and Privacy changes in v2026.8.2]]'
- '[[Changes/OpenCode/2026-09-01-core-apply-patch-no-longer-emits-an-empty-move-path-in-permission-metadata|Core
  apply_patch no longer emits an empty move path in permission metadata]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-02-v2-1-259-github-381579834-0f335a0f|claude-code-2026-09-02-v2-1-259-github-381579834-0f335a0f]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v2.1.259
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v2.1.259

**Claude Code** · 2026-09-02 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.259) · from [[Releases/Claude Code/claude-code-2026-09-02-v2-1-259-github-381579834-0f335a0f|v2.1.259]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `--permission-prompts none` for unattended headless hosts: anything that would prompt is denied automatically while the active permission mode (including auto mode) keeps deciding

> Fixed concurrent sessions silently reverting each other's `~/.claude.json` changes — workspace trust no longer resets and MCP/project state is no longer lost when running many sessions at once

> Fixed the file edit permission dialog sometimes showing a changed line cut short with no indication

> Fixed remote and scheduled sessions doing nothing after a connector-tool permission prompt was approved while the session was paused

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-02-improved-terminal-resize-and-first-render-performance-for-long-responses-by-reus|Improved terminal resize and first-render performance for long responses by reusing…]] · Developer Workflow
- [[Changes/Claude Code/2026-09-02-vscode-added-an-active-quick-filter-and-a-status-filter-menu-needs-input-working|VSCode Added an Active quick filter and a status filter menu…]] · Interface Experience
- [[Changes/Claude Code/2026-09-02-5-apps-and-integrations-changes-in-v2-1-259|5 Apps and Integrations changes in v2.1.259]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-02-2-agent-mode-changes-in-v2-1-259|2 Agent Mode changes in v2.1.259]] · Agent Mode
- [[Changes/Claude Code/2026-09-02-added-recognition-of-glab-mr-create-merge-close-reopen-note-update-so-gitlab-mer|Added recognition of glab mr create/merge/close/reopen/note/update so GitLab merge…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-01 · OpenCode · [[Changes/OpenCode/2026-09-01-core-apply-patch-no-longer-emits-an-empty-move-path-in-permission-metadata|Core apply_patch no longer emits an empty move path in permission metadata]]
- Later: 2026-09-02 · Google Antigravity · [[Changes/Google Antigravity/2026-09-02-permission-prompts-again-describe-the-specific-action-being-requested-instead-of|Permission prompts again describe the specific action being requested instead…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-02-bb25ae&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-02-4-safety-and-privacy-changes-in-v2-1-259.md%0ACard%20ID%3A%20claude-code-2026-09-02-bb25ae%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.259%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->