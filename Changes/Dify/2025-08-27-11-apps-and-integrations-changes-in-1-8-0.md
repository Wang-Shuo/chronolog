---
card_id: dify-2025-08-27-4659a9
date: '2025-08-27'
description: 'Dify · 2025-08-27 · Apps and Integrations: 11 changes in v1.8.0 - Async
  workflows meet multi-model management with OAuth-powered integrations. — **Dark
  Mode…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 888
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8894d5637624273cfa529fe9eb198ebfe285c4dff846f2d06c1837dd3182450c
product: dify
product_name: Dify
record:
  card_id: dify-2025-08-27-4659a9
  comparison: ''
  date: '2025-08-27'
  description: 'Dify — v1.8.0 - Async workflows meet multi-model management with OAuth-powered
    integrations.: 11 Apps and Integrations changes'
  evidence:
  - quote: '**Dark Mode Improvements**: Multiple dark mode fixes including backdrop-blur
      for plugin dropdowns, hover button contrast, and embedded modal icons. Thanks
      to @lyzno1 and team!'
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  - quote: '**Comprehensive Test Coverage**: Added testcontainers-based integration
      tests for multiple services including workflow app, website, auth, conversation,
      and more. Massive thanks to @NeatGuyCoding for this extensive testing effort!'
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  - quote: '**Configurable Plugin Buffer Sizes**: Added configurable stdio buffer
      sizes for plugins in compose file. Thanks to @crazywoola! (#23980)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  - quote: '**API Documentation**: Enhanced API documentation for files endpoint,
      MCP, and service API. Thanks to @laipz8200!'
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  - quote: '**AST-Grep Integration**: Added ast-grep tool for maintaining codebase
      consistency. Thanks to @asukaminato0721! (#24149)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  - quote: Feat/improved mcp timeout configs by @IthacaDream in https://github.com/langgenius/dify/pull/23605
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  - quote: 'chore: improved type annotations in MCP-related codes by @IthacaDream
      in https://github.com/langgenius/dify/pull/23984'
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  - quote: 'chore: add configurable stdio buffer sizes for plugins in compose file
      by @crazywoola in https://github.com/langgenius/dify/pull/23980'
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  - quote: Mcp support resource discovery by @CodeSpaceiiii in https://github.com/langgenius/dify/pull/24223
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  - quote: 'feat: API docs for mcp by @laipz8200 in https://github.com/langgenius/dify/pull/24424'
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  - quote: 'refactor: unify blob chunk merging logic for plugin tool and agent by
      @Yeuoly in https://github.com/langgenius/dify/pull/24575'
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 11-apps-and-integrations-changes-in-1-8-0
  source_release: dify-2025-08-27-1-8-0-github-242787340-c7104f29
  source_type: github_releases
  theme: apps-integrations
  title: 11 Apps and Integrations changes in 1.8.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2025-08-21-5-apps-and-integrations-changes-in-v0-6-23|5 Apps
  and Integrations changes in v0.6.23]]'
- "[[Changes/Open WebUI/2025-08-22-tool-server-loading-and-visibility-restored-resolved-an-issue-where-connected-to|\U0001F6E0️
  Tool Server Loading and Visibility Restored]]"
- '[[Changes/Codex CLI/2025-08-26-5-apps-and-integrations-changes-in-rust-v0-24-0|5
  Apps and Integrations changes in rust-v0.24.0]]'
source_release: '[[Releases/Dify/dify-2025-08-27-1-8-0-github-242787340-c7104f29|dify-2025-08-27-1-8-0-github-242787340-c7104f29]]'
source_type: github_releases
theme: apps-integrations
title: 11 Apps and Integrations changes in 1.8.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Apps and Integrations changes in 1.8.0

**Dify** · 2025-08-27 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.8.0) · from [[Releases/Dify/dify-2025-08-27-1-8-0-github-242787340-c7104f29|v1.8.0 - Async workflows meet multi-model management with OAuth-powered integrations.]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Dark Mode Improvements**: Multiple dark mode fixes including backdrop-blur for plugin dropdowns, hover button contrast, and embedded modal icons. Thanks to @lyzno1 and team!

> **Comprehensive Test Coverage**: Added testcontainers-based integration tests for multiple services including workflow app, website, auth, conversation, and more. Massive thanks to @NeatGuyCoding for this extensive testing effort!

> **Configurable Plugin Buffer Sizes**: Added configurable stdio buffer sizes for plugins in compose file. Thanks to @crazywoola! (#23980)

> **API Documentation**: Enhanced API documentation for files endpoint, MCP, and service API. Thanks to @laipz8200!

> **AST-Grep Integration**: Added ast-grep tool for maintaining codebase consistency. Thanks to @asukaminato0721! (#24149)

> Feat/improved mcp timeout configs by @IthacaDream in https://github.com/langgenius/dify/pull/23605

> chore: improved type annotations in MCP-related codes by @IthacaDream in https://github.com/langgenius/dify/pull/23984

> chore: add configurable stdio buffer sizes for plugins in compose file by @crazywoola in https://github.com/langgenius/dify/pull/23980

> Mcp support resource discovery by @CodeSpaceiiii in https://github.com/langgenius/dify/pull/24223

> feat: API docs for mcp by @laipz8200 in https://github.com/langgenius/dify/pull/24424

> refactor: unify blob chunk merging logic for plugin tool and agent by @Yeuoly in https://github.com/langgenius/dify/pull/24575

Source: https://github.com/langgenius/dify/releases/tag/1.8.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-08-27-6-reliability-and-performance-changes-in-1-8-0|6 Reliability and Performance changes in 1.8.0]] · Reliability and Performance
- [[Changes/Dify/2025-08-27-2-editor-experience-changes-in-1-8-0|2 Editor Experience changes in 1.8.0]] · Editor Experience
- [[Changes/Dify/2025-08-27-4-files-and-data-changes-in-1-8-0|4 Files and Data changes in 1.8.0]] · Files and Data
- [[Changes/Dify/2025-08-27-5-interface-experience-changes-in-1-8-0|5 Interface Experience changes in 1.8.0]] · Interface Experience
- [[Changes/Dify/2025-08-27-loop-exit-conditions-fixed-loop-exit-condition-to-accept-variables-from-nodes-in|Loop Exit Conditions]] · Automation and Scheduling
- [[Changes/Dify/2025-08-27-7-account-and-access-changes-in-1-8-0|7 Account and Access changes in 1.8.0]] · Account and Access
- [[Changes/Dify/2025-08-27-5-agent-mode-changes-in-1-8-0|5 Agent Mode changes in 1.8.0]] · Agent Mode
- [[Changes/Dify/2025-08-27-localized-documentation-updated-localized-readme-files-to-link-to-corresponding|Localized Documentation: Updated localized README files to link to corresponding…]] · Accessibility and Localization
- [[Changes/Dify/2025-08-27-9-model-support-changes-in-1-8-0|9 Model Support changes in 1.8.0]] · Model Support
- [[Changes/Dify/2025-08-27-3-developer-workflow-changes-in-1-8-0|3 Developer Workflow changes in 1.8.0]] · Developer Workflow
- [[Changes/Dify/2025-08-27-7-safety-and-privacy-changes-in-1-8-0|7 Safety and Privacy changes in 1.8.0]] · Safety and Privacy
- [[Changes/Dify/2025-08-27-146-other-changes-in-1-8-0|146 other changes in 1.8.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-08-26 · Codex CLI · [[Changes/Codex CLI/2025-08-26-5-apps-and-integrations-changes-in-rust-v0-24-0|5 Apps and Integrations changes in rust-v0.24.0]]
- Later: 2025-08-27 · Gemini CLI · [[Changes/Gemini CLI/2025-08-27-2-apps-and-integrations-changes-in-v0-2-0|2 Apps and Integrations changes in v0.2.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-08-27-4659a9&body=Card%3A%20Changes%2FDify%2F2025-08-27-11-apps-and-integrations-changes-in-1-8-0.md%0ACard%20ID%3A%20dify-2025-08-27-4659a9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->