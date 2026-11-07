---
card_id: codex-cli-2025-12-04-23cf9f
date: '2025-12-04'
description: 'Codex CLI · 2025-12-04 · Context Window: 3 changes in 0.65.0 — History
  and context hygiene (#6242, #7483, #7545, #7431, #7483): history.jsonl is trimmed
  by…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 945
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8d7b9be5ac032340821418927b7423832682b9a98db2b9c1ce09cf7829783c6a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-12-04-23cf9f
  comparison: ''
  date: '2025-12-04'
  description: 'Codex CLI — 0.65.0: 3 Context Window changes'
  evidence:
  - quote: 'History and context hygiene (#6242, #7483, #7545, #7431, #7483): history.jsonl
      is trimmed by history.max_bytes, common junk dirs (incl. __pycache__) are ignored
      by default, and paste placeholders stay distinct.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.65.0
  - quote: 'Show token used when context window is unknown #7497 @[Ahmed Ibrahim]'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.65.0
  - quote: 'feat: alias compaction #7442 @[jif-oai]'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.65.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-context-window-changes-in-rust-v0-65-0
  source_release: codex-cli-2025-12-04-rust-v0-65-0-github-267537191-959c7b4d
  source_type: github_releases
  theme: context-window
  title: 3 Context Window changes in rust-v0.65.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-12-02-5-context-window-changes-in-rust-v0-64-0|5 Context
  Window changes in rust-v0.64.0]]'
- "[[Changes/Open WebUI/2025-12-02-tool-call-response-token-duplication-was-fixed-by-removing-redundant-message-his|\U0001F504
  Tool call response token duplication was fixed by removing redundant message…]]"
- '[[Changes/Cline/2025-12-04-2-context-window-changes-in-v3-40-0|2 Context Window
  changes in v3.40.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-12-04-rust-v0-65-0-github-267537191-959c7b4d|codex-cli-2025-12-04-rust-v0-65-0-github-267537191-959c7b4d]]'
source_type: github_releases
theme: context-window
title: 3 Context Window changes in rust-v0.65.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Context Window changes in rust-v0.65.0

**Codex CLI** · 2025-12-04 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.65.0) · from [[Releases/Codex CLI/codex-cli-2025-12-04-rust-v0-65-0-github-267537191-959c7b4d|0.65.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> History and context hygiene (#6242, #7483, #7545, #7431, #7483): history.jsonl is trimmed by history.max_bytes, common junk dirs (incl. __pycache__) are ignored by default, and paste placeholders stay distinct.

> Show token used when context window is unknown #7497 @[Ahmed Ibrahim]

> feat: alias compaction #7442 @[jif-oai]

Source: https://github.com/openai/codex/releases/tag/rust-v0.65.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-12-04-persisting-credits-if-new-snapshot-does-not-contain-credit-info-7490-zhao-oai|persisting credits if new snapshot does not contain credit info ♯7490 @zhao-oai]] · Pricing Model
- [[Changes/Codex CLI/2025-12-04-3-interface-experience-changes-in-rust-v0-65-0|3 Interface Experience changes in rust-v0.65.0]] · Interface Experience
- [[Changes/Codex CLI/2025-12-04-chore-make-create-approval-requirement-for-command-an-async-fn-7501-michael-boli|chore: make create_approval_requirement_for_command an async fn ♯7501 @Michael Bolin]] · Developer Workflow
- [[Changes/Codex CLI/2025-12-04-2-reliability-and-performance-changes-in-rust-v0-65-0|2 Reliability and Performance changes in rust-v0.65.0]] · Reliability and Performance
- [[Changes/Codex CLI/2025-12-04-2-apps-and-integrations-changes-in-rust-v0-65-0|2 Apps and Integrations changes in rust-v0.65.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-12-04-6-model-support-changes-in-rust-v0-65-0|6 Model Support changes in rust-v0.65.0]] · Model Support
- [[Changes/Codex CLI/2025-12-04-29-other-changes-in-rust-v0-65-0|29 other changes in rust-v0.65.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2025-12-04 · Cline · [[Changes/Cline/2025-12-04-2-context-window-changes-in-v3-40-0|2 Context Window changes in v3.40.0]]
- Later: 2025-12-09 · Codex CLI · [[Changes/Codex CLI/2025-12-09-general-fixes-parallel-tool-call-chat-now-returns-correctly-ghost-snapshot-token|General fixes: parallel tool-call chat now returns correctly, ghost snapshot tokens…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-12-04-23cf9f&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-12-04-3-context-window-changes-in-rust-v0-65-0.md%0ACard%20ID%3A%20codex-cli-2025-12-04-23cf9f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.65.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->