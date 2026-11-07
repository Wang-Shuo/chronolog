---
card_id: open-webui-2025-09-25-4bea4d
date: '2025-09-25'
description: "Open WebUI · 2025-09-25 · Model Support: 4 changes in v0.6.31 — \U0001F4AC
  Channel models now support image processing, allowing AI assistants to view and
  analyze…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 990
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: deef3415df68b654cb94c24261d05a12d629eeff028f2dc3392ddad2b90e8f47
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-09-25-4bea4d
  comparison: ''
  date: '2025-09-25'
  description: 'Open WebUI — v0.6.31: 4 Model Support changes'
  evidence:
  - quote: "\U0001F4AC Channel models now support image processing, allowing AI assistants
      to view and analyze images shared in conversation threads. [Commit](https://github.com/open-webui/open-webui/commit/9f0010e234a6f40782a66021435d3c02b9c23639)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  - quote: "\U0001F4AC Attached conversation references now persist throughout the
      entire chat session, ensuring models can continue querying referenced conversations
      after multiple conversation turns. [#17750](https://github.com/open-webui/open-webui/issues/17750)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  - quote: "\U0001F4AC Chat jitter and delayed code block expansion in multi-model
      sessions were resolved by reverting dynamic CodeEditor loading, restoring stable
      rendering behavior. [#17715](https://github.com/open-webui/open-webui/pull/17715),
      [#17684](https://github.com/open-webui/open-webui/issues/17684)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  - quote: "\U0001F5D2️ Hidden models are now properly excluded from the notes section
      dropdown and default model selection, preventing users from accessing models
      they shouldn't see. [#17722](https://github.com/open-webui/open-webui/pull/17722)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-model-support-changes-in-v0-6-31
  source_release: open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in v0.6.31
  type: change
related_changes:
- '[[Changes/Ollama/2025-09-24-models-with-qwen3-s-architecture-including-moe-now-run-in-ollama-s-new-engine|Models
  with Qwen3''s architecture including MoE now run in Ollama''s new engine]]'
- '[[Changes/Cline/2025-09-25-refactor-append-stealth-models-on-readopenroutermodels-refreshopenroutermodels-b|refactor:
  append stealth models on readOpenRouterModels & refreshOpenRouterModels]]'
- '[[Changes/Gemini/2025-09-25-update-to-2-5-flash-in-gemini|Update to 2.5 Flash in
  Gemini]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead|open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in v0.6.31
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v0.6.31

**Open WebUI** · 2025-09-25 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.31) · from [[Releases/Open WebUI/open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead|v0.6.31]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 💬 Channel models now support image processing, allowing AI assistants to view and analyze images shared in conversation threads. [Commit](https://github.com/open-webui/open-webui/commit/9f0010e234a6f40782a66021435d3c02b9c23639)

> 💬 Attached conversation references now persist throughout the entire chat session, ensuring models can continue querying referenced conversations after multiple conversation turns. [#17750](https://github.com/open-webui/open-webui/issues/17750)

> 💬 Chat jitter and delayed code block expansion in multi-model sessions were resolved by reverting dynamic CodeEditor loading, restoring stable rendering behavior. [#17715](https://github.com/open-webui/open-webui/pull/17715), [#17684](https://github.com/open-webui/open-webui/issues/17684)

> 🗒️ Hidden models are now properly excluded from the notes section dropdown and default model selection, preventing users from accessing models they shouldn't see. [#17722](https://github.com/open-webui/open-webui/pull/17722)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-09-25-editor-collaboration-functionality-was-refactored-to-reduce-package-size-by-390k|⚡ Editor collaboration functionality was refactored to reduce package size by 390KB…]] · Collaboration
- [[Changes/Open WebUI/2025-09-25-4-apps-and-integrations-changes-in-v0-6-31|4 Apps and Integrations changes in v0.6.31]] · Apps and Integrations
- [[Changes/Open WebUI/2025-09-25-2-editor-experience-changes-in-v0-6-31|2 Editor Experience changes in v0.6.31]] · Editor Experience
- [[Changes/Open WebUI/2025-09-25-rag-query-generation-is-now-skipped-when-all-attached-files-are-set-to-full-cont|🔍 RAG query generation is now skipped when all attached files are set to full…]] · Context Window
- [[Changes/Open WebUI/2025-09-25-3-safety-and-privacy-changes-in-v0-6-31|3 Safety and Privacy changes in v0.6.31]] · Safety and Privacy
- [[Changes/Open WebUI/2025-09-25-enhanced-user-interface-accessibility-through-the-addition-of-unique-element-ids|♿ Enhanced user interface accessibility through the addition of unique element IDs…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-09-25-2-search-and-browsing-changes-in-v0-6-31|2 Search and Browsing changes in v0.6.31]] · Search and Browsing
- [[Changes/Open WebUI/2025-09-25-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-09-25-image-generation-model-selection-was-centralized-to-enable-dynamic-model-overrid|🎨 Image generation model selection was centralized to enable dynamic model override…]] · Image Generation
- [[Changes/Open WebUI/2025-09-25-4-interface-experience-changes-in-v0-6-31|4 Interface Experience changes in v0.6.31]] · Interface Experience
- [[Changes/Open WebUI/2025-09-25-file-upload-handling-was-improved-to-properly-recognize-uploaded-files-even-when|📎 File upload handling was improved to properly recognize uploaded files even…]] · Files and Data
- [[Changes/Open WebUI/2025-09-25-2-account-and-access-changes-in-v0-6-31|2 Account and Access changes in v0.6.31]] · Account and Access
- [[Changes/Open WebUI/2025-09-25-5-reliability-and-performance-changes-in-v0-6-31|5 Reliability and Performance changes in v0.6.31]] · Reliability and Performance
- [[Changes/Open WebUI/2025-09-25-2-developer-workflow-changes-in-v0-6-31|2 Developer Workflow changes in v0.6.31]] · Developer Workflow
- [[Changes/Open WebUI/2025-09-25-17-other-changes-in-v0-6-31|17 other changes in v0.6.31]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-09-25 · Gemini · [[Changes/Gemini/2025-09-25-update-to-2-5-flash-in-gemini|Update to 2.5 Flash in Gemini]]
- Later: 2025-09-25 · OpenHands · [[Changes/OpenHands/2025-09-25-set-claude-sonnet-output-token-limit|Set Claude Sonnet output token limit]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-09-25-4bea4d&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-09-25-4-model-support-changes-in-v0-6-31.md%0ACard%20ID%3A%20open-webui-2025-09-25-4bea4d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.31%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->