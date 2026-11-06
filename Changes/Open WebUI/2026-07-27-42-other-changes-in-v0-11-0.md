---
card_id: open-webui-2026-07-27-a63db5
date: '2026-07-27'
description: "Open WebUI · 2026-07-27 · Other changes: 42 changes in v0.11.0 — \U0001F4CC
  **Pin the conversation map.** The chat overview now has a pin control that stops
  it…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 719463d741a8c67aa4af8dc2bd2518c4cfe81208fe6ac0a903bc463682523a11
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-27-a63db5
  comparison: ''
  date: '2026-07-27'
  description: 'Open WebUI — v0.11.0: 42 other changes'
  evidence:
  - quote: "\U0001F4CC **Pin the conversation map.** The chat overview now has a pin
      control that stops it recentring on the newest message, so you can keep looking
      at the branch you were reading while a reply comes in. [#25736](https://github.com/open-webui/open-webui/pull/25736)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⌨️ **Turn keyboard shortcuts off.** A new switch in the keyboard settings
      disables every configurable shortcut and hides its hint, so combinations that
      clash with your browser or operating system pass straight through. [#27300](https://github.com/open-webui/open-webui/pull/27300),
      [#1008](https://github.com/open-webui/open-webui/issues/1008)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FAA7 **Group names in forwarded headers.** Custom headers on a connection
      can now carry the groups a person belongs to, by name or by id, so an upstream
      service or gateway can apply its own rules per group. [#27236](https://github.com/open-webui/open-webui/pull/27236),
      [#26834](https://github.com/open-webui/open-webui/issues/26834)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4D1 **Cheaper audit logging.** With audit logging on, each request
      is no longer authenticated a second time just to record the log entry, so audited
      instances carry noticeably less overhead. [#27373](https://github.com/open-webui/open-webui/pull/27373)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F6E2️ **Less database overhead per request.** SQLite installations
      no longer run a connection check before every database call, and requests that
      never touch the database skip the bookkeeping that used to run regardless. [#27385](https://github.com/open-webui/open-webui/pull/27385)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F999 **Fewer settings lookups on Ollama requests.** Ollama chat,
      generation and embedding requests now read their connection settings once instead
      of up to four times, so each request reaches the server sooner. [#27226](https://github.com/open-webui/open-webui/pull/27226)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F684 **Leaner passthrough streaming.** Responses the server only
      relays now go straight through in whole network reads instead of being split
      line by line, roughly halving the work spent shuttling a streamed reply on those
      routes. [#27384](https://github.com/open-webui/open-webui/pull/27384)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9F6 **Web page parsing off the critical path.** Reading those pages
      no longer holds up everything else on the server, so other people's replies,
      live updates and health checks keep flowing during a search instead of stalling
      for a second or more. [#27446](https://github.com/open-webui/open-webui/pull/27446)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F310 **Translation updates.** Slovenian is now available, and translations
      for English (UK), Finnish, German, Japanese, Portuguese (Brazil) and Portuguese
      (Portugal) were enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F39F️ **Ollama version no longer readable anonymously.** Reading
      the configured Ollama backend's version now requires signing in, closing a route
      that let anyone learn the version in use and count how many backends are configured.
      [#27199](https://github.com/open-webui/open-webui/pull/27199)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F6CE️ **Stopping someone else's generation.** Deleting a chat now
      checks who you are before anything is cancelled, so knowing another person's
      chat id no longer lets you cut off their reply or title generation on a request
      that is refused anyway. [#27006](https://github.com/open-webui/open-webui/pull/27006)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⏲️ **Cancelling someone else's timers.** Marking a chat as read now only
      clears your own pending timers on it, instead of clearing everyone's, which
      had let another person's scheduled prompt be silently cancelled without them
      being told. [#27472](https://github.com/open-webui/open-webui/pull/27472)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4D5 **Tool source shown to people who can only use it.** Opening
      a tool you were given read access to no longer returns its source code, which
      read access was never meant to include. [#27005](https://github.com/open-webui/open-webui/pull/27005)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9FA **Knowledge base cleanup reaching other collections.** Tidying
      up a knowledge base now acts only on files and folders that belong to it, so
      someone with write access to one knowledge base can no longer delete folders
      or search data belonging to another. [#26722](https://github.com/open-webui/open-webui/pull/26722)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⌛ **Searches that could stall the server.** A search pattern inside knowledge
      base commands now runs under a time budget, so a pattern that would take minutes
      to evaluate can no longer hold up everyone else on the instance. [#27471](https://github.com/open-webui/open-webui/pull/27471)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4D3 **Notes in folder knowledge are access checked.** Notes attached
      to a folder are now filtered against your own access before the list reaches
      the assistant, rather than relying on later checks further along. [#26739](https://github.com/open-webui/open-webui/pull/26739)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4C3 **Action functions receive the response text.** Running an
      action on a response now passes the assistant's text to the function, instead
      of handing it an empty message. [#26798](https://github.com/open-webui/open-webui/pull/26798),
      [#26672](https://github.com/open-webui/open-webui/issues/26672)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F50C **Dropped sessions during keepalive.** Live connections no
      longer break on a routine keepalive check, which had cut the session so that
      anything the server needed to run in your browser failed afterwards, most visibly
      the code execution tool reporting the client as disconnected on every run. [#27553](https://github.com/open-webui/open-webui/pull/27553),
      [#27550](https://github.com/open-webui/open-webui/issues/27550)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⬅️ **Back button after opening admin or workspace.** Going back in the
      browser now returns you to the page you came from, instead of being pushed forward
      again to where you just were. [#27478](https://github.com/open-webui/open-webui/pull/27478),
      [#27477](https://github.com/open-webui/open-webui/issues/27477)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F944 **Counting matches in knowledge base commands.** Piping text
      into a search inside knowledge base commands now honours the count and filenames-only
      flags, instead of returning the matching lines regardless. [#26721](https://github.com/open-webui/open-webui/pull/26721),
      [#26715](https://github.com/open-webui/open-webui/issues/26715)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4E7 **Outlook message uploads.** Uploading a .msg email now works,
      where it previously failed because the package it relied on could not be installed
      alongside the rest of the application at all. [#26704](https://github.com/open-webui/open-webui/pull/26704),
      [#26690](https://github.com/open-webui/open-webui/issues/26690)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F6A7 **Quoted entries in the web fetch filter list.** Stray quote
      marks around a filter entry, which Docker Compose passes through literally,
      no longer turn the list into one that blocks every web address. [#26910](https://github.com/open-webui/open-webui/pull/26910),
      [#26908](https://github.com/open-webui/open-webui/issues/26908)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F578️ **Mixed web page extraction.** Fetching several web pages
      at once now reads each one according to its own format, instead of applying
      the first page's format to the whole batch and garbling the rest. [#27367](https://github.com/open-webui/open-webui/pull/27367)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9EF **Leftover browser sessions on web fetches.** Fetching pages
      through a remote Playwright server now closes each page and the browser even
      when a page times out or the search is abandoned partway, instead of leaving
      sessions open and slowing every later search until that server was restarted.
      [#27526](https://github.com/open-webui/open-webui/pull/27526), [#25880](https://github.com/open-webui/open-webui/issues/25880)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F50A **Text-to-speech reliability.** Text-to-speech playback and
      other streamed responses no longer intermittently cut out partway through when
      several requests run at once. [#26924](https://github.com/open-webui/open-webui/pull/26924),
      [#26922](https://github.com/open-webui/open-webui/issues/26922)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4E8 **Non-streaming requests to strict providers.** A request that
      is not streaming no longer carries the streaming-only usage option, which some
      providers reject outright."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FA9D **Tool calls with structured arguments.** A provider that sends
      a tool call's arguments as an object, or as nothing at all, no longer breaks
      the reply partway through. [#27195](https://github.com/open-webui/open-webui/issues/27195)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FA79 **Startup with an ownerless tool or function.** A tool or function
      left without an owner no longer prevents the application from starting, which
      had blocked all chat responses until it was removed. [#26850](https://github.com/open-webui/open-webui/pull/26850),
      [#26843](https://github.com/open-webui/open-webui/issues/26843)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5C3️ **Milvus Lite collection creation.** Setting up collections
      now succeeds on embedded Milvus Lite, which previously could fail while creating
      the resource index. [#26911](https://github.com/open-webui/open-webui/pull/26911)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9FD **Milvus log noise.** Instances backed by Milvus no longer
      fill their logs with deprecation warnings while indexing and retrieving, and
      keep working with future PyMilvus releases that drop the old interface entirely.
      [#27521](https://github.com/open-webui/open-webui/pull/27521), [#26978](https://github.com/open-webui/open-webui/issues/26978)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F526 **Connections on hardened instances.** With the admin access
      bypass turned off, a connection that has no access grants yet is now reachable
      by administrators again, instead of being hidden from everyone including the
      admin who created it. [#27581](https://github.com/open-webui/open-webui/pull/27581),
      [#27580](https://github.com/open-webui/open-webui/issues/27580), [#27064](https://github.com/open-webui/open-webui/issues/27064)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FA9B **Deleting an Ollama connection.** Removing an Ollama connection
      now saves straight away, instead of reappearing until the Ollama API switch
      was toggled afterwards. [#27483](https://github.com/open-webui/open-webui/pull/27483),
      [#27482](https://github.com/open-webui/open-webui/issues/27482)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F527 **Sign-on settings from environment variables.** Single sign-on
      settings supplied through environment variables are no longer overridden by
      stale values saved at first startup, so changing them takes effect. [#26928](https://github.com/open-webui/open-webui/pull/26928),
      [#26917](https://github.com/open-webui/open-webui/issues/26917)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F513 **Single sign-on after a key rotation.** Signing in with OIDC
      now recovers when the provider rotates its signing key, refreshing the cached
      keys and retrying instead of failing with an invalid credentials error. [#27310](https://github.com/open-webui/open-webui/pull/27310),
      [#26407](https://github.com/open-webui/open-webui/issues/26407)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4BE **Errors kept after reloading.** An error that ends a streamed
      reply is now saved to the conversation, so it is still there when you reload
      instead of disappearing. [#27365](https://github.com/open-webui/open-webui/pull/27365),
      [#27074](https://github.com/open-webui/open-webui/issues/27074)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4AC **Readable error messages.** Errors in a conversation now always
      show readable text that wraps instead of running off the edge, including errors
      that arrive wrapped inside another error."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5D2️ **Readable audit log bodies.** Audit logs that record response
      bodies now store them as readable text instead of compressed data, so entries
      are legible whenever a browser requested compression. [#27369](https://github.com/open-webui/open-webui/pull/27369)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⏱️ **Accurate request timing header.** The processing time reported on
      each response now includes fractions of a second instead of rounding everything
      under a second down to zero. [#27368](https://github.com/open-webui/open-webui/pull/27368)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4C5 **Calendar invitation responses.** Whether you have accepted
      an invitation is now decided by your own response rather than by whoever created
      the event, and invitations you decline disappear from your calendar. [#27007](https://github.com/open-webui/open-webui/pull/27007)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4C5 **One calendar event stalling the server.** Working out when
      a repeating event happens next now walks its rule once rather than re-counting
      from the beginning for every occurrence, so an event repeating every minute
      from an old start date can no longer occupy the server for everyone. [#27468](https://github.com/open-webui/open-webui/pull/27468)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: '⚠️ **Database Migrations**: This release includes database schema changes;
      we strongly recommend backing up your database and all associated data before
      upgrading in production environments. If you are running a multi-worker, multi-server,
      or load-balanced deployment, all instances must be updated simultaneously, rolling
      updates are not supported and will cause application failures due to schema
      incompatibility.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9F3 **The \"python-jose\" library is no longer installed.** Nothing
      in Open WebUI imports it anymore, so it and the two packages it pulled in have
      been dropped from the image, and any tool or function that imports it directly
      now needs to install it itself. [#27444](https://github.com/open-webui/open-webui/pull/27444)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 42-other-changes-in-v0-11-0
  source_release: open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f
  source_type: github_releases
  theme: uncategorized
  title: 42 other changes in v0.11.0
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f]]'
source_type: github_releases
theme: uncategorized
title: 42 other changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 42 other changes in v0.11.0

**Open WebUI** · 2026-07-27 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) · from [[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📌 **Pin the conversation map.** The chat overview now has a pin control that stops it recentring on the newest message, so you can keep looking at the branch you were reading while a reply comes in. [#25736](https://github.com/open-webui/open-webui/pull/25736)

> ⌨️ **Turn keyboard shortcuts off.** A new switch in the keyboard settings disables every configurable shortcut and hides its hint, so combinations that clash with your browser or operating system pass straight through. [#27300](https://github.com/open-webui/open-webui/pull/27300), [#1008](https://github.com/open-webui/open-webui/issues/1008)

> 🪧 **Group names in forwarded headers.** Custom headers on a connection can now carry the groups a person belongs to, by name or by id, so an upstream service or gateway can apply its own rules per group. [#27236](https://github.com/open-webui/open-webui/pull/27236), [#26834](https://github.com/open-webui/open-webui/issues/26834)

> 📑 **Cheaper audit logging.** With audit logging on, each request is no longer authenticated a second time just to record the log entry, so audited instances carry noticeably less overhead. [#27373](https://github.com/open-webui/open-webui/pull/27373)

> 🛢️ **Less database overhead per request.** SQLite installations no longer run a connection check before every database call, and requests that never touch the database skip the bookkeeping that used to run regardless. [#27385](https://github.com/open-webui/open-webui/pull/27385)

> 🦙 **Fewer settings lookups on Ollama requests.** Ollama chat, generation and embedding requests now read their connection settings once instead of up to four times, so each request reaches the server sooner. [#27226](https://github.com/open-webui/open-webui/pull/27226)

> 🚄 **Leaner passthrough streaming.** Responses the server only relays now go straight through in whole network reads instead of being split line by line, roughly halving the work spent shuttling a streamed reply on those routes. [#27384](https://github.com/open-webui/open-webui/pull/27384)

> 🧶 **Web page parsing off the critical path.** Reading those pages no longer holds up everything else on the server, so other people's replies, live updates and health checks keep flowing during a search instead of stalling for a second or more. [#27446](https://github.com/open-webui/open-webui/pull/27446)

> 🌐 **Translation updates.** Slovenian is now available, and translations for English (UK), Finnish, German, Japanese, Portuguese (Brazil) and Portuguese (Portugal) were enhanced and expanded.

> 🎟️ **Ollama version no longer readable anonymously.** Reading the configured Ollama backend's version now requires signing in, closing a route that let anyone learn the version in use and count how many backends are configured. [#27199](https://github.com/open-webui/open-webui/pull/27199)

> 🛎️ **Stopping someone else's generation.** Deleting a chat now checks who you are before anything is cancelled, so knowing another person's chat id no longer lets you cut off their reply or title generation on a request that is refused anyway. [#27006](https://github.com/open-webui/open-webui/pull/27006)

> ⏲️ **Cancelling someone else's timers.** Marking a chat as read now only clears your own pending timers on it, instead of clearing everyone's, which had let another person's scheduled prompt be silently cancelled without them being told. [#27472](https://github.com/open-webui/open-webui/pull/27472)

> 📕 **Tool source shown to people who can only use it.** Opening a tool you were given read access to no longer returns its source code, which read access was never meant to include. [#27005](https://github.com/open-webui/open-webui/pull/27005)

> 🧺 **Knowledge base cleanup reaching other collections.** Tidying up a knowledge base now acts only on files and folders that belong to it, so someone with write access to one knowledge base can no longer delete folders or search data belonging to another. [#26722](https://github.com/open-webui/open-webui/pull/26722)

> ⌛ **Searches that could stall the server.** A search pattern inside knowledge base commands now runs under a time budget, so a pattern that would take minutes to evaluate can no longer hold up everyone else on the instance. [#27471](https://github.com/open-webui/open-webui/pull/27471)

> 📓 **Notes in folder knowledge are access checked.** Notes attached to a folder are now filtered against your own access before the list reaches the assistant, rather than relying on later checks further along. [#26739](https://github.com/open-webui/open-webui/pull/26739)

> 📃 **Action functions receive the response text.** Running an action on a response now passes the assistant's text to the function, instead of handing it an empty message. [#26798](https://github.com/open-webui/open-webui/pull/26798), [#26672](https://github.com/open-webui/open-webui/issues/26672)

> 🔌 **Dropped sessions during keepalive.** Live connections no longer break on a routine keepalive check, which had cut the session so that anything the server needed to run in your browser failed afterwards, most visibly the code execution tool reporting the client as disconnected on every run. [#27553](https://github.com/open-webui/open-webui/pull/27553), [#27550](https://github.com/open-webui/open-webui/issues/27550)

> ⬅️ **Back button after opening admin or workspace.** Going back in the browser now returns you to the page you came from, instead of being pushed forward again to where you just were. [#27478](https://github.com/open-webui/open-webui/pull/27478), [#27477](https://github.com/open-webui/open-webui/issues/27477)

> 🥄 **Counting matches in knowledge base commands.** Piping text into a search inside knowledge base commands now honours the count and filenames-only flags, instead of returning the matching lines regardless. [#26721](https://github.com/open-webui/open-webui/pull/26721), [#26715](https://github.com/open-webui/open-webui/issues/26715)

> 📧 **Outlook message uploads.** Uploading a .msg email now works, where it previously failed because the package it relied on could not be installed alongside the rest of the application at all. [#26704](https://github.com/open-webui/open-webui/pull/26704), [#26690](https://github.com/open-webui/open-webui/issues/26690)

> 🚧 **Quoted entries in the web fetch filter list.** Stray quote marks around a filter entry, which Docker Compose passes through literally, no longer turn the list into one that blocks every web address. [#26910](https://github.com/open-webui/open-webui/pull/26910), [#26908](https://github.com/open-webui/open-webui/issues/26908)

> 🕸️ **Mixed web page extraction.** Fetching several web pages at once now reads each one according to its own format, instead of applying the first page's format to the whole batch and garbling the rest. [#27367](https://github.com/open-webui/open-webui/pull/27367)

> 🧯 **Leftover browser sessions on web fetches.** Fetching pages through a remote Playwright server now closes each page and the browser even when a page times out or the search is abandoned partway, instead of leaving sessions open and slowing every later search until that server was restarted. [#27526](https://github.com/open-webui/open-webui/pull/27526), [#25880](https://github.com/open-webui/open-webui/issues/25880)

> 🔊 **Text-to-speech reliability.** Text-to-speech playback and other streamed responses no longer intermittently cut out partway through when several requests run at once. [#26924](https://github.com/open-webui/open-webui/pull/26924), [#26922](https://github.com/open-webui/open-webui/issues/26922)

> 📨 **Non-streaming requests to strict providers.** A request that is not streaming no longer carries the streaming-only usage option, which some providers reject outright.

> 🪝 **Tool calls with structured arguments.** A provider that sends a tool call's arguments as an object, or as nothing at all, no longer breaks the reply partway through. [#27195](https://github.com/open-webui/open-webui/issues/27195)

> 🩹 **Startup with an ownerless tool or function.** A tool or function left without an owner no longer prevents the application from starting, which had blocked all chat responses until it was removed. [#26850](https://github.com/open-webui/open-webui/pull/26850), [#26843](https://github.com/open-webui/open-webui/issues/26843)

> 🗃️ **Milvus Lite collection creation.** Setting up collections now succeeds on embedded Milvus Lite, which previously could fail while creating the resource index. [#26911](https://github.com/open-webui/open-webui/pull/26911)

> 🧽 **Milvus log noise.** Instances backed by Milvus no longer fill their logs with deprecation warnings while indexing and retrieving, and keep working with future PyMilvus releases that drop the old interface entirely. [#27521](https://github.com/open-webui/open-webui/pull/27521), [#26978](https://github.com/open-webui/open-webui/issues/26978)

> 🔦 **Connections on hardened instances.** With the admin access bypass turned off, a connection that has no access grants yet is now reachable by administrators again, instead of being hidden from everyone including the admin who created it. [#27581](https://github.com/open-webui/open-webui/pull/27581), [#27580](https://github.com/open-webui/open-webui/issues/27580), [#27064](https://github.com/open-webui/open-webui/issues/27064)

> 🪛 **Deleting an Ollama connection.** Removing an Ollama connection now saves straight away, instead of reappearing until the Ollama API switch was toggled afterwards. [#27483](https://github.com/open-webui/open-webui/pull/27483), [#27482](https://github.com/open-webui/open-webui/issues/27482)

> 🔧 **Sign-on settings from environment variables.** Single sign-on settings supplied through environment variables are no longer overridden by stale values saved at first startup, so changing them takes effect. [#26928](https://github.com/open-webui/open-webui/pull/26928), [#26917](https://github.com/open-webui/open-webui/issues/26917)

> 🔓 **Single sign-on after a key rotation.** Signing in with OIDC now recovers when the provider rotates its signing key, refreshing the cached keys and retrying instead of failing with an invalid credentials error. [#27310](https://github.com/open-webui/open-webui/pull/27310), [#26407](https://github.com/open-webui/open-webui/issues/26407)

> 💾 **Errors kept after reloading.** An error that ends a streamed reply is now saved to the conversation, so it is still there when you reload instead of disappearing. [#27365](https://github.com/open-webui/open-webui/pull/27365), [#27074](https://github.com/open-webui/open-webui/issues/27074)

> 💬 **Readable error messages.** Errors in a conversation now always show readable text that wraps instead of running off the edge, including errors that arrive wrapped inside another error.

> 🗒️ **Readable audit log bodies.** Audit logs that record response bodies now store them as readable text instead of compressed data, so entries are legible whenever a browser requested compression. [#27369](https://github.com/open-webui/open-webui/pull/27369)

> ⏱️ **Accurate request timing header.** The processing time reported on each response now includes fractions of a second instead of rounding everything under a second down to zero. [#27368](https://github.com/open-webui/open-webui/pull/27368)

> 📅 **Calendar invitation responses.** Whether you have accepted an invitation is now decided by your own response rather than by whoever created the event, and invitations you decline disappear from your calendar. [#27007](https://github.com/open-webui/open-webui/pull/27007)

> 📅 **One calendar event stalling the server.** Working out when a repeating event happens next now walks its rule once rather than re-counting from the beginning for every occurrence, so an event repeating every minute from an old start date can no longer occupy the server for everyone. [#27468](https://github.com/open-webui/open-webui/pull/27468)

> ⚠️ **Database Migrations**: This release includes database schema changes; we strongly recommend backing up your database and all associated data before upgrading in production environments. If you are running a multi-worker, multi-server, or load-balanced deployment, all instances must be updated simultaneously, rolling updates are not supported and will cause application failures due to schema incompatibility.

> 🧳 **The "python-jose" library is no longer installed.** Nothing in Open WebUI imports it anymore, so it and the two packages it pulled in have been dropped from the image, and any tool or function that imports it directly now needs to install it itself. [#27444](https://github.com/open-webui/open-webui/pull/27444)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-27-9-automation-and-scheduling-changes-in-v0-11-0|9 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-27-4-voice-and-audio-changes-in-v0-11-0|4 Voice and Audio changes in v0.11.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer Workflow changes in v0.11.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-27-19-interface-experience-changes-in-v0-11-0|19 Interface Experience changes in v0.11.0]] · Interface Experience
- [[Changes/Open WebUI/2026-07-27-7-memory-and-personalization-changes-in-v0-11-0|7 Memory and Personalization changes in v0.11.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|🤖 Sub-agents. Administrators can now enable sub-agents, which let a model hand…]] · Agent Mode
- [[Changes/Open WebUI/2026-07-27-media-types-an-extraction-engine-may-handle-administrators-can-now-list-which-im|🖼️ Media types an extraction engine may handle. Administrators can now list…]] · Multimodal Input
- [[Changes/Open WebUI/2026-07-27-15-account-and-access-changes-in-v0-11-0|15 Account and Access changes in v0.11.0]] · Account and Access
- [[Changes/Open WebUI/2026-07-27-shared-image-checkpoint-changes-only-administrators-can-now-change-the-instance|🖌️ Shared image checkpoint changes. Only administrators can now change…]] · Image Generation
- [[Changes/Open WebUI/2026-07-27-7-search-and-browsing-changes-in-v0-11-0|7 Search and Browsing changes in v0.11.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-07-27-2-collaboration-changes-in-v0-11-0|2 Collaboration changes in v0.11.0]] · Collaboration
- [[Changes/Open WebUI/2026-07-27-6-apps-and-integrations-changes-in-v0-11-0|6 Apps and Integrations changes in v0.11.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-07-27-3-enterprise-and-administration-changes-in-v0-11-0|3 Enterprise and Administration changes in v0.11.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-07-27-9-context-window-changes-in-v0-11-0|9 Context Window changes in v0.11.0]] · Context Window
- [[Changes/Open WebUI/2026-07-27-12-reliability-and-performance-changes-in-v0-11-0|12 Reliability and Performance changes in v0.11.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-07-27-2-pricing-model-changes-in-v0-11-0|2 Pricing Model changes in v0.11.0]] · Pricing Model
- [[Changes/Open WebUI/2026-07-27-9-files-and-data-changes-in-v0-11-0|9 Files and Data changes in v0.11.0]] · Files and Data
- [[Changes/Open WebUI/2026-07-27-39-model-support-changes-in-v0-11-0|39 Model Support changes in v0.11.0]] · Model Support
- [[Changes/Open WebUI/2026-07-27-7-editor-experience-changes-in-v0-11-0|7 Editor Experience changes in v0.11.0]] · Editor Experience
- [[Changes/Open WebUI/2026-07-27-2-mobile-and-desktop-changes-in-v0-11-0|2 Mobile and Desktop changes in v0.11.0]] · Mobile and Desktop
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-27-a63db5&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-27-42-other-changes-in-v0-11-0.md%0ACard%20ID%3A%20open-webui-2026-07-27-a63db5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->