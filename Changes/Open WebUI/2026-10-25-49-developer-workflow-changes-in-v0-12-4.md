---
card_id: open-webui-2026-10-25-9b5bf2
date: '2026-10-25'
description: 'Open WebUI · 2026-10-25 · Developer Workflow: 49 changes in v0.12.4
  — ⏱️ **Exact last active time.** Hovering the last active time in the admin user
  list and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1317
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bfb89dfd0ef09d3ee2fbb4585a7f8b2dd9353776065df4cc45a248af6a9c8d58
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-25-9b5bf2
  comparison: ''
  date: '2026-10-25'
  description: 'Open WebUI — v0.12.4: 49 Developer Workflow changes'
  evidence:
  - quote: ⏱️ **Exact last active time.** Hovering the last active time in the admin
      user list and in a group's member list now shows the exact date and time. [Commit](https://github.com/open-webui/open-webui/commit/7484c75e163cb17fee9ebcc11e57f462289cc03e)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F50D **Compare view stays aligned.** Matching rows in the two panes
      of the Compare view now stay lined up and in place while scrolling, resizing
      or editing, and a colored bar now marks changed lines also while whitespace
      or emphasis markers are ignored. [Commit](https://github.com/open-webui/open-webui/commit/32170b96fc5edc8c324c5de188be36e9d32059a2),
      [Commit](https://github.com/open-webui/open-webui/commit/596cdbb6caf6022947285722949de1f52272b673),
      [Commit](https://github.com/open-webui/open-webui/commit/5c9865a1f119d33ab11d77e79d8c8c8fb93704ec),
      [Commit](https://github.com/open-webui/open-webui/commit/aa8ce52c7a3afbb164bc16a3b7c20e40ba6390ed)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F5B1️ **Clickable setting labels.** Clicking the label of a setting
      across user and admin settings, including advanced parameters and connections,
      now toggles its switch, focuses its field or presses its button, and the label
      highlights while the row is hovered or focused, so the right control is easier
      to find. [Commit](https://github.com/open-webui/open-webui/commit/33e4c5f514d57ca8f654c1015dfb32774b833db6),
      [Commit](https://github.com/open-webui/open-webui/commit/131ddc32ecaeb06f9aa8740ff004710bacef72e0),
      [Commit](https://github.com/open-webui/open-webui/commit/b93b81246817b651bb47bb1f5e453503649d30d0),
      [#32768](https://github.com/open-webui/open-webui/issues/32768), [#32900](https://github.com/open-webui/open-webui/issues/32900)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F5C3️ **Bulk file management.** Manage Files in Settings > Data
      Controls can now download a single file and lets you select several files or
      all files matching a search to delete them or download them together as one
      zip archive, with progress and a stop button. [Commit](https://github.com/open-webui/open-webui/commit/2a86805648f45c36c479c6f9a0127cae799ee14f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4E5 **Accurate upload status.** A file uploaded to a knowledge
      base now only shows as done once it is indexed and linked to the knowledge base,
      so it no longer shows as done and then goes missing from the list until a reload.
      [Commit](https://github.com/open-webui/open-webui/commit/f5e8f84e69d0f4224cc27cabd4f8d2c441d4d58c),
      [#32803](https://github.com/open-webui/open-webui/issues/32803)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: ⏳ **Knowledge files show Processing.** A file added to a knowledge base
      now switches from Uploading to Processing once it reaches the server, and the
      list keeps itself up to date until the file is ready, so it no longer says Uploading
      until you reopen the knowledge base. [#32982](https://github.com/open-webui/open-webui/pull/32982),
      [Commit](https://github.com/open-webui/open-webui/commit/0a568f6a813d49ca6e7797c7940647782e44ad48)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F9EE **Knowledge uploads listed at once.** Files selected or dropped
      together into a knowledge base now all appear as Uploading right away in upload
      order, so each one no longer waits to appear until the file before it has finished
      processing. [#32992](https://github.com/open-webui/open-webui/pull/32992), [Commit](https://github.com/open-webui/open-webui/commit/0c684208bbc6e28e31995c0c4788429b38048db0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4C1 **File browser folder menu.** A folder's menu in the terminal
      file browser now has New File and New Folder items that create the file or folder
      inside that folder. [Commit](https://github.com/open-webui/open-webui/commit/b6b0fff5d6af2fefb84f8858244adeef50462aac),
      [Commit](https://github.com/open-webui/open-webui/commit/fbeee59e99f47c9ff4fb0f114f78eb9dc85f2967)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4EC **First-message terminal uploads.** With Chat Uploads set to
      Filesystem on a Per chat terminal, a file attached to the first message of a
      new chat now waits and uploads into that chat's own terminal when the message
      is sent, so it no longer lands in the shared workspace. [Commit](https://github.com/open-webui/open-webui/commit/049d75e176dd1ef3f2f1eef09d63f30c4e988b3c),
      [#30245](https://github.com/open-webui/open-webui/issues/30245)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001FAA7 **Folder descriptions.** Folders can now have a description
      in their settings, shown under the folder title on the folder's page. [Commit](https://github.com/open-webui/open-webui/commit/f625c37cce4ec971e7d86af6da644fee03561b1e),
      [Commit](https://github.com/open-webui/open-webui/commit/72d86c6b13c1ccb567e2ffa574b3a53a853361b3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F69A **Organize chats in shared folders.** The owner of a shared
      folder can now rename chats other people started in it and drag them to another
      folder within the same shared folder. [Commit](https://github.com/open-webui/open-webui/commit/2262073146bbeda1aa4f998bb61e15ec7f9b6491)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F9FE **Model usage in audit logs.** With audit logging on and \"/chat\"
      removed from \"AUDIT_EXCLUDED_PATHS\", where it is excluded by default, each
      chat reply and tool call round now writes its own audit log entry with the model
      and the input, output and total tokens the provider reported, linked to the
      request that started it. [Commit](https://github.com/open-webui/open-webui/commit/52e155019f511846a8066e012ff37f8aac6db2db),
      [#30098](https://github.com/open-webui/open-webui/issues/30098)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F9F3 **Faster folder changes.** Renaming, sharing, moving or deleting
      a folder and deleting all chats now finish quickly with thousands of users online,
      where each took several seconds and reloaded the open chat of everyone online.
      [#32888](https://github.com/open-webui/open-webui/pull/32888), [Commit](https://github.com/open-webui/open-webui/commit/e1e31973f0bfd04dc4195c896eff3476678d2005)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4CA **Faster analytics dashboard.** The Admin Analytics dashboard
      now gets its totals, model and user lists and daily charts from fewer and lighter
      database queries, so it opens faster on instances with many messages. [Commit](https://github.com/open-webui/open-webui/commit/97650bbbea43b98c1c403bf74b08736e9ad522d7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F512 **Live access after archiving.** People who see a chat through
      a shared folder now stop receiving its live updates when the owner archives
      it or archives all chats, and people with a share link stop when the owner unshares
      all chats, as they already did when a single chat was unshared or deleted. [#32887](https://github.com/open-webui/open-webui/pull/32887),
      [Commit](https://github.com/open-webui/open-webui/commit/ed3cf8355346689d790829074aa7d8cd004b7865)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F9F5 **Thread replies deleted too.** Deleting a channel message
      now also deletes its thread replies, which stayed behind and could still be
      found in search. [#32666](https://github.com/open-webui/open-webui/pull/32666),
      [Commit](https://github.com/open-webui/open-webui/commit/54fc21d6855ba4c41c9088c758949d6fcc0ff26f),
      [#32665](https://github.com/open-webui/open-webui/issues/32665)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4DC **Prompt history on unchanged saves.** Saving a prompt without
      changes no longer adds an identical version to its history. [#32709](https://github.com/open-webui/open-webui/pull/32709),
      [Commit](https://github.com/open-webui/open-webui/commit/312d113fd04bc43996cf97282c34b46ba79c26cd),
      [#32708](https://github.com/open-webui/open-webui/issues/32708)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4DE **Realtime calls answer once.** A Realtime call no longer answers
      the same sentence twice when a short pause splits it into two turns. [#32773](https://github.com/open-webui/open-webui/pull/32773),
      [Commit](https://github.com/open-webui/open-webui/commit/25b115662396a9e09ee115008f4516aaa2eebd1d),
      [#32764](https://github.com/open-webui/open-webui/issues/32764)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: ⬅️ **Right-to-left question cards.** Question cards from Ask User now follow
      the Chat Direction setting, so Hebrew and Arabic questions and answers are laid
      out right to left. [#32784](https://github.com/open-webui/open-webui/pull/32784),
      [Commit](https://github.com/open-webui/open-webui/commit/aee4cbf4639281f711018af08e029e0f501fd3c4),
      [#32778](https://github.com/open-webui/open-webui/issues/32778)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F9F7 **Tool server array parameters.** An array query parameter
      now reaches an OpenAPI tool server as repeated values instead of one text value
      that looks like a Python list. [#32677](https://github.com/open-webui/open-webui/pull/32677),
      [Commit](https://github.com/open-webui/open-webui/commit/fd1e59b25ff68ff015ce84707839084157df6045),
      [#32676](https://github.com/open-webui/open-webui/issues/32676)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4DA **Multi-folder knowledge drops.** Dropping several folders
      on a knowledge base now uploads all of them, where only the first one was uploaded.
      [#32653](https://github.com/open-webui/open-webui/pull/32653), [Commit](https://github.com/open-webui/open-webui/commit/d907b61816018202d2425109fbf9b506107e7182),
      [#32652](https://github.com/open-webui/open-webui/issues/32652)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F9E9 **Restored skill-only drafts.** A draft that holds only a skill,
      brought back to the chat input, now sends only that skill, where the names of
      every skill were sent. [#32690](https://github.com/open-webui/open-webui/pull/32690),
      [Commit](https://github.com/open-webui/open-webui/commit/14956af03f2ba50a154b13ff77166139fdcc0315),
      [#32689](https://github.com/open-webui/open-webui/issues/32689)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F40D **Python code block results.** Running a plotting block again
      now shows only the new plot, and a block whose last value is a date, decimal
      number or other object shows that value instead of \"Maximum call stack size
      exceeded\". [#32686](https://github.com/open-webui/open-webui/pull/32686), [Commit](https://github.com/open-webui/open-webui/commit/1a0bdb38a179ace36419aee87688727a9466a25a),
      [#32685](https://github.com/open-webui/open-webui/issues/32685), [#32682](https://github.com/open-webui/open-webui/pull/32682),
      [Commit](https://github.com/open-webui/open-webui/commit/fb5eec56dd2212d07a77dfb4ed4b25d26ccebcb2),
      [#32681](https://github.com/open-webui/open-webui/issues/32681)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001FA9F **Preview of an earlier artifact.** Preview on an earlier code
      block now opens that block's artifact when the artifacts pane was closed, where
      it opened the newest one. [#32688](https://github.com/open-webui/open-webui/pull/32688),
      [Commit](https://github.com/open-webui/open-webui/commit/9862a5bd613bb1c98166bb0eff1c8e824fa86723),
      [#32687](https://github.com/open-webui/open-webui/issues/32687)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F578️ **Web pages on fresh installs.** Attached web pages and other
      HTML text extraction return their text again on fresh installs, where a broken
      update of a library underneath made them come back empty. [#33103](https://github.com/open-webui/open-webui/pull/33103),
      [Commit](https://github.com/open-webui/open-webui/commit/f32de07ddead5453658c828cd7e2c3a1c680934c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F50E **Shared Chats search paging.** A search in Shared Chats or
      in an admin's view of a user's chats now loads more than the first 60 results.
      [#32675](https://github.com/open-webui/open-webui/pull/32675), [Commit](https://github.com/open-webui/open-webui/commit/0f2d1af1ce2092b2d6021823a923ddd179682f52),
      [#32674](https://github.com/open-webui/open-webui/issues/32674)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001FA9E **Notes open once.** A note that two people open at the same
      time, such as one imported from a Markdown or text file and not edited since,
      no longer shows and saves its text twice, also with several workers. [#33004](https://github.com/open-webui/open-webui/pull/33004),
      [Commit](https://github.com/open-webui/open-webui/commit/499b83fa8d47f592bd7d79cab270d5cfc12652be),
      [#33002](https://github.com/open-webui/open-webui/issues/33002), [Commit](https://github.com/open-webui/open-webui/commit/1407f83cfc8df4e727f82beabdd4da6e29fc1119),
      [#32824](https://github.com/open-webui/open-webui/issues/32824)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F508 **Read Aloud stops on failure.** Read Aloud now stops requesting
      the remaining sentences once one fails, so an unavailable speech provider shows
      a single error instead of one for every sentence. [#33028](https://github.com/open-webui/open-webui/pull/33028),
      [Commit](https://github.com/open-webui/open-webui/commit/ea615c3a2e89d827e24016d719acb5ee63f409d2),
      [#33023](https://github.com/open-webui/open-webui/issues/33023)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F5C4️ **Archived chats survive folders.** Archive All Chats now
      takes the chats out of their folders, so deleting a folder afterwards no longer
      deletes those archived chats for good. [#32647](https://github.com/open-webui/open-webui/pull/32647),
      [Commit](https://github.com/open-webui/open-webui/commit/97f5c4e973a703b63a2606b054de324db88f706f),
      [#32646](https://github.com/open-webui/open-webui/issues/32646)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F50C **No hangs after closed pages.** Closing a page while it was
      still loading, such as a chat export or a file's processing status, no longer
      loses database connections on SQLite, where later requests could hang or fail
      with 503 once enough were lost. [#32617](https://github.com/open-webui/open-webui/pull/32617),
      [Commit](https://github.com/open-webui/open-webui/commit/2355b8a3699826eaf1fe5a344f63e292f9532c48),
      [#32609](https://github.com/open-webui/open-webui/issues/32609), [#32741](https://github.com/open-webui/open-webui/issues/32741)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001FA84 **Function input dialogs answered.** Confirming or cancelling
      a function's input or confirmation dialog now reaches the function when a script
      event arrived while the dialog was open, where the function kept waiting for
      an answer. [#32744](https://github.com/open-webui/open-webui/pull/32744), [Commit](https://github.com/open-webui/open-webui/commit/2d9852c6048774c0d8913c722b5fe661326f1b4d),
      [#32742](https://github.com/open-webui/open-webui/issues/32742)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F6D1 **Stop sequences with percent.** A stop sequence containing
      % no longer stops every message from sending. [#32649](https://github.com/open-webui/open-webui/pull/32649),
      [Commit](https://github.com/open-webui/open-webui/commit/fdb304be2f5250c9282bacd3ff91757e55b89976),
      [#32648](https://github.com/open-webui/open-webui/issues/32648)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F5DC️ **Channel image compression by default.** With image compression
      on, images in channels are now compressed when Compress Images in Channels is
      left at its default, where they were sent uncompressed. [#32693](https://github.com/open-webui/open-webui/pull/32693),
      [Commit](https://github.com/open-webui/open-webui/commit/70fb5462eab6b71e258c9fbd9ce5714bd173bcfb),
      [#32692](https://github.com/open-webui/open-webui/issues/32692)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F399️ **Microphone off when leaving.** Leaving a chat while dictating
      now turns the microphone off. [#32640](https://github.com/open-webui/open-webui/pull/32640),
      [Commit](https://github.com/open-webui/open-webui/commit/636b631ab7cf2f4053c43466468cd4bb119dd250),
      [#32638](https://github.com/open-webui/open-webui/issues/32638), [#32639](https://github.com/open-webui/open-webui/issues/32639)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: ✏️ **Chat titles of only spaces.** Renaming a chat to only spaces now keeps
      its title and shows an error instead of saving a blank title. [#32770](https://github.com/open-webui/open-webui/pull/32770),
      [Commit](https://github.com/open-webui/open-webui/commit/9cbd27011b1d1842f52cbf91b4b5764b5820b52b),
      [#32769](https://github.com/open-webui/open-webui/issues/32769)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F524 **No stray formatting spaces.** Chat messages no longer show
      an extra space at the start of each paragraph and before italic, bold, struck-through
      or linked text, which appeared in 0.12.3 and left a gap after an em dash. [#32743](https://github.com/open-webui/open-webui/pull/32743),
      [Commit](https://github.com/open-webui/open-webui/commit/2bebbb44e1a04b220f831aced950b0e334529988),
      [#32739](https://github.com/open-webui/open-webui/issues/32739)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F9ED **Scrolling while a reply streams.** On slow or busy devices
      a streaming reply now keeps the view at the bottom as its content grows, where
      it stopped following partway through, and scrolling up while it streams is no
      longer pulled back down. [Commit](https://github.com/open-webui/open-webui/commit/5a46aad0f0702536c98c9a26ae7d04482cdac784),
      [#32728](https://github.com/open-webui/open-webui/issues/32728)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: ⚡ **Early updates in new chats.** The first reply of a new chat no longer
      stays empty with the Stop button showing when its error or content arrives before
      the page knows the new chat, a message added while a chat is still loading no
      longer stays missing until a reload, and a message queued during the first reply
      of a new chat is sent once that reply finishes. [Commit](https://github.com/open-webui/open-webui/commit/cbd06d2aad0d64c2a50b4989c4290762de2cd3f0),
      [Commit](https://github.com/open-webui/open-webui/commit/d5038fec44d2f37e81798a6c7f4340a8d1a62f10),
      [#32550](https://github.com/open-webui/open-webui/issues/32550), [#32761](https://github.com/open-webui/open-webui/issues/32761)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4CB **Drafts with variables kept.** Reloading the page with a chat
      input draft that contains {{ }} placeholders, or editing a queued message that
      contains them, now keeps the text as it was, where it asked for input variables
      and dropped the text. [Commit](https://github.com/open-webui/open-webui/commit/6dbd375c267dd0dafc83c480ec23e3b1a7156406),
      [#32650](https://github.com/open-webui/open-webui/issues/32650)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F374 **No fork in temporary chats.** The Fork chat option is now
      hidden in temporary chats and the /fork command answers that there is no chat
      to fork, where forking failed with an error. [#32839](https://github.com/open-webui/open-webui/pull/32839),
      [Commit](https://github.com/open-webui/open-webui/commit/1a492207971a5118dde2fe6b523edf7021f38cc9),
      [#32833](https://github.com/open-webui/open-webui/issues/32833)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F680 **First message after loading.** A message sent right after
      the page loads is no longer wiped by the new chat setup still running, where
      it disappeared and its reply stayed empty until a reload. [#32829](https://github.com/open-webui/open-webui/pull/32829),
      [Commit](https://github.com/open-webui/open-webui/commit/4ed1af6879ee632a3130771b4a960ccf37c1c305),
      [#32819](https://github.com/open-webui/open-webui/issues/32819)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F39E️ **Left-aligned PowerPoint titles.** The PowerPoint preview
      now keeps titles and subtitles that the file aligns left on the left, where
      it centered them. [#32876](https://github.com/open-webui/open-webui/pull/32876),
      [Commit](https://github.com/open-webui/open-webui/commit/8fa77c8282b10e7de36863c4df6583a62a55354c),
      [#32873](https://github.com/open-webui/open-webui/issues/32873)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F41A **Launcher help in zsh.** The examples in the Docker Compose
      launcher help now quote options with square brackets, so they also work when
      pasted into zsh. [#32881](https://github.com/open-webui/open-webui/pull/32881),
      [Commit](https://github.com/open-webui/open-webui/commit/52f51ea4f3044072d49eefd4feedb859bb66b80c),
      [#32878](https://github.com/open-webui/open-webui/issues/32878)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F3F7️ **Tooltips show text as written.** Tooltips now show names,
      paths and descriptions that contain angle brackets as written, where they came
      out mangled or partly missing. [#32953](https://github.com/open-webui/open-webui/pull/32953),
      [Commit](https://github.com/open-webui/open-webui/commit/3299a097530847ec53da01a5964cf7ef8592dee0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4E1 **Websockets after Redis reconnects.** With the Redis websocket
      manager and \"retry_on_timeout\" in \"WEBSOCKET_REDIS_OPTIONS\", an instance
      now accepts new browser connections again once Redis is back after its connection
      dropped, where since 0.12.3 every new connection could hang until the instance
      was restarted. [#33009](https://github.com/open-webui/open-webui/pull/33009),
      [Commit](https://github.com/open-webui/open-webui/commit/0d17660535dd2ad9d6f0b75a2a2f5855066cd0a0),
      [#33008](https://github.com/open-webui/open-webui/issues/33008)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F527 **Direct Integrations off disables connections.** While Direct
      Integrations is off, as it is by default, the tool servers and Open Terminal
      connections that users and admins saved in their Integrations settings are no
      longer used in chats, where turning it off only hid the settings tab, so instances
      that never turned it on lose those connections until an admin turns on Direct
      Integrations in Admin Settings > Connections or sets \"ENABLE_DIRECT_INTEGRATIONS\".
      [#32996](https://github.com/open-webui/open-webui/pull/32996), [Commit](https://github.com/open-webui/open-webui/commit/3e9d6cb9508a1ba4ec18017b3c80afaf6ac59a89)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F433 **Python 3.12 Docker image.** The Docker image now runs Python
      3.12 on Debian 13 instead of Python 3.11 on Debian 12, so custom functions,
      tools and packages installed with pip inside the container need versions that
      support Python 3.12. [#32861](https://github.com/open-webui/open-webui/pull/32861),
      [Commit](https://github.com/open-webui/open-webui/commit/a915df8ce12b32109b7b929cb2cad6046293aef6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F91D **Sharing permissions enforced everywhere.** Sharing permissions
      such as Models Sharing, Knowledge Sharing and Folders Sharing now also apply
      to sharing through the API, and a change in an item's Access settings that a
      user is not allowed to make is now refused with an error instead of being quietly
      left out. [Commit](https://github.com/open-webui/open-webui/commit/5f95008abdfbbbfbe5c080de0347deb70eb507b6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F5C4️ **Manage Files shows only yours.** Manage Files in Settings
      > Data Controls now lists only your own files, also for administrators, who
      saw every user's files there while \"BYPASS_ADMIN_ACCESS_CONTROL\" was on, as
      it is by default. [Commit](https://github.com/open-webui/open-webui/commit/2a86805648f45c36c479c6f9a0127cae799ee14f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 49-developer-workflow-changes-in-v0-12-4
  source_release: open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79
  source_type: github_releases
  theme: developer-workflow
  title: 49 Developer Workflow changes in v0.12.4
  type: change
related_changes:
- '[[Changes/Dify/2026-10-23-respect-xforward-headers-enabled-standalone-api-default-remains-false-bundled-co|
  /  RESPECT_XFORWARD_HEADERS_ENABLED  /  Standalone API default remains false]]'
- '[[Changes/Windsurf/2026-10-23-4-developer-workflow-changes-in-v3-11-212|4 Developer
  Workflow changes in v3.11.212]]'
- '[[Changes/Windsurf/2026-10-24-2-developer-workflow-changes-in-v3-11-216|2 Developer
  Workflow changes in v3.11.216]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79]]'
source_type: github_releases
theme: developer-workflow
title: 49 Developer Workflow changes in v0.12.4
type: change
---

<!-- chronolog:begin region="header" -->
# 49 Developer Workflow changes in v0.12.4

**Open WebUI** · 2026-10-25 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.4) · from [[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|v0.12.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⏱️ **Exact last active time.** Hovering the last active time in the admin user list and in a group's member list now shows the exact date and time. [Commit](https://github.com/open-webui/open-webui/commit/7484c75e163cb17fee9ebcc11e57f462289cc03e)

> 🔍 **Compare view stays aligned.** Matching rows in the two panes of the Compare view now stay lined up and in place while scrolling, resizing or editing, and a colored bar now marks changed lines also while whitespace or emphasis markers are ignored. [Commit](https://github.com/open-webui/open-webui/commit/32170b96fc5edc8c324c5de188be36e9d32059a2), [Commit](https://github.com/open-webui/open-webui/commit/596cdbb6caf6022947285722949de1f52272b673), [Commit](https://github.com/open-webui/open-webui/commit/5c9865a1f119d33ab11d77e79d8c8c8fb93704ec), [Commit](https://github.com/open-webui/open-webui/commit/aa8ce52c7a3afbb164bc16a3b7c20e40ba6390ed)

> 🖱️ **Clickable setting labels.** Clicking the label of a setting across user and admin settings, including advanced parameters and connections, now toggles its switch, focuses its field or presses its button, and the label highlights while the row is hovered or focused, so the right control is easier to find. [Commit](https://github.com/open-webui/open-webui/commit/33e4c5f514d57ca8f654c1015dfb32774b833db6), [Commit](https://github.com/open-webui/open-webui/commit/131ddc32ecaeb06f9aa8740ff004710bacef72e0), [Commit](https://github.com/open-webui/open-webui/commit/b93b81246817b651bb47bb1f5e453503649d30d0), [#32768](https://github.com/open-webui/open-webui/issues/32768), [#32900](https://github.com/open-webui/open-webui/issues/32900)

> 🗃️ **Bulk file management.** Manage Files in Settings > Data Controls can now download a single file and lets you select several files or all files matching a search to delete them or download them together as one zip archive, with progress and a stop button. [Commit](https://github.com/open-webui/open-webui/commit/2a86805648f45c36c479c6f9a0127cae799ee14f)

> 📥 **Accurate upload status.** A file uploaded to a knowledge base now only shows as done once it is indexed and linked to the knowledge base, so it no longer shows as done and then goes missing from the list until a reload. [Commit](https://github.com/open-webui/open-webui/commit/f5e8f84e69d0f4224cc27cabd4f8d2c441d4d58c), [#32803](https://github.com/open-webui/open-webui/issues/32803)

> ⏳ **Knowledge files show Processing.** A file added to a knowledge base now switches from Uploading to Processing once it reaches the server, and the list keeps itself up to date until the file is ready, so it no longer says Uploading until you reopen the knowledge base. [#32982](https://github.com/open-webui/open-webui/pull/32982), [Commit](https://github.com/open-webui/open-webui/commit/0a568f6a813d49ca6e7797c7940647782e44ad48)

> 🧮 **Knowledge uploads listed at once.** Files selected or dropped together into a knowledge base now all appear as Uploading right away in upload order, so each one no longer waits to appear until the file before it has finished processing. [#32992](https://github.com/open-webui/open-webui/pull/32992), [Commit](https://github.com/open-webui/open-webui/commit/0c684208bbc6e28e31995c0c4788429b38048db0)

> 📁 **File browser folder menu.** A folder's menu in the terminal file browser now has New File and New Folder items that create the file or folder inside that folder. [Commit](https://github.com/open-webui/open-webui/commit/b6b0fff5d6af2fefb84f8858244adeef50462aac), [Commit](https://github.com/open-webui/open-webui/commit/fbeee59e99f47c9ff4fb0f114f78eb9dc85f2967)

> 📬 **First-message terminal uploads.** With Chat Uploads set to Filesystem on a Per chat terminal, a file attached to the first message of a new chat now waits and uploads into that chat's own terminal when the message is sent, so it no longer lands in the shared workspace. [Commit](https://github.com/open-webui/open-webui/commit/049d75e176dd1ef3f2f1eef09d63f30c4e988b3c), [#30245](https://github.com/open-webui/open-webui/issues/30245)

> 🪧 **Folder descriptions.** Folders can now have a description in their settings, shown under the folder title on the folder's page. [Commit](https://github.com/open-webui/open-webui/commit/f625c37cce4ec971e7d86af6da644fee03561b1e), [Commit](https://github.com/open-webui/open-webui/commit/72d86c6b13c1ccb567e2ffa574b3a53a853361b3)

> 🚚 **Organize chats in shared folders.** The owner of a shared folder can now rename chats other people started in it and drag them to another folder within the same shared folder. [Commit](https://github.com/open-webui/open-webui/commit/2262073146bbeda1aa4f998bb61e15ec7f9b6491)

> 🧾 **Model usage in audit logs.** With audit logging on and "/chat" removed from "AUDIT_EXCLUDED_PATHS", where it is excluded by default, each chat reply and tool call round now writes its own audit log entry with the model and the input, output and total tokens the provider reported, linked to the request that started it. [Commit](https://github.com/open-webui/open-webui/commit/52e155019f511846a8066e012ff37f8aac6db2db), [#30098](https://github.com/open-webui/open-webui/issues/30098)

> 🧳 **Faster folder changes.** Renaming, sharing, moving or deleting a folder and deleting all chats now finish quickly with thousands of users online, where each took several seconds and reloaded the open chat of everyone online. [#32888](https://github.com/open-webui/open-webui/pull/32888), [Commit](https://github.com/open-webui/open-webui/commit/e1e31973f0bfd04dc4195c896eff3476678d2005)

> 📊 **Faster analytics dashboard.** The Admin Analytics dashboard now gets its totals, model and user lists and daily charts from fewer and lighter database queries, so it opens faster on instances with many messages. [Commit](https://github.com/open-webui/open-webui/commit/97650bbbea43b98c1c403bf74b08736e9ad522d7)

> 🔒 **Live access after archiving.** People who see a chat through a shared folder now stop receiving its live updates when the owner archives it or archives all chats, and people with a share link stop when the owner unshares all chats, as they already did when a single chat was unshared or deleted. [#32887](https://github.com/open-webui/open-webui/pull/32887), [Commit](https://github.com/open-webui/open-webui/commit/ed3cf8355346689d790829074aa7d8cd004b7865)

> 🧵 **Thread replies deleted too.** Deleting a channel message now also deletes its thread replies, which stayed behind and could still be found in search. [#32666](https://github.com/open-webui/open-webui/pull/32666), [Commit](https://github.com/open-webui/open-webui/commit/54fc21d6855ba4c41c9088c758949d6fcc0ff26f), [#32665](https://github.com/open-webui/open-webui/issues/32665)

> 📜 **Prompt history on unchanged saves.** Saving a prompt without changes no longer adds an identical version to its history. [#32709](https://github.com/open-webui/open-webui/pull/32709), [Commit](https://github.com/open-webui/open-webui/commit/312d113fd04bc43996cf97282c34b46ba79c26cd), [#32708](https://github.com/open-webui/open-webui/issues/32708)

> 📞 **Realtime calls answer once.** A Realtime call no longer answers the same sentence twice when a short pause splits it into two turns. [#32773](https://github.com/open-webui/open-webui/pull/32773), [Commit](https://github.com/open-webui/open-webui/commit/25b115662396a9e09ee115008f4516aaa2eebd1d), [#32764](https://github.com/open-webui/open-webui/issues/32764)

> ⬅️ **Right-to-left question cards.** Question cards from Ask User now follow the Chat Direction setting, so Hebrew and Arabic questions and answers are laid out right to left. [#32784](https://github.com/open-webui/open-webui/pull/32784), [Commit](https://github.com/open-webui/open-webui/commit/aee4cbf4639281f711018af08e029e0f501fd3c4), [#32778](https://github.com/open-webui/open-webui/issues/32778)

> 🧷 **Tool server array parameters.** An array query parameter now reaches an OpenAPI tool server as repeated values instead of one text value that looks like a Python list. [#32677](https://github.com/open-webui/open-webui/pull/32677), [Commit](https://github.com/open-webui/open-webui/commit/fd1e59b25ff68ff015ce84707839084157df6045), [#32676](https://github.com/open-webui/open-webui/issues/32676)

> 📚 **Multi-folder knowledge drops.** Dropping several folders on a knowledge base now uploads all of them, where only the first one was uploaded. [#32653](https://github.com/open-webui/open-webui/pull/32653), [Commit](https://github.com/open-webui/open-webui/commit/d907b61816018202d2425109fbf9b506107e7182), [#32652](https://github.com/open-webui/open-webui/issues/32652)

> 🧩 **Restored skill-only drafts.** A draft that holds only a skill, brought back to the chat input, now sends only that skill, where the names of every skill were sent. [#32690](https://github.com/open-webui/open-webui/pull/32690), [Commit](https://github.com/open-webui/open-webui/commit/14956af03f2ba50a154b13ff77166139fdcc0315), [#32689](https://github.com/open-webui/open-webui/issues/32689)

> 🐍 **Python code block results.** Running a plotting block again now shows only the new plot, and a block whose last value is a date, decimal number or other object shows that value instead of "Maximum call stack size exceeded". [#32686](https://github.com/open-webui/open-webui/pull/32686), [Commit](https://github.com/open-webui/open-webui/commit/1a0bdb38a179ace36419aee87688727a9466a25a), [#32685](https://github.com/open-webui/open-webui/issues/32685), [#32682](https://github.com/open-webui/open-webui/pull/32682), [Commit](https://github.com/open-webui/open-webui/commit/fb5eec56dd2212d07a77dfb4ed4b25d26ccebcb2), [#32681](https://github.com/open-webui/open-webui/issues/32681)

> 🪟 **Preview of an earlier artifact.** Preview on an earlier code block now opens that block's artifact when the artifacts pane was closed, where it opened the newest one. [#32688](https://github.com/open-webui/open-webui/pull/32688), [Commit](https://github.com/open-webui/open-webui/commit/9862a5bd613bb1c98166bb0eff1c8e824fa86723), [#32687](https://github.com/open-webui/open-webui/issues/32687)

> 🕸️ **Web pages on fresh installs.** Attached web pages and other HTML text extraction return their text again on fresh installs, where a broken update of a library underneath made them come back empty. [#33103](https://github.com/open-webui/open-webui/pull/33103), [Commit](https://github.com/open-webui/open-webui/commit/f32de07ddead5453658c828cd7e2c3a1c680934c)

> 🔎 **Shared Chats search paging.** A search in Shared Chats or in an admin's view of a user's chats now loads more than the first 60 results. [#32675](https://github.com/open-webui/open-webui/pull/32675), [Commit](https://github.com/open-webui/open-webui/commit/0f2d1af1ce2092b2d6021823a923ddd179682f52), [#32674](https://github.com/open-webui/open-webui/issues/32674)

> 🪞 **Notes open once.** A note that two people open at the same time, such as one imported from a Markdown or text file and not edited since, no longer shows and saves its text twice, also with several workers. [#33004](https://github.com/open-webui/open-webui/pull/33004), [Commit](https://github.com/open-webui/open-webui/commit/499b83fa8d47f592bd7d79cab270d5cfc12652be), [#33002](https://github.com/open-webui/open-webui/issues/33002), [Commit](https://github.com/open-webui/open-webui/commit/1407f83cfc8df4e727f82beabdd4da6e29fc1119), [#32824](https://github.com/open-webui/open-webui/issues/32824)

> 🔈 **Read Aloud stops on failure.** Read Aloud now stops requesting the remaining sentences once one fails, so an unavailable speech provider shows a single error instead of one for every sentence. [#33028](https://github.com/open-webui/open-webui/pull/33028), [Commit](https://github.com/open-webui/open-webui/commit/ea615c3a2e89d827e24016d719acb5ee63f409d2), [#33023](https://github.com/open-webui/open-webui/issues/33023)

> 🗄️ **Archived chats survive folders.** Archive All Chats now takes the chats out of their folders, so deleting a folder afterwards no longer deletes those archived chats for good. [#32647](https://github.com/open-webui/open-webui/pull/32647), [Commit](https://github.com/open-webui/open-webui/commit/97f5c4e973a703b63a2606b054de324db88f706f), [#32646](https://github.com/open-webui/open-webui/issues/32646)

> 🔌 **No hangs after closed pages.** Closing a page while it was still loading, such as a chat export or a file's processing status, no longer loses database connections on SQLite, where later requests could hang or fail with 503 once enough were lost. [#32617](https://github.com/open-webui/open-webui/pull/32617), [Commit](https://github.com/open-webui/open-webui/commit/2355b8a3699826eaf1fe5a344f63e292f9532c48), [#32609](https://github.com/open-webui/open-webui/issues/32609), [#32741](https://github.com/open-webui/open-webui/issues/32741)

> 🪄 **Function input dialogs answered.** Confirming or cancelling a function's input or confirmation dialog now reaches the function when a script event arrived while the dialog was open, where the function kept waiting for an answer. [#32744](https://github.com/open-webui/open-webui/pull/32744), [Commit](https://github.com/open-webui/open-webui/commit/2d9852c6048774c0d8913c722b5fe661326f1b4d), [#32742](https://github.com/open-webui/open-webui/issues/32742)

> 🛑 **Stop sequences with percent.** A stop sequence containing % no longer stops every message from sending. [#32649](https://github.com/open-webui/open-webui/pull/32649), [Commit](https://github.com/open-webui/open-webui/commit/fdb304be2f5250c9282bacd3ff91757e55b89976), [#32648](https://github.com/open-webui/open-webui/issues/32648)

> 🗜️ **Channel image compression by default.** With image compression on, images in channels are now compressed when Compress Images in Channels is left at its default, where they were sent uncompressed. [#32693](https://github.com/open-webui/open-webui/pull/32693), [Commit](https://github.com/open-webui/open-webui/commit/70fb5462eab6b71e258c9fbd9ce5714bd173bcfb), [#32692](https://github.com/open-webui/open-webui/issues/32692)

> 🎙️ **Microphone off when leaving.** Leaving a chat while dictating now turns the microphone off. [#32640](https://github.com/open-webui/open-webui/pull/32640), [Commit](https://github.com/open-webui/open-webui/commit/636b631ab7cf2f4053c43466468cd4bb119dd250), [#32638](https://github.com/open-webui/open-webui/issues/32638), [#32639](https://github.com/open-webui/open-webui/issues/32639)

> ✏️ **Chat titles of only spaces.** Renaming a chat to only spaces now keeps its title and shows an error instead of saving a blank title. [#32770](https://github.com/open-webui/open-webui/pull/32770), [Commit](https://github.com/open-webui/open-webui/commit/9cbd27011b1d1842f52cbf91b4b5764b5820b52b), [#32769](https://github.com/open-webui/open-webui/issues/32769)

> 🔤 **No stray formatting spaces.** Chat messages no longer show an extra space at the start of each paragraph and before italic, bold, struck-through or linked text, which appeared in 0.12.3 and left a gap after an em dash. [#32743](https://github.com/open-webui/open-webui/pull/32743), [Commit](https://github.com/open-webui/open-webui/commit/2bebbb44e1a04b220f831aced950b0e334529988), [#32739](https://github.com/open-webui/open-webui/issues/32739)

> 🧭 **Scrolling while a reply streams.** On slow or busy devices a streaming reply now keeps the view at the bottom as its content grows, where it stopped following partway through, and scrolling up while it streams is no longer pulled back down. [Commit](https://github.com/open-webui/open-webui/commit/5a46aad0f0702536c98c9a26ae7d04482cdac784), [#32728](https://github.com/open-webui/open-webui/issues/32728)

> ⚡ **Early updates in new chats.** The first reply of a new chat no longer stays empty with the Stop button showing when its error or content arrives before the page knows the new chat, a message added while a chat is still loading no longer stays missing until a reload, and a message queued during the first reply of a new chat is sent once that reply finishes. [Commit](https://github.com/open-webui/open-webui/commit/cbd06d2aad0d64c2a50b4989c4290762de2cd3f0), [Commit](https://github.com/open-webui/open-webui/commit/d5038fec44d2f37e81798a6c7f4340a8d1a62f10), [#32550](https://github.com/open-webui/open-webui/issues/32550), [#32761](https://github.com/open-webui/open-webui/issues/32761)

> 📋 **Drafts with variables kept.** Reloading the page with a chat input draft that contains {{ }} placeholders, or editing a queued message that contains them, now keeps the text as it was, where it asked for input variables and dropped the text. [Commit](https://github.com/open-webui/open-webui/commit/6dbd375c267dd0dafc83c480ec23e3b1a7156406), [#32650](https://github.com/open-webui/open-webui/issues/32650)

> 🍴 **No fork in temporary chats.** The Fork chat option is now hidden in temporary chats and the /fork command answers that there is no chat to fork, where forking failed with an error. [#32839](https://github.com/open-webui/open-webui/pull/32839), [Commit](https://github.com/open-webui/open-webui/commit/1a492207971a5118dde2fe6b523edf7021f38cc9), [#32833](https://github.com/open-webui/open-webui/issues/32833)

> 🚀 **First message after loading.** A message sent right after the page loads is no longer wiped by the new chat setup still running, where it disappeared and its reply stayed empty until a reload. [#32829](https://github.com/open-webui/open-webui/pull/32829), [Commit](https://github.com/open-webui/open-webui/commit/4ed1af6879ee632a3130771b4a960ccf37c1c305), [#32819](https://github.com/open-webui/open-webui/issues/32819)

> 🎞️ **Left-aligned PowerPoint titles.** The PowerPoint preview now keeps titles and subtitles that the file aligns left on the left, where it centered them. [#32876](https://github.com/open-webui/open-webui/pull/32876), [Commit](https://github.com/open-webui/open-webui/commit/8fa77c8282b10e7de36863c4df6583a62a55354c), [#32873](https://github.com/open-webui/open-webui/issues/32873)

> 🐚 **Launcher help in zsh.** The examples in the Docker Compose launcher help now quote options with square brackets, so they also work when pasted into zsh. [#32881](https://github.com/open-webui/open-webui/pull/32881), [Commit](https://github.com/open-webui/open-webui/commit/52f51ea4f3044072d49eefd4feedb859bb66b80c), [#32878](https://github.com/open-webui/open-webui/issues/32878)

> 🏷️ **Tooltips show text as written.** Tooltips now show names, paths and descriptions that contain angle brackets as written, where they came out mangled or partly missing. [#32953](https://github.com/open-webui/open-webui/pull/32953), [Commit](https://github.com/open-webui/open-webui/commit/3299a097530847ec53da01a5964cf7ef8592dee0)

> 📡 **Websockets after Redis reconnects.** With the Redis websocket manager and "retry_on_timeout" in "WEBSOCKET_REDIS_OPTIONS", an instance now accepts new browser connections again once Redis is back after its connection dropped, where since 0.12.3 every new connection could hang until the instance was restarted. [#33009](https://github.com/open-webui/open-webui/pull/33009), [Commit](https://github.com/open-webui/open-webui/commit/0d17660535dd2ad9d6f0b75a2a2f5855066cd0a0), [#33008](https://github.com/open-webui/open-webui/issues/33008)

> 🔧 **Direct Integrations off disables connections.** While Direct Integrations is off, as it is by default, the tool servers and Open Terminal connections that users and admins saved in their Integrations settings are no longer used in chats, where turning it off only hid the settings tab, so instances that never turned it on lose those connections until an admin turns on Direct Integrations in Admin Settings > Connections or sets "ENABLE_DIRECT_INTEGRATIONS". [#32996](https://github.com/open-webui/open-webui/pull/32996), [Commit](https://github.com/open-webui/open-webui/commit/3e9d6cb9508a1ba4ec18017b3c80afaf6ac59a89)

> 🐳 **Python 3.12 Docker image.** The Docker image now runs Python 3.12 on Debian 13 instead of Python 3.11 on Debian 12, so custom functions, tools and packages installed with pip inside the container need versions that support Python 3.12. [#32861](https://github.com/open-webui/open-webui/pull/32861), [Commit](https://github.com/open-webui/open-webui/commit/a915df8ce12b32109b7b929cb2cad6046293aef6)

> 🤝 **Sharing permissions enforced everywhere.** Sharing permissions such as Models Sharing, Knowledge Sharing and Folders Sharing now also apply to sharing through the API, and a change in an item's Access settings that a user is not allowed to make is now refused with an error instead of being quietly left out. [Commit](https://github.com/open-webui/open-webui/commit/5f95008abdfbbbfbe5c080de0347deb70eb507b6)

> 🗄️ **Manage Files shows only yours.** Manage Files in Settings > Data Controls now lists only your own files, also for administrators, who saw every user's files there while "BYPASS_ADMIN_ACCESS_CONTROL" was on, as it is by default. [Commit](https://github.com/open-webui/open-webui/commit/2a86805648f45c36c479c6f9a0127cae799ee14f)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-25-16-model-support-changes-in-v0-12-4|16 Model Support changes in v0.12.4]] · Model Support
- [[Changes/Open WebUI/2026-10-25-10-safety-and-privacy-changes-in-v0-12-4|10 Safety and Privacy changes in v0.12.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-25-13-interface-experience-changes-in-v0-12-4|13 Interface Experience changes in v0.12.4]] · Interface Experience
- [[Changes/Open WebUI/2026-10-25-images-settings-save-admins-can-now-save-images-settings-while-image-generation|🖌️ Images settings save. Admins can now save Images settings while Image…]] · Image Generation
- [[Changes/Open WebUI/2026-10-25-4-voice-and-audio-changes-in-v0-12-4|4 Voice and Audio changes in v0.12.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-25-4-context-window-changes-in-v0-12-4|4 Context Window changes in v0.12.4]] · Context Window
- [[Changes/Open WebUI/2026-10-25-5-apps-and-integrations-changes-in-v0-12-4|5 Apps and Integrations changes in v0.12.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-25-4-editor-experience-changes-in-v0-12-4|4 Editor Experience changes in v0.12.4]] · Editor Experience
- [[Changes/Open WebUI/2026-10-25-3-reliability-and-performance-changes-in-v0-12-4|3 Reliability and Performance changes in v0.12.4]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-25-5-account-and-access-changes-in-v0-12-4|5 Account and Access changes in v0.12.4]] · Account and Access
- [[Changes/Open WebUI/2026-10-25-3-files-and-data-changes-in-v0-12-4|3 Files and Data changes in v0.12.4]] · Files and Data
- [[Changes/Open WebUI/2026-10-25-shared-chat-pages-load-once-chats-opened-under-s-through-a-share-link-or-by-an-a|🔗 Shared chat pages load once. Chats opened under /s/, through a share link…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-25-web-search-settings-save-admins-can-now-save-web-search-settings-such-as-the-web|🌍 Web Search settings save. Admins can now save Web Search settings such…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-25-translation-updates-translations-for-korean-cebuano-thai-german-japanese-vietnam|🌐 Translation updates. Translations for Korean, Cebuano, Thai, German, Japanese…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-10-24 · Windsurf · [[Changes/Windsurf/2026-10-24-2-developer-workflow-changes-in-v3-11-216|2 Developer Workflow changes in v3.11.216]]
- Later: 2026-10-26 · Claude Code · [[Changes/Claude Code/2026-10-26-4-developer-workflow-changes-in-v2-1-311|4 Developer Workflow changes in v2.1.311]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-25-9b5bf2&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-25-49-developer-workflow-changes-in-v0-12-4.md%0ACard%20ID%3A%20open-webui-2026-10-25-9b5bf2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->