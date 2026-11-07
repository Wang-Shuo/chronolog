---
card_id: open-webui-2026-09-21-0f4bf8
date: '2026-09-21'
description: "Open WebUI · 2026-09-21 · Safety and Privacy: 4 changes in v0.11.4 —
  \U0001F6E1️ **Security Advisory**: This release includes security and access-control
  fixes. We…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2246
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7c2f8144954979a0a62d79093e3910fd1974f4c3a1bba048e4576505c3e0a756
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-0f4bf8
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 4 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F6E1️ **Security Advisory**: This release includes security and
      access-control fixes. We recommend updating production deployments at your earliest
      convenience. Not all security fixes in this version may be enumerated in the
      fixed section. Some may be withheld for a short time to give administrators
      time to upgrade. [Advisories](https://github.com/open-webui/open-webui/security)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4F2 **Terminal sessions follow access changes.** A terminal connection
      now re-checks your access to it every ten seconds for as long as it stays open,
      so removing someone's permission or deactivating their account ends their live
      terminal on the next check, on every worker and not only the one they signed
      in through. [Commit](https://github.com/open-webui/open-webui/commit/a1189a2d757407530a0c1c85a41b46cd6a4f7da5),
      [Commit](https://github.com/open-webui/open-webui/commit/e8bd0661d3774248c318286849041b94bb861909)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6BB **Group picker without permission.** The picker for sharing
      a chat, a note or a knowledge base with a group was offered to accounts not
      allowed to share with groups, and is now hidden from them. [#30189](https://github.com/open-webui/open-webui/pull/30189)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6AB **Model editor error messages.** A workspace model that cannot
      be loaded for editing now says so, instead of sending you back with \"You do
      not have permission to edit this model\" whatever the real reason. [#29694](https://github.com/open-webui/open-webui/pull/29694),
      [#29629](https://github.com/open-webui/open-webui/issues/29629)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-safety-and-privacy-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v0.11.4
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-21-privacy-center-is-rolling-out-to-signed-in-chatgpt-free-go-plus-and-pro-users-it-0d2f36|Privacy
  Center in ChatGPT]]'
- '[[Changes/GitHub Copilot CLI/2026-09-21-2-safety-and-privacy-changes-in-v1-0-87|2
  Safety and Privacy changes in v1.0.87]]'
- '[[Changes/Lovable/2026-09-21-use-your-connected-tools-from-lovable-in-telegram|Use
  your connected tools from Lovable in Telegram]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🛡️ **Security Advisory**: This release includes security and access-control fixes. We recommend updating production deployments at your earliest convenience. Not all security fixes in this version may be enumerated in the fixed section. Some may be withheld for a short time to give administrators time to upgrade. [Advisories](https://github.com/open-webui/open-webui/security)

> 📲 **Terminal sessions follow access changes.** A terminal connection now re-checks your access to it every ten seconds for as long as it stays open, so removing someone's permission or deactivating their account ends their live terminal on the next check, on every worker and not only the one they signed in through. [Commit](https://github.com/open-webui/open-webui/commit/a1189a2d757407530a0c1c85a41b46cd6a4f7da5), [Commit](https://github.com/open-webui/open-webui/commit/e8bd0661d3774248c318286849041b94bb861909)

> 🚻 **Group picker without permission.** The picker for sharing a chat, a note or a knowledge base with a group was offered to accounts not allowed to share with groups, and is now hidden from them. [#30189](https://github.com/open-webui/open-webui/pull/30189)

> 🚫 **Model editor error messages.** A workspace model that cannot be loaded for editing now says so, instead of sending you back with "You do not have permission to edit this model" whatever the real reason. [#29694](https://github.com/open-webui/open-webui/pull/29694), [#29629](https://github.com/open-webui/open-webui/issues/29629)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-09-21-3-context-window-changes-in-v0-11-4|3 Context Window changes in v0.11.4]] · Context Window
- [[Changes/Open WebUI/2026-09-21-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-09-21-6-account-and-access-changes-in-v0-11-4|6 Account and Access changes in v0.11.4]] · Account and Access
- [[Changes/Open WebUI/2026-09-21-39-developer-workflow-changes-in-v0-11-4|39 Developer Workflow changes in v0.11.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-09-21-2-image-generation-changes-in-v0-11-4|2 Image Generation changes in v0.11.4]] · Image Generation
- [[Changes/Open WebUI/2026-09-21-4-collaboration-changes-in-v0-11-4|4 Collaboration changes in v0.11.4]] · Collaboration
- [[Changes/Open WebUI/2026-09-21-5-voice-and-audio-changes-in-v0-11-4|5 Voice and Audio changes in v0.11.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-09-21-10-files-and-data-changes-in-v0-11-4|10 Files and Data changes in v0.11.4]] · Files and Data
- [[Changes/Open WebUI/2026-09-21-21-editor-experience-changes-in-v0-11-4|21 Editor Experience changes in v0.11.4]] · Editor Experience
- [[Changes/Open WebUI/2026-09-21-6-memory-and-personalization-changes-in-v0-11-4|6 Memory and Personalization changes in v0.11.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-09-21-apple-device-replies-an-assistant-reply-no-longer-comes-up-blank-in-a-home-scree|📱 Apple device replies. An assistant reply no longer comes up blank in a home…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps and Integrations changes in v0.11.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-09-21-6-search-and-browsing-changes-in-v0-11-4|6 Search and Browsing changes in v0.11.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-09-21-13-interface-experience-changes-in-v0-11-4|13 Interface Experience changes in v0.11.4]] · Interface Experience
- [[Changes/Open WebUI/2026-09-21-4-automation-and-scheduling-changes-in-v0-11-4|4 Automation and Scheduling changes in v0.11.4]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-09-21-41-model-support-changes-in-v0-11-4|41 Model Support changes in v0.11.4]] · Model Support
- [[Changes/Open WebUI/2026-09-21-5-enterprise-and-administration-changes-in-v0-11-4|5 Enterprise and Administration changes in v0.11.4]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-09-21-61-other-changes-in-v0-11-4|61 other changes in v0.11.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-21 · Lovable · [[Changes/Lovable/2026-09-21-use-your-connected-tools-from-lovable-in-telegram|Use your connected tools from Lovable in Telegram]]
- Later: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-2-safety-and-privacy-changes-in-v2-1-280|2 Safety and Privacy changes in v2.1.280]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-0f4bf8&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-4-safety-and-privacy-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-0f4bf8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->