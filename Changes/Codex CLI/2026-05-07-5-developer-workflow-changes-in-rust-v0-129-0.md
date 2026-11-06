---
card_id: codex-cli-2026-05-07-3c77bd
date: '2026-05-07'
description: 'Codex CLI · 2026-05-07 · Developer Workflow: 5 changes in 0.129.0 —
  The status line can show theme-aware colors plus optional PR and branch-change summaries…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1146
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5d50eeec59d34c536b7d7e20a5b51bcde08f4c84055750d5ed1796e11b2ef243
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-07-3c77bd
  comparison: ''
  date: '2026-05-07'
  description: 'Codex CLI — 0.129.0: 5 Developer Workflow changes'
  evidence:
  - quote: 'The status line can show theme-aware colors plus optional PR and branch-change
      summaries, and `/keymap debug` helps inspect terminal key events. (#19631, #20892,
      #20794)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: Documented how generated git commit attribution is gated by `codex_git_commit`
      and configured in `config.toml`. (#21379)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20654 fix(tui): bound startup terminal probes @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20794 feat(tui): add keymap debug inspector @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21381 [codex] Handle git pagination flags by position @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-developer-workflow-changes-in-rust-v0-129-0
  source_release: codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e
  source_type: github_releases
  theme: developer-workflow
  title: 5 Developer Workflow changes in rust-v0.129.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-06-2-developer-workflow-changes-in-v1-0-42|2
  Developer Workflow changes in v1.0.42]]'
- '[[Changes/GitHub Copilot CLI/2026-05-06-show-download-progress-when-running-the-update-command|Show
  download progress when running the update command]]'
- '[[Changes/Claude Code/2026-05-07-added-worktree-baseref-setting-fresh-head-to-choose-whether-worktree-enterworktr|Added
  worktree.baseRef setting (fresh  /  head) to choose whether --worktree…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e]]'
source_type: github_releases
theme: developer-workflow
title: 5 Developer Workflow changes in rust-v0.129.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Developer Workflow changes in rust-v0.129.0

**Codex CLI** · 2026-05-07 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.129.0) · from [[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|0.129.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The status line can show theme-aware colors plus optional PR and branch-change summaries, and `/keymap debug` helps inspect terminal key events. (#19631, #20892, #20794)

> Documented how generated git commit attribution is gated by `codex_git_commit` and configured in `config.toml`. (#21379)

> #20654 fix(tui): bound startup terminal probes @fcoury-oai

> #20794 feat(tui): add keymap debug inspector @fcoury-oai

> #21381 [codex] Handle git pagination flags by position @iceweasel-oai

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
- [[Changes/Codex CLI/2026-05-07-2-account-and-access-changes-in-rust-v0-129-0|2 Account and Access changes in rust-v0.129.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-07-7-context-window-changes-in-rust-v0-129-0|7 Context Window changes in rust-v0.129.0]] · Context Window
- [[Changes/Codex CLI/2026-05-07-tui-startup-and-accessibility-were-tightened-by-bounding-terminal-probes-clearin|TUI startup and accessibility were tightened by bounding terminal probes, clearing…]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-05-07-21379-document-codex-git-commit-attribution-config-henzelmann-oai|♯21379 Document Codex git commit attribution config @henzelmann-oai]] · Files and Data
- [[Changes/Codex CLI/2026-05-07-21054-rollout-store-web-search-and-mcp-tool-calls-owenlin0|♯21054 rollout: store web search and mcp tool calls @owenlin0]] · Search and Browsing
- [[Changes/Codex CLI/2026-05-07-16-memory-and-personalization-changes-in-rust-v0-129-0|16 Memory and Personalization changes in rust-v0.129.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-07-11-safety-and-privacy-changes-in-rust-v0-129-0|11 Safety and Privacy changes in rust-v0.129.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-07-2-reliability-and-performance-changes-in-rust-v0-129-0|2 Reliability and Performance changes in rust-v0.129.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-05-07-137-other-changes-in-rust-v0-129-0|137 other changes in rust-v0.129.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-05-07 · Claude Code · [[Changes/Claude Code/2026-05-07-added-worktree-baseref-setting-fresh-head-to-choose-whether-worktree-enterworktr|Added worktree.baseRef setting (fresh  /  head) to choose whether --worktree…]]
- Later: 2026-05-07 · Cursor · [[Changes/Cursor/2026-05-07-pr-review|PR review]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-07-3c77bd&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-07-5-developer-workflow-changes-in-rust-v0-129-0.md%0ACard%20ID%3A%20codex-cli-2026-05-07-3c77bd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.129.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->