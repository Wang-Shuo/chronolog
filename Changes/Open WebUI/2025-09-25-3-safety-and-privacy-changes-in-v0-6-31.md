---
card_id: open-webui-2025-09-25-3f2a93
date: '2025-09-25'
description: "Open WebUI · 2025-09-25 · Safety and Privacy: 3 changes in v0.6.31 —
  \U0001F6E0️ External & Built-In Tools can now support rich UI element embedding…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 893
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 19ca8fa5041ffa0e26b45c6ae21b03c695dc79004e87e3d7d74d54f87f62d1a2
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-09-25-3f2a93
  comparison: ''
  date: '2025-09-25'
  description: 'Open WebUI — v0.6.31: 3 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F6E0️ External & Built-In Tools can now support rich UI element
      embedding ([Docs](https://docs.openwebui.com/features/plugin/tools/development)),
      allowing tools to return HTML content and interactive iframes that display directly
      within chat conversations with configurable security settings. [Commit](https://github.com/open-webui/open-webui/commit/07c5b25bc8b63173f406feb3ba183d375fedee6a),
      [Commit](https://github.com/open-webui/open-webui/commit/a5d8882bba7933a2c2c31c0a1405aba507c370bb),
      [Commit](https://github.com/open-webui/open-webui/commit/7be5b7f50f498de97359003609fc5993a172f084),
      [Commit](https://github.com/open-webui/open-webui/commit/a89ffccd7e96705a4a40e845289f4fcf9c4ae596)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  - quote: "\U0001F6E1️ SVG content security was enhanced by implementing DOMPurify
      sanitization to prevent XSS attacks through malicious SVG elements, ensuring
      safe rendering of user-generated SVG content. [Commit](https://github.com/open-webui/open-webui/pull/17747/commits/750a659a9fee7687e667d9d755e17b8a0c77d557)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  - quote: "\U0001F4C1 Empty folder deletion is now allowed regardless of chat deletion
      permission restrictions, resolving cases where users couldn't remove folders
      after deleting all contained chats. [#17683](https://github.com/open-webui/open-webui/pull/17683)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-safety-and-privacy-changes-in-v0-6-31
  source_release: open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v0.6.31
  type: change
related_changes:
- '[[Changes/Dify/2025-09-22-5-safety-and-privacy-changes-in-1-9-0|5 Safety and Privacy
  changes in 1.9.0]]'
- '[[Changes/Codex CLI/2025-09-23-3880-add-non-sandbox-test-helper-3880|♯3880 Add
  non_sandbox_test helper (♯3880)]]'
- '[[Changes/Gemini CLI/2025-09-24-4-safety-and-privacy-changes-in-v0-6-0|4 Safety
  and Privacy changes in v0.6.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead|open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v0.6.31
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v0.6.31

**Open WebUI** · 2025-09-25 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.31) · from [[Releases/Open WebUI/open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead|v0.6.31]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🛠️ External & Built-In Tools can now support rich UI element embedding ([Docs](https://docs.openwebui.com/features/plugin/tools/development)), allowing tools to return HTML content and interactive iframes that display directly within chat conversations with configurable security settings. [Commit](https://github.com/open-webui/open-webui/commit/07c5b25bc8b63173f406feb3ba183d375fedee6a), [Commit](https://github.com/open-webui/open-webui/commit/a5d8882bba7933a2c2c31c0a1405aba507c370bb), [Commit](https://github.com/open-webui/open-webui/commit/7be5b7f50f498de97359003609fc5993a172f084), [Commit](https://github.com/open-webui/open-webui/commit/a89ffccd7e96705a4a40e845289f4fcf9c4ae596)

> 🛡️ SVG content security was enhanced by implementing DOMPurify sanitization to prevent XSS attacks through malicious SVG elements, ensuring safe rendering of user-generated SVG content. [Commit](https://github.com/open-webui/open-webui/pull/17747/commits/750a659a9fee7687e667d9d755e17b8a0c77d557)

> 📁 Empty folder deletion is now allowed regardless of chat deletion permission restrictions, resolving cases where users couldn't remove folders after deleting all contained chats. [#17683](https://github.com/open-webui/open-webui/pull/17683)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-09-25-editor-collaboration-functionality-was-refactored-to-reduce-package-size-by-390k|⚡ Editor collaboration functionality was refactored to reduce package size by 390KB…]] · Collaboration
- [[Changes/Open WebUI/2025-09-25-4-apps-and-integrations-changes-in-v0-6-31|4 Apps and Integrations changes in v0.6.31]] · Apps and Integrations
- [[Changes/Open WebUI/2025-09-25-2-editor-experience-changes-in-v0-6-31|2 Editor Experience changes in v0.6.31]] · Editor Experience
- [[Changes/Open WebUI/2025-09-25-rag-query-generation-is-now-skipped-when-all-attached-files-are-set-to-full-cont|🔍 RAG query generation is now skipped when all attached files are set to full…]] · Context Window
- [[Changes/Open WebUI/2025-09-25-4-model-support-changes-in-v0-6-31|4 Model Support changes in v0.6.31]] · Model Support
- [[Changes/Open WebUI/2025-09-25-enhanced-user-interface-accessibility-through-the-addition-of-unique-element-ids|♿ Enhanced user interface accessibility through the addition of unique element IDs…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-09-25-2-search-and-browsing-changes-in-v0-6-31|2 Search and Browsing changes in v0.6.31]] · Search and Browsing
- [[Changes/Open WebUI/2025-09-25-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-09-25-image-generation-model-selection-was-centralized-to-enable-dynamic-model-overrid|🎨 Image generation model selection was centralized to enable dynamic model override…]] · Image Generation
- [[Changes/Open WebUI/2025-09-25-4-interface-experience-changes-in-v0-6-31|4 Interface Experience changes in v0.6.31]] · Interface Experience
- [[Changes/Open WebUI/2025-09-25-file-upload-handling-was-improved-to-properly-recognize-uploaded-files-even-when|📎 File upload handling was improved to properly recognize uploaded files even…]] · Files and Data
- [[Changes/Open WebUI/2025-09-25-2-account-and-access-changes-in-v0-6-31|2 Account and Access changes in v0.6.31]] · Account and Access
- [[Changes/Open WebUI/2025-09-25-5-reliability-and-performance-changes-in-v0-6-31|5 Reliability and Performance changes in v0.6.31]] · Reliability and Performance
- [[Changes/Open WebUI/2025-09-25-2-developer-workflow-changes-in-v0-6-31|2 Developer Workflow changes in v0.6.31]] · Developer Workflow
- [[Changes/Open WebUI/2025-09-25-17-other-changes-in-v0-6-31|17 other changes in v0.6.31]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2025-09-24 · Gemini CLI · [[Changes/Gemini CLI/2025-09-24-4-safety-and-privacy-changes-in-v0-6-0|4 Safety and Privacy changes in v0.6.0]]
- Later: 2025-09-26 · Codex CLI · [[Changes/Codex CLI/2025-09-26-2-safety-and-privacy-changes-in-rust-v0-42-0|2 Safety and Privacy changes in rust-v0.42.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-09-25-3f2a93&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-09-25-3-safety-and-privacy-changes-in-v0-6-31.md%0ACard%20ID%3A%20open-webui-2025-09-25-3f2a93%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.31%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->