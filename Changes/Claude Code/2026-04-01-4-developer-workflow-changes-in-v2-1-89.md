---
card_id: claude-code-2026-04-01-22f9c0
date: '2026-04-01'
description: 'Claude Code · 2026-04-01 · Developer Workflow: 4 changes in v2.1.89
  — Improved Bash tool to warn when a formatter/linter command modifies files you
  have…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1110
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 710afb03851332df5602c0bef91cd52797b9be7217d2854b655e459cb5b90b80
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-01-22f9c0
  comparison: ''
  date: '2026-04-01'
  description: 'Claude Code — v2.1.89: 4 Developer Workflow changes'
  evidence:
  - quote: Improved Bash tool to warn when a formatter/linter command modifies files
      you have previously read, preventing stale-edit errors
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
  - quote: Preserved task notifications when backgrounding a running command with
      Ctrl+B
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
  - quote: '`/env` now applies to PowerShell tool commands (previously only affected
      Bash)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
  - quote: Pasting `!command` into an empty prompt now enters bash mode, matching
      typed `!` behavior
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-developer-workflow-changes-in-v2-1-89
  source_release: claude-code-2026-04-01-v2-1-89-github-303967782-358023f0
  source_type: github_releases
  theme: developer-workflow
  title: 4 Developer Workflow changes in v2.1.89
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-26-5-developer-workflow-changes-in-v2-1-84|5 Developer
  Workflow changes in v2.1.84]]'
- '[[Changes/Claude Code/2026-03-26-improved-powershell-dangerous-command-detection|Improved
  PowerShell dangerous command detection]]'
- '[[Changes/Claude Code/2026-03-27-added-x-claude-code-session-id-header-to-api-requests-so-proxies-can-aggregate-r|Added
  X-Claude-Code-Session-Id header to API requests so proxies can aggregate…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|claude-code-2026-04-01-v2-1-89-github-303967782-358023f0]]'
source_type: github_releases
theme: developer-workflow
title: 4 Developer Workflow changes in v2.1.89
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Developer Workflow changes in v2.1.89

**Claude Code** · 2026-04-01 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.89) · from [[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|v2.1.89]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved Bash tool to warn when a formatter/linter command modifies files you have previously read, preventing stale-edit errors

> Preserved task notifications when backgrounding a running command with Ctrl+B

> `/env` now applies to PowerShell tool commands (previously only affected Bash)

> Pasting `!command` into an empty prompt now enters bash mode, matching typed `!` behavior

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-01-3-apps-and-integrations-changes-in-v2-1-89|3 Apps and Integrations changes in v2.1.89]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-01-usage-now-hides-redundant-current-week-sonnet-only-bar-for-pro-and-enterprise-pl|/usage now hides redundant "Current week (Sonnet only)" bar for Pro and Enterprise plans]] · Model Support
- [[Changes/Claude Code/2026-04-01-changed-edit-to-work-on-files-viewed-via-bash-with-sed-n-or-cat-without-requirin|Changed Edit to work on files viewed via Bash with sed -n or cat, without…]] · Editor Experience
- [[Changes/Claude Code/2026-04-01-3-agent-mode-changes-in-v2-1-89|3 Agent Mode changes in v2.1.89]] · Agent Mode
- [[Changes/Claude Code/2026-04-01-2-safety-and-privacy-changes-in-v2-1-89|2 Safety and Privacy changes in v2.1.89]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-01-changed-hook-output-over-50k-characters-to-be-saved-to-disk-with-a-file-path-pre|Changed hook output over 50K characters to be saved to disk with a file path…]] · Context Window
- [[Changes/Claude Code/2026-04-01-powershell-tool-on-windows-external-command-arguments-containing-both-a-double-q|PowerShell tool on Windows]] · Mobile and Desktop
- [[Changes/Claude Code/2026-04-01-added-claude-code-no-flicker-1-environment-variable-to-opt-into-flicker-free-alt|Added CLAUDE_CODE_NO_FLICKER=1 environment variable to opt into flicker-free…]] · Interface Experience
- [[Changes/Claude Code/2026-04-01-6-other-changes-in-v2-1-89|6 other changes in v2.1.89]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-27 · Claude Code · [[Changes/Claude Code/2026-03-27-added-x-claude-code-session-id-header-to-api-requests-so-proxies-can-aggregate-r|Added X-Claude-Code-Session-Id header to API requests so proxies can aggregate…]]
- Later: 2026-04-02 · Cursor · [[Changes/Cursor/2026-04-02-2-developer-workflow-changes-in-3-0|2 Developer Workflow changes in 3.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-01-22f9c0&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-01-4-developer-workflow-changes-in-v2-1-89.md%0ACard%20ID%3A%20claude-code-2026-04-01-22f9c0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.89%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->