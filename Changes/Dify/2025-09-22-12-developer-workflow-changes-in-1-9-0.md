---
card_id: dify-2025-09-22-74092f
date: '2025-09-22'
description: 'Dify · 2025-09-22 · Developer Workflow: 12 changes in 1.9.0 – Orchestrating
  Knowledge, Powering Workflows — The Knowledge Pipeline provides a modularized and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 919
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b1c14955c1c36d3dd136522d3f6814c4696af0f89cd17ab80b51dfceebe68e99
product: dify
product_name: Dify
record:
  card_id: dify-2025-09-22-74092f
  comparison: ''
  date: '2025-09-22'
  description: 'Dify — 1.9.0 – Orchestrating Knowledge, Powering Workflows: 12 Developer
    Workflow changes'
  evidence:
  - quote: The Knowledge Pipeline provides a modularized and extensible workflow for
      knowledge ingestion and processing, while the Queue-based Graph Engine makes
      workflow execution more robust and controllable. We believe these will help
      you build and debug AI applications more smoothly, and we look forward to your
      experiences to help us continuously improve.
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: This provides safe iteration and debugging at every stage.
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: ❌ Insufficient debugging information
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: 'Debug mode: set `DEBUG=true` to enable DebugLoggingLayer.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: '[GraphEngineLayer Example](https://github.com/langgenius/dify/blob/feat/queue-based-graph-engine/api/core/workflow/graph_engine/layers/debug_logging.py)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: '**How can I debug workflow execution?**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: Enable `DEBUG=true` to view detailed logs.
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: '**Debugging Tools**: A visual interface to view execution states and variables
      in real time.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: '**More Complete Command Support**: Add Pause/Resume, breakpoint debugging.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: 'chore(workflows): remove redundant eslint command from style workflow
      by @17hz in https://github.com/langgenius/dify/pull/25900'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: 'chore: update post_create_command.sh to use dynamic workspace root for
      aliases by @ZeroZ-lab in https://github.com/langgenius/dify/pull/25913'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  - quote: Run import-linter within make lint by @laipz8200 in https://github.com/langgenius/dify/pull/25933
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 12-developer-workflow-changes-in-1-9-0
  source_release: dify-2025-09-22-1-9-0-github-249001568-ef530801
  source_type: github_releases
  theme: developer-workflow
  title: 12 Developer Workflow changes in 1.9.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-09-17-feat-commands-add-new-commands-for-docs-git-and-pr-review-by-allenhutchison-in-h|feat(commands):
  Add new commands for docs, git, and PR review]]'
- '[[Changes/Open WebUI/2025-09-17-12-developer-workflow-changes-in-v0-6-29|12 Developer
  Workflow changes in v0.6.29]]'
- '[[Changes/Codex CLI/2025-09-18-new-review-command-introduced-in-3774|new /review
  command introduced in ♯3774]]'
source_release: '[[Releases/Dify/dify-2025-09-22-1-9-0-github-249001568-ef530801|dify-2025-09-22-1-9-0-github-249001568-ef530801]]'
source_type: github_releases
theme: developer-workflow
title: 12 Developer Workflow changes in 1.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Developer Workflow changes in 1.9.0

**Dify** · 2025-09-22 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.9.0) · from [[Releases/Dify/dify-2025-09-22-1-9-0-github-249001568-ef530801|1.9.0 – Orchestrating Knowledge, Powering Workflows]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The Knowledge Pipeline provides a modularized and extensible workflow for knowledge ingestion and processing, while the Queue-based Graph Engine makes workflow execution more robust and controllable. We believe these will help you build and debug AI applications more smoothly, and we look forward to your experiences to help us continuously improve.

> This provides safe iteration and debugging at every stage.

> ❌ Insufficient debugging information

> Debug mode: set `DEBUG=true` to enable DebugLoggingLayer.

> [GraphEngineLayer Example](https://github.com/langgenius/dify/blob/feat/queue-based-graph-engine/api/core/workflow/graph_engine/layers/debug_logging.py)

> **How can I debug workflow execution?**

> Enable `DEBUG=true` to view detailed logs.

> **Debugging Tools**: A visual interface to view execution states and variables in real time.

> **More Complete Command Support**: Add Pause/Resume, breakpoint debugging.

> chore(workflows): remove redundant eslint command from style workflow by @17hz in https://github.com/langgenius/dify/pull/25900

> chore: update post_create_command.sh to use dynamic workspace root for aliases by @ZeroZ-lab in https://github.com/langgenius/dify/pull/25913

> Run import-linter within make lint by @laipz8200 in https://github.com/langgenius/dify/pull/25933

Source: https://github.com/langgenius/dify/releases/tag/1.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-09-22-5-model-support-changes-in-1-9-0|5 Model Support changes in 1.9.0]] · Model Support
- [[Changes/Dify/2025-09-22-customize-and-share-pipelines-by-importing-exporting-via-dsl-for-easier-reusabil|🔄 Customize and share pipelines by importing/exporting via DSL for easier…]] · Collaboration
- [[Changes/Dify/2025-09-22-5-safety-and-privacy-changes-in-1-9-0|5 Safety and Privacy changes in 1.9.0]] · Safety and Privacy
- [[Changes/Dify/2025-09-22-chore-remove-weird-account-login-by-zalcit-in-https-github-com-langgenius-dify-p|chore: remove weird account login]] · Account and Access
- [[Changes/Dify/2025-09-22-feat-add-circular-scrolling-to-gotoanything-command-menu-by-lyzno1-in-https-gith|feat: add circular scrolling to GotoAnything command menu]] · Interface Experience
- [[Changes/Dify/2025-09-22-multimodal-embedding-support-richer-content-types-beyond-text|Multimodal Embedding: Support richer content types beyond text]] · Multimodal Input
- [[Changes/Dify/2025-09-22-12-apps-and-integrations-changes-in-1-9-0|12 Apps and Integrations changes in 1.9.0]] · Apps and Integrations
- [[Changes/Dify/2025-09-22-6-files-and-data-changes-in-1-9-0|6 Files and Data changes in 1.9.0]] · Files and Data
- [[Changes/Dify/2025-09-22-5-automation-and-scheduling-changes-in-1-9-0|5 Automation and Scheduling changes in 1.9.0]] · Automation and Scheduling
- [[Changes/Dify/2025-09-22-5-reliability-and-performance-changes-in-1-9-0|5 Reliability and Performance changes in 1.9.0]] · Reliability and Performance
- [[Changes/Dify/2025-09-22-example-of-no-unstable-context-value-by-asukaminato0721-in-https-github-com-lang|example of no-unstable-context-value]] · Context Window
- [[Changes/Dify/2025-09-22-185-other-changes-in-1-9-0|185 other changes in 1.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2025-09-18 · Codex CLI · [[Changes/Codex CLI/2025-09-18-new-review-command-introduced-in-3774|new /review command introduced in ♯3774]]
- Later: 2025-09-23 · Codex CLI · [[Changes/Codex CLI/2025-09-23-2-developer-workflow-changes-in-rust-v0-40-0|2 Developer Workflow changes in rust-v0.40.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-09-22-74092f&body=Card%3A%20Changes%2FDify%2F2025-09-22-12-developer-workflow-changes-in-1-9-0.md%0ACard%20ID%3A%20dify-2025-09-22-74092f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->