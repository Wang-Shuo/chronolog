---
card_id: open-webui-2025-09-25-edc7b3
date: '2025-09-25'
description: "Open WebUI · 2025-09-25 · Account and Access: 2 changes in v0.6.31 —
  \U0001F510 Redis session storage support was added for OAuth redirects, providing
  better state…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 910
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 46be1e3fe5cd9edfb394e21175c977fac307c77044bd9cdeec9bca303b0f566d
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-09-25-edc7b3
  comparison: ''
  date: '2025-09-25'
  description: 'Open WebUI — v0.6.31: 2 Account and Access changes'
  evidence:
  - quote: "\U0001F510 Redis session storage support was added for OAuth redirects,
      providing better state handling in multi-pod Kubernetes deployments and resolving
      CSRF mismatch errors. [#17223](https://github.com/open-webui/open-webui/pull/17223),
      [#15373](https://github.com/open-webui/open-webui/issues/15373)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  - quote: "\U0001F510 OAuth access token refresh errors are resolved by properly
      implementing async/await patterns, preventing \"coroutine object has no attribute
      get\" failures during token expiry. [#17585](https://github.com/open-webui/open-webui/issues/17585),
      [#17678](https://github.com/open-webui/open-webui/issues/17678)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-account-and-access-changes-in-v0-6-31
  source_release: open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead
  source_type: github_releases
  theme: account-access
  title: 2 Account and Access changes in v0.6.31
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-09-17-refactor-authentication-components-and-hooks-by-scidomino-in-https-github-com-go|Refactor
  Authentication Components and Hooks]]'
- "[[Changes/Open WebUI/2025-09-17-oauth-token-retrieval-logic-was-refactored-improving-the-reliability-and-consist|\U0001F512
  OAuth token retrieval logic was refactored, improving the reliability…]]"
- '[[Changes/Dify/2025-09-22-chore-remove-weird-account-login-by-zalcit-in-https-github-com-langgenius-dify-p|chore:
  remove weird account login]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead|open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead]]'
source_type: github_releases
theme: account-access
title: 2 Account and Access changes in v0.6.31
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Account and Access changes in v0.6.31

**Open WebUI** · 2025-09-25 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.31) · from [[Releases/Open WebUI/open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead|v0.6.31]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 Redis session storage support was added for OAuth redirects, providing better state handling in multi-pod Kubernetes deployments and resolving CSRF mismatch errors. [#17223](https://github.com/open-webui/open-webui/pull/17223), [#15373](https://github.com/open-webui/open-webui/issues/15373)

> 🔐 OAuth access token refresh errors are resolved by properly implementing async/await patterns, preventing "coroutine object has no attribute get" failures during token expiry. [#17585](https://github.com/open-webui/open-webui/issues/17585), [#17678](https://github.com/open-webui/open-webui/issues/17678)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-09-25-editor-collaboration-functionality-was-refactored-to-reduce-package-size-by-390k|⚡ Editor collaboration functionality was refactored to reduce package size by 390KB…]] · Collaboration
- [[Changes/Open WebUI/2025-09-25-4-apps-and-integrations-changes-in-v0-6-31|4 Apps and Integrations changes in v0.6.31]] · Apps and Integrations
- [[Changes/Open WebUI/2025-09-25-2-editor-experience-changes-in-v0-6-31|2 Editor Experience changes in v0.6.31]] · Editor Experience
- [[Changes/Open WebUI/2025-09-25-rag-query-generation-is-now-skipped-when-all-attached-files-are-set-to-full-cont|🔍 RAG query generation is now skipped when all attached files are set to full…]] · Context Window
- [[Changes/Open WebUI/2025-09-25-3-safety-and-privacy-changes-in-v0-6-31|3 Safety and Privacy changes in v0.6.31]] · Safety and Privacy
- [[Changes/Open WebUI/2025-09-25-4-model-support-changes-in-v0-6-31|4 Model Support changes in v0.6.31]] · Model Support
- [[Changes/Open WebUI/2025-09-25-enhanced-user-interface-accessibility-through-the-addition-of-unique-element-ids|♿ Enhanced user interface accessibility through the addition of unique element IDs…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-09-25-2-search-and-browsing-changes-in-v0-6-31|2 Search and Browsing changes in v0.6.31]] · Search and Browsing
- [[Changes/Open WebUI/2025-09-25-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-09-25-image-generation-model-selection-was-centralized-to-enable-dynamic-model-overrid|🎨 Image generation model selection was centralized to enable dynamic model override…]] · Image Generation
- [[Changes/Open WebUI/2025-09-25-4-interface-experience-changes-in-v0-6-31|4 Interface Experience changes in v0.6.31]] · Interface Experience
- [[Changes/Open WebUI/2025-09-25-file-upload-handling-was-improved-to-properly-recognize-uploaded-files-even-when|📎 File upload handling was improved to properly recognize uploaded files even…]] · Files and Data
- [[Changes/Open WebUI/2025-09-25-5-reliability-and-performance-changes-in-v0-6-31|5 Reliability and Performance changes in v0.6.31]] · Reliability and Performance
- [[Changes/Open WebUI/2025-09-25-2-developer-workflow-changes-in-v0-6-31|2 Developer Workflow changes in v0.6.31]] · Developer Workflow
- [[Changes/Open WebUI/2025-09-25-17-other-changes-in-v0-6-31|17 other changes in v0.6.31]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2025-09-22 · Dify · [[Changes/Dify/2025-09-22-chore-remove-weird-account-login-by-zalcit-in-https-github-com-langgenius-dify-p|chore: remove weird account login]]
- Later: 2025-09-26 · Ollama · [[Changes/Ollama/2025-09-26-ollama-push-will-now-provide-a-url-to-follow-to-sign-in|ollama push will now provide a URL to follow to sign in]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-09-25-edc7b3&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-09-25-2-account-and-access-changes-in-v0-6-31.md%0ACard%20ID%3A%20open-webui-2025-09-25-edc7b3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.31%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->