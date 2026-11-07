---
card_id: dify-2026-02-03-5b4a3a
date: '2026-02-03'
description: 'Dify · 2026-02-03 · Context Window: 5 changes in v1.12.0 - Introducing
  Summary Index: Smarter Retrieval with AI Summarization — Traditional vector search…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2330
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a79474bcd295b0afab587ebf82487b22937d22e336d25b09618be81f50963cda
product: dify
product_name: Dify
record:
  card_id: dify-2026-02-03-5b4a3a
  comparison: ''
  date: '2026-02-03'
  description: 'Dify — v1.12.0 - Introducing Summary Index: Smarter Retrieval with
    AI Summarization: 5 Context Window changes'
  evidence:
  - quote: Traditional vector search relies on raw chunk embeddings, which can miss
      semantic nuances and context when matching user queries. This is especially
      challenging for long documents or complex content where key information might
      be scattered across multiple chunks. Summary Index addresses this by creating
      concise, semantically-rich summaries for each document chunk, which are then
      vectorized and used as an additional retrieval layer.
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  - quote: '**Manual Summary Editing:** Allows you to manually edit and refine AI-generated
      summaries to better align with the original chunk content, ensuring summaries
      accurately reflect domain-specific terminology and context.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  - quote: Added support for registering and reading context in workflows.
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  - quote: 'refactor: refactor workflow context by @fatelei in https://github.com/langgenius/dify/pull/30607'
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  - quote: 'feat: workflow support register context and read context by @fatelei in
      https://github.com/langgenius/dify/pull/31265'
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 5-context-window-changes-in-1-12-0
  source_release: dify-2026-02-03-1-12-0-github-282591953-290f70e4
  source_type: github_releases
  theme: context-window
  title: 5 Context Window changes in 1.12.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-01-31-core-add-copilot-specific-provider-to-properly-handle-reasoning-tokens|Core
  Add Copilot-specific provider to properly handle reasoning tokens]]'
- '[[Changes/Codex CLI/2026-02-02-2-context-window-changes-in-rust-v0-94-0|2 Context
  Window changes in rust-v0.94.0]]'
- '[[Changes/Claude Code/2026-02-03-added-pages-parameter-to-the-read-tool-for-pdfs-allowing-specific-page-ranges-to|Added
  pages parameter to the Read tool for PDFs, allowing specific page ranges…]]'
source_release: '[[Releases/Dify/dify-2026-02-03-1-12-0-github-282591953-290f70e4|dify-2026-02-03-1-12-0-github-282591953-290f70e4]]'
source_type: github_releases
theme: context-window
title: 5 Context Window changes in 1.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Context Window changes in 1.12.0

**Dify** · 2026-02-03 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.12.0) · from [[Releases/Dify/dify-2026-02-03-1-12-0-github-282591953-290f70e4|v1.12.0 - Introducing Summary Index: Smarter Retrieval with AI Summarization]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Traditional vector search relies on raw chunk embeddings, which can miss semantic nuances and context when matching user queries. This is especially challenging for long documents or complex content where key information might be scattered across multiple chunks. Summary Index addresses this by creating concise, semantically-rich summaries for each document chunk, which are then vectorized and used as an additional retrieval layer.

> **Manual Summary Editing:** Allows you to manually edit and refine AI-generated summaries to better align with the original chunk content, ensuring summaries accurately reflect domain-specific terminology and context.

> Added support for registering and reading context in workflows.

> refactor: refactor workflow context by @fatelei in https://github.com/langgenius/dify/pull/30607

> feat: workflow support register context and read context by @fatelei in https://github.com/langgenius/dify/pull/31265

Source: https://github.com/langgenius/dify/releases/tag/1.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-02-03-2-developer-workflow-changes-in-1-12-0|2 Developer Workflow changes in 1.12.0]] · Developer Workflow
- [[Changes/Dify/2026-02-03-chore-hide-disable-try-tab-when-not-support-by-iamjoel-in-https-github-com-langg|chore: hide disable try tab when not support]] · Editor Experience
- [[Changes/Dify/2026-02-03-chore-improve-accessibility-for-learn-more-link-by-khmandarrin-in-https-github-c|chore: improve accessibility for learn more link]] · Accessibility and Localization
- [[Changes/Dify/2026-02-03-9-safety-and-privacy-changes-in-1-12-0|9 Safety and Privacy changes in 1.12.0]] · Safety and Privacy
- [[Changes/Dify/2026-02-03-5-model-support-changes-in-1-12-0|5 Model Support changes in 1.12.0]] · Model Support
- [[Changes/Dify/2026-02-03-7-files-and-data-changes-in-1-12-0|7 Files and Data changes in 1.12.0]] · Files and Data
- [[Changes/Dify/2026-02-03-9-agent-mode-changes-in-1-12-0|9 Agent Mode changes in 1.12.0]] · Agent Mode
- [[Changes/Dify/2026-02-03-3-multimodal-input-changes-in-1-12-0|3 Multimodal Input changes in 1.12.0]] · Multimodal Input
- [[Changes/Dify/2026-02-03-test-enhance-hittestingpage-tests-with-additional-coverage-for-rendering-and-sta|test: enhance HitTestingPage tests with additional coverage for rendering and state…]] · Interface Experience
- [[Changes/Dify/2026-02-03-2-enterprise-and-administration-changes-in-1-12-0|2 Enterprise and Administration changes in 1.12.0]] · Enterprise and Administration
- [[Changes/Dify/2026-02-03-feat-use-xdist-to-make-make-test-faster-by-yihong0618-in-https-github-com-langge|feat: use xdist to make make test faster]] · Reliability and Performance
- [[Changes/Dify/2026-02-03-refactor-contract-restructure-console-contracts-with-nested-billing-module-by-ly|refactor(contract): restructure console contracts with nested billing module]] · Pricing Model
- [[Changes/Dify/2026-02-03-3-account-and-access-changes-in-1-12-0|3 Account and Access changes in 1.12.0]] · Account and Access
- [[Changes/Dify/2026-02-03-14-apps-and-integrations-changes-in-1-12-0|14 Apps and Integrations changes in 1.12.0]] · Apps and Integrations
- [[Changes/Dify/2026-02-03-149-other-changes-in-1-12-0|149 other changes in 1.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-02-03 · Claude Code · [[Changes/Claude Code/2026-02-03-added-pages-parameter-to-the-read-tool-for-pdfs-allowing-specific-page-ranges-to|Added pages parameter to the Read tool for PDFs, allowing specific page ranges…]]
- Later: 2026-02-03 · Ollama · [[Changes/Ollama/2026-02-03-5-context-window-changes-in-v0-15-5|5 Context Window changes in v0.15.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-02-03-5b4a3a&body=Card%3A%20Changes%2FDify%2F2026-02-03-5-context-window-changes-in-1-12-0.md%0ACard%20ID%3A%20dify-2026-02-03-5b4a3a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->