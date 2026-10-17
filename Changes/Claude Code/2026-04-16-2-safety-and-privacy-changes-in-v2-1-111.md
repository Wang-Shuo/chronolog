---
card_id: claude-code-2026-04-16-d3067a
date: '2026-04-16'
description: 'Claude Code · 2026-04-16 · Safety and Privacy: 2 changes in v2.1.111
  — Read-only bash commands with glob patterns (e.g. `ls *.ts`) and commands starting
  with…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1096
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0333be5df2b3cc46c46a59d7ed994a7fcb76d2432daad606f0881ddd5d1eda7a
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-16-d3067a
  comparison: ''
  date: '2026-04-16'
  description: 'Claude Code — v2.1.111: 2 Safety and Privacy changes'
  evidence:
  - quote: Read-only bash commands with glob patterns (e.g. `ls *.ts`) and commands
      starting with `cd <project-dir> &&` no longer trigger a permission prompt
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.111
  - quote: 'Windows: permission rules with drive-letter paths are now correctly root-anchored,
      and paths differing only by drive-letter case are recognized as the same path'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.111
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-safety-and-privacy-changes-in-v2-1-111
  source_release: claude-code-2026-04-16-v2-1-111-github-309911692-a3025e78
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v2.1.111
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-13-fixed-bash-tool-suggesting-acceptedits-permission-mode-when-exiting-plan-mode-wo|Fixed
  Bash tool suggesting acceptEdits permission mode when exiting plan mode…]]'
- '[[Changes/Claude Code/2026-04-14-2-safety-and-privacy-changes-in-v2-1-108|2 Safety
  and Privacy changes in v2.1.108]]'
- '[[Changes/Claude Code/2026-04-16-added-less-permission-prompts-skill-scans-transcripts-for-common-read-only-bash|Added
  /less-permission-prompts skill]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-16-v2-1-111-github-309911692-a3025e78|claude-code-2026-04-16-v2-1-111-github-309911692-a3025e78]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v2.1.111
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v2.1.111

**Claude Code** · 2026-04-16 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.111) · from [[Releases/Claude Code/claude-code-2026-04-16-v2-1-111-github-309911692-a3025e78|v2.1.111]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Read-only bash commands with glob patterns (e.g. `ls *.ts`) and commands starting with `cd <project-dir> &&` no longer trigger a permission prompt

> Windows: permission rules with drive-letter paths are now correctly root-anchored, and paths differing only by drive-letter case are recognized as the same path

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.111
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-16-transcript-view-footer-now-shows-dump-to-scrollback-and-v-open-in-editor-shortcu|Transcript view footer now shows  (dump to scrollback) and v (open in editor)…]] · Editor Experience
- [[Changes/Claude Code/2026-04-16-3-model-support-changes-in-v2-1-111|3 Model Support changes in v2.1.111]] · Model Support
- [[Changes/Claude Code/2026-04-16-2-apps-and-integrations-changes-in-v2-1-111|2 Apps and Integrations changes in v2.1.111]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-16-auto-mode-is-now-available-for-max-subscribers-when-using-opus-4-7|Auto mode is now available for Max subscribers when using Opus 4.7]] · Model Support
- [[Changes/Claude Code/2026-04-16-windows-powershell-tool-is-progressively-rolling-out-opt-in-or-out-with-claude-c|Windows: PowerShell tool is progressively rolling out]] · Mobile and Desktop
- [[Changes/Claude Code/2026-04-16-3-interface-experience-changes-in-v2-1-111|3 Interface Experience changes in v2.1.111]] · Interface Experience
- [[Changes/Claude Code/2026-04-16-added-less-permission-prompts-skill-scans-transcripts-for-common-read-only-bash|Added /less-permission-prompts skill]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-16-2-developer-workflow-changes-in-v2-1-111|2 Developer Workflow changes in v2.1.111]] · Developer Workflow
- [[Changes/Claude Code/2026-04-16-added-ultrareview-for-running-comprehensive-code-review-in-the-cloud-using-paral|Added /ultrareview for running comprehensive code review in the cloud using…]] · Developer Workflow
- [[Changes/Claude Code/2026-04-16-auto-mode-no-longer-requires-enable-auto-mode|Auto mode no longer requires --enable-auto-mode]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-14 · Claude Code · [[Changes/Claude Code/2026-04-14-2-safety-and-privacy-changes-in-v2-1-108|2 Safety and Privacy changes in v2.1.108]]
- Later: 2026-04-17 · Claude Code · [[Changes/Claude Code/2026-04-17-6-safety-and-privacy-changes-in-v2-1-113|6 Safety and Privacy changes in v2.1.113]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-16-d3067a&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-16-2-safety-and-privacy-changes-in-v2-1-111.md%0ACard%20ID%3A%20claude-code-2026-04-16-d3067a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.111%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->