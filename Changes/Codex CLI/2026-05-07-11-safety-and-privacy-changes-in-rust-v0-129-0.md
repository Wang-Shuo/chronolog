---
card_id: codex-cli-2026-05-07-f3ddcf
date: '2026-05-07'
description: 'Codex CLI · 2026-05-07 · Safety and Privacy: 11 changes in 0.129.0 —
  Linux sandbox startup is more reliable across older `bwrap`, slow mount probes…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1117
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6471b34defbddff022d3d656f51b94c222985d52f98b8538dfdc4f276197dc0b
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-07-f3ddcf
  comparison: ''
  date: '2026-05-07'
  description: 'Codex CLI — 0.129.0: 11 Safety and Privacy changes'
  evidence:
  - quote: 'Linux sandbox startup is more reliable across older `bwrap`, slow mount
      probes, symlink-protected paths, and shared `/tmp` setups. (#20628, #20111,
      #21127, #21234)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: 'Windows sandbox and exec policy now handle named pipes, ConPTY teardown,
      PowerShell-wrapped allow rules, worktree `safe.directory`, and unsafe Git options
      more reliably. (#20270, #20685, #20336, #21409, #21275)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: Vendored Bubblewrap was updated to 0.11.2, including upstream security
      changes around setuid support. (#21389)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20270 [codex] Fix elevated Windows sandbox named-pipe access @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20101 install WFP filters for Windows sandbox setup @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20628 fix(linux-sandbox): fall back when system bwrap lacks perms @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20708 Add Windows sandbox readiness RPC @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21127 fix(linux-sandbox): avoid panic on bwrap build failures @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21234 fix(linux-sandbox): isolate Linux sandbox synthetic mount registry
      per user for shared codex use case @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21255 linux-sandbox: use standalone bundled bwrap @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21409 [codex] Fix Windows sandbox git safe.directory for worktrees @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-safety-and-privacy-changes-in-rust-v0-129-0
  source_release: codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e
  source_type: github_releases
  theme: safety-privacy
  title: 11 Safety and Privacy changes in rust-v0.129.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-06-protect-against-rce-from-malicious-bare-repositories-nested-inside-a-project-for|Protect
  against RCE from malicious bare repositories nested inside a project…]]'
- '[[Changes/ChatGPT/2026-05-07-over-the-coming-weeks-we-ll-be-rolling-out-trusted-contact-an-optional-safety-fe|Trusted
  contact in ChatGPT]]'
- '[[Changes/Claude Code/2026-05-07-added-sandbox-bwrappath-and-sandbox-socatpath-managed-settings-linux-wsl-to-spec|Added
  sandbox.bwrapPath and sandbox.socatPath managed settings (Linux/WSL)…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e]]'
source_type: github_releases
theme: safety-privacy
title: 11 Safety and Privacy changes in rust-v0.129.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Safety and Privacy changes in rust-v0.129.0

**Codex CLI** · 2026-05-07 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.129.0) · from [[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|0.129.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Linux sandbox startup is more reliable across older `bwrap`, slow mount probes, symlink-protected paths, and shared `/tmp` setups. (#20628, #20111, #21127, #21234)

> Windows sandbox and exec policy now handle named pipes, ConPTY teardown, PowerShell-wrapped allow rules, worktree `safe.directory`, and unsafe Git options more reliably. (#20270, #20685, #20336, #21409, #21275)

> Vendored Bubblewrap was updated to 0.11.2, including upstream security changes around setuid support. (#21389)

> #20270 [codex] Fix elevated Windows sandbox named-pipe access @iceweasel-oai

> #20101 install WFP filters for Windows sandbox setup @iceweasel-oai

> #20628 fix(linux-sandbox): fall back when system bwrap lacks perms @viyatb-oai

> #20708 Add Windows sandbox readiness RPC @iceweasel-oai

> #21127 fix(linux-sandbox): avoid panic on bwrap build failures @viyatb-oai

> #21234 fix(linux-sandbox): isolate Linux sandbox synthetic mount registry per user for shared codex use case @viyatb-oai

> #21255 linux-sandbox: use standalone bundled bwrap @bolinfest

> #21409 [codex] Fix Windows sandbox git safe.directory for worktrees @iceweasel-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.129.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-07-5-agent-mode-changes-in-rust-v0-129-0|5 Agent Mode changes in rust-v0.129.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-07-39-apps-and-integrations-changes-in-rust-v0-129-0|39 Apps and Integrations changes in rust-v0.129.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-07-3-mobile-and-desktop-changes-in-rust-v0-129-0|3 Mobile and Desktop changes in rust-v0.129.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-07-3-collaboration-changes-in-rust-v0-129-0|3 Collaboration changes in rust-v0.129.0]] · Collaboration
- [[Changes/Codex CLI/2026-05-07-20065-feat-tui-redesign-session-picker-fcoury-oai|♯20065 feat(tui): redesign session picker @fcoury-oai]] · Interface Experience
- [[Changes/Codex CLI/2026-05-07-4-model-support-changes-in-rust-v0-129-0|4 Model Support changes in rust-v0.129.0]] · Model Support
- [[Changes/Codex CLI/2026-05-07-4-editor-experience-changes-in-rust-v0-129-0|4 Editor Experience changes in rust-v0.129.0]] · Editor Experience
- [[Changes/Codex CLI/2026-05-07-5-developer-workflow-changes-in-rust-v0-129-0|5 Developer Workflow changes in rust-v0.129.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-07-2-account-and-access-changes-in-rust-v0-129-0|2 Account and Access changes in rust-v0.129.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-07-7-context-window-changes-in-rust-v0-129-0|7 Context Window changes in rust-v0.129.0]] · Context Window
- [[Changes/Codex CLI/2026-05-07-tui-startup-and-accessibility-were-tightened-by-bounding-terminal-probes-clearin|TUI startup and accessibility were tightened by bounding terminal probes, clearing…]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-05-07-21379-document-codex-git-commit-attribution-config-henzelmann-oai|♯21379 Document Codex git commit attribution config @henzelmann-oai]] · Files and Data
- [[Changes/Codex CLI/2026-05-07-21054-rollout-store-web-search-and-mcp-tool-calls-owenlin0|♯21054 rollout: store web search and mcp tool calls @owenlin0]] · Search and Browsing
- [[Changes/Codex CLI/2026-05-07-16-memory-and-personalization-changes-in-rust-v0-129-0|16 Memory and Personalization changes in rust-v0.129.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-07-2-reliability-and-performance-changes-in-rust-v0-129-0|2 Reliability and Performance changes in rust-v0.129.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-05-07-137-other-changes-in-rust-v0-129-0|137 other changes in rust-v0.129.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-07 · Claude Code · [[Changes/Claude Code/2026-05-07-added-sandbox-bwrappath-and-sandbox-socatpath-managed-settings-linux-wsl-to-spec|Added sandbox.bwrapPath and sandbox.socatPath managed settings (Linux/WSL)…]]
- Later: 2026-05-08 · Claude Code · [[Changes/Claude Code/2026-05-08-2-safety-and-privacy-changes-in-v2-1-136|2 Safety and Privacy changes in v2.1.136]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-07-f3ddcf&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-07-11-safety-and-privacy-changes-in-rust-v0-129-0.md%0ACard%20ID%3A%20codex-cli-2026-05-07-f3ddcf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.129.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->