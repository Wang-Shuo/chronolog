---
card_id: dify-2025-09-22-a97ee7
date: '2025-09-22'
description: 'Dify · 2025-09-22 · Apps and Integrations: 12 changes in 1.9.0 – Orchestrating
  Knowledge, Powering Workflows — **With the brand-new orchestration interface for…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 914
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 89f82d6cff802827589b24dc2ca99c7edd491a9114f95da35db3db0da1451003
product: dify
product_name: Dify
record:
  card_id: dify-2025-09-22-a97ee7
  comparison: ''
  date: '2025-09-22'
  description: 'Dify — 1.9.0 – Orchestrating Knowledge, Powering Workflows: 12 Apps
    and Integrations changes'
  evidence:
  - quote: '**With the brand-new orchestration interface for knowledge pipelines**,
      we introduce a **fundamental architectural upgrade** that reshapes how document
      processing are designed and executed, providing a more modular and flexible
      workflow that enables users to **orchestrate** every stage of the pipeline.
      **Enhanced with a wide range of powerful plugins available in the marketplace**,
      it empowers users to flexibly integrate diverse data sources and processing
      tools. Ultimately, this architecture enables building **highly customized, domain-specific
      RAG solutions** that meet enterprises’ growing demands for scalability, adaptability,
      and precision.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: 'Previously, Dify''s RAG users still encounter persistent challenges in
      real-world adoption — from inaccurate knowledge retrieval and information loss
      to limited data integration and extensibility. Common pain points include:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: "\U0001F517 restricted integration of data sources"
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: Each knowledge base can support multiple data sources. You can seamlessly
      integrate **local files, online documents, cloud drives, and web crawlers**
      through a plugin-based ingestion framework. Developers can extend the ecosystem
      with new data-source plugins, while marketplace processors handle specialized
      use cases like formulas, spreadsheets, and image parsing — ensuring accurate
      ingestion and structured representation.
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: In addition to General and Parent-Child modes, the new **Q&A Processor
      plugin** supports Q&A structures. This expands coverage for more use cases,
      balancing retrieval precision with contextual completeness.
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: A new plugin layer that allows extending engine functionality without modifying
      core code. It can monitor states, send commands, and support custom monitoring.
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: 'refactor: improve plugin version validation to support full semantic versioning
      by @laipz8200 in https://github.com/langgenius/dify/pull/25161'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: add type annotations for Python SDK ChatClient Class by @EchterTimo in
      https://github.com/langgenius/dify/pull/24018
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: 'feat: add MCP server headers support #22718 by @Cluas in https://github.com/langgenius/dify/pull/24760'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: 'chore(deps): bump clickzetta-connector-python from 0.8.102 to 0.8.104
      in /api by @dependabot[bot] in https://github.com/langgenius/dify/pull/25697'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: 'chore(deps-dev): bump eslint-plugin-storybook from 0.11.6 to 9.0.7 in
      /web by @dependabot[bot] in https://github.com/langgenius/dify/pull/26011'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: 'Add Full-Text & Hybrid Search Support to Baidu Vector DB and Update SDK,
      Closes #25982 by @WayneCao in https://github.com/langgenius/dify/pull/25983'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 12-apps-and-integrations-changes-in-1-9-0
  source_release: dify-2025-09-22-1-9-0-github-249001568-ef530801
  source_type: github_releases
  theme: apps-integrations
  title: 12 Apps and Integrations changes in 1.9.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2025-09-17-onedrive-integration-was-fixed-after-recent-breakage-restoring-reliable-account|☁️
  OneDrive integration was fixed after recent breakage, restoring reliable account…]]'
- '[[Changes/Replit/2025-09-19-mobile-connectors-support|Mobile connectors support]]'
- '[[Changes/Cline/2025-09-20-feat-oca-ui-add-oca-provider-with-model-picker-and-auth-integration-by-nihar-ora|feat(oca-ui):
  add OCA provider with model picker and auth integration]]'
source_release: '[[Releases/Dify/dify-2025-09-22-1-9-0-github-249001568-ef530801|dify-2025-09-22-1-9-0-github-249001568-ef530801]]'
source_type: github_releases
theme: apps-integrations
title: 12 Apps and Integrations changes in 1.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Apps and Integrations changes in 1.9.0

**Dify** · 2025-09-22 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.9.0) · from [[Releases/Dify/dify-2025-09-22-1-9-0-github-249001568-ef530801|1.9.0 – Orchestrating Knowledge, Powering Workflows]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **With the brand-new orchestration interface for knowledge pipelines**, we introduce a **fundamental architectural upgrade** that reshapes how document processing are designed and executed, providing a more modular and flexible workflow that enables users to **orchestrate** every stage of the pipeline. **Enhanced with a wide range of powerful plugins available in the marketplace**, it empowers users to flexibly integrate diverse data sources and processing tools. Ultimately, this architecture enables building **highly customized, domain-specific RAG solutions** that meet enterprises’ growing demands for scalability, adaptability, and precision.

> Previously, Dify's RAG users still encounter persistent challenges in real-world adoption — from inaccurate knowledge retrieval and information loss to limited data integration and extensibility. Common pain points include:

> 🔗 restricted integration of data sources

> Each knowledge base can support multiple data sources. You can seamlessly integrate **local files, online documents, cloud drives, and web crawlers** through a plugin-based ingestion framework. Developers can extend the ecosystem with new data-source plugins, while marketplace processors handle specialized use cases like formulas, spreadsheets, and image parsing — ensuring accurate ingestion and structured representation.

> In addition to General and Parent-Child modes, the new **Q&A Processor plugin** supports Q&A structures. This expands coverage for more use cases, balancing retrieval precision with contextual completeness.

> A new plugin layer that allows extending engine functionality without modifying core code. It can monitor states, send commands, and support custom monitoring.

> refactor: improve plugin version validation to support full semantic versioning by @laipz8200 in https://github.com/langgenius/dify/pull/25161

> add type annotations for Python SDK ChatClient Class by @EchterTimo in https://github.com/langgenius/dify/pull/24018

> feat: add MCP server headers support #22718 by @Cluas in https://github.com/langgenius/dify/pull/24760

> chore(deps): bump clickzetta-connector-python from 0.8.102 to 0.8.104 in /api by @dependabot[bot] in https://github.com/langgenius/dify/pull/25697

> chore(deps-dev): bump eslint-plugin-storybook from 0.11.6 to 9.0.7 in /web by @dependabot[bot] in https://github.com/langgenius/dify/pull/26011

> Add Full-Text & Hybrid Search Support to Baidu Vector DB and Update SDK, Closes #25982 by @WayneCao in https://github.com/langgenius/dify/pull/25983

Source: https://github.com/langgenius/dify/releases/tag/1.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-09-22-5-model-support-changes-in-1-9-0|5 Model Support changes in 1.9.0]] · Model Support
- [[Changes/Dify/2025-09-22-customize-and-share-pipelines-by-importing-exporting-via-dsl-for-easier-reusabil|🔄 Customize and share pipelines by importing/exporting via DSL for easier…]] · Collaboration
- [[Changes/Dify/2025-09-22-5-safety-and-privacy-changes-in-1-9-0|5 Safety and Privacy changes in 1.9.0]] · Safety and Privacy
- [[Changes/Dify/2025-09-22-chore-remove-weird-account-login-by-zalcit-in-https-github-com-langgenius-dify-p|chore: remove weird account login]] · Account and Access
- [[Changes/Dify/2025-09-22-feat-add-circular-scrolling-to-gotoanything-command-menu-by-lyzno1-in-https-gith|feat: add circular scrolling to GotoAnything command menu]] · Interface Experience
- [[Changes/Dify/2025-09-22-12-developer-workflow-changes-in-1-9-0|12 Developer Workflow changes in 1.9.0]] · Developer Workflow
- [[Changes/Dify/2025-09-22-multimodal-embedding-support-richer-content-types-beyond-text|Multimodal Embedding: Support richer content types beyond text]] · Multimodal Input
- [[Changes/Dify/2025-09-22-6-files-and-data-changes-in-1-9-0|6 Files and Data changes in 1.9.0]] · Files and Data
- [[Changes/Dify/2025-09-22-5-automation-and-scheduling-changes-in-1-9-0|5 Automation and Scheduling changes in 1.9.0]] · Automation and Scheduling
- [[Changes/Dify/2025-09-22-5-reliability-and-performance-changes-in-1-9-0|5 Reliability and Performance changes in 1.9.0]] · Reliability and Performance
- [[Changes/Dify/2025-09-22-example-of-no-unstable-context-value-by-asukaminato0721-in-https-github-com-lang|example of no-unstable-context-value]] · Context Window
- [[Changes/Dify/2025-09-22-185-other-changes-in-1-9-0|185 other changes in 1.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-09-20 · Cline · [[Changes/Cline/2025-09-20-feat-oca-ui-add-oca-provider-with-model-picker-and-auth-integration-by-nihar-ora|feat(oca-ui): add OCA provider with model picker and auth integration]]
- Later: 2025-09-22 · ElevenLabs · [[Changes/ElevenLabs/2025-09-22-deprecated-endpoints|Deprecated Endpoints]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-09-22-a97ee7&body=Card%3A%20Changes%2FDify%2F2025-09-22-12-apps-and-integrations-changes-in-1-9-0.md%0ACard%20ID%3A%20dify-2025-09-22-a97ee7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->