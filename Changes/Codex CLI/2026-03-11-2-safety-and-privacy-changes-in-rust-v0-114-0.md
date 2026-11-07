---
card_id: codex-cli-2026-03-11-a2f22b
date: '2026-03-11'
description: 'Codex CLI · 2026-03-11 · Safety and Privacy: 2 changes in 0.114.0 —
  Fixed permission handling so legacy `workspace-write` behavior is preserved and
  newer…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1060
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 01087082ba5f9ae0554bf743279ffdf032d051108d7f6ec83f87f33314500005
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-11-a2f22b
  comparison: ''
  date: '2026-03-11'
  description: 'Codex CLI — 0.114.0: 2 Safety and Privacy changes'
  evidence:
  - quote: 'Fixed permission handling so legacy `workspace-write` behavior is preserved
      and newer permission profiles degrade more safely on older builds. (#13957,
      #14107)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14009 feat(core) Persist request_permission data across turns @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 2-safety-and-privacy-changes-in-rust-v0-114-0
  source_release: codex-cli-2026-03-11-rust-v0-114-0-github-295424880-aad043c8
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in rust-v0.114.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-10-6-safety-and-privacy-changes-in-v2-1-72|6 Safety
  and Privacy changes in v2.1.72]]'
- '[[Changes/Codex CLI/2026-03-10-10-safety-and-privacy-changes-in-rust-v0-113-0|10
  Safety and Privacy changes in rust-v0.113.0]]'
- '[[Changes/Claude Code/2026-03-11-fixed-freezes-and-100-cpu-loops-triggered-by-permission-prompts-for-complex-bash|Fixed
  freezes and 100% CPU loops triggered by permission prompts for complex bash commands]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-11-rust-v0-114-0-github-295424880-aad043c8|codex-cli-2026-03-11-rust-v0-114-0-github-295424880-aad043c8]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in rust-v0.114.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in rust-v0.114.0

**Codex CLI** · 2026-03-11 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.114.0) · from [[Releases/Codex CLI/codex-cli-2026-03-11-rust-v0-114-0-github-295424880-aad043c8|0.114.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed permission handling so legacy `workspace-write` behavior is preserved and newer permission profiles degrade more safely on older builds. (#13957, #14107)

> #14009 feat(core) Persist request_permission data across turns @dylan-hurd-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.114.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-11-14003-stabilize-split-pty-output-on-windows-aibrahim-oai|♯14003 Stabilize split PTY output on Windows @aibrahim-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-11-3-developer-workflow-changes-in-rust-v0-114-0|3 Developer Workflow changes in rust-v0.114.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-11-14136-fix-core-use-dedicated-types-for-responsesapi-web-search-tool-config-owenl|♯14136 fix(core): use dedicated types for responsesapi web search tool config @owenlin0]] · Search and Browsing
- [[Changes/Codex CLI/2026-03-11-14135-tui-only-show-fast-status-for-gpt-5-4-pash-openai|♯14135 tui: only show fast status for gpt-5.4 @pash-openai]] · Model Support
- [[Changes/Codex CLI/2026-03-11-2-context-window-changes-in-rust-v0-114-0|2 Context Window changes in rust-v0.114.0]] · Context Window
- [[Changes/Codex CLI/2026-03-11-8-apps-and-integrations-changes-in-rust-v0-114-0|8 Apps and Integrations changes in rust-v0.114.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-11-24-other-changes-in-rust-v0-114-0|24 other changes in rust-v0.114.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-11 · Claude Code · [[Changes/Claude Code/2026-03-11-fixed-freezes-and-100-cpu-loops-triggered-by-permission-prompts-for-complex-bash|Fixed freezes and 100% CPU loops triggered by permission prompts for complex bash commands]]
- Later: 2026-03-11 · Gemini CLI · [[Changes/Gemini CLI/2026-03-11-refactor-cli-fully-remove-react-anti-patterns-improve-type-safety-and-fix-ux-ove|refactor(cli): fully remove React anti patterns, improve type safety and fix UX…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-11-a2f22b&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-11-2-safety-and-privacy-changes-in-rust-v0-114-0.md%0ACard%20ID%3A%20codex-cli-2026-03-11-a2f22b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.114.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->