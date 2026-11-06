---
card_id: github-copilot-cli-2026-06-23-682ff9
date: '2026-06-23'
description: 'GitHub Copilot CLI · 2026-06-23 · Other changes: 42 changes in 1.0.64
  — Path access prompt shows resolved symlink targets so you can see exactly what
  access is…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 70e3e1be220a335ce7e8132902337f31507c94fc396f8a58a27a82ca22023497
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-23-682ff9
  comparison: ''
  date: '2026-06-23'
  description: 'GitHub Copilot CLI — 1.0.64: 42 other changes'
  evidence:
  - quote: Path access prompt shows resolved symlink targets so you can see exactly
      what access is being granted
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Show the pay-as-you-go additional usage budget at launch, refresh it after
      a request is rejected for hitting the additional spend limit, and show a friendly
      message when the additional usage limit is reached
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Add websocket responses support for BYOK OpenAI-compatible providers
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Preserve keystrokes typed while the CLI is still loading
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Link PR and issue references in markdown tables
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Use the GitHub theme by default and enable home tabs and prompt frame for
      all users
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Set an HTTP(S) proxy with a user setting
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Hide unsupported slash commands in remote-hosted sessions
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Add argument-hint frontmatter support for skills
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: PowerShell cmdlets (Select-String, Where-Object, ForEach-Object) no longer
      trigger spurious directory access prompts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Non-interactive prompt output now stays at column 1
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Remote export keeps running after /clear and /session info keeps the task
      URL
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Keep the cursor on the adjacent session after deleting one in the session
      selector
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Use the correct Linux libc target when resolving and auto-updating SEA
      packages on musl hosts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Keep the home session timeline visible after attaching and restoring
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: The /settings search field supports readline editing keys and cursor movement
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Show --remote-export and --no-remote-export in --help output
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Make links in markdown tables clickable
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: --continue and --resume select the most recent session for the current
      repository
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Keep truncated tool output previews valid UTF-8
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: CLI auto-updater downloads the correct musl Linux package on Alpine systems
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Copy the full last assistant turn, including multi-block responses
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Stacked diffs use the same file order as the file tree
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Make /pr status and web confirmations link to the PR's repository
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Restore later file changes when rewinding to a turn without a snapshot
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Scheduled prompts manager dialog shrinks to fit its entries
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Prevent pickers and dialogs from shifting or clipping as content loads
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Only render double tildes as strikethrough in markdown
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Allow /allow-all to work in relay sessions
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Restore clickable PR and issue links in compact timeline markdown
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: PowerShell script blocks and interpolated `$()` sub-expressions no longer
      trigger content-exclusion refusals
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Newly spawned sessions appear at the bottom of their group in the agents
      tab
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Use plain text labels instead of decorative emoji in CLI output
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Automatically follow your system light and dark mode changes
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Use semantic mascot theme colors in the CLI banner
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Let footer dialogs scroll with the timeline in unified view
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Render inline code with themed chip styling in Markdown
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Filter long streamed results correctly when content exclusion is enabled
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Show a friendly message when additional usage limit is reached
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Search tools handle Windows-style glob patterns correctly
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Prevent kill self-protection from flagging quoted pipes and paths ending
      in kill
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Remove the legacy intent-reporting tool from the CLI
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 42-other-changes-in-v1-0-64
  source_release: github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd
  source_type: github_releases
  theme: uncategorized
  title: 42 other changes in v1.0.64
  type: change
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd]]'
source_type: github_releases
theme: uncategorized
title: 42 other changes in v1.0.64
type: change
---

<!-- chronolog:begin region="header" -->
# 42 other changes in v1.0.64

**GitHub Copilot CLI** · 2026-06-23 · Other changes · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.64) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|1.0.64]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Path access prompt shows resolved symlink targets so you can see exactly what access is being granted

> Show the pay-as-you-go additional usage budget at launch, refresh it after a request is rejected for hitting the additional spend limit, and show a friendly message when the additional usage limit is reached

> Add websocket responses support for BYOK OpenAI-compatible providers

> Preserve keystrokes typed while the CLI is still loading

> Link PR and issue references in markdown tables

> Use the GitHub theme by default and enable home tabs and prompt frame for all users

> Set an HTTP(S) proxy with a user setting

> Hide unsupported slash commands in remote-hosted sessions

> Add argument-hint frontmatter support for skills

> PowerShell cmdlets (Select-String, Where-Object, ForEach-Object) no longer trigger spurious directory access prompts

> Non-interactive prompt output now stays at column 1

> Remote export keeps running after /clear and /session info keeps the task URL

> Keep the cursor on the adjacent session after deleting one in the session selector

> Use the correct Linux libc target when resolving and auto-updating SEA packages on musl hosts

> Keep the home session timeline visible after attaching and restoring

> The /settings search field supports readline editing keys and cursor movement

> Show --remote-export and --no-remote-export in --help output

> Make links in markdown tables clickable

> --continue and --resume select the most recent session for the current repository

> Keep truncated tool output previews valid UTF-8

> CLI auto-updater downloads the correct musl Linux package on Alpine systems

> Copy the full last assistant turn, including multi-block responses

> Stacked diffs use the same file order as the file tree

> Make /pr status and web confirmations link to the PR's repository

> Restore later file changes when rewinding to a turn without a snapshot

> Scheduled prompts manager dialog shrinks to fit its entries

> Prevent pickers and dialogs from shifting or clipping as content loads

> Only render double tildes as strikethrough in markdown

> Allow /allow-all to work in relay sessions

> Restore clickable PR and issue links in compact timeline markdown

> PowerShell script blocks and interpolated `$()` sub-expressions no longer trigger content-exclusion refusals

> Newly spawned sessions appear at the bottom of their group in the agents tab

> Use plain text labels instead of decorative emoji in CLI output

> Automatically follow your system light and dark mode changes

> Use semantic mascot theme colors in the CLI banner

> Let footer dialogs scroll with the timeline in unified view

> Render inline code with themed chip styling in Markdown

> Filter long streamed results correctly when content exclusion is enabled

> Show a friendly message when additional usage limit is reached

> Search tools handle Windows-style glob patterns correctly

> Prevent kill self-protection from flagging quoted pipes and paths ending in kill

> Remove the legacy intent-reporting tool from the CLI

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.64
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-23-clear-queued-tool-images-when-vision-is-disabled|Clear queued tool images when vision is disabled]] · Multimodal Input
- [[Changes/GitHub Copilot CLI/2026-06-23-9-editor-experience-changes-in-v1-0-64|9 Editor Experience changes in v1.0.64]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-23-2-account-and-access-changes-in-v1-0-64|2 Account and Access changes in v1.0.64]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-23-preserve-open-canvas-instances-across-reconnects-and-restarts|Preserve open canvas instances across reconnects and restarts]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-06-23-6-safety-and-privacy-changes-in-v1-0-64|6 Safety and Privacy changes in v1.0.64]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-23-preserve-markdown-blockquotes-in-share-exports|Preserve Markdown blockquotes in /share exports]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-06-23-show-per-model-token-totals-in-usage-and-speed-up-large-history-scans|Show per-model token totals in /usage and speed up large history scans]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-23-add-loop-alias-for-the-every-command|Add /loop alias for the /every command]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-23-add-mcp-registry-installation-for-browsing-and-installing-mcp-servers|Add /mcp registry installation for browsing and installing MCP servers]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-06-23-8-apps-and-integrations-changes-in-v1-0-64|8 Apps and Integrations changes in v1.0.64]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-23-7-model-support-changes-in-v1-0-64|7 Model Support changes in v1.0.64]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-23-6-agent-mode-changes-in-v1-0-64|6 Agent Mode changes in v1.0.64]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-23-11-interface-experience-changes-in-v1-0-64|11 Interface Experience changes in v1.0.64]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-23-15-developer-workflow-changes-in-v1-0-64|15 Developer Workflow changes in v1.0.64]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-23-4-projects-and-workspaces-changes-in-v1-0-64|4 Projects and Workspaces changes in v1.0.64]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-06-23-display-cache-write-pricing-for-models-that-omit-it|Display cache-write pricing for models that omit it]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-06-23-3-context-window-changes-in-v1-0-64|3 Context Window changes in v1.0.64]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-23-682ff9&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-23-42-other-changes-in-v1-0-64.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-23-682ff9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.64%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->