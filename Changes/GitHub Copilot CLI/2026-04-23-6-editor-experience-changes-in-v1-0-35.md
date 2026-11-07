---
card_id: github-copilot-cli-2026-04-23-0d0ec6
date: '2026-04-23'
description: 'GitHub Copilot CLI · 2026-04-23 · Editor Experience: 6 changes in 1.0.35
  — Slash commands support tab-completion for arguments and subcommands'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1136
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d333de3c1bde9202aa8f0093849bc240bcc3e4fa257efd037b308e7933e314cf
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-04-23-0d0ec6
  comparison: ''
  date: '2026-04-23'
  description: 'GitHub Copilot CLI — 1.0.35: 6 Editor Experience changes'
  evidence:
  - quote: Slash commands support tab-completion for arguments and subcommands
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Support COPILOT_GH_HOST environment variable for GitHub hostname, taking
      precedence over GH_HOST
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Press Ctrl+Y (in addition to Tab) to accept the highlighted option in completion
      popups (@-mentions, path completions, slash commands)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Shell completion notifications are not duplicated when read_bash already
      returned the result
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: User settings are now stored in ~/.copilot/settings.json, separate from
      internal state in config.json
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Transient I/O errors no longer appear as red error entries in the timeline
      when an IDE or extension disconnects
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 6-editor-experience-changes-in-v1-0-35
  source_release: github-copilot-cli-2026-04-23-v1-0-35-github-312982689-0111445c
  source_type: github_releases
  theme: editor-experience
  title: 6 Editor Experience changes in v1.0.35
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-23-config-settings-theme-editor-mode-verbose-etc-now-persist-to-claude-settings-jso|/config
  settings (theme, editor mode, verbose, etc.) now persist…]]'
- '[[Changes/Claude Code/2026-04-23-merged-cost-and-stats-into-usage-both-remain-as-typing-shortcuts-that-open-the-r|Merged
  /cost and /stats into /usage]]'
- '[[Changes/Gemini CLI/2026-04-23-chore-core-increase-codebase-investigator-turn-limits-to-50-by-abhipatel12-in-ht|chore(core):
  increase codebase investigator turn limits to 50]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-23-v1-0-35-github-312982689-0111445c|github-copilot-cli-2026-04-23-v1-0-35-github-312982689-0111445c]]'
source_type: github_releases
theme: editor-experience
title: 6 Editor Experience changes in v1.0.35
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Editor Experience changes in v1.0.35

**GitHub Copilot CLI** · 2026-04-23 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.35) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-23-v1-0-35-github-312982689-0111445c|1.0.35]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Slash commands support tab-completion for arguments and subcommands

> Support COPILOT_GH_HOST environment variable for GitHub hostname, taking precedence over GH_HOST

> Press Ctrl+Y (in addition to Tab) to accept the highlighted option in completion popups (@-mentions, path completions, slash commands)

> Shell completion notifications are not duplicated when read_bash already returned the result

> User settings are now stored in ~/.copilot/settings.json, separate from internal state in config.json

> Transient I/O errors no longer appear as red error entries in the timeline when an IDE or extension disconnects

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.35
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-04-23-tool-availability-detection-works-correctly-on-windows|Tool availability detection works correctly on Windows]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-04-23-2-account-and-access-changes-in-v1-0-35|2 Account and Access changes in v1.0.35]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-04-23-3-apps-and-integrations-changes-in-v1-0-35|3 Apps and Integrations changes in v1.0.35]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-04-23-7-agent-mode-changes-in-v1-0-35|7 Agent Mode changes in v1.0.35]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-04-23-4-interface-experience-changes-in-v1-0-35|4 Interface Experience changes in v1.0.35]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-04-23-2-context-window-changes-in-v1-0-35|2 Context Window changes in v1.0.35]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-04-23-2-model-support-changes-in-v1-0-35|2 Model Support changes in v1.0.35]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-04-23-improve-rendering-performance-when-displaying-large-amounts-of-text-in-the-timel|Improve rendering performance when displaying large amounts of text in the timeline]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-04-23-4-developer-workflow-changes-in-v1-0-35|4 Developer Workflow changes in v1.0.35]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-04-23-permission-prompts-appear-correctly-in-remote-sessions-for-the-cli-tui|Permission prompts appear correctly in remote sessions for the CLI TUI]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-04-23-12-other-changes-in-v1-0-35|12 other changes in v1.0.35]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-04-23 · Gemini CLI · [[Changes/Gemini CLI/2026-04-23-chore-core-increase-codebase-investigator-turn-limits-to-50-by-abhipatel12-in-ht|chore(core): increase codebase investigator turn limits to 50]]
- Later: 2026-04-24 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-24-2-editor-experience-changes-in-v1-0-36|2 Editor Experience changes in v1.0.36]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-04-23-0d0ec6&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-04-23-6-editor-experience-changes-in-v1-0-35.md%0ACard%20ID%3A%20github-copilot-cli-2026-04-23-0d0ec6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.35%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->