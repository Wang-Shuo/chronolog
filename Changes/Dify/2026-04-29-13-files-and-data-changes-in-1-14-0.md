---
card_id: dify-2026-04-29-0584ce
date: '2026-04-29'
description: 'Dify · 2026-04-29 · Files and Data: 13 changes in v1.14.0 — refactor:
  select in service API dataset document and segment controllers by @RenzoMXD in…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode
    offset]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2415
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2de4dad64a9ec9ab7f0cadc09fa259b08a68222cd6765f7ccc6b5b825a5fc0b2
product: dify
product_name: Dify
record:
  card_id: dify-2026-04-29-0584ce
  comparison: ''
  date: '2026-04-29'
  description: 'Dify — v1.14.0: 13 Files and Data changes'
  evidence:
  - quote: 'refactor: select in service API dataset document and segment controllers
      by @RenzoMXD in https://github.com/langgenius/dify/pull/34101'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): type document summary status detail with TypedDict by @YB0y
      in https://github.com/langgenius/dify/pull/34610'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: migrate session.query to select API in document task files by
      @RenzoMXD in https://github.com/langgenius/dify/pull/34646'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: migrate session.query to select API in summary and remove document
      tasks by @RenzoMXD in https://github.com/langgenius/dify/pull/34650'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: migrate session.query to select API in add document and clean
      document tasks by @RenzoMXD in https://github.com/langgenius/dify/pull/34761'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: migrate session.query to select API in document indexing sync
      task by @RenzoMXD in https://github.com/langgenius/dify/pull/34813'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): type Document.to_dict with DocumentDict TypedDict by @bittoby
      in https://github.com/langgenius/dify/pull/34924'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(tasks): migrate document_indexing_task and remove_app_and_related_data_task
      to SQLAlchemy 2.0 select() API by @wdeveloper16 in https://github.com/langgenius/dify/pull/34968'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate document indexing task tests to SQLAlchemy 2.0 select API
      by @bohdansolovie in https://github.com/langgenius/dify/pull/35145'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: remove document service status mock tests superseded by testcontainers
      by @jamesrayammons in https://github.com/langgenius/dify/pull/35197'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): migrate dataset document response schemas to BaseModel
      by @ai-hpc in https://github.com/langgenius/dify/pull/35298'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate dataset service document mock tests to testcontainers by
      @jamesrayammons in https://github.com/langgenius/dify/pull/35191'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: remove file upload migration tip by @hjlarry in https://github.com/langgenius/dify/pull/35409'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 13-files-and-data-changes-in-1-14-0
  source_release: dify-2026-04-29-1-14-0-github-314986233-63073e86
  source_type: github_releases
  theme: file-data
  title: 13 Files and Data changes in 1.14.0
  type: change
related_changes:
- '[[Changes/AnythingLLM/2026-04-22-4-files-and-data-changes-in-v1-12-1|4 Files and
  Data changes in v1.12.1]]'
- '[[Changes/Codex CLI/2026-04-23-18423-chore-document-intentional-await-holding-cases-bolinfest|♯18423
  chore: document intentional await-holding cases @bolinfest]]'
- "[[Changes/Open WebUI/2026-04-24-paddleocr-vl-document-extraction-administrators-can-now-use-paddleocr-vl-as-a-co|\U0001F9E0
  PaddleOCR-vl document extraction. Administrators can now use PaddleOCR-vl…]]"
source_release: '[[Releases/Dify/dify-2026-04-29-1-14-0-github-314986233-63073e86|dify-2026-04-29-1-14-0-github-314986233-63073e86]]'
source_type: github_releases
theme: file-data
title: 13 Files and Data changes in 1.14.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Files and Data changes in 1.14.0

**Dify** · 2026-04-29 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.14.0) · from [[Releases/Dify/dify-2026-04-29-1-14-0-github-314986233-63073e86|v1.14.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> refactor: select in service API dataset document and segment controllers by @RenzoMXD in https://github.com/langgenius/dify/pull/34101

> refactor(api): type document summary status detail with TypedDict by @YB0y in https://github.com/langgenius/dify/pull/34610

> refactor: migrate session.query to select API in document task files by @RenzoMXD in https://github.com/langgenius/dify/pull/34646

> refactor: migrate session.query to select API in summary and remove document tasks by @RenzoMXD in https://github.com/langgenius/dify/pull/34650

> refactor: migrate session.query to select API in add document and clean document tasks by @RenzoMXD in https://github.com/langgenius/dify/pull/34761

> refactor: migrate session.query to select API in document indexing sync task by @RenzoMXD in https://github.com/langgenius/dify/pull/34813

> refactor(api): type Document.to_dict with DocumentDict TypedDict by @bittoby in https://github.com/langgenius/dify/pull/34924

> refactor(tasks): migrate document_indexing_task and remove_app_and_related_data_task to SQLAlchemy 2.0 select() API by @wdeveloper16 in https://github.com/langgenius/dify/pull/34968

> test: migrate document indexing task tests to SQLAlchemy 2.0 select API by @bohdansolovie in https://github.com/langgenius/dify/pull/35145

> test: remove document service status mock tests superseded by testcontainers by @jamesrayammons in https://github.com/langgenius/dify/pull/35197

> refactor(api): migrate dataset document response schemas to BaseModel by @ai-hpc in https://github.com/langgenius/dify/pull/35298

> test: migrate dataset service document mock tests to testcontainers by @jamesrayammons in https://github.com/langgenius/dify/pull/35191

> refactor: remove file upload migration tip by @hjlarry in https://github.com/langgenius/dify/pull/35409

Source: https://github.com/langgenius/dify/releases/tag/1.14.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-04-29-2-developer-workflow-changes-in-1-14-0|2 Developer Workflow changes in 1.14.0]] · Developer Workflow
- [[Changes/Dify/2026-04-29-10-interface-experience-changes-in-1-14-0|10 Interface Experience changes in 1.14.0]] · Interface Experience
- [[Changes/Dify/2026-04-29-27-model-support-changes-in-1-14-0|27 Model Support changes in 1.14.0]] · Model Support
- [[Changes/Dify/2026-04-29-2-accessibility-and-localization-changes-in-1-14-0|2 Accessibility and Localization changes in 1.14.0]] · Accessibility and Localization
- [[Changes/Dify/2026-04-29-6-editor-experience-changes-in-1-14-0|6 Editor Experience changes in 1.14.0]] · Editor Experience
- [[Changes/Dify/2026-04-29-7-pricing-model-changes-in-1-14-0|7 Pricing Model changes in 1.14.0]] · Pricing Model
- [[Changes/Dify/2026-04-29-48-apps-and-integrations-changes-in-1-14-0|48 Apps and Integrations changes in 1.14.0]] · Apps and Integrations
- [[Changes/Dify/2026-04-29-13-collaboration-changes-in-1-14-0|13 Collaboration changes in 1.14.0]] · Collaboration
- [[Changes/Dify/2026-04-29-7-safety-and-privacy-changes-in-1-14-0|7 Safety and Privacy changes in 1.14.0]] · Safety and Privacy
- [[Changes/Dify/2026-04-29-8-account-and-access-changes-in-1-14-0|8 Account and Access changes in 1.14.0]] · Account and Access
- [[Changes/Dify/2026-04-29-2-agent-mode-changes-in-1-14-0|2 Agent Mode changes in 1.14.0]] · Agent Mode
- [[Changes/Dify/2026-04-29-3-automation-and-scheduling-changes-in-1-14-0|3 Automation and Scheduling changes in 1.14.0]] · Automation and Scheduling
- [[Changes/Dify/2026-04-29-2-enterprise-and-administration-changes-in-1-14-0|2 Enterprise and Administration changes in 1.14.0]] · Enterprise and Administration
- [[Changes/Dify/2026-04-29-3-context-window-changes-in-1-14-0|3 Context Window changes in 1.14.0]] · Context Window
- [[Changes/Dify/2026-04-29-3-reliability-and-performance-changes-in-1-14-0|3 Reliability and Performance changes in 1.14.0]] · Reliability and Performance
- [[Changes/Dify/2026-04-29-520-other-changes-in-1-14-0|520 other changes in 1.14.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-04-24 · Open WebUI · [[Changes/Open WebUI/2026-04-24-paddleocr-vl-document-extraction-administrators-can-now-use-paddleocr-vl-as-a-co|🧠 PaddleOCR-vl document extraction. Administrators can now use PaddleOCR-vl…]]
- Later: 2026-05-05 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-05-add-attachment-flag-in-non-interactive-p-prompt-mode-to-attach-files-images-or-n|Add --attachment flag in non-interactive (-p/--prompt) mode to attach files…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode offset]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-04-29-0584ce&body=Card%3A%20Changes%2FDify%2F2026-04-29-13-files-and-data-changes-in-1-14-0.md%0ACard%20ID%3A%20dify-2026-04-29-0584ce%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.14.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->