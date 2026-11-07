---
card_id: dify-2026-10-23-f1ec48
date: '2026-10-23'
description: 'Dify · 2026-10-23 · Files and Data: 8 changes in v1.18.0 — Smarter Agent
  Routing, Portable Apps, Deeper Workflow Visibility — **Document extraction:**…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1247
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b5133f363ec8bb0f80d03f3741f87488c703185d547ede4353f4bedcfb587d95
product: dify
product_name: Dify
record:
  card_id: dify-2026-10-23-f1ec48
  comparison: ''
  date: '2026-10-23'
  description: 'Dify — v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow
    Visibility: 8 Files and Data changes'
  evidence:
  - quote: '**Document extraction:** re-import/re-index affected content to apply
      extraction fixes to existing documents.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Built-in document metadata:** toggling built-in fields rewrites only
      enabled, non-archived documents whose indexing is complete. Other legacy rows
      can retain the old format and need a later rewrite when eligible; this release
      does not include a full backfill. (#44218)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '**Developer tooling:** faster TypeScript checks through tsrs, plus typed
      Document and CustomizedSnippet models that preserve existing constructors and
      database defaults. (#44562, #36084, #40818)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Preserve configured fallback values when Code node outputs are removed,
      added, or renamed; require confirmation before saving an empty canvas; and retain
      in-run tool-file access for later nodes. (#42678, #43668, #41300)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Preserve CSV cell content, Notion mentions/equations, and newlines in
      recursive splitting. URL imports infer useful file extensions from content type,
      and unsupported pipeline file types return an explicit error. Re-import affected
      documents to regenerate content already indexed incorrectly. (#42159, #42171,
      #44179, #42364, #44012)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Message citations retain document metadata. Built-in document dates use
      consistent UTC epoch values while preserving fractional seconds; existing mixed-format
      metadata is not automatically rewritten. (#41861, #44218)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '| `a8c2e6f4b901` | Track KnowledgeFS upgrade document availability independently
      of metadata. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '| `b9d3f7a5c102` | Persist delivery and execution leases for upgrade document
      reconciliation. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 8-files-and-data-changes-in-1-18-0
  source_release: dify-2026-10-23-1-18-0-github-421489030-879b0613
  source_type: github_releases
  theme: file-data
  title: 8 Files and Data changes in 1.18.0
  type: change
related_changes:
- '[[Changes/Lovable/2026-10-15-select-and-sort-files-faster-in-the-files-tab|Select
  and sort files faster in the Files tab]]'
- '[[Changes/Open WebUI/2026-10-16-4-files-and-data-changes-in-v0-12-3|4 Files and
  Data changes in v0.12.3]]'
- '[[Changes/v0/2026-10-16-polished-the-design-mode-canvas-toolbar-and-panel-with-crisper-selection-real-fo|Polished
  the Design Mode canvas, toolbar, and panel, with crisper selection, real…]]'
source_release: '[[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|dify-2026-10-23-1-18-0-github-421489030-879b0613]]'
source_type: github_releases
theme: file-data
title: 8 Files and Data changes in 1.18.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Files and Data changes in 1.18.0

**Dify** · 2026-10-23 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.18.0) · from [[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow Visibility]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Document extraction:** re-import/re-index affected content to apply extraction fixes to existing documents.

> **Built-in document metadata:** toggling built-in fields rewrites only enabled, non-archived documents whose indexing is complete. Other legacy rows can retain the old format and need a later rewrite when eligible; this release does not include a full backfill. (#44218)

> **Developer tooling:** faster TypeScript checks through tsrs, plus typed Document and CustomizedSnippet models that preserve existing constructors and database defaults. (#44562, #36084, #40818)

> Preserve configured fallback values when Code node outputs are removed, added, or renamed; require confirmation before saving an empty canvas; and retain in-run tool-file access for later nodes. (#42678, #43668, #41300)

> Preserve CSV cell content, Notion mentions/equations, and newlines in recursive splitting. URL imports infer useful file extensions from content type, and unsupported pipeline file types return an explicit error. Re-import affected documents to regenerate content already indexed incorrectly. (#42159, #42171, #44179, #42364, #44012)

> Message citations retain document metadata. Built-in document dates use consistent UTC epoch values while preserving fractional seconds; existing mixed-format metadata is not automatically rewritten. (#41861, #44218)

> | `a8c2e6f4b901` | Track KnowledgeFS upgrade document availability independently of metadata. |

> | `b9d3f7a5c102` | Persist delivery and execution leases for upgrade document reconciliation. |

Source: https://github.com/langgenius/dify/releases/tag/1.18.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-10-23-respect-xforward-headers-enabled-standalone-api-default-remains-false-bundled-co| /  RESPECT_XFORWARD_HEADERS_ENABLED  /  Standalone API default remains false]] · Developer Workflow
- [[Changes/Dify/2026-10-23-3-memory-and-personalization-changes-in-1-18-0|3 Memory and Personalization changes in 1.18.0]] · Memory and Personalization
- [[Changes/Dify/2026-10-23-3-accessibility-and-localization-changes-in-1-18-0|3 Accessibility and Localization changes in 1.18.0]] · Accessibility and Localization
- [[Changes/Dify/2026-10-23-3-context-window-changes-in-1-18-0|3 Context Window changes in 1.18.0]] · Context Window
- [[Changes/Dify/2026-10-23-operations-archive-storage-supports-configurable-s3-addressing-style-the-api-ima|Operations: archive storage supports configurable S3 addressing style]] · Model Support
- [[Changes/Dify/2026-10-23-2-interface-experience-changes-in-1-18-0|2 Interface Experience changes in 1.18.0]] · Interface Experience
- [[Changes/Dify/2026-10-23-3-editor-experience-changes-in-1-18-0|3 Editor Experience changes in 1.18.0]] · Editor Experience
- [[Changes/Dify/2026-10-23-32-agent-mode-changes-in-1-18-0|32 Agent Mode changes in 1.18.0]] · Agent Mode
- [[Changes/Dify/2026-10-23-11-safety-and-privacy-changes-in-1-18-0|11 Safety and Privacy changes in 1.18.0]] · Safety and Privacy
- [[Changes/Dify/2026-10-23-14-apps-and-integrations-changes-in-1-18-0|14 Apps and Integrations changes in 1.18.0]] · Apps and Integrations
- [[Changes/Dify/2026-10-23-6-account-and-access-changes-in-1-18-0|6 Account and Access changes in 1.18.0]] · Account and Access
- [[Changes/Dify/2026-10-23-2-reliability-and-performance-changes-in-1-18-0|2 Reliability and Performance changes in 1.18.0]] · Reliability and Performance
- [[Changes/Dify/2026-10-23-5-collaboration-changes-in-1-18-0|5 Collaboration changes in 1.18.0]] · Collaboration
- [[Changes/Dify/2026-10-23-2-automation-and-scheduling-changes-in-1-18-0|2 Automation and Scheduling changes in 1.18.0]] · Automation and Scheduling
- [[Changes/Dify/2026-10-23-81-other-changes-in-1-18-0|81 other changes in 1.18.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-10-16 · v0 · [[Changes/v0/2026-10-16-polished-the-design-mode-canvas-toolbar-and-panel-with-crisper-selection-real-fo|Polished the Design Mode canvas, toolbar, and panel, with crisper selection, real…]]
- Later: 2026-10-23 · OpenHands · [[Changes/OpenHands/2026-10-23-feat-canvas-quiet-backend-logs-by-default-by-neubig-in-https-github-com-openhand|feat(canvas): quiet backend logs by default]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-10-23-f1ec48&body=Card%3A%20Changes%2FDify%2F2026-10-23-8-files-and-data-changes-in-1-18-0.md%0ACard%20ID%3A%20dify-2026-10-23-f1ec48%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.18.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->