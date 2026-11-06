---
card_id: codex-cli-2026-05-07-2d6a99
date: '2026-05-07'
description: 'Codex CLI · 2026-05-07 · Editor Experience: 4 changes in 0.129.0 — Large
  paste placeholders and Ctrl+C-stashed drafts now survive clear/editor workflows…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1150
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a8fe39e1b6f9215d9abfd6a6ae3b8983356123ad8d330556246ff43cca041fdb
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-07-2d6a99
  comparison: ''
  date: '2026-05-07'
  description: 'Codex CLI — 0.129.0: 4 Editor Experience changes'
  evidence:
  - quote: 'Large paste placeholders and Ctrl+C-stashed drafts now survive clear/editor
      workflows without corrupting draft history. (#21091, #21190, #21351, #21397)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20379 Send external import completion for sync imports @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21190 fix(tui): external editor expansion for same-size large pastes
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21001 feat(tui): route /diff through workspace commands @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-editor-experience-changes-in-rust-v0-129-0
  source_release: codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e
  source_type: github_releases
  theme: editor-experience
  title: 4 Editor Experience changes in rust-v0.129.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-01-powershell-tool-bare-e-g-git-diff-file-is-no-longer-mis-flagged-as-the-stop-pars|PowerShell
  tool: bare -- (e.g. git diff -- file) is no longer mis-flagged…]]'
- '[[Changes/Cursor/2026-05-04-updated-usage-analytics-tab|Updated usage analytics
  tab]]'
- '[[Changes/GitHub Copilot CLI/2026-05-05-4-editor-experience-changes-in-v1-0-41|4
  Editor Experience changes in v1.0.41]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e]]'
source_type: github_releases
theme: editor-experience
title: 4 Editor Experience changes in rust-v0.129.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Editor Experience changes in rust-v0.129.0

**Codex CLI** · 2026-05-07 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.129.0) · from [[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|0.129.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Large paste placeholders and Ctrl+C-stashed drafts now survive clear/editor workflows without corrupting draft history. (#21091, #21190, #21351, #21397)

> #20379 Send external import completion for sync imports @alexsong-oai

> #21190 fix(tui): external editor expansion for same-size large pastes @fcoury-oai

> #21001 feat(tui): route /diff through workspace commands @fcoury-oai

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
- [[Changes/Codex CLI/2026-05-07-5-developer-workflow-changes-in-rust-v0-129-0|5 Developer Workflow changes in rust-v0.129.0]] · Developer Workflow
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
## Nearby in Editor Experience

- Earlier: 2026-05-05 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-05-4-editor-experience-changes-in-v1-0-41|4 Editor Experience changes in v1.0.41]]
- Later: 2026-05-07 · Cursor · [[Changes/Cursor/2026-05-07-improved-prompt-input-undo-grouping-so-undo-redo-feels-more-natural-during-edits|Improved prompt input undo grouping, so undo/redo feels more natural during edits]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-07-2d6a99&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-07-4-editor-experience-changes-in-rust-v0-129-0.md%0ACard%20ID%3A%20codex-cli-2026-05-07-2d6a99%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.129.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->