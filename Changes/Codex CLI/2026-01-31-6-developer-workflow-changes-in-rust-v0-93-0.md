---
card_id: codex-cli-2026-01-31-63d231
date: '2026-01-31'
description: 'Codex CLI · 2026-01-31 · Developer Workflow: 6 changes in 0.93.0 — Shell
  snapshots no longer inherit stdin, avoiding hangs from startup scripts. (#9735)'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1050
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ee240bcc01382cce433c905b8940eb075ec251a7eb066de7d79743b958e49b31
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-31-63d231
  comparison: ''
  date: '2026-01-31'
  description: 'Codex CLI — 0.93.0: 6 Developer Workflow changes'
  evidence:
  - quote: Shell snapshots no longer inherit stdin, avoiding hangs from startup scripts.
      (#9735)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9359 tui: stabilize shortcut overlay snapshots on WSL @slkzgm'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10103 tui: add feature-gated /plan slash command to switch to Plan mode
      @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10222 fix: make sure the shell exists @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9735 core: prevent shell_snapshot from inheriting stdin @swordfish444'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10265 Hide /approvals from the slash-command list @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-developer-workflow-changes-in-rust-v0-93-0
  source_release: codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8
  source_type: github_releases
  theme: developer-workflow
  title: 6 Developer Workflow changes in rust-v0.93.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-01-29-add-lsp-language-server-protocol-tool-for-code-intelligence-requires-staff-flag|Add
  LSP (Language Server Protocol) tool for code intelligence (requires staff flag)]]'
- '[[Changes/Claude Code/2026-01-30-2-developer-workflow-changes-in-v2-1-27|2 Developer
  Workflow changes in v2.1.27]]'
- '[[Changes/GitHub Copilot CLI/2026-01-30-3-developer-workflow-changes-in-v0-0-400|3
  Developer Workflow changes in v0.0.400]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8|codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8]]'
source_type: github_releases
theme: developer-workflow
title: 6 Developer Workflow changes in rust-v0.93.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Developer Workflow changes in rust-v0.93.0

**Codex CLI** · 2026-01-31 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.93.0) · from [[Releases/Codex CLI/codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8|0.93.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Shell snapshots no longer inherit stdin, avoiding hangs from startup scripts. (#9735)

> #9359 tui: stabilize shortcut overlay snapshots on WSL @slkzgm

> #10103 tui: add feature-gated /plan slash command to switch to Plan mode @charley-oai

> #10222 fix: make sure the shell exists @jif-oai

> #9735 core: prevent shell_snapshot from inheriting stdin @swordfish444

> #10265 Hide /approvals from the slash-command list @pakrym-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.93.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-31-6-context-window-changes-in-rust-v0-93-0|6 Context Window changes in rust-v0.93.0]] · Context Window
- [[Changes/Codex CLI/2026-01-31-6-memory-and-personalization-changes-in-rust-v0-93-0|6 Memory and Personalization changes in rust-v0.93.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-01-31-10191-chore-app-server-document-authmode-owenlin0|♯10191 chore(app-server): document AuthMode @owenlin0]] · Files and Data
- [[Changes/Codex CLI/2026-01-31-10011-really-fix-pwd-for-windows-codex-zip-iceweasel-oai|♯10011 really fix pwd for windows codex zip @iceweasel-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-31-9654-show-oauth-error-descriptions-in-callback-responses-blevy-oai|♯9654 Show OAuth error descriptions in callback responses @blevy-oai]] · Account and Access
- [[Changes/Codex CLI/2026-01-31-3-interface-experience-changes-in-rust-v0-93-0|3 Interface Experience changes in rust-v0.93.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-31-3-reliability-and-performance-changes-in-rust-v0-93-0|3 Reliability and Performance changes in rust-v0.93.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-01-31-10118-codex-cli-show-model-capacity-guidance-on-429-ccy-oai|♯10118 CodexCLI Show model-capacity guidance on 429 @ccy-oai]] · Model Support
- [[Changes/Codex CLI/2026-01-31-10030-clarify-external-editor-env-var-message-joshka-oai|♯10030 Clarify external editor env var message @joshka-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-01-31-smart-approvals-are-now-enabled-by-default-with-explicit-approval-prompts-for-mc|Smart approvals are now enabled by default, with explicit approval prompts for MCP…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-31-4-safety-and-privacy-changes-in-rust-v0-93-0|4 Safety and Privacy changes in rust-v0.93.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-31-14-apps-and-integrations-changes-in-rust-v0-93-0|14 Apps and Integrations changes in rust-v0.93.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-31-3-search-and-browsing-changes-in-rust-v0-93-0|3 Search and Browsing changes in rust-v0.93.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-01-31-added-apps-to-browse-connectors-in-tui-and-insertion-for-app-prompts-9728|Added /apps to browse connectors in TUI and $ insertion for app prompts]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-31-97-other-changes-in-rust-v0-93-0|97 other changes in rust-v0.93.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-01-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-01-30-3-developer-workflow-changes-in-v0-0-400|3 Developer Workflow changes in v0.0.400]]
- Later: 2026-02-03 · Claude Code · [[Changes/Claude Code/2026-02-03-2-developer-workflow-changes-in-v2-1-30|2 Developer Workflow changes in v2.1.30]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-31-63d231&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-31-6-developer-workflow-changes-in-rust-v0-93-0.md%0ACard%20ID%3A%20codex-cli-2026-01-31-63d231%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.93.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->