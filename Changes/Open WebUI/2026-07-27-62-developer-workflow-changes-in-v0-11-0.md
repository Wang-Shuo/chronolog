---
card_id: open-webui-2026-07-27-3aee42
date: '2026-07-27'
description: "Open WebUI · 2026-07-27 · Developer Workflow: 62 changes in v0.11.0
  — \U0001F4C2 **Folder pages.** Opening a folder now takes you to its own page, where
  its chats load…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1227
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 02b93e3f1e155eb6a30d38c1849167977a1dfd37807ce1818f950a61013a56a6
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-27-3aee42
  comparison: ''
  date: '2026-07-27'
  description: 'Open WebUI — v0.11.0: 62 Developer Workflow changes'
  evidence:
  - quote: "\U0001F4C2 **Folder pages.** Opening a folder now takes you to its own
      page, where its chats load a page at a time, can be sorted by title or last
      updated, and you can start a new chat straight from the folder. [Commit](https://github.com/open-webui/open-webui/commit/409fb39717be9ab7becd9e8c01801a08c5bae318)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⏲️ **Chat timers.** The assistant can now set a timer that brings a prompt
      back into the conversation later, after a delay or at a set time, and can drop
      it automatically if you read the chat or reply before it fires. [Commit](https://github.com/open-webui/open-webui/commit/b23ddeb2800098c6352203ec8fbe9fca40ba415c)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5EF️ **Full replies in channels.** A reply from the assistant in
      a channel is now saved and shown in full, with its reasoning, tool calls and
      other structured parts, where it previously came through blank. [Commit](https://github.com/open-webui/open-webui/commit/498cdab9a548d7d2fd19c389204ee26236fc7efe),
      [#26720](https://github.com/open-webui/open-webui/pull/26720), [#27409](https://github.com/open-webui/open-webui/pull/27409),
      [#26707](https://github.com/open-webui/open-webui/issues/26707), [#26656](https://github.com/open-webui/open-webui/issues/26656)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4E3 **Notifications from the assistant.** The assistant can now
      send you a notification itself when something is worth your attention, so a
      long task can reach you after you have moved on to something else. [Commit](https://github.com/open-webui/open-webui/commit/c55e373b994d3a14c99a97f44261422012f63266),
      [Commit](https://github.com/open-webui/open-webui/commit/200d447f6289faca42f2a666bbabae2c7f3ebadf)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5DC️ **Compact a chat on demand.** Typing a compact command in
      a long conversation now summarizes the earlier turns straight away, instead
      of waiting for it to happen automatically once the conversation grows past the
      threshold. [Commit](https://github.com/open-webui/open-webui/commit/7a9928ef172b7c280c377c86cb52957e39340158),
      [Commit](https://github.com/open-webui/open-webui/commit/75894161e46aafe30a7db4ecc946af60f04495e4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F33F **Fork a chat.** Every response now has a fork button that
      copies the conversation up to that point into a new chat which remembers where
      it branched, so you can carry on down a different path without touching the
      original. [Commit](https://github.com/open-webui/open-webui/commit/63ada247066dfc51e0e9559366f0cfd9a98db40b),
      [Commit](https://github.com/open-webui/open-webui/commit/cf887b68ea58bcd1d8b035842c4ea35a5113ed8b),
      [Commit](https://github.com/open-webui/open-webui/commit/73421c5b42ac5c2ebc5faa520b7ed3fa0e39f10d),
      [Commit](https://github.com/open-webui/open-webui/commit/e769f9ff4f9fa7b0faebdd4f34ff98fe0dcc300d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F3B9 **Customizable keyboard shortcuts.** Most keyboard shortcuts
      can now be rebound to key combinations of your choosing in settings, which saves
      them to your account, warns you when two actions share a combination, and offers
      a reset to the defaults, with moving to the previous or next chat and opening
      the controls panel available to bind as well. [Commit](https://github.com/open-webui/open-webui/commit/343eb1d659262cc9d762a2ce49bef25434a03bfa),
      [Commit](https://github.com/open-webui/open-webui/commit/de681aa543b356d456b83c13ad88c7f9941319e7),
      [#26624](https://github.com/open-webui/open-webui/pull/26624)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⌨️ **Skills in slash commands.** Typing a slash in the message input now
      lists your skills alongside your prompts, grouped under headings and with descriptions
      on hover, so you can attach a skill without leaving the keyboard. [Commit](https://github.com/open-webui/open-webui/commit/9588c97e64e10d161a9a0ab1ab9ba3fee6cbb94d)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5D2️ **Notes without stored contents.** A note whose contents were
      never filled in now opens and saves normally instead of failing. [Commit](https://github.com/open-webui/open-webui/commit/6c59ef313fdaac7fa8e9089be758c4651f8b9412)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⬇️ **Response auto-scroll toggle.** A new interface setting lets you stop
      the view following a reply as it is written, so you can read earlier text while
      generation continues. [Commit](https://github.com/open-webui/open-webui/commit/cea991260f279f004489dab5d930bc25b0abf612),
      [#26826](https://github.com/open-webui/open-webui/pull/26826)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⏱️ **Idle cap for streamed replies.** Administrators can now set an "AIOHTTP_CLIENT_STREAM_IDLE_TIMEOUT"
      that ends a streamed reply when the provider stops sending anything for that
      long, instead of holding the connection open until the overall timeout expires.
      [Commit](https://github.com/open-webui/open-webui/commit/4a7d4ebadac27d652ec200fa3939f10e9a5c17ed),
      [Commit](https://github.com/open-webui/open-webui/commit/c727643e05f3597395ee1a60b17117d04f693a18)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9F5 **Where a channel reply lands.** Administrators can now choose
      whether a reply to a mention posts in a thread under that message or straight
      into the channel. [Commit](https://github.com/open-webui/open-webui/commit/db2d24896b0682191a54f41c6b9f0b9d2971637f),
      [#27410](https://github.com/open-webui/open-webui/pull/27410)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4DA **Limits for knowledge tools.** Administrators can now set
      how much a knowledge search or file view may return, how many files one search
      may scan, and how many matches are reported, and a knowledge command's whole
      output is now capped so a single call cannot flood the conversation. [Commit](https://github.com/open-webui/open-webui/commit/11e61b69ebd922602edc37ded7b42fdd43bb8456),
      [#27524](https://github.com/open-webui/open-webui/pull/27524), [#27327](https://github.com/open-webui/open-webui/issues/27327),
      [#26139](https://github.com/open-webui/open-webui/issues/26139)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F39B️ **File streaming chunk size.** Administrators can now tune
      how large each chunk of a streamed file transfer is through a new \"AIOHTTP_FILE_STREAM_CHUNK_SIZE\"
      setting. [Commit](https://github.com/open-webui/open-webui/commit/429f2df50cd2f0ec8d0a1bb4136a46e2f94a4bf5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F39A️ **Passthrough parameters per connection.** Administrators
      can now list request parameters that a connection should receive untranslated,
      under a new Advanced section in connection settings, so provider-specific options
      reach the upstream API intact. [Commit](https://github.com/open-webui/open-webui/commit/bb12b1a18b77d80829cedb2d5bf965808222415b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F170️ **Anthropic requests passed straight through.** Requests to
      the Anthropic-compatible API aimed at an Anthropic or LiteLLM connection now
      reach the provider untouched rather than being translated on the way, and LiteLLM
      is selectable as a connection type. [Commit](https://github.com/open-webui/open-webui/commit/b81627b2c95aad184a6abf59145ca3b18a32bb2c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F522 **Anthropic token-counting endpoint.** The Anthropic-compatible
      API now offers a token-counting endpoint, so integrations can check how many
      input tokens a request will use before sending it. [Commit](https://github.com/open-webui/open-webui/commit/08dacd19da1b0eefd9d274d24ed59ec1e5d5a2de),
      [Commit](https://github.com/open-webui/open-webui/commit/23062e9fcaace42cf06db33f9533127bbbcd33d9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5B2️ **Terminal instructions read fresh.** The instructions a terminal
      server provides are now fetched for each request, so changing them on the server
      takes effect immediately instead of after re-saving the connection or restarting.
      [#27242](https://github.com/open-webui/open-webui/pull/27242)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5A5️ **Live terminal server policies.** Administrators can now
      read an orchestrator terminal server's current policy and lifecycle settings
      directly in connection settings rather than relying on a locally cached copy.
      [Commit](https://github.com/open-webui/open-webui/commit/2f37e853d1259a901f736a823bad29dcc2c3b130),
      [Commit](https://github.com/open-webui/open-webui/commit/3005b7bc71fcbd5abc6e73c3e4caa4ea781cdb76)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4C8 **Personal usage dashboard.** A new Usage tab in settings shows
      your own activity over time, including a token-activity heatmap, current and
      longest streaks, lifetime and peak token counts, your longest active chat, and
      your most used models and tools. [Commit](https://github.com/open-webui/open-webui/commit/af9a315ac30b83241f3df5556d7a2abfcd5d25b0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9FE **Group permissions at a glance.** The groups list now shows
      whether each group uses custom or default permissions, without opening it. [Commit](https://github.com/open-webui/open-webui/commit/ccb1ab7739fbeb77c810036dcac240570034a56a),
      [Commit](https://github.com/open-webui/open-webui/commit/1d1f60ab440b167b9c6ab8f4011b884caa99f27d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9CA **Quicker collection checks on Chroma.** Checking whether a
      collection exists now asks for that one collection instead of listing them all,
      which grew slower with every knowledge base and file. [Commit](https://github.com/open-webui/open-webui/commit/48ee357156fd7f567ea13eb5ddba0a25701c0351),
      [#27394](https://github.com/open-webui/open-webui/pull/27394)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F464 **Lighter user activity checks.** Checking whether someone
      is currently active now reads only that timestamp rather than their whole profile,
      including their profile image. [Commit](https://github.com/open-webui/open-webui/commit/c8f2e09fdcafc800c1e3af6da1cd6f2581cd9191),
      [#27224](https://github.com/open-webui/open-webui/pull/27224)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F30A **Steadier long responses.** Building up a streamed reply no
      longer costs more work as it grows, so long answers keep pace instead of slowing
      down toward the end. [#27231](https://github.com/open-webui/open-webui/pull/27231),
      [#27359](https://github.com/open-webui/open-webui/pull/27359), [Commit](https://github.com/open-webui/open-webui/commit/ba556bd8f0517881cb250bb512631ddf8a0c82c3),
      [#27390](https://github.com/open-webui/open-webui/pull/27390)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F6F0️ **Fewer Sentinel lookups.** Redis Sentinel deployments no
      longer ask which server is the primary and open a fresh connection before every
      single command, which had caused heavy connection churn and stalls under load.
      [Commit](https://github.com/open-webui/open-webui/commit/75a8a0046b5b2ebd9942b25035b346aa953f81cc),
      [#27213](https://github.com/open-webui/open-webui/pull/27213), [#27210](https://github.com/open-webui/open-webui/issues/27210)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⚡ **Lighter model lists.** Model lists no longer carry embedded profile
      images in their data, so they load faster. [Commit](https://github.com/open-webui/open-webui/commit/9281adc5647b7046e3ddcc53ac4b84be7f650221),
      [Commit](https://github.com/open-webui/open-webui/commit/f3a35507845e4a911c3d278d680a9989bb8d99ad)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F51B **Functions can react to being switched on or off.** Two new
      events fire just before a function is enabled or disabled, and the function
      being enabled receives its own event even though it is not active yet, so it
      can run whatever setup or teardown it needs. [Commit](https://github.com/open-webui/open-webui/commit/94a60b04573acf6423e9c0519997b779f82e0560),
      [#26754](https://github.com/open-webui/open-webui/pull/26754), [#26748](https://github.com/open-webui/open-webui/discussions/26748)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F397️ **Terminal single sign-on tokens.** The token forwarded to
      a terminal server for single sign-on is now taken from your own session on the
      server rather than from a header the browser supplied, so a caller can no longer
      send someone else's token in its place. [#26719](https://github.com/open-webui/open-webui/pull/26719)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9EB **Files attached to a shared folder.** Adding files to a folder
      is now refused unless the folder's owner can read them, and a folder's files
      are checked against what its owner can still read before they are used as knowledge
      in chat, so a collaborator can no longer place files into someone else's folder
      or keep serving files the owner has since lost access to. [#27464](https://github.com/open-webui/open-webui/pull/27464),
      [Commit](https://github.com/open-webui/open-webui/commit/56183fcb17142088e2a34d1e35228f013749030c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9F7 **Knowledge claimed by a direct connection.** Files listed
      as knowledge on a model supplied by the browser for a direct connection are
      now filtered against your own access before anything is retrieved, so a crafted
      request can no longer pull in documents you cannot otherwise open. [Commit](https://github.com/open-webui/open-webui/commit/305880f2e2aeb2dda2f4b2a18a20bdcd558f7134),
      [#26723](https://github.com/open-webui/open-webui/pull/26723)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5E8️ **Response text where it was missing.** Assistant replies
      are no longer stored without their text, so copying, exporting, searching and
      reusing a conversation return the reply instead of nothing. [Commit](https://github.com/open-webui/open-webui/commit/33cf3fbb7f017ab1b79dce5c5ca4d4e1c3092844),
      [#26799](https://github.com/open-webui/open-webui/pull/26799), [#26436](https://github.com/open-webui/open-webui/issues/26436)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FAAB **Terminal choice cleared on load.** Your selected terminal
      is no longer dropped while the list of terminals is still loading, so it survives
      a page refresh. [Commit](https://github.com/open-webui/open-webui/commit/9707d3a5c21d2fedada602f2cfd8a104cdc5e5d1),
      [Commit](https://github.com/open-webui/open-webui/commit/f59d86a10cb31e48d2dae0033081a09dbbaafc8c),
      [Commit](https://github.com/open-webui/open-webui/commit/2f2bf38e3481077597b5ad60f57685813e8d71b8),
      [#26775](https://github.com/open-webui/open-webui/pull/26775), [#26677](https://github.com/open-webui/open-webui/issues/26677)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4AD **Reasoning that arrives late or empty.** Reasoning sent by
      a provider after the answer has started is now shown in its proper place above
      the answer rather than appended after it, and reasoning notes carrying nothing
      no longer open an empty thinking block. [Commit](https://github.com/open-webui/open-webui/commit/051a1f6c41d1d37e5a12ce2068fc6f8488940591),
      [#26687](https://github.com/open-webui/open-webui/pull/26687), [#26645](https://github.com/open-webui/open-webui/issues/26645)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F6D1 **Stopping an answer the moment it starts.** Each answer in
      a chat now carries its own task identifier from the first event onward, so stopping
      one immediately after sending no longer misses. [Commit](https://github.com/open-webui/open-webui/commit/aadab2f480a8c17a9265a244d262947da23ddc79)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⏸️ **Deleting while a reply is being written.** The delete control is now
      hidden on messages while a response is generating or a task is running, so a
      conversation can no longer be left with the finished reply detached from the
      messages before it. [Commit](https://github.com/open-webui/open-webui/commit/b4d13793a3af2d75aaf33fe9793cbbf278958940),
      [#26668](https://github.com/open-webui/open-webui/issues/26668)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F381 **Feedback while a download is prepared.** Downloading a file
      or folder from the terminal now tells you it is being prepared, will not start
      the same archive twice if you click again, and reports a failure instead of
      quietly giving up or leaving a preview spinning. [#27421](https://github.com/open-webui/open-webui/pull/27421),
      [#27055](https://github.com/open-webui/open-webui/issues/27055)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4DC **Chats past the first sixty in a folder.** Folder listings
      now page through every chat instead of stopping at a fixed limit, so older chats
      no longer appear to vanish from a folder once it grows past sixty. [#26786](https://github.com/open-webui/open-webui/issues/26786),
      [Commit](https://github.com/open-webui/open-webui/commit/409fb39717be9ab7becd9e8c01801a08c5bae318)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F39B️ **Typing a top_k value.** The top_k box in advanced parameters
      now accepts whole numbers up to its limit and rejects anything else, instead
      of letting the slider and the box disagree over what is allowed. [Commit](https://github.com/open-webui/open-webui/commit/34920213619eb66467470105cbe3a275c812ccbc),
      [#26669](https://github.com/open-webui/open-webui/issues/26669)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F526 **Chat search on PostgreSQL.** Searching your chats now finds
      matches in current conversations on PostgreSQL setups, instead of only matching
      chats still stored in the older format. [Commit](https://github.com/open-webui/open-webui/commit/cc9a44569ef08b64ff44d15607c43966f362ce75)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F50D **Knowledge base file search.** Searching inside knowledge
      base files now returns matching lines with correct line numbers, and patterns
      that list alternatives separated by a pipe find matches instead of silently
      returning none. [#27249](https://github.com/open-webui/open-webui/pull/27249),
      [Commit](https://github.com/open-webui/open-webui/commit/e18e249d5da3d8fe701a885edc64341cc5dbf813),
      [Commit](https://github.com/open-webui/open-webui/commit/8d2fee5d4559d030b53575d377a0013e2c67b9fe),
      [#26795](https://github.com/open-webui/open-webui/pull/26795), [#26781](https://github.com/open-webui/open-webui/issues/26781),
      [#26744](https://github.com/open-webui/open-webui/issues/26744)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FA99 **Documents containing special tokens.** Splitting text by
      tokens no longer fails when the content contains reserved marker sequences,
      so those pages and files can be fetched and added to a knowledge base. [Commit](https://github.com/open-webui/open-webui/commit/33cf3fbb7f017ab1b79dce5c5ca4d4e1c3092844),
      [#27094](https://github.com/open-webui/open-webui/issues/27094)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FA83 **Backslashes in terminal proxy paths.** A request to the terminal
      proxy containing a backslash is now refused, closing a way to smuggle directory
      traversal past the path check to an upstream that treats it as a separator.
      [#27198](https://github.com/open-webui/open-webui/pull/27198)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9F1 **Internal addresses disguised as public ones.** A web address
      that hides an internal target inside an IPv6 address, through the mapped, 6to4,
      Teredo or NAT64 forms, is now recognised and refused like any other internal
      address. [Commit](https://github.com/open-webui/open-webui/commit/1717b493d83c86afa82aa8bc50139250852dd2f3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FAA4 **Tighter checks when a page is fetched.** Every request a
      fetched page makes is now checked against the address rules rather than only
      the page itself, each hop of a redirect is checked in turn, and background workers
      and socket connections the page tries to open are refused. [Commit](https://github.com/open-webui/open-webui/commit/bef63a2ae915571d50d2722a635e8bfa753d7877),
      [#27042](https://github.com/open-webui/open-webui/pull/27042), [#27008](https://github.com/open-webui/open-webui/pull/27008)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9EE **Anthropic usage reporting.** Responses from the Anthropic-compatible
      API now report accurate input and output token counts, pass through cache and
      server tool figures where the provider gives them, and leave the input count
      out entirely rather than reporting zero when it is unknown. [Commit](https://github.com/open-webui/open-webui/commit/e8b59b2ef35ecb727fa760cd565d6da20c9e7e79),
      [Commit](https://github.com/open-webui/open-webui/commit/51ff386fd6461c07225d10a0de530019eebdd157),
      [Commit](https://github.com/open-webui/open-webui/commit/0576e8eeb5797a36b43eba5790a4e2a5dd8e5a4d),
      [Commit](https://github.com/open-webui/open-webui/commit/8e74cac8decc0a54137d7214e70c33b0dd52a99a),
      [Commit](https://github.com/open-webui/open-webui/commit/93a34bb25b32ae0b3a876fd3161c7778227b76bf),
      [Commit](https://github.com/open-webui/open-webui/commit/4c2d864b3f4c1ae6c4c9bd93aea078d4bf520463),
      [#26790](https://github.com/open-webui/open-webui/pull/26790), [#27293](https://github.com/open-webui/open-webui/pull/27293),
      [Docs:#1328](https://github.com/open-webui/docs/issues/1328)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F68F **Stray terminal containers.** Terminal orchestrator connections
      that use a policy now send every request through that policy, so each person
      no longer ends up with a second unintended container alongside the intended
      one. [#26945](https://github.com/open-webui/open-webui/issues/26945), [Commit](https://github.com/open-webui/open-webui/commit/7088d245bb45fc69c0b22748563b9f3c6f0daa73)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9F9 **Orphaned sessions get cleaned up.** The instance that reaps
      sessions left behind by a crashed worker now keeps trying if another instance
      holds the job, rather than one instance giving up for good and leaving stale
      sessions to accumulate, and the lock it uses can no longer be released or renewed
      by an instance that does not hold it. [Commit](https://github.com/open-webui/open-webui/commit/bf35f64a7f14161933dfa608577a977d107b1569),
      [Commit](https://github.com/open-webui/open-webui/commit/846ba80a9d5e75837d3db37185e9a23b1e6bfe78)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9CA **Redis cluster connections.** A deployment using Redis in
      cluster mode is no longer handed a connection built for a single server, or
      the reverse, when both point at the same address. [Commit](https://github.com/open-webui/open-webui/commit/fc4906c9e9df3fa42bb9073ac197383347caa853)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F6DF **Redis failover on timeouts.** A Redis connection that times
      out now retries against a freshly resolved primary instead of failing, so Sentinel
      setups recover from a failover rather than erroring out. [Commit](https://github.com/open-webui/open-webui/commit/75a8a0046b5b2ebd9942b25035b346aa953f81cc),
      [#27210](https://github.com/open-webui/open-webui/issues/27210)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FAE5 **Temporary chats and channels write nothing.** Generating
      or editing an image and status updates in a temporary chat or a channel message
      no longer try to save themselves against a conversation that was never stored,
      and the task list tools are no longer offered there at all rather than being
      offered and then failing. [Commit](https://github.com/open-webui/open-webui/commit/d484a2a99e3a0c21fdcad007a50ebc412fffbb2e),
      [Commit](https://github.com/open-webui/open-webui/commit/d2936c880cfc8cb71bb5c235926048ae189bba25),
      [Commit](https://github.com/open-webui/open-webui/commit/b45c020f68a9499b66e598e854b17a3f232b6cf2),
      [Commit](https://github.com/open-webui/open-webui/commit/71c4da8c065491a96e41da3c9f0c663e5f759468),
      [#27432](https://github.com/open-webui/open-webui/issues/27432)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F39E️ **Artifacts panel reopening itself.** The artifacts panel
      now opens once when a finished block is detected, so closing it partway through
      a reply no longer sees it forced back open on every word that follows. [Commit](https://github.com/open-webui/open-webui/commit/4856afcef8251969f751ade5760cefea9577c051),
      [#27399](https://github.com/open-webui/open-webui/issues/27399)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5BC️ **External message images.** Images hosted on other sites
      and referenced in a message now display inline instead of being replaced with
      a placeholder. [Commit](https://github.com/open-webui/open-webui/commit/890bfd0d9771d1919ce24f04e11b6c96589fca5b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: 〰️ **Text above a collapsible block.** A line written directly above a
      collapsible section is no longer turned into a large heading, and the section
      itself still renders as a collapsible widget rather than leaking its markup.
      [Commit](https://github.com/open-webui/open-webui/commit/7d77efe0f1cfa4782893ffde78419a96a95240f4),
      [#27148](https://github.com/open-webui/open-webui/pull/27148), [#27001](https://github.com/open-webui/open-webui/issues/27001)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F523 **Chats containing unusual characters.** Broken character sequences
      are now cleaned out of text before it is stored, so a conversation that picked
      one up still saves and still opens instead of failing to load. [Commit](https://github.com/open-webui/open-webui/commit/43e7eefa959918baf9fbf867a12b5d721fd782af),
      [#27201](https://github.com/open-webui/open-webui/pull/27201), [#27081](https://github.com/open-webui/open-webui/issues/27081)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FA9D **Blocked webhook targets look like failures.** A webhook pointing
      at an address that is not publicly reachable is now skipped with a short warning,
      instead of an error and a full traceback that read like the server crashing
      on startup. [Commit](https://github.com/open-webui/open-webui/commit/0671b7aa2b59f5c6235bfa85d6aba54e2ba91353),
      [#26975](https://github.com/open-webui/open-webui/issues/26975)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F575️ **Values printed in error logs.** A failure no longer prints
      the contents of nearby variables alongside its traceback, which could put keys
      and message content into the logs, and a new \"LOGURU_DIAGNOSE\" setting turns
      that detail back on for debugging. [Commit](https://github.com/open-webui/open-webui/commit/6aebfd88e938d1cd139068b5737a83a82ff393ed),
      [#26814](https://github.com/open-webui/open-webui/pull/26814)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FAB5 **Empty audit exclusion list.** Clearing the list of paths
      excluded from audit logging no longer switches off auditing altogether, so requests
      are recorded as intended. [#27370](https://github.com/open-webui/open-webui/pull/27370),
      [Commit](https://github.com/open-webui/open-webui/commit/2ef6c76f5126ccdef5d1c814004920941275f45d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F44D **Rating in feedback events.** Events sent when someone rates
      a response now carry the rating that was given, instead of reporting it as empty.
      [Commit](https://github.com/open-webui/open-webui/commit/300302d43259e119cd88247b3f246bea82b4dd8e),
      [#26840](https://github.com/open-webui/open-webui/issues/26840)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5D3️ **Schedules written by hand.** A recurrence rule is now read
      the same way whether it is written in upper or lower case, a start date in the
      rule is respected, second-by-second rules are understood, and a rule that cannot
      be supported is refused with a clear message instead of behaving unpredictably.
      [Commit](https://github.com/open-webui/open-webui/commit/c4ae8c86786fed521960466f6d8eef8af22c2946),
      [Commit](https://github.com/open-webui/open-webui/commit/2d928df30443516a9a3d6b71b0f31426a2362499),
      [#27470](https://github.com/open-webui/open-webui/pull/27470)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F6E0️ **Admin settings moved into settings.** Admin settings and
      the analytics dashboard are no longer separate pages and now open alongside
      your personal settings in the settings window, under their own Admin section,
      with the old links redirecting there. [Commit](https://github.com/open-webui/open-webui/commit/c1460570b7e2897a3e648441a0206ad25e603b8c),
      [Commit](https://github.com/open-webui/open-webui/commit/3ce3c529365a3cd9e5631b14bfffead6baa2b1ed),
      [Commit](https://github.com/open-webui/open-webui/commit/667cba1a9561166941f59faf3bfa24038288b449)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F3F7️ **Shorter titles without emojis.** Automatically generated
      titles for chats and notes are now two to four words and no longer include an
      emoji, and anyone who prefers the old style can restore it by editing the title
      generation prompt in admin settings. [Commit](https://github.com/open-webui/open-webui/commit/50d3c927bfed3b8dd94fd9f79bff258a84ecbd92),
      [Commit](https://github.com/open-webui/open-webui/commit/7a9928ef172b7c280c377c86cb52957e39340158)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4E6 **Storage emulator no longer bundled.** The optional Google
      Cloud Storage emulator is no longer installed as part of the full package, so
      anyone who relied on it for local storage testing now needs to install \"gcp-storage-emulator\"
      themselves. [Commit](https://github.com/open-webui/open-webui/commit/30415c925a18b1ea1c3f2739bd944dd939f020cf)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 62-developer-workflow-changes-in-v0-11-0
  source_release: open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f
  source_type: github_releases
  theme: developer-workflow
  title: 62 Developer Workflow changes in v0.11.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-22-changed-code-review-to-run-as-a-background-subagent-so-review-work-no-longer-fil|Changed
  /code-review to run as a background subagent, so review work no longer…]]'
- '[[Changes/GitHub Copilot CLI/2026-07-23-2-developer-workflow-changes-in-v1-0-74|2
  Developer Workflow changes in v1.0.74]]'
- '[[Changes/OpenCode/2026-07-24-support-the-current-server-terminal-transport|Support
  the current server terminal transport]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f]]'
source_type: github_releases
theme: developer-workflow
title: 62 Developer Workflow changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 62 Developer Workflow changes in v0.11.0

**Open WebUI** · 2026-07-27 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) · from [[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📂 **Folder pages.** Opening a folder now takes you to its own page, where its chats load a page at a time, can be sorted by title or last updated, and you can start a new chat straight from the folder. [Commit](https://github.com/open-webui/open-webui/commit/409fb39717be9ab7becd9e8c01801a08c5bae318)

> ⏲️ **Chat timers.** The assistant can now set a timer that brings a prompt back into the conversation later, after a delay or at a set time, and can drop it automatically if you read the chat or reply before it fires. [Commit](https://github.com/open-webui/open-webui/commit/b23ddeb2800098c6352203ec8fbe9fca40ba415c)

> 🗯️ **Full replies in channels.** A reply from the assistant in a channel is now saved and shown in full, with its reasoning, tool calls and other structured parts, where it previously came through blank. [Commit](https://github.com/open-webui/open-webui/commit/498cdab9a548d7d2fd19c389204ee26236fc7efe), [#26720](https://github.com/open-webui/open-webui/pull/26720), [#27409](https://github.com/open-webui/open-webui/pull/27409), [#26707](https://github.com/open-webui/open-webui/issues/26707), [#26656](https://github.com/open-webui/open-webui/issues/26656)

> 📣 **Notifications from the assistant.** The assistant can now send you a notification itself when something is worth your attention, so a long task can reach you after you have moved on to something else. [Commit](https://github.com/open-webui/open-webui/commit/c55e373b994d3a14c99a97f44261422012f63266), [Commit](https://github.com/open-webui/open-webui/commit/200d447f6289faca42f2a666bbabae2c7f3ebadf)

> 🗜️ **Compact a chat on demand.** Typing a compact command in a long conversation now summarizes the earlier turns straight away, instead of waiting for it to happen automatically once the conversation grows past the threshold. [Commit](https://github.com/open-webui/open-webui/commit/7a9928ef172b7c280c377c86cb52957e39340158), [Commit](https://github.com/open-webui/open-webui/commit/75894161e46aafe30a7db4ecc946af60f04495e4)

> 🌿 **Fork a chat.** Every response now has a fork button that copies the conversation up to that point into a new chat which remembers where it branched, so you can carry on down a different path without touching the original. [Commit](https://github.com/open-webui/open-webui/commit/63ada247066dfc51e0e9559366f0cfd9a98db40b), [Commit](https://github.com/open-webui/open-webui/commit/cf887b68ea58bcd1d8b035842c4ea35a5113ed8b), [Commit](https://github.com/open-webui/open-webui/commit/73421c5b42ac5c2ebc5faa520b7ed3fa0e39f10d), [Commit](https://github.com/open-webui/open-webui/commit/e769f9ff4f9fa7b0faebdd4f34ff98fe0dcc300d)

> 🎹 **Customizable keyboard shortcuts.** Most keyboard shortcuts can now be rebound to key combinations of your choosing in settings, which saves them to your account, warns you when two actions share a combination, and offers a reset to the defaults, with moving to the previous or next chat and opening the controls panel available to bind as well. [Commit](https://github.com/open-webui/open-webui/commit/343eb1d659262cc9d762a2ce49bef25434a03bfa), [Commit](https://github.com/open-webui/open-webui/commit/de681aa543b356d456b83c13ad88c7f9941319e7), [#26624](https://github.com/open-webui/open-webui/pull/26624)

> ⌨️ **Skills in slash commands.** Typing a slash in the message input now lists your skills alongside your prompts, grouped under headings and with descriptions on hover, so you can attach a skill without leaving the keyboard. [Commit](https://github.com/open-webui/open-webui/commit/9588c97e64e10d161a9a0ab1ab9ba3fee6cbb94d)

> 🗒️ **Notes without stored contents.** A note whose contents were never filled in now opens and saves normally instead of failing. [Commit](https://github.com/open-webui/open-webui/commit/6c59ef313fdaac7fa8e9089be758c4651f8b9412)

> ⬇️ **Response auto-scroll toggle.** A new interface setting lets you stop the view following a reply as it is written, so you can read earlier text while generation continues. [Commit](https://github.com/open-webui/open-webui/commit/cea991260f279f004489dab5d930bc25b0abf612), [#26826](https://github.com/open-webui/open-webui/pull/26826)

> ⏱️ **Idle cap for streamed replies.** Administrators can now set an "AIOHTTP_CLIENT_STREAM_IDLE_TIMEOUT" that ends a streamed reply when the provider stops sending anything for that long, instead of holding the connection open until the overall timeout expires. [Commit](https://github.com/open-webui/open-webui/commit/4a7d4ebadac27d652ec200fa3939f10e9a5c17ed), [Commit](https://github.com/open-webui/open-webui/commit/c727643e05f3597395ee1a60b17117d04f693a18)

> 🧵 **Where a channel reply lands.** Administrators can now choose whether a reply to a mention posts in a thread under that message or straight into the channel. [Commit](https://github.com/open-webui/open-webui/commit/db2d24896b0682191a54f41c6b9f0b9d2971637f), [#27410](https://github.com/open-webui/open-webui/pull/27410)

> 📚 **Limits for knowledge tools.** Administrators can now set how much a knowledge search or file view may return, how many files one search may scan, and how many matches are reported, and a knowledge command's whole output is now capped so a single call cannot flood the conversation. [Commit](https://github.com/open-webui/open-webui/commit/11e61b69ebd922602edc37ded7b42fdd43bb8456), [#27524](https://github.com/open-webui/open-webui/pull/27524), [#27327](https://github.com/open-webui/open-webui/issues/27327), [#26139](https://github.com/open-webui/open-webui/issues/26139)

> 🎛️ **File streaming chunk size.** Administrators can now tune how large each chunk of a streamed file transfer is through a new "AIOHTTP_FILE_STREAM_CHUNK_SIZE" setting. [Commit](https://github.com/open-webui/open-webui/commit/429f2df50cd2f0ec8d0a1bb4136a46e2f94a4bf5)

> 🎚️ **Passthrough parameters per connection.** Administrators can now list request parameters that a connection should receive untranslated, under a new Advanced section in connection settings, so provider-specific options reach the upstream API intact. [Commit](https://github.com/open-webui/open-webui/commit/bb12b1a18b77d80829cedb2d5bf965808222415b)

> 🅰️ **Anthropic requests passed straight through.** Requests to the Anthropic-compatible API aimed at an Anthropic or LiteLLM connection now reach the provider untouched rather than being translated on the way, and LiteLLM is selectable as a connection type. [Commit](https://github.com/open-webui/open-webui/commit/b81627b2c95aad184a6abf59145ca3b18a32bb2c)

> 🔢 **Anthropic token-counting endpoint.** The Anthropic-compatible API now offers a token-counting endpoint, so integrations can check how many input tokens a request will use before sending it. [Commit](https://github.com/open-webui/open-webui/commit/08dacd19da1b0eefd9d274d24ed59ec1e5d5a2de), [Commit](https://github.com/open-webui/open-webui/commit/23062e9fcaace42cf06db33f9533127bbbcd33d9)

> 🖲️ **Terminal instructions read fresh.** The instructions a terminal server provides are now fetched for each request, so changing them on the server takes effect immediately instead of after re-saving the connection or restarting. [#27242](https://github.com/open-webui/open-webui/pull/27242)

> 🖥️ **Live terminal server policies.** Administrators can now read an orchestrator terminal server's current policy and lifecycle settings directly in connection settings rather than relying on a locally cached copy. [Commit](https://github.com/open-webui/open-webui/commit/2f37e853d1259a901f736a823bad29dcc2c3b130), [Commit](https://github.com/open-webui/open-webui/commit/3005b7bc71fcbd5abc6e73c3e4caa4ea781cdb76)

> 📈 **Personal usage dashboard.** A new Usage tab in settings shows your own activity over time, including a token-activity heatmap, current and longest streaks, lifetime and peak token counts, your longest active chat, and your most used models and tools. [Commit](https://github.com/open-webui/open-webui/commit/af9a315ac30b83241f3df5556d7a2abfcd5d25b0)

> 🧾 **Group permissions at a glance.** The groups list now shows whether each group uses custom or default permissions, without opening it. [Commit](https://github.com/open-webui/open-webui/commit/ccb1ab7739fbeb77c810036dcac240570034a56a), [Commit](https://github.com/open-webui/open-webui/commit/1d1f60ab440b167b9c6ab8f4011b884caa99f27d)

> 🧊 **Quicker collection checks on Chroma.** Checking whether a collection exists now asks for that one collection instead of listing them all, which grew slower with every knowledge base and file. [Commit](https://github.com/open-webui/open-webui/commit/48ee357156fd7f567ea13eb5ddba0a25701c0351), [#27394](https://github.com/open-webui/open-webui/pull/27394)

> 👤 **Lighter user activity checks.** Checking whether someone is currently active now reads only that timestamp rather than their whole profile, including their profile image. [Commit](https://github.com/open-webui/open-webui/commit/c8f2e09fdcafc800c1e3af6da1cd6f2581cd9191), [#27224](https://github.com/open-webui/open-webui/pull/27224)

> 🌊 **Steadier long responses.** Building up a streamed reply no longer costs more work as it grows, so long answers keep pace instead of slowing down toward the end. [#27231](https://github.com/open-webui/open-webui/pull/27231), [#27359](https://github.com/open-webui/open-webui/pull/27359), [Commit](https://github.com/open-webui/open-webui/commit/ba556bd8f0517881cb250bb512631ddf8a0c82c3), [#27390](https://github.com/open-webui/open-webui/pull/27390)

> 🛰️ **Fewer Sentinel lookups.** Redis Sentinel deployments no longer ask which server is the primary and open a fresh connection before every single command, which had caused heavy connection churn and stalls under load. [Commit](https://github.com/open-webui/open-webui/commit/75a8a0046b5b2ebd9942b25035b346aa953f81cc), [#27213](https://github.com/open-webui/open-webui/pull/27213), [#27210](https://github.com/open-webui/open-webui/issues/27210)

> ⚡ **Lighter model lists.** Model lists no longer carry embedded profile images in their data, so they load faster. [Commit](https://github.com/open-webui/open-webui/commit/9281adc5647b7046e3ddcc53ac4b84be7f650221), [Commit](https://github.com/open-webui/open-webui/commit/f3a35507845e4a911c3d278d680a9989bb8d99ad)

> 🔛 **Functions can react to being switched on or off.** Two new events fire just before a function is enabled or disabled, and the function being enabled receives its own event even though it is not active yet, so it can run whatever setup or teardown it needs. [Commit](https://github.com/open-webui/open-webui/commit/94a60b04573acf6423e9c0519997b779f82e0560), [#26754](https://github.com/open-webui/open-webui/pull/26754), [#26748](https://github.com/open-webui/open-webui/discussions/26748)

> 🎗️ **Terminal single sign-on tokens.** The token forwarded to a terminal server for single sign-on is now taken from your own session on the server rather than from a header the browser supplied, so a caller can no longer send someone else's token in its place. [#26719](https://github.com/open-webui/open-webui/pull/26719)

> 🧫 **Files attached to a shared folder.** Adding files to a folder is now refused unless the folder's owner can read them, and a folder's files are checked against what its owner can still read before they are used as knowledge in chat, so a collaborator can no longer place files into someone else's folder or keep serving files the owner has since lost access to. [#27464](https://github.com/open-webui/open-webui/pull/27464), [Commit](https://github.com/open-webui/open-webui/commit/56183fcb17142088e2a34d1e35228f013749030c)

> 🧷 **Knowledge claimed by a direct connection.** Files listed as knowledge on a model supplied by the browser for a direct connection are now filtered against your own access before anything is retrieved, so a crafted request can no longer pull in documents you cannot otherwise open. [Commit](https://github.com/open-webui/open-webui/commit/305880f2e2aeb2dda2f4b2a18a20bdcd558f7134), [#26723](https://github.com/open-webui/open-webui/pull/26723)

> 🗨️ **Response text where it was missing.** Assistant replies are no longer stored without their text, so copying, exporting, searching and reusing a conversation return the reply instead of nothing. [Commit](https://github.com/open-webui/open-webui/commit/33cf3fbb7f017ab1b79dce5c5ca4d4e1c3092844), [#26799](https://github.com/open-webui/open-webui/pull/26799), [#26436](https://github.com/open-webui/open-webui/issues/26436)

> 🪫 **Terminal choice cleared on load.** Your selected terminal is no longer dropped while the list of terminals is still loading, so it survives a page refresh. [Commit](https://github.com/open-webui/open-webui/commit/9707d3a5c21d2fedada602f2cfd8a104cdc5e5d1), [Commit](https://github.com/open-webui/open-webui/commit/f59d86a10cb31e48d2dae0033081a09dbbaafc8c), [Commit](https://github.com/open-webui/open-webui/commit/2f2bf38e3481077597b5ad60f57685813e8d71b8), [#26775](https://github.com/open-webui/open-webui/pull/26775), [#26677](https://github.com/open-webui/open-webui/issues/26677)

> 💭 **Reasoning that arrives late or empty.** Reasoning sent by a provider after the answer has started is now shown in its proper place above the answer rather than appended after it, and reasoning notes carrying nothing no longer open an empty thinking block. [Commit](https://github.com/open-webui/open-webui/commit/051a1f6c41d1d37e5a12ce2068fc6f8488940591), [#26687](https://github.com/open-webui/open-webui/pull/26687), [#26645](https://github.com/open-webui/open-webui/issues/26645)

> 🛑 **Stopping an answer the moment it starts.** Each answer in a chat now carries its own task identifier from the first event onward, so stopping one immediately after sending no longer misses. [Commit](https://github.com/open-webui/open-webui/commit/aadab2f480a8c17a9265a244d262947da23ddc79)

> ⏸️ **Deleting while a reply is being written.** The delete control is now hidden on messages while a response is generating or a task is running, so a conversation can no longer be left with the finished reply detached from the messages before it. [Commit](https://github.com/open-webui/open-webui/commit/b4d13793a3af2d75aaf33fe9793cbbf278958940), [#26668](https://github.com/open-webui/open-webui/issues/26668)

> 🎁 **Feedback while a download is prepared.** Downloading a file or folder from the terminal now tells you it is being prepared, will not start the same archive twice if you click again, and reports a failure instead of quietly giving up or leaving a preview spinning. [#27421](https://github.com/open-webui/open-webui/pull/27421), [#27055](https://github.com/open-webui/open-webui/issues/27055)

> 📜 **Chats past the first sixty in a folder.** Folder listings now page through every chat instead of stopping at a fixed limit, so older chats no longer appear to vanish from a folder once it grows past sixty. [#26786](https://github.com/open-webui/open-webui/issues/26786), [Commit](https://github.com/open-webui/open-webui/commit/409fb39717be9ab7becd9e8c01801a08c5bae318)

> 🎛️ **Typing a top_k value.** The top_k box in advanced parameters now accepts whole numbers up to its limit and rejects anything else, instead of letting the slider and the box disagree over what is allowed. [Commit](https://github.com/open-webui/open-webui/commit/34920213619eb66467470105cbe3a275c812ccbc), [#26669](https://github.com/open-webui/open-webui/issues/26669)

> 🔦 **Chat search on PostgreSQL.** Searching your chats now finds matches in current conversations on PostgreSQL setups, instead of only matching chats still stored in the older format. [Commit](https://github.com/open-webui/open-webui/commit/cc9a44569ef08b64ff44d15607c43966f362ce75)

> 🔍 **Knowledge base file search.** Searching inside knowledge base files now returns matching lines with correct line numbers, and patterns that list alternatives separated by a pipe find matches instead of silently returning none. [#27249](https://github.com/open-webui/open-webui/pull/27249), [Commit](https://github.com/open-webui/open-webui/commit/e18e249d5da3d8fe701a885edc64341cc5dbf813), [Commit](https://github.com/open-webui/open-webui/commit/8d2fee5d4559d030b53575d377a0013e2c67b9fe), [#26795](https://github.com/open-webui/open-webui/pull/26795), [#26781](https://github.com/open-webui/open-webui/issues/26781), [#26744](https://github.com/open-webui/open-webui/issues/26744)

> 🪙 **Documents containing special tokens.** Splitting text by tokens no longer fails when the content contains reserved marker sequences, so those pages and files can be fetched and added to a knowledge base. [Commit](https://github.com/open-webui/open-webui/commit/33cf3fbb7f017ab1b79dce5c5ca4d4e1c3092844), [#27094](https://github.com/open-webui/open-webui/issues/27094)

> 🪃 **Backslashes in terminal proxy paths.** A request to the terminal proxy containing a backslash is now refused, closing a way to smuggle directory traversal past the path check to an upstream that treats it as a separator. [#27198](https://github.com/open-webui/open-webui/pull/27198)

> 🧱 **Internal addresses disguised as public ones.** A web address that hides an internal target inside an IPv6 address, through the mapped, 6to4, Teredo or NAT64 forms, is now recognised and refused like any other internal address. [Commit](https://github.com/open-webui/open-webui/commit/1717b493d83c86afa82aa8bc50139250852dd2f3)

> 🪤 **Tighter checks when a page is fetched.** Every request a fetched page makes is now checked against the address rules rather than only the page itself, each hop of a redirect is checked in turn, and background workers and socket connections the page tries to open are refused. [Commit](https://github.com/open-webui/open-webui/commit/bef63a2ae915571d50d2722a635e8bfa753d7877), [#27042](https://github.com/open-webui/open-webui/pull/27042), [#27008](https://github.com/open-webui/open-webui/pull/27008)

> 🧮 **Anthropic usage reporting.** Responses from the Anthropic-compatible API now report accurate input and output token counts, pass through cache and server tool figures where the provider gives them, and leave the input count out entirely rather than reporting zero when it is unknown. [Commit](https://github.com/open-webui/open-webui/commit/e8b59b2ef35ecb727fa760cd565d6da20c9e7e79), [Commit](https://github.com/open-webui/open-webui/commit/51ff386fd6461c07225d10a0de530019eebdd157), [Commit](https://github.com/open-webui/open-webui/commit/0576e8eeb5797a36b43eba5790a4e2a5dd8e5a4d), [Commit](https://github.com/open-webui/open-webui/commit/8e74cac8decc0a54137d7214e70c33b0dd52a99a), [Commit](https://github.com/open-webui/open-webui/commit/93a34bb25b32ae0b3a876fd3161c7778227b76bf), [Commit](https://github.com/open-webui/open-webui/commit/4c2d864b3f4c1ae6c4c9bd93aea078d4bf520463), [#26790](https://github.com/open-webui/open-webui/pull/26790), [#27293](https://github.com/open-webui/open-webui/pull/27293), [Docs:#1328](https://github.com/open-webui/docs/issues/1328)

> 🚏 **Stray terminal containers.** Terminal orchestrator connections that use a policy now send every request through that policy, so each person no longer ends up with a second unintended container alongside the intended one. [#26945](https://github.com/open-webui/open-webui/issues/26945), [Commit](https://github.com/open-webui/open-webui/commit/7088d245bb45fc69c0b22748563b9f3c6f0daa73)

> 🧹 **Orphaned sessions get cleaned up.** The instance that reaps sessions left behind by a crashed worker now keeps trying if another instance holds the job, rather than one instance giving up for good and leaving stale sessions to accumulate, and the lock it uses can no longer be released or renewed by an instance that does not hold it. [Commit](https://github.com/open-webui/open-webui/commit/bf35f64a7f14161933dfa608577a977d107b1569), [Commit](https://github.com/open-webui/open-webui/commit/846ba80a9d5e75837d3db37185e9a23b1e6bfe78)

> 🧊 **Redis cluster connections.** A deployment using Redis in cluster mode is no longer handed a connection built for a single server, or the reverse, when both point at the same address. [Commit](https://github.com/open-webui/open-webui/commit/fc4906c9e9df3fa42bb9073ac197383347caa853)

> 🛟 **Redis failover on timeouts.** A Redis connection that times out now retries against a freshly resolved primary instead of failing, so Sentinel setups recover from a failover rather than erroring out. [Commit](https://github.com/open-webui/open-webui/commit/75a8a0046b5b2ebd9942b25035b346aa953f81cc), [#27210](https://github.com/open-webui/open-webui/issues/27210)

> 🫥 **Temporary chats and channels write nothing.** Generating or editing an image and status updates in a temporary chat or a channel message no longer try to save themselves against a conversation that was never stored, and the task list tools are no longer offered there at all rather than being offered and then failing. [Commit](https://github.com/open-webui/open-webui/commit/d484a2a99e3a0c21fdcad007a50ebc412fffbb2e), [Commit](https://github.com/open-webui/open-webui/commit/d2936c880cfc8cb71bb5c235926048ae189bba25), [Commit](https://github.com/open-webui/open-webui/commit/b45c020f68a9499b66e598e854b17a3f232b6cf2), [Commit](https://github.com/open-webui/open-webui/commit/71c4da8c065491a96e41da3c9f0c663e5f759468), [#27432](https://github.com/open-webui/open-webui/issues/27432)

> 🎞️ **Artifacts panel reopening itself.** The artifacts panel now opens once when a finished block is detected, so closing it partway through a reply no longer sees it forced back open on every word that follows. [Commit](https://github.com/open-webui/open-webui/commit/4856afcef8251969f751ade5760cefea9577c051), [#27399](https://github.com/open-webui/open-webui/issues/27399)

> 🖼️ **External message images.** Images hosted on other sites and referenced in a message now display inline instead of being replaced with a placeholder. [Commit](https://github.com/open-webui/open-webui/commit/890bfd0d9771d1919ce24f04e11b6c96589fca5b)

> 〰️ **Text above a collapsible block.** A line written directly above a collapsible section is no longer turned into a large heading, and the section itself still renders as a collapsible widget rather than leaking its markup. [Commit](https://github.com/open-webui/open-webui/commit/7d77efe0f1cfa4782893ffde78419a96a95240f4), [#27148](https://github.com/open-webui/open-webui/pull/27148), [#27001](https://github.com/open-webui/open-webui/issues/27001)

> 🔣 **Chats containing unusual characters.** Broken character sequences are now cleaned out of text before it is stored, so a conversation that picked one up still saves and still opens instead of failing to load. [Commit](https://github.com/open-webui/open-webui/commit/43e7eefa959918baf9fbf867a12b5d721fd782af), [#27201](https://github.com/open-webui/open-webui/pull/27201), [#27081](https://github.com/open-webui/open-webui/issues/27081)

> 🪝 **Blocked webhook targets look like failures.** A webhook pointing at an address that is not publicly reachable is now skipped with a short warning, instead of an error and a full traceback that read like the server crashing on startup. [Commit](https://github.com/open-webui/open-webui/commit/0671b7aa2b59f5c6235bfa85d6aba54e2ba91353), [#26975](https://github.com/open-webui/open-webui/issues/26975)

> 🕵️ **Values printed in error logs.** A failure no longer prints the contents of nearby variables alongside its traceback, which could put keys and message content into the logs, and a new "LOGURU_DIAGNOSE" setting turns that detail back on for debugging. [Commit](https://github.com/open-webui/open-webui/commit/6aebfd88e938d1cd139068b5737a83a82ff393ed), [#26814](https://github.com/open-webui/open-webui/pull/26814)

> 🪵 **Empty audit exclusion list.** Clearing the list of paths excluded from audit logging no longer switches off auditing altogether, so requests are recorded as intended. [#27370](https://github.com/open-webui/open-webui/pull/27370), [Commit](https://github.com/open-webui/open-webui/commit/2ef6c76f5126ccdef5d1c814004920941275f45d)

> 👍 **Rating in feedback events.** Events sent when someone rates a response now carry the rating that was given, instead of reporting it as empty. [Commit](https://github.com/open-webui/open-webui/commit/300302d43259e119cd88247b3f246bea82b4dd8e), [#26840](https://github.com/open-webui/open-webui/issues/26840)

> 🗓️ **Schedules written by hand.** A recurrence rule is now read the same way whether it is written in upper or lower case, a start date in the rule is respected, second-by-second rules are understood, and a rule that cannot be supported is refused with a clear message instead of behaving unpredictably. [Commit](https://github.com/open-webui/open-webui/commit/c4ae8c86786fed521960466f6d8eef8af22c2946), [Commit](https://github.com/open-webui/open-webui/commit/2d928df30443516a9a3d6b71b0f31426a2362499), [#27470](https://github.com/open-webui/open-webui/pull/27470)

> 🛠️ **Admin settings moved into settings.** Admin settings and the analytics dashboard are no longer separate pages and now open alongside your personal settings in the settings window, under their own Admin section, with the old links redirecting there. [Commit](https://github.com/open-webui/open-webui/commit/c1460570b7e2897a3e648441a0206ad25e603b8c), [Commit](https://github.com/open-webui/open-webui/commit/3ce3c529365a3cd9e5631b14bfffead6baa2b1ed), [Commit](https://github.com/open-webui/open-webui/commit/667cba1a9561166941f59faf3bfa24038288b449)

> 🏷️ **Shorter titles without emojis.** Automatically generated titles for chats and notes are now two to four words and no longer include an emoji, and anyone who prefers the old style can restore it by editing the title generation prompt in admin settings. [Commit](https://github.com/open-webui/open-webui/commit/50d3c927bfed3b8dd94fd9f79bff258a84ecbd92), [Commit](https://github.com/open-webui/open-webui/commit/7a9928ef172b7c280c377c86cb52957e39340158)

> 📦 **Storage emulator no longer bundled.** The optional Google Cloud Storage emulator is no longer installed as part of the full package, so anyone who relied on it for local storage testing now needs to install "gcp-storage-emulator" themselves. [Commit](https://github.com/open-webui/open-webui/commit/30415c925a18b1ea1c3f2739bd944dd939f020cf)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-27-9-automation-and-scheduling-changes-in-v0-11-0|9 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-27-4-voice-and-audio-changes-in-v0-11-0|4 Voice and Audio changes in v0.11.0]] · Voice and Audio
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
- [[Changes/Open WebUI/2026-07-27-42-other-changes-in-v0-11-0|42 other changes in v0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-07-24 · OpenCode · [[Changes/OpenCode/2026-07-24-support-the-current-server-terminal-transport|Support the current server terminal transport]]
- Later: 2026-07-27 · OpenCode · [[Changes/OpenCode/2026-07-27-desktop-improved-compatibility-with-the-newer-client-api-across-directory-projec|Desktop Improved compatibility with the newer client API across directory, project…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-27-3aee42&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-27-62-developer-workflow-changes-in-v0-11-0.md%0ACard%20ID%3A%20open-webui-2026-07-27-3aee42%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->