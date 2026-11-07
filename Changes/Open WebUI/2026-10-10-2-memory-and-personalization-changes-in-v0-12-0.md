---
card_id: open-webui-2026-10-10-87b336
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Memory and Personalization: 2 changes in v0.12.0
  — \U0001F3CE️ **Native hybrid search on Milvus.** Hybrid search on Milvus 2.5 and
  newer, with…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1178
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 92814e1c409a587ba7b9d30aff01668312b608d40aeb16d12194950e08fc24d0
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-87b336
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 2 Memory and Personalization changes'
  evidence:
  - quote: "\U0001F3CE️ **Native hybrid search on Milvus.** Hybrid search on Milvus
      2.5 and newer, with one collection per knowledge base or with multitenancy,
      now runs inside Milvus with its built-in BM25 full-text search next to the vectors
      in the same collection, where every search loaded every chunk of the collection
      into Open WebUI and scored it there, making hybrid search on Milvus much faster
      and lighter on memory; the BM25 weight setting works the same way it does on
      pgvector. [#31645](https://github.com/open-webui/open-webui/pull/31645), [#31660](https://github.com/open-webui/open-webui/pull/31660),
      [#26243](https://github.com/open-webui/open-webui/issues/26243)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FAAB **Server memory per chat.** A long-running server no longer
      keeps a little memory for every chat it has answered until it is restarted.
      [#31534](https://github.com/open-webui/open-webui/pull/31534), [#31521](https://github.com/open-webui/open-webui/issues/31521)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-memory-and-personalization-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: memory
  title: 2 Memory and Personalization changes in v0.12.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-08-51223-remove-legacy-personality-template-metadata-rhan-oai|♯51223
  Remove legacy personality template metadata @rhan-oai]]'
- '[[Changes/Midjourney/2026-10-08-organization-improvements|ORGANIZATION IMPROVEMENTS]]'
- '[[Changes/OpenClaw/2026-10-08-2-memory-and-personalization-changes-in-v2026-9-9|2
  Memory and Personalization changes in v2026.9.9]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: memory
title: 2 Memory and Personalization changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Memory and Personalization changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🏎️ **Native hybrid search on Milvus.** Hybrid search on Milvus 2.5 and newer, with one collection per knowledge base or with multitenancy, now runs inside Milvus with its built-in BM25 full-text search next to the vectors in the same collection, where every search loaded every chunk of the collection into Open WebUI and scored it there, making hybrid search on Milvus much faster and lighter on memory; the BM25 weight setting works the same way it does on pgvector. [#31645](https://github.com/open-webui/open-webui/pull/31645), [#31660](https://github.com/open-webui/open-webui/pull/31660), [#26243](https://github.com/open-webui/open-webui/issues/26243)

> 🪫 **Server memory per chat.** A long-running server no longer keeps a little memory for every chat it has answered until it is restarted. [#31534](https://github.com/open-webui/open-webui/pull/31534), [#31521](https://github.com/open-webui/open-webui/issues/31521)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-reliability-and-performance-changes-in-v0-12-0|5 Reliability and Performance changes in v0.12.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5 Enterprise and Administration changes in v0.12.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-10-27-developer-workflow-changes-in-v0-12-0|27 Developer Workflow changes in v0.12.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-10-5-image-generation-changes-in-v0-12-0|5 Image Generation changes in v0.12.0]] · Image Generation
- [[Changes/Open WebUI/2026-10-10-49-model-support-changes-in-v0-12-0|49 Model Support changes in v0.12.0]] · Model Support
- [[Changes/Open WebUI/2026-10-10-19-account-and-access-changes-in-v0-12-0|19 Account and Access changes in v0.12.0]] · Account and Access
- [[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10 Automation and Scheduling changes in v0.12.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile and Desktop changes in v0.12.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-10-10-6-files-and-data-changes-in-v0-12-0|6 Files and Data changes in v0.12.0]] · Files and Data
- [[Changes/Open WebUI/2026-10-10-13-collaboration-changes-in-v0-12-0|13 Collaboration changes in v0.12.0]] · Collaboration
- [[Changes/Open WebUI/2026-10-10-5-context-window-changes-in-v0-12-0|5 Context Window changes in v0.12.0]] · Context Window
- [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]] · Interface Experience
- [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Agent Mode
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-10-08 · OpenClaw · [[Changes/OpenClaw/2026-10-08-2-memory-and-personalization-changes-in-v2026-9-9|2 Memory and Personalization changes in v2026.9.9]]
- Later: 2026-10-10 · OpenClaw · [[Changes/OpenClaw/2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1|13 Memory and Personalization changes in v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-87b336&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-2-memory-and-personalization-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-87b336%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->