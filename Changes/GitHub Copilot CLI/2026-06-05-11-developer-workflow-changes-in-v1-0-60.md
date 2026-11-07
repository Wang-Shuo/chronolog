---
card_id: github-copilot-cli-2026-06-05-827bcb
date: '2026-06-05'
description: 'GitHub Copilot CLI · 2026-06-05 · Developer Workflow: 11 changes in
  1.0.60 — Screen no longer stays blank after waking from sleep inside a terminal
  multiplexer'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2824
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8f2432453b8a119f9be4633cd4bd91e51e014a58bf9672ab86847e764cb3b0d4
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-05-827bcb
  comparison: ''
  date: '2026-06-05'
  description: 'GitHub Copilot CLI — 1.0.60: 11 Developer Workflow changes'
  evidence:
  - quote: Screen no longer stays blank after waking from sleep inside a terminal
      multiplexer
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: Worktree directory uses a flat name when PR branch contains slashes (e.g.
      `cli/foo` → `.worktrees/cli-foo`)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: Status line progressively stacks across rows at narrow terminal widths
      instead of truncating elements beyond recognition
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: Clipboard operations on X11 no longer corrupt the terminal display
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: Interactive shell commands no longer hang when producing large amounts
      of output
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: Create a git worktree for a pull request directly from the pull requests
      screen
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: LSP workspace/configuration response returns the correct number of entries,
      preventing strict servers like ty from panicking
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: Wide characters (e.g. CJK) render correctly in the terminal diff view without
      visual corruption
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: Folder trust persists across git worktrees without re-prompting
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: The /init suggestion is no longer shown when running outside a git repository
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: 'Auto-link bare #number issue and PR references to the current git repository'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 11-developer-workflow-changes-in-v1-0-60
  source_release: github-copilot-cli-2026-06-05-v1-0-60-github-335046279-6a5628d4
  source_type: github_releases
  theme: developer-workflow
  title: 11 Developer Workflow changes in v1.0.60
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-06-04-6-developer-workflow-changes-in-rust-v0-137-0|6
  Developer Workflow changes in rust-v0.137.0]]'
- '[[Changes/Kimi Code/2026-06-04-3-developer-workflow-changes-in-kimi-code-0-10-0|3
  Developer Workflow changes in Kimi Code 0.10.0]]'
- '[[Changes/Devin/2026-06-05-devin-review-action-required-flags-on-prs-by-default|Devin
  Review: Action-Required Flags on PRs by Default]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-05-v1-0-60-github-335046279-6a5628d4|github-copilot-cli-2026-06-05-v1-0-60-github-335046279-6a5628d4]]'
source_type: github_releases
theme: developer-workflow
title: 11 Developer Workflow changes in v1.0.60
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Developer Workflow changes in v1.0.60

**GitHub Copilot CLI** · 2026-06-05 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.60) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-05-v1-0-60-github-335046279-6a5628d4|1.0.60]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Screen no longer stays blank after waking from sleep inside a terminal multiplexer

> Worktree directory uses a flat name when PR branch contains slashes (e.g. `cli/foo` → `.worktrees/cli-foo`)

> Status line progressively stacks across rows at narrow terminal widths instead of truncating elements beyond recognition

> Clipboard operations on X11 no longer corrupt the terminal display

> Interactive shell commands no longer hang when producing large amounts of output

> Create a git worktree for a pull request directly from the pull requests screen

> LSP workspace/configuration response returns the correct number of entries, preventing strict servers like ty from panicking

> Wide characters (e.g. CJK) render correctly in the terminal diff view without visual corruption

> Folder trust persists across git worktrees without re-prompting

> The /init suggestion is no longer shown when running outside a git repository

> Auto-link bare #number issue and PR references to the current git repository

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.60
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-05-add-billing-help-topic-with-an-overview-of-ai-credit-usage-features|Add billing help topic with an overview of AI credit usage features]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-06-05-show-the-mission-control-sharing-status-of-synced-sessions-in-the-session-info-v|Show the Mission Control sharing status of synced sessions in the /session info view]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-06-05-3-editor-experience-changes-in-v1-0-60|3 Editor Experience changes in v1.0.60]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-05-6-interface-experience-changes-in-v1-0-60|6 Interface Experience changes in v1.0.60]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-05-mcp-tools-added-or-removed-by-a-server-mid-turn-are-now-available-immediately-in|MCP tools added or removed by a server mid-turn are now available immediately…]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-05-mcp-oauth-re-authentication-no-longer-fails-with-an-address-in-use-error-when-a|MCP OAuth re-authentication no longer fails with an address-in-use error…]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-05-2-agent-mode-changes-in-v1-0-60|2 Agent Mode changes in v1.0.60]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-05-2-model-support-changes-in-v1-0-60|2 Model Support changes in v1.0.60]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-05-2-safety-and-privacy-changes-in-v1-0-60|2 Safety and Privacy changes in v1.0.60]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-05-10-apps-and-integrations-changes-in-v1-0-60|10 Apps and Integrations changes in v1.0.60]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-05-2-context-window-changes-in-v1-0-60|2 Context Window changes in v1.0.60]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-05-2-mobile-and-desktop-changes-in-v1-0-60|2 Mobile and Desktop changes in v1.0.60]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-06-05-15-other-changes-in-v1-0-60|15 other changes in v1.0.60]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-06-05 · Devin · [[Changes/Devin/2026-06-05-devin-review-action-required-flags-on-prs-by-default|Devin Review: Action-Required Flags on PRs by Default]]
- Later: 2026-06-05 · Kimi Code · [[Changes/Kimi Code/2026-06-05-show-unknown-command-instead-of-too-many-arguments-when-an-invalid-subcommand-is|Show "unknown command" instead of "too many arguments" when an invalid subcommand…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-05-827bcb&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-05-11-developer-workflow-changes-in-v1-0-60.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-05-827bcb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.60%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->