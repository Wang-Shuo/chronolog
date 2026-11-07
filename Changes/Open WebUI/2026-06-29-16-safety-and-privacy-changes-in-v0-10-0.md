---
card_id: open-webui-2026-06-29-82a2fb
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Safety and Privacy: 16 changes in v0.10.0
  — \U0001F91D **Share folders with your team.** You can now share a folder and the
  chats inside it…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2162
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d58e82f9f74e94ccbb1e5c0a5822df7a64b72909ad086dad484527d214a9245a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-82a2fb
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 16 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F91D **Share folders with your team.** You can now share a folder
      and the chats inside it with specific users, groups, or everyone, with read
      or write access; people you share with see shared folders in their sidebar and
      open the chats in a read-only view when they are not the owner, and administrators
      control who is allowed to share folders with a new \"Folders Sharing\" permission
      that is off by default. [Commit](https://github.com/open-webui/open-webui/commit/5019af79a0c45743ede8c9ff37d68f768e7f6174),
      [Commit](https://github.com/open-webui/open-webui/commit/38920c0ed1f6ad5fe3bb9d12898fa968ead3634a),
      [Commit](https://github.com/open-webui/open-webui/commit/d65ac445a43348c5f0323d54c37397ae7f483cb8),
      [Commit](https://github.com/open-webui/open-webui/commit/c783fd30f20d6be5028cf337bc5e5c2f9afbd3f8),
      [Commit](https://github.com/open-webui/open-webui/commit/45fcf272ef51c84cb01c1454589da3f98e4adc2c),
      [Commit](https://github.com/open-webui/open-webui/commit/76854d14246660af8222a5302513020e1f36c4f3),
      [Commit](https://github.com/open-webui/open-webui/commit/084d040e220ee39f62757d928d839646e813fb25),
      [Commit](https://github.com/open-webui/open-webui/commit/10558173fb155c63403aa8d80f16f8a3ccfa72a6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ↩️ **Reset permissions to defaults.** The group and default permission
      dialogs now include a button to restore all permissions back to their built-in
      defaults in one step. [#25931](https://github.com/open-webui/open-webui/pull/25931)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4E5 **Chat import permission.** Administrators can now control
      whether users are allowed to import or clone chats, with a new \"Allow Chat
      Import\" permission. [Commit](https://github.com/open-webui/open-webui/commit/edf3ae920989b01383be543e7379d3eade03c0b6),
      [Commit](https://github.com/open-webui/open-webui/commit/9ccda6715c3b2dc2cbc1302d2396b2f0233bdea8),
      [Commit](https://github.com/open-webui/open-webui/commit/ed4cb358a06fc6962b378f20ef846fd2b0af90bc),
      [#25927](https://github.com/open-webui/open-webui/pull/25927)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F514 **Per-group user webhook permission.** Administrators can now
      control which users may set a personal notification webhook, with a new \"User
      Webhooks\" permission. [#25923](https://github.com/open-webui/open-webui/pull/25923)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F6E1️ **Security Advisory**: This release includes security and
      access-control fixes. We recommend updating production deployments at your earliest
      convenience. Not all security fixes in this version may be enumerated in the
      fixed section — some may be withheld for a short time to give administrators
      time to upgrade. [Advisories](https://github.com/open-webui/open-webui/security)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5DD️ **API key permission enforced on all key endpoints.** Viewing
      and deleting API keys now respects the API keys permission, matching the protection
      already applied to key creation. [#25992](https://github.com/open-webui/open-webui/pull/25992)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F50A **Text-to-speech permission enforced on the speech endpoint.**
      The OpenAI speech proxy now honors the text-to-speech permission, so it can
      no longer be used by people who are not allowed to use that feature. [#25993](https://github.com/open-webui/open-webui/pull/25993)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚙️ **Interface settings update respects its permission.** Saving interface
      settings now enforces the interface permission, so users without it can no longer
      change those settings through the API. [#25996](https://github.com/open-webui/open-webui/pull/25996)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4E6 **Security updates to frontend dependencies.** Several frontend
      dependencies were updated to patch known security vulnerabilities. [#26281](https://github.com/open-webui/open-webui/pull/26281)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F91D **Chat sharing respects the user-sharing permission.** The
      share-chat dialog now hides the option to share with specific users from people
      who lack that permission, matching the access rules enforced elsewhere. [#25915](https://github.com/open-webui/open-webui/pull/25915)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4E4 **Chat export respects its permission everywhere.** Every chat
      export menu now checks the export permission, so users without it can no longer
      export chats through one of the dropdown menus. [#25914](https://github.com/open-webui/open-webui/pull/25914)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F58C️ **Image edit endpoint enforces permission.** The image-edit
      endpoint now checks the image-edit switch and the image-generation permission,
      matching image generation, so it can't be called by users who lack access. [#26009](https://github.com/open-webui/open-webui/pull/26009)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4C1 **Folder permission enforced on all folder actions.** Every
      folder operation now checks the folders permission, so the setting is respected
      consistently instead of only when listing folders. [Commit](https://github.com/open-webui/open-webui/commit/19a176fd36bea15c49d7f2d1539b4832e57a8bc2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5C2️ **Deleting nested folders checks chats correctly.** Deleting
      a folder that contains subfolders now accounts for the chats inside those subfolders
      when applying the delete-permission check, instead of only the top-level folder's
      chats. [Commit](https://github.com/open-webui/open-webui/commit/232421f40b84590e6d6fdecab4e43274aac37add),
      [#25920](https://github.com/open-webui/open-webui/issues/25920)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F6E0️ **Workspace menu shows for the skills permission.** Users
      who only have the skills permission now see the Workspace entry in their menu,
      which previously appeared only for other workspace permissions. [#25925](https://github.com/open-webui/open-webui/pull/25925)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F9E0 **Admins can always reach memories.** Administrators can now
      use the memories endpoints regardless of the memories permission toggle, matching
      how admin access works for other features. [#25924](https://github.com/open-webui/open-webui/pull/25924)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 16-safety-and-privacy-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: safety-privacy
  title: 16 Safety and Privacy changes in v0.10.0
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-06-26-add-a-host-cli-option-so-kimi-web-host-can-expose-the-server-to-the-internet-wit|Add
  a --host CLI option so kimi web --host can expose the server…]]'
- '[[Changes/Claude Code/2026-06-29-security-claude-mcp-list-get-no-longer-spawn-mcp-json-servers-that-a-repo-self-a|Security:
  claude mcp list/get no longer spawn .mcp.json servers that a repo…]]'
- '[[Changes/Lovable/2026-06-29-set-a-default-data-hosting-region-for-new-projects|Set
  a default data hosting region for new projects]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: safety-privacy
title: 16 Safety and Privacy changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Safety and Privacy changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🤝 **Share folders with your team.** You can now share a folder and the chats inside it with specific users, groups, or everyone, with read or write access; people you share with see shared folders in their sidebar and open the chats in a read-only view when they are not the owner, and administrators control who is allowed to share folders with a new "Folders Sharing" permission that is off by default. [Commit](https://github.com/open-webui/open-webui/commit/5019af79a0c45743ede8c9ff37d68f768e7f6174), [Commit](https://github.com/open-webui/open-webui/commit/38920c0ed1f6ad5fe3bb9d12898fa968ead3634a), [Commit](https://github.com/open-webui/open-webui/commit/d65ac445a43348c5f0323d54c37397ae7f483cb8), [Commit](https://github.com/open-webui/open-webui/commit/c783fd30f20d6be5028cf337bc5e5c2f9afbd3f8), [Commit](https://github.com/open-webui/open-webui/commit/45fcf272ef51c84cb01c1454589da3f98e4adc2c), [Commit](https://github.com/open-webui/open-webui/commit/76854d14246660af8222a5302513020e1f36c4f3), [Commit](https://github.com/open-webui/open-webui/commit/084d040e220ee39f62757d928d839646e813fb25), [Commit](https://github.com/open-webui/open-webui/commit/10558173fb155c63403aa8d80f16f8a3ccfa72a6)

> ↩️ **Reset permissions to defaults.** The group and default permission dialogs now include a button to restore all permissions back to their built-in defaults in one step. [#25931](https://github.com/open-webui/open-webui/pull/25931)

> 📥 **Chat import permission.** Administrators can now control whether users are allowed to import or clone chats, with a new "Allow Chat Import" permission. [Commit](https://github.com/open-webui/open-webui/commit/edf3ae920989b01383be543e7379d3eade03c0b6), [Commit](https://github.com/open-webui/open-webui/commit/9ccda6715c3b2dc2cbc1302d2396b2f0233bdea8), [Commit](https://github.com/open-webui/open-webui/commit/ed4cb358a06fc6962b378f20ef846fd2b0af90bc), [#25927](https://github.com/open-webui/open-webui/pull/25927)

> 🔔 **Per-group user webhook permission.** Administrators can now control which users may set a personal notification webhook, with a new "User Webhooks" permission. [#25923](https://github.com/open-webui/open-webui/pull/25923)

> 🛡️ **Security Advisory**: This release includes security and access-control fixes. We recommend updating production deployments at your earliest convenience. Not all security fixes in this version may be enumerated in the fixed section — some may be withheld for a short time to give administrators time to upgrade. [Advisories](https://github.com/open-webui/open-webui/security)

> 🗝️ **API key permission enforced on all key endpoints.** Viewing and deleting API keys now respects the API keys permission, matching the protection already applied to key creation. [#25992](https://github.com/open-webui/open-webui/pull/25992)

> 🔊 **Text-to-speech permission enforced on the speech endpoint.** The OpenAI speech proxy now honors the text-to-speech permission, so it can no longer be used by people who are not allowed to use that feature. [#25993](https://github.com/open-webui/open-webui/pull/25993)

> ⚙️ **Interface settings update respects its permission.** Saving interface settings now enforces the interface permission, so users without it can no longer change those settings through the API. [#25996](https://github.com/open-webui/open-webui/pull/25996)

> 📦 **Security updates to frontend dependencies.** Several frontend dependencies were updated to patch known security vulnerabilities. [#26281](https://github.com/open-webui/open-webui/pull/26281)

> 🤝 **Chat sharing respects the user-sharing permission.** The share-chat dialog now hides the option to share with specific users from people who lack that permission, matching the access rules enforced elsewhere. [#25915](https://github.com/open-webui/open-webui/pull/25915)

> 📤 **Chat export respects its permission everywhere.** Every chat export menu now checks the export permission, so users without it can no longer export chats through one of the dropdown menus. [#25914](https://github.com/open-webui/open-webui/pull/25914)

> 🖌️ **Image edit endpoint enforces permission.** The image-edit endpoint now checks the image-edit switch and the image-generation permission, matching image generation, so it can't be called by users who lack access. [#26009](https://github.com/open-webui/open-webui/pull/26009)

> 📁 **Folder permission enforced on all folder actions.** Every folder operation now checks the folders permission, so the setting is respected consistently instead of only when listing folders. [Commit](https://github.com/open-webui/open-webui/commit/19a176fd36bea15c49d7f2d1539b4832e57a8bc2)

> 🗂️ **Deleting nested folders checks chats correctly.** Deleting a folder that contains subfolders now accounts for the chats inside those subfolders when applying the delete-permission check, instead of only the top-level folder's chats. [Commit](https://github.com/open-webui/open-webui/commit/232421f40b84590e6d6fdecab4e43274aac37add), [#25920](https://github.com/open-webui/open-webui/issues/25920)

> 🛠️ **Workspace menu shows for the skills permission.** Users who only have the skills permission now see the Workspace entry in their menu, which previously appeared only for other workspace permissions. [#25925](https://github.com/open-webui/open-webui/pull/25925)

> 🧠 **Admins can always reach memories.** Administrators can now use the memories endpoints regardless of the memories permission toggle, matching how admin access works for other features. [#25924](https://github.com/open-webui/open-webui/pull/25924)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-29-5-files-and-data-changes-in-v0-10-0|5 Files and Data changes in v0.10.0]] · Files and Data
- [[Changes/Open WebUI/2026-06-29-5-memory-and-personalization-changes-in-v0-10-0|5 Memory and Personalization changes in v0.10.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-29-3-voice-and-audio-changes-in-v0-10-0|3 Voice and Audio changes in v0.10.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-29-14-interface-experience-changes-in-v0-10-0|14 Interface Experience changes in v0.10.0]] · Interface Experience
- [[Changes/Open WebUI/2026-06-29-4-collaboration-changes-in-v0-10-0|4 Collaboration changes in v0.10.0]] · Collaboration
- [[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|🪪 Client User-Agent forwarded to model backends. The browser's User-Agent is now…]] · Agent Mode
- [[Changes/Open WebUI/2026-06-29-scim-sync-can-t-demote-an-admin-a-scim-provisioning-sync-that-marks-a-user-inact|🛟 SCIM sync can't demote an admin. A SCIM provisioning sync that marks a user…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-29-8-search-and-browsing-changes-in-v0-10-0|8 Search and Browsing changes in v0.10.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-29-25-model-support-changes-in-v0-10-0|25 Model Support changes in v0.10.0]] · Model Support
- [[Changes/Open WebUI/2026-06-29-6-reliability-and-performance-changes-in-v0-10-0|6 Reliability and Performance changes in v0.10.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-29-4-mobile-and-desktop-changes-in-v0-10-0|4 Mobile and Desktop changes in v0.10.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-29-better-screen-reader-labels-on-toggles-integration-and-switch-toggles-now-expose|♿ Better screen-reader labels on toggles. Integration and switch toggles now…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-29-2-pricing-model-changes-in-v0-10-0|2 Pricing Model changes in v0.10.0]] · Pricing Model
- [[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-29-9-account-and-access-changes-in-v0-10-0|9 Account and Access changes in v0.10.0]] · Account and Access
- [[Changes/Open WebUI/2026-06-29-usable-chat-input-on-mobile-with-many-tools-when-skills-tools-terminal-web-searc|📱 Usable chat input on mobile with many tools. When skills, tools, terminal, web…]] · Image Generation
- [[Changes/Open WebUI/2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0|6 Automation and Scheduling changes in v0.10.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-29-3-context-window-changes-in-v0-10-0|3 Context Window changes in v0.10.0]] · Context Window
- [[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer Workflow changes in v0.10.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-29-10-editor-experience-changes-in-v0-10-0|10 Editor Experience changes in v0.10.0]] · Editor Experience
- [[Changes/Open WebUI/2026-06-29-29-other-changes-in-v0-10-0|29 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-29 · Lovable · [[Changes/Lovable/2026-06-29-set-a-default-data-hosting-region-for-new-projects|Set a default data hosting region for new projects]]
- Later: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-disabling-the-sandbox-for-the-rest-of-the-session-now-takes-effect-immediately-s|Disabling the sandbox for the rest of the session now takes effect immediately…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-82a2fb&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-16-safety-and-privacy-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-82a2fb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->