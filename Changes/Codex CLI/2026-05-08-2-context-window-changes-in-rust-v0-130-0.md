---
card_id: codex-cli-2026-05-08-28407c
date: '2026-05-08'
description: 'Codex CLI · 2026-05-08 · Context Window: 2 changes in 0.130.0 — Remote
  compaction now emits `response.processed` for v2 streams and avoids sending…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1100
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9ac6bb18512cfe7c707e1e5b59b03e0948400d34cef7129e3551827cababe035
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-08-28407c
  comparison: ''
  date: '2026-05-08'
  description: 'Codex CLI — 0.130.0: 2 Context Window changes'
  evidence:
  - quote: 'Remote compaction now emits `response.processed` for v2 streams and avoids
      sending `service_tier` on API-key compact requests. (#21642, #21676)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21642 Send response.processed after remote compaction v2 @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 2-context-window-changes-in-rust-v0-130-0
  source_release: codex-cli-2026-05-08-rust-v0-130-0-github-319777370-eab676f9
  source_type: github_releases
  theme: context-window
  title: 2 Context Window changes in rust-v0.130.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-01-remote-session-statusline-shows-the-remote-working-directory-and-branch-instead|Remote
  session statusline shows the remote working directory and branch instead…]]'
- '[[Changes/Cursor/2026-05-06-you-can-now-see-a-breakdown-of-your-agent-s-context-usage-e005b2|Context
  Usage Breakdown]]'
- '[[Changes/Codex CLI/2026-05-07-7-context-window-changes-in-rust-v0-129-0|7 Context
  Window changes in rust-v0.129.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-08-rust-v0-130-0-github-319777370-eab676f9|codex-cli-2026-05-08-rust-v0-130-0-github-319777370-eab676f9]]'
source_type: github_releases
theme: context-window
title: 2 Context Window changes in rust-v0.130.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Context Window changes in rust-v0.130.0

**Codex CLI** · 2026-05-08 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.130.0) · from [[Releases/Codex CLI/codex-cli-2026-05-08-rust-v0-130-0-github-319777370-eab676f9|0.130.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Remote compaction now emits `response.processed` for v2 streams and avoids sending `service_tier` on API-key compact requests. (#21642, #21676)

> #21642 Send response.processed after remote compaction v2 @pakrym-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.130.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-08-20665-make-environment-providers-own-default-selection-starr-openai|♯20665 Make environment providers own default selection @starr-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-05-08-2-editor-experience-changes-in-rust-v0-130-0|2 Editor Experience changes in rust-v0.130.0]] · Editor Experience
- [[Changes/Codex CLI/2026-05-08-2-safety-and-privacy-changes-in-rust-v0-130-0|2 Safety and Privacy changes in rust-v0.130.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-08-8-apps-and-integrations-changes-in-rust-v0-130-0|8 Apps and Integrations changes in rust-v0.130.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-08-2-account-and-access-changes-in-rust-v0-130-0|2 Account and Access changes in rust-v0.130.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-08-added-configurable-opentelemetry-trace-metadata-and-richer-review-feedback-analy|Added configurable OpenTelemetry trace metadata and richer review/feedback analytics…]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-08-added-a-faster-cargo-profiling-build-profile-and-disabled-empty-doctest-targets|Added a faster Cargo profiling build profile and disabled empty doctest targets…]] · Reliability and Performance
- [[Changes/Codex CLI/2026-05-08-40-other-changes-in-rust-v0-130-0|40 other changes in rust-v0.130.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-05-07 · Codex CLI · [[Changes/Codex CLI/2026-05-07-7-context-window-changes-in-rust-v0-129-0|7 Context Window changes in rust-v0.129.0]]
- Later: 2026-05-11 · Claude Code · [[Changes/Claude Code/2026-05-11-context-all-per-skill-token-estimates-now-account-for-the-model-s-tokenizer-and|/context all per-skill token estimates now account for the model's tokenizer…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-08-28407c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-08-2-context-window-changes-in-rust-v0-130-0.md%0ACard%20ID%3A%20codex-cli-2026-05-08-28407c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.130.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->