---
card_id: github-copilot-cli-2026-06-09-3c66b6
date: '2026-06-09'
description: 'GitHub Copilot CLI · 2026-06-09 · Developer Workflow: 6 changes in 1.0.61
  — /after and /every commands now appear in the /experimental slash command list'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1179
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8d8e7474d6b046d1af24cd48653ae431b5c7275c89b41ee5fcfc2e9d0a779f85
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-09-3c66b6
  comparison: ''
  date: '2026-06-09'
  description: 'GitHub Copilot CLI — 1.0.61: 6 Developer Workflow changes'
  evidence:
  - quote: /after and /every commands now appear in the /experimental slash command
      list
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.61
  - quote: Prevent crashes from malformed UTF-8, oversized string buffers, and terminal
      disconnect errors
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.61
  - quote: Bash tool correctly handles multi-byte UTF-8 characters (em dash, curly
      quotes, etc.) in command input
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.61
  - quote: Add /worktree command (aliased /move) to create a new git worktree and
      switch into it, moving any uncommitted changes along
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.61
  - quote: Colors render correctly in WSL and tmux sessions instead of falling back
      to a degraded palette
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.61
  - quote: Exit shell mode by pressing Esc or Ctrl+C on an empty prompt, in addition
      to Backspace
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.61
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 6-developer-workflow-changes-in-v1-0-61
  source_release: github-copilot-cli-2026-06-09-v1-0-61-github-336905979-4d0a69f2
  source_type: github_releases
  theme: developer-workflow
  title: 6 Developer Workflow changes in v1.0.61
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-06-08-7-developer-workflow-changes-in-rust-v0-138-0|7
  Developer Workflow changes in rust-v0.138.0]]'
- '[[Changes/v0/2026-06-08-pull-requests-opened-from-a-new-branch-chat-are-no-longer-titled-initialize-proj|Pull
  requests opened from a new-branch chat are no longer titled…]]'
- '[[Changes/Codex CLI/2026-06-09-release-builds-once-again-publish-separate-symbol-archives-with-line-tables-impr|Release
  builds once again publish separate symbol archives with line tables…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-09-v1-0-61-github-336905979-4d0a69f2|github-copilot-cli-2026-06-09-v1-0-61-github-336905979-4d0a69f2]]'
source_type: github_releases
theme: developer-workflow
title: 6 Developer Workflow changes in v1.0.61
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Developer Workflow changes in v1.0.61

**GitHub Copilot CLI** · 2026-06-09 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.61) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-09-v1-0-61-github-336905979-4d0a69f2|1.0.61]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> /after and /every commands now appear in the /experimental slash command list

> Prevent crashes from malformed UTF-8, oversized string buffers, and terminal disconnect errors

> Bash tool correctly handles multi-byte UTF-8 characters (em dash, curly quotes, etc.) in command input

> Add /worktree command (aliased /move) to create a new git worktree and switch into it, moving any uncommitted changes along

> Colors render correctly in WSL and tmux sessions instead of falling back to a degraded palette

> Exit shell mode by pressing Esc or Ctrl+C on an empty prompt, in addition to Backspace

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.61
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-09-2-interface-experience-changes-in-v1-0-61|2 Interface Experience changes in v1.0.61]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-09-grep-searches-in-large-monorepos-use-an-indexed-search-engine-for-significantly|Grep searches in large monorepos use an indexed search engine for significantly…]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-09-3-model-support-changes-in-v1-0-61|3 Model Support changes in v1.0.61]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-09-mcp-oauth-re-authentication-correctly-uses-the-saved-oauth-client-id-for-remote|MCP OAuth re-authentication correctly uses the saved OAuth client ID for remote servers]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-09-3-agent-mode-changes-in-v1-0-61|3 Agent Mode changes in v1.0.61]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-09-2-search-and-browsing-changes-in-v1-0-61|2 Search and Browsing changes in v1.0.61]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-06-09-use-natural-language-with-every-and-after-to-schedule-tasks-using-cron-expressio|Use natural language with /every and /after to schedule tasks using cron…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-09-4-editor-experience-changes-in-v1-0-61|4 Editor Experience changes in v1.0.61]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-09-resuming-a-local-session-with-memory-disabled-no-longer-crashes-the-ui-to-a-blan|Resuming a local session with memory disabled no longer crashes the UI to a blank screen]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-06-09-pasted-images-no-longer-leak-into-the-main-prompt-after-a-permission-dialog-clos|Pasted images no longer leak into the main prompt after a permission dialog closes]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-09-4-apps-and-integrations-changes-in-v1-0-61|4 Apps and Integrations changes in v1.0.61]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-09-8-other-changes-in-v1-0-61|8 other changes in v1.0.61]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-06-09 · Codex CLI · [[Changes/Codex CLI/2026-06-09-release-builds-once-again-publish-separate-symbol-archives-with-line-tables-impr|Release builds once again publish separate symbol archives with line tables…]]
- Later: 2026-06-10 · Claude Code · [[Changes/Claude Code/2026-06-10-2-developer-workflow-changes-in-v2-1-172|2 Developer Workflow changes in v2.1.172]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-09-3c66b6&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-09-6-developer-workflow-changes-in-v1-0-61.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-09-3c66b6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.61%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->