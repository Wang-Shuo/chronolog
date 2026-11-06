---
card_id: open-webui-2026-09-21-817065
date: '2026-09-21'
description: "Open WebUI · 2026-09-21 · Editor Experience: 21 changes in v0.11.4 —
  \U0001F304 **Model background images.** A workspace model can now carry a background
  image…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1287
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0b7f451b1e273490dcfb8f3868d99ba1e4a101af0c0edbdcd74386b70acc206a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-817065
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 21 Editor Experience changes'
  evidence:
  - quote: "\U0001F304 **Model background images.** A workspace model can now carry
      a background image, uploaded in its editor and drawn behind the chat whenever
      that model is selected, sitting below a folder's own background and above your
      personal one, and it travels with the model through export and import. [Commit](https://github.com/open-webui/open-webui/commit/66addbd6b47bfb25cf9aa37ec70d24db5b28b6b6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5E3️ **Per-language names and descriptions.** A model, tool, skill,
      function, banner or arena entry can now hold its name, description, starter
      prompts and valve labels once per language, written in a searchable table in
      its own editor or brought in as a JSON file, which is refused where a translation
      drops one of the placeholders the original fills in. The interface shows the
      wording for the language it is set to, and falls back to the plain text where
      that language has none. [Commit](https://github.com/open-webui/open-webui/commit/7b6562e3358956ec71eed05352538a646d047734),
      [Commit](https://github.com/open-webui/open-webui/commit/858ab727d2d80bb3c9ef40f01a32de7a12ca75c9),
      [Commit](https://github.com/open-webui/open-webui/commit/3facfa61d413945d7144d26b827fcce1f3aef7c5),
      [Commit](https://github.com/open-webui/open-webui/commit/85b11a4f3504434bd9cd0748629b8a84817fb4f2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F500 **Diffs are drawn as diffs.** A diff or patch block in a reply
      is now laid out as one, with the file and hunk headings, the old and new line
      numbers, and the added and removed lines picked out down to the part of the
      line that changed, and a button to switch to the plain text and back. [Commit](https://github.com/open-webui/open-webui/commit/254e29b9af634145dde0450451a36f0dfbd8f421)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4A1 **Follow-up ghost text.** Once a reply has finished, the first
      of the follow-up questions it suggests now sits greyed inside the empty message
      box as well as under the reply: Tab writes it out, and typing anything of your
      own clears it away. [Commit](https://github.com/open-webui/open-webui/commit/7aaa4a692e949724913834efc47c57572042703b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FA86 **Branch descent guard.** Stepping between reply branches walked
      a chat's children without tracking where it had already been, so a history that
      pointed back at itself spun forever and locked the tab, and a child id with
      no message behind it threw; every one of the eleven places that walk now shares
      a single guarded helper. [#30070](https://github.com/open-webui/open-webui/pull/30070)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F30D **Collaborative link handling.** In a note two people are writing
      at once, a plain web address arriving from the other editor was turned into
      a link on your screen but not on theirs; it is now left as written. [Commit](https://github.com/open-webui/open-webui/commit/d8f27e745bd31c89efa25cbe0f41bb0f70576fc5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F503 **Stale tab reload.** A tab still running the previous build
      met an error page after the server was updated instead of loading the new one,
      because every image built from Docker carried the same version stamp; the stamp
      now follows the build, and a stale tab reloads as it was meant to. [#29832](https://github.com/open-webui/open-webui/pull/29832),
      [#29831](https://github.com/open-webui/open-webui/issues/29831)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F518 **Model editor save button.** Saving a workspace model whose
      model list could not be refreshed afterwards now reports the error and frees
      the Save button, rather than leaving it disabled and spinning though the model
      had been saved. [Commit](https://github.com/open-webui/open-webui/commit/dc98e3023fc6e0113dbad76545cdb15e014db6ad),
      [Commit](https://github.com/open-webui/open-webui/commit/cc5479d16d5caf28ec19a16ffa1ee4f3dbc0f63f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FA82 **Closing the Edit User dialog.** Changes typed into the admin
      Edit User dialog and then abandoned showed on the row in the user list until
      the page was reloaded, and closing the dialog now drops them. [#30193](https://github.com/open-webui/open-webui/pull/30193)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9E4 **Model sharing survives a save.** Saving a model you cannot
      fully share no longer strips the access entries you cannot re-create, where
      an editor resending every stored entry had each one re-checked against what
      its author may grant, and a save from someone with narrow rights quietly took
      the model private for everyone else. [Commit](https://github.com/open-webui/open-webui/commit/754c4b5762ed0d79954ff28c4e06631004dc31b3),
      [#30093](https://github.com/open-webui/open-webui/pull/30093), [#30087](https://github.com/open-webui/open-webui/issues/30087)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4E0 **Prompt version saves.** Saving a new version of a prompt
      without Set as Production leaves the live prompt exactly as it was, where the
      draft quietly took its place, and the editor now shows the production text the
      moment a version is set. [#30231](https://github.com/open-webui/open-webui/pull/30231),
      [#30230](https://github.com/open-webui/open-webui/issues/30230), [#30233](https://github.com/open-webui/open-webui/pull/30233),
      [#30232](https://github.com/open-webui/open-webui/issues/30232)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F58A️ **Channel code blocks.** Where a model answers in a channel
      with structured output, the code inside it was drawn as plain highlighted text
      rather than in the editor every other message uses, so it could not be edited
      in place and a diff in it could not be opened for editing; it now renders the
      same way as everywhere else. [#29861](https://github.com/open-webui/open-webui/pull/29861)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4D0 **Code block edits on collapse.** An unsaved edit inside a
      code block stays on screen when the block is folded away and opened again, where
      collapsing it showed the saved text though the edit was still pending. [#30284](https://github.com/open-webui/open-webui/pull/30284),
      [#30283](https://github.com/open-webui/open-webui/issues/30283)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F201 **IME composition while renaming.** Confirming a chat rename
      with Enter or Escape part way through typing with an input method editor now
      finishes the composition without saving or cancelling the rename, where the
      key press acted at once. [Commit](https://github.com/open-webui/open-webui/commit/85146206f60a22385ed27dae30d4f00e7e2675eb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F392 **Skill settings survive saving.** Saving a skill from its
      editor cleared the tags and translations it carried and switched it back on
      where it had been disabled, and all of that now survives the save. [#30185](https://github.com/open-webui/open-webui/pull/30185)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ⏱️ **Stopped reply state.** Pressing stop saved the reply as finished while
      the parts inside it were still marked as running, so a block went on reading
      "Thinking..." or "Executing..." and came back that way after every reload; those
      parts are now closed off as the reply is stopped, and an open tab settles at
      once rather than only after a reload, while a tool call still waiting for your
      approval keeps its prompt. [#29495](https://github.com/open-webui/open-webui/pull/29495),
      [#29281](https://github.com/open-webui/open-webui/issues/29281)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5DD️ **Read-only folders read-only everywhere.** A folder shared
      with you as a viewer no longer shows its edit controls on the empty-chat page,
      where they appeared and a save went through or failed depending on rights the
      page never checked. [Commit](https://github.com/open-webui/open-webui/commit/ee3ece1e2b8c9a38c94faf354ca020d66aba801d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ✍️ **Continued reply text.** Asking for the rest of a cut-off reply in
      a temporary chat replaced what was on screen with only the new text, because
      the message being continued was read back from the saved chat it did not have.
      It is now taken from the request before the model is called, the continuation
      joins the same message instead of arriving as a second one, on a connection
      whose provider is set to llama.cpp the model is told to carry on from the text
      it is handed rather than repeat it back, opening the result in the message editor
      no longer shows a line break where the two halves meet, and, where haptic feedback
      is switched on, a continuation buzzes as it streams like any other reply. [Commit](https://github.com/open-webui/open-webui/commit/77d2000eb79e1cb6ae2004d40e8cca8c9e754cd0),
      [Commit](https://github.com/open-webui/open-webui/commit/6c7aa3543d21442241f6c53add5ff623ec816c44),
      [Commit](https://github.com/open-webui/open-webui/commit/57fc344873edc0db9e9f7ff3e9fb167cd80e3ef2),
      [Commit](https://github.com/open-webui/open-webui/commit/7eefeef4f17118f81c87acb464ad562803a6f26c),
      [Commit](https://github.com/open-webui/open-webui/commit/d418840aa9c4b77f613308cdaa4f2c6a062a8715),
      [Commit](https://github.com/open-webui/open-webui/commit/3795d5b29253d4b8d7a0adbab457c7317c40f3c6),
      [Commit](https://github.com/open-webui/open-webui/commit/57acc2b68f2f9e40b53aa7e609fdd52a4b0d15c4)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F517 **Cancelled edits keep attachments.** Cancelling the edit of
      a message no longer strips the files attached to it, where dropping the edit
      took the attachments down with it. [#30281](https://github.com/open-webui/open-webui/pull/30281),
      [#30192](https://github.com/open-webui/open-webui/issues/30192)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5BC **Playground image edits.** Editing an image in the Images
      playground now works, where every attempt came back rejected since the request
      carried its fields under a heading the endpoint never read. [Commit](https://github.com/open-webui/open-webui/commit/c07fa08b995e8d1a1fc2d94a88d8cea691bdc5ee)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F194 **Model ID whitespace.** A workspace model whose ID contains
      a space or a tab is now refused in the editor, through the API and on import;
      one already stored goes on answering but cannot be saved again until it is recreated.
      [Commit](https://github.com/open-webui/open-webui/commit/8a19e2f867063256bb2836649e2fe80af41ef748)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 21-editor-experience-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: editor-experience
  title: 21 Editor Experience changes in v0.11.4
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-09-17-2-editor-experience-changes-in-v1-0-86|2
  Editor Experience changes in v1.0.86]]'
- '[[Changes/Claude Code/2026-09-18-2-editor-experience-changes-in-v2-1-277|2 Editor
  Experience changes in v2.1.277]]'
- '[[Changes/Lovable/2026-09-20-organize-project-files-into-collections|Organize project
  files into collections]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: editor-experience
title: 21 Editor Experience changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 21 Editor Experience changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🌄 **Model background images.** A workspace model can now carry a background image, uploaded in its editor and drawn behind the chat whenever that model is selected, sitting below a folder's own background and above your personal one, and it travels with the model through export and import. [Commit](https://github.com/open-webui/open-webui/commit/66addbd6b47bfb25cf9aa37ec70d24db5b28b6b6)

> 🗣️ **Per-language names and descriptions.** A model, tool, skill, function, banner or arena entry can now hold its name, description, starter prompts and valve labels once per language, written in a searchable table in its own editor or brought in as a JSON file, which is refused where a translation drops one of the placeholders the original fills in. The interface shows the wording for the language it is set to, and falls back to the plain text where that language has none. [Commit](https://github.com/open-webui/open-webui/commit/7b6562e3358956ec71eed05352538a646d047734), [Commit](https://github.com/open-webui/open-webui/commit/858ab727d2d80bb3c9ef40f01a32de7a12ca75c9), [Commit](https://github.com/open-webui/open-webui/commit/3facfa61d413945d7144d26b827fcce1f3aef7c5), [Commit](https://github.com/open-webui/open-webui/commit/85b11a4f3504434bd9cd0748629b8a84817fb4f2)

> 🔀 **Diffs are drawn as diffs.** A diff or patch block in a reply is now laid out as one, with the file and hunk headings, the old and new line numbers, and the added and removed lines picked out down to the part of the line that changed, and a button to switch to the plain text and back. [Commit](https://github.com/open-webui/open-webui/commit/254e29b9af634145dde0450451a36f0dfbd8f421)

> 💡 **Follow-up ghost text.** Once a reply has finished, the first of the follow-up questions it suggests now sits greyed inside the empty message box as well as under the reply: Tab writes it out, and typing anything of your own clears it away. [Commit](https://github.com/open-webui/open-webui/commit/7aaa4a692e949724913834efc47c57572042703b)

> 🪆 **Branch descent guard.** Stepping between reply branches walked a chat's children without tracking where it had already been, so a history that pointed back at itself spun forever and locked the tab, and a child id with no message behind it threw; every one of the eleven places that walk now shares a single guarded helper. [#30070](https://github.com/open-webui/open-webui/pull/30070)

> 🌍 **Collaborative link handling.** In a note two people are writing at once, a plain web address arriving from the other editor was turned into a link on your screen but not on theirs; it is now left as written. [Commit](https://github.com/open-webui/open-webui/commit/d8f27e745bd31c89efa25cbe0f41bb0f70576fc5)

> 🔃 **Stale tab reload.** A tab still running the previous build met an error page after the server was updated instead of loading the new one, because every image built from Docker carried the same version stamp; the stamp now follows the build, and a stale tab reloads as it was meant to. [#29832](https://github.com/open-webui/open-webui/pull/29832), [#29831](https://github.com/open-webui/open-webui/issues/29831)

> 🔘 **Model editor save button.** Saving a workspace model whose model list could not be refreshed afterwards now reports the error and frees the Save button, rather than leaving it disabled and spinning though the model had been saved. [Commit](https://github.com/open-webui/open-webui/commit/dc98e3023fc6e0113dbad76545cdb15e014db6ad), [Commit](https://github.com/open-webui/open-webui/commit/cc5479d16d5caf28ec19a16ffa1ee4f3dbc0f63f)

> 🪂 **Closing the Edit User dialog.** Changes typed into the admin Edit User dialog and then abandoned showed on the row in the user list until the page was reloaded, and closing the dialog now drops them. [#30193](https://github.com/open-webui/open-webui/pull/30193)

> 🧤 **Model sharing survives a save.** Saving a model you cannot fully share no longer strips the access entries you cannot re-create, where an editor resending every stored entry had each one re-checked against what its author may grant, and a save from someone with narrow rights quietly took the model private for everyone else. [Commit](https://github.com/open-webui/open-webui/commit/754c4b5762ed0d79954ff28c4e06631004dc31b3), [#30093](https://github.com/open-webui/open-webui/pull/30093), [#30087](https://github.com/open-webui/open-webui/issues/30087)

> 📠 **Prompt version saves.** Saving a new version of a prompt without Set as Production leaves the live prompt exactly as it was, where the draft quietly took its place, and the editor now shows the production text the moment a version is set. [#30231](https://github.com/open-webui/open-webui/pull/30231), [#30230](https://github.com/open-webui/open-webui/issues/30230), [#30233](https://github.com/open-webui/open-webui/pull/30233), [#30232](https://github.com/open-webui/open-webui/issues/30232)

> 🖊️ **Channel code blocks.** Where a model answers in a channel with structured output, the code inside it was drawn as plain highlighted text rather than in the editor every other message uses, so it could not be edited in place and a diff in it could not be opened for editing; it now renders the same way as everywhere else. [#29861](https://github.com/open-webui/open-webui/pull/29861)

> 📐 **Code block edits on collapse.** An unsaved edit inside a code block stays on screen when the block is folded away and opened again, where collapsing it showed the saved text though the edit was still pending. [#30284](https://github.com/open-webui/open-webui/pull/30284), [#30283](https://github.com/open-webui/open-webui/issues/30283)

> 🈁 **IME composition while renaming.** Confirming a chat rename with Enter or Escape part way through typing with an input method editor now finishes the composition without saving or cancelling the rename, where the key press acted at once. [Commit](https://github.com/open-webui/open-webui/commit/85146206f60a22385ed27dae30d4f00e7e2675eb)

> 🎒 **Skill settings survive saving.** Saving a skill from its editor cleared the tags and translations it carried and switched it back on where it had been disabled, and all of that now survives the save. [#30185](https://github.com/open-webui/open-webui/pull/30185)

> ⏱️ **Stopped reply state.** Pressing stop saved the reply as finished while the parts inside it were still marked as running, so a block went on reading "Thinking..." or "Executing..." and came back that way after every reload; those parts are now closed off as the reply is stopped, and an open tab settles at once rather than only after a reload, while a tool call still waiting for your approval keeps its prompt. [#29495](https://github.com/open-webui/open-webui/pull/29495), [#29281](https://github.com/open-webui/open-webui/issues/29281)

> 🗝️ **Read-only folders read-only everywhere.** A folder shared with you as a viewer no longer shows its edit controls on the empty-chat page, where they appeared and a save went through or failed depending on rights the page never checked. [Commit](https://github.com/open-webui/open-webui/commit/ee3ece1e2b8c9a38c94faf354ca020d66aba801d)

> ✍️ **Continued reply text.** Asking for the rest of a cut-off reply in a temporary chat replaced what was on screen with only the new text, because the message being continued was read back from the saved chat it did not have. It is now taken from the request before the model is called, the continuation joins the same message instead of arriving as a second one, on a connection whose provider is set to llama.cpp the model is told to carry on from the text it is handed rather than repeat it back, opening the result in the message editor no longer shows a line break where the two halves meet, and, where haptic feedback is switched on, a continuation buzzes as it streams like any other reply. [Commit](https://github.com/open-webui/open-webui/commit/77d2000eb79e1cb6ae2004d40e8cca8c9e754cd0), [Commit](https://github.com/open-webui/open-webui/commit/6c7aa3543d21442241f6c53add5ff623ec816c44), [Commit](https://github.com/open-webui/open-webui/commit/57fc344873edc0db9e9f7ff3e9fb167cd80e3ef2), [Commit](https://github.com/open-webui/open-webui/commit/7eefeef4f17118f81c87acb464ad562803a6f26c), [Commit](https://github.com/open-webui/open-webui/commit/d418840aa9c4b77f613308cdaa4f2c6a062a8715), [Commit](https://github.com/open-webui/open-webui/commit/3795d5b29253d4b8d7a0adbab457c7317c40f3c6), [Commit](https://github.com/open-webui/open-webui/commit/57acc2b68f2f9e40b53aa7e609fdd52a4b0d15c4)

> 🔗 **Cancelled edits keep attachments.** Cancelling the edit of a message no longer strips the files attached to it, where dropping the edit took the attachments down with it. [#30281](https://github.com/open-webui/open-webui/pull/30281), [#30192](https://github.com/open-webui/open-webui/issues/30192)

> 🖼 **Playground image edits.** Editing an image in the Images playground now works, where every attempt came back rejected since the request carried its fields under a heading the endpoint never read. [Commit](https://github.com/open-webui/open-webui/commit/c07fa08b995e8d1a1fc2d94a88d8cea691bdc5ee)

> 🆔 **Model ID whitespace.** A workspace model whose ID contains a space or a tab is now refused in the editor, through the API and on import; one already stored goes on answering but cannot be saved again until it is recreated. [Commit](https://github.com/open-webui/open-webui/commit/8a19e2f867063256bb2836649e2fe80af41ef748)

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
## Nearby in Editor Experience

- Earlier: 2026-09-20 · Lovable · [[Changes/Lovable/2026-09-20-organize-project-files-into-collections|Organize project files into collections]]
- Later: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-vscode-changed-open-in-new-tab-to-open-claude-beside-the-editor-group-you-are-wo|VSCode Changed "Open in New Tab" to open Claude beside the editor group you…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-817065&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-21-editor-experience-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-817065%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->