---
card_id: open-webui-2026-10-10-b35758
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Editor Experience: 21 changes in v0.12.0 —
  \U0001F9F3 **Multi-file skills with version history.** Workspace skills can now
  hold supporting…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1306
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5f9835fd847291ed49a245d8c37edd181cad670399ab7f5bd3828b23d63d3766
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-b35758
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 21 Editor Experience changes'
  evidence:
  - quote: "\U0001F9F3 **Multi-file skills with version history.** Workspace skills
      can now hold supporting files such as scripts, references and templates next
      to SKILL.md, managed in a file tree in the skill editor, and every save keeps
      a version you can page through, compare with the current one, make the live
      version again or delete. Skills import from a ZIP folder, a JSON file or a single
      SKILL.md with a preview first, and export as ZIP or JSON. Models can read a
      skill's supporting files and create skills or edit their files on their own,
      so for anyone allowed to create workspace skills \"/skills:create\" now saves
      the new skill straight to the workspace without needing a terminal. [Commit](https://github.com/open-webui/open-webui/commit/9bbb95048b841d5f6a1fedf606ae93ec28969521),
      [Commit](https://github.com/open-webui/open-webui/commit/178de36662909b072864733aad5e074f2bb5d01e),
      [Commit](https://github.com/open-webui/open-webui/commit/24ee1cb168a1b2071195c0331aa186a1d62bc197)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ⏮️ **Model version history.** Every save of a workspace model now keeps
      a version you can page through in the model editor, make the live version again
      or delete, and a version whose knowledge, tools, functions or terminal are gone
      or no longer yours to use is refused instead of being switched on half working.
      [Commit](https://github.com/open-webui/open-webui/commit/16849284ffbf7a7cd5deac179799ce4d5716848b),
      [Commit](https://github.com/open-webui/open-webui/commit/27b48b70df2e01af0db4d4668ea3aa29d9f4cd6f)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F519 **Tool and function version history.** Every save of a tool
      or function now keeps a version you can page through in its editor, make the
      live version again or delete, so a change can be tried and rolled back without
      creating a copy and setting it up again. [#29496](https://github.com/open-webui/open-webui/issues/29496),
      [Commit](https://github.com/open-webui/open-webui/commit/e6476928eeb02def4a0cfc3ed1eb57b1a3630ae3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F19A **Compare prompt versions.** The prompt editor's history now
      compares any earlier version with the current one in a diff view and can start
      editing from an old version as a new one, and asks before unsaved changes are
      dropped. [Commit](https://github.com/open-webui/open-webui/commit/37138282fbd21bdff642723ad0b6f054b2241a19),
      [Commit](https://github.com/open-webui/open-webui/commit/33dd7dd224d4fc4031185a4dd589242681f24af7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F333 **Nested groups.** Administrators can now give a group a parent
      group, so members of the inner group also get everything shared with the parent
      groups above it and their permissions, the group editor shows the inherited
      permissions and lists direct and inherited members separately, deleting a group
      moves its subgroups up to its parent, and open browsers pick up changed group
      access right away without reloading. [Commit](https://github.com/open-webui/open-webui/commit/d4c561d9f22b6fe069c1a4e49f83d05fa6839991)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6CD️ **Skills on the community site.** With Community Sharing on,
      the Skills workspace now has a Discover a skill link to the skills on openwebui.com,
      the skill menu has Share for people allowed to export skills, which sends the
      skill with all its files to openwebui.com, and a skill opened from openwebui.com
      loads straight into the new skill editor for people allowed to import skills.
      [Commit](https://github.com/open-webui/open-webui/commit/a3cd6158bb188837dcbfbc11ade56d1a1f748db2),
      [Commit](https://github.com/open-webui/open-webui/commit/e86c82406da3438e269955221f78757132e30727)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4C4 **Copy button in the model JSON Preview.** The JSON Preview
      in the model editor now has a Copy button that copies the model's JSON to the
      clipboard exactly as the preview shows it, including edits that have not been
      saved yet. [Commit](https://github.com/open-webui/open-webui/commit/fe2c694915bf7915f7555620dd4bdd8c7f3c5f41),
      [Commit](https://github.com/open-webui/open-webui/commit/106aae70e9ad1a3356762779d72673b7dc1293a7),
      [#31955](https://github.com/open-webui/open-webui/issues/31955)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6AA **Sign out all devices for a user.** Administrators can now
      sign a user out of every device from the user edit dialog, while the user's
      API keys keep working. [Commit](https://github.com/open-webui/open-webui/commit/24e30d1cbdaab624dfe20f479f805e6791cf0226)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3F7️ **Workspace model list links.** In the workspace model list,
      clicking a model's name now opens its editor and a small arrow next to it opens
      the model in a new chat, the enable switch goes back if saving fails, and deleting
      with Shift held now asks for confirmation. [Commit](https://github.com/open-webui/open-webui/commit/5bb1c470802c7df9a48cc0ca45c1886c294d6e6e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6B7 **Revoked access ends live updates.** Removing someone's access
      to a shared channel or a note, or deleting it, now also stops the live messages
      and edits their open sessions were still receiving from it. [Commit](https://github.com/open-webui/open-webui/commit/e93a59f4dd8eea5b1df55b4e6dcc57465887b95d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ✏️ **Shared knowledge file edits.** Users with write access to a shared
      knowledge base can now save edits to its files, where the editor reported success
      but the old content stayed in place. [#30448](https://github.com/open-webui/open-webui/pull/30448),
      [#30319](https://github.com/open-webui/open-webui/issues/30319)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F40D **Code mentioning matplotlib.** Python code that only mentions
      matplotlib in a comment, a string or an availability check now runs, and the
      code editor's Python formatter works on code that imports it. [#30381](https://github.com/open-webui/open-webui/pull/30381),
      [#29894](https://github.com/open-webui/open-webui/issues/29894)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5BC️ **ComfyUI Save Image (Advanced).** Images from ComfyUI workflows
      that end in the \"Save Image (Advanced)\" node, such as the Qwen Image Edit
      template, now appear in the chat for both generation and editing. [#30420](https://github.com/open-webui/open-webui/pull/30420),
      [#30404](https://github.com/open-webui/open-webui/issues/30404)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6AB **Read-only prompt controls.** Prompts you can only read now
      show their edit, share, delete and enable controls in the workspace as unavailable,
      where they looked usable but could not be changed. [Commit](https://github.com/open-webui/open-webui/commit/ff89756b6dcafc129d29dea3c4a7c0f93ebc0895),
      [#30219](https://github.com/open-webui/open-webui/issues/30219)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6F0️ **Tool prompts across instances.** With \"WEBSOCKET_MANAGER\"
      set to redis and several instances or workers, a confirmation or input dialog
      from a tool or Function now receives the user's answer whichever instance the
      browser tab is connected to, where the tool waited until it timed out. [#31620](https://github.com/open-webui/open-webui/pull/31620)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FA9B **List valves in Chat Controls.** List user valves in Chat
      Controls now keep their default when unset and save edits as a list, where saving
      any other valve replaced the list with an empty entry and every later edit failed
      silently. [#31300](https://github.com/open-webui/open-webui/pull/31300), [#31299](https://github.com/open-webui/open-webui/issues/31299)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F453 **Model JSON Preview shows unsaved changes.** The JSON Preview
      in the model editor now updates as you edit the name, system prompt, advanced
      parameters, capabilities, tools and other settings, showing exactly what will
      be saved, where most changes only appeared after saving and reopening the model.
      [#31851](https://github.com/open-webui/open-webui/pull/31851), [#31848](https://github.com/open-webui/open-webui/issues/31848)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4D3 **Large pastes into notes are saved.** Pasting a large block
      of text, around 150 KB or more, into a note no longer drops the note's live
      connection and loses the text on reload, as the server now accepts edit messages
      up to 16 MiB, so notes with up to about 2 MB of text save again. [#31893](https://github.com/open-webui/open-webui/pull/31893),
      [#26140](https://github.com/open-webui/open-webui/issues/26140)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9CA **Pasting large text no longer freezes the browser.** Text
      boxes using the rich text editor, such as the chat input and the knowledge text
      editor, now only convert their content when it actually changes, where every
      cursor move or selection converted the whole text again and pasting a large
      amount could freeze the page. [Commit](https://github.com/open-webui/open-webui/commit/286926d2993603738084c3c55e44028f53bd5c7c),
      [#12087](https://github.com/open-webui/open-webui/issues/12087)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6A8 **Knowledge text edits that did not index.** Saving the edited
      text of a knowledge file now shows an error when the text could not be processed
      or a knowledge base using the file could not be updated, where the editor reported
      success while searches kept the old text. [Commit](https://github.com/open-webui/open-webui/commit/33dd7dd224d4fc4031185a4dd589242681f24af7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4DC **Skill details read from SKILL.md.** The skill editor now
      reads a skill's name and description from its SKILL.md header as proper YAML,
      so quoted values, values containing a colon and descriptions spread over several
      lines fill in correctly, where they came out cut off or with stray quotes. [Commit](https://github.com/open-webui/open-webui/commit/dc1203d34c93ed7a73d6f8e19e0c1f5ab312b22c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 21-editor-experience-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: editor-experience
  title: 21 Editor Experience changes in v0.12.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-08-50216-use-the-shared-text-editor-for-command-center-task-renaming-bc-openai|♯50216
  Use the shared text editor for command-center task renaming @bc-openai]]'
- '[[Changes/Midjourney/2026-10-08-thinking-mode|THINKING MODE]]'
- '[[Changes/Claude Code/2026-10-09-3-editor-experience-changes-in-v2-1-296|3 Editor
  Experience changes in v2.1.296]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: editor-experience
title: 21 Editor Experience changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 21 Editor Experience changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧳 **Multi-file skills with version history.** Workspace skills can now hold supporting files such as scripts, references and templates next to SKILL.md, managed in a file tree in the skill editor, and every save keeps a version you can page through, compare with the current one, make the live version again or delete. Skills import from a ZIP folder, a JSON file or a single SKILL.md with a preview first, and export as ZIP or JSON. Models can read a skill's supporting files and create skills or edit their files on their own, so for anyone allowed to create workspace skills "/skills:create" now saves the new skill straight to the workspace without needing a terminal. [Commit](https://github.com/open-webui/open-webui/commit/9bbb95048b841d5f6a1fedf606ae93ec28969521), [Commit](https://github.com/open-webui/open-webui/commit/178de36662909b072864733aad5e074f2bb5d01e), [Commit](https://github.com/open-webui/open-webui/commit/24ee1cb168a1b2071195c0331aa186a1d62bc197)

> ⏮️ **Model version history.** Every save of a workspace model now keeps a version you can page through in the model editor, make the live version again or delete, and a version whose knowledge, tools, functions or terminal are gone or no longer yours to use is refused instead of being switched on half working. [Commit](https://github.com/open-webui/open-webui/commit/16849284ffbf7a7cd5deac179799ce4d5716848b), [Commit](https://github.com/open-webui/open-webui/commit/27b48b70df2e01af0db4d4668ea3aa29d9f4cd6f)

> 🔙 **Tool and function version history.** Every save of a tool or function now keeps a version you can page through in its editor, make the live version again or delete, so a change can be tried and rolled back without creating a copy and setting it up again. [#29496](https://github.com/open-webui/open-webui/issues/29496), [Commit](https://github.com/open-webui/open-webui/commit/e6476928eeb02def4a0cfc3ed1eb57b1a3630ae3)

> 🆚 **Compare prompt versions.** The prompt editor's history now compares any earlier version with the current one in a diff view and can start editing from an old version as a new one, and asks before unsaved changes are dropped. [Commit](https://github.com/open-webui/open-webui/commit/37138282fbd21bdff642723ad0b6f054b2241a19), [Commit](https://github.com/open-webui/open-webui/commit/33dd7dd224d4fc4031185a4dd589242681f24af7)

> 🌳 **Nested groups.** Administrators can now give a group a parent group, so members of the inner group also get everything shared with the parent groups above it and their permissions, the group editor shows the inherited permissions and lists direct and inherited members separately, deleting a group moves its subgroups up to its parent, and open browsers pick up changed group access right away without reloading. [Commit](https://github.com/open-webui/open-webui/commit/d4c561d9f22b6fe069c1a4e49f83d05fa6839991)

> 🛍️ **Skills on the community site.** With Community Sharing on, the Skills workspace now has a Discover a skill link to the skills on openwebui.com, the skill menu has Share for people allowed to export skills, which sends the skill with all its files to openwebui.com, and a skill opened from openwebui.com loads straight into the new skill editor for people allowed to import skills. [Commit](https://github.com/open-webui/open-webui/commit/a3cd6158bb188837dcbfbc11ade56d1a1f748db2), [Commit](https://github.com/open-webui/open-webui/commit/e86c82406da3438e269955221f78757132e30727)

> 📄 **Copy button in the model JSON Preview.** The JSON Preview in the model editor now has a Copy button that copies the model's JSON to the clipboard exactly as the preview shows it, including edits that have not been saved yet. [Commit](https://github.com/open-webui/open-webui/commit/fe2c694915bf7915f7555620dd4bdd8c7f3c5f41), [Commit](https://github.com/open-webui/open-webui/commit/106aae70e9ad1a3356762779d72673b7dc1293a7), [#31955](https://github.com/open-webui/open-webui/issues/31955)

> 🚪 **Sign out all devices for a user.** Administrators can now sign a user out of every device from the user edit dialog, while the user's API keys keep working. [Commit](https://github.com/open-webui/open-webui/commit/24e30d1cbdaab624dfe20f479f805e6791cf0226)

> 🏷️ **Workspace model list links.** In the workspace model list, clicking a model's name now opens its editor and a small arrow next to it opens the model in a new chat, the enable switch goes back if saving fails, and deleting with Shift held now asks for confirmation. [Commit](https://github.com/open-webui/open-webui/commit/5bb1c470802c7df9a48cc0ca45c1886c294d6e6e)

> 🚷 **Revoked access ends live updates.** Removing someone's access to a shared channel or a note, or deleting it, now also stops the live messages and edits their open sessions were still receiving from it. [Commit](https://github.com/open-webui/open-webui/commit/e93a59f4dd8eea5b1df55b4e6dcc57465887b95d)

> ✏️ **Shared knowledge file edits.** Users with write access to a shared knowledge base can now save edits to its files, where the editor reported success but the old content stayed in place. [#30448](https://github.com/open-webui/open-webui/pull/30448), [#30319](https://github.com/open-webui/open-webui/issues/30319)

> 🐍 **Code mentioning matplotlib.** Python code that only mentions matplotlib in a comment, a string or an availability check now runs, and the code editor's Python formatter works on code that imports it. [#30381](https://github.com/open-webui/open-webui/pull/30381), [#29894](https://github.com/open-webui/open-webui/issues/29894)

> 🖼️ **ComfyUI Save Image (Advanced).** Images from ComfyUI workflows that end in the "Save Image (Advanced)" node, such as the Qwen Image Edit template, now appear in the chat for both generation and editing. [#30420](https://github.com/open-webui/open-webui/pull/30420), [#30404](https://github.com/open-webui/open-webui/issues/30404)

> 🚫 **Read-only prompt controls.** Prompts you can only read now show their edit, share, delete and enable controls in the workspace as unavailable, where they looked usable but could not be changed. [Commit](https://github.com/open-webui/open-webui/commit/ff89756b6dcafc129d29dea3c4a7c0f93ebc0895), [#30219](https://github.com/open-webui/open-webui/issues/30219)

> 🛰️ **Tool prompts across instances.** With "WEBSOCKET_MANAGER" set to redis and several instances or workers, a confirmation or input dialog from a tool or Function now receives the user's answer whichever instance the browser tab is connected to, where the tool waited until it timed out. [#31620](https://github.com/open-webui/open-webui/pull/31620)

> 🪛 **List valves in Chat Controls.** List user valves in Chat Controls now keep their default when unset and save edits as a list, where saving any other valve replaced the list with an empty entry and every later edit failed silently. [#31300](https://github.com/open-webui/open-webui/pull/31300), [#31299](https://github.com/open-webui/open-webui/issues/31299)

> 👓 **Model JSON Preview shows unsaved changes.** The JSON Preview in the model editor now updates as you edit the name, system prompt, advanced parameters, capabilities, tools and other settings, showing exactly what will be saved, where most changes only appeared after saving and reopening the model. [#31851](https://github.com/open-webui/open-webui/pull/31851), [#31848](https://github.com/open-webui/open-webui/issues/31848)

> 📓 **Large pastes into notes are saved.** Pasting a large block of text, around 150 KB or more, into a note no longer drops the note's live connection and loses the text on reload, as the server now accepts edit messages up to 16 MiB, so notes with up to about 2 MB of text save again. [#31893](https://github.com/open-webui/open-webui/pull/31893), [#26140](https://github.com/open-webui/open-webui/issues/26140)

> 🧊 **Pasting large text no longer freezes the browser.** Text boxes using the rich text editor, such as the chat input and the knowledge text editor, now only convert their content when it actually changes, where every cursor move or selection converted the whole text again and pasting a large amount could freeze the page. [Commit](https://github.com/open-webui/open-webui/commit/286926d2993603738084c3c55e44028f53bd5c7c), [#12087](https://github.com/open-webui/open-webui/issues/12087)

> 🚨 **Knowledge text edits that did not index.** Saving the edited text of a knowledge file now shows an error when the text could not be processed or a knowledge base using the file could not be updated, where the editor reported success while searches kept the old text. [Commit](https://github.com/open-webui/open-webui/commit/33dd7dd224d4fc4031185a4dd589242681f24af7)

> 📜 **Skill details read from SKILL.md.** The skill editor now reads a skill's name and description from its SKILL.md header as proper YAML, so quoted values, values containing a colon and descriptions spread over several lines fill in correctly, where they came out cut off or with stray quotes. [Commit](https://github.com/open-webui/open-webui/commit/dc1203d34c93ed7a73d6f8e19e0c1f5ab312b22c)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-reliability-and-performance-changes-in-v0-12-0|5 Reliability and Performance changes in v0.12.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5 Enterprise and Administration changes in v0.12.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-10-27-developer-workflow-changes-in-v0-12-0|27 Developer Workflow changes in v0.12.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-10-5-image-generation-changes-in-v0-12-0|5 Image Generation changes in v0.12.0]] · Image Generation
- [[Changes/Open WebUI/2026-10-10-49-model-support-changes-in-v0-12-0|49 Model Support changes in v0.12.0]] · Model Support
- [[Changes/Open WebUI/2026-10-10-19-account-and-access-changes-in-v0-12-0|19 Account and Access changes in v0.12.0]] · Account and Access
- [[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10 Automation and Scheduling changes in v0.12.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile and Desktop changes in v0.12.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-10-10-6-files-and-data-changes-in-v0-12-0|6 Files and Data changes in v0.12.0]] · Files and Data
- [[Changes/Open WebUI/2026-10-10-13-collaboration-changes-in-v0-12-0|13 Collaboration changes in v0.12.0]] · Collaboration
- [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-10-5-context-window-changes-in-v0-12-0|5 Context Window changes in v0.12.0]] · Context Window
- [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]] · Interface Experience
- [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Agent Mode
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-10-09 · Claude Code · [[Changes/Claude Code/2026-10-09-3-editor-experience-changes-in-v2-1-296|3 Editor Experience changes in v2.1.296]]
- Later: 2026-10-10 · OpenClaw · [[Changes/OpenClaw/2026-10-10-10-editor-experience-changes-in-v2026-10-1|10 Editor Experience changes in v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-b35758&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-21-editor-experience-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-b35758%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->