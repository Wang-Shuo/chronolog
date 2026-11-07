---
card_id: open-webui-2024-09-24-4ccd10
date: '2024-09-24'
description: "Open WebUI · 2024-09-24 · Safety and Privacy: 2 changes in v0.3.24 —
  **\U0001F513 Authentication Toggle Issue**: Resolved the malfunction where setting…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 527
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 63806eb63fac53909b51406bdcfeee202011adf92fc46da3aa08a0faad014939
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2024-09-24-4ccd10
  comparison: ''
  date: '2024-09-24'
  description: 'Open WebUI — v0.3.24: 2 Safety and Privacy changes'
  evidence:
  - quote: "**\U0001F513 Authentication Toggle Issue**: Resolved the malfunction where
      setting 'WEBUI_AUTH=False' did not appropriately disable authentication, ensuring
      that user experience and system security settings function as configured."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.24
  - quote: "**\U0001F6E1️ Tooltip XSS Vulnerability**: Resolved a cross-site scripting
      (XSS) issue within tooltips, ensuring enhanced security and data integrity during
      user interactions."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.24
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-safety-and-privacy-changes-in-v0-3-24
  source_release: open-webui-2024-09-24-v0-3-24-github-176599575-c46b93e9
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v0.3.24
  type: change
related_changes:
- '[[Changes/Cursor/2024-09-17-this-update-fixes-the-following-security-issue-cve-2024-45599|This
  update fixes the following security issue: CVE-2024-45599]]'
- "[[Changes/Open WebUI/2024-09-19-secure-response-headers-implemented-security-response-headers-bolstering-web-app|\U0001F517
  Secure Response Headers]]"
- '[[Changes/Dify/2024-09-20-validate-user-permission-before-enter-app-detail-page-by-douxc-in-https-github-c|validate
  user permission before enter app detail page]]'
source_release: '[[Releases/Open WebUI/open-webui-2024-09-24-v0-3-24-github-176599575-c46b93e9|open-webui-2024-09-24-v0-3-24-github-176599575-c46b93e9]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v0.3.24
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v0.3.24

**Open WebUI** · 2024-09-24 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.3.24) · from [[Releases/Open WebUI/open-webui-2024-09-24-v0-3-24-github-176599575-c46b93e9|v0.3.24]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **🔓 Authentication Toggle Issue**: Resolved the malfunction where setting 'WEBUI_AUTH=False' did not appropriately disable authentication, ensuring that user experience and system security settings function as configured.

> **🛡️ Tooltip XSS Vulnerability**: Resolved a cross-site scripting (XSS) issue within tooltips, ensuring enhanced security and data integrity during user interactions.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.3.24
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2024-09-24-enhanced-audio-support-now-includes-support-for-audio-x-m4a-files-broadening-com|🎵 Enhanced Audio Support]] · Voice and Audio
- [[Changes/Open WebUI/2024-09-24-update-info-notification-for-admins-ensures-administrators-receive-immediate-upd|❗ Update Info Notification for Admins]] · Account and Access
- [[Changes/Open WebUI/2024-09-24-2-reliability-and-performance-changes-in-v0-3-24|2 Reliability and Performance changes in v0.3.24]] · Reliability and Performance
- [[Changes/Open WebUI/2024-09-24-enhanced-pdf-citations-pdf-citations-now-open-at-the-associated-page-streamlinin|📄 Enhanced PDF Citations]] · Files and Data
- [[Changes/Open WebUI/2024-09-24-temporary-file-handling-on-windows-fixed-an-issue-causing-errors-when-accessing|🗑️ Temporary File Handling On Windows]] · Mobile and Desktop
- [[Changes/Open WebUI/2024-09-24-3-model-support-changes-in-v0-3-24|3 Model Support changes in v0.3.24]] · Model Support
- [[Changes/Open WebUI/2024-09-24-2-interface-experience-changes-in-v0-3-24|2 Interface Experience changes in v0.3.24]] · Interface Experience
- [[Changes/Open WebUI/2024-09-24-9-other-changes-in-v0-3-24|9 other changes in v0.3.24]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2024-09-20 · Dify · [[Changes/Dify/2024-09-20-validate-user-permission-before-enter-app-detail-page-by-douxc-in-https-github-c|validate user permission before enter app detail page]]
- Later: 2024-10-09 · Cursor · [[Changes/Cursor/2024-10-09-update-0-42-1-0-42-5-fixes-the-following-upstream-security-issue-cve-2024-43601|UPDATE (0.42.1 - 0.42.5): Fixes the following upstream security issue: CVE-2024-43601]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2024-09-24-4ccd10&body=Card%3A%20Changes%2FOpen%20WebUI%2F2024-09-24-2-safety-and-privacy-changes-in-v0-3-24.md%0ACard%20ID%3A%20open-webui-2024-09-24-4ccd10%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.3.24%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->