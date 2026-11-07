---
card_id: open-webui-2025-08-28-8891f7
date: '2025-08-28'
description: "Open WebUI · 2025-08-28 · Account and Access: 2 changes in v0.6.26 —
  \U0001F510 **Azure Document Intelligence DefaultAzureCredential Support**: Added
  support for…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1857
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1b707d997cc381934abbf885fbe9aa24edb60ab60a422f904e40dd996fce7887
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-28-8891f7
  comparison: ''
  date: '2025-08-28'
  description: 'Open WebUI — v0.6.26: 2 Account and Access changes'
  evidence:
  - quote: "\U0001F510 **Azure Document Intelligence DefaultAzureCredential Support**:
      Added support for authenticating with Azure Document Intelligence using DefaultAzureCredential
      in addition to API key authentication, enabling seamless integration with Azure
      Entra ID and managed identity authentication for enterprise Azure environments."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  - quote: "\U0001F510 **Authentication Bootstrapping Enhancements**: Added \"ENABLE_INITIAL_ADMIN_SIGNUP\"
      environment variable and \"?form=true\" URL parameter to enable initial admin
      user creation and forced login form display in SSO-only deployments. This resolves
      bootstrap issues where administrators couldn't create the first user when login
      forms were disabled, allowing proper initialization of SSO-configured deployments
      without requiring temporary configuration changes."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-account-and-access-changes-in-v0-6-26
  source_release: open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3
  source_type: github_releases
  theme: account-access
  title: 2 Account and Access changes in v0.6.26
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-08-26-2528-fix-login-for-internal-employees|♯2528 Fix
  login for internal employees]]'
- '[[Changes/Dify/2025-08-27-7-account-and-access-changes-in-1-8-0|7 Account and Access
  changes in 1.8.0]]'
- '[[Changes/Cline/2025-08-28-feature-qwen-code-cli-api-support-with-oauth-by-evinelias-in-https-github-com-cl|Feature/Qwen
  Code CLI API Support with OAuth]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3|open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3]]'
source_type: github_releases
theme: account-access
title: 2 Account and Access changes in v0.6.26
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Account and Access changes in v0.6.26

**Open WebUI** · 2025-08-28 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.26) · from [[Releases/Open WebUI/open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3|v0.6.26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 **Azure Document Intelligence DefaultAzureCredential Support**: Added support for authenticating with Azure Document Intelligence using DefaultAzureCredential in addition to API key authentication, enabling seamless integration with Azure Entra ID and managed identity authentication for enterprise Azure environments.

> 🔐 **Authentication Bootstrapping Enhancements**: Added "ENABLE_INITIAL_ADMIN_SIGNUP" environment variable and "?form=true" URL parameter to enable initial admin user creation and forced login form display in SSO-only deployments. This resolves bootstrap issues where administrators couldn't create the first user when login forms were disabled, allowing proper initialization of SSO-configured deployments without requiring temporary configuration changes.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-28-2-model-support-changes-in-v0-6-26|2 Model Support changes in v0.6.26]] · Model Support
- [[Changes/Open WebUI/2025-08-28-2-context-window-changes-in-v0-6-26|2 Context Window changes in v0.6.26]] · Context Window
- [[Changes/Open WebUI/2025-08-28-code-block-copy-button-content-fixed-fixed-an-issue-where-the-copy-button-in-cod|📋 Code Block Copy Button Content Fixed]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-28-2-safety-and-privacy-changes-in-v0-6-26|2 Safety and Privacy changes in v0.6.26]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-28-2-reliability-and-performance-changes-in-v0-6-26|2 Reliability and Performance changes in v0.6.26]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-28-2-interface-experience-changes-in-v0-6-26|2 Interface Experience changes in v0.6.26]] · Interface Experience
- [[Changes/Open WebUI/2025-08-28-pdf-export-content-mismatch-fixed-resolved-an-issue-where-exporting-a-pdf-of-one|📄 PDF Export Content Mismatch Fixed]] · Memory and Personalization
- [[Changes/Open WebUI/2025-08-28-2-accessibility-and-localization-changes-in-v0-6-26|2 Accessibility and Localization changes in v0.6.26]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-28-2-search-and-browsing-changes-in-v0-6-26|2 Search and Browsing changes in v0.6.26]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-28-configurable-file-upload-processing-mode-added-process-in-background-query-param|📁 Configurable File Upload Processing Mode]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-28-3-files-and-data-changes-in-v0-6-26|3 Files and Data changes in v0.6.26]] · Files and Data
- [[Changes/Open WebUI/2025-08-28-7-other-changes-in-v0-6-26|7 other changes in v0.6.26]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2025-08-28 · Cline · [[Changes/Cline/2025-08-28-feature-qwen-code-cli-api-support-with-oauth-by-evinelias-in-https-github-com-cl|Feature/Qwen Code CLI API Support with OAuth]]
- Later: 2025-08-29 · Codex CLI · [[Changes/Codex CLI/2025-08-29-2737-changed-oauth-success-screen-to-use-the-string-codex-rather-than-codex-cli|♯2737 Changed OAuth success screen to use the string "Codex" rather than "Codex CLI"]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-28-8891f7&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-28-2-account-and-access-changes-in-v0-6-26.md%0ACard%20ID%3A%20open-webui-2025-08-28-8891f7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->