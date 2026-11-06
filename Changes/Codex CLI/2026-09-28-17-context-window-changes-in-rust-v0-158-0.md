---
card_id: codex-cli-2026-09-28-f573b8
date: '2026-09-28'
description: 'Codex CLI · 2026-09-28 · Context Window: 17 changes in 0.158.0 — Secure
  direct exec-server WebSocket connections with bearer tokens, including connections…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1243
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bc2bcb44fe5f9082ba31ecba8b12601ea0cb82c1118b0aac9a7bc8ab8c7fe89b
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-28-f573b8
  comparison: ''
  date: '2026-09-28'
  description: 'Codex CLI — 0.158.0: 17 Context Window changes'
  evidence:
  - quote: 'Secure direct exec-server WebSocket connections with bearer tokens, including
      connections configured through app-server. (#47601, #47648)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47536 Route agent lookups and V2 context through `AgentControl` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47571 Wait for idle before injecting remote compaction test history @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47582 Retain assistant context for Guardian authorization reviews @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47584 Preserve streamed assistant message order in retained context @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47585 Preserve delivered assistant messages in Guardian retained context
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47596 Refresh realtime context for each model request @reia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47624 Recognize `user_message` tools in Guardian authorization context
      @ankushg'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47625 Allow history and notes without experimental context capability
      @pmccrary-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47648 Support bearer tokens for app-server executor connections @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47686 Make thread-owned Guardian context always enabled @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47689 Make Guardian thread context capture unconditional @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47690 Remove obsolete Guardian context capture mode branches @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47947 Expand root authorization context to 16 messages @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48098 Preserve recent authorization context for Guardian reviews @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48110 Deduplicate retained instructions in async Guardian context @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48115 Preserve user text parts during local compaction @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 17-context-window-changes-in-rust-v0-158-0
  source_release: codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7
  source_type: github_releases
  theme: context-window
  title: 17 Context Window changes in rust-v0.158.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-25-2-context-window-changes-in-v2-1-283|2 Context
  Window changes in v2.1.283]]'
- '[[Changes/Codex CLI/2026-09-25-6-context-window-changes-in-rust-v0-157-0|6 Context
  Window changes in rust-v0.157.0]]'
- '[[Changes/OpenHands/2026-09-25-refactor-remove-test-conversation-id-fallbacks-in-websocket-context-add-state-up|refactor:
  remove test-conversation-id fallbacks in websocket context + add…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7]]'
source_type: github_releases
theme: context-window
title: 17 Context Window changes in rust-v0.158.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Context Window changes in rust-v0.158.0

**Codex CLI** · 2026-09-28 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.158.0) · from [[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|0.158.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Secure direct exec-server WebSocket connections with bearer tokens, including connections configured through app-server. (#47601, #47648)

> #47536 Route agent lookups and V2 context through `AgentControl` @jif-oai

> #47571 Wait for idle before injecting remote compaction test history @felixxia-oai

> #47582 Retain assistant context for Guardian authorization reviews @felixxia-oai

> #47584 Preserve streamed assistant message order in retained context @felixxia-oai

> #47585 Preserve delivered assistant messages in Guardian retained context @felixxia-oai

> #47596 Refresh realtime context for each model request @reia-oai

> #47624 Recognize `user_message` tools in Guardian authorization context @ankushg

> #47625 Allow history and notes without experimental context capability @pmccrary-oai

> #47648 Support bearer tokens for app-server executor connections @euroelessar

> #47686 Make thread-owned Guardian context always enabled @felixxia-oai

> #47689 Make Guardian thread context capture unconditional @felixxia-oai

> #47690 Remove obsolete Guardian context capture mode branches @felixxia-oai

> #47947 Expand root authorization context to 16 messages @felixxia-oai

> #48098 Preserve recent authorization context for Guardian reviews @felixxia-oai

> #48110 Deduplicate retained instructions in async Guardian context @felixxia-oai

> #48115 Preserve user text parts during local compaction @felixxia-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.158.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-28-9-safety-and-privacy-changes-in-rust-v0-158-0|9 Safety and Privacy changes in rust-v0.158.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-28-47975-prevent-stale-voice-answers-from-reappearing-during-speech-recovery-etraut|♯47975 Prevent stale voice answers from reappearing during speech recovery @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-28-13-apps-and-integrations-changes-in-rust-v0-158-0|13 Apps and Integrations changes in rust-v0.158.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-28-8-account-and-access-changes-in-rust-v0-158-0|8 Account and Access changes in rust-v0.158.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-28-3-mobile-and-desktop-changes-in-rust-v0-158-0|3 Mobile and Desktop changes in rust-v0.158.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-28-3-memory-and-personalization-changes-in-rust-v0-158-0|3 Memory and Personalization changes in rust-v0.158.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-28-2-collaboration-changes-in-rust-v0-158-0|2 Collaboration changes in rust-v0.158.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-28-7-model-support-changes-in-rust-v0-158-0|7 Model Support changes in rust-v0.158.0]] · Model Support
- [[Changes/Codex CLI/2026-09-28-3-image-generation-changes-in-rust-v0-158-0|3 Image Generation changes in rust-v0.158.0]] · Image Generation
- [[Changes/Codex CLI/2026-09-28-4-editor-experience-changes-in-rust-v0-158-0|4 Editor Experience changes in rust-v0.158.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-28-6-interface-experience-changes-in-rust-v0-158-0|6 Interface Experience changes in rust-v0.158.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-28-47984-add-multi-agent-spawn-latency-and-failure-metrics-owenlin0|♯47984 Add multi-agent spawn latency and failure metrics @owenlin0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-28-14-developer-workflow-changes-in-rust-v0-158-0|14 Developer Workflow changes in rust-v0.158.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-28-11-agent-mode-changes-in-rust-v0-158-0|11 Agent Mode changes in rust-v0.158.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-28-96-other-changes-in-rust-v0-158-0|96 other changes in rust-v0.158.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-25 · OpenHands · [[Changes/OpenHands/2026-09-25-refactor-remove-test-conversation-id-fallbacks-in-websocket-context-add-state-up|refactor: remove test-conversation-id fallbacks in websocket context + add…]]
- Later: 2026-09-29 · Claude Code · [[Changes/Claude Code/2026-09-29-2-context-window-changes-in-v2-1-285|2 Context Window changes in v2.1.285]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-28-f573b8&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-28-17-context-window-changes-in-rust-v0-158-0.md%0ACard%20ID%3A%20codex-cli-2026-09-28-f573b8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.158.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->