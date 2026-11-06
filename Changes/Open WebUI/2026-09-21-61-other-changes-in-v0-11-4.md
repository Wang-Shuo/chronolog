---
card_id: open-webui-2026-09-21-710b75
date: '2026-09-21'
description: "Open WebUI · 2026-09-21 · Other changes: 61 changes in v0.11.4 — \U0001F4BD
  **Long conversations stream cheaper.** Writing or reading a single message no longer
  loads…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4f47309d4ab50506fc400a747168ca0deae202bd8d7692131c1622d35b91260d
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-710b75
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 61 other changes'
  evidence:
  - quote: "\U0001F4BD **Long conversations stream cheaper.** Writing or reading a
      single message no longer loads, checks and rewrites the entire conversation
      to change a few hundred bytes, so streaming into a long chat stops getting more
      expensive as it grows, and the whole round trip a message event costs falls
      to a fraction on conversations of thousands of messages. [#28184](https://github.com/open-webui/open-webui/pull/28184),
      [#28169](https://github.com/open-webui/open-webui/issues/28169)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F310 **Translation updates.** Translations for Japanese, Traditional
      Chinese, Korean, Finnish, Russian, Ukrainian, German, Spanish, Portuguese (Brazil),
      Arabic, Arabic (Bahrain), Azerbaijani, Bulgarian, Bengali, Tibetan, Bosnian,
      Catalan, Cebuano, Czech, Danish, Basque, Croatian, Dutch, Italian, Turkish,
      Simplified Chinese, Bosnian, Catalan, Danish, Estonian, Finnish, Galician, Croatian,
      Kabyle, Norwegian Bokmål, Portuguese (Portugal), Romanian and Turkmen were enhanced
      and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6E1 **Diagrams and SVG stay on this origin.** Mermaid diagrams
      and SVG previews, attached or uploaded, no longer follow references pointing
      at another origin, a picture, style or configuration line among them, and a
      diagram that reaches outside is refused with an error; a file whose drawing
      leans on an external sprite now shows that part blank. [#30271](https://github.com/open-webui/open-webui/pull/30271)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F50F **Knowledge file access.** A file's access through a knowledge
      base now follows its actual attachment alone, rather than also a collection
      name left behind on the file record. [#29937](https://github.com/open-webui/open-webui/pull/29937)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5D2 **Home page chat drafts.** A message typed into a chat started
      from the home page now comes back after a reload, text, uploads and all, where
      the draft was stored under a key the page never read again. [#29762](https://github.com/open-webui/open-webui/pull/29762),
      [#29760](https://github.com/open-webui/open-webui/issues/29760)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F3DE️ **S3-hosted chat images.** A chat image whose host echoes
      a Content-Encoding nothing asked for, an S3 or MinIO object uploaded with that
      metadata among them, no longer breaks the reply it sits in; it is sent as its
      link the way an unreachable image already was. [#29623](https://github.com/open-webui/open-webui/pull/29623)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5D2️ **Note save on exit.** A note's title and its attachments
      save a moment after they change, and leaving the note inside that moment dropped
      the save, so the notes list kept showing the old title until the page was reloaded;
      the pending save now finishes before the next page opens. [#29745](https://github.com/open-webui/open-webui/pull/29745),
      [#29744](https://github.com/open-webui/open-webui/issues/29744)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9FF **Insert into note on read-only notes.** The Insert into note
      action no longer appears on a note you may only read, which offered it where
      it could not land. [#30223](https://github.com/open-webui/open-webui/pull/30223),
      [#30174](https://github.com/open-webui/open-webui/issues/30174)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ☑️ **Unchecked checkbox defaults.** A prompt variable written as a checkbox
      with a default of false opened the form already ticked, as did False, "false",
      0 and "0", because any non-empty default counted as ticked; it is now ticked
      only where the value really is true. [#30037](https://github.com/open-webui/open-webui/pull/30037),
      [#30036](https://github.com/open-webui/open-webui/issues/30036)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ⎋ **Escape key targeting.** The shortcut for closing a dialog always shut
      the settings window, whichever dialog was actually in front, so a dialog opened
      from within settings took both away at once; each dialog now answers the shortcut
      for itself, as it already did for the escape key. [#29830](https://github.com/open-webui/open-webui/pull/29830),
      [#29817](https://github.com/open-webui/open-webui/issues/29817)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F3B9 **Message pair shortcut.** The shortcut that adds an empty
      question and answer to a chat also sent whatever was typed in the message box,
      so the pair arrived alongside a message you had not meant to send yet. [#30167](https://github.com/open-webui/open-webui/pull/30167)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F941 **Collapsing the task list.** Folding away the list of tasks
      under a reply also sent whatever you had typed in the message box. [#30202](https://github.com/open-webui/open-webui/pull/30202)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ⌨️ **Recording a new shortcut.** Pressing a key combination to record it
      as a shortcut also ran whatever that combination was already bound to, so setting
      one up did the thing you were trying to rebind. [#30160](https://github.com/open-webui/open-webui/pull/30160)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4CC **Channel code headers.** The bar naming a piece of code in
      a channel thread or its pinned messages now sits flush at the top of the panel,
      clipped to the block, rather than floating over the code as it scrolls. [#29836](https://github.com/open-webui/open-webui/pull/29836),
      [#29835](https://github.com/open-webui/open-webui/issues/29835)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FA83 **Responses API tool calling.** A forced tool choice sent to
      a connection on the Responses API went out in the wrong shape and was refused
      by providers that check it, and a tool call in a reply that was not streamed
      came back as empty text, so nothing reading the API ever saw it. [#30095](https://github.com/open-webui/open-webui/pull/30095),
      [#30085](https://github.com/open-webui/open-webui/issues/30085)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FAF1 **Rating a reply again.** Switching a reply's rating from one
      thumb to the other kept the score and the reason given the first time, and rating
      a reply whose feedback had since been deleted failed outright; both now record
      the rating you just gave. [#30075](https://github.com/open-webui/open-webui/pull/30075),
      [#30077](https://github.com/open-webui/open-webui/pull/30077)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4F6 **Sorting feedback by user.** The User column in the admin
      feedback history did nothing when clicked, and now sorts by who left the feedback.
      [#30191](https://github.com/open-webui/open-webui/pull/30191)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F464 **A custom gender shown back.** An account whose gender is
      a wording of its own came back to an empty dropdown in the account form, and
      the form now shows Custom with that wording beside it. [#30215](https://github.com/open-webui/open-webui/pull/30215)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5D3️ **Clearing a calendar event.** Emptying the repeat, the description
      or the location of a calendar event did not take and the old wording came back,
      and those fields can be cleared again. [#30204](https://github.com/open-webui/open-webui/pull/30204)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4D5 **Required prompt dropdowns.** A prompt's form could be sent
      with a required dropdown left unchosen, and now asks you to pick something first.
      [#30078](https://github.com/open-webui/open-webui/pull/30078)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F3AB **Account form required fields.** The account form now refuses
      to save with a required field left empty, the way the admin user dialog does,
      and a date of birth is no longer demanded of accounts that never set one. [#30296](https://github.com/open-webui/open-webui/pull/30296),
      [#30295](https://github.com/open-webui/open-webui/issues/30295)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FAC2 **Group dialog reset.** The new-group dialog opens empty after
      a group is created, where the next one came up holding the group just made.
      [#30280](https://github.com/open-webui/open-webui/pull/30280), [#30279](https://github.com/open-webui/open-webui/issues/30279)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9F5 **Thread reply notifications.** Clicking the notification for
      a reply written inside a thread dropped you at the bottom of the channel with
      the thread still shut and the reply nowhere in sight; it now opens the thread
      the reply belongs to. [#29856](https://github.com/open-webui/open-webui/pull/29856),
      [#29855](https://github.com/open-webui/open-webui/issues/29855)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F53D **Dropdown arrow spacing.** The arrow in the dropdowns drawn
      no wider than their contents, among them the provider on a new connection, no
      longer overlaps the last characters of the longest choice. [#29866](https://github.com/open-webui/open-webui/pull/29866),
      [#29865](https://github.com/open-webui/open-webui/issues/29865)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9CA **Lowercase header handling.** Headers from an upstream that
      writes them in lower case, as anything served by uvicorn does, are now matched
      without regard to case, so \"Content-Encoding\" is stripped and clients stop
      failing to decompress a body the server had already decoded. [#29843](https://github.com/open-webui/open-webui/pull/29843)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6A8 **Code run errors with output.** A code run that ends with
      an error now shows the error alongside what it printed, where a run that printed
      anything at all showed its error nowhere. [#30286](https://github.com/open-webui/open-webui/pull/30286),
      [#30285](https://github.com/open-webui/open-webui/issues/30285)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F3AF **Knowledge search accuracy on PostgreSQL.** A fresh install
      using PostgreSQL built its search index before a single piece of text existed
      to organise it around, so the index was never fit for the content that arrived
      afterwards and every search quietly returned the wrong passages; the index now
      waits until there is enough text to build on, and until then searches read everything
      exactly. An install already carrying such an index can restore it by rebuilding
      that one index. [#30143](https://github.com/open-webui/open-webui/pull/30143),
      [#30134](https://github.com/open-webui/open-webui/issues/30134)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5C2 **Knowledge file filter on first click.** The File content
      filter in a knowledge base now narrows the listing the first time it is clicked,
      where the first click only armed the checkbox and everything stayed listed until
      it was clicked again. [#30211](https://github.com/open-webui/open-webui/pull/30211),
      [#30210](https://github.com/open-webui/open-webui/issues/30210)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FAA3 **Searches that found nothing.** A knowledge search that came
      back empty never handed its database connection back, so enough of them left
      knowledge search failing outright until the server was restarted; connections
      are returned now on PostgreSQL and on openGauss alike. [#30142](https://github.com/open-webui/open-webui/pull/30142),
      [#30133](https://github.com/open-webui/open-webui/issues/30133), [#30144](https://github.com/open-webui/open-webui/pull/30144)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ⏲️ **Recurrence counts and start dates.** A rule repeating a set number
      of times, ten or a hundred, is read as the limited repeat it is, where any count
      beginning with a one was treated as one-shot, and a rule carrying its start
      date on the same line as its repeat text now follows the start you picked, on
      schedules and calendar events alike. [#29262](https://github.com/open-webui/open-webui/pull/29262)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F600 **Multi-codepoint emoji.** An emoji whose shortcode is several
      codepoints, the flags among them, is inserted whole, where only its first part
      reached the message. [#30213](https://github.com/open-webui/open-webui/pull/30213),
      [#30212](https://github.com/open-webui/open-webui/issues/30212)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F514 **Custom webhook names.** A webhook target named with a space
      or a slash is now tidied the way an automatic name always was, so it can still
      be edited, deleted, made the default or tested afterwards. [#29947](https://github.com/open-webui/open-webui/pull/29947)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4AD **Anthropic thinking blocks.** Open WebUI's own thinking blocks
      are no longer forwarded to an OpenAI-compatible backend, which since 0.11.0
      made a strict server such as NVIDIA Dynamo refuse an Anthropic client's second
      turn; signed blocks still pass through. [#29849](https://github.com/open-webui/open-webui/pull/29849),
      [#29799](https://github.com/open-webui/open-webui/issues/29799)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9FA **Deleted channel messages leave no quotes.** Deleting a channel
      message now clears the quote of it sitting on every reply and drops it from
      the reply box, where a reply kept showing the deleted message and could still
      be sent addressed to it. [#30314](https://github.com/open-webui/open-webui/pull/30314),
      [#30313](https://github.com/open-webui/open-webui/issues/30313)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F433 **Dotless host addresses.** With local web fetching turned
      on, an address pointing at a container name on the same network, \"http://apprise:8000\"
      and the like, is now accepted rather than refused as invalid. [#29945](https://github.com/open-webui/open-webui/pull/29945),
      [#28161](https://github.com/open-webui/open-webui/issues/28161)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FAE5 **Webhook avatar forwarding.** Turning \"ENABLE_PROFILE_IMAGE_URL_FORWARDING\"
      off stops browsers being sent on to outside picture addresses, and a channel
      webhook's picture was sent on regardless; it now serves the built-in picture
      like the rest, in the webhooks dialog as well as the message list, where the
      dialog had been sending every viewer's browser straight to the outside address.
      [#29889](https://github.com/open-webui/open-webui/pull/29889), [#29892](https://github.com/open-webui/open-webui/pull/29892)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FA9F **Statistics window origin.** The window that shares chat statistics
      with the community accepted requests from any page that opened it and answered
      to anywhere; it now reads and replies only where the community site is at the
      other end. [#29918](https://github.com/open-webui/open-webui/pull/29918)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FA7A **Knowledge sync errors.** A knowledge base sync that fails
      now names the file it happened on and what the browser said, rather than reporting
      nothing beyond \"Error accessing directory\". [#29507](https://github.com/open-webui/open-webui/pull/29507)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F39E️ **Tool embed scope.** The frames a tool call can ask to have
      shown, which run scripts of their own, were drawn wherever a message was rendered,
      a channel among them; they are now drawn only in the replies of the chat you
      are in, and never in a channel. [#29985](https://github.com/open-webui/open-webui/pull/29985)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F374 **Forked chat folder.** Forking a chat put the copy in the
      original's folder even where you cannot write to that folder; it is now created
      outside any folder unless you can. [#30069](https://github.com/open-webui/open-webui/pull/30069)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FAA2 **Dropping a folder in place.** Dragging a folder onto the
      folder it already sits in failed with \"Folder already exists\", and is now
      taken for the no-op it is. [#30169](https://github.com/open-webui/open-webui/pull/30169)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6BF **Deleting a folder, keeping chats.** Removing a folder while
      keeping the chats inside it was refused for an account not allowed to delete
      chats, even though nothing was being deleted, and it now goes through. [#30163](https://github.com/open-webui/open-webui/pull/30163)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F331 **Forking past an unfinished reply.** A chat that held an interrupted
      reply anywhere in it refused every fork from then on and never recovered; forking
      now waits only on a reply actually being generated, and a turn paused for tool
      approval still forks with its prompt showing. [#30131](https://github.com/open-webui/open-webui/pull/30131),
      [#30128](https://github.com/open-webui/open-webui/issues/30128)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ♻️ **Session pool cleanup.** The task that clears out abandoned websocket
      sessions now carries on through an error from Redis instead of ending for good,
      and stops properly at shutdown. [#29976](https://github.com/open-webui/open-webui/pull/29976),
      [#29979](https://github.com/open-webui/open-webui/pull/29979)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F52C **Page fetch CPU spin.** Fetching a page through the browser-driven
      loader never returned where that page opened a WebSocket, holding a worker thread
      at full CPU for the life of the process and costing another core on every further
      fetch, which left the whole instance slow. [#30050](https://github.com/open-webui/open-webui/pull/30050),
      [#30024](https://github.com/open-webui/open-webui/issues/30024)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F501 **Duplicate search tracebacks.** A vector database outage wrote
      a full traceback twice for every collection and query pair, turning one outage
      into hundreds of identical stack traces per message on every replica; a single
      record now names every collection that failed. [#29981](https://github.com/open-webui/open-webui/pull/29981)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9EF **Page fetch logging.** Fetching a page through the browser-driven
      loader filled the log with tracebacks where the page closed while it was still
      pulling pieces of itself, as sites behind Cloudflare and similar do; those requests
      are now let go of before the page closes. [#29325](https://github.com/open-webui/open-webui/pull/29325),
      [#28869](https://github.com/open-webui/open-webui/issues/28869)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9F3 **Imported chats keep more.** A chat brought back from an export
      arrived unpinned and unarchived and without the variables it was saved with,
      and all three now survive the round trip. [#30155](https://github.com/open-webui/open-webui/pull/30155),
      [#30151](https://github.com/open-webui/open-webui/pull/30151)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F648 **Folder filters with no match.** A chat search narrowed by
      a folder name that matches no folder now finds nothing, where the folder filter
      was quietly dropped and every chat came back. [#30273](https://github.com/open-webui/open-webui/pull/30273),
      [#29959](https://github.com/open-webui/open-webui/discussions/29959)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6AA **Webhook pictures follow channel access.** The picture belonging
      to a channel webhook is now shown only to people with access to that channel,
      where anyone signed in could fetch it or be sent on to wherever it pointed,
      and it is refused outright where channels are turned off. [#29703](https://github.com/open-webui/open-webui/pull/29703)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6A6 **Citation link schemes.** A source attached to a reply now
      opens only where it points at a web address, falling back to the panel that
      shows the source rather than following anything else. [#29701](https://github.com/open-webui/open-webui/pull/29701)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F21A **Citation chips inside formatted text.** A citation inside
      bold, italic or linked text now renders its chip, where the formatting took
      it and the citation vanished from the sentence. [#30278](https://github.com/open-webui/open-webui/pull/30278),
      [#30277](https://github.com/open-webui/open-webui/issues/30277)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F40D **Saving a tool or function.** Saving a tool or function in
      the admin pages no longer fails with a missing module error from the built-in
      code formatter, which was not installing everything it needed. [#29503](https://github.com/open-webui/open-webui/pull/29503)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6E0️ **Tool request duplication.** A tool that writes through an
      address carrying part of its input no longer has that part repeated in the body
      of the request as well, which servers checking their input strictly turned away,
      so those calls now go through. [#29717](https://github.com/open-webui/open-webui/pull/29717),
      [#29716](https://github.com/open-webui/open-webui/issues/29716)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F53C **Honest version checks.** An instance that cannot reach the
      release listing now says the check failed, instead of reporting whatever it
      is running as the newest version and recording nothing about it. [#29626](https://github.com/open-webui/open-webui/pull/29626),
      [#29580](https://github.com/open-webui/open-webui/issues/29580)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9F9 **Direct connections stop leaking listeners.** A server talking
      to a direct connection no longer leaves a listener behind for every request
      that ends any way but a clean finish, which grew without limit while a connection
      kept failing. [#29509](https://github.com/open-webui/open-webui/pull/29509)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4DD **Starting a note from search.** Starting a note from the search
      box now works when you are already on the notes page, keeps the whole of what
      you typed including characters such as ampersands and hashes, and no longer
      makes a further note each time the browser back button is pressed. [#29645](https://github.com/open-webui/open-webui/pull/29645),
      [#29642](https://github.com/open-webui/open-webui/issues/29642)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4CA **Single source relevance.** A reply drawing on a single source
      now shows how relevant that source is, where the figure appeared only once a
      second source joined it and so looked as though it came and went. [#29647](https://github.com/open-webui/open-webui/pull/29647),
      [#29646](https://github.com/open-webui/open-webui/issues/29646)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ⌨️ **Literal arrow sequences.** A sequence such as three hyphens after
      a less-than sign is now shown as the characters it is made of rather than drawn
      as an arrow, which had text look changed when it never was. [#29595](https://github.com/open-webui/open-webui/pull/29595),
      [#29594](https://github.com/open-webui/open-webui/issues/29594)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F3A8 **A tidier attach webpage dialog.** The row holding the Add
      button no longer carries a grey band of its own between the address box and
      the button, matching every other dialog. [#29664](https://github.com/open-webui/open-webui/pull/29664),
      [#29663](https://github.com/open-webui/open-webui/issues/29663)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5B1️ **A plain note date.** The date under a note title no longer
      shows a pointing hand or announces itself as something to press, having never
      done anything when clicked. [#29708](https://github.com/open-webui/open-webui/pull/29708)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 61-other-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: uncategorized
  title: 61 other changes in v0.11.4
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: uncategorized
title: 61 other changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 61 other changes in v0.11.4

**Open WebUI** · 2026-09-21 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 💽 **Long conversations stream cheaper.** Writing or reading a single message no longer loads, checks and rewrites the entire conversation to change a few hundred bytes, so streaming into a long chat stops getting more expensive as it grows, and the whole round trip a message event costs falls to a fraction on conversations of thousands of messages. [#28184](https://github.com/open-webui/open-webui/pull/28184), [#28169](https://github.com/open-webui/open-webui/issues/28169)

> 🌐 **Translation updates.** Translations for Japanese, Traditional Chinese, Korean, Finnish, Russian, Ukrainian, German, Spanish, Portuguese (Brazil), Arabic, Arabic (Bahrain), Azerbaijani, Bulgarian, Bengali, Tibetan, Bosnian, Catalan, Cebuano, Czech, Danish, Basque, Croatian, Dutch, Italian, Turkish, Simplified Chinese, Bosnian, Catalan, Danish, Estonian, Finnish, Galician, Croatian, Kabyle, Norwegian Bokmål, Portuguese (Portugal), Romanian and Turkmen were enhanced and expanded.

> 🛡 **Diagrams and SVG stay on this origin.** Mermaid diagrams and SVG previews, attached or uploaded, no longer follow references pointing at another origin, a picture, style or configuration line among them, and a diagram that reaches outside is refused with an error; a file whose drawing leans on an external sprite now shows that part blank. [#30271](https://github.com/open-webui/open-webui/pull/30271)

> 🔏 **Knowledge file access.** A file's access through a knowledge base now follows its actual attachment alone, rather than also a collection name left behind on the file record. [#29937](https://github.com/open-webui/open-webui/pull/29937)

> 🗒 **Home page chat drafts.** A message typed into a chat started from the home page now comes back after a reload, text, uploads and all, where the draft was stored under a key the page never read again. [#29762](https://github.com/open-webui/open-webui/pull/29762), [#29760](https://github.com/open-webui/open-webui/issues/29760)

> 🏞️ **S3-hosted chat images.** A chat image whose host echoes a Content-Encoding nothing asked for, an S3 or MinIO object uploaded with that metadata among them, no longer breaks the reply it sits in; it is sent as its link the way an unreachable image already was. [#29623](https://github.com/open-webui/open-webui/pull/29623)

> 🗒️ **Note save on exit.** A note's title and its attachments save a moment after they change, and leaving the note inside that moment dropped the save, so the notes list kept showing the old title until the page was reloaded; the pending save now finishes before the next page opens. [#29745](https://github.com/open-webui/open-webui/pull/29745), [#29744](https://github.com/open-webui/open-webui/issues/29744)

> 🧿 **Insert into note on read-only notes.** The Insert into note action no longer appears on a note you may only read, which offered it where it could not land. [#30223](https://github.com/open-webui/open-webui/pull/30223), [#30174](https://github.com/open-webui/open-webui/issues/30174)

> ☑️ **Unchecked checkbox defaults.** A prompt variable written as a checkbox with a default of false opened the form already ticked, as did False, "false", 0 and "0", because any non-empty default counted as ticked; it is now ticked only where the value really is true. [#30037](https://github.com/open-webui/open-webui/pull/30037), [#30036](https://github.com/open-webui/open-webui/issues/30036)

> ⎋ **Escape key targeting.** The shortcut for closing a dialog always shut the settings window, whichever dialog was actually in front, so a dialog opened from within settings took both away at once; each dialog now answers the shortcut for itself, as it already did for the escape key. [#29830](https://github.com/open-webui/open-webui/pull/29830), [#29817](https://github.com/open-webui/open-webui/issues/29817)

> 🎹 **Message pair shortcut.** The shortcut that adds an empty question and answer to a chat also sent whatever was typed in the message box, so the pair arrived alongside a message you had not meant to send yet. [#30167](https://github.com/open-webui/open-webui/pull/30167)

> 🥁 **Collapsing the task list.** Folding away the list of tasks under a reply also sent whatever you had typed in the message box. [#30202](https://github.com/open-webui/open-webui/pull/30202)

> ⌨️ **Recording a new shortcut.** Pressing a key combination to record it as a shortcut also ran whatever that combination was already bound to, so setting one up did the thing you were trying to rebind. [#30160](https://github.com/open-webui/open-webui/pull/30160)

> 📌 **Channel code headers.** The bar naming a piece of code in a channel thread or its pinned messages now sits flush at the top of the panel, clipped to the block, rather than floating over the code as it scrolls. [#29836](https://github.com/open-webui/open-webui/pull/29836), [#29835](https://github.com/open-webui/open-webui/issues/29835)

> 🪃 **Responses API tool calling.** A forced tool choice sent to a connection on the Responses API went out in the wrong shape and was refused by providers that check it, and a tool call in a reply that was not streamed came back as empty text, so nothing reading the API ever saw it. [#30095](https://github.com/open-webui/open-webui/pull/30095), [#30085](https://github.com/open-webui/open-webui/issues/30085)

> 🫱 **Rating a reply again.** Switching a reply's rating from one thumb to the other kept the score and the reason given the first time, and rating a reply whose feedback had since been deleted failed outright; both now record the rating you just gave. [#30075](https://github.com/open-webui/open-webui/pull/30075), [#30077](https://github.com/open-webui/open-webui/pull/30077)

> 📶 **Sorting feedback by user.** The User column in the admin feedback history did nothing when clicked, and now sorts by who left the feedback. [#30191](https://github.com/open-webui/open-webui/pull/30191)

> 👤 **A custom gender shown back.** An account whose gender is a wording of its own came back to an empty dropdown in the account form, and the form now shows Custom with that wording beside it. [#30215](https://github.com/open-webui/open-webui/pull/30215)

> 🗓️ **Clearing a calendar event.** Emptying the repeat, the description or the location of a calendar event did not take and the old wording came back, and those fields can be cleared again. [#30204](https://github.com/open-webui/open-webui/pull/30204)

> 📕 **Required prompt dropdowns.** A prompt's form could be sent with a required dropdown left unchosen, and now asks you to pick something first. [#30078](https://github.com/open-webui/open-webui/pull/30078)

> 🎫 **Account form required fields.** The account form now refuses to save with a required field left empty, the way the admin user dialog does, and a date of birth is no longer demanded of accounts that never set one. [#30296](https://github.com/open-webui/open-webui/pull/30296), [#30295](https://github.com/open-webui/open-webui/issues/30295)

> 🫂 **Group dialog reset.** The new-group dialog opens empty after a group is created, where the next one came up holding the group just made. [#30280](https://github.com/open-webui/open-webui/pull/30280), [#30279](https://github.com/open-webui/open-webui/issues/30279)

> 🧵 **Thread reply notifications.** Clicking the notification for a reply written inside a thread dropped you at the bottom of the channel with the thread still shut and the reply nowhere in sight; it now opens the thread the reply belongs to. [#29856](https://github.com/open-webui/open-webui/pull/29856), [#29855](https://github.com/open-webui/open-webui/issues/29855)

> 🔽 **Dropdown arrow spacing.** The arrow in the dropdowns drawn no wider than their contents, among them the provider on a new connection, no longer overlaps the last characters of the longest choice. [#29866](https://github.com/open-webui/open-webui/pull/29866), [#29865](https://github.com/open-webui/open-webui/issues/29865)

> 🧊 **Lowercase header handling.** Headers from an upstream that writes them in lower case, as anything served by uvicorn does, are now matched without regard to case, so "Content-Encoding" is stripped and clients stop failing to decompress a body the server had already decoded. [#29843](https://github.com/open-webui/open-webui/pull/29843)

> 🚨 **Code run errors with output.** A code run that ends with an error now shows the error alongside what it printed, where a run that printed anything at all showed its error nowhere. [#30286](https://github.com/open-webui/open-webui/pull/30286), [#30285](https://github.com/open-webui/open-webui/issues/30285)

> 🎯 **Knowledge search accuracy on PostgreSQL.** A fresh install using PostgreSQL built its search index before a single piece of text existed to organise it around, so the index was never fit for the content that arrived afterwards and every search quietly returned the wrong passages; the index now waits until there is enough text to build on, and until then searches read everything exactly. An install already carrying such an index can restore it by rebuilding that one index. [#30143](https://github.com/open-webui/open-webui/pull/30143), [#30134](https://github.com/open-webui/open-webui/issues/30134)

> 🗂 **Knowledge file filter on first click.** The File content filter in a knowledge base now narrows the listing the first time it is clicked, where the first click only armed the checkbox and everything stayed listed until it was clicked again. [#30211](https://github.com/open-webui/open-webui/pull/30211), [#30210](https://github.com/open-webui/open-webui/issues/30210)

> 🪣 **Searches that found nothing.** A knowledge search that came back empty never handed its database connection back, so enough of them left knowledge search failing outright until the server was restarted; connections are returned now on PostgreSQL and on openGauss alike. [#30142](https://github.com/open-webui/open-webui/pull/30142), [#30133](https://github.com/open-webui/open-webui/issues/30133), [#30144](https://github.com/open-webui/open-webui/pull/30144)

> ⏲️ **Recurrence counts and start dates.** A rule repeating a set number of times, ten or a hundred, is read as the limited repeat it is, where any count beginning with a one was treated as one-shot, and a rule carrying its start date on the same line as its repeat text now follows the start you picked, on schedules and calendar events alike. [#29262](https://github.com/open-webui/open-webui/pull/29262)

> 😀 **Multi-codepoint emoji.** An emoji whose shortcode is several codepoints, the flags among them, is inserted whole, where only its first part reached the message. [#30213](https://github.com/open-webui/open-webui/pull/30213), [#30212](https://github.com/open-webui/open-webui/issues/30212)

> 🔔 **Custom webhook names.** A webhook target named with a space or a slash is now tidied the way an automatic name always was, so it can still be edited, deleted, made the default or tested afterwards. [#29947](https://github.com/open-webui/open-webui/pull/29947)

> 💭 **Anthropic thinking blocks.** Open WebUI's own thinking blocks are no longer forwarded to an OpenAI-compatible backend, which since 0.11.0 made a strict server such as NVIDIA Dynamo refuse an Anthropic client's second turn; signed blocks still pass through. [#29849](https://github.com/open-webui/open-webui/pull/29849), [#29799](https://github.com/open-webui/open-webui/issues/29799)

> 🧺 **Deleted channel messages leave no quotes.** Deleting a channel message now clears the quote of it sitting on every reply and drops it from the reply box, where a reply kept showing the deleted message and could still be sent addressed to it. [#30314](https://github.com/open-webui/open-webui/pull/30314), [#30313](https://github.com/open-webui/open-webui/issues/30313)

> 🐳 **Dotless host addresses.** With local web fetching turned on, an address pointing at a container name on the same network, "http://apprise:8000" and the like, is now accepted rather than refused as invalid. [#29945](https://github.com/open-webui/open-webui/pull/29945), [#28161](https://github.com/open-webui/open-webui/issues/28161)

> 🫥 **Webhook avatar forwarding.** Turning "ENABLE_PROFILE_IMAGE_URL_FORWARDING" off stops browsers being sent on to outside picture addresses, and a channel webhook's picture was sent on regardless; it now serves the built-in picture like the rest, in the webhooks dialog as well as the message list, where the dialog had been sending every viewer's browser straight to the outside address. [#29889](https://github.com/open-webui/open-webui/pull/29889), [#29892](https://github.com/open-webui/open-webui/pull/29892)

> 🪟 **Statistics window origin.** The window that shares chat statistics with the community accepted requests from any page that opened it and answered to anywhere; it now reads and replies only where the community site is at the other end. [#29918](https://github.com/open-webui/open-webui/pull/29918)

> 🩺 **Knowledge sync errors.** A knowledge base sync that fails now names the file it happened on and what the browser said, rather than reporting nothing beyond "Error accessing directory". [#29507](https://github.com/open-webui/open-webui/pull/29507)

> 🎞️ **Tool embed scope.** The frames a tool call can ask to have shown, which run scripts of their own, were drawn wherever a message was rendered, a channel among them; they are now drawn only in the replies of the chat you are in, and never in a channel. [#29985](https://github.com/open-webui/open-webui/pull/29985)

> 🍴 **Forked chat folder.** Forking a chat put the copy in the original's folder even where you cannot write to that folder; it is now created outside any folder unless you can. [#30069](https://github.com/open-webui/open-webui/pull/30069)

> 🪢 **Dropping a folder in place.** Dragging a folder onto the folder it already sits in failed with "Folder already exists", and is now taken for the no-op it is. [#30169](https://github.com/open-webui/open-webui/pull/30169)

> 🚿 **Deleting a folder, keeping chats.** Removing a folder while keeping the chats inside it was refused for an account not allowed to delete chats, even though nothing was being deleted, and it now goes through. [#30163](https://github.com/open-webui/open-webui/pull/30163)

> 🌱 **Forking past an unfinished reply.** A chat that held an interrupted reply anywhere in it refused every fork from then on and never recovered; forking now waits only on a reply actually being generated, and a turn paused for tool approval still forks with its prompt showing. [#30131](https://github.com/open-webui/open-webui/pull/30131), [#30128](https://github.com/open-webui/open-webui/issues/30128)

> ♻️ **Session pool cleanup.** The task that clears out abandoned websocket sessions now carries on through an error from Redis instead of ending for good, and stops properly at shutdown. [#29976](https://github.com/open-webui/open-webui/pull/29976), [#29979](https://github.com/open-webui/open-webui/pull/29979)

> 🔬 **Page fetch CPU spin.** Fetching a page through the browser-driven loader never returned where that page opened a WebSocket, holding a worker thread at full CPU for the life of the process and costing another core on every further fetch, which left the whole instance slow. [#30050](https://github.com/open-webui/open-webui/pull/30050), [#30024](https://github.com/open-webui/open-webui/issues/30024)

> 🔁 **Duplicate search tracebacks.** A vector database outage wrote a full traceback twice for every collection and query pair, turning one outage into hundreds of identical stack traces per message on every replica; a single record now names every collection that failed. [#29981](https://github.com/open-webui/open-webui/pull/29981)

> 🧯 **Page fetch logging.** Fetching a page through the browser-driven loader filled the log with tracebacks where the page closed while it was still pulling pieces of itself, as sites behind Cloudflare and similar do; those requests are now let go of before the page closes. [#29325](https://github.com/open-webui/open-webui/pull/29325), [#28869](https://github.com/open-webui/open-webui/issues/28869)

> 🧳 **Imported chats keep more.** A chat brought back from an export arrived unpinned and unarchived and without the variables it was saved with, and all three now survive the round trip. [#30155](https://github.com/open-webui/open-webui/pull/30155), [#30151](https://github.com/open-webui/open-webui/pull/30151)

> 🙈 **Folder filters with no match.** A chat search narrowed by a folder name that matches no folder now finds nothing, where the folder filter was quietly dropped and every chat came back. [#30273](https://github.com/open-webui/open-webui/pull/30273), [#29959](https://github.com/open-webui/open-webui/discussions/29959)

> 🚪 **Webhook pictures follow channel access.** The picture belonging to a channel webhook is now shown only to people with access to that channel, where anyone signed in could fetch it or be sent on to wherever it pointed, and it is refused outright where channels are turned off. [#29703](https://github.com/open-webui/open-webui/pull/29703)

> 🚦 **Citation link schemes.** A source attached to a reply now opens only where it points at a web address, falling back to the panel that shows the source rather than following anything else. [#29701](https://github.com/open-webui/open-webui/pull/29701)

> 🈚 **Citation chips inside formatted text.** A citation inside bold, italic or linked text now renders its chip, where the formatting took it and the citation vanished from the sentence. [#30278](https://github.com/open-webui/open-webui/pull/30278), [#30277](https://github.com/open-webui/open-webui/issues/30277)

> 🐍 **Saving a tool or function.** Saving a tool or function in the admin pages no longer fails with a missing module error from the built-in code formatter, which was not installing everything it needed. [#29503](https://github.com/open-webui/open-webui/pull/29503)

> 🛠️ **Tool request duplication.** A tool that writes through an address carrying part of its input no longer has that part repeated in the body of the request as well, which servers checking their input strictly turned away, so those calls now go through. [#29717](https://github.com/open-webui/open-webui/pull/29717), [#29716](https://github.com/open-webui/open-webui/issues/29716)

> 🔼 **Honest version checks.** An instance that cannot reach the release listing now says the check failed, instead of reporting whatever it is running as the newest version and recording nothing about it. [#29626](https://github.com/open-webui/open-webui/pull/29626), [#29580](https://github.com/open-webui/open-webui/issues/29580)

> 🧹 **Direct connections stop leaking listeners.** A server talking to a direct connection no longer leaves a listener behind for every request that ends any way but a clean finish, which grew without limit while a connection kept failing. [#29509](https://github.com/open-webui/open-webui/pull/29509)

> 📝 **Starting a note from search.** Starting a note from the search box now works when you are already on the notes page, keeps the whole of what you typed including characters such as ampersands and hashes, and no longer makes a further note each time the browser back button is pressed. [#29645](https://github.com/open-webui/open-webui/pull/29645), [#29642](https://github.com/open-webui/open-webui/issues/29642)

> 📊 **Single source relevance.** A reply drawing on a single source now shows how relevant that source is, where the figure appeared only once a second source joined it and so looked as though it came and went. [#29647](https://github.com/open-webui/open-webui/pull/29647), [#29646](https://github.com/open-webui/open-webui/issues/29646)

> ⌨️ **Literal arrow sequences.** A sequence such as three hyphens after a less-than sign is now shown as the characters it is made of rather than drawn as an arrow, which had text look changed when it never was. [#29595](https://github.com/open-webui/open-webui/pull/29595), [#29594](https://github.com/open-webui/open-webui/issues/29594)

> 🎨 **A tidier attach webpage dialog.** The row holding the Add button no longer carries a grey band of its own between the address box and the button, matching every other dialog. [#29664](https://github.com/open-webui/open-webui/pull/29664), [#29663](https://github.com/open-webui/open-webui/issues/29663)

> 🖱️ **A plain note date.** The date under a note title no longer shows a pointing hand or announces itself as something to press, having never done anything when clicked. [#29708](https://github.com/open-webui/open-webui/pull/29708)

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
- [[Changes/Open WebUI/2026-09-21-13-interface-experience-changes-in-v0-11-4|13 Interface Experience changes in v0.11.4]] · Interface Experience
- [[Changes/Open WebUI/2026-09-21-4-automation-and-scheduling-changes-in-v0-11-4|4 Automation and Scheduling changes in v0.11.4]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-09-21-41-model-support-changes-in-v0-11-4|41 Model Support changes in v0.11.4]] · Model Support
- [[Changes/Open WebUI/2026-09-21-5-enterprise-and-administration-changes-in-v0-11-4|5 Enterprise and Administration changes in v0.11.4]] · Enterprise and Administration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-710b75&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-61-other-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-710b75%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->