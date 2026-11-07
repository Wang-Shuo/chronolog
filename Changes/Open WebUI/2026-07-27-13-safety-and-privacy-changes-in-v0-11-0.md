---
card_id: open-webui-2026-07-27-25fe62
date: '2026-07-27'
description: "Open WebUI · 2026-07-27 · Safety and Privacy: 13 changes in v0.11.0
  — \U0001F30E **Share a chat with anyone holding the link.** A shared chat can now
  be set to Open so…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2190
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2c8542112b0e465db7792da29c1ce3358f809b7cedbf010bfe1bfbfb051441e1
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-27-25fe62
  comparison: ''
  date: '2026-07-27'
  description: 'Open WebUI — v0.11.0: 13 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F30E **Share a chat with anyone holding the link.** A shared chat
      can now be set to Open so it opens without signing in, with visitors no longer
      bounced to the sign-in page on their way to it, which administrators must first
      allow through a new \"Chats Open Sharing\" permission that stays off by default,
      and such pages ask search engines not to index them. [Commit](https://github.com/open-webui/open-webui/commit/1f0dc90abe879a55f654f2333e29fb0f630831c7),
      [Commit](https://github.com/open-webui/open-webui/commit/0e0d08382ac0d05b1ad98c47e8a2e37df2a185bb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F465 **Restrict sharing with groups.** Admins can now stop resources
      from being shared with entire groups through a new \"USER_PERMISSIONS_ACCESS_GRANTS_ALLOW_GROUPS\"
      permission, which stays enabled by default so existing group sharing keeps working
      untouched. [Commit](https://github.com/open-webui/open-webui/commit/4ed19d504bd30c0fc801e9228d9816669ec1c09c),
      [Commit](https://github.com/open-webui/open-webui/commit/f84dabe3d97ff701c097055023f28f3f2f7ebd07),
      [Commit](https://github.com/open-webui/open-webui/commit/77da3d8c81b9a6fda4354619de94f5d433328d8e),
      [Commit](https://github.com/open-webui/open-webui/commit/84e4d6ef8277f4b4f3ac4d355b3219e9b5a37268),
      [#27124](https://github.com/open-webui/open-webui/pull/27124)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F91D **Shared folder collaboration.** People with access to a shared
      folder can now use its files and system prompt as knowledge in chat and, with
      write access, rename and manage the folder, all according to their read or write
      permission. [Commit](https://github.com/open-webui/open-webui/commit/797293c74957bd79e42262d1dc0fd637a45d0357),
      [Commit](https://github.com/open-webui/open-webui/commit/caa2457c17e592587b804f21054cc000944af75c),
      [Commit](https://github.com/open-webui/open-webui/commit/009715cd63d1c8b5320aba68e9a70afcde519016),
      [Commit](https://github.com/open-webui/open-webui/commit/53ccd718a53de25bb6d61476a6617bfb3f130a44)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F30D **Model privacy at a glance.** Admins can now make a model
      public or private straight from its menu in the model list, where each model
      is marked as public, shared, or private. [Commit](https://github.com/open-webui/open-webui/commit/fb2ea272952ed96b0db5ac59a861637204100cb6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9F9 **Less repeated work on every response.** Security headers
      are now worked out once at startup rather than rebuilt for each response, and
      ordinary page requests skip the redirect handling they never needed, so responses
      carry less overhead. [#27229](https://github.com/open-webui/open-webui/pull/27229)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ♿ **Improved UI accessibility.** Keyboard and screen reader users can now
      tell which chat in the sidebar is the one being viewed, open reasoning and detail
      blocks in a response, expand sidebar sections and open a folder without a mouse,
      sort the admin user list from the keyboard and hear which column it is sorted
      by, open a dropdown and its submenus with the keyboard, close them again with
      Escape and land back where they started, hear which value a dropdown is set
      to rather than only its label, hear what each admin settings switch, group permission
      toggle, checkbox, API key field and advanced model parameter slider controls,
      have the message box announced by its placeholder instead of as an unnamed field,
      press Enter on Cancel in a confirmation dialog without triggering the delete,
      reach the regenerate control, jump straight past the sidebar to the conversation
      with a skip link, hear what an icon-only button does across chat, calls, file
      previews, modals and the admin pages rather than an unlabelled button, placeholder
      text, section headings, field descriptions, inactive tab labels, timestamps,
      counters and icons are now readable against their background when High Contrast
      Mode is on, and sidebar buttons across notes, automations, the playground, and
      admin pages announce whether they open or close the sidebar. [#27510](https://github.com/open-webui/open-webui/pull/27510),
      [#27513](https://github.com/open-webui/open-webui/pull/27513), [#27503](https://github.com/open-webui/open-webui/pull/27503),
      [#27494](https://github.com/open-webui/open-webui/pull/27494), [#27491](https://github.com/open-webui/open-webui/pull/27491),
      [#27490](https://github.com/open-webui/open-webui/pull/27490), [#27489](https://github.com/open-webui/open-webui/pull/27489),
      [#27488](https://github.com/open-webui/open-webui/pull/27488), [#27555](https://github.com/open-webui/open-webui/pull/27555),
      [#27556](https://github.com/open-webui/open-webui/pull/27556), [#27554](https://github.com/open-webui/open-webui/pull/27554),
      [#27558](https://github.com/open-webui/open-webui/pull/27558), [#27501](https://github.com/open-webui/open-webui/pull/27501),
      [#27492](https://github.com/open-webui/open-webui/pull/27492), [#27509](https://github.com/open-webui/open-webui/pull/27509),
      [#27502](https://github.com/open-webui/open-webui/pull/27502), [#26769](https://github.com/open-webui/open-webui/pull/26769),
      [Commit](https://github.com/open-webui/open-webui/commit/89caa7c849c471561dfd76140d0c3c3ce7a68df8),
      [Commit](https://github.com/open-webui/open-webui/commit/7801909d27b18331a9a2bc399e1d618ab99ba5bf),
      [#26768](https://github.com/open-webui/open-webui/pull/26768), [#26770](https://github.com/open-webui/open-webui/pull/26770),
      [Commit](https://github.com/open-webui/open-webui/commit/421834b2de287b8d5291d4b695ba6ed4528a5e7f),
      [Commit](https://github.com/open-webui/open-webui/commit/7bfc4bb2c25249d3922acd54d5bc516db52c8519),
      [Commit](https://github.com/open-webui/open-webui/commit/e8fda1c7a07d1a0f91201ff977b77fd5a43e014a),
      [#27508](https://github.com/open-webui/open-webui/pull/27508)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F6E1️ **Security Advisory**: This release includes security and
      access-control fixes. We recommend updating production deployments at your earliest
      convenience. Not all security fixes in this version may be enumerated in the
      fixed section. Some may be withheld for a short time to give administrators
      time to upgrade. [Advisories](https://github.com/open-webui/open-webui/security)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F529 **Updated file upload parsing library.** The library that parses
      file uploads and form submissions has been updated to a release that addresses
      a security advisory affecting that parsing path. [#26991](https://github.com/open-webui/open-webui/pull/26991)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F510 **Folder sharing permission.** The folder sharing setting in
      default and group permissions now saves instead of being silently discarded,
      so allowing or restricting folder sharing actually takes effect. [#27296](https://github.com/open-webui/open-webui/pull/27296),
      [#27120](https://github.com/open-webui/open-webui/issues/27120)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F515 **Webhook permission enforcement.** People without permission
      to use webhooks can no longer save webhook notification destinations to their
      settings, so the permission is enforced when settings are saved rather than
      only reflected in the interface. [#27297](https://github.com/open-webui/open-webui/pull/27297),
      [Commit](https://github.com/open-webui/open-webui/commit/af629177f46fa4595175f914c971c47701d1a676)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F58C️ **Image generation and web search without permission.** Turning
      on image generation or web search through the older request format now checks
      your permission first, so someone denied those features can no longer trigger
      them, and the billing that comes with them, by asking for that format. [#26703](https://github.com/open-webui/open-webui/pull/26703)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F422 **Dropped pages when fetches are paced.** Pages fetched through
      Firecrawl, Tavily, Microsoft Web IQ or Playwright are no longer discarded whenever
      the loader has to pause between requests, which quietly lost any page following
      close behind another and sometimes blamed it on a failed security check. [#27528](https://github.com/open-webui/open-webui/pull/27528),
      [#26079](https://github.com/open-webui/open-webui/issues/26079)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9D1\U0001F527 **Startup as an arbitrary user.** Running the image
      as a non-root account, as OpenShift and similar setups do, no longer fills the
      boot log with permission errors while it writes its own icons and manifest.
      [#26664](https://github.com/open-webui/open-webui/pull/26664), [#26662](https://github.com/open-webui/open-webui/issues/26662)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 13-safety-and-privacy-changes-in-v0-11-0
  source_release: open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f
  source_type: github_releases
  theme: safety-privacy
  title: 13 Safety and Privacy changes in v0.11.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-23-show-a-first-run-splash-to-opt-into-the-default-sandbox|Show
  a first-run splash to opt into the default sandbox]]'
- '[[Changes/Lovable/2026-07-23-payments-is-always-visible-in-your-project|Payments
  is always visible in your project]]'
- '[[Changes/Claude Code/2026-07-24-2-safety-and-privacy-changes-in-v2-1-219|2 Safety
  and Privacy changes in v2.1.219]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f]]'
source_type: github_releases
theme: safety-privacy
title: 13 Safety and Privacy changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Safety and Privacy changes in v0.11.0

**Open WebUI** · 2026-07-27 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) · from [[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🌎 **Share a chat with anyone holding the link.** A shared chat can now be set to Open so it opens without signing in, with visitors no longer bounced to the sign-in page on their way to it, which administrators must first allow through a new "Chats Open Sharing" permission that stays off by default, and such pages ask search engines not to index them. [Commit](https://github.com/open-webui/open-webui/commit/1f0dc90abe879a55f654f2333e29fb0f630831c7), [Commit](https://github.com/open-webui/open-webui/commit/0e0d08382ac0d05b1ad98c47e8a2e37df2a185bb)

> 👥 **Restrict sharing with groups.** Admins can now stop resources from being shared with entire groups through a new "USER_PERMISSIONS_ACCESS_GRANTS_ALLOW_GROUPS" permission, which stays enabled by default so existing group sharing keeps working untouched. [Commit](https://github.com/open-webui/open-webui/commit/4ed19d504bd30c0fc801e9228d9816669ec1c09c), [Commit](https://github.com/open-webui/open-webui/commit/f84dabe3d97ff701c097055023f28f3f2f7ebd07), [Commit](https://github.com/open-webui/open-webui/commit/77da3d8c81b9a6fda4354619de94f5d433328d8e), [Commit](https://github.com/open-webui/open-webui/commit/84e4d6ef8277f4b4f3ac4d355b3219e9b5a37268), [#27124](https://github.com/open-webui/open-webui/pull/27124)

> 🤝 **Shared folder collaboration.** People with access to a shared folder can now use its files and system prompt as knowledge in chat and, with write access, rename and manage the folder, all according to their read or write permission. [Commit](https://github.com/open-webui/open-webui/commit/797293c74957bd79e42262d1dc0fd637a45d0357), [Commit](https://github.com/open-webui/open-webui/commit/caa2457c17e592587b804f21054cc000944af75c), [Commit](https://github.com/open-webui/open-webui/commit/009715cd63d1c8b5320aba68e9a70afcde519016), [Commit](https://github.com/open-webui/open-webui/commit/53ccd718a53de25bb6d61476a6617bfb3f130a44)

> 🌍 **Model privacy at a glance.** Admins can now make a model public or private straight from its menu in the model list, where each model is marked as public, shared, or private. [Commit](https://github.com/open-webui/open-webui/commit/fb2ea272952ed96b0db5ac59a861637204100cb6)

> 🧹 **Less repeated work on every response.** Security headers are now worked out once at startup rather than rebuilt for each response, and ordinary page requests skip the redirect handling they never needed, so responses carry less overhead. [#27229](https://github.com/open-webui/open-webui/pull/27229)

> ♿ **Improved UI accessibility.** Keyboard and screen reader users can now tell which chat in the sidebar is the one being viewed, open reasoning and detail blocks in a response, expand sidebar sections and open a folder without a mouse, sort the admin user list from the keyboard and hear which column it is sorted by, open a dropdown and its submenus with the keyboard, close them again with Escape and land back where they started, hear which value a dropdown is set to rather than only its label, hear what each admin settings switch, group permission toggle, checkbox, API key field and advanced model parameter slider controls, have the message box announced by its placeholder instead of as an unnamed field, press Enter on Cancel in a confirmation dialog without triggering the delete, reach the regenerate control, jump straight past the sidebar to the conversation with a skip link, hear what an icon-only button does across chat, calls, file previews, modals and the admin pages rather than an unlabelled button, placeholder text, section headings, field descriptions, inactive tab labels, timestamps, counters and icons are now readable against their background when High Contrast Mode is on, and sidebar buttons across notes, automations, the playground, and admin pages announce whether they open or close the sidebar. [#27510](https://github.com/open-webui/open-webui/pull/27510), [#27513](https://github.com/open-webui/open-webui/pull/27513), [#27503](https://github.com/open-webui/open-webui/pull/27503), [#27494](https://github.com/open-webui/open-webui/pull/27494), [#27491](https://github.com/open-webui/open-webui/pull/27491), [#27490](https://github.com/open-webui/open-webui/pull/27490), [#27489](https://github.com/open-webui/open-webui/pull/27489), [#27488](https://github.com/open-webui/open-webui/pull/27488), [#27555](https://github.com/open-webui/open-webui/pull/27555), [#27556](https://github.com/open-webui/open-webui/pull/27556), [#27554](https://github.com/open-webui/open-webui/pull/27554), [#27558](https://github.com/open-webui/open-webui/pull/27558), [#27501](https://github.com/open-webui/open-webui/pull/27501), [#27492](https://github.com/open-webui/open-webui/pull/27492), [#27509](https://github.com/open-webui/open-webui/pull/27509), [#27502](https://github.com/open-webui/open-webui/pull/27502), [#26769](https://github.com/open-webui/open-webui/pull/26769), [Commit](https://github.com/open-webui/open-webui/commit/89caa7c849c471561dfd76140d0c3c3ce7a68df8), [Commit](https://github.com/open-webui/open-webui/commit/7801909d27b18331a9a2bc399e1d618ab99ba5bf), [#26768](https://github.com/open-webui/open-webui/pull/26768), [#26770](https://github.com/open-webui/open-webui/pull/26770), [Commit](https://github.com/open-webui/open-webui/commit/421834b2de287b8d5291d4b695ba6ed4528a5e7f), [Commit](https://github.com/open-webui/open-webui/commit/7bfc4bb2c25249d3922acd54d5bc516db52c8519), [Commit](https://github.com/open-webui/open-webui/commit/e8fda1c7a07d1a0f91201ff977b77fd5a43e014a), [#27508](https://github.com/open-webui/open-webui/pull/27508)

> 🛡️ **Security Advisory**: This release includes security and access-control fixes. We recommend updating production deployments at your earliest convenience. Not all security fixes in this version may be enumerated in the fixed section. Some may be withheld for a short time to give administrators time to upgrade. [Advisories](https://github.com/open-webui/open-webui/security)

> 🔩 **Updated file upload parsing library.** The library that parses file uploads and form submissions has been updated to a release that addresses a security advisory affecting that parsing path. [#26991](https://github.com/open-webui/open-webui/pull/26991)

> 🔐 **Folder sharing permission.** The folder sharing setting in default and group permissions now saves instead of being silently discarded, so allowing or restricting folder sharing actually takes effect. [#27296](https://github.com/open-webui/open-webui/pull/27296), [#27120](https://github.com/open-webui/open-webui/issues/27120)

> 🔕 **Webhook permission enforcement.** People without permission to use webhooks can no longer save webhook notification destinations to their settings, so the permission is enforced when settings are saved rather than only reflected in the interface. [#27297](https://github.com/open-webui/open-webui/pull/27297), [Commit](https://github.com/open-webui/open-webui/commit/af629177f46fa4595175f914c971c47701d1a676)

> 🖌️ **Image generation and web search without permission.** Turning on image generation or web search through the older request format now checks your permission first, so someone denied those features can no longer trigger them, and the billing that comes with them, by asking for that format. [#26703](https://github.com/open-webui/open-webui/pull/26703)

> 🐢 **Dropped pages when fetches are paced.** Pages fetched through Firecrawl, Tavily, Microsoft Web IQ or Playwright are no longer discarded whenever the loader has to pause between requests, which quietly lost any page following close behind another and sometimes blamed it on a failed security check. [#27528](https://github.com/open-webui/open-webui/pull/27528), [#26079](https://github.com/open-webui/open-webui/issues/26079)

> 🧑🔧 **Startup as an arbitrary user.** Running the image as a non-root account, as OpenShift and similar setups do, no longer fills the boot log with permission errors while it writes its own icons and manifest. [#26664](https://github.com/open-webui/open-webui/pull/26664), [#26662](https://github.com/open-webui/open-webui/issues/26662)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-27-9-automation-and-scheduling-changes-in-v0-11-0|9 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-27-4-voice-and-audio-changes-in-v0-11-0|4 Voice and Audio changes in v0.11.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer Workflow changes in v0.11.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-27-19-interface-experience-changes-in-v0-11-0|19 Interface Experience changes in v0.11.0]] · Interface Experience
- [[Changes/Open WebUI/2026-07-27-7-memory-and-personalization-changes-in-v0-11-0|7 Memory and Personalization changes in v0.11.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|🤖 Sub-agents. Administrators can now enable sub-agents, which let a model hand…]] · Agent Mode
- [[Changes/Open WebUI/2026-07-27-media-types-an-extraction-engine-may-handle-administrators-can-now-list-which-im|🖼️ Media types an extraction engine may handle. Administrators can now list…]] · Multimodal Input
- [[Changes/Open WebUI/2026-07-27-15-account-and-access-changes-in-v0-11-0|15 Account and Access changes in v0.11.0]] · Account and Access
- [[Changes/Open WebUI/2026-07-27-shared-image-checkpoint-changes-only-administrators-can-now-change-the-instance|🖌️ Shared image checkpoint changes. Only administrators can now change…]] · Image Generation
- [[Changes/Open WebUI/2026-07-27-7-search-and-browsing-changes-in-v0-11-0|7 Search and Browsing changes in v0.11.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-07-27-2-collaboration-changes-in-v0-11-0|2 Collaboration changes in v0.11.0]] · Collaboration
- [[Changes/Open WebUI/2026-07-27-6-apps-and-integrations-changes-in-v0-11-0|6 Apps and Integrations changes in v0.11.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-07-27-3-enterprise-and-administration-changes-in-v0-11-0|3 Enterprise and Administration changes in v0.11.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-07-27-9-context-window-changes-in-v0-11-0|9 Context Window changes in v0.11.0]] · Context Window
- [[Changes/Open WebUI/2026-07-27-12-reliability-and-performance-changes-in-v0-11-0|12 Reliability and Performance changes in v0.11.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-07-27-2-pricing-model-changes-in-v0-11-0|2 Pricing Model changes in v0.11.0]] · Pricing Model
- [[Changes/Open WebUI/2026-07-27-9-files-and-data-changes-in-v0-11-0|9 Files and Data changes in v0.11.0]] · Files and Data
- [[Changes/Open WebUI/2026-07-27-39-model-support-changes-in-v0-11-0|39 Model Support changes in v0.11.0]] · Model Support
- [[Changes/Open WebUI/2026-07-27-7-editor-experience-changes-in-v0-11-0|7 Editor Experience changes in v0.11.0]] · Editor Experience
- [[Changes/Open WebUI/2026-07-27-2-mobile-and-desktop-changes-in-v0-11-0|2 Mobile and Desktop changes in v0.11.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-07-27-42-other-changes-in-v0-11-0|42 other changes in v0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-24 · Claude Code · [[Changes/Claude Code/2026-07-24-2-safety-and-privacy-changes-in-v2-1-219|2 Safety and Privacy changes in v2.1.219]]
- Later: 2026-07-28 · Dify · [[Changes/Dify/2026-07-28-11-safety-and-privacy-changes-in-1-16-1|11 Safety and Privacy changes in 1.16.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-27-25fe62&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-27-13-safety-and-privacy-changes-in-v0-11-0.md%0ACard%20ID%3A%20open-webui-2026-07-27-25fe62%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->