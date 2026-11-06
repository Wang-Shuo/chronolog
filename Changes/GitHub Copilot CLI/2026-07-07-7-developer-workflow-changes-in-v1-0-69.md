---
card_id: github-copilot-cli-2026-07-07-2cc2b1
date: '2026-07-07'
description: 'GitHub Copilot CLI · 2026-07-07 · Developer Workflow: 7 changes in 1.0.69
  — Show disabled servers as disabled in /lsp test'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1207
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7272f3fdb55fe0b6f756c4c1c247b08fcfc3d0a7f14474432c85dd5ee7c66c13
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-07-07-2cc2b1
  comparison: ''
  date: '2026-07-07'
  description: 'GitHub Copilot CLI — 1.0.69: 7 Developer Workflow changes'
  evidence:
  - quote: Show disabled servers as disabled in /lsp test
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Auto-approval timeline entries now include the request subject, such as
      the command, path, URL, or tool name
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Show plain Shift+Enter in /terminal-setup output
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Collect debug logs without truncating large files or dropping multiline
      secrets
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Find PRs from worktree branches when the local branch name differs from
      the PR head ref
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Allow WSL UNC paths for local files in the CLI
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  - quote: Wrap clipboard writes in tmux passthrough so copy reaches the outer terminal
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.69
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 7-developer-workflow-changes-in-v1-0-69
  source_release: github-copilot-cli-2026-07-07-v1-0-69-github-350582031-19558357
  source_type: github_releases
  theme: developer-workflow
  title: 7 Developer Workflow changes in v1.0.69
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-06-changed-review-pr-back-to-a-fast-single-pass-review-use-code-review-level-pr-for|Changed
  /review pr back to a fast single-pass review]]'
- '[[Changes/OpenHands/2026-07-06-feat-add-full-git-history-user-setting-by-malhotra5-in-https-github-com-openhand|feat:
  Add full Git history user setting]]'
- '[[Changes/Claude Code/2026-07-07-removed-the-startup-claude-command-missing-or-broken-warnings-they-now-appear-in|Removed
  the startup "claude command missing or broken" warnings]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-07-v1-0-69-github-350582031-19558357|github-copilot-cli-2026-07-07-v1-0-69-github-350582031-19558357]]'
source_type: github_releases
theme: developer-workflow
title: 7 Developer Workflow changes in v1.0.69
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Developer Workflow changes in v1.0.69

**GitHub Copilot CLI** · 2026-07-07 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.69) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-07-v1-0-69-github-350582031-19558357|1.0.69]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Show disabled servers as disabled in /lsp test

> Auto-approval timeline entries now include the request subject, such as the command, path, URL, or tool name

> Show plain Shift+Enter in /terminal-setup output

> Collect debug logs without truncating large files or dropping multiline secrets

> Find PRs from worktree branches when the local branch name differs from the PR head ref

> Allow WSL UNC paths for local files in the CLI

> Wrap clipboard writes in tmux passthrough so copy reaches the outer terminal

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.69
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-07-07-8-safety-and-privacy-changes-in-v1-0-69|8 Safety and Privacy changes in v1.0.69]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-07-07-6-model-support-changes-in-v1-0-69|6 Model Support changes in v1.0.69]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-07-07-warn-when-static-context-uses-most-of-the-prompt-budget-and-block-requests-when|Warn when static context uses most of the prompt budget and block requests…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-07-07-6-account-and-access-changes-in-v1-0-69|6 Account and Access changes in v1.0.69]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-07-07-5-reliability-and-performance-changes-in-v1-0-69|5 Reliability and Performance changes in v1.0.69]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-07-07-3-mobile-and-desktop-changes-in-v1-0-69|3 Mobile and Desktop changes in v1.0.69]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-07-07-2-editor-experience-changes-in-v1-0-69|2 Editor Experience changes in v1.0.69]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-07-07-keep-session-resume-working-when-token-timing-includes-fractional-milliseconds|Keep session resume working when token timing includes fractional milliseconds]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-07-07-improve-chronicle-cost-tips-with-more-precise-evidence-backed-recommendations|Improve /chronicle cost-tips with more precise evidence-backed recommendations]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-07-07-double-press-esc-now-interrupts-the-running-main-turn-flushing-queued-messages-o|Double-press Esc now interrupts the running main turn (flushing queued messages)…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-07-07-5-interface-experience-changes-in-v1-0-69|5 Interface Experience changes in v1.0.69]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-07-07-7-apps-and-integrations-changes-in-v1-0-69|7 Apps and Integrations changes in v1.0.69]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-07-07-24-other-changes-in-v1-0-69|24 other changes in v1.0.69]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-07-07 · Claude Code · [[Changes/Claude Code/2026-07-07-removed-the-startup-claude-command-missing-or-broken-warnings-they-now-appear-in|Removed the startup "claude command missing or broken" warnings]]
- Later: 2026-07-08 · Codex CLI · [[Changes/Codex CLI/2026-07-08-7-developer-workflow-changes-in-rust-v0-143-0|7 Developer Workflow changes in rust-v0.143.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-07-07-2cc2b1&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-07-07-7-developer-workflow-changes-in-v1-0-69.md%0ACard%20ID%3A%20github-copilot-cli-2026-07-07-2cc2b1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.69%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->