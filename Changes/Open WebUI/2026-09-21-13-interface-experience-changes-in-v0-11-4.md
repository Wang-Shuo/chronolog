---
card_id: open-webui-2026-09-21-bd9469
date: '2026-09-21'
description: 'Open WebUI · 2026-09-21 · Interface Experience: 13 changes in v0.11.4
  — ✒️ **A formatting switch for notes.** A note you can edit carries a Formatting
  switch…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1351
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 476e543ed2d066737d16d20eb42d526e68db246a2c1f9afdad7cdcce8f8d5c59
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-bd9469
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 13 Interface Experience changes'
  evidence:
  - quote: '✒️ **A formatting switch for notes.** A note you can edit carries a Formatting
      switch in its menu: turned off, Markdown you type or paste stays as the characters
      you wrote, a paste keeps its plain text, and a web address is left as text,
      while formatting already in the note is untouched. [Commit](https://github.com/open-webui/open-webui/commit/d8f27e745bd31c89efa25cbe0f41bb0f70576fc5)'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F520 **Menu text scaling.** The entries in the menus that drop down
      across the interface now scale with the rest of it, rather than staying at a
      fixed size while the menu around them grew. [#29493](https://github.com/open-webui/open-webui/pull/29493),
      [#29488](https://github.com/open-webui/open-webui/issues/29488)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FA9E **Account menu highlighting.** An account menu entry carrying
      a pin button beside it now lights up across the whole row in the shared colour,
      and a long label no longer pushes the pin out of the menu. [Commit](https://github.com/open-webui/open-webui/commit/e723dcda58f638a5da2398743d22d3e5854042bf)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ⛓️ **Missing tools in links.** Opening a chat from a link whose "tools"
      or "tool-ids" parameter names a tool that no longer exists, or that the account
      cannot see, kept that id in the selection and sent it with the message; ids
      matching no tool the account has are now dropped and the rest of the link works
      as before. [#29803](https://github.com/open-webui/open-webui/pull/29803)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F515 **Reactions on read-only channels.** The reaction picker no
      longer appears on a channel open to you as a viewer alone, matching the reply
      and menu options already hidden there. [#30241](https://github.com/open-webui/open-webui/pull/30241),
      [#30240](https://github.com/open-webui/open-webui/issues/30240)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F18E **Chromium spellcheck corrections.** Picking a suggestion from
      the browser's own spelling menu in the message box did nothing, or put the misspelling
      straight back, because a highlight meant for the notes editor was being drawn
      over the selection and rebuilding the text underneath it, taking the browser's
      spelling marks with it; that highlight is now kept out of the message box and
      only drawn where the editor is not in use. [#29952](https://github.com/open-webui/open-webui/pull/29952),
      [#29944](https://github.com/open-webui/open-webui/issues/29944)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5BC️ **Tool image rendering.** Where a tool answered with an image
      tucked inside an object or a list rather than on its own, the image was written
      into the conversation as its raw text, a single screenshot costing hundreds
      of thousands of tokens and crowding out everything else; such an image is now
      taken out wherever it sits and attached to the reply, so the model is handed
      the picture and you see it. An older fault that let every second image through
      untouched goes with it, and in a saved chat such an image is now kept as a file
      and referred to rather than written into the conversation itself, so the chat
      stays small. [#29665](https://github.com/open-webui/open-webui/pull/29665),
      [#29208](https://github.com/open-webui/open-webui/issues/29208), [Commit](https://github.com/open-webui/open-webui/commit/d372bec70427fe2d568e052ce5e1529e2ad41da9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5C2️ **Unarchiving from search.** The menu on a search result offered
      to archive a chat that was already archived and said it had been archived when
      it had been brought back, and it now names and reports whichever of the two
      it did. [#30177](https://github.com/open-webui/open-webui/pull/30177)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9F9 **Sidebar after bulk actions.** Archiving, deleting or unarchiving
      every chat at once, or importing a batch of them, left the folders and the pinned
      chats in the sidebar showing what was no longer there until the page was reloaded,
      and a bulk action that failed no longer reports success. [Commit](https://github.com/open-webui/open-webui/commit/8b3ee2827241ccc952a3073b2a6bbfad5df01827)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F526 **Readable slash command labels.** The entries in the slash
      command menu no longer show as white text on a white background in the light
      theme. [#29512](https://github.com/open-webui/open-webui/pull/29512), [#29510](https://github.com/open-webui/open-webui/issues/29510)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F307 **Folder backgrounds on creation.** The background image picked
      in the Create Folder dialog now arrives on the folder when it is created from
      the sidebar, where the image was discarded unless the dialog was opened from
      an existing folder. [#30218](https://github.com/open-webui/open-webui/pull/30218),
      [#30217](https://github.com/open-webui/open-webui/issues/30217)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F587 **Delete Chat shortcut everywhere.** The keyboard shortcut
      that deletes the open chat now works wherever the chat was opened from, where
      it did nothing unless the chat's row happened to be on screen in the sidebar
      at that moment. [#30165](https://github.com/open-webui/open-webui/pull/30165),
      [#30164](https://github.com/open-webui/open-webui/issues/30164)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F441️ **Compact hover previews in Safari.** Holding over a chat
      in the sidebar shows the small preview every other browser shows, rather than
      one laid out at the width and spacing of a full conversation. [#29734](https://github.com/open-webui/open-webui/pull/29734)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 13-interface-experience-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: interface-experience
  title: 13 Interface Experience changes in v0.11.4
  type: change
related_changes:
- '[[Changes/Lovable/2026-09-18-redesigned-project-cards|Redesigned project cards]]'
- '[[Changes/OpenClaw/2026-09-19-32-interface-experience-changes-in-v2026-9-5|32 Interface
  Experience changes in v2026.9.5]]'
- '[[Changes/GitHub Copilot CLI/2026-09-21-number-key-selection-in-the-question-dialog-works-for-choices-10-and-beyond|Number-key
  selection in the question dialog works for choices 10 and beyond]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: interface-experience
title: 13 Interface Experience changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Interface Experience changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ✒️ **A formatting switch for notes.** A note you can edit carries a Formatting switch in its menu: turned off, Markdown you type or paste stays as the characters you wrote, a paste keeps its plain text, and a web address is left as text, while formatting already in the note is untouched. [Commit](https://github.com/open-webui/open-webui/commit/d8f27e745bd31c89efa25cbe0f41bb0f70576fc5)

> 🔠 **Menu text scaling.** The entries in the menus that drop down across the interface now scale with the rest of it, rather than staying at a fixed size while the menu around them grew. [#29493](https://github.com/open-webui/open-webui/pull/29493), [#29488](https://github.com/open-webui/open-webui/issues/29488)

> 🪞 **Account menu highlighting.** An account menu entry carrying a pin button beside it now lights up across the whole row in the shared colour, and a long label no longer pushes the pin out of the menu. [Commit](https://github.com/open-webui/open-webui/commit/e723dcda58f638a5da2398743d22d3e5854042bf)

> ⛓️ **Missing tools in links.** Opening a chat from a link whose "tools" or "tool-ids" parameter names a tool that no longer exists, or that the account cannot see, kept that id in the selection and sent it with the message; ids matching no tool the account has are now dropped and the rest of the link works as before. [#29803](https://github.com/open-webui/open-webui/pull/29803)

> 🔕 **Reactions on read-only channels.** The reaction picker no longer appears on a channel open to you as a viewer alone, matching the reply and menu options already hidden there. [#30241](https://github.com/open-webui/open-webui/pull/30241), [#30240](https://github.com/open-webui/open-webui/issues/30240)

> 🆎 **Chromium spellcheck corrections.** Picking a suggestion from the browser's own spelling menu in the message box did nothing, or put the misspelling straight back, because a highlight meant for the notes editor was being drawn over the selection and rebuilding the text underneath it, taking the browser's spelling marks with it; that highlight is now kept out of the message box and only drawn where the editor is not in use. [#29952](https://github.com/open-webui/open-webui/pull/29952), [#29944](https://github.com/open-webui/open-webui/issues/29944)

> 🖼️ **Tool image rendering.** Where a tool answered with an image tucked inside an object or a list rather than on its own, the image was written into the conversation as its raw text, a single screenshot costing hundreds of thousands of tokens and crowding out everything else; such an image is now taken out wherever it sits and attached to the reply, so the model is handed the picture and you see it. An older fault that let every second image through untouched goes with it, and in a saved chat such an image is now kept as a file and referred to rather than written into the conversation itself, so the chat stays small. [#29665](https://github.com/open-webui/open-webui/pull/29665), [#29208](https://github.com/open-webui/open-webui/issues/29208), [Commit](https://github.com/open-webui/open-webui/commit/d372bec70427fe2d568e052ce5e1529e2ad41da9)

> 🗂️ **Unarchiving from search.** The menu on a search result offered to archive a chat that was already archived and said it had been archived when it had been brought back, and it now names and reports whichever of the two it did. [#30177](https://github.com/open-webui/open-webui/pull/30177)

> 🧹 **Sidebar after bulk actions.** Archiving, deleting or unarchiving every chat at once, or importing a batch of them, left the folders and the pinned chats in the sidebar showing what was no longer there until the page was reloaded, and a bulk action that failed no longer reports success. [Commit](https://github.com/open-webui/open-webui/commit/8b3ee2827241ccc952a3073b2a6bbfad5df01827)

> 🔦 **Readable slash command labels.** The entries in the slash command menu no longer show as white text on a white background in the light theme. [#29512](https://github.com/open-webui/open-webui/pull/29512), [#29510](https://github.com/open-webui/open-webui/issues/29510)

> 🌇 **Folder backgrounds on creation.** The background image picked in the Create Folder dialog now arrives on the folder when it is created from the sidebar, where the image was discarded unless the dialog was opened from an existing folder. [#30218](https://github.com/open-webui/open-webui/pull/30218), [#30217](https://github.com/open-webui/open-webui/issues/30217)

> 🖇 **Delete Chat shortcut everywhere.** The keyboard shortcut that deletes the open chat now works wherever the chat was opened from, where it did nothing unless the chat's row happened to be on screen in the sidebar at that moment. [#30165](https://github.com/open-webui/open-webui/pull/30165), [#30164](https://github.com/open-webui/open-webui/issues/30164)

> 👁️ **Compact hover previews in Safari.** Holding over a chat in the sidebar shows the small preview every other browser shows, rather than one laid out at the width and spacing of a full conversation. [#29734](https://github.com/open-webui/open-webui/pull/29734)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety and Privacy changes in v0.11.4]] · Safety and Privacy
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
- [[Changes/Open WebUI/2026-09-21-4-automation-and-scheduling-changes-in-v0-11-4|4 Automation and Scheduling changes in v0.11.4]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-09-21-41-model-support-changes-in-v0-11-4|41 Model Support changes in v0.11.4]] · Model Support
- [[Changes/Open WebUI/2026-09-21-5-enterprise-and-administration-changes-in-v0-11-4|5 Enterprise and Administration changes in v0.11.4]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-09-21-61-other-changes-in-v0-11-4|61 other changes in v0.11.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-number-key-selection-in-the-question-dialog-works-for-choices-10-and-beyond|Number-key selection in the question dialog works for choices 10 and beyond]]
- Later: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-5-interface-experience-changes-in-v2-1-280|5 Interface Experience changes in v2.1.280]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-bd9469&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-13-interface-experience-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-bd9469%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->