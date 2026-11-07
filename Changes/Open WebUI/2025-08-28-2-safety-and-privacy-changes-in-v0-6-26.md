---
card_id: open-webui-2025-08-28-632768
date: '2025-08-28'
description: "Open WebUI · 2025-08-28 · Safety and Privacy: 2 changes in v0.6.26 —
  \U0001F6C2 **Granular Chat Interaction Permissions**: Added fine-grained permission
  controls for…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1857
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 87dc603e8355b793bd4aa513d180adc3f108654c83e436c120e5d0cc7d7853ad
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-28-632768
  comparison: ''
  date: '2025-08-28'
  description: 'Open WebUI — v0.6.26: 2 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F6C2 **Granular Chat Interaction Permissions**: Added fine-grained
      permission controls for individual chat actions including \"Continue Response\",
      \"Regenerate Response\", \"Rate Response\", and \"Delete Messages\". Administrators
      can now configure these permissions per user group or set system defaults via
      environment variables, providing enhanced security and governance by preventing
      potential system prompt leakage through response continuation and enabling precise
      control over user interactions with AI responses."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  - quote: "\U0001F527 **Configurable Tool Call Retry Limit**: Added \"CHAT_RESPONSE_MAX_TOOL_CALL_RETRIES\"
      environment variable to control the maximum number of sequential tool calls
      allowed before safety stopping a chat session. This replaces the previous hardcoded
      limit of 10, enabling administrators to configure higher limits for complex
      workflows requiring extensive tool interactions."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-safety-and-privacy-changes-in-v0-6-26
  source_release: open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v0.6.26
  type: change
related_changes:
- '[[Changes/Replit/2025-08-22-soc-2-type-ii-certification|SOC 2 Type II certification]]'
- '[[Changes/Codex CLI/2025-08-26-2587-do-not-show-timeouts-as-sandbox-error-s|♯2587
  do not show timeouts as "sandbox error"s]]'
- '[[Changes/Dify/2025-08-27-7-safety-and-privacy-changes-in-1-8-0|7 Safety and Privacy
  changes in 1.8.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3|open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v0.6.26
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v0.6.26

**Open WebUI** · 2025-08-28 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.26) · from [[Releases/Open WebUI/open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3|v0.6.26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🛂 **Granular Chat Interaction Permissions**: Added fine-grained permission controls for individual chat actions including "Continue Response", "Regenerate Response", "Rate Response", and "Delete Messages". Administrators can now configure these permissions per user group or set system defaults via environment variables, providing enhanced security and governance by preventing potential system prompt leakage through response continuation and enabling precise control over user interactions with AI responses.

> 🔧 **Configurable Tool Call Retry Limit**: Added "CHAT_RESPONSE_MAX_TOOL_CALL_RETRIES" environment variable to control the maximum number of sequential tool calls allowed before safety stopping a chat session. This replaces the previous hardcoded limit of 10, enabling administrators to configure higher limits for complex workflows requiring extensive tool interactions.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-28-2-model-support-changes-in-v0-6-26|2 Model Support changes in v0.6.26]] · Model Support
- [[Changes/Open WebUI/2025-08-28-2-context-window-changes-in-v0-6-26|2 Context Window changes in v0.6.26]] · Context Window
- [[Changes/Open WebUI/2025-08-28-code-block-copy-button-content-fixed-fixed-an-issue-where-the-copy-button-in-cod|📋 Code Block Copy Button Content Fixed]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-28-2-reliability-and-performance-changes-in-v0-6-26|2 Reliability and Performance changes in v0.6.26]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-28-2-interface-experience-changes-in-v0-6-26|2 Interface Experience changes in v0.6.26]] · Interface Experience
- [[Changes/Open WebUI/2025-08-28-2-account-and-access-changes-in-v0-6-26|2 Account and Access changes in v0.6.26]] · Account and Access
- [[Changes/Open WebUI/2025-08-28-pdf-export-content-mismatch-fixed-resolved-an-issue-where-exporting-a-pdf-of-one|📄 PDF Export Content Mismatch Fixed]] · Memory and Personalization
- [[Changes/Open WebUI/2025-08-28-2-accessibility-and-localization-changes-in-v0-6-26|2 Accessibility and Localization changes in v0.6.26]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-28-2-search-and-browsing-changes-in-v0-6-26|2 Search and Browsing changes in v0.6.26]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-28-configurable-file-upload-processing-mode-added-process-in-background-query-param|📁 Configurable File Upload Processing Mode]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-28-3-files-and-data-changes-in-v0-6-26|3 Files and Data changes in v0.6.26]] · Files and Data
- [[Changes/Open WebUI/2025-08-28-7-other-changes-in-v0-6-26|7 other changes in v0.6.26]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2025-08-27 · Dify · [[Changes/Dify/2025-08-27-7-safety-and-privacy-changes-in-1-8-0|7 Safety and Privacy changes in 1.8.0]]
- Later: 2025-08-29 · Replit · [[Changes/Replit/2025-08-29-security-rating-improvement|Security rating improvement]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-28-632768&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-28-2-safety-and-privacy-changes-in-v0-6-26.md%0ACard%20ID%3A%20open-webui-2025-08-28-632768%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->