---
card_id: open-webui-2026-10-14-2bafd0
date: '2026-10-14'
description: "Open WebUI · 2026-10-14 · Developer Workflow: 6 changes in v0.12.1 —
  \U0001F465 **Who wrote in a shared chat.** Chats in shared folders now show the
  pictures of…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1306
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4707770c0653f6ded2156fc4b3525601065a6ddd34714e7254e753d9d8e88c81
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-14-2bafd0
  comparison: ''
  date: '2026-10-14'
  description: 'Open WebUI — v0.12.1: 6 Developer Workflow changes'
  evidence:
  - quote: "\U0001F465 **Who wrote in a shared chat.** Chats in shared folders now
      show the pictures of everyone who wrote in them, up to three and a count for
      the rest, each opening that person's profile card. [Commit](https://github.com/open-webui/open-webui/commit/35c927ba99bea3997f57899008df2a2abd8b9354)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F576️ **Follow-ups in temporary chats.** Follow-up suggestions in
      temporary chats are now based on the reply just written, where they were generated
      without it. [Commit](https://github.com/open-webui/open-webui/commit/53a8f131f305a3beb87376d5dbc05889883fb950)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: ▶️ **Code blocks show their last value.** Running a code block in the browser
      whose last line returns a number, list or other value, such as square(7), now
      shows that value, where it stayed on Running for a minute and ended with "Execution
      Time Limit Exceeded". [#32360](https://github.com/open-webui/open-webui/pull/32360),
      [#32359](https://github.com/open-webui/open-webui/issues/32359)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F5D1️ **Deleting one language's custom translation.** In Admin Settings
      > General > Translations, Delete now removes only the translation for the language
      shown and keeps the row while other languages still have text, where it removed
      the row with its translations for every language. [Commit](https://github.com/open-webui/open-webui/commit/1283b2701ecb0037cc2c374e34e69976c302a25c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001FA9D **Webhooks for group and direct messages.** Members of group
      channels and direct messages now get their channel message webhook notifications,
      where only regular channels sent them, and muting such a channel stops them
      except for messages that mention the member. [#32404](https://github.com/open-webui/open-webui/pull/32404),
      [Commit](https://github.com/open-webui/open-webui/commit/3b2b89205e4fff7e4546ca4034e0293e2d1bd3f3),
      [#32403](https://github.com/open-webui/open-webui/issues/32403)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F4A1 **Follow-ups as next messages.** The default follow-up prompt
      now suggests the messages you would most likely send next, in your own tone
      and latest language, as requests or questions, without repeating finished work,
      with the strongest suggestion first, and reads only the chat's first message
      and the last four, each cut to 1,000 characters, so long chats stay quick, where
      it asked for questions only over the last six messages; instances with a custom
      follow-up prompt are not affected. [Commit](https://github.com/open-webui/open-webui/commit/7ae09967459151433be79c2e98f096c171fc5b18),
      [Commit](https://github.com/open-webui/open-webui/commit/53a8f131f305a3beb87376d5dbc05889883fb950)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-developer-workflow-changes-in-v0-12-1
  source_release: open-webui-2026-10-14-v0-12-1-github-412917560-ae297772
  source_type: github_releases
  theme: developer-workflow
  title: 6 Developer Workflow changes in v0.12.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-14-added-a-dir-prop-on-a-mod-s-text-for-right-to-left-text-on-windows-and-in-vs-cod|Added
  a dir prop on a mod''s Text for right-to-left text]]'
- '[[Changes/Claude Code/2026-10-14-10-developer-workflow-changes-in-v2-1-299|10 Developer
  Workflow changes in v2.1.299]]'
- '[[Changes/Open WebUI/2026-10-14-6-developer-workflow-changes-in-v0-12-2|6 Developer
  Workflow changes in v0.12.2]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|open-webui-2026-10-14-v0-12-1-github-412917560-ae297772]]'
source_type: github_releases
theme: developer-workflow
title: 6 Developer Workflow changes in v0.12.1
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Developer Workflow changes in v0.12.1

**Open WebUI** · 2026-10-14 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.1) · from [[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|v0.12.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 👥 **Who wrote in a shared chat.** Chats in shared folders now show the pictures of everyone who wrote in them, up to three and a count for the rest, each opening that person's profile card. [Commit](https://github.com/open-webui/open-webui/commit/35c927ba99bea3997f57899008df2a2abd8b9354)

> 🕶️ **Follow-ups in temporary chats.** Follow-up suggestions in temporary chats are now based on the reply just written, where they were generated without it. [Commit](https://github.com/open-webui/open-webui/commit/53a8f131f305a3beb87376d5dbc05889883fb950)

> ▶️ **Code blocks show their last value.** Running a code block in the browser whose last line returns a number, list or other value, such as square(7), now shows that value, where it stayed on Running for a minute and ended with "Execution Time Limit Exceeded". [#32360](https://github.com/open-webui/open-webui/pull/32360), [#32359](https://github.com/open-webui/open-webui/issues/32359)

> 🗑️ **Deleting one language's custom translation.** In Admin Settings > General > Translations, Delete now removes only the translation for the language shown and keeps the row while other languages still have text, where it removed the row with its translations for every language. [Commit](https://github.com/open-webui/open-webui/commit/1283b2701ecb0037cc2c374e34e69976c302a25c)

> 🪝 **Webhooks for group and direct messages.** Members of group channels and direct messages now get their channel message webhook notifications, where only regular channels sent them, and muting such a channel stops them except for messages that mention the member. [#32404](https://github.com/open-webui/open-webui/pull/32404), [Commit](https://github.com/open-webui/open-webui/commit/3b2b89205e4fff7e4546ca4034e0293e2d1bd3f3), [#32403](https://github.com/open-webui/open-webui/issues/32403)

> 💡 **Follow-ups as next messages.** The default follow-up prompt now suggests the messages you would most likely send next, in your own tone and latest language, as requests or questions, without repeating finished work, with the strongest suggestion first, and reads only the chat's first message and the last four, each cut to 1,000 characters, so long chats stay quick, where it asked for questions only over the last six messages; instances with a custom follow-up prompt are not affected. [Commit](https://github.com/open-webui/open-webui/commit/7ae09967459151433be79c2e98f096c171fc5b18), [Commit](https://github.com/open-webui/open-webui/commit/53a8f131f305a3beb87376d5dbc05889883fb950)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-14-rich-ui-embed-console-errors-rich-ui-tool-embeds-no-longer-log-a-security-error|🧩 Rich UI embed console errors. Rich UI tool embeds no longer log a security…]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-14-translated-model-prompt-suggestions-editing-the-prompt-suggestions-of-a-model-th|💬 Translated model prompt suggestions. Editing the prompt suggestions of a model…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-14-tools-picked-in-new-chats-tools-picked-from-the-integrations-menu-the-web-search|🧰 Tools picked in new chats. Tools picked from the Integrations menu, the Web…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-14-2-context-window-changes-in-v0-12-1|2 Context Window changes in v0.12.1]] · Context Window
- [[Changes/Open WebUI/2026-10-14-3-account-and-access-changes-in-v0-12-1|3 Account and Access changes in v0.12.1]] · Account and Access
- [[Changes/Open WebUI/2026-10-14-save-hidden-on-others-messages-in-a-chat-shared-with-allow-replies-editing-a-mes|💾 Save hidden on others' messages. In a chat shared with Allow replies, editing…]] · Collaboration
- [[Changes/Open WebUI/2026-10-14-9-model-support-changes-in-v0-12-1|9 Model Support changes in v0.12.1]] · Model Support
- [[Changes/Open WebUI/2026-10-14-7-interface-experience-changes-in-v0-12-1|7 Interface Experience changes in v0.12.1]] · Interface Experience
- [[Changes/Open WebUI/2026-10-14-recurring-automations-run-once-automations-set-with-the-daily-weekly-or-monthly|📅 Recurring automations run once. Automations set with the Daily, Weekly…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-14-2-apps-and-integrations-changes-in-v0-12-1|2 Apps and Integrations changes in v0.12.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-14-4-editor-experience-changes-in-v0-12-1|4 Editor Experience changes in v0.12.1]] · Editor Experience
- [[Changes/Open WebUI/2026-10-14-memory-in-automations-automations-now-get-the-memory-tools-when-the-user-has-mem|🧠 Memory in automations. Automations now get the memory tools when the user has…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-14-2-reliability-and-performance-changes-in-v0-12-1|2 Reliability and Performance changes in v0.12.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-14-10-voice-and-audio-changes-in-v0-12-1|10 Voice and Audio changes in v0.12.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-14-11-other-changes-in-v0-12-1|11 other changes in v0.12.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-10-14 · Open WebUI · [[Changes/Open WebUI/2026-10-14-6-developer-workflow-changes-in-v0-12-2|6 Developer Workflow changes in v0.12.2]]
- Later: 2026-10-15 · Claude Code · [[Changes/Claude Code/2026-10-15-2-developer-workflow-changes-in-v2-1-301|2 Developer Workflow changes in v2.1.301]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-14-2bafd0&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-14-6-developer-workflow-changes-in-v0-12-1.md%0ACard%20ID%3A%20open-webui-2026-10-14-2bafd0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->