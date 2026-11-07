---
card_id: open-webui-2026-04-21-867197
date: '2026-04-21'
description: 'Open WebUI · 2026-04-21 · Memory and Personalization: 7 changes in v0.9.0
  — ⚡ **Drawer performance and memory optimization.** Drawer interactions now stay…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1006
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: beb3f31659f0562b726ab8cb005820ea4ae6e2e0bd38e4955a77ec5e2bce9857
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-867197
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 7 Memory and Personalization changes'
  evidence:
  - quote: ⚡ **Drawer performance and memory optimization.** Drawer interactions now
      stay smoother over long sessions by removing stale keyboard listeners on teardown,
      which reduces memory growth and avoids accumulated event handling overhead.
      [#23724](https://github.com/open-webui/open-webui/pull/23724#issuecomment-4245840810)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9E0 **HTML entity decode performance.** Streaming text decoding
      now avoids repeated document parsing for HTML entity handling, reducing memory
      churn and improving responsiveness in token-heavy chat output. [#23165](https://github.com/open-webui/open-webui/pull/23165)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4C8 **Sidebar memory optimization.** Sidebar chat items now use
      shared drag-preview resources and safer listener cleanup, reducing memory growth
      and keeping large chat lists more responsive during long sessions. [#23209](https://github.com/open-webui/open-webui/pull/23209)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9E0 **Image viewer memory optimization.** Viewing images and SVGs
      now uses significantly less memory and performs faster, keeping the application
      snappy and responsive even when browsing through many media files during extended
      sessions. [#23236](https://github.com/open-webui/open-webui/pull/23236)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4A8 **Optimized shared chat deletion.** Deleting shared chats by
      user is now faster and more memory-efficient by only loading necessary data.
      [#23216](https://github.com/open-webui/open-webui/pull/23216)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9E0 **Memory search filtering.** Memory search now correctly filters
      by the query text instead of returning unrelated results. [Commit](https://github.com/open-webui/open-webui/commit/43e5905c133049036353978704b0abd179716749),
      [#23826](https://github.com/open-webui/open-webui/issues/23826)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6A6 **Async vector search responsiveness.** File processing, memory
      updates, and knowledge retrieval no longer block the server event loop during
      vector database operations, so other chats and requests stay responsive while
      indexing or search is running. [#23706](https://github.com/open-webui/open-webui/pull/23706)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-memory-and-personalization-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: memory
  title: 7 Memory and Personalization changes in v0.9.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-04-16-core-the-bash-tool-uses-less-memory-on-large-command-output|Core
  The bash tool uses less memory on large command output]]'
- '[[Changes/Codex CLI/2026-04-20-4-memory-and-personalization-changes-in-rust-v0-122-0|4
  Memory and Personalization changes in rust-v0.122.0]]'
- '[[Changes/ElevenLabs/2026-04-20-elevenagents-d2ebb2|ElevenAgents]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: memory
title: 7 Memory and Personalization changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Memory and Personalization changes in v0.9.0

**Open WebUI** · 2026-04-21 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⚡ **Drawer performance and memory optimization.** Drawer interactions now stay smoother over long sessions by removing stale keyboard listeners on teardown, which reduces memory growth and avoids accumulated event handling overhead. [#23724](https://github.com/open-webui/open-webui/pull/23724#issuecomment-4245840810)

> 🧠 **HTML entity decode performance.** Streaming text decoding now avoids repeated document parsing for HTML entity handling, reducing memory churn and improving responsiveness in token-heavy chat output. [#23165](https://github.com/open-webui/open-webui/pull/23165)

> 📈 **Sidebar memory optimization.** Sidebar chat items now use shared drag-preview resources and safer listener cleanup, reducing memory growth and keeping large chat lists more responsive during long sessions. [#23209](https://github.com/open-webui/open-webui/pull/23209)

> 🧠 **Image viewer memory optimization.** Viewing images and SVGs now uses significantly less memory and performs faster, keeping the application snappy and responsive even when browsing through many media files during extended sessions. [#23236](https://github.com/open-webui/open-webui/pull/23236)

> 💨 **Optimized shared chat deletion.** Deleting shared chats by user is now faster and more memory-efficient by only loading necessary data. [#23216](https://github.com/open-webui/open-webui/pull/23216)

> 🧠 **Memory search filtering.** Memory search now correctly filters by the query text instead of returning unrelated results. [Commit](https://github.com/open-webui/open-webui/commit/43e5905c133049036353978704b0abd179716749), [#23826](https://github.com/open-webui/open-webui/issues/23826)

> 🚦 **Async vector search responsiveness.** File processing, memory updates, and knowledge retrieval no longer block the server event loop during vector database operations, so other chats and requests stay responsive while indexing or search is running. [#23706](https://github.com/open-webui/open-webui/pull/23706)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-3-files-and-data-changes-in-v0-9-0|3 Files and Data changes in v0.9.0]] · Files and Data
- [[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation changes in v0.9.0]] · Image Generation
- [[Changes/Open WebUI/2026-04-21-28-model-support-changes-in-v0-9-0|28 Model Support changes in v0.9.0]] · Model Support
- [[Changes/Open WebUI/2026-04-21-5-editor-experience-changes-in-v0-9-0|5 Editor Experience changes in v0.9.0]] · Editor Experience
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-8-context-window-changes-in-v0-9-0|8 Context Window changes in v0.9.0]] · Context Window
- [[Changes/Open WebUI/2026-04-21-24-reliability-and-performance-changes-in-v0-9-0|24 Reliability and Performance changes in v0.9.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-21-4-apps-and-integrations-changes-in-v0-9-0|4 Apps and Integrations changes in v0.9.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-21-46-developer-workflow-changes-in-v0-9-0|46 Developer Workflow changes in v0.9.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-04-21-8-automation-and-scheduling-changes-in-v0-9-0|8 Automation and Scheduling changes in v0.9.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-21-2-mobile-and-desktop-changes-in-v0-9-0|2 Mobile and Desktop changes in v0.9.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-04-21-17-interface-experience-changes-in-v0-9-0|17 Interface Experience changes in v0.9.0]] · Interface Experience
- [[Changes/Open WebUI/2026-04-21-11-safety-and-privacy-changes-in-v0-9-0|11 Safety and Privacy changes in v0.9.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-04-21-4-search-and-browsing-changes-in-v0-9-0|4 Search and Browsing changes in v0.9.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-04-21-shared-chat-access-controls-you-can-now-control-who-has-access-to-a-shared-chat|🔗 Shared chat access controls. You can now control who has access to a shared…]] · Collaboration
- [[Changes/Open WebUI/2026-04-21-4-voice-and-audio-changes-in-v0-9-0|4 Voice and Audio changes in v0.9.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-04-21-17-account-and-access-changes-in-v0-9-0|17 Account and Access changes in v0.9.0]] · Account and Access
- [[Changes/Open WebUI/2026-04-21-21-other-changes-in-v0-9-0|21 other changes in v0.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-04-20 · ElevenLabs · [[Changes/ElevenLabs/2026-04-20-elevenagents-d2ebb2|ElevenAgents]]
- Later: 2026-04-22 · ChatGPT · [[Changes/ChatGPT/2026-04-22-sometimes-you-just-want-the-right-answer-as-quickly-as-possible-we-re-rolling-ou|Fast answers in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-867197&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-7-memory-and-personalization-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-867197%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->