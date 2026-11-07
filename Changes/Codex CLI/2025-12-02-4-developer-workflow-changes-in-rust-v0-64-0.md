---
card_id: codex-cli-2025-12-02-d6ba32
date: '2025-12-02'
description: 'Codex CLI · 2025-12-02 · Developer Workflow: 4 changes in 0.64.0 — TTY
  stdin is required, WSL clipboard paths are normalized, and stale conversations are…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2639
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8f02d819b65b7c74c080d9dc788fba379211578c022779ca547bb4bfadce409a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-12-02-d6ba32
  comparison: ''
  date: '2025-12-02'
  description: 'Codex CLI — 0.64.0: 4 Developer Workflow changes'
  evidence:
  - quote: TTY stdin is required, WSL clipboard paths are normalized, and stale conversations
      are dropped on /new to avoid conflicts.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: Custom prompt expansion with large pastes is fixed, example-config mistakes
      are corrected, and relative links and streamable_shell references are cleaned
      up. Upgrade messaging is corrected.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'Documentation is refreshed: approvals and config guidance, codex max and
      xhigh defaults, example-config fixes, CLA guidance, and removal of streamable_shell
      references.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'Removed streamable_shell from docs by @etraut-openai in #7235'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-developer-workflow-changes-in-rust-v0-64-0
  source_release: codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886
  source_type: github_releases
  theme: developer-workflow
  title: 4 Developer Workflow changes in rust-v0.64.0
  type: change
related_changes:
- '[[Changes/Dify/2025-11-26-3-developer-workflow-changes-in-1-10-1|3 Developer Workflow
  changes in 1.10.1]]'
- '[[Changes/Gemini CLI/2025-11-26-feat-add-click-to-focus-support-for-interactive-shell-by-galz10-in-https-github|feat:
  add click-to-focus support for interactive shell]]'
- '[[Changes/Cline/2025-12-02-2-developer-workflow-changes-in-v3-39-0|2 Developer
  Workflow changes in v3.39.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886|codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886]]'
source_type: github_releases
theme: developer-workflow
title: 4 Developer Workflow changes in rust-v0.64.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Developer Workflow changes in rust-v0.64.0

**Codex CLI** · 2025-12-02 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.64.0) · from [[Releases/Codex CLI/codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886|0.64.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> TTY stdin is required, WSL clipboard paths are normalized, and stale conversations are dropped on /new to avoid conflicts.

> Custom prompt expansion with large pastes is fixed, example-config mistakes are corrected, and relative links and streamable_shell references are cleaned up. Upgrade messaging is corrected.

> Documentation is refreshed: approvals and config guidance, codex max and xhigh defaults, example-config fixes, CLA guidance, and removal of streamable_shell references.

> Removed streamable_shell from docs by @etraut-openai in #7235

Source: https://github.com/openai/codex/releases/tag/rust-v0.64.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-12-02-2-model-support-changes-in-rust-v0-64-0|2 Model Support changes in rust-v0.64.0]] · Model Support
- [[Changes/Codex CLI/2025-12-02-5-context-window-changes-in-rust-v0-64-0|5 Context Window changes in rust-v0.64.0]] · Context Window
- [[Changes/Codex CLI/2025-12-02-feat-support-login-as-an-option-on-shell-tool-mcp-by-bolinfest-in-7120|feat: support login as an option on shell-tool-mcp by @bolinfest in ♯7120]] · Account and Access
- [[Changes/Codex CLI/2025-12-02-3-apps-and-integrations-changes-in-rust-v0-64-0|3 Apps and Integrations changes in rust-v0.64.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-12-02-9-safety-and-privacy-changes-in-rust-v0-64-0|9 Safety and Privacy changes in rust-v0.64.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-12-02-powershell-apply-patch-parsing-is-corrected-and-apply-patch-tests-now-cover-shel|PowerShell apply_patch parsing is corrected, and apply_patch tests now cover…]] · Agent Mode
- [[Changes/Codex CLI/2025-12-02-execution-gains-an-experimental-exp-model-unified-exec-pruning-to-limit-session|Execution gains an experimental “exp” model, unified exec pruning to limit session…]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-12-02-3-editor-experience-changes-in-rust-v0-64-0|3 Editor Experience changes in rust-v0.64.0]] · Editor Experience
- [[Changes/Codex CLI/2025-12-02-chore-dedup-unified-exec-waited-rendering-by-jif-oai-in-7256|chore: dedup unified exec "waited" rendering by @jif-oai in ♯7256]] · Interface Experience
- [[Changes/Codex CLI/2025-12-02-46-other-changes-in-rust-v0-64-0|46 other changes in rust-v0.64.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2025-12-02 · Cline · [[Changes/Cline/2025-12-02-2-developer-workflow-changes-in-v3-39-0|2 Developer Workflow changes in v3.39.0]]
- Later: 2025-12-02 · Gemini CLI · [[Changes/Gemini CLI/2025-12-02-4-developer-workflow-changes-in-v0-19-0|4 Developer Workflow changes in v0.19.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-12-02-d6ba32&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-12-02-4-developer-workflow-changes-in-rust-v0-64-0.md%0ACard%20ID%3A%20codex-cli-2025-12-02-d6ba32%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.64.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->