---
card_id: github-copilot-cli-2026-06-30-7e851d
date: '2026-06-30'
description: 'GitHub Copilot CLI · 2026-06-30 · Developer Workflow: 21 changes in
  1.0.66 — Use a non-blinking block cursor during interactive sessions, restoring
  your…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2849
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0ac1c3a732207a6d14fa25bd055ecd0771420e8a82a4cfe81341239e96bdf630
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-30-7e851d
  comparison: ''
  date: '2026-06-30'
  description: 'GitHub Copilot CLI — 1.0.66: 21 Developer Workflow changes'
  evidence:
  - quote: Use a non-blinking block cursor during interactive sessions, restoring
      your terminal's default cursor on exit
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Keep LSP servers from starting twice during startup
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Terminal title updates work in more terminals
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Git commands work in sandboxed linked worktrees
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Show the current pull request link as a status-line item
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Format terminal titles with the session title and GitHub Copilot suffix
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: View LSP server logs in /lsp logs and read_agent
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Return to the prompt after cancelling attached shell commands
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Keep background git status checks from disrupting concurrent git commands
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Keep multi-line /worktree tasks intact when starting them
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Paste WSL images when Windows env vars are unavailable
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Return to the last open GitHub issue, pull request, or gist view when switching
      tabs
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: CLI git checks skip optional locks so status and branch lookups keep working
      in busy repositories
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Show merge status for each pull request in the Pull requests tab, and refresh
      the cached statuses on demand by pressing r
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Copy text to the clipboard on WSL when cmd.exe is not on PATH
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Inline images stop writing to the shell after exit
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Display descriptions for slash command subcommands
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: LSP commands and tools resolve project configs and server paths more reliably
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Use clearer icons for shell and search timeline entries
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: /worktree keeps a valid branch name exactly as typed, e.g. feature/JIRA-123,
      instead of flattening it to a slug like feature-jira-123
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: With no argument, /worktree names the branch from your uncommitted changes
      and recent conversation using your active model instead of a fixed small one
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 21-developer-workflow-changes-in-v1-0-66
  source_release: github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740
  source_type: github_releases
  theme: developer-workflow
  title: 21 Developer Workflow changes in v1.0.66
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-06-26-2-developer-workflow-changes-in-kimi-code-0-20-1|2
  Developer Workflow changes in Kimi Code 0.20.1]]'
- '[[Changes/Claude Code/2026-06-29-2-developer-workflow-changes-in-v2-1-196|2 Developer
  Workflow changes in v2.1.196]]'
- '[[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer
  Workflow changes in v0.10.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740|github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740]]'
source_type: github_releases
theme: developer-workflow
title: 21 Developer Workflow changes in v1.0.66
type: change
---

<!-- chronolog:begin region="header" -->
# 21 Developer Workflow changes in v1.0.66

**GitHub Copilot CLI** · 2026-06-30 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.66) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740|1.0.66]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Use a non-blinking block cursor during interactive sessions, restoring your terminal's default cursor on exit

> Keep LSP servers from starting twice during startup

> Terminal title updates work in more terminals

> Git commands work in sandboxed linked worktrees

> Show the current pull request link as a status-line item

> Format terminal titles with the session title and GitHub Copilot suffix

> View LSP server logs in /lsp logs and read_agent

> Return to the prompt after cancelling attached shell commands

> Keep background git status checks from disrupting concurrent git commands

> Keep multi-line /worktree tasks intact when starting them

> Paste WSL images when Windows env vars are unavailable

> Return to the last open GitHub issue, pull request, or gist view when switching tabs

> CLI git checks skip optional locks so status and branch lookups keep working in busy repositories

> Show merge status for each pull request in the Pull requests tab, and refresh the cached statuses on demand by pressing r

> Copy text to the clipboard on WSL when cmd.exe is not on PATH

> Inline images stop writing to the shell after exit

> Display descriptions for slash command subcommands

> LSP commands and tools resolve project configs and server paths more reliably

> Use clearer icons for shell and search timeline entries

> /worktree keeps a valid branch name exactly as typed, e.g. feature/JIRA-123, instead of flattening it to a slug like feature-jira-123

> With no argument, /worktree names the branch from your uncommitted changes and recent conversation using your active model instead of a fixed small one

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.66
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-30-2-editor-experience-changes-in-v1-0-66|2 Editor Experience changes in v1.0.66]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-30-voice-mode-turns-itself-off-when-the-engine-fails-to-start-at-boot|Voice mode turns itself off when the engine fails to start at boot]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-06-30-perform-tokenizer-warmup-in-parallel-on-a-background-thread-for-better-startup-p|Perform tokenizer warmup in parallel on a background thread for better startup performance]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-30-2-collaboration-changes-in-v1-0-66|2 Collaboration changes in v1.0.66]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-06-30-pr-auto-now-starts-a-self-paced-loop-that-fixes-one-thing-per-run-and-paces-itse|/pr auto now starts a self-paced loop that fixes one thing per run and paces itself…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-30-3-interface-experience-changes-in-v1-0-66|3 Interface Experience changes in v1.0.66]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-30-9-apps-and-integrations-changes-in-v1-0-66|9 Apps and Integrations changes in v1.0.66]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-30-match-the-terminal-text-color-to-the-github-theme-canvas|Match the terminal text color to the GitHub theme canvas]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-06-30-6-account-and-access-changes-in-v1-0-66|6 Account and Access changes in v1.0.66]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-30-configure-subagent-concurrency-and-depth-limits-in-settings-usage-based-billing|Configure subagent concurrency and depth limits in /settings (usage-based billing users)]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-06-30-2-mobile-and-desktop-changes-in-v1-0-66|2 Mobile and Desktop changes in v1.0.66]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-06-30-3-safety-and-privacy-changes-in-v1-0-66|3 Safety and Privacy changes in v1.0.66]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-30-recover-corrupted-session-history-on-load|Recover corrupted session history on load]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-06-30-8-agent-mode-changes-in-v1-0-66|8 Agent Mode changes in v1.0.66]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-30-keep-session-store-searches-and-context-lookups-responsive|Keep session-store searches and context lookups responsive]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-30-5-model-support-changes-in-v1-0-66|5 Model Support changes in v1.0.66]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-30-33-other-changes-in-v1-0-66|33 other changes in v1.0.66]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-06-29 · Open WebUI · [[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer Workflow changes in v0.10.0]]
- Later: 2026-06-30 · OpenClaw · [[Changes/OpenClaw/2026-06-30-9-developer-workflow-changes-in-v2026-6-11|9 Developer Workflow changes in v2026.6.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-30-7e851d&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-30-21-developer-workflow-changes-in-v1-0-66.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-30-7e851d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.66%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->