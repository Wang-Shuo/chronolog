---
card_id: open-webui-2026-03-25-a098c2
date: '2026-03-25'
description: "Open WebUI · 2026-03-25 · Memory and Personalization: 4 changes in v0.8.11
  — \U0001F9E0 **Memory management search and sort.** Users can now search and sort
  their…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 979
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 35ba410637a9fdbe12ec1095b915b89c91fe1650e55fb03cabb8b2e186e7dcc0
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-25-a098c2
  comparison: ''
  date: '2026-03-25'
  description: 'Open WebUI — v0.8.11: 4 Memory and Personalization changes'
  evidence:
  - quote: "\U0001F9E0 **Memory management search and sort.** Users can now search
      and sort their personal memories in the Memory management modal, making it easier
      to find specific memories. [Commit](https://github.com/open-webui/open-webui/commit/47ab4c71d50fd631b04c95f2febb085dd0a13083)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4A1 **Memory deletion confirmation.** Users are now asked to confirm
      before deleting individual memory entries, with the memory content displayed
      for review. [#22888](https://github.com/open-webui/open-webui/pull/22888)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001FAE7 **Memory modal event bubbling.** Fixed an issue where clicking
      the Delete button in the Memory management modal would also open the Edit Memory
      modal due to event bubbling. [#22783](https://github.com/open-webui/open-webui/issues/22783)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F9E9 **Memory tool registration.** Models with capabilities.memory:
      true now correctly have memory tools available for execution, fixing a retry
      loop where add_memory appeared in the tool schema but was not registered for
      backend execution. [#22666](https://github.com/open-webui/open-webui/issues/22666),
      [#22675](https://github.com/open-webui/open-webui/pull/22675), [Commit](https://github.com/open-webui/open-webui/commit/d9339919046c3e977f313f603782d220aab4257f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-memory-and-personalization-changes-in-v0-8-11
  source_release: open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69
  source_type: github_releases
  theme: memory
  title: 4 Memory and Personalization changes in v0.8.11
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-03-17-docs-document-tool-exclusion-from-memory-via-deny-policy-by-abhijit-2592-in-http|docs:
  document tool exclusion from memory via deny policy]]'
- '[[Changes/Codex CLI/2026-03-19-4-memory-and-personalization-changes-in-rust-v0-116-0|4
  Memory and Personalization changes in rust-v0.116.0]]'
- '[[Changes/Gemini CLI/2026-03-24-refactor-core-align-jit-memory-placement-with-tiered-context-model-by-sandytao52|refactor(core):
  align JIT memory placement with tiered context model]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69]]'
source_type: github_releases
theme: memory
title: 4 Memory and Personalization changes in v0.8.11
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Memory and Personalization changes in v0.8.11

**Open WebUI** · 2026-03-25 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.11) · from [[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|v0.8.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧠 **Memory management search and sort.** Users can now search and sort their personal memories in the Memory management modal, making it easier to find specific memories. [Commit](https://github.com/open-webui/open-webui/commit/47ab4c71d50fd631b04c95f2febb085dd0a13083)

> 💡 **Memory deletion confirmation.** Users are now asked to confirm before deleting individual memory entries, with the memory content displayed for review. [#22888](https://github.com/open-webui/open-webui/pull/22888)

> 🫧 **Memory modal event bubbling.** Fixed an issue where clicking the Delete button in the Memory management modal would also open the Edit Memory modal due to event bubbling. [#22783](https://github.com/open-webui/open-webui/issues/22783)

> 🧩 **Memory tool registration.** Models with capabilities.memory: true now correctly have memory tools available for execution, fixing a retry loop where add_memory appeared in the tool schema but was not registered for backend execution. [#22666](https://github.com/open-webui/open-webui/issues/22666), [#22675](https://github.com/open-webui/open-webui/pull/22675), [Commit](https://github.com/open-webui/open-webui/commit/d9339919046c3e977f313f603782d220aab4257f)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-25-4-editor-experience-changes-in-v0-8-11|4 Editor Experience changes in v0.8.11]] · Editor Experience
- [[Changes/Open WebUI/2026-03-25-rag-query-generation-robustness-the-rag-query-generation-web-search-and-image-ge|🔍 RAG query generation robustness. The RAG query generation, web search…]] · Image Generation
- [[Changes/Open WebUI/2026-03-25-shared-chat-viewing-crash-shared-chats-can-now-be-viewed-by-unauthenticated-user|🐛 Shared chat viewing crash. Shared chats can now be viewed by unauthenticated…]] · Collaboration
- [[Changes/Open WebUI/2026-03-25-11-account-and-access-changes-in-v0-8-11|11 Account and Access changes in v0.8.11]] · Account and Access
- [[Changes/Open WebUI/2026-03-25-3-context-window-changes-in-v0-8-11|3 Context Window changes in v0.8.11]] · Context Window
- [[Changes/Open WebUI/2026-03-25-2-search-and-browsing-changes-in-v0-8-11|2 Search and Browsing changes in v0.8.11]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-25-2-files-and-data-changes-in-v0-8-11|2 Files and Data changes in v0.8.11]] · Files and Data
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
## Nearby in Memory and Personalization

- Earlier: 2026-03-24 · Gemini CLI · [[Changes/Gemini CLI/2026-03-24-refactor-core-align-jit-memory-placement-with-tiered-context-model-by-sandytao52|refactor(core): align JIT memory placement with tiered context model]]
- Later: 2026-03-26 · Codex CLI · [[Changes/Codex CLI/2026-03-26-15175-chore-morpheus-does-not-generate-memories-jif-oai|♯15175 chore: morpheus does not generate memories @jif-oai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-25-a098c2&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-25-4-memory-and-personalization-changes-in-v0-8-11.md%0ACard%20ID%3A%20open-webui-2026-03-25-a098c2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->