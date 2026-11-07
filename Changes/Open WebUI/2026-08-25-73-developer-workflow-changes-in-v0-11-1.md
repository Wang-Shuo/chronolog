---
card_id: open-webui-2026-08-25-c19a21
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Developer Workflow: 73 changes in v0.11.1
  — \U0001F587 **Agents can now display terminal files directly.** A model can now
  show a file it made…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2905
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a13b44eca2018f53b203e2caf9c73325859717d3204ae44080b817b5909cb75f
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-c19a21
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 73 Developer Workflow changes'
  evidence:
  - quote: "\U0001F587 **Agents can now display terminal files directly.** A model
      can now show a file it made in a terminal directly in its reply, with a preview
      and a download button, instead of describing a path that led nowhere when clicked,
      and a new interface setting chooses whether these open in the reply or in the
      files pane. [Commit](https://github.com/open-webui/open-webui/commit/78f48a21eef330c0b78c33f2b5fc2169b084997c),
      [Commit](https://github.com/open-webui/open-webui/commit/e623c02acc70c4ee5d7f2eb2f32d9b7f39287663),
      [Commit](https://github.com/open-webui/open-webui/commit/f64c0c87e8d1bfdbe060ea5e5a3dee24c0323657),
      [#27650](https://github.com/open-webui/open-webui/issues/27650)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FA7B **Faster tools on large instances.** Listing or exporting tools
      no longer checks every tool on the instance one at a time, so the integrations
      menu and the tools workspace open faster where many exist. [Commit](https://github.com/open-webui/open-webui/commit/4807866a1cf47340f1b5ea76fded95f8114305f9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5C3 **Cheaper attaching of sources and files to a reply.** Adding
      a source, file, or embedded item to a reply now reads just that one field rather
      than rebuilding the whole conversation to find it, which on a two hundred message
      chat is around 3.1 ms per item down to 0.65 ms, and no longer grows with the
      length of the conversation. [Commit](https://github.com/open-webui/open-webui/commit/536b9edec00547d5b84ef2e6ea0f929c054c1333),
      [Commit](https://github.com/open-webui/open-webui/commit/9dff5e93277aa1a2236d702e7e2f55dbb35ea7fa)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F50D **Smarter chat search.** Searching your chats now finds conversations
      containing all of your words in any order rather than only the exact phrase
      you typed, with exact matches still listed first, and the preview snippet points
      at whichever word it found. [Commit](https://github.com/open-webui/open-webui/commit/0800c21c64c64810f24c2ec88cca5e36daebb10e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4CE **Sending while attachments upload.** Sending a message before
      its files have finished uploading now queues it and sends it automatically once
      they are ready, instead of refusing with an error, and each queued message shows
      the progress of its attachments. [Commit](https://github.com/open-webui/open-webui/commit/6c4d0ace163a89aba6e8cd2aa9fef185167ebe0f),
      [Commit](https://github.com/open-webui/open-webui/commit/c1c07cbe0f847e4dd04e21f2a6c5f12cdc0fc7ee),
      [#28381](https://github.com/open-webui/open-webui/pull/28381), [#28380](https://github.com/open-webui/open-webui/issues/28380)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4BC **Attachments that go straight to a terminal.** A terminal
      connection can now be set to receive files attached in chat into its own working
      directory rather than into the conversation, which also means files can be attached
      while using a model that cannot read them itself. [Commit](https://github.com/open-webui/open-webui/commit/8a42aa53e826d5f25d6443ca95e0173e3cf034cf),
      [Commit](https://github.com/open-webui/open-webui/commit/d7d935275a77fb185586a5130cd37acf1175ca0a),
      [Commit](https://github.com/open-webui/open-webui/commit/1b3b9375bb4de0f360782dd2f9d8c7c2903b8baa),
      [Commit](https://github.com/open-webui/open-webui/commit/d17f06a23501e5c39cf98d9c9642178da25343fb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F526 **Searching files in the terminal browser.** The file browser
      now has a search box that finds files by name and by what is inside them, and
      opening a result takes you to the matching line. [Commit](https://github.com/open-webui/open-webui/commit/7abe11346a1cc309da2c3fcec2f61faaeb47b96a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F50E **Searching tools and skills in chat.** The integrations menu
      now has a search box for tools and for skills, so a long list can be narrowed
      by name instead of scrolled through. [#26709](https://github.com/open-webui/open-webui/issues/26709),
      [Commit](https://github.com/open-webui/open-webui/commit/954613944b317a78d5929456ae1388543aa052c8),
      [#28807](https://github.com/open-webui/open-webui/pull/28807), [#28812](https://github.com/open-webui/open-webui/pull/28812)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6A8 **Being told when a file fails to process.** A file that cannot
      be processed for a knowledge base now raises a notification naming the file
      and what went wrong, and keeps that reason on the file, instead of quietly being
      marked as failed. [#27666](https://github.com/open-webui/open-webui/pull/27666),
      [#6311](https://github.com/open-webui/open-webui/issues/6311), [Commit](https://github.com/open-webui/open-webui/commit/1a376ac17fa0c3f957656a997b6f8ffacb1f6f30)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F52C **Zoom controls on previewed images.** An image opened in the
      file browser now has zoom in, zoom out, and a reset button showing the current
      zoom, and pinching, scrolling, and holding a modifier key while scrolling now
      zoom and pan as they do elsewhere. [Commit](https://github.com/open-webui/open-webui/commit/2befa8f796266e92fa55861bb8eaa81639ff4053),
      [Commit](https://github.com/open-webui/open-webui/commit/bfb68feea766e8d5408fb6e278be56cbca0c4afe),
      [Commit](https://github.com/open-webui/open-webui/commit/ec9bf5a64f9f718e472123350ec83bce1b064884),
      [Commit](https://github.com/open-webui/open-webui/commit/467be93e6d7e4a31358f9c75ee67bfac1200c0a1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5C2️ **Recognisable file icons.** The terminal file browser now
      marks each file with an icon for its type, so code, images, archives, documents,
      and configuration files can be told apart at a glance instead of sharing one
      generic page icon. [Commit](https://github.com/open-webui/open-webui/commit/60feca71a6a77b7d1eef1c172a61624d5fe48150),
      [Commit](https://github.com/open-webui/open-webui/commit/8d25ad00e2fc5f0a328a2098c2e73fb00f2ca934),
      [Commit](https://github.com/open-webui/open-webui/commit/c1f914a6268580f7722825390ac8a204743a4520)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5DD **Deleting your API key.** An API key can now be revoked outright
      from your account settings, where the only way to retire one was to replace
      it with a new one. [#28874](https://github.com/open-webui/open-webui/issues/28874),
      [Commit](https://github.com/open-webui/open-webui/commit/b30b11d4c975b8ff9a6c6eb9e39fbb310aed1072)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F39A️ **Default interface settings for everyone.** Administrators
      can now set system-wide defaults for the interface options in Settings, either
      from the admin panel or through \"DEFAULT_INTERFACE_SETTINGS\", with each person's
      own choices still taking precedence and anything left untouched shown as inherited
      and kept in step with later changes to the defaults. [Commit](https://github.com/open-webui/open-webui/commit/37f2548155efdd5cd8114ceb9b57c7864de4bef2),
      [Commit](https://github.com/open-webui/open-webui/commit/13346c5f1621b014e2fcaabd41375d6f7035dd0a),
      [Commit](https://github.com/open-webui/open-webui/commit/90a0e61cef119154e89d900d6921123b599a0389),
      [Commit](https://github.com/open-webui/open-webui/commit/eeaf1a1df01525e4b6d4eb73060b32a9a75ebfc6),
      [Commit](https://github.com/open-webui/open-webui/commit/d4461bd6f39936460a989e8bd50097de604b4b00),
      [Commit](https://github.com/open-webui/open-webui/commit/b4d3b27caf1587b783a46268c769132eb9211c80),
      [Commit](https://github.com/open-webui/open-webui/commit/407c40f72cdadcd9f57538d9ce38070662ce42c7),
      [Commit](https://github.com/open-webui/open-webui/commit/724d2ebbf1bd2fc90f27a2e5bc571d40afc3db4c),
      [Commit](https://github.com/open-webui/open-webui/commit/1674e5a9ef835696f0963cdbcf477c8b92ce0b8a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F512 **Read-only files in the terminal browser.** Files and folders
      you are not allowed to change are now labelled read-only, with uploading, editing,
      renaming, moving, and deleting turned off for them rather than failing at the
      moment you try. [Commit](https://github.com/open-webui/open-webui/commit/2dadc5435af77b0638af69200e3af1b9654417b6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FAA4 **Control over what embedded pages may do.** Two new interface
      settings decide whether pages shown inside a chat, such as an artifact or an
      HTML preview, may run scripts and start downloads. [Commit](https://github.com/open-webui/open-webui/commit/3c66d639e31ba8a7477d337b37d8d671ea2430cf),
      [#28924](https://github.com/open-webui/open-webui/issues/28924), [Commit](https://github.com/open-webui/open-webui/commit/842c1f9d677c0d9940cccdd18e34add13f746a68)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5C4 **Keeping files removed from a knowledge base.** A new \"ENABLE_KNOWLEDGE_FILE_RETENTION\"
      setting keeps the stored file and its search data when a file is taken out of
      a knowledge base, rather than deleting them. [Commit](https://github.com/open-webui/open-webui/commit/363ad352fec9553469852d111bc0506b896504a6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FA9B **Naming background worker threads.** A new \"THREAD_POOL_THREAD_NAME_PREFIX\"
      setting labels the threads that background work runs in, so they can be told
      apart when reading a profile or a thread dump. [Commit](https://github.com/open-webui/open-webui/commit/4ec6ee14418edd04eaba9e34bd5868453f61df40)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F30D **Pointing Tavily somewhere else.** A new \"TAVILY_API_BASE_URL\"
      setting sends Tavily searches and page fetches to a different address, for instances
      that reach the internet only through a gateway of their own or that use a compatible
      service. [Commit](https://github.com/open-webui/open-webui/commit/98ee2bdfd3e90faec6bfe8e7ebf5803159f379e3),
      [#28701](https://github.com/open-webui/open-webui/issues/28701)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4CF **Widening the chat controls pane.** The controls pane can
      now be dragged as wide as you like, where it stopped at a fixed limit regardless
      of screen size. [Commit](https://github.com/open-webui/open-webui/commit/0fb542b3764cefecf2366607a4685288051d1b46)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ✍️ **Typing cursor while responding.** A blinking cursor now marks where
      the reply is being written, from the moment you send your message until generation
      finishes, in place of the previous loading placeholder. [Commit](https://github.com/open-webui/open-webui/commit/cbb3aade2b4e901c22aa9a30530634721c80b078)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4E5 **Adding group members from a file.** Administrators can now
      add many people to a group at once by uploading a CSV of names and email addresses,
      with a template to download and a message naming any row whose address does
      not match an account. [Commit](https://github.com/open-webui/open-webui/commit/f3f7659da754b51c216b17b2d6def4d59071d78f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⌛ **Expiring abandoned reply state.** A new "REDIS_RESPONSE_STREAM_TTL"
      setting expires the saved state of a reply that never finished, so a server
      killed mid-answer no longer leaves that data behind for good. [Commit](https://github.com/open-webui/open-webui/commit/176fa462128d5298492db29c67080a4e1afc2642)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4A8 **No filter work on installs without filters.** A completed
      message on an install with no filter functions and no pipeline filters, which
      is the default, no longer rebuilds the whole conversation and ships it to the
      browser as an event nothing acts on. [Commit](https://github.com/open-webui/open-webui/commit/28f2965934f5b6fba0e0c38a15b2af6ee790819f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4C2 **Opening a file in a knowledge base.** A file listed in a
      knowledge base can now be opened and read straight from that list, where the
      name was shown but nothing happened when it was clicked. [Commit](https://github.com/open-webui/open-webui/commit/20f35d157bc7d535091ce6a90b517c23d26486c0),
      [#28086](https://github.com/open-webui/open-webui/issues/28086)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F579️ **Control over what a terminal port preview may reach.** A
      new interface setting decides whether a previewed port runs with access to same-origin
      browser APIs, so you can lock a preview out of them on installs where previews
      serve content you do not fully trust. [Commit](https://github.com/open-webui/open-webui/commit/54d7a223707f03172efbb9e754db6e69709956d0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6C2 **Knowledge search reaching past what you may read.** Searching
      knowledge bases now applies the list of collections you are allowed to open,
      where that restriction was handed to the vector store and silently discarded,
      so results could include material from knowledge bases you have no access to.
      [Commit](https://github.com/open-webui/open-webui/commit/1d6d4e6e6647e1d403438ede7bd9ba20bc4cc8f6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9E8 **Searching a knowledge base with a costly pattern.** A search
      pattern written so that it expands enormously before it even runs is now refused,
      where it could tie up the server; ordinary patterns are unaffected. [Commit](https://github.com/open-webui/open-webui/commit/d5b66533e7829654f6fb343abbaaeab988dbfde8),
      [#28284](https://github.com/open-webui/open-webui/pull/28284)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4E5 **Queued messages disappearing.** Messages waiting to be sent
      are put back in the queue if sending them fails, rather than vanishing without
      being sent. [Commit](https://github.com/open-webui/open-webui/commit/f79b443c226098564386d0a31708e71ec0146158)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F30A **Replies arriving in oversized pieces.** Very large streamed
      pieces no longer break the response on default settings, where the reader that
      splits them safely only ran when a chunk size limit was configured. [Commit](https://github.com/open-webui/open-webui/commit/a33fa05adc6def8f3d098539a4786dc9c7bf61d2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F50C **Role changes taking effect at once.** Changing someone's
      role now ends their live sessions no matter how the change was made, whether
      by a directory sync, an identity provider, a trusted header, or deleting the
      account, so permissions from their old role cannot linger, and their browser
      reconnects on its own. [Commit](https://github.com/open-webui/open-webui/commit/ce3c175e260709f359d7e6cbb3132f0572098b95)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F50E **Chat search finding recent messages.** Searching your chats
      now looks inside the messages of current conversations on default installations,
      where it had only been reading an older storage format and missing their content
      entirely. [Commit](https://github.com/open-webui/open-webui/commit/0800c21c64c64810f24c2ec88cca5e36daebb10e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9ED **Your place in a compacted chat.** Opening a conversation
      whose history has been compacted now takes you to its most recent message instead
      of leaving you parked on the summary, and updates to an existing message no
      longer move your place in the conversation. [Commit](https://github.com/open-webui/open-webui/commit/5caa91a49304148696641d1cd39e43184ba8d748)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5A5️ **Chats with a personal terminal.** Sending a message with
      a terminal you added yourself under Settings selected no longer fails with a
      terminal unavailable error, which had blocked those chats since 0.11.0. [#27621](https://github.com/open-webui/open-webui/issues/27621),
      [Commit](https://github.com/open-webui/open-webui/commit/5b333d75c6adea4d8bde96439974d6e9c83d8198),
      [Commit](https://github.com/open-webui/open-webui/commit/3becec6ccfc7dc457270d4e9f0d8c957e8160ddc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5D3️ **Recurring event times.** Repeating calendar events now show
      at the time you set them for instead of being worked out in the server's time
      zone and shifted by the gap between the two. [#27774](https://github.com/open-webui/open-webui/issues/27774),
      [Commit](https://github.com/open-webui/open-webui/commit/d721b0d19621d01e35505105a778ce5681b2ffba)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9EE **JSON options honoured again.** Options passed to the shared
      JSON helper are no longer silently ignored when the \"ENABLE_ORJSON\" option
      is turned on, falling back to the standard encoder that supports them. [Commit](https://github.com/open-webui/open-webui/commit/78ed5a0235c4de67828ba4b0d6147035067cec2c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4C1 **Dragging chats into shared folders.** A shared folder you
      can write to now highlights and accepts a dropped chat, while one you only have
      read access to no longer offers itself as a drop target for an action that could
      only fail. [Commit](https://github.com/open-webui/open-webui/commit/e4dd6c4bf14c7ea54c1effa6c40ad9e95185c413),
      [#28261](https://github.com/open-webui/open-webui/issues/28261)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4DD **Notes saved in an unexpected shape.** A note whose content
      was stored as structured data rather than text no longer breaks the notes page
      for everything else, and opens with that content shown as a formatted code block.
      [Commit](https://github.com/open-webui/open-webui/commit/8d1c205d8e7335ef7c292afb125a7270976f327b),
      [#28222](https://github.com/open-webui/open-webui/issues/28222)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4AC **Direct messages after an account is deleted.** A direct message
      conversation no longer counts a deleted account among its members, and opening
      a direct message with someone finds the existing conversation instead of starting
      a second one alongside it. [Commit](https://github.com/open-webui/open-webui/commit/a41faa3c226b20e7db7508c49c7d1d015ac9e973),
      [#28257](https://github.com/open-webui/open-webui/issues/28257)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F587️ **Adding terminals over plain connections.** Saving a terminal
      connection now works when the interface is served without HTTPS, where the dialog
      would sit there doing nothing because the browser withholds the tool used to
      generate its identifier. [Commit](https://github.com/open-webui/open-webui/commit/2a45fa04cb1d07b258e0b880ab0c02577f0dc035),
      [#28148](https://github.com/open-webui/open-webui/issues/28148)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6C2 **Connecting external accounts.** Authorizing a tool's external
      account now completes only for the person who started it, rather than for whoever
      happens to return with the authorization, and signing out clears the session
      it relies on. [Commit](https://github.com/open-webui/open-webui/commit/c2107e5bb3689a69c170ca526925f4ed84bd00f5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ✂️ **Clipped icons and avatars.** The terminal icon beside the message
      box and the profile picture in account settings are no longer shaved flat along
      their left edge. [#27691](https://github.com/open-webui/open-webui/pull/27691),
      [#27690](https://github.com/open-webui/open-webui/issues/27690)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5B1️ **Sections opening by accident.** Folders, collapsible sections,
      and tool call blocks now open and close only when you click them, rather than
      also reacting when you release the mouse over them after dragging or selecting
      text. [Commit](https://github.com/open-webui/open-webui/commit/bd250a0e2431f8c2c7e2f4a34c5327f21fc77d4b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4CC **Attaching a chat shared with you.** Attaching a conversation
      that was shared with you, directly or through a shared folder, now brings its
      content along instead of quietly attaching nothing. [Commit](https://github.com/open-webui/open-webui/commit/5cd9a395344e882b4384bec0899f503ad540aecc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9F9 **Session cleanup on multi-instance setups.** The instance
      doing the periodic session cleanup now keeps its claim on that job alive between
      passes, so an idle deployment stops logging a renewal warning every two minutes
      and the claim no longer lapses for half of every cycle. [Commit](https://github.com/open-webui/open-webui/commit/939bcdb79e3dcad2278f1e7f4f517a3f2f36f3ec),
      [#27762](https://github.com/open-webui/open-webui/issues/27762)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F3E0 **Starting folder in the file browser.** Reopening the file
      browser now keeps the folder you were in, instead of the breadcrumb losing its
      starting point and jumping you elsewhere. [Commit](https://github.com/open-webui/open-webui/commit/52c5e3b20d3cd8c3a15db50e2cc75bbd6e82068e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⏹️ **Stopping a reply that is waiting.** The stop button now ends a reply
      that is sitting waiting for you, such as one paused on a tool approval, rather
      than leaving the conversation stuck part way through. [Commit](https://github.com/open-webui/open-webui/commit/f7767d6be774720e16265c6d016bf6a24a1a8759)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F570️ **Saving a calendar event without a date.** Creating or editing
      an event with the date cleared now asks for one, where it was sent anyway, refused
      by the server, and reported as an unreadable error. [Commit](https://github.com/open-webui/open-webui/commit/f100edb70874808c93fab84eae1810595f9e9dc3),
      [#28133](https://github.com/open-webui/open-webui/issues/28133)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F58A️ **Message buttons in channels.** The buttons that appear when
      you hover a channel message now sit above the message rather than over its content,
      so they can be clicked on a message that starts with a code block or a table,
      and so the code and table controls stay clickable too. [#27737](https://github.com/open-webui/open-webui/pull/27737),
      [#27736](https://github.com/open-webui/open-webui/issues/27736)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FAE7 **Attachments replaced by a loading dot.** Pinning a channel
      message, or otherwise updating one, no longer replaces its attachment with a
      loading indicator that never resolves until you reload or leave the channel.
      [Commit](https://github.com/open-webui/open-webui/commit/76d01602950a9e40823b53278557708d5bcd1036),
      [#27734](https://github.com/open-webui/open-webui/pull/27734), [#27731](https://github.com/open-webui/open-webui/issues/27731)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6E0️ **Rebuilding empty server lists on every request.** An instance
      with no tool servers or no terminal servers configured no longer rebuilds that
      empty list on every request that needs it. [Commit](https://github.com/open-webui/open-webui/commit/f1a64ccfc2eb2a58086c55fe413a455bb488c35a),
      [#28568](https://github.com/open-webui/open-webui/issues/28568)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FAAB **Errors logged for a cache that was simply empty.** A shared
      cache that has not been filled yet no longer logs an error suggesting its stored
      value is broken. [Commit](https://github.com/open-webui/open-webui/commit/f1a64ccfc2eb2a58086c55fe413a455bb488c35a),
      [#28568](https://github.com/open-webui/open-webui/issues/28568)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FAC2 **Signing in from another application.** Signing in through
      an application that exchanges a token from your identity provider now applies
      your role and group memberships the same way signing in through the browser
      does, and an account whose provider sends no role keeps the one it has rather
      than being reset to the default. [Commit](https://github.com/open-webui/open-webui/commit/d799e81edbdc971c6deb096b6474cd95b93504bf),
      [Commit](https://github.com/open-webui/open-webui/commit/e9684458125c3202ebc3378aef32f0b6015171d8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6A7 **The files pane reopening by itself.** With a terminal selected,
      closing the files pane now keeps it closed, where saving any setting reopened
      it, including something as incidental as picking an emoji for a folder. [#28693](https://github.com/open-webui/open-webui/pull/28693),
      [#28691](https://github.com/open-webui/open-webui/issues/28691), [Commit](https://github.com/open-webui/open-webui/commit/c1c81f8127466a4cd59a16d8658155b1b8faa2d0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5DC️ **Embedding settings for other providers.** Saving your embedding
      settings now writes only the provider you have selected, where it also overwrote
      the address and key stored for the other two, losing them if their fields were
      not filled in. [Commit](https://github.com/open-webui/open-webui/commit/87d9b7e84e71b097eadf1df4f9852359104f17ed)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ↔ **Dragging a side panel closed.** Dragging the chat controls, the note
      chat, or a channel thread panel closed by its edge no longer floods the browser
      console with errors and leaves stray handlers behind, and the divider can now
      be moved with the arrow keys once focused. [#28759](https://github.com/open-webui/open-webui/issues/28759),
      [Commit](https://github.com/open-webui/open-webui/commit/33dff414e829d10dc6691b1cac7457077fa6799c)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ❌ **Tool calls that failed looking successful.** A tool call that returned
      an error is now marked as failed with a red cross rather than a green tick,
      so a reply built on a failed call is easier to spot. [Commit](https://github.com/open-webui/open-webui/commit/f3f76095d18e07a3a944f22a4b25993bbffe90a3),
      [#28016](https://github.com/open-webui/open-webui/issues/28016)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5DC **Download links in a cited source doing nothing.** A link
      in a citation shown as formatted content now downloads the file when clicked,
      where it silently did nothing at all. [Commit](https://github.com/open-webui/open-webui/commit/3c66d639e31ba8a7477d337b37d8d671ea2430cf),
      [#28924](https://github.com/open-webui/open-webui/issues/28924)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5A5 **Stopping a reply after the shared cache restarts.** Stopping
      a reply now keeps working across a cluster after the shared cache restarts or
      its connection drops, where the part that carries a stop between instances gave
      up for good and silently, and only restarting the application brought it back.
      [Commit](https://github.com/open-webui/open-webui/commit/bf3a58dbcd18ddc2c7f130d8f9529477fe7cb042),
      [#28909](https://github.com/open-webui/open-webui/issues/28909)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5C2 **Directory sync listing local accounts.** A directory service
      syncing accounts over SCIM now sees only the accounts that came from a directory,
      where it also listed and could modify accounts created with a password in Open
      WebUI itself. [Commit](https://github.com/open-webui/open-webui/commit/fb4f476316a2f83e4d2914d535c19b3440cbc490)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ↕ **Sorting a list of people.** Sorting the admin user list, or a channel's
      member list, now works when no search term has been entered, where the chosen
      order was ignored unless something was being searched for. [Commit](https://github.com/open-webui/open-webui/commit/fb4f476316a2f83e4d2914d535c19b3440cbc490)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F58A **Dragging a side panel wider than the window.** A side panel
      can no longer be dragged so wide that the chat beside it is squeezed away, and
      dragging one below its minimum width now closes it rather than sticking. [Commit](https://github.com/open-webui/open-webui/commit/ef455fcef9d6cb1136275c26e49bc3c5d6661795),
      [#28965](https://github.com/open-webui/open-webui/issues/28965)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9FB **Logs flooded by an unreachable server.** A terminal or tool
      server that cannot be reached now records one line per attempt rather than a
      full stack trace, where a few minutes of downtime could fill the log with hundreds
      of megabytes and drown out everything else. [#27755](https://github.com/open-webui/open-webui/pull/27755),
      [#27751](https://github.com/open-webui/open-webui/issues/27751), [#27757](https://github.com/open-webui/open-webui/pull/27757),
      [#27756](https://github.com/open-webui/open-webui/issues/27756)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FAA3 **Files left behind when a knowledge base is emptied.** Emptying
      a knowledge base now removes the files it held, along with their stored copies
      and their search data, where all three were left behind with nothing in the
      interface to clear them. [Commit](https://github.com/open-webui/open-webui/commit/363ad352fec9553469852d111bc0506b896504a6),
      [#27988](https://github.com/open-webui/open-webui/issues/27988)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F58D **Clearing the supported media types.** Emptying the supported
      media types in the documents settings now stays empty, where the previous value
      came back on the next visit, so images kept being sent to the extraction engine
      instead of straight to a model that can read them. [#28750](https://github.com/open-webui/open-webui/pull/28750),
      [#28747](https://github.com/open-webui/open-webui/issues/28747), [Commit](https://github.com/open-webui/open-webui/commit/ecad20b77f9bd700bd818a2f447176f5994320c3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5B2 **Filtering while on a later page.** Changing a filter in the
      workspace, such as showing only what you created, now returns to the first page,
      where the list could come back empty with the page controls gone and no way
      back. [#28734](https://github.com/open-webui/open-webui/issues/28734), [Commit](https://github.com/open-webui/open-webui/commit/a914868e3c83b08be1399dbae1e4da25a0c00c87)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F3A7 **Who a channel says its members are.** The member list of
      a channel now includes its owner and everyone in a group that was granted access,
      where the owner never appeared and granting both a person and a group they were
      not in listed nobody at all while the count beside it said two. [#28289](https://github.com/open-webui/open-webui/pull/28289),
      [#28288](https://github.com/open-webui/open-webui/issues/28288), [Commit](https://github.com/open-webui/open-webui/commit/e3e82b14714661ba5bd24e2c47e42cef5594b132)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F46A **Group member counts updating.** Adding or removing someone
      from a group in the admin panel now updates that group's member count straight
      away, where it stayed at the old number until the page was reloaded. [Commit](https://github.com/open-webui/open-webui/commit/18bf0ade7b35fb25ff7920ad3713624d93f04401)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F92B **Replies stopping silently after a tool ran.** When a provider
      rejects the follow-up request made after a tool finishes, the reason is now
      shown in the chat instead of the reply simply ending with nothing said. [Commit](https://github.com/open-webui/open-webui/commit/a610d77137fabf60a2e0daa961a8ef8f7320293a),
      [#28633](https://github.com/open-webui/open-webui/issues/28633)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F50C **Stream filters on direct API calls.** A filter reading a
      streamed event as an object now works on requests made straight to the chat
      completions endpoint, matching every other path, where it used to raise and
      end the reply partway. [Commit](https://github.com/open-webui/open-webui/commit/684111715f742f56a3c7efac9eb7a1e68e54a3ec)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F3CB️ **What \"THREAD_POOL_SIZE\" now sizes.** The setting now governs
      both of the pools that background work runs in, where it previously governed
      only one and the other, carrying most of the blocking work including knowledge
      searches, sign-ins and file storage, was fixed at a small ceiling no setting
      could raise, so an instance that set it high will now use more threads than
      before, up to twice the configured value across the two pools, and one that
      relied on the old ceiling to hold thread use down should review it. [Commit](https://github.com/open-webui/open-webui/commit/4ec6ee14418edd04eaba9e34bd5868453f61df40),
      [#28168](https://github.com/open-webui/open-webui/issues/28168)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4BE **Saving replies as they stream.** The \"ENABLE_REALTIME_CHAT_SAVE\"
      setting no longer has any effect, because a reply in progress is now held outside
      the database and written once when it finishes. [Commit](https://github.com/open-webui/open-webui/commit/a1579a01ff43cacb357269707d36267ad35e01d6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6E1 **Forms in embedded pages now work by default.** A page shown
      inside a chat, such as an artifact or an HTML preview, may now submit forms
      unless you turn that off, where it was blocked unless you turned it on. [Commit](https://github.com/open-webui/open-webui/commit/3c66d639e31ba8a7477d337b37d8d671ea2430cf)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4CA **Default usage statistics range.** Usage statistics now cover
      the past two years by default for everyone, instead of starting from the date
      the account was created. [Commit](https://github.com/open-webui/open-webui/commit/8dbbc206c5a0706789722c42827479e5db10bb2b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 73-developer-workflow-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: developer-workflow
  title: 73 Developer Workflow changes in v0.11.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-25-2-developer-workflow-changes-in-v2-1-246|2 Developer
  Workflow changes in v2.1.246]]'
- '[[Changes/Dify/2026-08-25-4-developer-workflow-changes-in-1-17-0|4 Developer Workflow
  changes in 1.17.0]]'
- '[[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-24935-force-terminal-buffer-rerender-after-exiting-external|SSR
  Agent Issue Fix (24935)]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: developer-workflow
title: 73 Developer Workflow changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 73 Developer Workflow changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🖇 **Agents can now display terminal files directly.** A model can now show a file it made in a terminal directly in its reply, with a preview and a download button, instead of describing a path that led nowhere when clicked, and a new interface setting chooses whether these open in the reply or in the files pane. [Commit](https://github.com/open-webui/open-webui/commit/78f48a21eef330c0b78c33f2b5fc2169b084997c), [Commit](https://github.com/open-webui/open-webui/commit/e623c02acc70c4ee5d7f2eb2f32d9b7f39287663), [Commit](https://github.com/open-webui/open-webui/commit/f64c0c87e8d1bfdbe060ea5e5a3dee24c0323657), [#27650](https://github.com/open-webui/open-webui/issues/27650)

> 🩻 **Faster tools on large instances.** Listing or exporting tools no longer checks every tool on the instance one at a time, so the integrations menu and the tools workspace open faster where many exist. [Commit](https://github.com/open-webui/open-webui/commit/4807866a1cf47340f1b5ea76fded95f8114305f9)

> 🗃 **Cheaper attaching of sources and files to a reply.** Adding a source, file, or embedded item to a reply now reads just that one field rather than rebuilding the whole conversation to find it, which on a two hundred message chat is around 3.1 ms per item down to 0.65 ms, and no longer grows with the length of the conversation. [Commit](https://github.com/open-webui/open-webui/commit/536b9edec00547d5b84ef2e6ea0f929c054c1333), [Commit](https://github.com/open-webui/open-webui/commit/9dff5e93277aa1a2236d702e7e2f55dbb35ea7fa)

> 🔍 **Smarter chat search.** Searching your chats now finds conversations containing all of your words in any order rather than only the exact phrase you typed, with exact matches still listed first, and the preview snippet points at whichever word it found. [Commit](https://github.com/open-webui/open-webui/commit/0800c21c64c64810f24c2ec88cca5e36daebb10e)

> 📎 **Sending while attachments upload.** Sending a message before its files have finished uploading now queues it and sends it automatically once they are ready, instead of refusing with an error, and each queued message shows the progress of its attachments. [Commit](https://github.com/open-webui/open-webui/commit/6c4d0ace163a89aba6e8cd2aa9fef185167ebe0f), [Commit](https://github.com/open-webui/open-webui/commit/c1c07cbe0f847e4dd04e21f2a6c5f12cdc0fc7ee), [#28381](https://github.com/open-webui/open-webui/pull/28381), [#28380](https://github.com/open-webui/open-webui/issues/28380)

> 💼 **Attachments that go straight to a terminal.** A terminal connection can now be set to receive files attached in chat into its own working directory rather than into the conversation, which also means files can be attached while using a model that cannot read them itself. [Commit](https://github.com/open-webui/open-webui/commit/8a42aa53e826d5f25d6443ca95e0173e3cf034cf), [Commit](https://github.com/open-webui/open-webui/commit/d7d935275a77fb185586a5130cd37acf1175ca0a), [Commit](https://github.com/open-webui/open-webui/commit/1b3b9375bb4de0f360782dd2f9d8c7c2903b8baa), [Commit](https://github.com/open-webui/open-webui/commit/d17f06a23501e5c39cf98d9c9642178da25343fb)

> 🔦 **Searching files in the terminal browser.** The file browser now has a search box that finds files by name and by what is inside them, and opening a result takes you to the matching line. [Commit](https://github.com/open-webui/open-webui/commit/7abe11346a1cc309da2c3fcec2f61faaeb47b96a)

> 🔎 **Searching tools and skills in chat.** The integrations menu now has a search box for tools and for skills, so a long list can be narrowed by name instead of scrolled through. [#26709](https://github.com/open-webui/open-webui/issues/26709), [Commit](https://github.com/open-webui/open-webui/commit/954613944b317a78d5929456ae1388543aa052c8), [#28807](https://github.com/open-webui/open-webui/pull/28807), [#28812](https://github.com/open-webui/open-webui/pull/28812)

> 🚨 **Being told when a file fails to process.** A file that cannot be processed for a knowledge base now raises a notification naming the file and what went wrong, and keeps that reason on the file, instead of quietly being marked as failed. [#27666](https://github.com/open-webui/open-webui/pull/27666), [#6311](https://github.com/open-webui/open-webui/issues/6311), [Commit](https://github.com/open-webui/open-webui/commit/1a376ac17fa0c3f957656a997b6f8ffacb1f6f30)

> 🔬 **Zoom controls on previewed images.** An image opened in the file browser now has zoom in, zoom out, and a reset button showing the current zoom, and pinching, scrolling, and holding a modifier key while scrolling now zoom and pan as they do elsewhere. [Commit](https://github.com/open-webui/open-webui/commit/2befa8f796266e92fa55861bb8eaa81639ff4053), [Commit](https://github.com/open-webui/open-webui/commit/bfb68feea766e8d5408fb6e278be56cbca0c4afe), [Commit](https://github.com/open-webui/open-webui/commit/ec9bf5a64f9f718e472123350ec83bce1b064884), [Commit](https://github.com/open-webui/open-webui/commit/467be93e6d7e4a31358f9c75ee67bfac1200c0a1)

> 🗂️ **Recognisable file icons.** The terminal file browser now marks each file with an icon for its type, so code, images, archives, documents, and configuration files can be told apart at a glance instead of sharing one generic page icon. [Commit](https://github.com/open-webui/open-webui/commit/60feca71a6a77b7d1eef1c172a61624d5fe48150), [Commit](https://github.com/open-webui/open-webui/commit/8d25ad00e2fc5f0a328a2098c2e73fb00f2ca934), [Commit](https://github.com/open-webui/open-webui/commit/c1f914a6268580f7722825390ac8a204743a4520)

> 🗝 **Deleting your API key.** An API key can now be revoked outright from your account settings, where the only way to retire one was to replace it with a new one. [#28874](https://github.com/open-webui/open-webui/issues/28874), [Commit](https://github.com/open-webui/open-webui/commit/b30b11d4c975b8ff9a6c6eb9e39fbb310aed1072)

> 🎚️ **Default interface settings for everyone.** Administrators can now set system-wide defaults for the interface options in Settings, either from the admin panel or through "DEFAULT_INTERFACE_SETTINGS", with each person's own choices still taking precedence and anything left untouched shown as inherited and kept in step with later changes to the defaults. [Commit](https://github.com/open-webui/open-webui/commit/37f2548155efdd5cd8114ceb9b57c7864de4bef2), [Commit](https://github.com/open-webui/open-webui/commit/13346c5f1621b014e2fcaabd41375d6f7035dd0a), [Commit](https://github.com/open-webui/open-webui/commit/90a0e61cef119154e89d900d6921123b599a0389), [Commit](https://github.com/open-webui/open-webui/commit/eeaf1a1df01525e4b6d4eb73060b32a9a75ebfc6), [Commit](https://github.com/open-webui/open-webui/commit/d4461bd6f39936460a989e8bd50097de604b4b00), [Commit](https://github.com/open-webui/open-webui/commit/b4d3b27caf1587b783a46268c769132eb9211c80), [Commit](https://github.com/open-webui/open-webui/commit/407c40f72cdadcd9f57538d9ce38070662ce42c7), [Commit](https://github.com/open-webui/open-webui/commit/724d2ebbf1bd2fc90f27a2e5bc571d40afc3db4c), [Commit](https://github.com/open-webui/open-webui/commit/1674e5a9ef835696f0963cdbcf477c8b92ce0b8a)

> 🔒 **Read-only files in the terminal browser.** Files and folders you are not allowed to change are now labelled read-only, with uploading, editing, renaming, moving, and deleting turned off for them rather than failing at the moment you try. [Commit](https://github.com/open-webui/open-webui/commit/2dadc5435af77b0638af69200e3af1b9654417b6)

> 🪤 **Control over what embedded pages may do.** Two new interface settings decide whether pages shown inside a chat, such as an artifact or an HTML preview, may run scripts and start downloads. [Commit](https://github.com/open-webui/open-webui/commit/3c66d639e31ba8a7477d337b37d8d671ea2430cf), [#28924](https://github.com/open-webui/open-webui/issues/28924), [Commit](https://github.com/open-webui/open-webui/commit/842c1f9d677c0d9940cccdd18e34add13f746a68)

> 🗄 **Keeping files removed from a knowledge base.** A new "ENABLE_KNOWLEDGE_FILE_RETENTION" setting keeps the stored file and its search data when a file is taken out of a knowledge base, rather than deleting them. [Commit](https://github.com/open-webui/open-webui/commit/363ad352fec9553469852d111bc0506b896504a6)

> 🪛 **Naming background worker threads.** A new "THREAD_POOL_THREAD_NAME_PREFIX" setting labels the threads that background work runs in, so they can be told apart when reading a profile or a thread dump. [Commit](https://github.com/open-webui/open-webui/commit/4ec6ee14418edd04eaba9e34bd5868453f61df40)

> 🌍 **Pointing Tavily somewhere else.** A new "TAVILY_API_BASE_URL" setting sends Tavily searches and page fetches to a different address, for instances that reach the internet only through a gateway of their own or that use a compatible service. [Commit](https://github.com/open-webui/open-webui/commit/98ee2bdfd3e90faec6bfe8e7ebf5803159f379e3), [#28701](https://github.com/open-webui/open-webui/issues/28701)

> 📏 **Widening the chat controls pane.** The controls pane can now be dragged as wide as you like, where it stopped at a fixed limit regardless of screen size. [Commit](https://github.com/open-webui/open-webui/commit/0fb542b3764cefecf2366607a4685288051d1b46)

> ✍️ **Typing cursor while responding.** A blinking cursor now marks where the reply is being written, from the moment you send your message until generation finishes, in place of the previous loading placeholder. [Commit](https://github.com/open-webui/open-webui/commit/cbb3aade2b4e901c22aa9a30530634721c80b078)

> 📥 **Adding group members from a file.** Administrators can now add many people to a group at once by uploading a CSV of names and email addresses, with a template to download and a message naming any row whose address does not match an account. [Commit](https://github.com/open-webui/open-webui/commit/f3f7659da754b51c216b17b2d6def4d59071d78f)

> ⌛ **Expiring abandoned reply state.** A new "REDIS_RESPONSE_STREAM_TTL" setting expires the saved state of a reply that never finished, so a server killed mid-answer no longer leaves that data behind for good. [Commit](https://github.com/open-webui/open-webui/commit/176fa462128d5298492db29c67080a4e1afc2642)

> 💨 **No filter work on installs without filters.** A completed message on an install with no filter functions and no pipeline filters, which is the default, no longer rebuilds the whole conversation and ships it to the browser as an event nothing acts on. [Commit](https://github.com/open-webui/open-webui/commit/28f2965934f5b6fba0e0c38a15b2af6ee790819f)

> 📂 **Opening a file in a knowledge base.** A file listed in a knowledge base can now be opened and read straight from that list, where the name was shown but nothing happened when it was clicked. [Commit](https://github.com/open-webui/open-webui/commit/20f35d157bc7d535091ce6a90b517c23d26486c0), [#28086](https://github.com/open-webui/open-webui/issues/28086)

> 🕹️ **Control over what a terminal port preview may reach.** A new interface setting decides whether a previewed port runs with access to same-origin browser APIs, so you can lock a preview out of them on installs where previews serve content you do not fully trust. [Commit](https://github.com/open-webui/open-webui/commit/54d7a223707f03172efbb9e754db6e69709956d0)

> 🛂 **Knowledge search reaching past what you may read.** Searching knowledge bases now applies the list of collections you are allowed to open, where that restriction was handed to the vector store and silently discarded, so results could include material from knowledge bases you have no access to. [Commit](https://github.com/open-webui/open-webui/commit/1d6d4e6e6647e1d403438ede7bd9ba20bc4cc8f6)

> 🧨 **Searching a knowledge base with a costly pattern.** A search pattern written so that it expands enormously before it even runs is now refused, where it could tie up the server; ordinary patterns are unaffected. [Commit](https://github.com/open-webui/open-webui/commit/d5b66533e7829654f6fb343abbaaeab988dbfde8), [#28284](https://github.com/open-webui/open-webui/pull/28284)

> 📥 **Queued messages disappearing.** Messages waiting to be sent are put back in the queue if sending them fails, rather than vanishing without being sent. [Commit](https://github.com/open-webui/open-webui/commit/f79b443c226098564386d0a31708e71ec0146158)

> 🌊 **Replies arriving in oversized pieces.** Very large streamed pieces no longer break the response on default settings, where the reader that splits them safely only ran when a chunk size limit was configured. [Commit](https://github.com/open-webui/open-webui/commit/a33fa05adc6def8f3d098539a4786dc9c7bf61d2)

> 🔌 **Role changes taking effect at once.** Changing someone's role now ends their live sessions no matter how the change was made, whether by a directory sync, an identity provider, a trusted header, or deleting the account, so permissions from their old role cannot linger, and their browser reconnects on its own. [Commit](https://github.com/open-webui/open-webui/commit/ce3c175e260709f359d7e6cbb3132f0572098b95)

> 🔎 **Chat search finding recent messages.** Searching your chats now looks inside the messages of current conversations on default installations, where it had only been reading an older storage format and missing their content entirely. [Commit](https://github.com/open-webui/open-webui/commit/0800c21c64c64810f24c2ec88cca5e36daebb10e)

> 🧭 **Your place in a compacted chat.** Opening a conversation whose history has been compacted now takes you to its most recent message instead of leaving you parked on the summary, and updates to an existing message no longer move your place in the conversation. [Commit](https://github.com/open-webui/open-webui/commit/5caa91a49304148696641d1cd39e43184ba8d748)

> 🖥️ **Chats with a personal terminal.** Sending a message with a terminal you added yourself under Settings selected no longer fails with a terminal unavailable error, which had blocked those chats since 0.11.0. [#27621](https://github.com/open-webui/open-webui/issues/27621), [Commit](https://github.com/open-webui/open-webui/commit/5b333d75c6adea4d8bde96439974d6e9c83d8198), [Commit](https://github.com/open-webui/open-webui/commit/3becec6ccfc7dc457270d4e9f0d8c957e8160ddc)

> 🗓️ **Recurring event times.** Repeating calendar events now show at the time you set them for instead of being worked out in the server's time zone and shifted by the gap between the two. [#27774](https://github.com/open-webui/open-webui/issues/27774), [Commit](https://github.com/open-webui/open-webui/commit/d721b0d19621d01e35505105a778ce5681b2ffba)

> 🧮 **JSON options honoured again.** Options passed to the shared JSON helper are no longer silently ignored when the "ENABLE_ORJSON" option is turned on, falling back to the standard encoder that supports them. [Commit](https://github.com/open-webui/open-webui/commit/78ed5a0235c4de67828ba4b0d6147035067cec2c)

> 📁 **Dragging chats into shared folders.** A shared folder you can write to now highlights and accepts a dropped chat, while one you only have read access to no longer offers itself as a drop target for an action that could only fail. [Commit](https://github.com/open-webui/open-webui/commit/e4dd6c4bf14c7ea54c1effa6c40ad9e95185c413), [#28261](https://github.com/open-webui/open-webui/issues/28261)

> 📝 **Notes saved in an unexpected shape.** A note whose content was stored as structured data rather than text no longer breaks the notes page for everything else, and opens with that content shown as a formatted code block. [Commit](https://github.com/open-webui/open-webui/commit/8d1c205d8e7335ef7c292afb125a7270976f327b), [#28222](https://github.com/open-webui/open-webui/issues/28222)

> 💬 **Direct messages after an account is deleted.** A direct message conversation no longer counts a deleted account among its members, and opening a direct message with someone finds the existing conversation instead of starting a second one alongside it. [Commit](https://github.com/open-webui/open-webui/commit/a41faa3c226b20e7db7508c49c7d1d015ac9e973), [#28257](https://github.com/open-webui/open-webui/issues/28257)

> 🖇️ **Adding terminals over plain connections.** Saving a terminal connection now works when the interface is served without HTTPS, where the dialog would sit there doing nothing because the browser withholds the tool used to generate its identifier. [Commit](https://github.com/open-webui/open-webui/commit/2a45fa04cb1d07b258e0b880ab0c02577f0dc035), [#28148](https://github.com/open-webui/open-webui/issues/28148)

> 🛂 **Connecting external accounts.** Authorizing a tool's external account now completes only for the person who started it, rather than for whoever happens to return with the authorization, and signing out clears the session it relies on. [Commit](https://github.com/open-webui/open-webui/commit/c2107e5bb3689a69c170ca526925f4ed84bd00f5)

> ✂️ **Clipped icons and avatars.** The terminal icon beside the message box and the profile picture in account settings are no longer shaved flat along their left edge. [#27691](https://github.com/open-webui/open-webui/pull/27691), [#27690](https://github.com/open-webui/open-webui/issues/27690)

> 🖱️ **Sections opening by accident.** Folders, collapsible sections, and tool call blocks now open and close only when you click them, rather than also reacting when you release the mouse over them after dragging or selecting text. [Commit](https://github.com/open-webui/open-webui/commit/bd250a0e2431f8c2c7e2f4a34c5327f21fc77d4b)

> 📌 **Attaching a chat shared with you.** Attaching a conversation that was shared with you, directly or through a shared folder, now brings its content along instead of quietly attaching nothing. [Commit](https://github.com/open-webui/open-webui/commit/5cd9a395344e882b4384bec0899f503ad540aecc)

> 🧹 **Session cleanup on multi-instance setups.** The instance doing the periodic session cleanup now keeps its claim on that job alive between passes, so an idle deployment stops logging a renewal warning every two minutes and the claim no longer lapses for half of every cycle. [Commit](https://github.com/open-webui/open-webui/commit/939bcdb79e3dcad2278f1e7f4f517a3f2f36f3ec), [#27762](https://github.com/open-webui/open-webui/issues/27762)

> 🏠 **Starting folder in the file browser.** Reopening the file browser now keeps the folder you were in, instead of the breadcrumb losing its starting point and jumping you elsewhere. [Commit](https://github.com/open-webui/open-webui/commit/52c5e3b20d3cd8c3a15db50e2cc75bbd6e82068e)

> ⏹️ **Stopping a reply that is waiting.** The stop button now ends a reply that is sitting waiting for you, such as one paused on a tool approval, rather than leaving the conversation stuck part way through. [Commit](https://github.com/open-webui/open-webui/commit/f7767d6be774720e16265c6d016bf6a24a1a8759)

> 🕰️ **Saving a calendar event without a date.** Creating or editing an event with the date cleared now asks for one, where it was sent anyway, refused by the server, and reported as an unreadable error. [Commit](https://github.com/open-webui/open-webui/commit/f100edb70874808c93fab84eae1810595f9e9dc3), [#28133](https://github.com/open-webui/open-webui/issues/28133)

> 🖊️ **Message buttons in channels.** The buttons that appear when you hover a channel message now sit above the message rather than over its content, so they can be clicked on a message that starts with a code block or a table, and so the code and table controls stay clickable too. [#27737](https://github.com/open-webui/open-webui/pull/27737), [#27736](https://github.com/open-webui/open-webui/issues/27736)

> 🫧 **Attachments replaced by a loading dot.** Pinning a channel message, or otherwise updating one, no longer replaces its attachment with a loading indicator that never resolves until you reload or leave the channel. [Commit](https://github.com/open-webui/open-webui/commit/76d01602950a9e40823b53278557708d5bcd1036), [#27734](https://github.com/open-webui/open-webui/pull/27734), [#27731](https://github.com/open-webui/open-webui/issues/27731)

> 🛠️ **Rebuilding empty server lists on every request.** An instance with no tool servers or no terminal servers configured no longer rebuilds that empty list on every request that needs it. [Commit](https://github.com/open-webui/open-webui/commit/f1a64ccfc2eb2a58086c55fe413a455bb488c35a), [#28568](https://github.com/open-webui/open-webui/issues/28568)

> 🪫 **Errors logged for a cache that was simply empty.** A shared cache that has not been filled yet no longer logs an error suggesting its stored value is broken. [Commit](https://github.com/open-webui/open-webui/commit/f1a64ccfc2eb2a58086c55fe413a455bb488c35a), [#28568](https://github.com/open-webui/open-webui/issues/28568)

> 🫂 **Signing in from another application.** Signing in through an application that exchanges a token from your identity provider now applies your role and group memberships the same way signing in through the browser does, and an account whose provider sends no role keeps the one it has rather than being reset to the default. [Commit](https://github.com/open-webui/open-webui/commit/d799e81edbdc971c6deb096b6474cd95b93504bf), [Commit](https://github.com/open-webui/open-webui/commit/e9684458125c3202ebc3378aef32f0b6015171d8)

> 🚧 **The files pane reopening by itself.** With a terminal selected, closing the files pane now keeps it closed, where saving any setting reopened it, including something as incidental as picking an emoji for a folder. [#28693](https://github.com/open-webui/open-webui/pull/28693), [#28691](https://github.com/open-webui/open-webui/issues/28691), [Commit](https://github.com/open-webui/open-webui/commit/c1c81f8127466a4cd59a16d8658155b1b8faa2d0)

> 🗜️ **Embedding settings for other providers.** Saving your embedding settings now writes only the provider you have selected, where it also overwrote the address and key stored for the other two, losing them if their fields were not filled in. [Commit](https://github.com/open-webui/open-webui/commit/87d9b7e84e71b097eadf1df4f9852359104f17ed)

> ↔ **Dragging a side panel closed.** Dragging the chat controls, the note chat, or a channel thread panel closed by its edge no longer floods the browser console with errors and leaves stray handlers behind, and the divider can now be moved with the arrow keys once focused. [#28759](https://github.com/open-webui/open-webui/issues/28759), [Commit](https://github.com/open-webui/open-webui/commit/33dff414e829d10dc6691b1cac7457077fa6799c)

> ❌ **Tool calls that failed looking successful.** A tool call that returned an error is now marked as failed with a red cross rather than a green tick, so a reply built on a failed call is easier to spot. [Commit](https://github.com/open-webui/open-webui/commit/f3f76095d18e07a3a944f22a4b25993bbffe90a3), [#28016](https://github.com/open-webui/open-webui/issues/28016)

> 🗜 **Download links in a cited source doing nothing.** A link in a citation shown as formatted content now downloads the file when clicked, where it silently did nothing at all. [Commit](https://github.com/open-webui/open-webui/commit/3c66d639e31ba8a7477d337b37d8d671ea2430cf), [#28924](https://github.com/open-webui/open-webui/issues/28924)

> 🖥 **Stopping a reply after the shared cache restarts.** Stopping a reply now keeps working across a cluster after the shared cache restarts or its connection drops, where the part that carries a stop between instances gave up for good and silently, and only restarting the application brought it back. [Commit](https://github.com/open-webui/open-webui/commit/bf3a58dbcd18ddc2c7f130d8f9529477fe7cb042), [#28909](https://github.com/open-webui/open-webui/issues/28909)

> 🗂 **Directory sync listing local accounts.** A directory service syncing accounts over SCIM now sees only the accounts that came from a directory, where it also listed and could modify accounts created with a password in Open WebUI itself. [Commit](https://github.com/open-webui/open-webui/commit/fb4f476316a2f83e4d2914d535c19b3440cbc490)

> ↕ **Sorting a list of people.** Sorting the admin user list, or a channel's member list, now works when no search term has been entered, where the chosen order was ignored unless something was being searched for. [Commit](https://github.com/open-webui/open-webui/commit/fb4f476316a2f83e4d2914d535c19b3440cbc490)

> 🖊 **Dragging a side panel wider than the window.** A side panel can no longer be dragged so wide that the chat beside it is squeezed away, and dragging one below its minimum width now closes it rather than sticking. [Commit](https://github.com/open-webui/open-webui/commit/ef455fcef9d6cb1136275c26e49bc3c5d6661795), [#28965](https://github.com/open-webui/open-webui/issues/28965)

> 🧻 **Logs flooded by an unreachable server.** A terminal or tool server that cannot be reached now records one line per attempt rather than a full stack trace, where a few minutes of downtime could fill the log with hundreds of megabytes and drown out everything else. [#27755](https://github.com/open-webui/open-webui/pull/27755), [#27751](https://github.com/open-webui/open-webui/issues/27751), [#27757](https://github.com/open-webui/open-webui/pull/27757), [#27756](https://github.com/open-webui/open-webui/issues/27756)

> 🪣 **Files left behind when a knowledge base is emptied.** Emptying a knowledge base now removes the files it held, along with their stored copies and their search data, where all three were left behind with nothing in the interface to clear them. [Commit](https://github.com/open-webui/open-webui/commit/363ad352fec9553469852d111bc0506b896504a6), [#27988](https://github.com/open-webui/open-webui/issues/27988)

> 🖍 **Clearing the supported media types.** Emptying the supported media types in the documents settings now stays empty, where the previous value came back on the next visit, so images kept being sent to the extraction engine instead of straight to a model that can read them. [#28750](https://github.com/open-webui/open-webui/pull/28750), [#28747](https://github.com/open-webui/open-webui/issues/28747), [Commit](https://github.com/open-webui/open-webui/commit/ecad20b77f9bd700bd818a2f447176f5994320c3)

> 🖲 **Filtering while on a later page.** Changing a filter in the workspace, such as showing only what you created, now returns to the first page, where the list could come back empty with the page controls gone and no way back. [#28734](https://github.com/open-webui/open-webui/issues/28734), [Commit](https://github.com/open-webui/open-webui/commit/a914868e3c83b08be1399dbae1e4da25a0c00c87)

> 🎧 **Who a channel says its members are.** The member list of a channel now includes its owner and everyone in a group that was granted access, where the owner never appeared and granting both a person and a group they were not in listed nobody at all while the count beside it said two. [#28289](https://github.com/open-webui/open-webui/pull/28289), [#28288](https://github.com/open-webui/open-webui/issues/28288), [Commit](https://github.com/open-webui/open-webui/commit/e3e82b14714661ba5bd24e2c47e42cef5594b132)

> 👪 **Group member counts updating.** Adding or removing someone from a group in the admin panel now updates that group's member count straight away, where it stayed at the old number until the page was reloaded. [Commit](https://github.com/open-webui/open-webui/commit/18bf0ade7b35fb25ff7920ad3713624d93f04401)

> 🤫 **Replies stopping silently after a tool ran.** When a provider rejects the follow-up request made after a tool finishes, the reason is now shown in the chat instead of the reply simply ending with nothing said. [Commit](https://github.com/open-webui/open-webui/commit/a610d77137fabf60a2e0daa961a8ef8f7320293a), [#28633](https://github.com/open-webui/open-webui/issues/28633)

> 🔌 **Stream filters on direct API calls.** A filter reading a streamed event as an object now works on requests made straight to the chat completions endpoint, matching every other path, where it used to raise and end the reply partway. [Commit](https://github.com/open-webui/open-webui/commit/684111715f742f56a3c7efac9eb7a1e68e54a3ec)

> 🏋️ **What "THREAD_POOL_SIZE" now sizes.** The setting now governs both of the pools that background work runs in, where it previously governed only one and the other, carrying most of the blocking work including knowledge searches, sign-ins and file storage, was fixed at a small ceiling no setting could raise, so an instance that set it high will now use more threads than before, up to twice the configured value across the two pools, and one that relied on the old ceiling to hold thread use down should review it. [Commit](https://github.com/open-webui/open-webui/commit/4ec6ee14418edd04eaba9e34bd5868453f61df40), [#28168](https://github.com/open-webui/open-webui/issues/28168)

> 💾 **Saving replies as they stream.** The "ENABLE_REALTIME_CHAT_SAVE" setting no longer has any effect, because a reply in progress is now held outside the database and written once when it finishes. [Commit](https://github.com/open-webui/open-webui/commit/a1579a01ff43cacb357269707d36267ad35e01d6)

> 🛡 **Forms in embedded pages now work by default.** A page shown inside a chat, such as an artifact or an HTML preview, may now submit forms unless you turn that off, where it was blocked unless you turned it on. [Commit](https://github.com/open-webui/open-webui/commit/3c66d639e31ba8a7477d337b37d8d671ea2430cf)

> 📊 **Default usage statistics range.** Usage statistics now cover the past two years by default for everyone, instead of starting from the date the account was created. [Commit](https://github.com/open-webui/open-webui/commit/8dbbc206c5a0706789722c42827479e5db10bb2b)

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
- [[Changes/Open WebUI/2026-08-25-8-memory-and-personalization-changes-in-v0-11-1|8 Memory and Personalization changes in v0.11.1]] · Memory and Personalization
- [[Changes/Open WebUI/2026-08-25-files-for-delegated-tasks-a-task-handed-to-a-sub-agent-can-now-carry-the-attachm|🤝 Files for delegated tasks. A task handed to a sub-agent can now carry…]] · Agent Mode
- [[Changes/Open WebUI/2026-08-25-4-enterprise-and-administration-changes-in-v0-11-1|4 Enterprise and Administration changes in v0.11.1]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-08-25-24-interface-experience-changes-in-v0-11-1|24 Interface Experience changes in v0.11.1]] · Interface Experience
- [[Changes/Open WebUI/2026-08-25-5-search-and-browsing-changes-in-v0-11-1|5 Search and Browsing changes in v0.11.1]] · Search and Browsing
- [[Changes/Open WebUI/2026-08-25-4-voice-and-audio-changes-in-v0-11-1|4 Voice and Audio changes in v0.11.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-08-25-56-model-support-changes-in-v0-11-1|56 Model Support changes in v0.11.1]] · Model Support
- [[Changes/Open WebUI/2026-08-25-39-other-changes-in-v0-11-1|39 other changes in v0.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-08-25 · Gemini CLI · [[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-24935-force-terminal-buffer-rerender-after-exiting-external|SSR Agent Issue Fix (24935)]]
- Later: 2026-08-25 · OpenCode · [[Changes/OpenCode/2026-08-25-terminal-fixed-github-auth-for-immutable-oidc-subject-tokens|Terminal Fixed GitHub auth for immutable OIDC subject tokens]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-c19a21&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-73-developer-workflow-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-c19a21%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->