---
card_id: open-webui-2026-06-29-a67cb9
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Other changes: 29 changes in v0.10.0 — \U0001F9F7
  **Separate skills import and export permissions.** Administrators can now control
  importing…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c1b0c7244eb9da4e55a229dff1eaac6f8dc313e37143df878405414c7cb9886c
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-a67cb9
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 29 other changes'
  evidence:
  - quote: "\U0001F9F7 **Separate skills import and export permissions.** Administrators
      can now control importing and exporting skills independently, with new skills
      import and export permissions. [#25921](https://github.com/open-webui/open-webui/pull/25921)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F522 **Chat and file counts in their dialogs.** The Chats and Files
      dialogs now show the total number of chats and files in their titles. [#25872](https://github.com/open-webui/open-webui/pull/25872),
      [#25873](https://github.com/open-webui/open-webui/pull/25873)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Lighter Markdown setup.** Markdown extension setup now runs once instead
      of on every render, avoiding repeated work and extension stacking. [#25837](https://github.com/open-webui/open-webui/pull/25837)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Fewer queries for channel reactions and replies.** Channel reactions
      and thread replies now load through batched queries, reducing database load
      on busy channels. [#25831](https://github.com/open-webui/open-webui/pull/25831)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Lighter streaming.** Streaming responses now skip re-processing message
      content that hasn't changed, reducing work on every update. [#26325](https://github.com/open-webui/open-webui/pull/26325),
      [#26326](https://github.com/open-webui/open-webui/pull/26326)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F310 **Updated translations.** Catalan, Brazilian Portuguese (pt-BR),
      Irish, German (de-DE), and Spanish (es-ES) translations were updated."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F510 **Knowledge base write access enforced on upload.** Attaching
      an uploaded file to a knowledge base now requires the same write access as the
      rest of the knowledge API, so users without write access can no longer add files
      to a collection by referencing its ID. [#26001](https://github.com/open-webui/open-webui/pull/26001)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F6A7 **Heavily encoded paths rejected behind the proxy.** Request
      paths that remain encoded after repeated decoding are now rejected instead of
      forwarded, preventing a path traversal that could otherwise slip through. [#26050](https://github.com/open-webui/open-webui/pull/26050)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F310 **Image URL fetches hardened against DNS rebinding.** Fetching
      user-supplied image URLs now re-checks the destination address at connection
      time, closing a path that could be used to reach internal addresses behind a
      public hostname. [#25960](https://github.com/open-webui/open-webui/pull/25960)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F6C2 **Web fetch blocklist matches on hostname.** The web fetch
      filter now matches entries against the request's hostname on domain boundaries,
      so blocked hosts can no longer slip through with an added path and lookalike
      domains are no longer mistaken for allowed ones. [#25949](https://github.com/open-webui/open-webui/pull/25949)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4E1 **Real-time events only reach your own session.** The server
      now verifies that a real-time event is delivered only to the requesting user's
      own active session, instead of trusting a client-supplied session identifier.
      [#25763](https://github.com/open-webui/open-webui/pull/25763)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F573️ **Another DNS-rebinding gap closed in URL fetching.** Fetching
      a URL's content now re-checks the destination address at connection time, closing
      another path that could reach internal addresses behind a public hostname. [#25775](https://github.com/open-webui/open-webui/pull/25775)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F9E9 **Code Execution settings collapse when off.** The Code Execution
      settings section now collapses when the toggle is disabled, keeping the settings
      page tidy. [#25970](https://github.com/open-webui/open-webui/pull/25970)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4C5 **German date format in Notes.** Dates in the Notes view now
      display correctly for German, where they previously failed to render. [#25985](https://github.com/open-webui/open-webui/pull/25985)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5B1️ **Dragging chats into folders is more reliable.** Dragging
      a chat into a folder no longer throws an error in cases where the chat couldn't
      be resolved. [#25928](https://github.com/open-webui/open-webui/pull/25928)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5BC️ **Image settings page survives a config load failure.** The
      admin image settings page no longer crashes when its configuration fails to
      load, showing the page instead. [#25933](https://github.com/open-webui/open-webui/pull/25933)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F535 **No more false unread badges on chats.** Chats no longer show
      an unread indicator after automatic changes like title generation or pinning,
      archiving, and moving them between folders, and newly created chats are marked
      read correctly so they don't appear unread after a refresh. [#25912](https://github.com/open-webui/open-webui/pull/25912),
      [#25782](https://github.com/open-webui/open-webui/pull/25782), [#25108](https://github.com/open-webui/open-webui/issues/25108)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4C5 **All-day calendar events keep their date.** Saving an all-day
      calendar event no longer shifts it by a day for users in certain time zones.
      [#25864](https://github.com/open-webui/open-webui/pull/25864)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5C2️ **Chroma collection detection fixed.** Open WebUI now correctly
      detects existing Chroma collections, fixing a case where it always reported
      them as missing. [#25780](https://github.com/open-webui/open-webui/pull/25780)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F9F0 **Valves icon stays visible.** The icon for configuring valves
      no longer disappears, so user-configurable tool and function settings remain
      reachable. [#26256](https://github.com/open-webui/open-webui/pull/26256)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4E4 **Clearer upload error messages.** Failed uploads now show
      a readable explanation instead of an opaque error stub. [#25961](https://github.com/open-webui/open-webui/pull/25961)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4CB **Cloned prompts get a proper title.** Cloning a prompt now
      adds the clone suffix to the correct field, so the duplicate is named as expected.
      [#25800](https://github.com/open-webui/open-webui/pull/25800)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4E1 **Error messages show for non-standard streaming responses.**
      Providers that send errors over non-standard server-sent events now surface
      a readable error instead of nothing. [#23228](https://github.com/open-webui/open-webui/pull/23228)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F6AA **Sign out works from the Account Pending page.** Signing out
      while your account is pending now goes through the proper sign-out flow, so
      single sign-on sessions are ended and you are no longer left stuck on the pending
      screen. [#25681](https://github.com/open-webui/open-webui/pull/25681), [#25644](https://github.com/open-webui/open-webui/issues/25644)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F9F5 **Channel threads bind to the right channel.** A channel thread's
      parent and replies are now tied to the channel in the URL, preventing mismatches
      when switching channels. [#25766](https://github.com/open-webui/open-webui/pull/25766)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ␣ **Space key works when renaming.** Pressing space while renaming a file
      or folder no longer opens it, so spaces can be typed in names. [#25627](https://github.com/open-webui/open-webui/pull/25627)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F524 **Consistent settings label capitalization.** Toggle labels
      in settings now use consistent title casing. [#25765](https://github.com/open-webui/open-webui/pull/25765)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5C4️ **Oversized chunks no longer break Milvus indexing.** Overly
      long text chunks are now trimmed before being sent to Milvus, so a single large
      chunk can no longer fail the whole batch and leave a file with no embeddings.
      [#25857](https://github.com/open-webui/open-webui/pull/25857), [#25858](https://github.com/open-webui/open-webui/pull/25858)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: '⚠️ **Database Migrations**: This update contains database migrations.
      Please be sure to back up your database before updating, as downgrading after
      the migration is not supported.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 29-other-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: uncategorized
  title: 29 other changes in v0.10.0
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: uncategorized
title: 29 other changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 29 other changes in v0.10.0

**Open WebUI** · 2026-06-29 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧷 **Separate skills import and export permissions.** Administrators can now control importing and exporting skills independently, with new skills import and export permissions. [#25921](https://github.com/open-webui/open-webui/pull/25921)

> 🔢 **Chat and file counts in their dialogs.** The Chats and Files dialogs now show the total number of chats and files in their titles. [#25872](https://github.com/open-webui/open-webui/pull/25872), [#25873](https://github.com/open-webui/open-webui/pull/25873)

> ⚡ **Lighter Markdown setup.** Markdown extension setup now runs once instead of on every render, avoiding repeated work and extension stacking. [#25837](https://github.com/open-webui/open-webui/pull/25837)

> ⚡ **Fewer queries for channel reactions and replies.** Channel reactions and thread replies now load through batched queries, reducing database load on busy channels. [#25831](https://github.com/open-webui/open-webui/pull/25831)

> ⚡ **Lighter streaming.** Streaming responses now skip re-processing message content that hasn't changed, reducing work on every update. [#26325](https://github.com/open-webui/open-webui/pull/26325), [#26326](https://github.com/open-webui/open-webui/pull/26326)

> 🌐 **Updated translations.** Catalan, Brazilian Portuguese (pt-BR), Irish, German (de-DE), and Spanish (es-ES) translations were updated.

> 🔐 **Knowledge base write access enforced on upload.** Attaching an uploaded file to a knowledge base now requires the same write access as the rest of the knowledge API, so users without write access can no longer add files to a collection by referencing its ID. [#26001](https://github.com/open-webui/open-webui/pull/26001)

> 🚧 **Heavily encoded paths rejected behind the proxy.** Request paths that remain encoded after repeated decoding are now rejected instead of forwarded, preventing a path traversal that could otherwise slip through. [#26050](https://github.com/open-webui/open-webui/pull/26050)

> 🌐 **Image URL fetches hardened against DNS rebinding.** Fetching user-supplied image URLs now re-checks the destination address at connection time, closing a path that could be used to reach internal addresses behind a public hostname. [#25960](https://github.com/open-webui/open-webui/pull/25960)

> 🛂 **Web fetch blocklist matches on hostname.** The web fetch filter now matches entries against the request's hostname on domain boundaries, so blocked hosts can no longer slip through with an added path and lookalike domains are no longer mistaken for allowed ones. [#25949](https://github.com/open-webui/open-webui/pull/25949)

> 📡 **Real-time events only reach your own session.** The server now verifies that a real-time event is delivered only to the requesting user's own active session, instead of trusting a client-supplied session identifier. [#25763](https://github.com/open-webui/open-webui/pull/25763)

> 🕳️ **Another DNS-rebinding gap closed in URL fetching.** Fetching a URL's content now re-checks the destination address at connection time, closing another path that could reach internal addresses behind a public hostname. [#25775](https://github.com/open-webui/open-webui/pull/25775)

> 🧩 **Code Execution settings collapse when off.** The Code Execution settings section now collapses when the toggle is disabled, keeping the settings page tidy. [#25970](https://github.com/open-webui/open-webui/pull/25970)

> 📅 **German date format in Notes.** Dates in the Notes view now display correctly for German, where they previously failed to render. [#25985](https://github.com/open-webui/open-webui/pull/25985)

> 🖱️ **Dragging chats into folders is more reliable.** Dragging a chat into a folder no longer throws an error in cases where the chat couldn't be resolved. [#25928](https://github.com/open-webui/open-webui/pull/25928)

> 🖼️ **Image settings page survives a config load failure.** The admin image settings page no longer crashes when its configuration fails to load, showing the page instead. [#25933](https://github.com/open-webui/open-webui/pull/25933)

> 🔵 **No more false unread badges on chats.** Chats no longer show an unread indicator after automatic changes like title generation or pinning, archiving, and moving them between folders, and newly created chats are marked read correctly so they don't appear unread after a refresh. [#25912](https://github.com/open-webui/open-webui/pull/25912), [#25782](https://github.com/open-webui/open-webui/pull/25782), [#25108](https://github.com/open-webui/open-webui/issues/25108)

> 📅 **All-day calendar events keep their date.** Saving an all-day calendar event no longer shifts it by a day for users in certain time zones. [#25864](https://github.com/open-webui/open-webui/pull/25864)

> 🗂️ **Chroma collection detection fixed.** Open WebUI now correctly detects existing Chroma collections, fixing a case where it always reported them as missing. [#25780](https://github.com/open-webui/open-webui/pull/25780)

> 🧰 **Valves icon stays visible.** The icon for configuring valves no longer disappears, so user-configurable tool and function settings remain reachable. [#26256](https://github.com/open-webui/open-webui/pull/26256)

> 📤 **Clearer upload error messages.** Failed uploads now show a readable explanation instead of an opaque error stub. [#25961](https://github.com/open-webui/open-webui/pull/25961)

> 📋 **Cloned prompts get a proper title.** Cloning a prompt now adds the clone suffix to the correct field, so the duplicate is named as expected. [#25800](https://github.com/open-webui/open-webui/pull/25800)

> 📡 **Error messages show for non-standard streaming responses.** Providers that send errors over non-standard server-sent events now surface a readable error instead of nothing. [#23228](https://github.com/open-webui/open-webui/pull/23228)

> 🚪 **Sign out works from the Account Pending page.** Signing out while your account is pending now goes through the proper sign-out flow, so single sign-on sessions are ended and you are no longer left stuck on the pending screen. [#25681](https://github.com/open-webui/open-webui/pull/25681), [#25644](https://github.com/open-webui/open-webui/issues/25644)

> 🧵 **Channel threads bind to the right channel.** A channel thread's parent and replies are now tied to the channel in the URL, preventing mismatches when switching channels. [#25766](https://github.com/open-webui/open-webui/pull/25766)

> ␣ **Space key works when renaming.** Pressing space while renaming a file or folder no longer opens it, so spaces can be typed in names. [#25627](https://github.com/open-webui/open-webui/pull/25627)

> 🔤 **Consistent settings label capitalization.** Toggle labels in settings now use consistent title casing. [#25765](https://github.com/open-webui/open-webui/pull/25765)

> 🗄️ **Oversized chunks no longer break Milvus indexing.** Overly long text chunks are now trimmed before being sent to Milvus, so a single large chunk can no longer fail the whole batch and leave a file with no embeddings. [#25857](https://github.com/open-webui/open-webui/pull/25857), [#25858](https://github.com/open-webui/open-webui/pull/25858)

> ⚠️ **Database Migrations**: This update contains database migrations. Please be sure to back up your database before updating, as downgrading after the migration is not supported.

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
- [[Changes/Open WebUI/2026-06-29-10-editor-experience-changes-in-v0-10-0|10 Editor Experience changes in v0.10.0]] · Editor Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-a67cb9&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-29-other-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-a67cb9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->