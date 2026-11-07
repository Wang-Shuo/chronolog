---
card_id: codex-cli-2026-02-05-078033
date: '2026-02-05'
description: 'Codex CLI · 2026-02-05 · Memory and Personalization: 4 changes in 0.97.0
  — Introduced initial memory plumbing (API client + local persistence) to support…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 931
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 73e74641040e2ae692950e330e216fe04c9be71fed80614e8bf6cc13ff6d0985
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-05-078033
  comparison: ''
  date: '2026-02-05'
  description: 'Codex CLI — 0.97.0: 4 Memory and Personalization changes'
  evidence:
  - quote: 'Introduced initial memory plumbing (API client + local persistence) to
      support thread memory summaries. (#10629, #10634)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: Added a `none` personality option in protocol/config surfaces. (#10688)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10688 add none personality option @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10650 chore(core) personality migration tests @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-memory-and-personalization-changes-in-rust-v0-97-0
  source_release: codex-cli-2026-02-05-rust-v0-97-0-github-283219180-522ab2d0
  source_type: github_releases
  theme: memory
  title: 4 Memory and Personalization changes in rust-v0.97.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-01-31-6-memory-and-personalization-changes-in-rust-v0-93-0|6
  Memory and Personalization changes in rust-v0.93.0]]'
- '[[Changes/Codex CLI/2026-02-02-7-memory-and-personalization-changes-in-rust-v0-94-0|7
  Memory and Personalization changes in rust-v0.94.0]]'
- '[[Changes/Claude Code/2026-02-05-claude-now-automatically-records-and-recalls-memories-as-it-works|Claude
  now automatically records and recalls memories as it works]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-05-rust-v0-97-0-github-283219180-522ab2d0|codex-cli-2026-02-05-rust-v0-97-0-github-283219180-522ab2d0]]'
source_type: github_releases
theme: memory
title: 4 Memory and Personalization changes in rust-v0.97.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Memory and Personalization changes in rust-v0.97.0

**Codex CLI** · 2026-02-05 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.97.0) · from [[Releases/Codex CLI/codex-cli-2026-02-05-rust-v0-97-0-github-283219180-522ab2d0|0.97.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Introduced initial memory plumbing (API client + local persistence) to support thread memory summaries. (#10629, #10634)

> Added a `none` personality option in protocol/config surfaces. (#10688)

> #10688 add none personality option @aibrahim-oai

> #10650 chore(core) personality migration tests @dylan-hurd-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.97.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-05-2-model-support-changes-in-rust-v0-97-0|2 Model Support changes in rust-v0.97.0]] · Model Support
- [[Changes/Codex CLI/2026-02-05-2-developer-workflow-changes-in-rust-v0-97-0|2 Developer Workflow changes in rust-v0.97.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-05-10649-fix-test-shell-command-interruption-flake-gt-oai|♯10649 Fix test_shell_command_interruption flake @gt-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-02-05-6-apps-and-integrations-changes-in-rust-v0-97-0|6 Apps and Integrations changes in rust-v0.97.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-05-2-safety-and-privacy-changes-in-rust-v0-97-0|2 Safety and Privacy changes in rust-v0.97.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-05-10667-chore-app-server-document-experimental-api-opt-in-owenlin0|♯10667 chore(app-server): document experimental API opt-in @owenlin0]] · Files and Data
- [[Changes/Codex CLI/2026-02-05-2-interface-experience-changes-in-rust-v0-97-0|2 Interface Experience changes in rust-v0.97.0]] · Interface Experience
- [[Changes/Codex CLI/2026-02-05-18-other-changes-in-rust-v0-97-0|18 other changes in rust-v0.97.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-02-05 · Claude Code · [[Changes/Claude Code/2026-02-05-claude-now-automatically-records-and-recalls-memories-as-it-works|Claude now automatically records and recalls memories as it works]]
- Later: 2026-02-05 · Codex CLI · [[Changes/Codex CLI/2026-02-05-2-memory-and-personalization-changes-in-rust-v0-98-0|2 Memory and Personalization changes in rust-v0.98.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-05-078033&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-05-4-memory-and-personalization-changes-in-rust-v0-97-0.md%0ACard%20ID%3A%20codex-cli-2026-02-05-078033%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.97.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->