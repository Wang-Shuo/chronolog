---
card_id: github-copilot-cli-2026-03-11-ce104f
date: '2026-03-11'
description: 'GitHub Copilot CLI · 2026-03-11 · Developer Workflow: 4 changes in 1.0.4
  — Add `session.shell.exec` and `session.shell.kill` RPC methods for executing shell…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1089
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 75ab1033889f16d65870e98240a95dc9749480ed18dda896da2f2b981b577c6a
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-03-11-ce104f
  comparison: ''
  date: '2026-03-11'
  description: 'GitHub Copilot CLI — 1.0.4: 4 Developer Workflow changes'
  evidence:
  - quote: Add `session.shell.exec` and `session.shell.kill` RPC methods for executing
      shell commands with streaming stdout/stderr output
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.4
  - quote: Terminal properly resets when CLI crashes, preventing shell corruption
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.4
  - quote: /update command automatically restarts to apply updates instead of requiring
      manual exit
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.4
  - quote: Interactive shell initialization no longer times out on slow machines
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-developer-workflow-changes-in-v1-0-4
  source_release: github-copilot-cli-2026-03-11-v1-0-4-github-295850245-f6b8c4f1
  source_type: github_releases
  theme: developer-workflow
  title: 4 Developer Workflow changes in v1.0.4
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-11-deprecated-output-style-command-use-config-instead-output-style-is-now-fixed-at|Deprecated
  /output-style command — use /config instead]]'
- '[[Changes/Codex CLI/2026-03-11-3-developer-workflow-changes-in-rust-v0-114-0|3
  Developer Workflow changes in rust-v0.114.0]]'
- '[[Changes/Gemini CLI/2026-03-11-code-review-fixes-as-a-pr-by-jacob314-in-https-github-com-google-gemini-gemini-c|Code
  review fixes as a pr]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-11-v1-0-4-github-295850245-f6b8c4f1|github-copilot-cli-2026-03-11-v1-0-4-github-295850245-f6b8c4f1]]'
source_type: github_releases
theme: developer-workflow
title: 4 Developer Workflow changes in v1.0.4
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Developer Workflow changes in v1.0.4

**GitHub Copilot CLI** · 2026-03-11 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.4) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-11-v1-0-4-github-295850245-f6b8c4f1|1.0.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add `session.shell.exec` and `session.shell.kill` RPC methods for executing shell commands with streaming stdout/stderr output

> Terminal properly resets when CLI crashes, preventing shell corruption

> /update command automatically restarts to apply updates instead of requiring manual exit

> Interactive shell initialization no longer times out on slow machines

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-03-11-status-line-context-window-percentage-no-longer-inflates-across-turns-by-using-t|Status line context window percentage no longer inflates across turns by using…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-03-11-2-interface-experience-changes-in-v1-0-4|2 Interface Experience changes in v1.0.4]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-03-11-2-safety-and-privacy-changes-in-v1-0-4|2 Safety and Privacy changes in v1.0.4]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-03-11-session-export-header-renders-each-field-on-its-own-line-in-shared-gists|Session export header renders each field on its own line in shared gists]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-03-11-faster-shell-commands-on-windows-by-skipping-powershell-profile-loading|Faster shell commands on Windows by skipping PowerShell profile loading]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-03-11-4-apps-and-integrations-changes-in-v1-0-4|4 Apps and Integrations changes in v1.0.4]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-03-11-3-account-and-access-changes-in-v1-0-4|3 Account and Access changes in v1.0.4]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-03-11-2-agent-mode-changes-in-v1-0-4|2 Agent Mode changes in v1.0.4]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-03-11-2-model-support-changes-in-v1-0-4|2 Model Support changes in v1.0.4]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-03-11-5-other-changes-in-v1-0-4|5 other changes in v1.0.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-11 · Gemini CLI · [[Changes/Gemini CLI/2026-03-11-code-review-fixes-as-a-pr-by-jacob314-in-https-github-com-google-gemini-gemini-c|Code review fixes as a pr]]
- Later: 2026-03-11 · OpenHands · [[Changes/OpenHands/2026-03-11-2-developer-workflow-changes-in-1-5-0|2 Developer Workflow changes in 1.5.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-03-11-ce104f&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-03-11-4-developer-workflow-changes-in-v1-0-4.md%0ACard%20ID%3A%20github-copilot-cli-2026-03-11-ce104f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->