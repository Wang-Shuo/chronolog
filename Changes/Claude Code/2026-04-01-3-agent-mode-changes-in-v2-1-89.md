---
card_id: claude-code-2026-04-01-421b73
date: '2026-04-01'
description: 'Claude Code · 2026-04-01 · Agent Mode: 3 changes in v2.1.89 — Added
  `PermissionDenied` hook that fires after auto mode classifier denials — return `{retry…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1000
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c6a43f607e9d629f7b7a6b3437413681afe6b1cbd95d5f92033a0b7c89f1a079
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-01-421b73
  comparison: ''
  date: '2026-04-01'
  description: 'Claude Code — v2.1.89: 3 Agent Mode changes'
  evidence:
  - quote: 'Added `PermissionDenied` hook that fires after auto mode classifier denials
      — return `{retry: true}` to tell the model it can retry'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
  - quote: Added named subagents to `@` mention typeahead suggestions
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
  - quote: 'Auto mode: denied commands now show a notification and appear in `/permissions`
      → Recent tab where you can retry with `r`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-agent-mode-changes-in-v2-1-89
  source_release: claude-code-2026-04-01-v2-1-89-github-303967782-358023f0
  source_type: github_releases
  theme: agent-mode
  title: 3 Agent Mode changes in v2.1.89
  type: change
related_changes:
- '[[Changes/Cursor/2026-03-25-cursor-now-supports-self-hosted-cloud-agents-that-keep-your-code-and-tool-execut-e411f3|Self-hosted
  Cloud Agents]]'
- '[[Changes/Claude Code/2026-03-26-2-agent-mode-changes-in-v2-1-84|2 Agent Mode changes
  in v2.1.84]]'
- '[[Changes/Claude Code/2026-03-27-auto-mode-now-shows-unavailable-for-your-plan-when-disabled-by-plan-restrictions|Auto
  mode now shows "unavailable for your plan" when disabled by plan restrictions…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|claude-code-2026-04-01-v2-1-89-github-303967782-358023f0]]'
source_type: github_releases
theme: agent-mode
title: 3 Agent Mode changes in v2.1.89
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Agent Mode changes in v2.1.89

**Claude Code** · 2026-04-01 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.89) · from [[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|v2.1.89]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `PermissionDenied` hook that fires after auto mode classifier denials — return `{retry: true}` to tell the model it can retry

> Added named subagents to `@` mention typeahead suggestions

> Auto mode: denied commands now show a notification and appear in `/permissions` → Recent tab where you can retry with `r`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-01-3-apps-and-integrations-changes-in-v2-1-89|3 Apps and Integrations changes in v2.1.89]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-01-usage-now-hides-redundant-current-week-sonnet-only-bar-for-pro-and-enterprise-pl|/usage now hides redundant "Current week (Sonnet only)" bar for Pro and Enterprise plans]] · Model Support
- [[Changes/Claude Code/2026-04-01-changed-edit-to-work-on-files-viewed-via-bash-with-sed-n-or-cat-without-requirin|Changed Edit to work on files viewed via Bash with sed -n or cat, without…]] · Editor Experience
- [[Changes/Claude Code/2026-04-01-4-developer-workflow-changes-in-v2-1-89|4 Developer Workflow changes in v2.1.89]] · Developer Workflow
- [[Changes/Claude Code/2026-04-01-2-safety-and-privacy-changes-in-v2-1-89|2 Safety and Privacy changes in v2.1.89]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-01-changed-hook-output-over-50k-characters-to-be-saved-to-disk-with-a-file-path-pre|Changed hook output over 50K characters to be saved to disk with a file path…]] · Context Window
- [[Changes/Claude Code/2026-04-01-powershell-tool-on-windows-external-command-arguments-containing-both-a-double-q|PowerShell tool on Windows]] · Mobile and Desktop
- [[Changes/Claude Code/2026-04-01-added-claude-code-no-flicker-1-environment-variable-to-opt-into-flicker-free-alt|Added CLAUDE_CODE_NO_FLICKER=1 environment variable to opt into flicker-free…]] · Interface Experience
- [[Changes/Claude Code/2026-04-01-6-other-changes-in-v2-1-89|6 other changes in v2.1.89]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-03-27 · Claude Code · [[Changes/Claude Code/2026-03-27-auto-mode-now-shows-unavailable-for-your-plan-when-disabled-by-plan-restrictions|Auto mode now shows "unavailable for your plan" when disabled by plan restrictions…]]
- Later: 2026-04-02 · Cursor · [[Changes/Cursor/2026-04-02-4-agent-mode-changes-in-3-0|4 Agent Mode changes in 3.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-01-421b73&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-01-3-agent-mode-changes-in-v2-1-89.md%0ACard%20ID%3A%20claude-code-2026-04-01-421b73%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.89%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->