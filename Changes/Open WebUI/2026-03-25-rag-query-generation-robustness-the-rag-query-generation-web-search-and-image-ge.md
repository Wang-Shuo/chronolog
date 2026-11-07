---
card_id: open-webui-2026-03-25-2bac21
date: '2026-03-25'
description: "Open WebUI · 2026-03-25 · Image Generation: \U0001F50D **RAG query generation
  robustness.** The RAG query generation, web search, and image generation handlers
  now…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2023-06-26-text-to-image-generation|Text-to-image
    generation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1003
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: image-generation
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: df531f72d3ce0007989db63ebe1a200cce5663f4ec996433682e0c3430ddc6be
product: open-webui
product_name: Open WebUI
record:
  ai_generated: true
  card_id: open-webui-2026-03-25-2bac21
  comparison: ''
  confidence: low
  date: '2026-03-25'
  description: "Open WebUI — v0.8.11: \U0001F50D **RAG query generation robustness.**
    The RAG query generation, web search, and image generation handlers now correctly
    extract JSON from model responses containing thinking tags by finding the last
    JSON block instead of the first, preventing \"No sources found\" errors with thinking
    models. [#21888](https://github.com/open-webui/open-webui/issues/21888), [Commit](https://github.com/open-webui/open-webui/commit/c0fcbc5b4cb29012e2913983c632edc5d24b9aea)"
  evidence:
  - quote: "\U0001F50D **RAG query generation robustness.** The RAG query generation,
      web search, and image generation handlers now correctly extract JSON from model
      responses containing thinking tags by finding the last JSON block instead of
      the first, preventing \"No sources found\" errors with thinking models. [#21888](https://github.com/open-webui/open-webui/issues/21888),
      [Commit](https://github.com/open-webui/open-webui/commit/c0fcbc5b4cb29012e2913983c632edc5d24b9aea)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: rag-query-generation-robustness-the-rag-query-generation-web-search-and-image-ge
  source_release: open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69
  source_type: github_releases
  theme: image-generation
  theme_matches:
  - matched_terms:
    - image generation
    score: 120
    theme: image-generation
  - matched_terms:
    - model
    - models
    score: 100
    theme: model-support
  - matched_terms:
    - web search
    score: 60
    theme: search-browsing
  theme_resolution: manual-semantic-rule-v1
  title: "\U0001F50D **RAG query generation robustness.** The RAG query generation,
    web search…"
  type: change
related_changes:
- '[[Changes/Lovable/2026-03-16-image-generation-updates|Image generation updates]]'
- '[[Changes/v0/2026-03-16-added-image-generation-capability-to-the-plan-agent|Added
  image generation capability to the Plan agent]]'
- '[[Changes/Descript/2026-03-17-generated-avatar-images-are-now-saved-in-your-project-files|Generated
  avatar images are now saved in your project files]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69]]'
source_type: github_releases
theme: image-generation
title: "\U0001F50D RAG query generation robustness. The RAG query generation, web
  search…"
type: change
---

<!-- chronolog:begin region="header" -->
# 🔍 **RAG query generation robustness.** The RAG query generation, web search…

**Open WebUI** · 2026-03-25 · [[Themes/image-generation|Image Generation]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.11) · from [[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|v0.8.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> 🔍 **RAG query generation robustness.** The RAG query generation, web search, and image generation handlers now correctly extract JSON from model responses containing thinking tags by finding the last JSON block instead of the first, preventing "No sources found" errors with thinking models. [#21888](https://github.com/open-webui/open-webui/issues/21888), [Commit](https://github.com/open-webui/open-webui/commit/c0fcbc5b4cb29012e2913983c632edc5d24b9aea)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-25-4-editor-experience-changes-in-v0-8-11|4 Editor Experience changes in v0.8.11]] · Editor Experience
- [[Changes/Open WebUI/2026-03-25-shared-chat-viewing-crash-shared-chats-can-now-be-viewed-by-unauthenticated-user|🐛 Shared chat viewing crash. Shared chats can now be viewed by unauthenticated…]] · Collaboration
- [[Changes/Open WebUI/2026-03-25-11-account-and-access-changes-in-v0-8-11|11 Account and Access changes in v0.8.11]] · Account and Access
- [[Changes/Open WebUI/2026-03-25-3-context-window-changes-in-v0-8-11|3 Context Window changes in v0.8.11]] · Context Window
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
## Nearby in Image Generation

- Earlier: 2026-03-17 · Descript · [[Changes/Descript/2026-03-17-generated-avatar-images-are-now-saved-in-your-project-files|Generated avatar images are now saved in your project files]]
- Later: 2026-03-26 · Codex CLI · [[Changes/Codex CLI/2026-03-26-2-image-generation-changes-in-rust-v0-117-0|2 Image Generation changes in rust-v0.117.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-06-26 · Descript · [[Changes/Descript/2023-06-26-text-to-image-generation|Text-to-image generation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-25-2bac21&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-25-rag-query-generation-robustness-the-rag-query-generation-web-search-and-image-ge.md%0ACard%20ID%3A%20open-webui-2026-03-25-2bac21%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->