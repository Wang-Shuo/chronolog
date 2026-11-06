---
card_id: open-webui-2026-10-10-e0fce3
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Other changes: 68 changes in v0.12.0 — \U0001F310
  **Translation updates.** Translations for German, Italian, Turkish, Persian, Indonesian…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a14c906d333ff0b2f35add1e2c34cd5e9901e2d820bda76d833bf8378a47e4a6
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-e0fce3
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 68 other changes'
  evidence:
  - quote: "\U0001F310 **Translation updates.** Translations for German, Italian,
      Turkish, Persian, Indonesian, Catalan, French, Malay, Simplified Chinese, Hindi,
      Japanese, Romanian, Czech, Slovenian, Croatian, Slovak, Dutch, Hungarian, Tamil,
      Spanish, Vietnamese, Norwegian Bokmål, Hebrew, Greek, Lithuanian, Korean, Canadian
      French, Swedish, Portuguese (Portugal), Brazilian Portuguese, Thai, Estonian,
      Russian, Bosnian, Ukrainian, Basque, Bulgarian, Azerbaijani, Danish, Irish,
      Finnish, Bengali, Latvian, Traditional Chinese, Polish, Georgian and Galician
      were enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F465 **Direct message members.** The person who started a direct
      message can no longer add or remove people through the API, where someone added
      this way could read the whole earlier conversation and the original pair ended
      up in a second, empty direct message. [#31575](https://github.com/open-webui/open-webui/pull/31575),
      [#31570](https://github.com/open-webui/open-webui/issues/31570)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9FE **Passwords kept out of the audit log.** With request auditing
      on, every field whose name ends in \"password\" is now masked in both logged
      requests and logged responses, including admin settings such as YaCy, Jupyter
      and the LDAP Application DN Password, and passwords containing a double quote,
      where only fields named exactly \"password\" in requests were masked and only
      up to the first quote. [#31622](https://github.com/open-webui/open-webui/pull/31622),
      [#31659](https://github.com/open-webui/open-webui/pull/31659)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6AA **Removed channel members stop receiving messages.** Removing
      someone from a group channel now also disconnects their open sessions from it,
      so they stop receiving its live messages right away. [#30446](https://github.com/open-webui/open-webui/pull/30446)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5DD️ **Stronger generated secret key.** The secret key Open WebUI
      generates when \"WEBUI_SECRET_KEY\" is not set now comes from a cryptographically
      secure random source. [#30441](https://github.com/open-webui/open-webui/pull/30441)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F40C **Wildcard searches on SQLite.** Searches on SQLite can no
      longer tie up the server with a search term full of wildcards, which could make
      matching take exponentially long. [#30393](https://github.com/open-webui/open-webui/pull/30393)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F300 **Message cleanup for background tasks.** Cleaning details
      blocks and images out of messages before titles, tags and follow-ups are generated
      can no longer stall on crafted message content. [#30394](https://github.com/open-webui/open-webui/pull/30394)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F517 **Only safe file links open.** File attachment links and file
      links in code execution results now open only web, mail, phone and relative
      links, the same check links in chat messages go through. [#31491](https://github.com/open-webui/open-webui/pull/31491)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4C6 **Calendar tools check calendar access.** Editing or deleting
      a calendar event through the chat tools now checks access to the event's calendar
      the same way the calendar API does. [#31537](https://github.com/open-webui/open-webui/pull/31537)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5E3️ **Interface language detection.** Browsers reporting a bare
      or regional language code, such as German, Dutch or Polish in Firefox and Japanese
      or Latin American Spanish in Chrome, get the matching translation again, where
      0.11.4 fell back to English. [#30377](https://github.com/open-webui/open-webui/pull/30377)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5E3️ **System prompt after a tool approval.** With tool approval
      set to ask, the request sent after approving a tool call now carries the system
      prompt and, in a compacted chat, the conversation summary instead of the whole
      history, taking the prompt from the chat Controls, then your personal settings,
      then the admin default; a system prompt sent only in an API request is still
      not kept. [#31501](https://github.com/open-webui/open-webui/pull/31501), [#31499](https://github.com/open-webui/open-webui/issues/31499)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9EF **Responses API errors kept.** Errors from providers on connections
      set to the Responses API now appear in the chat and are still there after a
      reload, where some never showed at all and others vanished and left an empty
      reply. [#31439](https://github.com/open-webui/open-webui/pull/31439), [#31433](https://github.com/open-webui/open-webui/issues/31433)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F514 **Webhook chat links.** The link in \"chat finished\" and \"chat
      failed\" webhook notifications opens the chat again, where the missing \"/c/\"
      part of the address led to a 404 page. [#31572](https://github.com/open-webui/open-webui/pull/31572),
      [#31565](https://github.com/open-webui/open-webui/issues/31565)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4DD **Cleared chat system prompt.** Clearing a chat's own system
      prompt now falls back to your personal system prompt, where the chat was previously
      sent no system prompt at all. [#30333](https://github.com/open-webui/open-webui/pull/30333)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F30A **Per-chat streaming setting.** A chat's own Stream Chat Response
      setting in Controls now takes effect, where it was ignored whenever the account-wide
      setting was set. [#31362](https://github.com/open-webui/open-webui/pull/31362),
      [#31361](https://github.com/open-webui/open-webui/issues/31361)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4EC **Send queue recovers.** Deleting or editing a queued message
      held back by a failed attachment now lets the rest of the queue send, where
      the chat's queue previously stayed stuck until the chat was reopened. [#30447](https://github.com/open-webui/open-webui/pull/30447),
      [#28880](https://github.com/open-webui/open-webui/issues/28880)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3C5 **Copied replies start unrated.** A reply saved as a copy no
      longer carries over the original's rating, so rating the copy no longer overwrites
      the original's feedback. [#30962](https://github.com/open-webui/open-webui/pull/30962),
      [#30961](https://github.com/open-webui/open-webui/issues/30961)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3AD **Artifacts pane after deleting a message.** Deleting the message
      holding the newest artifact while the artifacts pane shows it now moves the
      pane to the last remaining artifact, where it kept showing the deleted one with
      wrong version numbers. [#30435](https://github.com/open-webui/open-webui/pull/30435),
      [#30287](https://github.com/open-webui/open-webui/issues/30287)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F50C **Deleting a direct connection sticks.** Deleting one of your
      own direct connections in Settings is now saved right away, where it came back
      after a reload unless you also pressed Save. [#31384](https://github.com/open-webui/open-webui/pull/31384),
      [#31383](https://github.com/open-webui/open-webui/issues/31383)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9F9 **Add Connection form reset.** Adding several connections in
      a row no longer silently saves the advanced settings of the first one, such
      as its headers, provider and API type, with the next. [#30958](https://github.com/open-webui/open-webui/pull/30958),
      [#30957](https://github.com/open-webui/open-webui/issues/30957)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ⌨️ **Ctrl+Enter to Send in channels.** With "Ctrl+Enter to Send" turned
      on, Enter in a channel or thread reply now starts a new line and Ctrl+Enter
      sends, where Enter always sent the message. [#31319](https://github.com/open-webui/open-webui/pull/31319),
      [#31318](https://github.com/open-webui/open-webui/issues/31318)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3F7️ **Tags after bulk chat actions.** Unarchiving all chats now
      brings their tags back, and deleting all chats removes tags no longer used by
      any chat from the suggestions. [#30453](https://github.com/open-webui/open-webui/pull/30453),
      [#30452](https://github.com/open-webui/open-webui/issues/30452)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ⌨️ **Enter after a smiley.** Pressing Enter now sends a message that ends
      in a smiley such as ":)" or in a word starting with ":", "/" or "#", where it
      did nothing because an empty suggestion list still held on to the key. [#31506](https://github.com/open-webui/open-webui/pull/31506),
      [#31504](https://github.com/open-webui/open-webui/issues/31504)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F50E **Hybrid search on large Chroma collections.** Hybrid search
      over a knowledge base of more than about 32,000 chunks stored in Chroma now
      returns results, where it previously failed with \"Error querying knowledge
      base\". [#30368](https://github.com/open-webui/open-webui/pull/30368), [#30351](https://github.com/open-webui/open-webui/issues/30351)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9ED **Qdrant strict mode.** File uploads and hybrid search now
      work on Qdrant with strict mode enabled, where every upload after the first
      failed with \"Limit exceeded\" and hybrid search found nothing, and hybrid search
      now falls back to normal vector search whenever a collection cannot be read.
      [#31461](https://github.com/open-webui/open-webui/pull/31461), [#31460](https://github.com/open-webui/open-webui/pull/31460),
      [#31459](https://github.com/open-webui/open-webui/issues/31459)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F524 **Korean and Japanese text files.** Korean and Japanese text
      files in legacy encodings such as EUC-KR and Shift-JIS are now read correctly
      for chats and knowledge bases, where they were stored as garbled Chinese characters.
      [#31356](https://github.com/open-webui/open-webui/pull/31356), [#31352](https://github.com/open-webui/open-webui/issues/31352)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9F5 **Backslashes in HTML uploads.** Uploaded HTML files now keep
      their backslashes as written, where a path such as \"C:\\new\\table\" gained
      line breaks and one containing \"C:\\Users\" failed to upload. [#31450](https://github.com/open-webui/open-webui/pull/31450),
      [#31440](https://github.com/open-webui/open-webui/issues/31440)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F578️ **Unreachable links named.** Attaching or adding a link that
      cannot be fetched, such as one whose server refuses the connection or returns
      an error page, now reports \"Could not read content from\" the link instead
      of a vague processing or knowledge base error. [#31351](https://github.com/open-webui/open-webui/pull/31351),
      [#31354](https://github.com/open-webui/open-webui/pull/31354), [#31347](https://github.com/open-webui/open-webui/issues/31347)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F465 **Admin user chat list after deletion.** Deleting a chat from
      a user's chat list in the admin panel no longer leaves the list empty. [#30604](https://github.com/open-webui/open-webui/pull/30604),
      [#30601](https://github.com/open-webui/open-webui/issues/30601)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4C7 **User CSV import blank line.** Importing users from a CSV
      file that ends with a line break no longer reports the empty last line as an
      invalid row. [#31374](https://github.com/open-webui/open-webui/pull/31374),
      [#31373](https://github.com/open-webui/open-webui/issues/31373)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4C5 **Calendar event end moves with its date.** Changing a calendar
      event's date now moves its end along with it, where the end kept its old date
      and events could span several days or lose their duration. [#31303](https://github.com/open-webui/open-webui/pull/31303),
      [#31302](https://github.com/open-webui/open-webui/issues/31302)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F502 **Repeating events that started earlier.** A repeating calendar
      event that is still running when the visible dates begin, such as a weekly event
      from 23:00 to 01:00, now shows on the following day, where only the same event
      without a repeat did. [#31606](https://github.com/open-webui/open-webui/pull/31606),
      [#31605](https://github.com/open-webui/open-webui/issues/31605)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4CB **Copy buttons in account settings.** Copying your token or
      API key in the account settings no longer also saves the account form and any
      unsaved profile changes along with it. [#30956](https://github.com/open-webui/open-webui/pull/30956),
      [#30955](https://github.com/open-webui/open-webui/issues/30955)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4E8 **Anthropic Messages endpoint with empty tools.** Requests
      to the Anthropic-compatible Messages endpoint that send an empty or null tools
      list, as Claude Code does for text-only requests, no longer fail against backends
      such as vLLM and OpenAI. [#31343](https://github.com/open-webui/open-webui/pull/31343),
      [#31341](https://github.com/open-webui/open-webui/issues/31341)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6A7 **Failed streams on the Anthropic Messages endpoint.** A streamed
      request to the Anthropic-compatible Messages endpoint that fails partway now
      ends with an error, so clients such as Claude Code no longer take the cut-off
      answer as complete. [#31405](https://github.com/open-webui/open-webui/pull/31405),
      [#31403](https://github.com/open-webui/open-webui/issues/31403)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F550 **Group filter on the hourly analytics chart.** The analytics
      chart for the last 24 hours now respects the selected group, where it counted
      every user's messages while the rest of the page was filtered. [#30978](https://github.com/open-webui/open-webui/pull/30978),
      [#30977](https://github.com/open-webui/open-webui/issues/30977)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4DC **Title generation log noise.** Starting a new chat no longer
      writes a misleading \"Error generating initial chat title\" traceback to the
      server log. [#30356](https://github.com/open-webui/open-webui/pull/30356), [#30339](https://github.com/open-webui/open-webui/issues/30339)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F30A **Code blocks fenced with tildes.** Code blocks fenced with
      ~~~ now show as code blocks with their language label and Copy button, where
      they were shown as a single line of plain text. [#31543](https://github.com/open-webui/open-webui/pull/31543),
      [#31542](https://github.com/open-webui/open-webui/issues/31542)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5FA️ **DEFAULT_LOCALE on the first visit.** A new visitor now gets
      the language set in \"DEFAULT_LOCALE\" again, where since 0.11.4 they always
      got their browser's language; a language picked in Settings or a ?lang= link
      still takes precedence. [#31551](https://github.com/open-webui/open-webui/pull/31551),
      [#31548](https://github.com/open-webui/open-webui/issues/31548)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4CB **Multi-line table cells in notes.** A note table cell with
      more than one line now stays inside its row in the note's Markdown download
      and its Chat panel, where the second line broke the row and shifted cells into
      other columns. [#31539](https://github.com/open-webui/open-webui/pull/31539),
      [#31538](https://github.com/open-webui/open-webui/issues/31538)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3AF **Exact matches on Weaviate.** With Weaviate, a chunk identical
      to the query now scores 1 instead of 0, so perfect matches no longer land at
      the bottom of the results or fall below the relevance threshold. [#31531](https://github.com/open-webui/open-webui/pull/31531),
      [#31527](https://github.com/open-webui/open-webui/issues/31527)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4CD **Unpinning folder chats by dragging.** Dragging a pinned chat
      out of a folder onto Chats now unpins it, where it stayed pinned. [#31368](https://github.com/open-webui/open-webui/pull/31368),
      [#31367](https://github.com/open-webui/open-webui/issues/31367)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F50D **New chat from the search dialog.** Starting a new conversation
      from the search dialog now sends the typed text unchanged, where everything
      from a # or & on was dropped and + turned into a space. [#31592](https://github.com/open-webui/open-webui/pull/31592),
      [#31469](https://github.com/open-webui/open-webui/issues/31469)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4C8 **OpenTelemetry logs sent once.** With \"ENABLE_OTEL\", \"ENABLE_OTEL_TRACES\"
      and \"ENABLE_OTEL_LOGS\" all on, each log line now reaches the collector once
      instead of twice, so \"OTEL_PYTHON_LOG_AUTO_INSTRUMENTATION=false\" is no longer
      needed as a workaround. [#31528](https://github.com/open-webui/open-webui/pull/31528),
      [#31524](https://github.com/open-webui/open-webui/issues/31524)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4CE **Large pastes in channels.** With Paste Large Text as File
      on, pasting more than 1,000 characters into a channel or thread now attaches
      it as a text file, where the text vanished. [#31366](https://github.com/open-webui/open-webui/pull/31366),
      [#31365](https://github.com/open-webui/open-webui/issues/31365)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FAA2 **SCIM group member links.** Members in SCIM group responses
      now carry the link to their user, where every member came back with \"$ref\":
      null. [#31529](https://github.com/open-webui/open-webui/pull/31529), [#31525](https://github.com/open-webui/open-webui/issues/31525)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9E9 **Tool HTML embeds with entities.** HTML embeds, arguments
      and file links from tools now show exactly what the tool returned, where an
      embed containing an entity such as &quot; did not show at all and &amp; or &lt;
      were turned into real characters. [#31390](https://github.com/open-webui/open-webui/pull/31390),
      [#28085](https://github.com/open-webui/open-webui/issues/28085)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ↩️ **Pending reply when switching channels.** Switching to another channel
      now drops a reply you had started, where it carried over, failed to send and
      left a faded copy behind. [#31376](https://github.com/open-webui/open-webui/pull/31376),
      [#31375](https://github.com/open-webui/open-webui/issues/31375)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3A8 **Invalid image Additional Parameters.** Saving the Images
      settings with invalid JSON in the Additional Parameters for OpenAI or AUTOMATIC1111
      now shows an error, where Save kept spinning. [#31382](https://github.com/open-webui/open-webui/pull/31382),
      [#31381](https://github.com/open-webui/open-webui/issues/31381)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ♻️ **Editing a repeating event from a later occurrence.** Opening a repeating
      calendar event from a later occurrence and saving it now keeps the series' own
      start date, where it moved the start to the clicked occurrence and deleted every
      earlier one. [#30971](https://github.com/open-webui/open-webui/pull/30971),
      [#30970](https://github.com/open-webui/open-webui/issues/30970)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4AC **Readable mention notifications.** Notifications for channel
      messages that mention a user or channel now show the mention as it appears in
      the channel, such as \"@ Alex\", where they showed the raw mention markup with
      the internal id. [#31601](https://github.com/open-webui/open-webui/pull/31601),
      [#31586](https://github.com/open-webui/open-webui/issues/31586)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3B9 **Enter in the search dialog.** Pressing Enter on a highlighted
      chat in the search dialog now opens it, where the dialog only closed. [#31004](https://github.com/open-webui/open-webui/pull/31004),
      [#31003](https://github.com/open-webui/open-webui/issues/31003)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9FA **Edited knowledge files on Elasticsearch.** With Elasticsearch
      as the vector database, editing a knowledge file now removes its old text from
      search, where chats and searches kept returning the old text next to the new.
      [#31530](https://github.com/open-webui/open-webui/pull/31530), [#31523](https://github.com/open-webui/open-webui/issues/31523)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F418 **External pgvector knowledge bases.** External knowledge bases
      on the pgvector provider return results again, where every search failed with
      \"operator does not exist: vector <=> double precision[]\" and the knowledge
      base looked empty. [#31112](https://github.com/open-webui/open-webui/pull/31112),
      [#26663](https://github.com/open-webui/open-webui/issues/26663)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F46F **Duplicate files in knowledge batch add.** Adding files to
      a knowledge base in a batch now rejects a file whose text is already in it,
      the same way adding a single file does, where the same text was embedded twice
      and retrieval returned the same passages twice. [#31336](https://github.com/open-webui/open-webui/pull/31336),
      [#31333](https://github.com/open-webui/open-webui/issues/31333)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ⏳ **Older unfinished responses no longer spin forever.** Opening a chat
      with no generation running now shows every unfinished response as finished,
      with its copy and regenerate buttons, where only the newest one was repaired
      and older ones from cancelled or interrupted generations kept a loading cursor
      forever; responses waiting for the user to answer a tool's question are left
      as they are. [#31895](https://github.com/open-webui/open-webui/pull/31895),
      [#14806](https://github.com/open-webui/open-webui/issues/14806)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ➗ **Inline math next to dashes.** Inline math written directly next to
      an em dash or en dash, with either $...$ or \(...\), now renders in chat replies
      instead of showing as plain text. [#31901](https://github.com/open-webui/open-webui/pull/31901)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6CE️ **Ctrl+Shift+Enter with Ctrl+Enter to Send.** With \"Ctrl+Enter
      to Send\" on, Ctrl+Shift+Enter now only adds an empty message pair, where it
      also sent the typed message. [#31864](https://github.com/open-webui/open-webui/pull/31864),
      [#31468](https://github.com/open-webui/open-webui/issues/31468)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F50D **Edited replies stay searchable.** Chats can now be found
      in search by the new text of an edited reply, where editing a reply made it
      unsearchable by both its old and new text. [#31844](https://github.com/open-webui/open-webui/pull/31844),
      [#31471](https://github.com/open-webui/open-webui/issues/31471)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4E7 **Pasted emails sent once.** With Rich Text Input for Chat
      on, pasting an HTML email or newsletter laid out with nested tables no longer
      sends the same text repeated many times. [#31890](https://github.com/open-webui/open-webui/pull/31890),
      [#24657](https://github.com/open-webui/open-webui/issues/24657)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4CA **Daily Messages chart on All time.** The Daily Messages chart
      in Analytics now loads on All time when a message was saved without a timestamp,
      and messages after such a message in the same chat are counted again. [#31888](https://github.com/open-webui/open-webui/pull/31888),
      [#27316](https://github.com/open-webui/open-webui/issues/27316)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ↔️ **Mixed right-to-left and left-to-right lines.** Each line of a message
      now gets its own text direction and alignment, both while typing and in the
      sent message, so an English line under an Arabic one no longer shows its punctuation
      on the wrong side. [#31868](https://github.com/open-webui/open-webui/pull/31868),
      [#31827](https://github.com/open-webui/open-webui/issues/31827)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F69B **Large files on Milvus.** With Milvus as the vector database,
      large files now finish processing instead of failing with a RESOURCE_EXHAUSTED
      error after the whole embedding step, because their chunks are sent to Milvus
      in batches of 128 rather than in one request that exceeded its size limit, with
      and without multitenancy mode. [#31990](https://github.com/open-webui/open-webui/pull/31990),
      [#31989](https://github.com/open-webui/open-webui/issues/31989)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F370 **Partial files in knowledge bases on Qdrant.** On Qdrant,
      a file uploaded to a knowledge base or edited there now always arrives with
      all of its content, where it could end up with only part of its chunks, often
      exactly 64, while showing as completed; file processing on a busy Qdrant may
      take a little longer since each save now waits for Qdrant to finish storing.
      [#31961](https://github.com/open-webui/open-webui/pull/31961), [#31959](https://github.com/open-webui/open-webui/issues/31959)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FA79 **Chats right after a Redis restart.** After Redis restarts
      or closes its connections, Open WebUI now reconnects and retries the call once,
      so chat requests no longer fail with a 500 error and newly opened tabs get live
      updates again as soon as Redis is back. [#31619](https://github.com/open-webui/open-webui/pull/31619)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9EE **Deeply nested chat variable values.** A chat variable property
      whose value is deeply nested JSON is now kept as plain text, where it could
      make the request fail. [#30389](https://github.com/open-webui/open-webui/pull/30389)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5C3️ **Back and Forward between folder pages.** Going Back or Forward
      from one folder page to another now shows the folder named in the address bar,
      where the page kept showing the folder you had left. [#32146](https://github.com/open-webui/open-webui/pull/32146),
      [#32144](https://github.com/open-webui/open-webui/issues/32144)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: Release notes shortened. [Read the full changelog](https://github.com/open-webui/open-webui/blob/f8ae8a6c328946dc62cd0712961a0632574581bf/CHANGELOG.md).
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 68-other-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: uncategorized
  title: 68 other changes in v0.12.0
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: uncategorized
title: 68 other changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 68 other changes in v0.12.0

**Open WebUI** · 2026-10-10 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🌐 **Translation updates.** Translations for German, Italian, Turkish, Persian, Indonesian, Catalan, French, Malay, Simplified Chinese, Hindi, Japanese, Romanian, Czech, Slovenian, Croatian, Slovak, Dutch, Hungarian, Tamil, Spanish, Vietnamese, Norwegian Bokmål, Hebrew, Greek, Lithuanian, Korean, Canadian French, Swedish, Portuguese (Portugal), Brazilian Portuguese, Thai, Estonian, Russian, Bosnian, Ukrainian, Basque, Bulgarian, Azerbaijani, Danish, Irish, Finnish, Bengali, Latvian, Traditional Chinese, Polish, Georgian and Galician were enhanced and expanded.

> 👥 **Direct message members.** The person who started a direct message can no longer add or remove people through the API, where someone added this way could read the whole earlier conversation and the original pair ended up in a second, empty direct message. [#31575](https://github.com/open-webui/open-webui/pull/31575), [#31570](https://github.com/open-webui/open-webui/issues/31570)

> 🧾 **Passwords kept out of the audit log.** With request auditing on, every field whose name ends in "password" is now masked in both logged requests and logged responses, including admin settings such as YaCy, Jupyter and the LDAP Application DN Password, and passwords containing a double quote, where only fields named exactly "password" in requests were masked and only up to the first quote. [#31622](https://github.com/open-webui/open-webui/pull/31622), [#31659](https://github.com/open-webui/open-webui/pull/31659)

> 🚪 **Removed channel members stop receiving messages.** Removing someone from a group channel now also disconnects their open sessions from it, so they stop receiving its live messages right away. [#30446](https://github.com/open-webui/open-webui/pull/30446)

> 🗝️ **Stronger generated secret key.** The secret key Open WebUI generates when "WEBUI_SECRET_KEY" is not set now comes from a cryptographically secure random source. [#30441](https://github.com/open-webui/open-webui/pull/30441)

> 🐌 **Wildcard searches on SQLite.** Searches on SQLite can no longer tie up the server with a search term full of wildcards, which could make matching take exponentially long. [#30393](https://github.com/open-webui/open-webui/pull/30393)

> 🌀 **Message cleanup for background tasks.** Cleaning details blocks and images out of messages before titles, tags and follow-ups are generated can no longer stall on crafted message content. [#30394](https://github.com/open-webui/open-webui/pull/30394)

> 🔗 **Only safe file links open.** File attachment links and file links in code execution results now open only web, mail, phone and relative links, the same check links in chat messages go through. [#31491](https://github.com/open-webui/open-webui/pull/31491)

> 📆 **Calendar tools check calendar access.** Editing or deleting a calendar event through the chat tools now checks access to the event's calendar the same way the calendar API does. [#31537](https://github.com/open-webui/open-webui/pull/31537)

> 🗣️ **Interface language detection.** Browsers reporting a bare or regional language code, such as German, Dutch or Polish in Firefox and Japanese or Latin American Spanish in Chrome, get the matching translation again, where 0.11.4 fell back to English. [#30377](https://github.com/open-webui/open-webui/pull/30377)

> 🗣️ **System prompt after a tool approval.** With tool approval set to ask, the request sent after approving a tool call now carries the system prompt and, in a compacted chat, the conversation summary instead of the whole history, taking the prompt from the chat Controls, then your personal settings, then the admin default; a system prompt sent only in an API request is still not kept. [#31501](https://github.com/open-webui/open-webui/pull/31501), [#31499](https://github.com/open-webui/open-webui/issues/31499)

> 🧯 **Responses API errors kept.** Errors from providers on connections set to the Responses API now appear in the chat and are still there after a reload, where some never showed at all and others vanished and left an empty reply. [#31439](https://github.com/open-webui/open-webui/pull/31439), [#31433](https://github.com/open-webui/open-webui/issues/31433)

> 🔔 **Webhook chat links.** The link in "chat finished" and "chat failed" webhook notifications opens the chat again, where the missing "/c/" part of the address led to a 404 page. [#31572](https://github.com/open-webui/open-webui/pull/31572), [#31565](https://github.com/open-webui/open-webui/issues/31565)

> 📝 **Cleared chat system prompt.** Clearing a chat's own system prompt now falls back to your personal system prompt, where the chat was previously sent no system prompt at all. [#30333](https://github.com/open-webui/open-webui/pull/30333)

> 🌊 **Per-chat streaming setting.** A chat's own Stream Chat Response setting in Controls now takes effect, where it was ignored whenever the account-wide setting was set. [#31362](https://github.com/open-webui/open-webui/pull/31362), [#31361](https://github.com/open-webui/open-webui/issues/31361)

> 📬 **Send queue recovers.** Deleting or editing a queued message held back by a failed attachment now lets the rest of the queue send, where the chat's queue previously stayed stuck until the chat was reopened. [#30447](https://github.com/open-webui/open-webui/pull/30447), [#28880](https://github.com/open-webui/open-webui/issues/28880)

> 🏅 **Copied replies start unrated.** A reply saved as a copy no longer carries over the original's rating, so rating the copy no longer overwrites the original's feedback. [#30962](https://github.com/open-webui/open-webui/pull/30962), [#30961](https://github.com/open-webui/open-webui/issues/30961)

> 🎭 **Artifacts pane after deleting a message.** Deleting the message holding the newest artifact while the artifacts pane shows it now moves the pane to the last remaining artifact, where it kept showing the deleted one with wrong version numbers. [#30435](https://github.com/open-webui/open-webui/pull/30435), [#30287](https://github.com/open-webui/open-webui/issues/30287)

> 🔌 **Deleting a direct connection sticks.** Deleting one of your own direct connections in Settings is now saved right away, where it came back after a reload unless you also pressed Save. [#31384](https://github.com/open-webui/open-webui/pull/31384), [#31383](https://github.com/open-webui/open-webui/issues/31383)

> 🧹 **Add Connection form reset.** Adding several connections in a row no longer silently saves the advanced settings of the first one, such as its headers, provider and API type, with the next. [#30958](https://github.com/open-webui/open-webui/pull/30958), [#30957](https://github.com/open-webui/open-webui/issues/30957)

> ⌨️ **Ctrl+Enter to Send in channels.** With "Ctrl+Enter to Send" turned on, Enter in a channel or thread reply now starts a new line and Ctrl+Enter sends, where Enter always sent the message. [#31319](https://github.com/open-webui/open-webui/pull/31319), [#31318](https://github.com/open-webui/open-webui/issues/31318)

> 🏷️ **Tags after bulk chat actions.** Unarchiving all chats now brings their tags back, and deleting all chats removes tags no longer used by any chat from the suggestions. [#30453](https://github.com/open-webui/open-webui/pull/30453), [#30452](https://github.com/open-webui/open-webui/issues/30452)

> ⌨️ **Enter after a smiley.** Pressing Enter now sends a message that ends in a smiley such as ":)" or in a word starting with ":", "/" or "#", where it did nothing because an empty suggestion list still held on to the key. [#31506](https://github.com/open-webui/open-webui/pull/31506), [#31504](https://github.com/open-webui/open-webui/issues/31504)

> 🔎 **Hybrid search on large Chroma collections.** Hybrid search over a knowledge base of more than about 32,000 chunks stored in Chroma now returns results, where it previously failed with "Error querying knowledge base". [#30368](https://github.com/open-webui/open-webui/pull/30368), [#30351](https://github.com/open-webui/open-webui/issues/30351)

> 🧭 **Qdrant strict mode.** File uploads and hybrid search now work on Qdrant with strict mode enabled, where every upload after the first failed with "Limit exceeded" and hybrid search found nothing, and hybrid search now falls back to normal vector search whenever a collection cannot be read. [#31461](https://github.com/open-webui/open-webui/pull/31461), [#31460](https://github.com/open-webui/open-webui/pull/31460), [#31459](https://github.com/open-webui/open-webui/issues/31459)

> 🔤 **Korean and Japanese text files.** Korean and Japanese text files in legacy encodings such as EUC-KR and Shift-JIS are now read correctly for chats and knowledge bases, where they were stored as garbled Chinese characters. [#31356](https://github.com/open-webui/open-webui/pull/31356), [#31352](https://github.com/open-webui/open-webui/issues/31352)

> 🧵 **Backslashes in HTML uploads.** Uploaded HTML files now keep their backslashes as written, where a path such as "C:\new\table" gained line breaks and one containing "C:\Users" failed to upload. [#31450](https://github.com/open-webui/open-webui/pull/31450), [#31440](https://github.com/open-webui/open-webui/issues/31440)

> 🕸️ **Unreachable links named.** Attaching or adding a link that cannot be fetched, such as one whose server refuses the connection or returns an error page, now reports "Could not read content from" the link instead of a vague processing or knowledge base error. [#31351](https://github.com/open-webui/open-webui/pull/31351), [#31354](https://github.com/open-webui/open-webui/pull/31354), [#31347](https://github.com/open-webui/open-webui/issues/31347)

> 👥 **Admin user chat list after deletion.** Deleting a chat from a user's chat list in the admin panel no longer leaves the list empty. [#30604](https://github.com/open-webui/open-webui/pull/30604), [#30601](https://github.com/open-webui/open-webui/issues/30601)

> 📇 **User CSV import blank line.** Importing users from a CSV file that ends with a line break no longer reports the empty last line as an invalid row. [#31374](https://github.com/open-webui/open-webui/pull/31374), [#31373](https://github.com/open-webui/open-webui/issues/31373)

> 📅 **Calendar event end moves with its date.** Changing a calendar event's date now moves its end along with it, where the end kept its old date and events could span several days or lose their duration. [#31303](https://github.com/open-webui/open-webui/pull/31303), [#31302](https://github.com/open-webui/open-webui/issues/31302)

> 🔂 **Repeating events that started earlier.** A repeating calendar event that is still running when the visible dates begin, such as a weekly event from 23:00 to 01:00, now shows on the following day, where only the same event without a repeat did. [#31606](https://github.com/open-webui/open-webui/pull/31606), [#31605](https://github.com/open-webui/open-webui/issues/31605)

> 📋 **Copy buttons in account settings.** Copying your token or API key in the account settings no longer also saves the account form and any unsaved profile changes along with it. [#30956](https://github.com/open-webui/open-webui/pull/30956), [#30955](https://github.com/open-webui/open-webui/issues/30955)

> 📨 **Anthropic Messages endpoint with empty tools.** Requests to the Anthropic-compatible Messages endpoint that send an empty or null tools list, as Claude Code does for text-only requests, no longer fail against backends such as vLLM and OpenAI. [#31343](https://github.com/open-webui/open-webui/pull/31343), [#31341](https://github.com/open-webui/open-webui/issues/31341)

> 🚧 **Failed streams on the Anthropic Messages endpoint.** A streamed request to the Anthropic-compatible Messages endpoint that fails partway now ends with an error, so clients such as Claude Code no longer take the cut-off answer as complete. [#31405](https://github.com/open-webui/open-webui/pull/31405), [#31403](https://github.com/open-webui/open-webui/issues/31403)

> 🕐 **Group filter on the hourly analytics chart.** The analytics chart for the last 24 hours now respects the selected group, where it counted every user's messages while the rest of the page was filtered. [#30978](https://github.com/open-webui/open-webui/pull/30978), [#30977](https://github.com/open-webui/open-webui/issues/30977)

> 📜 **Title generation log noise.** Starting a new chat no longer writes a misleading "Error generating initial chat title" traceback to the server log. [#30356](https://github.com/open-webui/open-webui/pull/30356), [#30339](https://github.com/open-webui/open-webui/issues/30339)

> 🌊 **Code blocks fenced with tildes.** Code blocks fenced with ~~~ now show as code blocks with their language label and Copy button, where they were shown as a single line of plain text. [#31543](https://github.com/open-webui/open-webui/pull/31543), [#31542](https://github.com/open-webui/open-webui/issues/31542)

> 🗺️ **DEFAULT_LOCALE on the first visit.** A new visitor now gets the language set in "DEFAULT_LOCALE" again, where since 0.11.4 they always got their browser's language; a language picked in Settings or a ?lang= link still takes precedence. [#31551](https://github.com/open-webui/open-webui/pull/31551), [#31548](https://github.com/open-webui/open-webui/issues/31548)

> 📋 **Multi-line table cells in notes.** A note table cell with more than one line now stays inside its row in the note's Markdown download and its Chat panel, where the second line broke the row and shifted cells into other columns. [#31539](https://github.com/open-webui/open-webui/pull/31539), [#31538](https://github.com/open-webui/open-webui/issues/31538)

> 🎯 **Exact matches on Weaviate.** With Weaviate, a chunk identical to the query now scores 1 instead of 0, so perfect matches no longer land at the bottom of the results or fall below the relevance threshold. [#31531](https://github.com/open-webui/open-webui/pull/31531), [#31527](https://github.com/open-webui/open-webui/issues/31527)

> 📍 **Unpinning folder chats by dragging.** Dragging a pinned chat out of a folder onto Chats now unpins it, where it stayed pinned. [#31368](https://github.com/open-webui/open-webui/pull/31368), [#31367](https://github.com/open-webui/open-webui/issues/31367)

> 🔍 **New chat from the search dialog.** Starting a new conversation from the search dialog now sends the typed text unchanged, where everything from a # or & on was dropped and + turned into a space. [#31592](https://github.com/open-webui/open-webui/pull/31592), [#31469](https://github.com/open-webui/open-webui/issues/31469)

> 📈 **OpenTelemetry logs sent once.** With "ENABLE_OTEL", "ENABLE_OTEL_TRACES" and "ENABLE_OTEL_LOGS" all on, each log line now reaches the collector once instead of twice, so "OTEL_PYTHON_LOG_AUTO_INSTRUMENTATION=false" is no longer needed as a workaround. [#31528](https://github.com/open-webui/open-webui/pull/31528), [#31524](https://github.com/open-webui/open-webui/issues/31524)

> 📎 **Large pastes in channels.** With Paste Large Text as File on, pasting more than 1,000 characters into a channel or thread now attaches it as a text file, where the text vanished. [#31366](https://github.com/open-webui/open-webui/pull/31366), [#31365](https://github.com/open-webui/open-webui/issues/31365)

> 🪢 **SCIM group member links.** Members in SCIM group responses now carry the link to their user, where every member came back with "$ref": null. [#31529](https://github.com/open-webui/open-webui/pull/31529), [#31525](https://github.com/open-webui/open-webui/issues/31525)

> 🧩 **Tool HTML embeds with entities.** HTML embeds, arguments and file links from tools now show exactly what the tool returned, where an embed containing an entity such as &quot; did not show at all and &amp; or &lt; were turned into real characters. [#31390](https://github.com/open-webui/open-webui/pull/31390), [#28085](https://github.com/open-webui/open-webui/issues/28085)

> ↩️ **Pending reply when switching channels.** Switching to another channel now drops a reply you had started, where it carried over, failed to send and left a faded copy behind. [#31376](https://github.com/open-webui/open-webui/pull/31376), [#31375](https://github.com/open-webui/open-webui/issues/31375)

> 🎨 **Invalid image Additional Parameters.** Saving the Images settings with invalid JSON in the Additional Parameters for OpenAI or AUTOMATIC1111 now shows an error, where Save kept spinning. [#31382](https://github.com/open-webui/open-webui/pull/31382), [#31381](https://github.com/open-webui/open-webui/issues/31381)

> ♻️ **Editing a repeating event from a later occurrence.** Opening a repeating calendar event from a later occurrence and saving it now keeps the series' own start date, where it moved the start to the clicked occurrence and deleted every earlier one. [#30971](https://github.com/open-webui/open-webui/pull/30971), [#30970](https://github.com/open-webui/open-webui/issues/30970)

> 💬 **Readable mention notifications.** Notifications for channel messages that mention a user or channel now show the mention as it appears in the channel, such as "@ Alex", where they showed the raw mention markup with the internal id. [#31601](https://github.com/open-webui/open-webui/pull/31601), [#31586](https://github.com/open-webui/open-webui/issues/31586)

> 🎹 **Enter in the search dialog.** Pressing Enter on a highlighted chat in the search dialog now opens it, where the dialog only closed. [#31004](https://github.com/open-webui/open-webui/pull/31004), [#31003](https://github.com/open-webui/open-webui/issues/31003)

> 🧺 **Edited knowledge files on Elasticsearch.** With Elasticsearch as the vector database, editing a knowledge file now removes its old text from search, where chats and searches kept returning the old text next to the new. [#31530](https://github.com/open-webui/open-webui/pull/31530), [#31523](https://github.com/open-webui/open-webui/issues/31523)

> 🐘 **External pgvector knowledge bases.** External knowledge bases on the pgvector provider return results again, where every search failed with "operator does not exist: vector <=> double precision[]" and the knowledge base looked empty. [#31112](https://github.com/open-webui/open-webui/pull/31112), [#26663](https://github.com/open-webui/open-webui/issues/26663)

> 👯 **Duplicate files in knowledge batch add.** Adding files to a knowledge base in a batch now rejects a file whose text is already in it, the same way adding a single file does, where the same text was embedded twice and retrieval returned the same passages twice. [#31336](https://github.com/open-webui/open-webui/pull/31336), [#31333](https://github.com/open-webui/open-webui/issues/31333)

> ⏳ **Older unfinished responses no longer spin forever.** Opening a chat with no generation running now shows every unfinished response as finished, with its copy and regenerate buttons, where only the newest one was repaired and older ones from cancelled or interrupted generations kept a loading cursor forever; responses waiting for the user to answer a tool's question are left as they are. [#31895](https://github.com/open-webui/open-webui/pull/31895), [#14806](https://github.com/open-webui/open-webui/issues/14806)

> ➗ **Inline math next to dashes.** Inline math written directly next to an em dash or en dash, with either $...$ or \(...\), now renders in chat replies instead of showing as plain text. [#31901](https://github.com/open-webui/open-webui/pull/31901)

> 🛎️ **Ctrl+Shift+Enter with Ctrl+Enter to Send.** With "Ctrl+Enter to Send" on, Ctrl+Shift+Enter now only adds an empty message pair, where it also sent the typed message. [#31864](https://github.com/open-webui/open-webui/pull/31864), [#31468](https://github.com/open-webui/open-webui/issues/31468)

> 🔍 **Edited replies stay searchable.** Chats can now be found in search by the new text of an edited reply, where editing a reply made it unsearchable by both its old and new text. [#31844](https://github.com/open-webui/open-webui/pull/31844), [#31471](https://github.com/open-webui/open-webui/issues/31471)

> 📧 **Pasted emails sent once.** With Rich Text Input for Chat on, pasting an HTML email or newsletter laid out with nested tables no longer sends the same text repeated many times. [#31890](https://github.com/open-webui/open-webui/pull/31890), [#24657](https://github.com/open-webui/open-webui/issues/24657)

> 📊 **Daily Messages chart on All time.** The Daily Messages chart in Analytics now loads on All time when a message was saved without a timestamp, and messages after such a message in the same chat are counted again. [#31888](https://github.com/open-webui/open-webui/pull/31888), [#27316](https://github.com/open-webui/open-webui/issues/27316)

> ↔️ **Mixed right-to-left and left-to-right lines.** Each line of a message now gets its own text direction and alignment, both while typing and in the sent message, so an English line under an Arabic one no longer shows its punctuation on the wrong side. [#31868](https://github.com/open-webui/open-webui/pull/31868), [#31827](https://github.com/open-webui/open-webui/issues/31827)

> 🚛 **Large files on Milvus.** With Milvus as the vector database, large files now finish processing instead of failing with a RESOURCE_EXHAUSTED error after the whole embedding step, because their chunks are sent to Milvus in batches of 128 rather than in one request that exceeded its size limit, with and without multitenancy mode. [#31990](https://github.com/open-webui/open-webui/pull/31990), [#31989](https://github.com/open-webui/open-webui/issues/31989)

> 🍰 **Partial files in knowledge bases on Qdrant.** On Qdrant, a file uploaded to a knowledge base or edited there now always arrives with all of its content, where it could end up with only part of its chunks, often exactly 64, while showing as completed; file processing on a busy Qdrant may take a little longer since each save now waits for Qdrant to finish storing. [#31961](https://github.com/open-webui/open-webui/pull/31961), [#31959](https://github.com/open-webui/open-webui/issues/31959)

> 🩹 **Chats right after a Redis restart.** After Redis restarts or closes its connections, Open WebUI now reconnects and retries the call once, so chat requests no longer fail with a 500 error and newly opened tabs get live updates again as soon as Redis is back. [#31619](https://github.com/open-webui/open-webui/pull/31619)

> 🧮 **Deeply nested chat variable values.** A chat variable property whose value is deeply nested JSON is now kept as plain text, where it could make the request fail. [#30389](https://github.com/open-webui/open-webui/pull/30389)

> 🗃️ **Back and Forward between folder pages.** Going Back or Forward from one folder page to another now shows the folder named in the address bar, where the page kept showing the folder you had left. [#32146](https://github.com/open-webui/open-webui/pull/32146), [#32144](https://github.com/open-webui/open-webui/issues/32144)

> Release notes shortened. [Read the full changelog](https://github.com/open-webui/open-webui/blob/f8ae8a6c328946dc62cd0712961a0632574581bf/CHANGELOG.md).

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
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-e0fce3&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-68-other-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-e0fce3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->