---
card_id: open-webui-2026-08-25-6b2002
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Other changes: 39 changes in v0.11.1 — \U0001F6F0️
  **Cheaper log export.** Deployments that export their logs to a telemetry collector,
  with…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 60a84f24fb3248b15e5c947c62ea0875484482d747744fac50a23ee3a2d48859
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-6b2002
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 39 other changes'
  evidence:
  - quote: "\U0001F6F0️ **Cheaper log export.** Deployments that export their logs
      to a telemetry collector, with \"ENABLE_OTEL\" and \"ENABLE_OTEL_LOGS\" both
      set, now prepare each exported line once instead of twice, which matters more
      than it used to now that log text is only assembled when something will actually
      read it. [#27840](https://github.com/open-webui/open-webui/pull/27840)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FAB6 **Lighter page loads.** Several small requests the interface
      makes on every page load, along with a few administrative ones, no longer set
      up database access they never used, which took several times longer than the
      rest of the request put together. [#28178](https://github.com/open-webui/open-webui/pull/28178)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ♻️ **One less read per message.** Sending a message no longer loads the
      whole conversation from the database twice over, which mattered most in long
      chats where that record is largest. [#28809](https://github.com/open-webui/open-webui/pull/28809)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F38F **Turning off compression of live updates.** A new \"UVICORN_WS_PER_MESSAGE_DEFLATE\"
      setting stops the server compressing every live update it sends, which costs
      processor time on each one for almost no saving now that a reply streams as
      small pieces; compression stays on unless it is turned off. [#28613](https://github.com/open-webui/open-webui/pull/28613)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⚡ **Uninterrupted chat during knowledge search.** Responses now keep streaming
      for everyone on the server while knowledge base searches run, instead of pausing
      until each search finishes. [#27824](https://github.com/open-webui/open-webui/pull/27824)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4C0 **Less repeated work setting up built-in tools.** Every chat
      request no longer rebuilds a fresh copy of each built-in tool's definition from
      scratch, which was paid once per tool on every message. [#28860](https://github.com/open-webui/open-webui/pull/28860)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F310 **Translation updates.** Faroese was added, and translations
      for Slovenian, Hungarian, Finnish, Korean, Portuguese (Brazil), Catalan, and
      French were enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6A7 **Web address checks that could be skipped.** The fetchable-address
      test and the operator's web fetch filter list now run on every outgoing request,
      where a proxied or already-open connection could bypass them and a filter entry
      written as an address range silently matched nothing at all. [#27823](https://github.com/open-webui/open-webui/pull/27823)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F47B **Vanishing responses.** Replies from Responses-API providers
      that report an empty output at the end of a stream no longer disappear the moment
      generation finishes, leaving an empty message in their place. [#27800](https://github.com/open-webui/open-webui/pull/27800),
      [#27789](https://github.com/open-webui/open-webui/discussions/27789)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9F5 **Replies cut short mid-stream.** A reply no longer breaks
      off part way through when a provider sends the pieces of its response in an
      unexpected order, which had left the answer truncated and skipped the filters
      that run once a message finishes. [#28312](https://github.com/open-webui/open-webui/pull/28312)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4C6 **Default date for new events.** Creating a calendar event
      now starts on today's date rather than tomorrow's when you open the form in
      the evening, or yesterday's when you open it early in the morning. [#27779](https://github.com/open-webui/open-webui/pull/27779),
      [#27778](https://github.com/open-webui/open-webui/issues/27778)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4E8 **Reliable streaming with unusual characters.** Responses containing
      any of three rare invisible line break characters no longer arrive split or
      broken when the \"ENABLE_ORJSON\" option is turned on. [#27819](https://github.com/open-webui/open-webui/pull/27819)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4AD **Readable errors on chat actions.** When moving, renaming,
      or otherwise changing a chat fails, the message explaining why now appears in
      place of an unhelpful object placeholder. [#28260](https://github.com/open-webui/open-webui/pull/28260),
      [#28259](https://github.com/open-webui/open-webui/issues/28259)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5C3️ **openGauss vector storage.** Deployments using openGauss
      for vector storage no longer fail the moment they touch it. [#27838](https://github.com/open-webui/open-webui/pull/27838)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F578️ **Overlapping branches in the overview.** Branch nodes in
      a chat's overview keep a clear gap between them when the interface is scaled
      up, rather than sitting on top of one another. [#27995](https://github.com/open-webui/open-webui/pull/27995),
      [#27994](https://github.com/open-webui/open-webui/issues/27994)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F506 **Regenerate in high contrast mode.** With high contrast mode
      on, the regenerate button now stays visible on earlier replies instead of appearing
      only when you hover over them. [#27644](https://github.com/open-webui/open-webui/pull/27644),
      [#27638](https://github.com/open-webui/open-webui/issues/27638)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4F7 **Round profile pictures on narrow screens.** Profile pictures
      in the admin user list and other lists no longer squash into ovals of differing
      widths when the window is narrow. [#28000](https://github.com/open-webui/open-webui/pull/28000),
      [#27999](https://github.com/open-webui/open-webui/issues/27999)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5D2️ **Reply box in threads.** The reply box in a channel thread
      now stays at the bottom of the panel while you scroll back through the replies,
      instead of scrolling out of sight with them. [#27768](https://github.com/open-webui/open-webui/pull/27768),
      [#27767](https://github.com/open-webui/open-webui/issues/27767)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F3F7️ **Folder names with unusual characters.** Naming a folder
      is no longer refused because another folder's name happens to be similar, and
      a name ending in a backslash no longer fails outright on PostgreSQL, because
      names are now compared exactly rather than treated as a search pattern. [#28695](https://github.com/open-webui/open-webui/pull/28695),
      [#28694](https://github.com/open-webui/open-webui/issues/28694)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F36A **Signed-in tool servers.** A tool server that relies on your
      session now receives the credentials belonging to its own connection, rather
      than whichever were most recently prepared. [#28630](https://github.com/open-webui/open-webui/pull/28630)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⬆️ **Scroll to top on the first click.** In a long chat where older messages
      had not been loaded yet, one click of scroll to top now reaches the first message
      instead of stopping short and needing a second. [#28659](https://github.com/open-webui/open-webui/pull/28659),
      [#28658](https://github.com/open-webui/open-webui/issues/28658)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F518 **Double bullets in the release notes.** Each entry in the
      what's new dialog shows a single bullet again, rather than two sitting at different
      heights. [#28676](https://github.com/open-webui/open-webui/pull/28676), [#28675](https://github.com/open-webui/open-webui/issues/28675)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F517 **Deleting a message in a looping chat.** Deleting a message
      no longer hangs when the conversation contains a cycle in its reply structure.
      [#28035](https://github.com/open-webui/open-webui/pull/28035)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6B0 **Watching file processing tying up the database.** Waiting
      for a file or a knowledge base to finish processing no longer holds a database
      connection open for as long as the page is watching, which on busy instances
      could use up every available connection and leave the rest of the application
      unable to reach the database. [#28183](https://github.com/open-webui/open-webui/pull/28183)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F515 **Calendar reminders stopping for everyone.** A single event
      whose reminder time was stored as something other than a number no longer stops
      reminders being sent, for that event or for anyone else's, and falls back to
      the usual reminder window instead. [#28790](https://github.com/open-webui/open-webui/pull/28790)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F3AB **Saving a message with unusual characters on PostgreSQL.**
      A message carrying characters PostgreSQL will not store outside its text no
      longer fails to save, where those characters were cleaned from the conversation
      but passed through raw to the separate message record. [#28820](https://github.com/open-webui/open-webui/pull/28820)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⌨ **Errors after sending a long message.** With prompt autocompletion on,
      sending or clearing a message of several paragraphs within a second of typing
      no longer throws an error in the browser console. [#28824](https://github.com/open-webui/open-webui/pull/28824),
      [#28823](https://github.com/open-webui/open-webui/issues/28823)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ✅ **Checklists in notes.** A checklist in a note now previews and downloads
      as a proper checklist, where each item carried a stray second pair of brackets
      and its text began two lines below the box. [#27671](https://github.com/open-webui/open-webui/pull/27671),
      [#26067](https://github.com/open-webui/open-webui/issues/26067)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9F6 **Text dropped from a reply by a filter.** A filter that rewrites
      a reply as it streams, or a provider that sends something other than plain text
      in a chunk, no longer causes that part of the reply to vanish without explanation.
      [#28840](https://github.com/open-webui/open-webui/pull/28840)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F3D7 **Timers firing twice after a fork.** Branching a conversation
      that has a timer set no longer leaves the copy able to fire that timer as well.
      [#27663](https://github.com/open-webui/open-webui/pull/27663), [#27622](https://github.com/open-webui/open-webui/issues/27622),
      [#27745](https://github.com/open-webui/open-webui/issues/27745)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F46F **Code in pinned messages.** Opening the pinned messages of
      a channel now shows the code in those messages, where each block appeared empty
      and its contents were drawn into the channel behind the dialog instead, doubling
      them there. [#27740](https://github.com/open-webui/open-webui/pull/27740), [#27739](https://github.com/open-webui/open-webui/issues/27739)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6E2 **Using pgvector with database access by role.** An instance
      on Amazon RDS that signs in to its database with a temporary credential rather
      than a stored password now starts when pgvector is the vector store, where the
      two could not be used together and the container exited on startup. [#27754](https://github.com/open-webui/open-webui/pull/27754),
      [#27752](https://github.com/open-webui/open-webui/issues/27752)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F39A **Retrieval mode shown from another item.** The retrieval mode
      shown when opening a knowledge item is now that item's own, where it could show
      the setting of whichever item was opened before it. [#27686](https://github.com/open-webui/open-webui/pull/27686),
      [#27684](https://github.com/open-webui/open-webui/issues/27684), [#27801](https://github.com/open-webui/open-webui/issues/27801),
      [#28825](https://github.com/open-webui/open-webui/issues/28825)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4DB **Editing the wrong group.** The dialog for editing a user
      group now stays with the group it was opened for, where a reordering of the
      list beneath it could leave it saving to a different group. [#28076](https://github.com/open-webui/open-webui/pull/28076),
      [#28075](https://github.com/open-webui/open-webui/issues/28075)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ☎ **Chats opening halfway up.** A conversation whose recent messages are
      short now opens at the latest message rather than somewhere in the middle, and
      older messages loaded while scrolling up no longer shift what you were reading.
      [#28657](https://github.com/open-webui/open-webui/pull/28657), [#28656](https://github.com/open-webui/open-webui/issues/28656)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F464 **Fallback profile pictures.** A profile picture that fails
      to load, such as one belonging to a deleted account, now falls back to the default
      avatar instead of showing clipped placeholder text beside the message. [#28270](https://github.com/open-webui/open-webui/pull/28270),
      [#28269](https://github.com/open-webui/open-webui/issues/28269)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: '⚠️ **Database Migrations**: This release includes database schema changes;
      we strongly recommend backing up your database and all associated data before
      upgrading in production environments. If you are running a multi-worker, multi-server,
      or load-balanced deployment, all instances must be updated simultaneously, rolling
      updates are not supported and will cause application failures due to schema
      incompatibility.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F3AD **Playwright web loader egress.** When a page is fetched with
      the Playwright loader, the page's own requests for its images, scripts, and
      stylesheets are now made by the Open WebUI backend instead of by the browser,
      so administrators using a remote browser through \"PLAYWRIGHT_WS_URL\" should
      expect that traffic to leave from the backend's address rather than the browser
      host, those using a private certificate authority should expect it to be trusted
      through \"AIOHTTP_CLIENT_SSL_CERT_FILE\" rather than the browser's own store,
      and those who set a proxy on the loader should know it no longer applies to
      these requests, which follow the environment's proxy settings instead. [#28634](https://github.com/open-webui/open-webui/pull/28634)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F40C **Slower Playwright page loads without async.** A page fetched
      with the Playwright loader on the synchronous path now fetches its images, scripts,
      and stylesheets one at a time rather than together, which in the change's own
      measurements took a page with thirty assets from 2.0 to 3.0 seconds, and one
      with eight slow assets from 1.1 to 4.5 seconds; the asynchronous path is unaffected.
      [#28634](https://github.com/open-webui/open-webui/pull/28634)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 39-other-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: uncategorized
  title: 39 other changes in v0.11.1
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: uncategorized
title: 39 other changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 39 other changes in v0.11.1

**Open WebUI** · 2026-08-25 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🛰️ **Cheaper log export.** Deployments that export their logs to a telemetry collector, with "ENABLE_OTEL" and "ENABLE_OTEL_LOGS" both set, now prepare each exported line once instead of twice, which matters more than it used to now that log text is only assembled when something will actually read it. [#27840](https://github.com/open-webui/open-webui/pull/27840)

> 🪶 **Lighter page loads.** Several small requests the interface makes on every page load, along with a few administrative ones, no longer set up database access they never used, which took several times longer than the rest of the request put together. [#28178](https://github.com/open-webui/open-webui/pull/28178)

> ♻️ **One less read per message.** Sending a message no longer loads the whole conversation from the database twice over, which mattered most in long chats where that record is largest. [#28809](https://github.com/open-webui/open-webui/pull/28809)

> 🎏 **Turning off compression of live updates.** A new "UVICORN_WS_PER_MESSAGE_DEFLATE" setting stops the server compressing every live update it sends, which costs processor time on each one for almost no saving now that a reply streams as small pieces; compression stays on unless it is turned off. [#28613](https://github.com/open-webui/open-webui/pull/28613)

> ⚡ **Uninterrupted chat during knowledge search.** Responses now keep streaming for everyone on the server while knowledge base searches run, instead of pausing until each search finishes. [#27824](https://github.com/open-webui/open-webui/pull/27824)

> 📀 **Less repeated work setting up built-in tools.** Every chat request no longer rebuilds a fresh copy of each built-in tool's definition from scratch, which was paid once per tool on every message. [#28860](https://github.com/open-webui/open-webui/pull/28860)

> 🌐 **Translation updates.** Faroese was added, and translations for Slovenian, Hungarian, Finnish, Korean, Portuguese (Brazil), Catalan, and French were enhanced and expanded.

> 🚧 **Web address checks that could be skipped.** The fetchable-address test and the operator's web fetch filter list now run on every outgoing request, where a proxied or already-open connection could bypass them and a filter entry written as an address range silently matched nothing at all. [#27823](https://github.com/open-webui/open-webui/pull/27823)

> 👻 **Vanishing responses.** Replies from Responses-API providers that report an empty output at the end of a stream no longer disappear the moment generation finishes, leaving an empty message in their place. [#27800](https://github.com/open-webui/open-webui/pull/27800), [#27789](https://github.com/open-webui/open-webui/discussions/27789)

> 🧵 **Replies cut short mid-stream.** A reply no longer breaks off part way through when a provider sends the pieces of its response in an unexpected order, which had left the answer truncated and skipped the filters that run once a message finishes. [#28312](https://github.com/open-webui/open-webui/pull/28312)

> 📆 **Default date for new events.** Creating a calendar event now starts on today's date rather than tomorrow's when you open the form in the evening, or yesterday's when you open it early in the morning. [#27779](https://github.com/open-webui/open-webui/pull/27779), [#27778](https://github.com/open-webui/open-webui/issues/27778)

> 📨 **Reliable streaming with unusual characters.** Responses containing any of three rare invisible line break characters no longer arrive split or broken when the "ENABLE_ORJSON" option is turned on. [#27819](https://github.com/open-webui/open-webui/pull/27819)

> 💭 **Readable errors on chat actions.** When moving, renaming, or otherwise changing a chat fails, the message explaining why now appears in place of an unhelpful object placeholder. [#28260](https://github.com/open-webui/open-webui/pull/28260), [#28259](https://github.com/open-webui/open-webui/issues/28259)

> 🗃️ **openGauss vector storage.** Deployments using openGauss for vector storage no longer fail the moment they touch it. [#27838](https://github.com/open-webui/open-webui/pull/27838)

> 🕸️ **Overlapping branches in the overview.** Branch nodes in a chat's overview keep a clear gap between them when the interface is scaled up, rather than sitting on top of one another. [#27995](https://github.com/open-webui/open-webui/pull/27995), [#27994](https://github.com/open-webui/open-webui/issues/27994)

> 🔆 **Regenerate in high contrast mode.** With high contrast mode on, the regenerate button now stays visible on earlier replies instead of appearing only when you hover over them. [#27644](https://github.com/open-webui/open-webui/pull/27644), [#27638](https://github.com/open-webui/open-webui/issues/27638)

> 📷 **Round profile pictures on narrow screens.** Profile pictures in the admin user list and other lists no longer squash into ovals of differing widths when the window is narrow. [#28000](https://github.com/open-webui/open-webui/pull/28000), [#27999](https://github.com/open-webui/open-webui/issues/27999)

> 🗒️ **Reply box in threads.** The reply box in a channel thread now stays at the bottom of the panel while you scroll back through the replies, instead of scrolling out of sight with them. [#27768](https://github.com/open-webui/open-webui/pull/27768), [#27767](https://github.com/open-webui/open-webui/issues/27767)

> 🏷️ **Folder names with unusual characters.** Naming a folder is no longer refused because another folder's name happens to be similar, and a name ending in a backslash no longer fails outright on PostgreSQL, because names are now compared exactly rather than treated as a search pattern. [#28695](https://github.com/open-webui/open-webui/pull/28695), [#28694](https://github.com/open-webui/open-webui/issues/28694)

> 🍪 **Signed-in tool servers.** A tool server that relies on your session now receives the credentials belonging to its own connection, rather than whichever were most recently prepared. [#28630](https://github.com/open-webui/open-webui/pull/28630)

> ⬆️ **Scroll to top on the first click.** In a long chat where older messages had not been loaded yet, one click of scroll to top now reaches the first message instead of stopping short and needing a second. [#28659](https://github.com/open-webui/open-webui/pull/28659), [#28658](https://github.com/open-webui/open-webui/issues/28658)

> 🔘 **Double bullets in the release notes.** Each entry in the what's new dialog shows a single bullet again, rather than two sitting at different heights. [#28676](https://github.com/open-webui/open-webui/pull/28676), [#28675](https://github.com/open-webui/open-webui/issues/28675)

> 🔗 **Deleting a message in a looping chat.** Deleting a message no longer hangs when the conversation contains a cycle in its reply structure. [#28035](https://github.com/open-webui/open-webui/pull/28035)

> 🚰 **Watching file processing tying up the database.** Waiting for a file or a knowledge base to finish processing no longer holds a database connection open for as long as the page is watching, which on busy instances could use up every available connection and leave the rest of the application unable to reach the database. [#28183](https://github.com/open-webui/open-webui/pull/28183)

> 🔕 **Calendar reminders stopping for everyone.** A single event whose reminder time was stored as something other than a number no longer stops reminders being sent, for that event or for anyone else's, and falls back to the usual reminder window instead. [#28790](https://github.com/open-webui/open-webui/pull/28790)

> 🎫 **Saving a message with unusual characters on PostgreSQL.** A message carrying characters PostgreSQL will not store outside its text no longer fails to save, where those characters were cleaned from the conversation but passed through raw to the separate message record. [#28820](https://github.com/open-webui/open-webui/pull/28820)

> ⌨ **Errors after sending a long message.** With prompt autocompletion on, sending or clearing a message of several paragraphs within a second of typing no longer throws an error in the browser console. [#28824](https://github.com/open-webui/open-webui/pull/28824), [#28823](https://github.com/open-webui/open-webui/issues/28823)

> ✅ **Checklists in notes.** A checklist in a note now previews and downloads as a proper checklist, where each item carried a stray second pair of brackets and its text began two lines below the box. [#27671](https://github.com/open-webui/open-webui/pull/27671), [#26067](https://github.com/open-webui/open-webui/issues/26067)

> 🧶 **Text dropped from a reply by a filter.** A filter that rewrites a reply as it streams, or a provider that sends something other than plain text in a chunk, no longer causes that part of the reply to vanish without explanation. [#28840](https://github.com/open-webui/open-webui/pull/28840)

> 🏗 **Timers firing twice after a fork.** Branching a conversation that has a timer set no longer leaves the copy able to fire that timer as well. [#27663](https://github.com/open-webui/open-webui/pull/27663), [#27622](https://github.com/open-webui/open-webui/issues/27622), [#27745](https://github.com/open-webui/open-webui/issues/27745)

> 👯 **Code in pinned messages.** Opening the pinned messages of a channel now shows the code in those messages, where each block appeared empty and its contents were drawn into the channel behind the dialog instead, doubling them there. [#27740](https://github.com/open-webui/open-webui/pull/27740), [#27739](https://github.com/open-webui/open-webui/issues/27739)

> 🛢 **Using pgvector with database access by role.** An instance on Amazon RDS that signs in to its database with a temporary credential rather than a stored password now starts when pgvector is the vector store, where the two could not be used together and the container exited on startup. [#27754](https://github.com/open-webui/open-webui/pull/27754), [#27752](https://github.com/open-webui/open-webui/issues/27752)

> 🎚 **Retrieval mode shown from another item.** The retrieval mode shown when opening a knowledge item is now that item's own, where it could show the setting of whichever item was opened before it. [#27686](https://github.com/open-webui/open-webui/pull/27686), [#27684](https://github.com/open-webui/open-webui/issues/27684), [#27801](https://github.com/open-webui/open-webui/issues/27801), [#28825](https://github.com/open-webui/open-webui/issues/28825)

> 📛 **Editing the wrong group.** The dialog for editing a user group now stays with the group it was opened for, where a reordering of the list beneath it could leave it saving to a different group. [#28076](https://github.com/open-webui/open-webui/pull/28076), [#28075](https://github.com/open-webui/open-webui/issues/28075)

> ☎ **Chats opening halfway up.** A conversation whose recent messages are short now opens at the latest message rather than somewhere in the middle, and older messages loaded while scrolling up no longer shift what you were reading. [#28657](https://github.com/open-webui/open-webui/pull/28657), [#28656](https://github.com/open-webui/open-webui/issues/28656)

> 👤 **Fallback profile pictures.** A profile picture that fails to load, such as one belonging to a deleted account, now falls back to the default avatar instead of showing clipped placeholder text beside the message. [#28270](https://github.com/open-webui/open-webui/pull/28270), [#28269](https://github.com/open-webui/open-webui/issues/28269)

> ⚠️ **Database Migrations**: This release includes database schema changes; we strongly recommend backing up your database and all associated data before upgrading in production environments. If you are running a multi-worker, multi-server, or load-balanced deployment, all instances must be updated simultaneously, rolling updates are not supported and will cause application failures due to schema incompatibility.

> 🎭 **Playwright web loader egress.** When a page is fetched with the Playwright loader, the page's own requests for its images, scripts, and stylesheets are now made by the Open WebUI backend instead of by the browser, so administrators using a remote browser through "PLAYWRIGHT_WS_URL" should expect that traffic to leave from the backend's address rather than the browser host, those using a private certificate authority should expect it to be trusted through "AIOHTTP_CLIENT_SSL_CERT_FILE" rather than the browser's own store, and those who set a proxy on the loader should know it no longer applies to these requests, which follow the environment's proxy settings instead. [#28634](https://github.com/open-webui/open-webui/pull/28634)

> 🐌 **Slower Playwright page loads without async.** A page fetched with the Playwright loader on the synchronous path now fetches its images, scripts, and stylesheets one at a time rather than together, which in the change's own measurements took a page with thirty assets from 2.0 to 3.0 seconds, and one with eight slow assets from 1.1 to 4.5 seconds; the asynchronous path is unaffected. [#28634](https://github.com/open-webui/open-webui/pull/28634)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-25-9-files-and-data-changes-in-v0-11-1|9 Files and Data changes in v0.11.1]] · Files and Data
- [[Changes/Open WebUI/2026-08-25-image-generation-and-web-search-staying-switched-off-turning-either-off-now-take|🎨 Image generation and web search staying switched off. Turning either off now…]] · Image Generation
- [[Changes/Open WebUI/2026-08-25-7-safety-and-privacy-changes-in-v0-11-1|7 Safety and Privacy changes in v0.11.1]] · Safety and Privacy
- [[Changes/Open WebUI/2026-08-25-improved-ui-accessibility-a-closed-sidebar-is-no-longer-reachable-by-keyboard-or|♿ Improved UI accessibility. A closed sidebar is no longer reachable by keyboard…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-08-25-2-pricing-model-changes-in-v0-11-1|2 Pricing Model changes in v0.11.1]] · Pricing Model
- [[Changes/Open WebUI/2026-08-25-11-automation-and-scheduling-changes-in-v0-11-1|11 Automation and Scheduling changes in v0.11.1]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-08-25-10-reliability-and-performance-changes-in-v0-11-1|10 Reliability and Performance changes in v0.11.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-08-25-6-collaboration-changes-in-v0-11-1|6 Collaboration changes in v0.11.1]] · Collaboration
- [[Changes/Open WebUI/2026-08-25-4-context-window-changes-in-v0-11-1|4 Context Window changes in v0.11.1]] · Context Window
- [[Changes/Open WebUI/2026-08-25-13-account-and-access-changes-in-v0-11-1|13 Account and Access changes in v0.11.1]] · Account and Access
- [[Changes/Open WebUI/2026-08-25-starting-up-on-windows-the-windows-start-script-now-creates-the-secret-key-it-ne|🪟 Starting up on Windows. The Windows start script now creates the secret key…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-08-25-2-multimodal-input-changes-in-v0-11-1|2 Multimodal Input changes in v0.11.1]] · Multimodal Input
- [[Changes/Open WebUI/2026-08-25-12-editor-experience-changes-in-v0-11-1|12 Editor Experience changes in v0.11.1]] · Editor Experience
- [[Changes/Open WebUI/2026-08-25-4-apps-and-integrations-changes-in-v0-11-1|4 Apps and Integrations changes in v0.11.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-08-25-73-developer-workflow-changes-in-v0-11-1|73 Developer Workflow changes in v0.11.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-08-25-8-memory-and-personalization-changes-in-v0-11-1|8 Memory and Personalization changes in v0.11.1]] · Memory and Personalization
- [[Changes/Open WebUI/2026-08-25-files-for-delegated-tasks-a-task-handed-to-a-sub-agent-can-now-carry-the-attachm|🤝 Files for delegated tasks. A task handed to a sub-agent can now carry…]] · Agent Mode
- [[Changes/Open WebUI/2026-08-25-4-enterprise-and-administration-changes-in-v0-11-1|4 Enterprise and Administration changes in v0.11.1]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-08-25-24-interface-experience-changes-in-v0-11-1|24 Interface Experience changes in v0.11.1]] · Interface Experience
- [[Changes/Open WebUI/2026-08-25-5-search-and-browsing-changes-in-v0-11-1|5 Search and Browsing changes in v0.11.1]] · Search and Browsing
- [[Changes/Open WebUI/2026-08-25-4-voice-and-audio-changes-in-v0-11-1|4 Voice and Audio changes in v0.11.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-08-25-56-model-support-changes-in-v0-11-1|56 Model Support changes in v0.11.1]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-6b2002&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-39-other-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-6b2002%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->