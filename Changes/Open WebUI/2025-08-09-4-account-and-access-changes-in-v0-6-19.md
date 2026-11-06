---
card_id: open-webui-2025-08-09-cab31f
date: '2025-08-09'
description: "Open WebUI · 2025-08-09 · Account and Access: 4 changes in v0.6.19 —
  \U0001F4CA **Granular OpenTelemetry Metrics Configuration**: Introduced dedicated
  environment…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 863
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a582674c827de378a67a613f54bab4e1869a8f88f5bc9fd6ea5e8ee5aa74802e
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-09-cab31f
  comparison: ''
  date: '2025-08-09'
  description: 'Open WebUI — v0.6.19: 4 Account and Access changes'
  evidence:
  - quote: "\U0001F4CA **Granular OpenTelemetry Metrics Configuration**: Introduced
      dedicated environment variables and enhanced configuration options for OpenTelemetry
      metrics, allowing for separate OTLP endpoints, basic authentication credentials,
      and protocol (HTTP/gRPC) specifically for metrics export, independent of trace
      settings. This provides greater flexibility for integrating with diverse observability
      stacks."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001FAB5 **Granular OpenTelemetry Logging Configuration**: Enhanced
      the OpenTelemetry logging integration by introducing dedicated environment variables
      for logs, allowing separate OTLP endpoints, basic authentication credentials,
      and protocol (HTTP/gRPC) specifically for log export, independent of general
      OTel settings. The application's default Python logger now leverages this configuration
      to automatically send logs to your OTel endpoint when enabled via 'ENABLE_OTEL_LOGS'."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F6C2 **Customizable OAuth 'sub' Claim**: Administrators can now
      use the 'OAUTH_SUB_CLAIM_OVERRIDE' environment variable to specify which claim
      from the identity provider should be used as the unique user identifier ('sub').
      This provides greater flexibility and control for complex enterprise authentication
      setups where modifying the IDP's default claims is not possible."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '⚠️ **OAuth Configuration Warning for Missing OPENID_PROVIDER_URL**: Added
      a proactive startup warning that notifies administrators when OAuth providers
      (Google, Microsoft, or GitHub) are configured but the essential ''OPENID_PROVIDER_URL''
      environment variable is missing. This prevents silent OAuth logout failures
      and guides administrators to complete their setup correctly.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-account-and-access-changes-in-v0-6-19
  source_release: open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243
  source_type: github_releases
  theme: account-access
  title: 4 Account and Access changes in v0.6.19
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-08-06-6-account-and-access-changes-in-v0-1-18|6 Account
  and Access changes in v0.1.18]]'
- '[[Changes/Replit/2025-08-08-object-storage-agent-integration|Object Storage Agent
  integration]]'
- '[[Changes/Codex CLI/2025-08-09-https-github-com-openai-codex-pull-2042-should-help-fix-the-python-certificates|(source
  link) should help/fix the Python certificates…]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243|open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243]]'
source_type: github_releases
theme: account-access
title: 4 Account and Access changes in v0.6.19
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Account and Access changes in v0.6.19

**Open WebUI** · 2025-08-09 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.19) · from [[Releases/Open WebUI/open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243|v0.6.19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📊 **Granular OpenTelemetry Metrics Configuration**: Introduced dedicated environment variables and enhanced configuration options for OpenTelemetry metrics, allowing for separate OTLP endpoints, basic authentication credentials, and protocol (HTTP/gRPC) specifically for metrics export, independent of trace settings. This provides greater flexibility for integrating with diverse observability stacks.

> 🪵 **Granular OpenTelemetry Logging Configuration**: Enhanced the OpenTelemetry logging integration by introducing dedicated environment variables for logs, allowing separate OTLP endpoints, basic authentication credentials, and protocol (HTTP/gRPC) specifically for log export, independent of general OTel settings. The application's default Python logger now leverages this configuration to automatically send logs to your OTel endpoint when enabled via 'ENABLE_OTEL_LOGS'.

> 🛂 **Customizable OAuth 'sub' Claim**: Administrators can now use the 'OAUTH_SUB_CLAIM_OVERRIDE' environment variable to specify which claim from the identity provider should be used as the unique user identifier ('sub'). This provides greater flexibility and control for complex enterprise authentication setups where modifying the IDP's default claims is not possible.

> ⚠️ **OAuth Configuration Warning for Missing OPENID_PROVIDER_URL**: Added a proactive startup warning that notifies administrators when OAuth providers (Google, Microsoft, or GitHub) are configured but the essential 'OPENID_PROVIDER_URL' environment variable is missing. This prevents silent OAuth logout failures and guides administrators to complete their setup correctly.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-09-7-apps-and-integrations-changes-in-v0-6-19|7 Apps and Integrations changes in v0.6.19]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-09-2-editor-experience-changes-in-v0-6-19|2 Editor Experience changes in v0.6.19]] · Editor Experience
- [[Changes/Open WebUI/2025-08-09-3-enterprise-and-administration-changes-in-v0-6-19|3 Enterprise and Administration changes in v0.6.19]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-08-09-2-mobile-and-desktop-changes-in-v0-6-19|2 Mobile and Desktop changes in v0.6.19]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-08-09-2-search-and-browsing-changes-in-v0-6-19|2 Search and Browsing changes in v0.6.19]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-09-customizable-floating-quick-actions-with-tool-support-take-full-control-of-your|✍️ Customizable Floating Quick Actions with Tool Support]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-08-09-15-reliability-and-performance-changes-in-v0-6-19|15 Reliability and Performance changes in v0.6.19]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-09-2-files-and-data-changes-in-v0-6-19|2 Files and Data changes in v0.6.19]] · Files and Data
- [[Changes/Open WebUI/2025-08-09-folder-system-prompt-variables-restored-fixed-a-bug-where-prompt-variables-e-g-c|📁 Folder System Prompt Variables Restored]] · Context Window
- [[Changes/Open WebUI/2025-08-09-admin-first-whisper-language-priority-the-global-whisper-language-setting-now-ac|🗣️ Admin-First Whisper Language Priority]] · Voice and Audio
- [[Changes/Open WebUI/2025-08-09-2-developer-workflow-changes-in-v0-6-19|2 Developer Workflow changes in v0.6.19]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-09-enhanced-memory-stability-and-security-refactored-memory-update-and-delete-opera|🧠 Enhanced Memory Stability and Security]] · Memory and Personalization
- [[Changes/Open WebUI/2025-08-09-11-model-support-changes-in-v0-6-19|11 Model Support changes in v0.6.19]] · Model Support
- [[Changes/Open WebUI/2025-08-09-10-safety-and-privacy-changes-in-v0-6-19|10 Safety and Privacy changes in v0.6.19]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-09-3-collaboration-changes-in-v0-6-19|3 Collaboration changes in v0.6.19]] · Collaboration
- [[Changes/Open WebUI/2025-08-09-3-accessibility-and-localization-changes-in-v0-6-19|3 Accessibility and Localization changes in v0.6.19]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-09-13-interface-experience-changes-in-v0-6-19|13 Interface Experience changes in v0.6.19]] · Interface Experience
- [[Changes/Open WebUI/2025-08-09-29-other-changes-in-v0-6-19|29 other changes in v0.6.19]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2025-08-09 · Codex CLI · [[Changes/Codex CLI/2025-08-09-https-github-com-openai-codex-pull-2042-should-help-fix-the-python-certificates|(source link) should help/fix the Python certificates…]]
- Later: 2025-08-12 · Gemini CLI · [[Changes/Gemini CLI/2025-08-12-feat-cli-allow-exiting-authentication-menu-with-ctrl-c-sigint-by-dizzydroid-in-h|feat(cli): Allow Exiting Authentication Menu with CTRL+C (SIGINT)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-09-cab31f&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-09-4-account-and-access-changes-in-v0-6-19.md%0ACard%20ID%3A%20open-webui-2025-08-09-cab31f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->