---
card_id: dify-2026-02-03-b8e38b
date: '2026-02-03'
description: 'Dify · 2026-02-03 · Account and Access: 3 changes in v1.12.0 - Introducing
  Summary Index: Smarter Retrieval with AI Summarization — refactor: split changes
  for…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1041
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 84f0b61f7cdb5e41b1b8b92481351085f6abebdc40d641e4a0219e5a1e1fee22
product: dify
product_name: Dify
record:
  card_id: dify-2026-02-03-b8e38b
  comparison: ''
  date: '2026-02-03'
  description: 'Dify — v1.12.0 - Introducing Summary Index: Smarter Retrieval with
    AI Summarization: 3 Account and Access changes'
  evidence:
  - quote: 'refactor: split changes for api/controllers/web/login.py by @asukaminato0721
      in https://github.com/langgenius/dify/pull/29854'
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  - quote: 'refactor: port api/controllers/console/app/audio.py api/controllers/console/app/message.py
      api/controllers/console/auth/data_source_oauth.py api/controllers/console/auth/forgot_password.py
      api/controllers/console/workspace/endpoint.py by @asukaminato0721 in https://github.com/langgenius/dify/pull/30680'
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  - quote: 'refactor: update oauth_new_user handling in AppInitializer to use parseAsBoolean
      by @CodingOnStar in https://github.com/langgenius/dify/pull/31862'
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 3-account-and-access-changes-in-1-12-0
  source_release: dify-2026-02-03-1-12-0-github-282591953-290f70e4
  source_type: github_releases
  theme: account-access
  title: 3 Account and Access changes in 1.12.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-01-30-improve-compatibility-with-remote-mcp-servers-that-use-oauth|Improve
  compatibility with remote MCP servers that use OAuth]]'
- '[[Changes/Codex CLI/2026-01-31-9654-show-oauth-error-descriptions-in-callback-responses-blevy-oai|♯9654
  Show OAuth error descriptions in callback responses @blevy-oai]]'
- '[[Changes/Claude Code/2026-02-03-added-pre-configured-oauth-client-credentials-for-mcp-servers-that-don-t-support|Added
  pre-configured OAuth client credentials for MCP servers that don''t support…]]'
source_release: '[[Releases/Dify/dify-2026-02-03-1-12-0-github-282591953-290f70e4|dify-2026-02-03-1-12-0-github-282591953-290f70e4]]'
source_type: github_releases
theme: account-access
title: 3 Account and Access changes in 1.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Account and Access changes in 1.12.0

**Dify** · 2026-02-03 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.12.0) · from [[Releases/Dify/dify-2026-02-03-1-12-0-github-282591953-290f70e4|v1.12.0 - Introducing Summary Index: Smarter Retrieval with AI Summarization]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> refactor: split changes for api/controllers/web/login.py by @asukaminato0721 in https://github.com/langgenius/dify/pull/29854

> refactor: port api/controllers/console/app/audio.py api/controllers/console/app/message.py api/controllers/console/auth/data_source_oauth.py api/controllers/console/auth/forgot_password.py api/controllers/console/workspace/endpoint.py by @asukaminato0721 in https://github.com/langgenius/dify/pull/30680

> refactor: update oauth_new_user handling in AppInitializer to use parseAsBoolean by @CodingOnStar in https://github.com/langgenius/dify/pull/31862

Source: https://github.com/langgenius/dify/releases/tag/1.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-02-03-2-developer-workflow-changes-in-1-12-0|2 Developer Workflow changes in 1.12.0]] · Developer Workflow
- [[Changes/Dify/2026-02-03-chore-hide-disable-try-tab-when-not-support-by-iamjoel-in-https-github-com-langg|chore: hide disable try tab when not support]] · Editor Experience
- [[Changes/Dify/2026-02-03-chore-improve-accessibility-for-learn-more-link-by-khmandarrin-in-https-github-c|chore: improve accessibility for learn more link]] · Accessibility and Localization
- [[Changes/Dify/2026-02-03-9-safety-and-privacy-changes-in-1-12-0|9 Safety and Privacy changes in 1.12.0]] · Safety and Privacy
- [[Changes/Dify/2026-02-03-5-context-window-changes-in-1-12-0|5 Context Window changes in 1.12.0]] · Context Window
- [[Changes/Dify/2026-02-03-5-model-support-changes-in-1-12-0|5 Model Support changes in 1.12.0]] · Model Support
- [[Changes/Dify/2026-02-03-7-files-and-data-changes-in-1-12-0|7 Files and Data changes in 1.12.0]] · Files and Data
- [[Changes/Dify/2026-02-03-9-agent-mode-changes-in-1-12-0|9 Agent Mode changes in 1.12.0]] · Agent Mode
- [[Changes/Dify/2026-02-03-3-multimodal-input-changes-in-1-12-0|3 Multimodal Input changes in 1.12.0]] · Multimodal Input
- [[Changes/Dify/2026-02-03-test-enhance-hittestingpage-tests-with-additional-coverage-for-rendering-and-sta|test: enhance HitTestingPage tests with additional coverage for rendering and state…]] · Interface Experience
- [[Changes/Dify/2026-02-03-2-enterprise-and-administration-changes-in-1-12-0|2 Enterprise and Administration changes in 1.12.0]] · Enterprise and Administration
- [[Changes/Dify/2026-02-03-feat-use-xdist-to-make-make-test-faster-by-yihong0618-in-https-github-com-langge|feat: use xdist to make make test faster]] · Reliability and Performance
- [[Changes/Dify/2026-02-03-refactor-contract-restructure-console-contracts-with-nested-billing-module-by-ly|refactor(contract): restructure console contracts with nested billing module]] · Pricing Model
- [[Changes/Dify/2026-02-03-14-apps-and-integrations-changes-in-1-12-0|14 Apps and Integrations changes in 1.12.0]] · Apps and Integrations
- [[Changes/Dify/2026-02-03-149-other-changes-in-1-12-0|149 other changes in 1.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-02-03 · Claude Code · [[Changes/Claude Code/2026-02-03-added-pre-configured-oauth-client-credentials-for-mcp-servers-that-don-t-support|Added pre-configured OAuth client credentials for MCP servers that don't support…]]
- Later: 2026-02-03 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-03-2-account-and-access-changes-in-v0-0-401|2 Account and Access changes in v0.0.401]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-02-03-b8e38b&body=Card%3A%20Changes%2FDify%2F2026-02-03-3-account-and-access-changes-in-1-12-0.md%0ACard%20ID%3A%20dify-2026-02-03-b8e38b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->