---
card_id: github-copilot-cli-2026-04-23-599ff8
date: '2026-04-23'
description: 'GitHub Copilot CLI · 2026-04-23 · Other changes: 12 changes in 1.0.35
  — Session selector shows branch names, idle/in-use status, and has improved search
  with…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8d628f49790d9bdccc4d6b10033b2f9b586b675401cb00262ed949a35749f134
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-04-23-599ff8
  comparison: ''
  date: '2026-04-23'
  description: 'GitHub Copilot CLI — 1.0.35: 12 other changes'
  evidence:
  - quote: Session selector shows branch names, idle/in-use status, and has improved
      search with cursor support
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: /update and /version commands now honor your configured update channel
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Session sync prompt uses clearer labels and explains GitHub.com cross-device
      sync
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Skill slash commands (e.g. /skill-name) passed as the initial prompt via
      -i are recognized correctly on startup
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: --continue prefers resuming sessions from the current working directory
      instead of the most recently touched session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Name sessions with --name and resume them by name with --resume=<name>
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Show a helpful error message with install instructions when clipboard utilities
      (wl-clipboard or xclip) are missing on Linux
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Session token expiry during a turn is handled automatically without requiring
      you to resend your message
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Pattern-specific instruction files (.github/instructions/\*.instructions.md)
      no longer include their full body in the system prompt on every session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Extension shutdown errors no longer appear as error-level log noise on
      every session exit
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Pressing Escape on startup dialogs no longer causes race conditions
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: grep and glob tools now accept multiple search paths
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 12-other-changes-in-v1-0-35
  source_release: github-copilot-cli-2026-04-23-v1-0-35-github-312982689-0111445c
  source_type: github_releases
  theme: uncategorized
  title: 12 other changes in v1.0.35
  type: change
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-23-v1-0-35-github-312982689-0111445c|github-copilot-cli-2026-04-23-v1-0-35-github-312982689-0111445c]]'
source_type: github_releases
theme: uncategorized
title: 12 other changes in v1.0.35
type: change
---

<!-- chronolog:begin region="header" -->
# 12 other changes in v1.0.35

**GitHub Copilot CLI** · 2026-04-23 · Other changes · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.35) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-23-v1-0-35-github-312982689-0111445c|1.0.35]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Session selector shows branch names, idle/in-use status, and has improved search with cursor support

> /update and /version commands now honor your configured update channel

> Session sync prompt uses clearer labels and explains GitHub.com cross-device sync

> Skill slash commands (e.g. /skill-name) passed as the initial prompt via -i are recognized correctly on startup

> --continue prefers resuming sessions from the current working directory instead of the most recently touched session

> Name sessions with --name and resume them by name with --resume=\<name>

> Show a helpful error message with install instructions when clipboard utilities (wl-clipboard or xclip) are missing on Linux

> Session token expiry during a turn is handled automatically without requiring you to resend your message

> Pattern-specific instruction files (.github/instructions/\*.instructions.md) no longer include their full body in the system prompt on every session

> Extension shutdown errors no longer appear as error-level log noise on every session exit

> Pressing Escape on startup dialogs no longer causes race conditions

> grep and glob tools now accept multiple search paths

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.35
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-04-23-6-editor-experience-changes-in-v1-0-35|6 Editor Experience changes in v1.0.35]] · Editor Experience
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
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-04-23-599ff8&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-04-23-12-other-changes-in-v1-0-35.md%0ACard%20ID%3A%20github-copilot-cli-2026-04-23-599ff8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.35%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->