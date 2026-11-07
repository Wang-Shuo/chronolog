---
card_id: github-copilot-cli-2026-04-14-dd1662
date: '2026-04-14'
description: 'GitHub Copilot CLI · 2026-04-14 · Context Window: 4 changes in 1.0.26
  — Agent sessions no longer fail with unrecoverable errors when context compaction
  splits…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2400
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 46e771e1a1e6cd227b0ef25d68abac35fa5cc3bebad0b498ecc1d37d93598891
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-04-14-dd1662
  comparison: ''
  date: '2026-04-14'
  description: 'GitHub Copilot CLI — 1.0.26: 4 Context Window changes'
  evidence:
  - quote: Agent sessions no longer fail with unrecoverable errors when context compaction
      splits a tool call across a checkpoint boundary
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.26
  - quote: Single-segment slash-prefixed tokens (e.g. /help, /start) no longer treated
      as file paths in bash commands
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.26
  - quote: Avoid sending duplicate custom instruction files (e.g. copilot-instructions.md
      and CLAUDE.md with identical content) to reduce wasted tokens per turn
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.26
  - quote: Instruction files with specific applyTo patterns are consolidated into
      a table instead of inlining full content, reducing context window usage
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.26
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-context-window-changes-in-v1-0-26
  source_release: github-copilot-cli-2026-04-14-v1-0-26-github-308996136-aa8c4bf2
  source_type: github_releases
  theme: context-window
  title: 4 Context Window changes in v1.0.26
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-04-11-3-context-window-changes-in-rust-v0-120-0|3 Context
  Window changes in rust-v0.120.0]]'
- '[[Changes/Claude Code/2026-04-14-2-context-window-changes-in-v2-1-108|2 Context
  Window changes in v2.1.108]]'
- '[[Changes/Gemini CLI/2026-04-14-2-context-window-changes-in-v0-38-0|2 Context Window
  changes in v0.38.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-14-v1-0-26-github-308996136-aa8c4bf2|github-copilot-cli-2026-04-14-v1-0-26-github-308996136-aa8c4bf2]]'
source_type: github_releases
theme: context-window
title: 4 Context Window changes in v1.0.26
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Context Window changes in v1.0.26

**GitHub Copilot CLI** · 2026-04-14 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.26) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-14-v1-0-26-github-308996136-aa8c4bf2|1.0.26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Agent sessions no longer fail with unrecoverable errors when context compaction splits a tool call across a checkpoint boundary

> Single-segment slash-prefixed tokens (e.g. /help, /start) no longer treated as file paths in bash commands

> Avoid sending duplicate custom instruction files (e.g. copilot-instructions.md and CLAUDE.md with identical content) to reduce wasted tokens per turn

> Instruction files with specific applyTo patterns are consolidated into a table instead of inlining full content, reducing context window usage

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-04-14-lsp-language-servers-correctly-initialize-on-windows-using-proper-file-uri-paths|LSP language servers correctly initialize on Windows using proper file URI paths]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-04-14-enterprise-login-accepts-hostnames-without-a-url-scheme-e-g-github-example-com|Enterprise login accepts hostnames without a URL scheme (e.g. 'github.example.com')]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-04-14-4-apps-and-integrations-changes-in-v1-0-26|4 Apps and Integrations changes in v1.0.26]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-04-14-permission-prompt-notification-hook-only-fires-when-a-prompt-is-actually-shown-t|Permission prompt notification hook only fires when a prompt is actually shown to the user]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-04-14-2-editor-experience-changes-in-v1-0-26|2 Editor Experience changes in v1.0.26]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-04-14-6-other-changes-in-v1-0-26|6 other changes in v1.0.26]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-04-14 · Gemini CLI · [[Changes/Gemini CLI/2026-04-14-2-context-window-changes-in-v0-38-0|2 Context Window changes in v0.38.0]]
- Later: 2026-04-15 · Claude Code · [[Changes/Claude Code/2026-04-15-added-option-to-show-claude-s-last-response-as-commented-context-in-the-ctrl-g-e|Added option to show Claude's last response as commented context in the Ctrl+G…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-04-14-dd1662&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-04-14-4-context-window-changes-in-v1-0-26.md%0ACard%20ID%3A%20github-copilot-cli-2026-04-14-dd1662%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->