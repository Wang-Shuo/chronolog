---
card_id: dify-2025-09-22-196c6e
date: '2025-09-22'
description: 'Dify · 2025-09-22 · Model Support: 5 changes in 1.9.0 – Orchestrating
  Knowledge, Powering Workflows — A new **ResponseCoordinator** handles streaming
  outputs…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 987
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4b573f1f4fc0d4b4a2410c84abfa164678a67c7171eb16d4dce94660fc03c9a6
product: dify
product_name: Dify
record:
  card_id: dify-2025-09-22-196c6e
  comparison: ''
  date: '2025-09-22'
  description: 'Dify — 1.9.0 – Orchestrating Knowledge, Powering Workflows: 5 Model
    Support changes'
  evidence:
  - quote: A new **ResponseCoordinator** handles streaming outputs from multiple nodes,
      such as token-by-token LLM generation or staged results from long-running tasks.
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: 'Minor fix: correct get_app_model mode for delete() by @hyongtao-code in
      https://github.com/langgenius/dify/pull/25082'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: 'feat: add reasoning format processing to LLMNode for <think> tag handling
      by @ultramancode in https://github.com/langgenius/dify/pull/23313'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: '[Chore/Refactor] Improve type annotations in models module by @laipz8200
      in https://github.com/langgenius/dify/pull/25281'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: Enhance LLM model configuration validation to include active status c…
      by @GareArc in https://github.com/langgenius/dify/pull/25759
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 5-model-support-changes-in-1-9-0
  source_release: dify-2025-09-22-1-9-0-github-249001568-ef530801
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in 1.9.0
  type: change
related_changes:
- '[[Changes/Ollama/2025-09-18-6-model-support-changes-in-v0-12-0|6 Model Support
  changes in v0.12.0]]'
- '[[Changes/Cline/2025-09-19-add-code-supernova-stealth-model-by-saoudrizwan-in-https-github-com-cline-cline|Add
  code-supernova stealth model]]'
- '[[Changes/Ollama/2025-09-21-2-model-support-changes-in-v0-12-1|2 Model Support
  changes in v0.12.1]]'
source_release: '[[Releases/Dify/dify-2025-09-22-1-9-0-github-249001568-ef530801|dify-2025-09-22-1-9-0-github-249001568-ef530801]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in 1.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in 1.9.0

**Dify** · 2025-09-22 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.9.0) · from [[Releases/Dify/dify-2025-09-22-1-9-0-github-249001568-ef530801|1.9.0 – Orchestrating Knowledge, Powering Workflows]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> A new **ResponseCoordinator** handles streaming outputs from multiple nodes, such as token-by-token LLM generation or staged results from long-running tasks.

> Minor fix: correct get_app_model mode for delete() by @hyongtao-code in https://github.com/langgenius/dify/pull/25082

> feat: add reasoning format processing to LLMNode for \<think> tag handling by @ultramancode in https://github.com/langgenius/dify/pull/23313

> [Chore/Refactor] Improve type annotations in models module by @laipz8200 in https://github.com/langgenius/dify/pull/25281

> Enhance LLM model configuration validation to include active status c… by @GareArc in https://github.com/langgenius/dify/pull/25759

Source: https://github.com/langgenius/dify/releases/tag/1.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-09-22-customize-and-share-pipelines-by-importing-exporting-via-dsl-for-easier-reusabil|🔄 Customize and share pipelines by importing/exporting via DSL for easier…]] · Collaboration
- [[Changes/Dify/2025-09-22-5-safety-and-privacy-changes-in-1-9-0|5 Safety and Privacy changes in 1.9.0]] · Safety and Privacy
- [[Changes/Dify/2025-09-22-chore-remove-weird-account-login-by-zalcit-in-https-github-com-langgenius-dify-p|chore: remove weird account login]] · Account and Access
- [[Changes/Dify/2025-09-22-feat-add-circular-scrolling-to-gotoanything-command-menu-by-lyzno1-in-https-gith|feat: add circular scrolling to GotoAnything command menu]] · Interface Experience
- [[Changes/Dify/2025-09-22-12-developer-workflow-changes-in-1-9-0|12 Developer Workflow changes in 1.9.0]] · Developer Workflow
- [[Changes/Dify/2025-09-22-multimodal-embedding-support-richer-content-types-beyond-text|Multimodal Embedding: Support richer content types beyond text]] · Multimodal Input
- [[Changes/Dify/2025-09-22-12-apps-and-integrations-changes-in-1-9-0|12 Apps and Integrations changes in 1.9.0]] · Apps and Integrations
- [[Changes/Dify/2025-09-22-6-files-and-data-changes-in-1-9-0|6 Files and Data changes in 1.9.0]] · Files and Data
- [[Changes/Dify/2025-09-22-5-automation-and-scheduling-changes-in-1-9-0|5 Automation and Scheduling changes in 1.9.0]] · Automation and Scheduling
- [[Changes/Dify/2025-09-22-5-reliability-and-performance-changes-in-1-9-0|5 Reliability and Performance changes in 1.9.0]] · Reliability and Performance
- [[Changes/Dify/2025-09-22-example-of-no-unstable-context-value-by-asukaminato0721-in-https-github-com-lang|example of no-unstable-context-value]] · Context Window
- [[Changes/Dify/2025-09-22-185-other-changes-in-1-9-0|185 other changes in 1.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-09-21 · Ollama · [[Changes/Ollama/2025-09-21-2-model-support-changes-in-v0-12-1|2 Model Support changes in v0.12.1]]
- Later: 2025-09-23 · Codex CLI · [[Changes/Codex CLI/2025-09-23-2-model-support-changes-in-rust-v0-40-0|2 Model Support changes in rust-v0.40.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-09-22-196c6e&body=Card%3A%20Changes%2FDify%2F2025-09-22-5-model-support-changes-in-1-9-0.md%0ACard%20ID%3A%20dify-2025-09-22-196c6e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->