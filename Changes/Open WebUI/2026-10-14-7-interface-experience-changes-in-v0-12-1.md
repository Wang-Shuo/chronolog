---
card_id: open-webui-2026-10-14-8f7096
date: '2026-10-14'
description: "Open WebUI · 2026-10-14 · Interface Experience: 7 changes in v0.12.1
  — \U0001FAAA **Profile cards from profile pictures.** Clicking the picture of the
  person who wrote…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2740
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5d47fcf94a63abdef9457276472584891154c9b0d4c91513c36e06541925d549
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-14-8f7096
  comparison: ''
  date: '2026-10-14'
  description: 'Open WebUI — v0.12.1: 7 Interface Experience changes'
  evidence:
  - quote: "\U0001FAAA **Profile cards from profile pictures.** Clicking the picture
      of the person who wrote a message in a shared chat, of a shared chat's owner
      in the sidebar or of a direct message partner in the sidebar now opens their
      profile card. [Commit](https://github.com/open-webui/open-webui/commit/a165c8385843c4f87e3eeb5797527004765e5708)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F5C2️ **Open sidebar folders in a new tab.** Folders in the sidebar
      can now be opened in a new tab with a middle click or Ctrl or Cmd click, and
      their link can be copied from the browser's context menu. [Commit](https://github.com/open-webui/open-webui/commit/ed3caa5619b8a577d0fc2fe2b6bdae90fc47ac69),
      [#29750](https://github.com/open-webui/open-webui/issues/29750)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F515 **Mute channels.** The menu of a channel or direct message
      now has a Notifications setting where Mentions only mutes it, so it no longer
      shows an unread count or notifies you unless someone @mentions you. [Commit](https://github.com/open-webui/open-webui/commit/e5c80682b9dc9a38274dc81eeb35a3c41be6dfd0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F4E4 **Export a skill as a .skill file.** The skill menu has Export
      .skill, which downloads one skill with all its files as a single .skill archive,
      and .skill files can be imported like ZIP files, from disk or a link. [Commit](https://github.com/open-webui/open-webui/commit/fe0e725997a7f7be16e7463b3731f0340b5a62ab)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F5C2 **Folder previews on hover.** Hovering a folder in the sidebar
      shows a card with its default model, its knowledge and its chat counts, with
      a button to edit the folder. [Commit](https://github.com/open-webui/open-webui/commit/e5c80682b9dc9a38274dc81eeb35a3c41be6dfd0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: '☁️ **Azure OpenAI Realtime calls.** Realtime voice calls can now use Azure
      OpenAI: in the Voice calls section of Audio settings, administrators pick Azure
      OpenAI as the Provider, enter the Azure endpoint and the deployment name and
      sign in with an API key or with Microsoft Entra ID, and clearer errors now point
      to wrong credentials or a wrong URL or deployment, with the "AUDIO_REALTIME_PROVIDER"
      and "AUDIO_REALTIME_AUTH_TYPE" environment variables for the new settings. [Commit](https://github.com/open-webui/open-webui/commit/3ec07745036897f52bacf24351dd71f999902034),
      [#32343](https://github.com/open-webui/open-webui/issues/32343)'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001FAA7 **Ask and Explain popup cut off.** The Ask and Explain popup
      is no longer cut off when you select text near the end of a reply and stays
      next to the selection while you scroll. [#32330](https://github.com/open-webui/open-webui/pull/32330),
      [Commit](https://github.com/open-webui/open-webui/commit/7129cc1d843b35516428c61af413b3815aee2e3b),
      [#32329](https://github.com/open-webui/open-webui/issues/32329)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-interface-experience-changes-in-v0-12-1
  source_release: open-webui-2026-10-14-v0-12-1-github-412917560-ae297772
  source_type: github_releases
  theme: interface-experience
  title: 7 Interface Experience changes in v0.12.1
  type: change
related_changes:
- '[[Changes/Devin/2026-10-14-export-findings-as-sarif|Export Findings as SARIF]]'
- '[[Changes/Kimi Code/2026-10-14-add-sticky-user-message-summaries-in-fullscreen-mode-when-a-user-message-scrolls|Add
  sticky user message summaries in fullscreen mode]]'
- '[[Changes/Lovable/2026-10-14-restore-a-deleted-project-yourself|Restore a deleted
  project yourself]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|open-webui-2026-10-14-v0-12-1-github-412917560-ae297772]]'
source_type: github_releases
theme: interface-experience
title: 7 Interface Experience changes in v0.12.1
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Interface Experience changes in v0.12.1

**Open WebUI** · 2026-10-14 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.1) · from [[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|v0.12.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🪪 **Profile cards from profile pictures.** Clicking the picture of the person who wrote a message in a shared chat, of a shared chat's owner in the sidebar or of a direct message partner in the sidebar now opens their profile card. [Commit](https://github.com/open-webui/open-webui/commit/a165c8385843c4f87e3eeb5797527004765e5708)

> 🗂️ **Open sidebar folders in a new tab.** Folders in the sidebar can now be opened in a new tab with a middle click or Ctrl or Cmd click, and their link can be copied from the browser's context menu. [Commit](https://github.com/open-webui/open-webui/commit/ed3caa5619b8a577d0fc2fe2b6bdae90fc47ac69), [#29750](https://github.com/open-webui/open-webui/issues/29750)

> 🔕 **Mute channels.** The menu of a channel or direct message now has a Notifications setting where Mentions only mutes it, so it no longer shows an unread count or notifies you unless someone @mentions you. [Commit](https://github.com/open-webui/open-webui/commit/e5c80682b9dc9a38274dc81eeb35a3c41be6dfd0)

> 📤 **Export a skill as a .skill file.** The skill menu has Export .skill, which downloads one skill with all its files as a single .skill archive, and .skill files can be imported like ZIP files, from disk or a link. [Commit](https://github.com/open-webui/open-webui/commit/fe0e725997a7f7be16e7463b3731f0340b5a62ab)

> 🗂 **Folder previews on hover.** Hovering a folder in the sidebar shows a card with its default model, its knowledge and its chat counts, with a button to edit the folder. [Commit](https://github.com/open-webui/open-webui/commit/e5c80682b9dc9a38274dc81eeb35a3c41be6dfd0)

> ☁️ **Azure OpenAI Realtime calls.** Realtime voice calls can now use Azure OpenAI: in the Voice calls section of Audio settings, administrators pick Azure OpenAI as the Provider, enter the Azure endpoint and the deployment name and sign in with an API key or with Microsoft Entra ID, and clearer errors now point to wrong credentials or a wrong URL or deployment, with the "AUDIO_REALTIME_PROVIDER" and "AUDIO_REALTIME_AUTH_TYPE" environment variables for the new settings. [Commit](https://github.com/open-webui/open-webui/commit/3ec07745036897f52bacf24351dd71f999902034), [#32343](https://github.com/open-webui/open-webui/issues/32343)

> 🪧 **Ask and Explain popup cut off.** The Ask and Explain popup is no longer cut off when you select text near the end of a reply and stays next to the selection while you scroll. [#32330](https://github.com/open-webui/open-webui/pull/32330), [Commit](https://github.com/open-webui/open-webui/commit/7129cc1d843b35516428c61af413b3815aee2e3b), [#32329](https://github.com/open-webui/open-webui/issues/32329)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-14-rich-ui-embed-console-errors-rich-ui-tool-embeds-no-longer-log-a-security-error|🧩 Rich UI embed console errors. Rich UI tool embeds no longer log a security…]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-14-6-developer-workflow-changes-in-v0-12-1|6 Developer Workflow changes in v0.12.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-14-translated-model-prompt-suggestions-editing-the-prompt-suggestions-of-a-model-th|💬 Translated model prompt suggestions. Editing the prompt suggestions of a model…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-14-tools-picked-in-new-chats-tools-picked-from-the-integrations-menu-the-web-search|🧰 Tools picked in new chats. Tools picked from the Integrations menu, the Web…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-14-2-context-window-changes-in-v0-12-1|2 Context Window changes in v0.12.1]] · Context Window
- [[Changes/Open WebUI/2026-10-14-3-account-and-access-changes-in-v0-12-1|3 Account and Access changes in v0.12.1]] · Account and Access
- [[Changes/Open WebUI/2026-10-14-save-hidden-on-others-messages-in-a-chat-shared-with-allow-replies-editing-a-mes|💾 Save hidden on others' messages. In a chat shared with Allow replies, editing…]] · Collaboration
- [[Changes/Open WebUI/2026-10-14-9-model-support-changes-in-v0-12-1|9 Model Support changes in v0.12.1]] · Model Support
- [[Changes/Open WebUI/2026-10-14-recurring-automations-run-once-automations-set-with-the-daily-weekly-or-monthly|📅 Recurring automations run once. Automations set with the Daily, Weekly…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-14-2-apps-and-integrations-changes-in-v0-12-1|2 Apps and Integrations changes in v0.12.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-14-4-editor-experience-changes-in-v0-12-1|4 Editor Experience changes in v0.12.1]] · Editor Experience
- [[Changes/Open WebUI/2026-10-14-memory-in-automations-automations-now-get-the-memory-tools-when-the-user-has-mem|🧠 Memory in automations. Automations now get the memory tools when the user has…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-14-2-reliability-and-performance-changes-in-v0-12-1|2 Reliability and Performance changes in v0.12.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-14-10-voice-and-audio-changes-in-v0-12-1|10 Voice and Audio changes in v0.12.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-14-11-other-changes-in-v0-12-1|11 other changes in v0.12.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-10-14 · Lovable · [[Changes/Lovable/2026-10-14-restore-a-deleted-project-yourself|Restore a deleted project yourself]]
- Later: 2026-10-14 · Open WebUI · [[Changes/Open WebUI/2026-10-14-2-interface-experience-changes-in-v0-12-2|2 Interface Experience changes in v0.12.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-14-8f7096&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-14-7-interface-experience-changes-in-v0-12-1.md%0ACard%20ID%3A%20open-webui-2026-10-14-8f7096%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->