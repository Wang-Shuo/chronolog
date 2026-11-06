---
card_id: github-copilot-cli-2026-05-01-7e13c1
date: '2026-05-01'
description: 'GitHub Copilot CLI · 2026-05-01 · Other changes: 10 changes in 1.0.40
  — Assistant responses stream with smoother text output'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 35426523733bd56f3a5ceb7acc8defa429bda06ff1c897f490adef0fdfb1489a
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-05-01-7e13c1
  comparison: ''
  date: '2026-05-01'
  description: 'GitHub Copilot CLI — 1.0.40: 10 other changes'
  evidence:
  - quote: Assistant responses stream with smoother text output
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  - quote: Switching sessions with /new or /resume no longer carries over pending
      messages to the new session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  - quote: CLI no longer hangs at 100% CPU when sending a large file attachment
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  - quote: Print "Exiting…" to stderr immediately on Ctrl+C during prompt mode so
      shutdown progress is visible
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  - quote: Autopilot mode now limits continuation messages to 5 by default (configurable
      with --max-autopilot-continues)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  - quote: Automatically clean up old CLI package versions from disk during auto-update
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  - quote: /update no longer re-submits the original -i prompt after restarting
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  - quote: Skills are available as slash commands in ACP clients, matching the CLI
      experience
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  - quote: Resuming a session no longer falsely reports it as in use after a previous
      CLI process exited unexpectedly
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  - quote: Ctrl+C and double-Esc remove pending queued messages one at a time instead
      of all at once
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 10-other-changes-in-v1-0-40
  source_release: github-copilot-cli-2026-05-01-v1-0-40-github-316385532-9c4aec71
  source_type: github_releases
  theme: uncategorized
  title: 10 other changes in v1.0.40
  type: change
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-01-v1-0-40-github-316385532-9c4aec71|github-copilot-cli-2026-05-01-v1-0-40-github-316385532-9c4aec71]]'
source_type: github_releases
theme: uncategorized
title: 10 other changes in v1.0.40
type: change
---

<!-- chronolog:begin region="header" -->
# 10 other changes in v1.0.40

**GitHub Copilot CLI** · 2026-05-01 · Other changes · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.40) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-01-v1-0-40-github-316385532-9c4aec71|1.0.40]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Assistant responses stream with smoother text output

> Switching sessions with /new or /resume no longer carries over pending messages to the new session

> CLI no longer hangs at 100% CPU when sending a large file attachment

> Print "Exiting…" to stderr immediately on Ctrl+C during prompt mode so shutdown progress is visible

> Autopilot mode now limits continuation messages to 5 by default (configurable with --max-autopilot-continues)

> Automatically clean up old CLI package versions from disk during auto-update

> /update no longer re-submits the original -i prompt after restarting

> Skills are available as slash commands in ACP clients, matching the CLI experience

> Resuming a session no longer falsely reports it as in use after a previous CLI process exited unexpectedly

> Ctrl+C and double-Esc remove pending queued messages one at a time instead of all at once

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.40
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-05-01-slash-command-suggestions-rank-prefix-matches-above-fuzzy-matches|Slash command suggestions rank prefix matches above fuzzy matches]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-05-01-3-agent-mode-changes-in-v1-0-40|3 Agent Mode changes in v1.0.40]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-05-01-2-model-support-changes-in-v1-0-40|2 Model Support changes in v1.0.40]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-05-01-2-account-and-access-changes-in-v1-0-40|2 Account and Access changes in v1.0.40]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-05-01-session-history-file-tracking-and-the-chronicle-command-are-now-available-to-all|Session history, file tracking, and the /chronicle command are now available to all users]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-05-01-remote-session-statusline-shows-the-remote-working-directory-and-branch-instead|Remote session statusline shows the remote working directory and branch instead…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-05-01-improve-cli-startup-speed-by-loading-custom-ca-certificates-asynchronously|Improve CLI startup speed by loading custom CA certificates asynchronously]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-05-01-research-uses-an-orchestrator-subagent-model-for-more-thorough-and-reliable-deep|/research uses an orchestrator/subagent model for more thorough and reliable deep…]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-05-01-session-resume-selector-displays-summaries-on-a-single-line-truncated-to-fit-the|Session resume selector displays summaries on a single line, truncated to fit…]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-05-01-6-apps-and-integrations-changes-in-v1-0-40|6 Apps and Integrations changes in v1.0.40]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-05-01-3-interface-experience-changes-in-v1-0-40|3 Interface Experience changes in v1.0.40]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-05-01-7e13c1&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-05-01-10-other-changes-in-v1-0-40.md%0ACard%20ID%3A%20github-copilot-cli-2026-05-01-7e13c1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.40%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->