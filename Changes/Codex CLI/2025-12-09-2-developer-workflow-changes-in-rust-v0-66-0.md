---
card_id: codex-cli-2025-12-09-a51191
date: '2025-12-09'
description: 'Codex CLI · 2025-12-09 · Developer Workflow: 2 changes in 0.66.0 — Unified
  exec & shell stability: status line shows clearer progress, Windows unified-exec…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 997
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4b91d85ca4c9a94d5b7848c67d7d7f09acabd34840261b11d8272f802c045629
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-12-09-a51191
  comparison: ''
  date: '2025-12-09'
  description: 'Codex CLI — 0.66.0: 2 Developer Workflow changes'
  evidence:
  - quote: 'Unified exec & shell stability: status line shows clearer progress, Windows
      unified-exec crash fixed, long commands wrap without breaking layout, and SSE/session
      cleanup reduces stuck or'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#6793 FIX: WSL Paste image does not work @Waxime64'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 2-developer-workflow-changes-in-rust-v0-66-0
  source_release: codex-cli-2025-12-09-rust-v0-66-0-github-268559734-698ec8f9
  source_type: github_releases
  theme: developer-workflow
  title: 2 Developer Workflow changes in rust-v0.66.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-12-02-4-developer-workflow-changes-in-v0-19-0|4 Developer
  Workflow changes in v0.19.0]]'
- '[[Changes/Cline/2025-12-04-docs-remove-advanced-patterns-and-testing-debugging-from-hooks-docs-by-jl-codes|docs:
  remove Advanced Patterns and Testing & Debugging from Hooks docs]]'
- '[[Changes/Codex CLI/2025-12-04-chore-make-create-approval-requirement-for-command-an-async-fn-7501-michael-boli|chore:
  make create_approval_requirement_for_command an async fn ♯7501 @Michael Bolin]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-12-09-rust-v0-66-0-github-268559734-698ec8f9|codex-cli-2025-12-09-rust-v0-66-0-github-268559734-698ec8f9]]'
source_type: github_releases
theme: developer-workflow
title: 2 Developer Workflow changes in rust-v0.66.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Developer Workflow changes in rust-v0.66.0

**Codex CLI** · 2025-12-09 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.66.0) · from [[Releases/Codex CLI/codex-cli-2025-12-09-rust-v0-66-0-github-268559734-698ec8f9|0.66.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Unified exec & shell stability: status line shows clearer progress, Windows unified-exec crash fixed, long commands wrap without breaking layout, and SSE/session cleanup reduces stuck or

> #6793 FIX: WSL Paste image does not work @Waxime64

Source: https://github.com/openai/codex/releases/tag/rust-v0.66.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-12-09-3-apps-and-integrations-changes-in-rust-v0-66-0|3 Apps and Integrations changes in rust-v0.66.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-12-09-2-account-and-access-changes-in-rust-v0-66-0|2 Account and Access changes in rust-v0.66.0]] · Account and Access
- [[Changes/Codex CLI/2025-12-09-3-editor-experience-changes-in-rust-v0-66-0|3 Editor Experience changes in rust-v0.66.0]] · Editor Experience
- [[Changes/Codex CLI/2025-12-09-2-interface-experience-changes-in-rust-v0-66-0|2 Interface Experience changes in rust-v0.66.0]] · Interface Experience
- [[Changes/Codex CLI/2025-12-09-7729-feat-add-is-mutating-detection-for-shell-command-handler-jif-oai|♯7729 feat: add is-mutating detection for shell command handler @jif-oai]] · Agent Mode
- [[Changes/Codex CLI/2025-12-09-7547-use-shared-check-sandboxing-pakrym-oai|♯7547 Use shared check sandboxing @pakrym-oai]] · Collaboration
- [[Changes/Codex CLI/2025-12-09-3-safety-and-privacy-changes-in-rust-v0-66-0|3 Safety and Privacy changes in rust-v0.66.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-12-09-8-model-support-changes-in-rust-v0-66-0|8 Model Support changes in rust-v0.66.0]] · Model Support
- [[Changes/Codex CLI/2025-12-09-general-fixes-parallel-tool-call-chat-now-returns-correctly-ghost-snapshot-token|General fixes: parallel tool-call chat now returns correctly, ghost snapshot tokens…]] · Context Window
- [[Changes/Codex CLI/2025-12-09-4-mobile-and-desktop-changes-in-rust-v0-66-0|4 Mobile and Desktop changes in rust-v0.66.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-12-09-52-other-changes-in-rust-v0-66-0|52 other changes in rust-v0.66.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2025-12-04 · Codex CLI · [[Changes/Codex CLI/2025-12-04-chore-make-create-approval-requirement-for-command-an-async-fn-7501-michael-boli|chore: make create_approval_requirement_for_command an async fn ♯7501 @Michael Bolin]]
- Later: 2025-12-09 · Gemini CLI · [[Changes/Gemini CLI/2025-12-09-feat-core-add-configurable-inactivity-timeout-for-shell-commands-by-galz10-in-ht|feat(core): Add configurable inactivity timeout for shell commands]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-12-09-a51191&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-12-09-2-developer-workflow-changes-in-rust-v0-66-0.md%0ACard%20ID%3A%20codex-cli-2025-12-09-a51191%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.66.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->