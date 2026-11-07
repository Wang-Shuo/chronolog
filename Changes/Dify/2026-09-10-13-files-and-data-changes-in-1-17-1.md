---
card_id: dify-2026-09-10-be773f
date: '2026-09-10'
description: 'Dify · 2026-09-10 · Files and Data: 13 changes in v1.17.1 - Bug Fixes
  and Improvements — This release fixes a cluster of extraction bugs that changed
  document…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1204
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 261f30356fc05bd9578f348f18aae9176eb6bfe6f8538198d4b0d29f0b3016b3
product: dify
product_name: Dify
record:
  card_id: dify-2026-09-10-be773f
  comparison: ''
  date: '2026-09-10'
  description: 'Dify — v1.17.1 - Bug Fixes and Improvements: 13 Files and Data changes'
  evidence:
  - quote: This release fixes a cluster of extraction bugs that changed document content
      without reporting an error. Re-import affected documents after upgrading; indexed
      text is not retroactively repaired.
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Documents with invalid Markdown image links could stall the indexing
      queue.** Relative, protocol-relative, `data:`, `ftp:`, and malformed image targets
      were all handed to the remote image fetcher and entered its SSRF retry loop,
      so a single document with many bad references could hold an indexing worker
      long enough to back up everything behind it. Non-fetchable targets are now validated
      and skipped. (#41343)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**The built-in file upload data source asked for authorization it does
      not need.** When creating a RAG Pipeline knowledge base, local file upload showed
      "Please authorize first" and the creation checklist flagged it, because providers
      that declare no credentials schema never have a stored-credential row and were
      therefore always reported as unauthorized. Credential-free providers are now
      marked authorized directly. (#39772)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Document create and update could report "One or more files not found."
      on MySQL** even though the upload had committed. Under MySQL''s default `REPEATABLE
      READ`, the request session''s read snapshot was pinned before the upload happened
      in a separate session, so the just-written rows were invisible. All four affected
      endpoints — create-by-text, create-by-file, update-by-text, update-by-file —
      now refresh the snapshot before the lookup. PostgreSQL was never affected. (#41840)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Pagination silently truncated results.** `has_more` was computed against
      the client-requested `limit` while the query capped page size at 100, so requesting
      `limit=200` against 150 rows returned 100 rows and `has_more=false` — the remaining
      50 were unreachable. Segment, dataset, and document list endpoints now compute
      `has_more` from the effective page size and report that size in the response.
      (#41776, #41784)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: Re-import any CSV, Excel, Notion, or web-scraped documents ingested on
      an earlier version — the extraction fixes in this release do not repair already-indexed
      text.
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(web): migrate document metadata input by @lyzno1 in https://github.com/langgenius/dify/pull/41276'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(service-api): inject file upload service by @hjlarry in https://github.com/langgenius/dify/pull/41585'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(web): inject file upload service by @hjlarry in https://github.com/langgenius/dify/pull/41586'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(openapi): inject file upload service by @hjlarry in https://github.com/langgenius/dify/pull/41606'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'docs(dify-ui): document combobox chip keyboard hints by @lyzno1 in https://github.com/langgenius/dify/pull/41815'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(api): extract human input file upload persistence by @hjlarry
      in https://github.com/langgenius/dify/pull/41716'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'chore: fit the app canvas when create from DSL and preview by @iamjoel
      in https://github.com/langgenius/dify/pull/42073'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 13-files-and-data-changes-in-1-17-1
  source_release: dify-2026-09-10-1-17-1-github-386157159-e472b6fe
  source_type: github_releases
  theme: file-data
  title: 13 Files and Data changes in 1.17.1
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-08-2-files-and-data-changes-in-v2026-9-3|2 Files and
  Data changes in v2026.9.3]]'
- '[[Changes/Google Antigravity/2026-09-09-introducing-new-documents-section-and-several-ux-enhancements-for-organization-a|Introducing
  new Documents section and several UX enhancements for organization and control]]'
- '[[Changes/OpenHands/2026-09-09-4-files-and-data-changes-in-v1-17-0|4 Files and
  Data changes in v1.17.0]]'
source_release: '[[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|dify-2026-09-10-1-17-1-github-386157159-e472b6fe]]'
source_type: github_releases
theme: file-data
title: 13 Files and Data changes in 1.17.1
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Files and Data changes in 1.17.1

**Dify** · 2026-09-10 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.1) · from [[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|v1.17.1 - Bug Fixes and Improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> This release fixes a cluster of extraction bugs that changed document content without reporting an error. Re-import affected documents after upgrading; indexed text is not retroactively repaired.

> **Documents with invalid Markdown image links could stall the indexing queue.** Relative, protocol-relative, `data:`, `ftp:`, and malformed image targets were all handed to the remote image fetcher and entered its SSRF retry loop, so a single document with many bad references could hold an indexing worker long enough to back up everything behind it. Non-fetchable targets are now validated and skipped. (#41343)

> **The built-in file upload data source asked for authorization it does not need.** When creating a RAG Pipeline knowledge base, local file upload showed "Please authorize first" and the creation checklist flagged it, because providers that declare no credentials schema never have a stored-credential row and were therefore always reported as unauthorized. Credential-free providers are now marked authorized directly. (#39772)

> **Document create and update could report "One or more files not found." on MySQL** even though the upload had committed. Under MySQL's default `REPEATABLE READ`, the request session's read snapshot was pinned before the upload happened in a separate session, so the just-written rows were invisible. All four affected endpoints — create-by-text, create-by-file, update-by-text, update-by-file — now refresh the snapshot before the lookup. PostgreSQL was never affected. (#41840)

> **Pagination silently truncated results.** `has_more` was computed against the client-requested `limit` while the query capped page size at 100, so requesting `limit=200` against 150 rows returned 100 rows and `has_more=false` — the remaining 50 were unreachable. Segment, dataset, and document list endpoints now compute `has_more` from the effective page size and report that size in the response. (#41776, #41784)

> Re-import any CSV, Excel, Notion, or web-scraped documents ingested on an earlier version — the extraction fixes in this release do not repair already-indexed text.

> refactor(web): migrate document metadata input by @lyzno1 in https://github.com/langgenius/dify/pull/41276

> refactor(service-api): inject file upload service by @hjlarry in https://github.com/langgenius/dify/pull/41585

> refactor(web): inject file upload service by @hjlarry in https://github.com/langgenius/dify/pull/41586

> refactor(openapi): inject file upload service by @hjlarry in https://github.com/langgenius/dify/pull/41606

> docs(dify-ui): document combobox chip keyboard hints by @lyzno1 in https://github.com/langgenius/dify/pull/41815

> refactor(api): extract human input file upload persistence by @hjlarry in https://github.com/langgenius/dify/pull/41716

> chore: fit the app canvas when create from DSL and preview by @iamjoel in https://github.com/langgenius/dify/pull/42073

Source: https://github.com/langgenius/dify/releases/tag/1.17.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-09-10-4-pricing-model-changes-in-1-17-1|4 Pricing Model changes in 1.17.1]] · Pricing Model
- [[Changes/Dify/2026-09-10-3-automation-and-scheduling-changes-in-1-17-1|3 Automation and Scheduling changes in 1.17.1]] · Automation and Scheduling
- [[Changes/Dify/2026-09-10-8-interface-experience-changes-in-1-17-1|8 Interface Experience changes in 1.17.1]] · Interface Experience
- [[Changes/Dify/2026-09-10-76-model-support-changes-in-1-17-1|76 Model Support changes in 1.17.1]] · Model Support
- [[Changes/Dify/2026-09-10-42-agent-mode-changes-in-1-17-1|42 Agent Mode changes in 1.17.1]] · Agent Mode
- [[Changes/Dify/2026-09-10-4-developer-workflow-changes-in-1-17-1|4 Developer Workflow changes in 1.17.1]] · Developer Workflow
- [[Changes/Dify/2026-09-10-3-collaboration-changes-in-1-17-1|3 Collaboration changes in 1.17.1]] · Collaboration
- [[Changes/Dify/2026-09-10-2-memory-and-personalization-changes-in-1-17-1|2 Memory and Personalization changes in 1.17.1]] · Memory and Personalization
- [[Changes/Dify/2026-09-10-16-safety-and-privacy-changes-in-1-17-1|16 Safety and Privacy changes in 1.17.1]] · Safety and Privacy
- [[Changes/Dify/2026-09-10-skill-packages-built-on-windows-failed-with-a-misleading-error-a-skill-md-using|Skill packages built on Windows failed with a misleading error. A SKILL.md…]] · Mobile and Desktop
- [[Changes/Dify/2026-09-10-12-apps-and-integrations-changes-in-1-17-1|12 Apps and Integrations changes in 1.17.1]] · Apps and Integrations
- [[Changes/Dify/2026-09-10-6-account-and-access-changes-in-1-17-1|6 Account and Access changes in 1.17.1]] · Account and Access
- [[Changes/Dify/2026-09-10-3-multimodal-input-changes-in-1-17-1|3 Multimodal Input changes in 1.17.1]] · Multimodal Input
- [[Changes/Dify/2026-09-10-6-editor-experience-changes-in-1-17-1|6 Editor Experience changes in 1.17.1]] · Editor Experience
- [[Changes/Dify/2026-09-10-3-accessibility-and-localization-changes-in-1-17-1|3 Accessibility and Localization changes in 1.17.1]] · Accessibility and Localization
- [[Changes/Dify/2026-09-10-a-plugin-could-exhaust-worker-memory-with-one-declared-number-the-blob-chunk-mer|A plugin could exhaust worker memory with one declared number. The blob chunk…]] · Reliability and Performance
- [[Changes/Dify/2026-09-10-6-context-window-changes-in-1-17-1|6 Context Window changes in 1.17.1]] · Context Window
- [[Changes/Dify/2026-09-10-205-other-changes-in-1-17-1|205 other changes in 1.17.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-09-09 · OpenHands · [[Changes/OpenHands/2026-09-09-4-files-and-data-changes-in-v1-17-0|4 Files and Data changes in v1.17.0]]
- Later: 2026-09-10 · Gemini · [[Changes/Gemini/2026-09-10-bring-google-gemini-to-your-pc-with-the-new-windows-app|Bring Google Gemini to your PC with the new Windows app]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-09-10-be773f&body=Card%3A%20Changes%2FDify%2F2026-09-10-13-files-and-data-changes-in-1-17-1.md%0ACard%20ID%3A%20dify-2026-09-10-be773f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->