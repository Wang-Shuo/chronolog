---
card_id: codex-cli-2026-11-06-6ec175
date: '2026-11-06'
description: 'Codex CLI · 2026-11-06 · Context Window: 8 changes in 0.167.0 — Automatic
  context compaction now accounts for retained output from failed responses and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1282
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e627dcc63c8867880129d0f3af4b56878753fa34bead36a35701463ee69c3821
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-11-06-6ec175
  comparison: ''
  date: '2026-11-06'
  description: 'Codex CLI — 0.167.0: 8 Context Window changes'
  evidence:
  - quote: Automatic context compaction now accounts for retained output from failed
      responses and responses with missing token usage data (#58404).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58071 Share the Guardian context delivery token limit @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58144 Record additional context counts, sizes, and truncation metrics
      @akira-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58388 Add whole-entry elastic allocation for Guardian context @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58390 Expose parent context for host-managed child startup @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58404 Fix context token estimates for responses without usable usage
      @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58444 Cap Guardian context entries before elastic allocation @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  - quote: '#58454 Add elastic budgeting for Guardian context preparation @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.167.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-context-window-changes-in-rust-v0-167-0
  source_release: codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc
  source_type: github_releases
  theme: context-window
  title: 8 Context Window changes in rust-v0.167.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-11-03-5-context-window-changes-in-v2026-10-10|5 Context
  Window changes in v2026.10.10]]'
- '[[Changes/Dify/2026-11-04-6-context-window-changes-in-1-19-0|6 Context Window changes
  in 1.19.0]]'
- '[[Changes/OpenClaw/2026-11-05-3-context-window-changes-in-v2026-11-1|3 Context
  Window changes in v2026.11.1]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc|codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc]]'
source_type: github_releases
theme: context-window
title: 8 Context Window changes in rust-v0.167.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Context Window changes in rust-v0.167.0

**Codex CLI** · 2026-11-06 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.167.0) · from [[Releases/Codex CLI/codex-cli-2026-11-06-rust-v0-167-0-github-435979892-a2e140bc|0.167.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Automatic context compaction now accounts for retained output from failed responses and responses with missing token usage data (#58404).

> #58071 Share the Guardian context delivery token limit @ioanbudea-OAI

> #58144 Record additional context counts, sizes, and truncation metrics @akira-oai

> #58388 Add whole-entry elastic allocation for Guardian context @ioanbudea-OAI

> #58390 Expose parent context for host-managed child startup @rhan-oai

> #58404 Fix context token estimates for responses without usable usage @dkovalenko-oai

> #58444 Cap Guardian context entries before elastic allocation @ioanbudea-OAI

> #58454 Add elastic budgeting for Guardian context preparation @ioanbudea-OAI

Source: https://github.com/openai/codex/releases/tag/rust-v0.167.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-11-06-2-memory-and-personalization-changes-in-rust-v0-167-0|2 Memory and Personalization changes in rust-v0.167.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-11-06-2-editor-experience-changes-in-rust-v0-167-0|2 Editor Experience changes in rust-v0.167.0]] · Editor Experience
- [[Changes/Codex CLI/2026-11-06-3-search-and-browsing-changes-in-rust-v0-167-0|3 Search and Browsing changes in rust-v0.167.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-11-06-7-model-support-changes-in-rust-v0-167-0|7 Model Support changes in rust-v0.167.0]] · Model Support
- [[Changes/Codex CLI/2026-11-06-6-developer-workflow-changes-in-rust-v0-167-0|6 Developer Workflow changes in rust-v0.167.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-11-06-4-voice-and-audio-changes-in-rust-v0-167-0|4 Voice and Audio changes in rust-v0.167.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-11-06-2-mobile-and-desktop-changes-in-rust-v0-167-0|2 Mobile and Desktop changes in rust-v0.167.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-11-06-5-account-and-access-changes-in-rust-v0-167-0|5 Account and Access changes in rust-v0.167.0]] · Account and Access
- [[Changes/Codex CLI/2026-11-06-6-agent-mode-changes-in-rust-v0-167-0|6 Agent Mode changes in rust-v0.167.0]] · Agent Mode
- [[Changes/Codex CLI/2026-11-06-13-interface-experience-changes-in-rust-v0-167-0|13 Interface Experience changes in rust-v0.167.0]] · Interface Experience
- [[Changes/Codex CLI/2026-11-06-57985-skip-read-only-volume-root-expansion-in-the-mxc-sandbox-iceweasel-oai|♯57985 Skip read-only volume-root expansion in the MXC sandbox @iceweasel-oai]] · Safety and Privacy
- [[Changes/Codex CLI/2026-11-06-12-apps-and-integrations-changes-in-rust-v0-167-0|12 Apps and Integrations changes in rust-v0.167.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-11-06-65-other-changes-in-rust-v0-167-0|65 other changes in rust-v0.167.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-11-05 · OpenClaw · [[Changes/OpenClaw/2026-11-05-3-context-window-changes-in-v2026-11-1|3 Context Window changes in v2026.11.1]]
- Later: 2026-11-06 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-11-06-17-context-window-changes-in-v1-0-106|17 Context Window changes in v1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-11-06-6ec175&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-11-06-8-context-window-changes-in-rust-v0-167-0.md%0ACard%20ID%3A%20codex-cli-2026-11-06-6ec175%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.167.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->