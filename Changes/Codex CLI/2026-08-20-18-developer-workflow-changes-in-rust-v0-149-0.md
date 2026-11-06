---
card_id: codex-cli-2026-08-20-0bfe5e
date: '2026-08-20'
description: 'Codex CLI · 2026-08-20 · Developer Workflow: 18 changes in 0.149.0 —
  Queued messages now wake idle sessions reliably, resolve duplicate session names
  more…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1251
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1022910eea68870cca9a4336860d797e18029df260741d3c5dddc7c83d060a3d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-20-0bfe5e
  comparison: ''
  date: '2026-08-20'
  description: 'Codex CLI — 0.149.0: 18 Developer Workflow changes'
  evidence:
  - quote: 'Queued messages now wake idle sessions reliably, resolve duplicate session
      names more usefully, and preserve pasted or deferred command semantics. (#39034,
      #39385, #39604)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: Inline TUI history now remains available in Windows Terminal scrollback.
      (#39619)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: Clarified that external contributions should go through issues and design
      discussion rather than pull requests. (#39089)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38902 Honor per-environment shell variable policies @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38921 Compact successful command activity in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38942 Enforce environment-specific command policies @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39065 Limit terminal hyperlink layout to the visible viewport @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39075 Avoid redundant terminal row clears @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39092 Add a command to queue messages for existing sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39100 Avoid redundant terminal size queries during history insertion
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39122 Fail closed on deeply nested command wrappers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39159 Require approval for commands with dynamic shell words @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39311 Bind unified exec approvals to shell executables @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39524 Stop treating Git commands as inherently safe @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39588 Preserve unparsed shell wrappers in exec policy @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39602 Use in-process parsing for PowerShell command classification @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39619 Preserve inline TUI scrollback in Windows Terminal @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39631 Skip sandboxed shell commands in Guardian v2 by default @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 18-developer-workflow-changes-in-rust-v0-149-0
  source_release: codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944
  source_type: github_releases
  theme: developer-workflow
  title: 18 Developer Workflow changes in rust-v0.149.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-08-18-5-developer-workflow-changes-in-rust-v0-148-0|5
  Developer Workflow changes in rust-v0.148.0]]'
- '[[Changes/Claude Code/2026-08-19-2-developer-workflow-changes-in-v2-1-236|2 Developer
  Workflow changes in v2.1.236]]'
- '[[Changes/Claude Code/2026-08-20-2-developer-workflow-changes-in-v2-1-238|2 Developer
  Workflow changes in v2.1.238]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944|codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944]]'
source_type: github_releases
theme: developer-workflow
title: 18 Developer Workflow changes in rust-v0.149.0
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Developer Workflow changes in rust-v0.149.0

**Codex CLI** · 2026-08-20 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.149.0) · from [[Releases/Codex CLI/codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944|0.149.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Queued messages now wake idle sessions reliably, resolve duplicate session names more usefully, and preserve pasted or deferred command semantics. (#39034, #39385, #39604)

> Inline TUI history now remains available in Windows Terminal scrollback. (#39619)

> Clarified that external contributions should go through issues and design discussion rather than pull requests. (#39089)

> #38902 Honor per-environment shell variable policies @copyberry

> #38921 Compact successful command activity in the TUI @copyberry

> #38942 Enforce environment-specific command policies @copyberry

> #39065 Limit terminal hyperlink layout to the visible viewport @copyberry

> #39075 Avoid redundant terminal row clears @copyberry

> #39092 Add a command to queue messages for existing sessions @copyberry

> #39100 Avoid redundant terminal size queries during history insertion @copyberry

> #39122 Fail closed on deeply nested command wrappers @copyberry

> #39159 Require approval for commands with dynamic shell words @copyberry

> #39311 Bind unified exec approvals to shell executables @copyberry

> #39524 Stop treating Git commands as inherently safe @copyberry

> #39588 Preserve unparsed shell wrappers in exec policy @copyberry

> #39602 Use in-process parsing for PowerShell command classification @copyberry

> #39619 Preserve inline TUI scrollback in Windows Terminal @copyberry

> #39631 Skip sandboxed shell commands in Guardian v2 by default @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.149.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-20-2-reliability-and-performance-changes-in-rust-v0-149-0|2 Reliability and Performance changes in rust-v0.149.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-08-20-6-model-support-changes-in-rust-v0-149-0|6 Model Support changes in rust-v0.149.0]] · Model Support
- [[Changes/Codex CLI/2026-08-20-2-memory-and-personalization-changes-in-rust-v0-149-0|2 Memory and Personalization changes in rust-v0.149.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-08-20-39045-add-managed-gates-for-in-app-chat-and-dictation-copyberry|♯39045 Add managed gates for in-app chat and dictation @copyberry]] · Voice and Audio
- [[Changes/Codex CLI/2026-08-20-18-safety-and-privacy-changes-in-rust-v0-149-0|18 Safety and Privacy changes in rust-v0.149.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-20-9-context-window-changes-in-rust-v0-149-0|9 Context Window changes in rust-v0.149.0]] · Context Window
- [[Changes/Codex CLI/2026-08-20-2-collaboration-changes-in-rust-v0-149-0|2 Collaboration changes in rust-v0.149.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-20-5-editor-experience-changes-in-rust-v0-149-0|5 Editor Experience changes in rust-v0.149.0]] · Editor Experience
- [[Changes/Codex CLI/2026-08-20-7-mobile-and-desktop-changes-in-rust-v0-149-0|7 Mobile and Desktop changes in rust-v0.149.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-20-3-interface-experience-changes-in-rust-v0-149-0|3 Interface Experience changes in rust-v0.149.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-20-33-apps-and-integrations-changes-in-rust-v0-149-0|33 Apps and Integrations changes in rust-v0.149.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-20-8-account-and-access-changes-in-rust-v0-149-0|8 Account and Access changes in rust-v0.149.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-20-39072-persist-generated-images-through-turn-executors-copyberry|♯39072 Persist generated images through turn executors @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-20-12-agent-mode-changes-in-rust-v0-149-0|12 Agent Mode changes in rust-v0.149.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-20-39283-document-secure-devcontainer-dns-exfiltration-risk-copyberry|♯39283 Document secure devcontainer DNS exfiltration risk @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-08-20-39006-emit-api-key-turn-cost-telemetry-from-app-server-copyberry|♯39006 Emit API-key turn cost telemetry from app-server @copyberry]] · Pricing Model
- [[Changes/Codex CLI/2026-08-20-125-other-changes-in-rust-v0-149-0|125 other changes in rust-v0.149.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-08-20 · Claude Code · [[Changes/Claude Code/2026-08-20-2-developer-workflow-changes-in-v2-1-238|2 Developer Workflow changes in v2.1.238]]
- Later: 2026-08-21 · Claude Code · [[Changes/Claude Code/2026-08-21-2-developer-workflow-changes-in-v2-1-239|2 Developer Workflow changes in v2.1.239]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-20-0bfe5e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-20-18-developer-workflow-changes-in-rust-v0-149-0.md%0ACard%20ID%3A%20codex-cli-2026-08-20-0bfe5e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.149.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->