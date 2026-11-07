---
card_id: open-webui-2026-03-25-7b3fe1
date: '2026-03-25'
description: "Open WebUI · 2026-03-25 · Context Window: 3 changes in v0.8.11 — \U0001F6E0️
  **Tool HTML embed context.** Tools can now return custom context alongside HTML
  embeds by…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2380
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f3dbf59338c829af2de23197c81563a5fe0178f2c05b35b6f8b4b3fd85930f77
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-25-7b3fe1
  comparison: ''
  date: '2026-03-25'
  description: 'Open WebUI — v0.8.11: 3 Context Window changes'
  evidence:
  - quote: "\U0001F6E0️ **Tool HTML embed context.** Tools can now return custom context
      alongside HTML embeds by using a tuple format, providing the LLM with actionable
      information instead of a generic message. [#22691](https://github.com/open-webui/open-webui/pull/22691)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: ✏️ **File renaming.** Files and folders in the File Navigator can now be
      renamed by double-clicking or using the context menu, with Enter to confirm
      and Escape to cancel. [Commit](https://github.com/open-webui/open-webui/commit/637cd136c2271baf4787815bc8bc25241626a943)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F50D **Ollama embedding robustness.** Ollama embedding requests
      now include the truncate parameter to handle inputs exceeding the context window,
      preventing 500 errors when processing long documents. Error messages from failed
      embedding requests are also now properly surfaced instead of being silently
      swallowed. [#22671](https://github.com/open-webui/open-webui/issues/22671),
      [Commit](https://github.com/open-webui/open-webui/commit/d738044f47c70c755bec9bf244aa11878fe98d9c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-context-window-changes-in-v0-8-11
  source_release: open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69
  source_type: github_releases
  theme: context-window
  title: 3 Context Window changes in v0.8.11
  type: change
related_changes:
- '[[Changes/OpenCode/2026-03-22-2-context-window-changes-in-v1-3-0|2 Context Window
  changes in v1.3.0]]'
- '[[Changes/Gemini CLI/2026-03-24-2-context-window-changes-in-v0-35-0|2 Context Window
  changes in v0.35.0]]'
- '[[Changes/ChatGPT/2026-03-25-starting-today-for-chatgpt-plus-pro-and-business-users-long-pastes-are-handled-d|Large
  pastes are now handled as attachments]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69]]'
source_type: github_releases
theme: context-window
title: 3 Context Window changes in v0.8.11
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Context Window changes in v0.8.11

**Open WebUI** · 2026-03-25 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.11) · from [[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|v0.8.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🛠️ **Tool HTML embed context.** Tools can now return custom context alongside HTML embeds by using a tuple format, providing the LLM with actionable information instead of a generic message. [#22691](https://github.com/open-webui/open-webui/pull/22691)

> ✏️ **File renaming.** Files and folders in the File Navigator can now be renamed by double-clicking or using the context menu, with Enter to confirm and Escape to cancel. [Commit](https://github.com/open-webui/open-webui/commit/637cd136c2271baf4787815bc8bc25241626a943)

> 🔍 **Ollama embedding robustness.** Ollama embedding requests now include the truncate parameter to handle inputs exceeding the context window, preventing 500 errors when processing long documents. Error messages from failed embedding requests are also now properly surfaced instead of being silently swallowed. [#22671](https://github.com/open-webui/open-webui/issues/22671), [Commit](https://github.com/open-webui/open-webui/commit/d738044f47c70c755bec9bf244aa11878fe98d9c)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-25-4-editor-experience-changes-in-v0-8-11|4 Editor Experience changes in v0.8.11]] · Editor Experience
- [[Changes/Open WebUI/2026-03-25-rag-query-generation-robustness-the-rag-query-generation-web-search-and-image-ge|🔍 RAG query generation robustness. The RAG query generation, web search…]] · Image Generation
- [[Changes/Open WebUI/2026-03-25-shared-chat-viewing-crash-shared-chats-can-now-be-viewed-by-unauthenticated-user|🐛 Shared chat viewing crash. Shared chats can now be viewed by unauthenticated…]] · Collaboration
- [[Changes/Open WebUI/2026-03-25-11-account-and-access-changes-in-v0-8-11|11 Account and Access changes in v0.8.11]] · Account and Access
- [[Changes/Open WebUI/2026-03-25-2-search-and-browsing-changes-in-v0-8-11|2 Search and Browsing changes in v0.8.11]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-25-2-files-and-data-changes-in-v0-8-11|2 Files and Data changes in v0.8.11]] · Files and Data
- [[Changes/Open WebUI/2026-03-25-4-memory-and-personalization-changes-in-v0-8-11|4 Memory and Personalization changes in v0.8.11]] · Memory and Personalization
- [[Changes/Open WebUI/2026-03-25-3-apps-and-integrations-changes-in-v0-8-11|3 Apps and Integrations changes in v0.8.11]] · Apps and Integrations
- [[Changes/Open WebUI/2026-03-25-17-interface-experience-changes-in-v0-8-11|17 Interface Experience changes in v0.8.11]] · Interface Experience
- [[Changes/Open WebUI/2026-03-25-5-reliability-and-performance-changes-in-v0-8-11|5 Reliability and Performance changes in v0.8.11]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-25-tool-binary-response-handling-tool-servers-can-now-return-binary-data-such-as-im|🏮 Tool binary response handling. Tool servers can now return binary data such…]] · Multimodal Input
- [[Changes/Open WebUI/2026-03-25-23-model-support-changes-in-v0-8-11|23 Model Support changes in v0.8.11]] · Model Support
- [[Changes/Open WebUI/2026-03-25-4-safety-and-privacy-changes-in-v0-8-11|4 Safety and Privacy changes in v0.8.11]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-25-34-developer-workflow-changes-in-v0-8-11|34 Developer Workflow changes in v0.8.11]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-25-metrics-export-interval-configuration-administrators-can-now-control-opentelemet|📊 Metrics export interval configuration. Administrators can now control…]] · Pricing Model
- [[Changes/Open WebUI/2026-03-25-19-other-changes-in-v0-8-11|19 other changes in v0.8.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-03-25 · ChatGPT · [[Changes/ChatGPT/2026-03-25-starting-today-for-chatgpt-plus-pro-and-business-users-long-pastes-are-handled-d|Large pastes are now handled as attachments]]
- Later: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-reduced-ui-stutter-when-compaction-triggers-on-large-sessions|Reduced UI stutter when compaction triggers on large sessions]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-25-7b3fe1&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-25-3-context-window-changes-in-v0-8-11.md%0ACard%20ID%3A%20open-webui-2026-03-25-7b3fe1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->