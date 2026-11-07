---
card_id: dify-2025-08-11-57bbd9
date: '2025-08-11'
description: 'Dify · 2025-08-11 · Apps and Integrations: 6 changes in v1.7.2 — **Notion
  Database Row Extraction**: The Notion Database integration now extracts rows in
  their…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 872
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ef549aa14ed7340df79623a2c0f5b47fa5e8ac76dcd91e8eeb4493b3286a17e9
product: dify
product_name: Dify
record:
  card_id: dify-2025-08-11-57bbd9
  comparison: ''
  date: '2025-08-11'
  description: 'Dify — v1.7.2: 6 Apps and Integrations changes'
  evidence:
  - quote: '**Notion Database Row Extraction**: The Notion Database integration now
      extracts rows in their original order and appends the Row Page URL. Thanks @ThreeFish-AI!
      #22646'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.2
  - quote: '**Tool JSON Response**: Datetime and UUID are now supported in tool JSON
      responses, making those integrations even more powerful. Kudos to @jiangbo721!
      #22738'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.2
  - quote: retention of data filled on tab switch for tool plugin by @jubinsoni in
      https://github.com/langgenius/dify/pull/23323
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.2
  - quote: 'feat: Add Clickzetta Lakehouse vector database integration by @yunqiqiliang
      in https://github.com/langgenius/dify/pull/22551'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.2
  - quote: 'feat: improved MCP timeout by @IthacaDream in https://github.com/langgenius/dify/pull/23546'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.2
  - quote: 'Revert "feat: improved MCP timeout" by @crazywoola in https://github.com/langgenius/dify/pull/23602'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 6-apps-and-integrations-changes-in-1-7-2
  source_release: dify-2025-08-11-1-7-2-github-238903756-6cc5a2a0
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in 1.7.2
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-08-06-26-apps-and-integrations-changes-in-v0-1-18|26
  Apps and Integrations changes in v0.1.18]]'
- '[[Changes/Gamma/2025-08-08-we-ve-just-launched-our-generate-api-in-beta-for-gamma-pro-users-now-you-can-cre|We’ve
  just launched our Generate API in beta for Gamma Pro users! Now you can…]]'
- '[[Changes/Open WebUI/2025-08-09-7-apps-and-integrations-changes-in-v0-6-19|7 Apps
  and Integrations changes in v0.6.19]]'
source_release: '[[Releases/Dify/dify-2025-08-11-1-7-2-github-238903756-6cc5a2a0|dify-2025-08-11-1-7-2-github-238903756-6cc5a2a0]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in 1.7.2
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in 1.7.2

**Dify** · 2025-08-11 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.7.2) · from [[Releases/Dify/dify-2025-08-11-1-7-2-github-238903756-6cc5a2a0|v1.7.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Notion Database Row Extraction**: The Notion Database integration now extracts rows in their original order and appends the Row Page URL. Thanks @ThreeFish-AI! #22646

> **Tool JSON Response**: Datetime and UUID are now supported in tool JSON responses, making those integrations even more powerful. Kudos to @jiangbo721! #22738

> retention of data filled on tab switch for tool plugin by @jubinsoni in https://github.com/langgenius/dify/pull/23323

> feat: Add Clickzetta Lakehouse vector database integration by @yunqiqiliang in https://github.com/langgenius/dify/pull/22551

> feat: improved MCP timeout by @IthacaDream in https://github.com/langgenius/dify/pull/23546

> Revert "feat: improved MCP timeout" by @crazywoola in https://github.com/langgenius/dify/pull/23602

Source: https://github.com/langgenius/dify/releases/tag/1.7.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-08-11-internationalization-i18n-numerous-i18n-fixes-and-enhancements-across-the-board|Internationalization (i18n): Numerous i18n fixes and enhancements across the board]] · Accessibility and Localization
- [[Changes/Dify/2025-08-11-4-developer-workflow-changes-in-1-7-2|4 Developer Workflow changes in 1.7.2]] · Developer Workflow
- [[Changes/Dify/2025-08-11-3-safety-and-privacy-changes-in-1-7-2|3 Safety and Privacy changes in 1.7.2]] · Safety and Privacy
- [[Changes/Dify/2025-08-11-minor-fix-wrong-position-of-retry-document-indexing-task-time-elapsed-by-neatguy|minor fix: wrong position of retry_document_indexing_task time elapsed]] · Files and Data
- [[Changes/Dify/2025-08-11-fixing-chat-window-api-recall-fix-on-changing-browser-tab-or-window-by-jubinsoni|fixing chat window api recall fix on changing browser tab or window]] · Editor Experience
- [[Changes/Dify/2025-08-11-chore-remove-unused-variable-pruned-memory-by-hyongtao-db-in-https-github-com-la|Chore: remove unused variable pruned_memory]] · Memory and Personalization
- [[Changes/Dify/2025-08-11-you-can-now-easily-find-nodes-in-the-workflow-editor-using-the-new-search-featur|Easily find nodes in the workflow editor using the new search feature by @croatialu…]] · Editor Experience
- [[Changes/Dify/2025-08-11-4-interface-experience-changes-in-1-7-2|4 Interface Experience changes in 1.7.2]] · Interface Experience
- [[Changes/Dify/2025-08-11-feat-enhance-the-alignment-logic-of-the-nodes-in-the-context-menu-by-zeroz-lab-i|feat: Enhance the alignment logic of the nodes in the context menu]] · Context Window
- [[Changes/Dify/2025-08-11-testcontainers-tests-we-re-serious-about-stability-neatguycoding-and-others-have|Testcontainers Tests: We're serious about stability!]] · Reliability and Performance
- [[Changes/Dify/2025-08-11-92-other-changes-in-1-7-2|92 other changes in 1.7.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-08-09 · Open WebUI · [[Changes/Open WebUI/2025-08-09-7-apps-and-integrations-changes-in-v0-6-19|7 Apps and Integrations changes in v0.6.19]]
- Later: 2025-08-11 · ElevenLabs · [[Changes/ElevenLabs/2025-08-11-sdks|SDKs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-08-11-57bbd9&body=Card%3A%20Changes%2FDify%2F2025-08-11-6-apps-and-integrations-changes-in-1-7-2.md%0ACard%20ID%3A%20dify-2025-08-11-57bbd9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.7.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->