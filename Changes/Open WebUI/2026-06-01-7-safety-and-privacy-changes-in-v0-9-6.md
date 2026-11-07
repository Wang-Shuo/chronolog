---
card_id: open-webui-2026-06-01-468e35
date: '2026-06-01'
description: "Open WebUI · 2026-06-01 · Safety and Privacy: 7 changes in v0.9.6 —
  \U0001F50E **Access preview for users and groups.** Administrators can now preview
  exactly which…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2134
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4aad1c704612242923a321d7dd1e902b201dc7eeb5b10dec45513314810ec842
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-01-468e35
  comparison: ''
  date: '2026-06-01'
  description: 'Open WebUI — v0.9.6: 7 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F50E **Access preview for users and groups.** Administrators can
      now preview exactly which models, knowledge bases, and tools a given user or
      group can access, making it easier to audit and verify permission setups. [Commit](https://github.com/open-webui/open-webui/commit/9c14740ffb009d550dcbd5d6c599dac57053f112)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F6E1️ **Security Advisory**: This release includes security and
      access-control fixes. We recommend updating production deployments at your earliest
      convenience. Not all security fixes in this version may be enumerated in the
      fixed section — some may be withheld for a short time to give administrators
      time to upgrade. [Advisories](https://github.com/open-webui/open-webui/security)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F6E1️ **Tool server permission enforcement.** The per-user permission
      for inline tool servers is now enforced on chat-completion requests, so users
      without that permission can no longer bypass the admin setting by supplying
      tool servers directly in their requests. [Commit](https://github.com/open-webui/open-webui/commit/5cc1eb517094e3507915664817285f1e6e37a16d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F6A6 **Code interpreter permission on the legacy path.** The legacy
      code-execution path now enforces the same permission and capability checks as
      the current one, so users without the code interpreter permission can no longer
      trigger code execution through it. [#24724](https://github.com/open-webui/open-webui/pull/24724)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F6C2 **DNS rebinding protection for URL fetches.** The IP address
      validated for an outbound URL fetch is now the same one used for the actual
      connection, closing a DNS rebinding window where an attacker-controlled hostname
      could resolve to a public IP during the safety check and then to a private IP
      when the connection was opened. [#24759](https://github.com/open-webui/open-webui/pull/24759)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F50F **Cross-origin embed prompt control.** When Open WebUI is embedded
      in an iframe on a different origin, the embedding page can now only drive the
      chat input or submit prompts if the user has explicitly opted in via the \"iframe
      Sandbox Allow Same Origin\" setting, preventing untrusted host pages from triggering
      confirmation dialogs or controlling the chat. [#24767](https://github.com/open-webui/open-webui/pull/24767),
      [Commit](https://github.com/open-webui/open-webui/commit/eb3076c1b02d90c2ce6e6d3beb08a37987c740ec)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F9ED **Workspace skills permission.** Users granted only the \"workspace.skills\"
      permission can now see the workspace entry in the sidebar and are correctly
      routed to the skills page from the workspace index. [#24729](https://github.com/open-webui/open-webui/pull/24729)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-safety-and-privacy-changes-in-v0-9-6
  source_release: open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e
  source_type: github_releases
  theme: safety-privacy
  title: 7 Safety and Privacy changes in v0.9.6
  type: change
related_changes:
- '[[Changes/Lovable/2026-06-01-improvements-and-bug-fixes|Improvements and bug fixes]]'
- '[[Changes/Lovable/2026-06-01-security-scan-profiles|Security scan profiles]]'
- '[[Changes/Lovable/2026-06-01-scheduled-security-scans-enterprise|Scheduled security
  scans (Enterprise)]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e]]'
source_type: github_releases
theme: safety-privacy
title: 7 Safety and Privacy changes in v0.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in v0.9.6

**Open WebUI** · 2026-06-01 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.6) · from [[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔎 **Access preview for users and groups.** Administrators can now preview exactly which models, knowledge bases, and tools a given user or group can access, making it easier to audit and verify permission setups. [Commit](https://github.com/open-webui/open-webui/commit/9c14740ffb009d550dcbd5d6c599dac57053f112)

> 🛡️ **Security Advisory**: This release includes security and access-control fixes. We recommend updating production deployments at your earliest convenience. Not all security fixes in this version may be enumerated in the fixed section — some may be withheld for a short time to give administrators time to upgrade. [Advisories](https://github.com/open-webui/open-webui/security)

> 🛡️ **Tool server permission enforcement.** The per-user permission for inline tool servers is now enforced on chat-completion requests, so users without that permission can no longer bypass the admin setting by supplying tool servers directly in their requests. [Commit](https://github.com/open-webui/open-webui/commit/5cc1eb517094e3507915664817285f1e6e37a16d)

> 🚦 **Code interpreter permission on the legacy path.** The legacy code-execution path now enforces the same permission and capability checks as the current one, so users without the code interpreter permission can no longer trigger code execution through it. [#24724](https://github.com/open-webui/open-webui/pull/24724)

> 🛂 **DNS rebinding protection for URL fetches.** The IP address validated for an outbound URL fetch is now the same one used for the actual connection, closing a DNS rebinding window where an attacker-controlled hostname could resolve to a public IP during the safety check and then to a private IP when the connection was opened. [#24759](https://github.com/open-webui/open-webui/pull/24759)

> 🔏 **Cross-origin embed prompt control.** When Open WebUI is embedded in an iframe on a different origin, the embedding page can now only drive the chat input or submit prompts if the user has explicitly opted in via the "iframe Sandbox Allow Same Origin" setting, preventing untrusted host pages from triggering confirmation dialogs or controlling the chat. [#24767](https://github.com/open-webui/open-webui/pull/24767), [Commit](https://github.com/open-webui/open-webui/commit/eb3076c1b02d90c2ce6e6d3beb08a37987c740ec)

> 🧭 **Workspace skills permission.** Users granted only the "workspace.skills" permission can now see the workspace entry in the sidebar and are correctly routed to the skills page from the workspace index. [#24729](https://github.com/open-webui/open-webui/pull/24729)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-01-bulk-enable-or-disable-automations-automations-can-now-be-enabled-or-disabled-in|🔘 Bulk enable or disable automations. Automations can now be enabled or disabled…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-01-4-context-window-changes-in-v0-9-6|4 Context Window changes in v0.9.6]] · Context Window
- [[Changes/Open WebUI/2026-06-01-2-memory-and-personalization-changes-in-v0-9-6|2 Memory and Personalization changes in v0.9.6]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-01-keyboard-and-screen-reader-access-to-menus-the-integrations-more-options-and-use|♿ Keyboard and screen reader access to menus. The integrations, more-options…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-01-27-developer-workflow-changes-in-v0-9-6|27 Developer Workflow changes in v0.9.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-01-4-interface-experience-changes-in-v0-9-6|4 Interface Experience changes in v0.9.6]] · Interface Experience
- [[Changes/Open WebUI/2026-06-01-4-editor-experience-changes-in-v0-9-6|4 Editor Experience changes in v0.9.6]] · Editor Experience
- [[Changes/Open WebUI/2026-06-01-5-files-and-data-changes-in-v0-9-6|5 Files and Data changes in v0.9.6]] · Files and Data
- [[Changes/Open WebUI/2026-06-01-startup-on-non-unicode-consoles-open-webui-no-longer-crashes-at-startup-when-the|🥾 Startup on non-Unicode consoles. Open WebUI no longer crashes at startup…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-01-youtube-short-link-transcripts-pasting-a-youtu-be-short-link-into-a-chat-now-loa|📺 YouTube short link transcripts. Pasting a "youtu.be" short link into a chat…]] · Multimodal Input
- [[Changes/Open WebUI/2026-06-01-9-search-and-browsing-changes-in-v0-9-6|9 Search and Browsing changes in v0.9.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-01-shared-chat-file-write-protection-access-to-a-file-through-a-shared-chat-now-onl|🔐 Shared-chat file write protection. Access to a file through a shared chat now…]] · Collaboration
- [[Changes/Open WebUI/2026-06-01-2-enterprise-and-administration-changes-in-v0-9-6|2 Enterprise and Administration changes in v0.9.6]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-01-image-generation-with-non-standard-response-headers-image-generation-now-works-w|🖌️ Image generation with non-standard response headers. Image generation now…]] · Image Generation
- [[Changes/Open WebUI/2026-06-01-6-account-and-access-changes-in-v0-9-6|6 Account and Access changes in v0.9.6]] · Account and Access
- [[Changes/Open WebUI/2026-06-01-12-model-support-changes-in-v0-9-6|12 Model Support changes in v0.9.6]] · Model Support
- [[Changes/Open WebUI/2026-06-01-4-apps-and-integrations-changes-in-v0-9-6|4 Apps and Integrations changes in v0.9.6]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-01-5-reliability-and-performance-changes-in-v0-9-6|5 Reliability and Performance changes in v0.9.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-01-4-voice-and-audio-changes-in-v0-9-6|4 Voice and Audio changes in v0.9.6]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-01-20-other-changes-in-v0-9-6|20 other changes in v0.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-01 · Lovable · [[Changes/Lovable/2026-06-01-scheduled-security-scans-enterprise|Scheduled security scans (Enterprise)]]
- Later: 2026-06-02 · ChatGPT · [[Changes/ChatGPT/2026-06-02-we-re-rolling-out-active-sessions-a-new-security-feature-in-chatgpt-that-helps-u-51e977|ChatGPT rolls out Active sessions, a new security feature that helps users review…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-01-468e35&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-01-7-safety-and-privacy-changes-in-v0-9-6.md%0ACard%20ID%3A%20open-webui-2026-06-01-468e35%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->