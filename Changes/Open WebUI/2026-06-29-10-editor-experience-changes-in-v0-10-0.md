---
card_id: open-webui-2026-06-29-dec77c
date: '2026-06-29'
description: 'Open WebUI · 2026-06-29 · Editor Experience: 10 changes in v0.10.0 —
  ✍️ **Customizable autocomplete prompt.** Administrators can now set a custom prompt…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1203
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4fce77b209261c75648ae6769c75d84453895c7ce3c153d418f74f664c9e8279
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-dec77c
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 10 Editor Experience changes'
  evidence:
  - quote: ✍️ **Customizable autocomplete prompt.** Administrators can now set a custom
      prompt template for autocomplete generation from the admin interface settings.
      [Commit](https://github.com/open-webui/open-webui/commit/4dbb2f94a66d6e0035e2da857ddb6a841a68f862),
      [#25879](https://github.com/open-webui/open-webui/pull/25879)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ✏️ **Edit prompts from the menu.** The prompts list now has an Edit option
      in each prompt's menu, taking you straight to its editor. [#25789](https://github.com/open-webui/open-webui/pull/25789)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F501 **Recurring calendar events.** The calendar event editor now
      includes a repeat option, so events can recur on a schedule. [#25865](https://github.com/open-webui/open-webui/pull/25865)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F3F7️ **Tag suggestions in the model editor.** The model editor
      now suggests existing tags as you type, making it easier to reuse a consistent
      set. [Commit](https://github.com/open-webui/open-webui/commit/b58b0ea7ca849b89d217e1077498a8a3fc92471f),
      [#25703](https://github.com/open-webui/open-webui/pull/25703)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F50D **Searchable pickers in the model editor.** Attaching actions,
      filters, tools, knowledge, and skills to a model now uses type-to-search pickers
      instead of long checkbox lists, making large libraries easier to manage. [Commit](https://github.com/open-webui/open-webui/commit/61cee42ded4e84e31d7cc9b168994ef165efa8ca)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001FA9F **Default Permissions modal resets on close.** Closing the
      Default Permissions dialog without saving now discards unsaved edits instead
      of keeping them around the next time you open it. [Commit](https://github.com/open-webui/open-webui/commit/78a5015846a9e55ff2bc9d6cc98f880437abe8ed)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F233 **Search no longer fires mid-composition.** Typing in search
      with an input method editor (such as Japanese, Chinese, or Korean) no longer
      triggers a search when you press Enter to confirm a composition. [#26238](https://github.com/open-webui/open-webui/pull/26238),
      [#26285](https://github.com/open-webui/open-webui/pull/26285), [#26172](https://github.com/open-webui/open-webui/issues/26172)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4DD **Note file attachments stay in sync.** Updating the files
      attached to a note now keeps the editor and saved note in sync. [Commit](https://github.com/open-webui/open-webui/commit/5055fb85aa8c8d5ef785daea7438498e36ddf33f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F527 **Background completion no longer clears active tasks.** Finishing
      a chat in the background no longer wipes the set of active tasks, fixing a case
      where ongoing task indicators could be lost. [Commit](https://github.com/open-webui/open-webui/commit/388f62f8a002b789887d016892a1bf152c9d90af),
      [#25217](https://github.com/open-webui/open-webui/issues/25217)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4DD **Code editor stays open when empty.** The code editor drawer
      no longer collapses when its content is empty. [#25855](https://github.com/open-webui/open-webui/pull/25855)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 10-editor-experience-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: editor-experience
  title: 10 Editor Experience changes in v0.10.0
  type: change
related_changes:
- '[[Changes/Dify/2026-06-25-3-editor-experience-changes-in-1-15-0|3 Editor Experience
  changes in 1.15.0]]'
- '[[Changes/Cline/2026-06-26-add-edit-and-regenerate-support-for-previous-user-messages-with-clearer-reset-ch|Add
  edit-and-regenerate support for previous user messages, with clearer Reset Chat…]]'
- '[[Changes/v0/2026-06-26-the-editor-no-longer-shows-a-false-start-error-when-a-preview-dev-server-or-inst|The
  editor no longer shows a false start error when a preview, dev server…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: editor-experience
title: 10 Editor Experience changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Editor Experience changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ✍️ **Customizable autocomplete prompt.** Administrators can now set a custom prompt template for autocomplete generation from the admin interface settings. [Commit](https://github.com/open-webui/open-webui/commit/4dbb2f94a66d6e0035e2da857ddb6a841a68f862), [#25879](https://github.com/open-webui/open-webui/pull/25879)

> ✏️ **Edit prompts from the menu.** The prompts list now has an Edit option in each prompt's menu, taking you straight to its editor. [#25789](https://github.com/open-webui/open-webui/pull/25789)

> 🔁 **Recurring calendar events.** The calendar event editor now includes a repeat option, so events can recur on a schedule. [#25865](https://github.com/open-webui/open-webui/pull/25865)

> 🏷️ **Tag suggestions in the model editor.** The model editor now suggests existing tags as you type, making it easier to reuse a consistent set. [Commit](https://github.com/open-webui/open-webui/commit/b58b0ea7ca849b89d217e1077498a8a3fc92471f), [#25703](https://github.com/open-webui/open-webui/pull/25703)

> 🔍 **Searchable pickers in the model editor.** Attaching actions, filters, tools, knowledge, and skills to a model now uses type-to-search pickers instead of long checkbox lists, making large libraries easier to manage. [Commit](https://github.com/open-webui/open-webui/commit/61cee42ded4e84e31d7cc9b168994ef165efa8ca)

> 🪟 **Default Permissions modal resets on close.** Closing the Default Permissions dialog without saving now discards unsaved edits instead of keeping them around the next time you open it. [Commit](https://github.com/open-webui/open-webui/commit/78a5015846a9e55ff2bc9d6cc98f880437abe8ed)

> 🈳 **Search no longer fires mid-composition.** Typing in search with an input method editor (such as Japanese, Chinese, or Korean) no longer triggers a search when you press Enter to confirm a composition. [#26238](https://github.com/open-webui/open-webui/pull/26238), [#26285](https://github.com/open-webui/open-webui/pull/26285), [#26172](https://github.com/open-webui/open-webui/issues/26172)

> 📝 **Note file attachments stay in sync.** Updating the files attached to a note now keeps the editor and saved note in sync. [Commit](https://github.com/open-webui/open-webui/commit/5055fb85aa8c8d5ef785daea7438498e36ddf33f)

> 🔧 **Background completion no longer clears active tasks.** Finishing a chat in the background no longer wipes the set of active tasks, fixing a case where ongoing task indicators could be lost. [Commit](https://github.com/open-webui/open-webui/commit/388f62f8a002b789887d016892a1bf152c9d90af), [#25217](https://github.com/open-webui/open-webui/issues/25217)

> 📝 **Code editor stays open when empty.** The code editor drawer no longer collapses when its content is empty. [#25855](https://github.com/open-webui/open-webui/pull/25855)

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
- [[Changes/Open WebUI/2026-06-29-16-safety-and-privacy-changes-in-v0-10-0|16 Safety and Privacy changes in v0.10.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-29-2-pricing-model-changes-in-v0-10-0|2 Pricing Model changes in v0.10.0]] · Pricing Model
- [[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-29-9-account-and-access-changes-in-v0-10-0|9 Account and Access changes in v0.10.0]] · Account and Access
- [[Changes/Open WebUI/2026-06-29-usable-chat-input-on-mobile-with-many-tools-when-skills-tools-terminal-web-searc|📱 Usable chat input on mobile with many tools. When skills, tools, terminal, web…]] · Image Generation
- [[Changes/Open WebUI/2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0|6 Automation and Scheduling changes in v0.10.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-29-3-context-window-changes-in-v0-10-0|3 Context Window changes in v0.10.0]] · Context Window
- [[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer Workflow changes in v0.10.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-29-29-other-changes-in-v0-10-0|29 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-06-26 · v0 · [[Changes/v0/2026-06-26-the-editor-no-longer-shows-a-false-start-error-when-a-preview-dev-server-or-inst|The editor no longer shows a false start error when a preview, dev server…]]
- Later: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-2-editor-experience-changes-in-v1-0-66|2 Editor Experience changes in v1.0.66]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-dec77c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-10-editor-experience-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-dec77c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->