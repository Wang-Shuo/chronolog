---
card_id: github-copilot-cli-2026-05-05-068cc7
date: '2026-05-05'
description: 'GitHub Copilot CLI · 2026-05-05 · Editor Experience: 4 changes in 1.0.41
  — Shell completions (bash, zsh, fish) are automatically installed on first run and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1148
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5419aa4342f494ea127762beadb5a75bb84a7517f8e50c066498d7254b839ed7
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-05-05-068cc7
  comparison: ''
  date: '2026-05-05'
  description: 'GitHub Copilot CLI — 1.0.41: 4 Editor Experience changes'
  evidence:
  - quote: Shell completions (bash, zsh, fish) are automatically installed on first
      run and updated after `copilot update`
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.41
  - quote: Tab-completing slash commands that accept arguments now adds a trailing
      space automatically
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.41
  - quote: '@-mention completion works for ./ paths, no longer adds trailing space
      on directories, and shows project files before workspace roots'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.41
  - quote: Improve reliability of file edits by better recovering from fuzzy or misaligned
      edit blocks
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.41
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-editor-experience-changes-in-v1-0-41
  source_release: github-copilot-cli-2026-05-05-v1-0-41-github-318057614-7319e863
  source_type: github_releases
  theme: editor-experience
  title: 4 Editor Experience changes in v1.0.41
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-04-30-20045-fix-plan-mode-nudge-test-after-task-completion-signature-change-canvrno-oa|♯20045
  Fix plan mode nudge test after task completion signature change @canvrno-oai]]'
- '[[Changes/Claude Code/2026-05-01-powershell-tool-bare-e-g-git-diff-file-is-no-longer-mis-flagged-as-the-stop-pars|PowerShell
  tool: bare -- (e.g. git diff -- file) is no longer mis-flagged…]]'
- '[[Changes/Cursor/2026-05-04-updated-usage-analytics-tab|Updated usage analytics
  tab]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-05-v1-0-41-github-318057614-7319e863|github-copilot-cli-2026-05-05-v1-0-41-github-318057614-7319e863]]'
source_type: github_releases
theme: editor-experience
title: 4 Editor Experience changes in v1.0.41
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Editor Experience changes in v1.0.41

**GitHub Copilot CLI** · 2026-05-05 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.41) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-05-v1-0-41-github-318057614-7319e863|1.0.41]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Shell completions (bash, zsh, fish) are automatically installed on first run and updated after `copilot update`

> Tab-completing slash commands that accept arguments now adds a trailing space automatically

> @-mention completion works for ./ paths, no longer adds trailing space on directories, and shows project files before workspace roots

> Improve reliability of file edits by better recovering from fuzzy or misaligned edit blocks

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.41
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-05-05-add-experimental-mcp-tasks-support-mcp-tools-with-tasksupport-required-run-as-no|Add experimental MCP Tasks support]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-05-05-package-extraction-no-longer-crashes-on-windows-when-antivirus-or-filesystem-loc|Package extraction no longer crashes on Windows when antivirus or filesystem locks…]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-05-05-cli-starts-faster-by-rendering-the-ui-immediately-while-authentication-resolves|CLI starts faster by rendering the UI immediately while authentication resolves…]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-05-05-improve-stability-on-windows-by-working-around-a-v8-crash-in-node-24-x|Improve stability on Windows by working around a V8 crash in Node 24.x]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-05-05-2-interface-experience-changes-in-v1-0-41|2 Interface Experience changes in v1.0.41]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-05-05-2-apps-and-integrations-changes-in-v1-0-41|2 Apps and Integrations changes in v1.0.41]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-05-05-add-attachment-flag-in-non-interactive-p-prompt-mode-to-attach-files-images-or-n|Add --attachment flag in non-interactive (-p/--prompt) mode to attach files…]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-05-05-memory-tool-confirmation-prompt-now-shows-the-scope-repository-or-user-when-requ|Memory tool confirmation prompt now shows the scope (repository or user)…]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-05-05-7-other-changes-in-v1-0-41|7 other changes in v1.0.41]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-05-04 · Cursor · [[Changes/Cursor/2026-05-04-updated-usage-analytics-tab|Updated usage analytics tab]]
- Later: 2026-05-07 · Codex CLI · [[Changes/Codex CLI/2026-05-07-4-editor-experience-changes-in-rust-v0-129-0|4 Editor Experience changes in rust-v0.129.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-05-05-068cc7&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-05-05-4-editor-experience-changes-in-v1-0-41.md%0ACard%20ID%3A%20github-copilot-cli-2026-05-05-068cc7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.41%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->