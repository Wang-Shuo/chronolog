---
card_id: open-webui-2026-10-14-c9483c
date: '2026-10-14'
description: "Open WebUI · 2026-10-14 · Editor Experience: 4 changes in v0.12.1 —
  \U0001F9F1 **External apps in channels.** Administrators can now turn on Apps in
  Admin Settings >…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2894
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 91b6350252a906f5f2a4814f6c922d2b88efa069292040de91586ef683657659
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-14-c9483c
  comparison: ''
  date: '2026-10-14'
  description: 'Open WebUI — v0.12.1: 4 Editor Experience changes'
  evidence:
  - quote: "\U0001F9F1 **External apps in channels.** Administrators can now turn
      on Apps in Admin Settings > General, or with \"ENABLE_APPS\", and connect external
      apps in the new Apps tab of Admin Settings by their HTTPS address, reviewing
      the permissions each app asks for, such as reading its mentions, reading channel
      messages or posting messages, and choosing who may use it; channel managers
      then add an app to a channel with Add Members in the channel info, where it
      is listed with the members and its own profile picture, and mentioning it with
      @ lets it answer in the channel with replies that can be shown only to the person
      who asked, show cards with a title, fields and a thumbnail, offer buttons or
      links, follow up with a later message for longer tasks or provide a Markdown
      file to download. Apps on a private network address can be reached over plain
      HTTP once their address is listed in \"APP_ALLOWED_PRIVATE_ORIGINS\". Open WebUI
      keeps a live connection to each app, Admin Settings > Apps shows whether it
      is connected, and a failed connection names the cause, such as a rejected API
      key, a wrong public key or an unreachable address. [Commit](https://github.com/open-webui/open-webui/commit/04bccecb8e3289c9336404c1ab4c6d124fabdc2f),
      [Commit](https://github.com/open-webui/open-webui/commit/774007d7284f6266b4df728eb661c50e165cf2b2),
      [Commit](https://github.com/open-webui/open-webui/commit/2ba35625b35b2bd92fa34033dedfc29d2ab1e5fb),
      [Commit](https://github.com/open-webui/open-webui/commit/2d4712824218faa96d9da7d7772f78f2872f25db),
      [Commit](https://github.com/open-webui/open-webui/commit/4ab60527e70ffb3c75c6bf9d1ce12578dcf15e96),
      [Commit](https://github.com/open-webui/open-webui/commit/e9635596ddef29589ab3c747da4e7563bd77ad2f),
      [Commit](https://github.com/open-webui/open-webui/commit/d823ebd96d2996e2d8a5cd4cf5596c5e8b8db1fd),
      [Commit](https://github.com/open-webui/open-webui/commit/1786d6cdb0a9db80649816eaa987da4aba5de0ed),
      [Commit](https://github.com/open-webui/open-webui/commit/03f5191acab77a5e3ab9ed3c09f9e2e8ba889c20),
      [Commit](https://github.com/open-webui/open-webui/commit/be6f0a66562920f38fcb0a876ce54970a47d169c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F500 **Compare and merge a revision.** The skill file editor, the
      prompt editor and the system prompt in the model editor have a Compare revision
      button, and the chat input has Compare text in its + menu and a /compare command,
      each opening a side-by-side view where you paste a proposed revision, for example
      one written by a model, step through each change, copy changes in either direction
      and apply the result to your draft, the skill file editor also gets a Copy button
      for the open file, and comparing two files in the terminal file browser, with
      Select for Compare and Compare with Selected, now opens the same view. [Commit](https://github.com/open-webui/open-webui/commit/ab518a43218e5d1549292f7d995895cf4e8afd93),
      [Commit](https://github.com/open-webui/open-webui/commit/b374e0bb263d3793f024af1038e40e15a7f14867),
      [Commit](https://github.com/open-webui/open-webui/commit/cae8a7e19943332cae6f1f35bbe8f7b51eadf48c),
      [Commit](https://github.com/open-webui/open-webui/commit/ff502881e0d3e4acf58d4d756e3144fde259e042),
      [Commit](https://github.com/open-webui/open-webui/commit/1045d74c757bdd08151e2c18e0d44155a590495f),
      [Commit](https://github.com/open-webui/open-webui/commit/d51fffb4688d84310abba73301bc2f0c76c62c89),
      [Commit](https://github.com/open-webui/open-webui/commit/de642f1dba23d0cb5b2305704947e381c26f53c0),
      [Commit](https://github.com/open-webui/open-webui/commit/b0ba137551e1290062d8d1f3dba8ab7c6f884a1d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F4CE **Note uploads no longer stuck.** A file uploaded to a note
      while another file or edit was saved now finishes and stays attached after a
      reload, where it kept spinning and was saved without its file. [#32328](https://github.com/open-webui/open-webui/pull/32328),
      [#32327](https://github.com/open-webui/open-webui/issues/32327)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F22F **Model editor language switching.** Switching the Editing
      language in the model editor from one translated language to another now shows
      that language's name and description, where the fields kept the text of the
      language shown before. [#32224](https://github.com/open-webui/open-webui/pull/32224),
      [#32223](https://github.com/open-webui/open-webui/issues/32223)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-editor-experience-changes-in-v0-12-1
  source_release: open-webui-2026-10-14-v0-12-1-github-412917560-ae297772
  source_type: github_releases
  theme: editor-experience
  title: 4 Editor Experience changes in v0.12.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-14-3-editor-experience-changes-in-v2-1-300|3 Editor
  Experience changes in v2.1.300]]'
- '[[Changes/Claude Code/2026-10-14-2-editor-experience-changes-in-v2-1-299|2 Editor
  Experience changes in v2.1.299]]'
- "[[Changes/Open WebUI/2026-10-14-open-attached-knowledge-from-its-preview-clicking-the-name-in-the-preview-of-an|\U0001F4DA
  Open attached knowledge from its preview. Clicking the name in the preview…]]"
source_release: '[[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|open-webui-2026-10-14-v0-12-1-github-412917560-ae297772]]'
source_type: github_releases
theme: editor-experience
title: 4 Editor Experience changes in v0.12.1
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Editor Experience changes in v0.12.1

**Open WebUI** · 2026-10-14 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.1) · from [[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|v0.12.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧱 **External apps in channels.** Administrators can now turn on Apps in Admin Settings > General, or with "ENABLE_APPS", and connect external apps in the new Apps tab of Admin Settings by their HTTPS address, reviewing the permissions each app asks for, such as reading its mentions, reading channel messages or posting messages, and choosing who may use it; channel managers then add an app to a channel with Add Members in the channel info, where it is listed with the members and its own profile picture, and mentioning it with @ lets it answer in the channel with replies that can be shown only to the person who asked, show cards with a title, fields and a thumbnail, offer buttons or links, follow up with a later message for longer tasks or provide a Markdown file to download. Apps on a private network address can be reached over plain HTTP once their address is listed in "APP_ALLOWED_PRIVATE_ORIGINS". Open WebUI keeps a live connection to each app, Admin Settings > Apps shows whether it is connected, and a failed connection names the cause, such as a rejected API key, a wrong public key or an unreachable address. [Commit](https://github.com/open-webui/open-webui/commit/04bccecb8e3289c9336404c1ab4c6d124fabdc2f), [Commit](https://github.com/open-webui/open-webui/commit/774007d7284f6266b4df728eb661c50e165cf2b2), [Commit](https://github.com/open-webui/open-webui/commit/2ba35625b35b2bd92fa34033dedfc29d2ab1e5fb), [Commit](https://github.com/open-webui/open-webui/commit/2d4712824218faa96d9da7d7772f78f2872f25db), [Commit](https://github.com/open-webui/open-webui/commit/4ab60527e70ffb3c75c6bf9d1ce12578dcf15e96), [Commit](https://github.com/open-webui/open-webui/commit/e9635596ddef29589ab3c747da4e7563bd77ad2f), [Commit](https://github.com/open-webui/open-webui/commit/d823ebd96d2996e2d8a5cd4cf5596c5e8b8db1fd), [Commit](https://github.com/open-webui/open-webui/commit/1786d6cdb0a9db80649816eaa987da4aba5de0ed), [Commit](https://github.com/open-webui/open-webui/commit/03f5191acab77a5e3ab9ed3c09f9e2e8ba889c20), [Commit](https://github.com/open-webui/open-webui/commit/be6f0a66562920f38fcb0a876ce54970a47d169c)

> 🔀 **Compare and merge a revision.** The skill file editor, the prompt editor and the system prompt in the model editor have a Compare revision button, and the chat input has Compare text in its + menu and a /compare command, each opening a side-by-side view where you paste a proposed revision, for example one written by a model, step through each change, copy changes in either direction and apply the result to your draft, the skill file editor also gets a Copy button for the open file, and comparing two files in the terminal file browser, with Select for Compare and Compare with Selected, now opens the same view. [Commit](https://github.com/open-webui/open-webui/commit/ab518a43218e5d1549292f7d995895cf4e8afd93), [Commit](https://github.com/open-webui/open-webui/commit/b374e0bb263d3793f024af1038e40e15a7f14867), [Commit](https://github.com/open-webui/open-webui/commit/cae8a7e19943332cae6f1f35bbe8f7b51eadf48c), [Commit](https://github.com/open-webui/open-webui/commit/ff502881e0d3e4acf58d4d756e3144fde259e042), [Commit](https://github.com/open-webui/open-webui/commit/1045d74c757bdd08151e2c18e0d44155a590495f), [Commit](https://github.com/open-webui/open-webui/commit/d51fffb4688d84310abba73301bc2f0c76c62c89), [Commit](https://github.com/open-webui/open-webui/commit/de642f1dba23d0cb5b2305704947e381c26f53c0), [Commit](https://github.com/open-webui/open-webui/commit/b0ba137551e1290062d8d1f3dba8ab7c6f884a1d)

> 📎 **Note uploads no longer stuck.** A file uploaded to a note while another file or edit was saved now finishes and stays attached after a reload, where it kept spinning and was saved without its file. [#32328](https://github.com/open-webui/open-webui/pull/32328), [#32327](https://github.com/open-webui/open-webui/issues/32327)

> 🈯 **Model editor language switching.** Switching the Editing language in the model editor from one translated language to another now shows that language's name and description, where the fields kept the text of the language shown before. [#32224](https://github.com/open-webui/open-webui/pull/32224), [#32223](https://github.com/open-webui/open-webui/issues/32223)

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
- [[Changes/Open WebUI/2026-10-14-7-interface-experience-changes-in-v0-12-1|7 Interface Experience changes in v0.12.1]] · Interface Experience
- [[Changes/Open WebUI/2026-10-14-recurring-automations-run-once-automations-set-with-the-daily-weekly-or-monthly|📅 Recurring automations run once. Automations set with the Daily, Weekly…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-14-2-apps-and-integrations-changes-in-v0-12-1|2 Apps and Integrations changes in v0.12.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-14-memory-in-automations-automations-now-get-the-memory-tools-when-the-user-has-mem|🧠 Memory in automations. Automations now get the memory tools when the user has…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-14-2-reliability-and-performance-changes-in-v0-12-1|2 Reliability and Performance changes in v0.12.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-14-10-voice-and-audio-changes-in-v0-12-1|10 Voice and Audio changes in v0.12.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-14-11-other-changes-in-v0-12-1|11 other changes in v0.12.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-10-14 · Open WebUI · [[Changes/Open WebUI/2026-10-14-open-attached-knowledge-from-its-preview-clicking-the-name-in-the-preview-of-an|📚 Open attached knowledge from its preview. Clicking the name in the preview…]]
- Later: 2026-10-15 · Codex CLI · [[Changes/Codex CLI/2026-10-15-4-editor-experience-changes-in-rust-v0-163-0|4 Editor Experience changes in rust-v0.163.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-14-c9483c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-14-4-editor-experience-changes-in-v0-12-1.md%0ACard%20ID%3A%20open-webui-2026-10-14-c9483c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->