---
card_id: dify-2025-08-27-17f78d
date: '2025-08-27'
description: 'Dify · 2025-08-27 · Reliability and Performance: 6 changes in v1.8.0
  - Async workflows meet multi-model management with OAuth-powered integrations. —
  **Default…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2473
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 948fdea35f574a014f14ad2971ffc5ee58ae7910d5b890d60959286082eac24a
product: dify
product_name: Dify
record:
  card_id: dify-2025-08-27-17f78d
  comparison: ''
  date: '2025-08-27'
  description: 'Dify — v1.8.0 - Async workflows meet multi-model management with OAuth-powered
    integrations.: 6 Reliability and Performance changes'
  evidence:
  - quote: '**Default Values for Workflow Variables**: All workflow start node variable
      types now support default values, making workflows more robust. Thanks to @17hz!
      (#24129)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  - quote: '**Database Performance**: Fixed major performance issue by removing provider
      table updates on every message creation. Thanks to @QuantumGhost! (#24520)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  - quote: '**Async WorkflowRun/WorkflowNodeRun Repositories**: Implemented asynchronous
      repositories for workflow execution, delivering dramatic performance improvements.
      This architectural change enables non-blocking operations during workflow runs,
      with early testing showing execution times nearly halved in typical workflows.
      This optimization particularly benefits complex workflows with multiple nodes
      and parallel operations. Thanks to @xinlmain for this game-changing performance
      enhancement! (#20050)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  - quote: '**Dataset Cleanup**: Optimized dataset cleanup task for better performance.
      Thanks to @aopstudio! (#24467)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  - quote: 'feat: Add an asynchronous repository to improve workflow performance by
      @xinlmain in https://github.com/langgenius/dify/pull/20050'
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  - quote: 'feat: integrate flask-orjson for improved JSON serialization performance
      by @laipz8200 in https://github.com/langgenius/dify/pull/23935'
    source_release: https://github.com/langgenius/dify/releases/tag/1.8.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 6-reliability-and-performance-changes-in-1-8-0
  source_release: dify-2025-08-27-1-8-0-github-242787340-c7104f29
  source_type: github_releases
  theme: reliability-performance
  title: 6 Reliability and Performance changes in 1.8.0
  type: change
related_changes:
- '[[Changes/Devin/2025-08-22-various-reliability-performance-and-usability-improvements-across-the-app|Various
  reliability, performance, and usability improvements across the app]]'
- '[[Changes/Raycast/2025-08-25-we-are-happy-to-introduce-a-new-and-faster-file-system-indexer-for-windows-by-en|Raycast
  introduces a new and faster file system indexer for Windows]]'
- '[[Changes/Codex CLI/2025-08-26-2-reliability-and-performance-changes-in-rust-v0-24-0|2
  Reliability and Performance changes in rust-v0.24.0]]'
source_release: '[[Releases/Dify/dify-2025-08-27-1-8-0-github-242787340-c7104f29|dify-2025-08-27-1-8-0-github-242787340-c7104f29]]'
source_type: github_releases
theme: reliability-performance
title: 6 Reliability and Performance changes in 1.8.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Reliability and Performance changes in 1.8.0

**Dify** · 2025-08-27 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.8.0) · from [[Releases/Dify/dify-2025-08-27-1-8-0-github-242787340-c7104f29|v1.8.0 - Async workflows meet multi-model management with OAuth-powered integrations.]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Default Values for Workflow Variables**: All workflow start node variable types now support default values, making workflows more robust. Thanks to @17hz! (#24129)

> **Database Performance**: Fixed major performance issue by removing provider table updates on every message creation. Thanks to @QuantumGhost! (#24520)

> **Async WorkflowRun/WorkflowNodeRun Repositories**: Implemented asynchronous repositories for workflow execution, delivering dramatic performance improvements. This architectural change enables non-blocking operations during workflow runs, with early testing showing execution times nearly halved in typical workflows. This optimization particularly benefits complex workflows with multiple nodes and parallel operations. Thanks to @xinlmain for this game-changing performance enhancement! (#20050)

> **Dataset Cleanup**: Optimized dataset cleanup task for better performance. Thanks to @aopstudio! (#24467)

> feat: Add an asynchronous repository to improve workflow performance by @xinlmain in https://github.com/langgenius/dify/pull/20050

> feat: integrate flask-orjson for improved JSON serialization performance by @laipz8200 in https://github.com/langgenius/dify/pull/23935

Source: https://github.com/langgenius/dify/releases/tag/1.8.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-08-27-2-editor-experience-changes-in-1-8-0|2 Editor Experience changes in 1.8.0]] · Editor Experience
- [[Changes/Dify/2025-08-27-11-apps-and-integrations-changes-in-1-8-0|11 Apps and Integrations changes in 1.8.0]] · Apps and Integrations
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
## Nearby in Reliability and Performance

- Earlier: 2025-08-26 · Codex CLI · [[Changes/Codex CLI/2025-08-26-2-reliability-and-performance-changes-in-rust-v0-24-0|2 Reliability and Performance changes in rust-v0.24.0]]
- Later: 2025-08-28 · Open WebUI · [[Changes/Open WebUI/2025-08-28-2-reliability-and-performance-changes-in-v0-6-26|2 Reliability and Performance changes in v0.6.26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-08-27-17f78d&body=Card%3A%20Changes%2FDify%2F2025-08-27-6-reliability-and-performance-changes-in-1-8-0.md%0ACard%20ID%3A%20dify-2025-08-27-17f78d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->