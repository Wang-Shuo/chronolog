---
card_id: open-webui-2026-10-25-60999e
date: '2026-10-25'
description: "Open WebUI · 2026-10-25 · Interface Experience: 13 changes in v0.12.4
  — \U0001F576️ **Hide controls for users.** Administrators can now hide single controls
  from users…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1385
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 75de89795a2dd700cfc1d142a53833aa9653e2c5b060651cd8e36482a588dc61
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-25-60999e
  comparison: ''
  date: '2026-10-25'
  description: 'Open WebUI — v0.12.4: 13 Interface Experience changes'
  evidence:
  - quote: "\U0001F576️ **Hide controls for users.** Administrators can now hide single
      controls from users under Visible controls in Admin Settings > Interface or
      with \"UI_VISIBILITY\", such as model capabilities, default features and built-in
      tools in the model editor, Capture, Compare text, Attach Webpage, Attach Files,
      Attach Notes, Attach Knowledge and Reference Chats in the + menu, the /status,
      /model and /settings commands, the usage info, Fork, Merge Responses, Preview,
      Artifacts, Archive and Tags in chats, Set as default and Keep in Sidebar for
      models and settings such as the Usage tab and the speech engines, while hidden
      controls keep their values and the features behind them stay usable, hiding
      Archive also hides Unarchive, and administrators still see every control. [Commit](https://github.com/open-webui/open-webui/commit/08bfaa4be67f6f87878b2209d568a648818506a7),
      [#32830](https://github.com/open-webui/open-webui/issues/32830)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F5E8️ **New chat from folders.** A folder's menu in the sidebar
      now has a New Chat item that starts a chat in that folder. [Commit](https://github.com/open-webui/open-webui/commit/0512f1b3763ea4e15b5adc25d087c96f728fa25e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F522 **Turn count in chat previews.** The preview shown when hovering
      a chat in the sidebar now shows how many user and assistant turns its current
      branch has. [Commit](https://github.com/open-webui/open-webui/commit/b5046f9d8686e18450a200dccda181f2ac7f97c9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001FAF2 **Swipe open Chat Controls.** On a phone, swiping left across
      a chat now pulls in the Chat Controls panel, which follows your finger like
      the sidebar does and closes again with a swipe to the right. [Commit](https://github.com/open-webui/open-webui/commit/f83f9f40b3513acc82f53696aaf78a2c5d251e70)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: ♿ **Improved UI accessibility.** Screen reader users now hear the Send
      button, the sidebar's user menu button by the name it shows, Playground's role
      button by the word it shows, the model editor's Description, Tools, Skills,
      Filters and Actions rows by what they show, a sidebar folder's options button,
      the sidebar button on Calendar, Notes, Channels and Home on phones, the on/off
      switches on Skills, Functions and Automations rows, the suggested prompts on
      a new chat as buttons, Archived Chats as a table, the sort order on the column
      headers of Archived Chats and the Evaluations leaderboard, chat input pills
      and menus, copy, export, merge and artifact buttons, clear search and Cancel
      buttons, the note editor's Undo, Redo, Record and Note Menu buttons, Playground's
      System Instructions button and model selects, the code box in the tool and function
      editors, switches, icon buttons, selects and number inputs in Admin Settings,
      the Create knowledge base, Create Prompt and Clone Prompt dialogs and the close
      button of 22 dialogs by name, together with a source's number, the number on
      a channel's member count button, the choice a Visibility button shows, a resizable
      panel's width, how long ago each sidebar chat was updated, the info button under
      a reply with its usage figures, a model's description, notifications such as
      copy confirmations (copying a prompt in Workspace included), when a reply starts
      and finishes, call mode's Listening and Thinking status, menu buttons as menus
      with their open state, the selected search content type, how many archived chats
      a search found, how many models match a search in the model picker, the Settings
      window by name, the sidebar folder toggle by name with its open state, the chosen
      option in Select dropdowns, the search window's list by its visible caption,
      a heading on each Workspace page, the sidebar section titles and chat date groups
      as headings, the sidebar's models, folders and chats as lists, the Settings
      tabs as Personal and Admin tab lists that point to their panels, the items of
      the input, integrations, user and chat menus as menu items, the Keyboard tab's
      shortcut categories as headings with a list under each, the chat input as a
      text field, the sidebar logo link as New Chat, the onboarding logo by the instance
      name with other branding images hidden as decoration, the model logos on a new
      chat by model name (hidden when only one model is selected), the model the arrow
      keys are on in the model picker, the model name and the Suggested label on a
      new chat as headings, the suggestion list by name and the chat title as the
      page heading, and no longer hear an open or closed state on the area around
      the sidebar button in Channels on phones; keyboard users get the model picker's
      More and Eject buttons that show on focus, filter lists that move focus to their
      options when opened, tooltips that show on focus and close with Escape, Escape
      in the model picker's More menu or filter list that closes only that list, focus
      that returns to the model picker button when the picker closes with Accessibility
      Mode on, an outline on the model picker row the arrow keys are on, focus that
      moves to the other sidebar button when the sidebar opens or closes, arrow keys
      that move through the input, integrations, user, chat and Terminal menus, a
      Terminal menu that opens on its first terminal, a Tab key that reaches the note
      editor's Record and Note Menu buttons, Evaluations leaderboard columns they
      can sort and models they can open from it, focus that stays on a Workspace section
      link after choosing it, focus that stays in the Archived Chats list after unarchiving
      a chat, focus on the recording bar when dictation starts and a Skip to main
      content link that now moves focus to the page content; notification text in
      the light theme and the chat dates in Archived Chats now meet the 4.5:1 contrast
      minimum; buttons in the collapsed sidebar, on sidebar folders, on Prompts, Skills,
      Functions and Automations rows, on Workspace and Notes list rows, on attached
      files and in the Integrations menu are no longer nested inside other buttons;
      the Archived Chats and Keyboard lists stay usable at 400% zoom; and with Accessibility
      Mode on, pinch zoom works on phones, the active Workspace section is underlined,
      code editor placeholders, the model editor's JSON Preview row and Calendar's
      days from other months and today's date meet the contrast minimum, and the More
      and Eject buttons and Set as default in the model picker, the version link and
      See what's new in Settings > About, the sidebar's Chat Menu button, the Note
      Menu and Delete buttons in Notes, the More button on file rows, the Create button's
      menu arrow, Calendar's previous and next month buttons and the name, ID and
      command fields in the model and prompt editors are at least 24 pixels in size.
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F9F9 **Deleting the open chat.** Deleting the chat you are viewing
      from the sidebar now opens an empty new chat, where the deleted chat's messages
      stayed on screen and the next message failed, in Safari with \"The string did
      not match the expected pattern.\" [#33069](https://github.com/open-webui/open-webui/pull/33069),
      [Commit](https://github.com/open-webui/open-webui/commit/c04e408432b24e2a6cbeb2eaf513b8f2840460b6),
      [#33068](https://github.com/open-webui/open-webui/issues/33068)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F5BC️ **Note menu image uploads.** Images picked with Upload files
      in a note's menu now appear in the note, where they were saved with the note's
      files but never inserted. [#32793](https://github.com/open-webui/open-webui/pull/32793),
      [Commit](https://github.com/open-webui/open-webui/commit/4604f2a3bc2f112135eac75c06048916d3ff37df),
      [#32792](https://github.com/open-webui/open-webui/issues/32792)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4C2 **Open folder stays open.** Deleting another folder in the
      sidebar no longer closes the folder page you have open. [#32697](https://github.com/open-webui/open-webui/pull/32697),
      [Commit](https://github.com/open-webui/open-webui/commit/db9aa8c9c02f841f4d35f65ee061eddd2e4a57f9),
      [#32696](https://github.com/open-webui/open-webui/issues/32696)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4DD **Note pins and counts.** The Notes list now shows Pin for
      a note unpinned from the sidebar, and readers of a note shared as read only
      see its word and character counts instead of zero. [#32707](https://github.com/open-webui/open-webui/pull/32707),
      [Commit](https://github.com/open-webui/open-webui/commit/6a7205e965072a016c9c3046e1be320921a0af5f),
      [#32706](https://github.com/open-webui/open-webui/issues/32706), [#32711](https://github.com/open-webui/open-webui/pull/32711),
      [Commit](https://github.com/open-webui/open-webui/commit/252338964223cc75b5d0f02ba9e3cb7f6bd9ab90),
      [#32710](https://github.com/open-webui/open-webui/issues/32710)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4AC **Prompts from / in channels.** Picking a prompt from the /
      menu in a channel now inserts the prompt text instead of a command chip. [#32713](https://github.com/open-webui/open-webui/pull/32713),
      [Commit](https://github.com/open-webui/open-webui/commit/1d0b78271910cb5a20e121fd586389906b87dbbe),
      [#32712](https://github.com/open-webui/open-webui/issues/32712)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F95E **One model More menu open.** Clicking the More button of another
      model in the model picker, or clicking another model, now closes the More menu
      that was open, where the menus stayed open and piled up over the picker. [#33020](https://github.com/open-webui/open-webui/pull/33020),
      [Commit](https://github.com/open-webui/open-webui/commit/fa629e5ca5015f6bc3e3be1f7a4a76c5ccd57e18),
      [#33019](https://github.com/open-webui/open-webui/issues/33019)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: ⌨️ **Shift quick actions removed.** Holding Shift over a sidebar chat no
      longer shows the quick Archive and Delete buttons, since Shift-click now selects
      chats, which are then archived or deleted together, and deleting asks for confirmation
      first. [Commit](https://github.com/open-webui/open-webui/commit/acc231774d00d8856feefd2e7a3ef4b503a8224e),
      [#32543](https://github.com/open-webui/open-webui/issues/32543)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: ✉️ **No emails on hover.** Hovering an owner in the workspace lists and
      admin Functions, or a person in access settings, no longer shows their email
      address, since the profile card that replaces the tooltip does not include it.
      [Commit](https://github.com/open-webui/open-webui/commit/02974f41e9b7c9d34f2cd7c664c2a04fd6ac12ae),
      [Commit](https://github.com/open-webui/open-webui/commit/72cc79b8f336a753b6e75e0f3415630601b14759),
      [Commit](https://github.com/open-webui/open-webui/commit/ba34b1c47c1d054d2f9c498d0aed862ec06da41a)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 13-interface-experience-changes-in-v0-12-4
  source_release: open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79
  source_type: github_releases
  theme: interface-experience
  title: 13 Interface Experience changes in v0.12.4
  type: change
related_changes:
- '[[Changes/Dify/2026-10-23-2-interface-experience-changes-in-1-18-0|2 Interface
  Experience changes in 1.18.0]]'
- '[[Changes/OpenHands/2026-10-23-refactor-sidebar-express-mobile-drawer-duration-in-css-by-enyst-in-https-github|refactor(sidebar):
  express mobile drawer duration in CSS]]'
- '[[Changes/Windsurf/2026-10-23-2-interface-experience-changes-in-v3-11-212|2 Interface
  Experience changes in v3.11.212]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79]]'
source_type: github_releases
theme: interface-experience
title: 13 Interface Experience changes in v0.12.4
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Interface Experience changes in v0.12.4

**Open WebUI** · 2026-10-25 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.4) · from [[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|v0.12.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🕶️ **Hide controls for users.** Administrators can now hide single controls from users under Visible controls in Admin Settings > Interface or with "UI_VISIBILITY", such as model capabilities, default features and built-in tools in the model editor, Capture, Compare text, Attach Webpage, Attach Files, Attach Notes, Attach Knowledge and Reference Chats in the + menu, the /status, /model and /settings commands, the usage info, Fork, Merge Responses, Preview, Artifacts, Archive and Tags in chats, Set as default and Keep in Sidebar for models and settings such as the Usage tab and the speech engines, while hidden controls keep their values and the features behind them stay usable, hiding Archive also hides Unarchive, and administrators still see every control. [Commit](https://github.com/open-webui/open-webui/commit/08bfaa4be67f6f87878b2209d568a648818506a7), [#32830](https://github.com/open-webui/open-webui/issues/32830)

> 🗨️ **New chat from folders.** A folder's menu in the sidebar now has a New Chat item that starts a chat in that folder. [Commit](https://github.com/open-webui/open-webui/commit/0512f1b3763ea4e15b5adc25d087c96f728fa25e)

> 🔢 **Turn count in chat previews.** The preview shown when hovering a chat in the sidebar now shows how many user and assistant turns its current branch has. [Commit](https://github.com/open-webui/open-webui/commit/b5046f9d8686e18450a200dccda181f2ac7f97c9)

> 🫲 **Swipe open Chat Controls.** On a phone, swiping left across a chat now pulls in the Chat Controls panel, which follows your finger like the sidebar does and closes again with a swipe to the right. [Commit](https://github.com/open-webui/open-webui/commit/f83f9f40b3513acc82f53696aaf78a2c5d251e70)

> ♿ **Improved UI accessibility.** Screen reader users now hear the Send button, the sidebar's user menu button by the name it shows, Playground's role button by the word it shows, the model editor's Description, Tools, Skills, Filters and Actions rows by what they show, a sidebar folder's options button, the sidebar button on Calendar, Notes, Channels and Home on phones, the on/off switches on Skills, Functions and Automations rows, the suggested prompts on a new chat as buttons, Archived Chats as a table, the sort order on the column headers of Archived Chats and the Evaluations leaderboard, chat input pills and menus, copy, export, merge and artifact buttons, clear search and Cancel buttons, the note editor's Undo, Redo, Record and Note Menu buttons, Playground's System Instructions button and model selects, the code box in the tool and function editors, switches, icon buttons, selects and number inputs in Admin Settings, the Create knowledge base, Create Prompt and Clone Prompt dialogs and the close button of 22 dialogs by name, together with a source's number, the number on a channel's member count button, the choice a Visibility button shows, a resizable panel's width, how long ago each sidebar chat was updated, the info button under a reply with its usage figures, a model's description, notifications such as copy confirmations (copying a prompt in Workspace included), when a reply starts and finishes, call mode's Listening and Thinking status, menu buttons as menus with their open state, the selected search content type, how many archived chats a search found, how many models match a search in the model picker, the Settings window by name, the sidebar folder toggle by name with its open state, the chosen option in Select dropdowns, the search window's list by its visible caption, a heading on each Workspace page, the sidebar section titles and chat date groups as headings, the sidebar's models, folders and chats as lists, the Settings tabs as Personal and Admin tab lists that point to their panels, the items of the input, integrations, user and chat menus as menu items, the Keyboard tab's shortcut categories as headings with a list under each, the chat input as a text field, the sidebar logo link as New Chat, the onboarding logo by the instance name with other branding images hidden as decoration, the model logos on a new chat by model name (hidden when only one model is selected), the model the arrow keys are on in the model picker, the model name and the Suggested label on a new chat as headings, the suggestion list by name and the chat title as the page heading, and no longer hear an open or closed state on the area around the sidebar button in Channels on phones; keyboard users get the model picker's More and Eject buttons that show on focus, filter lists that move focus to their options when opened, tooltips that show on focus and close with Escape, Escape in the model picker's More menu or filter list that closes only that list, focus that returns to the model picker button when the picker closes with Accessibility Mode on, an outline on the model picker row the arrow keys are on, focus that moves to the other sidebar button when the sidebar opens or closes, arrow keys that move through the input, integrations, user, chat and Terminal menus, a Terminal menu that opens on its first terminal, a Tab key that reaches the note editor's Record and Note Menu buttons, Evaluations leaderboard columns they can sort and models they can open from it, focus that stays on a Workspace section link after choosing it, focus that stays in the Archived Chats list after unarchiving a chat, focus on the recording bar when dictation starts and a Skip to main content link that now moves focus to the page content; notification text in the light theme and the chat dates in Archived Chats now meet the 4.5:1 contrast minimum; buttons in the collapsed sidebar, on sidebar folders, on Prompts, Skills, Functions and Automations rows, on Workspace and Notes list rows, on attached files and in the Integrations menu are no longer nested inside other buttons; the Archived Chats and Keyboard lists stay usable at 400% zoom; and with Accessibility Mode on, pinch zoom works on phones, the active Workspace section is underlined, code editor placeholders, the model editor's JSON Preview row and Calendar's days from other months and today's date meet the contrast minimum, and the More and Eject buttons and Set as default in the model picker, the version link and See what's new in Settings > About, the sidebar's Chat Menu button, the Note Menu and Delete buttons in Notes, the More button on file rows, the Create button's menu arrow, Calendar's previous and next month buttons and the name, ID and command fields in the model and prompt editors are at least 24 pixels in size.

> 🧹 **Deleting the open chat.** Deleting the chat you are viewing from the sidebar now opens an empty new chat, where the deleted chat's messages stayed on screen and the next message failed, in Safari with "The string did not match the expected pattern." [#33069](https://github.com/open-webui/open-webui/pull/33069), [Commit](https://github.com/open-webui/open-webui/commit/c04e408432b24e2a6cbeb2eaf513b8f2840460b6), [#33068](https://github.com/open-webui/open-webui/issues/33068)

> 🖼️ **Note menu image uploads.** Images picked with Upload files in a note's menu now appear in the note, where they were saved with the note's files but never inserted. [#32793](https://github.com/open-webui/open-webui/pull/32793), [Commit](https://github.com/open-webui/open-webui/commit/4604f2a3bc2f112135eac75c06048916d3ff37df), [#32792](https://github.com/open-webui/open-webui/issues/32792)

> 📂 **Open folder stays open.** Deleting another folder in the sidebar no longer closes the folder page you have open. [#32697](https://github.com/open-webui/open-webui/pull/32697), [Commit](https://github.com/open-webui/open-webui/commit/db9aa8c9c02f841f4d35f65ee061eddd2e4a57f9), [#32696](https://github.com/open-webui/open-webui/issues/32696)

> 📝 **Note pins and counts.** The Notes list now shows Pin for a note unpinned from the sidebar, and readers of a note shared as read only see its word and character counts instead of zero. [#32707](https://github.com/open-webui/open-webui/pull/32707), [Commit](https://github.com/open-webui/open-webui/commit/6a7205e965072a016c9c3046e1be320921a0af5f), [#32706](https://github.com/open-webui/open-webui/issues/32706), [#32711](https://github.com/open-webui/open-webui/pull/32711), [Commit](https://github.com/open-webui/open-webui/commit/252338964223cc75b5d0f02ba9e3cb7f6bd9ab90), [#32710](https://github.com/open-webui/open-webui/issues/32710)

> 💬 **Prompts from / in channels.** Picking a prompt from the / menu in a channel now inserts the prompt text instead of a command chip. [#32713](https://github.com/open-webui/open-webui/pull/32713), [Commit](https://github.com/open-webui/open-webui/commit/1d0b78271910cb5a20e121fd586389906b87dbbe), [#32712](https://github.com/open-webui/open-webui/issues/32712)

> 🥞 **One model More menu open.** Clicking the More button of another model in the model picker, or clicking another model, now closes the More menu that was open, where the menus stayed open and piled up over the picker. [#33020](https://github.com/open-webui/open-webui/pull/33020), [Commit](https://github.com/open-webui/open-webui/commit/fa629e5ca5015f6bc3e3be1f7a4a76c5ccd57e18), [#33019](https://github.com/open-webui/open-webui/issues/33019)

> ⌨️ **Shift quick actions removed.** Holding Shift over a sidebar chat no longer shows the quick Archive and Delete buttons, since Shift-click now selects chats, which are then archived or deleted together, and deleting asks for confirmation first. [Commit](https://github.com/open-webui/open-webui/commit/acc231774d00d8856feefd2e7a3ef4b503a8224e), [#32543](https://github.com/open-webui/open-webui/issues/32543)

> ✉️ **No emails on hover.** Hovering an owner in the workspace lists and admin Functions, or a person in access settings, no longer shows their email address, since the profile card that replaces the tooltip does not include it. [Commit](https://github.com/open-webui/open-webui/commit/02974f41e9b7c9d34f2cd7c664c2a04fd6ac12ae), [Commit](https://github.com/open-webui/open-webui/commit/72cc79b8f336a753b6e75e0f3415630601b14759), [Commit](https://github.com/open-webui/open-webui/commit/ba34b1c47c1d054d2f9c498d0aed862ec06da41a)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-25-16-model-support-changes-in-v0-12-4|16 Model Support changes in v0.12.4]] · Model Support
- [[Changes/Open WebUI/2026-10-25-10-safety-and-privacy-changes-in-v0-12-4|10 Safety and Privacy changes in v0.12.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-25-images-settings-save-admins-can-now-save-images-settings-while-image-generation|🖌️ Images settings save. Admins can now save Images settings while Image…]] · Image Generation
- [[Changes/Open WebUI/2026-10-25-4-voice-and-audio-changes-in-v0-12-4|4 Voice and Audio changes in v0.12.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-25-4-context-window-changes-in-v0-12-4|4 Context Window changes in v0.12.4]] · Context Window
- [[Changes/Open WebUI/2026-10-25-5-apps-and-integrations-changes-in-v0-12-4|5 Apps and Integrations changes in v0.12.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-25-49-developer-workflow-changes-in-v0-12-4|49 Developer Workflow changes in v0.12.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-25-4-editor-experience-changes-in-v0-12-4|4 Editor Experience changes in v0.12.4]] · Editor Experience
- [[Changes/Open WebUI/2026-10-25-3-reliability-and-performance-changes-in-v0-12-4|3 Reliability and Performance changes in v0.12.4]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-25-5-account-and-access-changes-in-v0-12-4|5 Account and Access changes in v0.12.4]] · Account and Access
- [[Changes/Open WebUI/2026-10-25-3-files-and-data-changes-in-v0-12-4|3 Files and Data changes in v0.12.4]] · Files and Data
- [[Changes/Open WebUI/2026-10-25-shared-chat-pages-load-once-chats-opened-under-s-through-a-share-link-or-by-an-a|🔗 Shared chat pages load once. Chats opened under /s/, through a share link…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-25-web-search-settings-save-admins-can-now-save-web-search-settings-such-as-the-web|🌍 Web Search settings save. Admins can now save Web Search settings such…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-25-translation-updates-translations-for-korean-cebuano-thai-german-japanese-vietnam|🌐 Translation updates. Translations for Korean, Cebuano, Thai, German, Japanese…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-10-23 · Windsurf · [[Changes/Windsurf/2026-10-23-2-interface-experience-changes-in-v3-11-212|2 Interface Experience changes in v3.11.212]]
- Later: 2026-10-26 · Claude Code · [[Changes/Claude Code/2026-10-26-changed-clicks-on-scrollbar-arrows-and-bars-in-fullscreen-lists-to-act-when-the|Changed clicks on scrollbar arrows and bars in fullscreen lists to act…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-25-60999e&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-25-13-interface-experience-changes-in-v0-12-4.md%0ACard%20ID%3A%20open-webui-2026-10-25-60999e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->