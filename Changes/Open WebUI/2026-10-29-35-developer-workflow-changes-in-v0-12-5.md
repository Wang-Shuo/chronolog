---
card_id: open-webui-2026-10-29-4f0bd6
date: '2026-10-29'
description: "Open WebUI · 2026-10-29 · Developer Workflow: 35 changes in v0.12.5
  — \U0001F9ED **Analytics session explorer.** Administrators can now open a Sessions
  tab in Admin…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1321
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6c57463da5a9e0b76533c2accb5746247f722ee0c0a9a0aea5bb94780c16a835
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-29-4f0bd6
  comparison: ''
  date: '2026-10-29'
  description: 'Open WebUI — v0.12.5: 35 Developer Workflow changes'
  evidence:
  - quote: "\U0001F9ED **Analytics session explorer.** Administrators can now open
      a Sessions tab in Admin Analytics that lists each chat with its tokens, responses,
      errors and time span, filters them by search, model, token range or sub-agents,
      and shows a chat's saved replies and tool calls with their timing and outcome,
      as long as \"ENABLE_ADMIN_CHAT_ACCESS\" is on. [Commit](https://github.com/open-webui/open-webui/commit/7b303cf496f22d665ff1f1013a2308de0d74a7a4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F4D1 **Pages in notes.** Notes can now hold several pages and subpages,
      which you can add, rename, reorder, move under another page, download, link
      to and delete from the page tabs, and search results and the model now work
      with notes page by page. [Commit](https://github.com/open-webui/open-webui/commit/b34885efc639c10cbf06c35cd2d4ff6055e36b45)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F440 **Live presence in notes.** A note now shows who else has it
      open, and clicking a person jumps to the page and spot they are working on.
      [Commit](https://github.com/open-webui/open-webui/commit/e3ad014fb250c663a124ada0046c4017b85aabd6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F5BC️ **Generated images in terminals.** When a terminal is selected
      in a chat, generated and edited images are now also saved to its working folder,
      so the model can keep working on them with the terminal's tools. [Commit](https://github.com/open-webui/open-webui/commit/b420726ff1f04dff07a2877511b30ebe7b9887bb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F5C3️ **Models show chat files.** Models can now show a file attached
      in the chat or stored in an attached knowledge base right in the reply with
      the built-in display_file tool, which until now only worked for terminal files.
      [#32471](https://github.com/open-webui/open-webui/issues/32471), [Commit](https://github.com/open-webui/open-webui/commit/f2cdbbebe3cb40aab77516515198c7fa6c4818b7),
      [Commit](https://github.com/open-webui/open-webui/commit/ef29fb12f1f641bf1d83b434a37298846d211deb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: ⌨️ **Unassign single shortcuts.** Settings > Keyboard now shows a small
      x beside every assigned shortcut that unassigns only that one, so a shortcut
      such as Regenerate Response on Ctrl+R or Cmd+R can be switched off while all
      others keep working. [#33185](https://github.com/open-webui/open-webui/pull/33185),
      [#31463](https://github.com/open-webui/open-webui/discussions/31463), [Commit](https://github.com/open-webui/open-webui/commit/9fef07de3ae8c16b8f53e46b456c144bd739a8a2)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F9F2 **Embedding prefixes in settings.** Administrators can now
      set the query and content prefixes that some embedding models need under Admin
      Settings > Documents, where they could only be set with the \"RAG_EMBEDDING_QUERY_PREFIX\"
      and \"RAG_EMBEDDING_CONTENT_PREFIX\" environment variables. [Commit](https://github.com/open-webui/open-webui/commit/4a10c093ab1dc9d195c4bcd662c22aec97bba22c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: ⏱️ **Terminal start timeout.** Open WebUI now waits up to 60 seconds by
      default when it asks a terminal for its skills, AGENTS.md file or uploads, so
      a terminal that is still starting can answer, with "AIOHTTP_CLIENT_TIMEOUT_TERMINAL"
      to change the limit and a message naming the terminal when it still times out.
      [Commit](https://github.com/open-webui/open-webui/commit/ab133dba2183491d7c22229ae2b3b30cacf020d4)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F52D **Faster chat search.** Searching your chats, including from
      the Reference Chats menu and the model's chat search tool, no longer loads every
      matching chat in full, so results come back faster on large chat histories,
      and a result's message preview in the Reference Chats menu now loads when you
      hover it. [Commit](https://github.com/open-webui/open-webui/commit/44a9d499db851f7c6243ada8bfddb9d5b419f473)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F9FE **Mistral OCR model choice.** Administrators can now pick the
      Mistral OCR model and send extra request options through a Parameters field
      in Admin Settings > Documents or \"MISTRAL_OCR_PARAMS\", for example to stay
      on an older OCR model or to match what an Azure AI Foundry endpoint expects.
      [#33333](https://github.com/open-webui/open-webui/pull/33333), [#19707](https://github.com/open-webui/open-webui/issues/19707),
      [Commit](https://github.com/open-webui/open-webui/commit/f1f0a194aef3d029f8243f7e7ac553d492283c07)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F4E1 **Metrics skip health checks.** OpenTelemetry metrics now leave
      out requests whose URL matches \"OTEL_PYTHON_FASTAPI_EXCLUDED_URLS\" or \"OTEL_PYTHON_EXCLUDED_URLS\",
      so health checks and probes no longer fill the request metrics, the same way
      traces already skip them. [#33329](https://github.com/open-webui/open-webui/pull/33329),
      [#31609](https://github.com/open-webui/open-webui/issues/31609), [Commit](https://github.com/open-webui/open-webui/commit/76b7be67fce6375244e4b00f0fdda5fb896e056e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F50E **Search dialog filters restored.** The search dialog again
      understands and suggests the \"tag:\", \"folder:\", \"pinned:\", \"shared:\"
      and \"archived:\" filters, where adding one emptied the results and archived
      chats could not be found at all. [#33181](https://github.com/open-webui/open-webui/pull/33181),
      [#32518](https://github.com/open-webui/open-webui/issues/32518), [Commit](https://github.com/open-webui/open-webui/commit/ec83763f1373801e7d0ed2f39e0b53f58a75156c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F4CD **Search locations by type.** The Location filter in the search
      window now lists only folders for Chats and only channels for Messages, and
      switching the content type clears a location that no longer fits, where such
      a pick returned an empty list. [#33183](https://github.com/open-webui/open-webui/pull/33183),
      [#33182](https://github.com/open-webui/open-webui/issues/33182), [Commit](https://github.com/open-webui/open-webui/commit/0f28fa402354aa4f5526dbd238da1ec567582466)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F9EE **Inflated streamed token counts.** Token counts for a reply
      are no longer inflated when the provider reports its usage again on every streamed
      chunk, where every report was added up, so the usage shown for the reply and
      in Admin Analytics now matches the provider's final count. [#32052](https://github.com/open-webui/open-webui/issues/32052),
      [#29064](https://github.com/open-webui/open-webui/issues/29064), [#28528](https://github.com/open-webui/open-webui/issues/28528),
      [Commit](https://github.com/open-webui/open-webui/commit/7b303cf496f22d665ff1f1013a2308de0d74a7a4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F399️ **Note recordings kept.** A recording in a note now stays
      in the note when the connection drops while it is being transcribed, for example
      when a laptop goes to sleep. [#33240](https://github.com/open-webui/open-webui/issues/33240),
      [Commit](https://github.com/open-webui/open-webui/commit/3b8205505b871b92dd23e010b61f51a02d515a92)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F004 **IME typing with Backspace.** Pressing Backspace while composing
      text with a Japanese or other input method in the chat input no longer ends
      the composition or makes the text appear twice, which started in 0.12.4. [#33245](https://github.com/open-webui/open-webui/pull/33245),
      [#33223](https://github.com/open-webui/open-webui/issues/33223), [Commit](https://github.com/open-webui/open-webui/commit/a88fbc41a197f46ca148bf6dee16ad9ebafa2245)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001FA86 **Sub-agent partial output kept.** A foreground sub-agent that
      stops at the tool-call limit now hands the model its partial output along with
      the error, where everything it had written was lost, and the error now reads
      as a plain message in both foreground and background. [#33269](https://github.com/open-webui/open-webui/pull/33269),
      [#33267](https://github.com/open-webui/open-webui/issues/33267), [Commit](https://github.com/open-webui/open-webui/commit/e77204559bd92b43b7320ab128aac768e9be23db)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F503 **Cut-off replies stay finished.** A reply cut off by a server
      restart no longer goes back to the loading dots when the connection comes back
      later. [#33277](https://github.com/open-webui/open-webui/issues/33277), [Commit](https://github.com/open-webui/open-webui/commit/7b4d4b51f6d40587a6de94bc09cfd145f71dea2f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F422 **Slow chat loads.** Opening a chat on a slow connection or
      switching chats quickly now shows the chat you opened, where a slower earlier
      load could replace it with an old copy and the next message forked the chat.
      [#33180](https://github.com/open-webui/open-webui/issues/33180), [Commit](https://github.com/open-webui/open-webui/commit/193cf225f377ccc021b5128b80e5370e93895b2f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F441️ **Tool images with Vision off.** Models with Vision turned
      off now get a short \"[image]\" note in place of each image a tool returns,
      where the reply failed with an error and every later message in that chat failed
      the same way. [#33345](https://github.com/open-webui/open-webui/pull/33345),
      [#32720](https://github.com/open-webui/open-webui/issues/32720), [Commit](https://github.com/open-webui/open-webui/commit/63ca4237eb43d64911af9b4a0e3ab7501c25560f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: ✋ **Stop button on others' replies.** In a chat shared with Allow replies,
      the Stop button no longer shows on someone else's running reply, where it showed
      but did nothing. [#33343](https://github.com/open-webui/open-webui/issues/33343),
      [Commit](https://github.com/open-webui/open-webui/commit/d6610adaa9ffebaa4fb2058d1116debc4e47d5f4)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F50C **Tool server Headers reset.** Adding another connection in
      External Tool Servers now starts with empty Headers, where it kept the previous
      connection's Headers and saved them on the new one. [#33201](https://github.com/open-webui/open-webui/pull/33201),
      [#33200](https://github.com/open-webui/open-webui/issues/33200), [Commit](https://github.com/open-webui/open-webui/commit/8889e8d6affd487b9dae5df7f0c971fc30ae58b3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F9F0 **OpenAPI tools listed.** The Available Tools window in a chat
      now lists the tools of an OpenAPI tool server, where it said \"No tools found\".
      [#33205](https://github.com/open-webui/open-webui/pull/33205), [#33204](https://github.com/open-webui/open-webui/issues/33204),
      [Commit](https://github.com/open-webui/open-webui/commit/722f71f2cca9ad5cf7def62452eeddfea9248e2e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F5C2️ **Local knowledge filter.** Picking Local in the source filter
      on Workspace > Knowledge now lists knowledge bases made with Create, where it
      showed \"No knowledge found\". [#33199](https://github.com/open-webui/open-webui/pull/33199),
      [#33198](https://github.com/open-webui/open-webui/issues/33198), [Commit](https://github.com/open-webui/open-webui/commit/6635a45df49eef925fc2c4949c445d197a81e6e9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001FAA3 **Large S3 Vectors deletes.** Removing a file or knowledge
      base with more than 500 chunks from S3 Vectors now works, where the delete request
      went over the service's limit of 500 keys and failed. [Commit](https://github.com/open-webui/open-webui/commit/58536b65038dc7ff17d02dd78c60cc71ce110f92)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F509 **Kokoro.js without a GPU.** Kokoro.js (Browser) now runs on
      the CPU in browsers that offer WebGPU but have no GPU available, where its voices
      never finished loading and Read Aloud kept spinning without speaking. [#33233](https://github.com/open-webui/open-webui/pull/33233),
      [#33232](https://github.com/open-webui/open-webui/issues/33232), [Commit](https://github.com/open-webui/open-webui/commit/bafe181330dc8cb3c54afd78cc3e2901a448ea3f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F4CB **Shift paste in channels.** Holding Shift while pasting long
      text into a channel message or thread reply now keeps it as text when Paste
      Large Text as File is on, as it already did in chats. [#33190](https://github.com/open-webui/open-webui/pull/33190),
      [#33189](https://github.com/open-webui/open-webui/issues/33189), [Commit](https://github.com/open-webui/open-webui/commit/eb2bcba2154a27d76f1bad6deda78d1ff90ec2fc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F465 **Analytics model chats by group.** A model's Chats tab in
      Admin Analytics now follows the User group filter, where it listed every user's
      chats with that model. [#33207](https://github.com/open-webui/open-webui/pull/33207),
      [#33206](https://github.com/open-webui/open-webui/issues/33206), [Commit](https://github.com/open-webui/open-webui/commit/02821c50584193377da4e0320cf8a14652ab2327)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F648 **Hidden files in folder counts.** The item count under a folder
      in a chat's terminal file browser now leaves out hidden files while Show Hidden
      Files is off. [#33213](https://github.com/open-webui/open-webui/pull/33213),
      [#33212](https://github.com/open-webui/open-webui/issues/33212), [Commit](https://github.com/open-webui/open-webui/commit/4cb37dd539f94f2d80fae9f1448f317553430872)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F4CC **Pins kept in shared folders.** A member's chat now keeps
      its pin when the owner of a shared folder moves it to another folder inside
      that folder, where it dropped out of the member's Pinned list. [#33342](https://github.com/open-webui/open-webui/pull/33342),
      [#33341](https://github.com/open-webui/open-webui/issues/33341), [Commit](https://github.com/open-webui/open-webui/commit/226dca18cdd79cac04bc36888ea0f834762b90cc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F319 **Overnight calendar events.** A calendar event that ends after
      midnight, such as 8:00 PM to 1:00 AM, now keeps its end time on the next day,
      where saving dropped it and stored the event as ending at its start time. [#33290](https://github.com/open-webui/open-webui/pull/33290),
      [#33289](https://github.com/open-webui/open-webui/issues/33289), [Commit](https://github.com/open-webui/open-webui/commit/a8e8e7e792201346553c6e911c3f81306f23d60f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F5D3️ **Midnight calendar events.** A calendar event that ends at
      midnight now shows only on its own day in Month view, where it also showed on
      the next day. [#33292](https://github.com/open-webui/open-webui/pull/33292),
      [#33291](https://github.com/open-webui/open-webui/issues/33291), [Commit](https://github.com/open-webui/open-webui/commit/1b92d9848488dd2402686c2da25b16c6382c1520)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001FA9D **Old webhook removable.** A notification webhook carried over
      from before v0.11 now stays removed from Settings > Notifications, where it
      came right back after Remove. [#33295](https://github.com/open-webui/open-webui/pull/33295),
      [#33294](https://github.com/open-webui/open-webui/issues/33294), [Commit](https://github.com/open-webui/open-webui/commit/0ac55c8e7205aed414c1f265ca8e7047a772c08d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F514 **New default notification target.** A notification target
      added after removing the last one now becomes the default, where it never did.
      [#33284](https://github.com/open-webui/open-webui/pull/33284), [#33283](https://github.com/open-webui/open-webui/issues/33283),
      [Commit](https://github.com/open-webui/open-webui/commit/77398eba3126eb6b3614e8bc868a268aff668e44)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F4CE **Note attachments in pages.** Files attached to a note now
      sit inside the page where they were added, and the attached files of existing
      notes move to the end of the note's first page. [Commit](https://github.com/open-webui/open-webui/commit/b34885efc639c10cbf06c35cd2d4ff6055e36b45)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 35-developer-workflow-changes-in-v0-12-5
  source_release: open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e
  source_type: github_releases
  theme: developer-workflow
  title: 35 Developer Workflow changes in v0.12.5
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-27-3-developer-workflow-changes-in-rust-v0-165-0|3
  Developer Workflow changes in rust-v0.165.0]]'
- '[[Changes/OpenHands/2026-10-27-chore-bump-shell-quote-and-dompurify-dependencies-by-devinvinson-in-https-github|chore:
  bump shell-quote and DOMPurify dependencies]]'
- '[[Changes/Codex CLI/2026-10-29-10-developer-workflow-changes-in-rust-v0-166-0|10
  Developer Workflow changes in rust-v0.166.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e|open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e]]'
source_type: github_releases
theme: developer-workflow
title: 35 Developer Workflow changes in v0.12.5
type: change
---

<!-- chronolog:begin region="header" -->
# 35 Developer Workflow changes in v0.12.5

**Open WebUI** · 2026-10-29 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.5) · from [[Releases/Open WebUI/open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e|v0.12.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧭 **Analytics session explorer.** Administrators can now open a Sessions tab in Admin Analytics that lists each chat with its tokens, responses, errors and time span, filters them by search, model, token range or sub-agents, and shows a chat's saved replies and tool calls with their timing and outcome, as long as "ENABLE_ADMIN_CHAT_ACCESS" is on. [Commit](https://github.com/open-webui/open-webui/commit/7b303cf496f22d665ff1f1013a2308de0d74a7a4)

> 📑 **Pages in notes.** Notes can now hold several pages and subpages, which you can add, rename, reorder, move under another page, download, link to and delete from the page tabs, and search results and the model now work with notes page by page. [Commit](https://github.com/open-webui/open-webui/commit/b34885efc639c10cbf06c35cd2d4ff6055e36b45)

> 👀 **Live presence in notes.** A note now shows who else has it open, and clicking a person jumps to the page and spot they are working on. [Commit](https://github.com/open-webui/open-webui/commit/e3ad014fb250c663a124ada0046c4017b85aabd6)

> 🖼️ **Generated images in terminals.** When a terminal is selected in a chat, generated and edited images are now also saved to its working folder, so the model can keep working on them with the terminal's tools. [Commit](https://github.com/open-webui/open-webui/commit/b420726ff1f04dff07a2877511b30ebe7b9887bb)

> 🗃️ **Models show chat files.** Models can now show a file attached in the chat or stored in an attached knowledge base right in the reply with the built-in display_file tool, which until now only worked for terminal files. [#32471](https://github.com/open-webui/open-webui/issues/32471), [Commit](https://github.com/open-webui/open-webui/commit/f2cdbbebe3cb40aab77516515198c7fa6c4818b7), [Commit](https://github.com/open-webui/open-webui/commit/ef29fb12f1f641bf1d83b434a37298846d211deb)

> ⌨️ **Unassign single shortcuts.** Settings > Keyboard now shows a small x beside every assigned shortcut that unassigns only that one, so a shortcut such as Regenerate Response on Ctrl+R or Cmd+R can be switched off while all others keep working. [#33185](https://github.com/open-webui/open-webui/pull/33185), [#31463](https://github.com/open-webui/open-webui/discussions/31463), [Commit](https://github.com/open-webui/open-webui/commit/9fef07de3ae8c16b8f53e46b456c144bd739a8a2)

> 🧲 **Embedding prefixes in settings.** Administrators can now set the query and content prefixes that some embedding models need under Admin Settings > Documents, where they could only be set with the "RAG_EMBEDDING_QUERY_PREFIX" and "RAG_EMBEDDING_CONTENT_PREFIX" environment variables. [Commit](https://github.com/open-webui/open-webui/commit/4a10c093ab1dc9d195c4bcd662c22aec97bba22c)

> ⏱️ **Terminal start timeout.** Open WebUI now waits up to 60 seconds by default when it asks a terminal for its skills, AGENTS.md file or uploads, so a terminal that is still starting can answer, with "AIOHTTP_CLIENT_TIMEOUT_TERMINAL" to change the limit and a message naming the terminal when it still times out. [Commit](https://github.com/open-webui/open-webui/commit/ab133dba2183491d7c22229ae2b3b30cacf020d4)

> 🔭 **Faster chat search.** Searching your chats, including from the Reference Chats menu and the model's chat search tool, no longer loads every matching chat in full, so results come back faster on large chat histories, and a result's message preview in the Reference Chats menu now loads when you hover it. [Commit](https://github.com/open-webui/open-webui/commit/44a9d499db851f7c6243ada8bfddb9d5b419f473)

> 🧾 **Mistral OCR model choice.** Administrators can now pick the Mistral OCR model and send extra request options through a Parameters field in Admin Settings > Documents or "MISTRAL_OCR_PARAMS", for example to stay on an older OCR model or to match what an Azure AI Foundry endpoint expects. [#33333](https://github.com/open-webui/open-webui/pull/33333), [#19707](https://github.com/open-webui/open-webui/issues/19707), [Commit](https://github.com/open-webui/open-webui/commit/f1f0a194aef3d029f8243f7e7ac553d492283c07)

> 📡 **Metrics skip health checks.** OpenTelemetry metrics now leave out requests whose URL matches "OTEL_PYTHON_FASTAPI_EXCLUDED_URLS" or "OTEL_PYTHON_EXCLUDED_URLS", so health checks and probes no longer fill the request metrics, the same way traces already skip them. [#33329](https://github.com/open-webui/open-webui/pull/33329), [#31609](https://github.com/open-webui/open-webui/issues/31609), [Commit](https://github.com/open-webui/open-webui/commit/76b7be67fce6375244e4b00f0fdda5fb896e056e)

> 🔎 **Search dialog filters restored.** The search dialog again understands and suggests the "tag:", "folder:", "pinned:", "shared:" and "archived:" filters, where adding one emptied the results and archived chats could not be found at all. [#33181](https://github.com/open-webui/open-webui/pull/33181), [#32518](https://github.com/open-webui/open-webui/issues/32518), [Commit](https://github.com/open-webui/open-webui/commit/ec83763f1373801e7d0ed2f39e0b53f58a75156c)

> 📍 **Search locations by type.** The Location filter in the search window now lists only folders for Chats and only channels for Messages, and switching the content type clears a location that no longer fits, where such a pick returned an empty list. [#33183](https://github.com/open-webui/open-webui/pull/33183), [#33182](https://github.com/open-webui/open-webui/issues/33182), [Commit](https://github.com/open-webui/open-webui/commit/0f28fa402354aa4f5526dbd238da1ec567582466)

> 🧮 **Inflated streamed token counts.** Token counts for a reply are no longer inflated when the provider reports its usage again on every streamed chunk, where every report was added up, so the usage shown for the reply and in Admin Analytics now matches the provider's final count. [#32052](https://github.com/open-webui/open-webui/issues/32052), [#29064](https://github.com/open-webui/open-webui/issues/29064), [#28528](https://github.com/open-webui/open-webui/issues/28528), [Commit](https://github.com/open-webui/open-webui/commit/7b303cf496f22d665ff1f1013a2308de0d74a7a4)

> 🎙️ **Note recordings kept.** A recording in a note now stays in the note when the connection drops while it is being transcribed, for example when a laptop goes to sleep. [#33240](https://github.com/open-webui/open-webui/issues/33240), [Commit](https://github.com/open-webui/open-webui/commit/3b8205505b871b92dd23e010b61f51a02d515a92)

> 🀄 **IME typing with Backspace.** Pressing Backspace while composing text with a Japanese or other input method in the chat input no longer ends the composition or makes the text appear twice, which started in 0.12.4. [#33245](https://github.com/open-webui/open-webui/pull/33245), [#33223](https://github.com/open-webui/open-webui/issues/33223), [Commit](https://github.com/open-webui/open-webui/commit/a88fbc41a197f46ca148bf6dee16ad9ebafa2245)

> 🪆 **Sub-agent partial output kept.** A foreground sub-agent that stops at the tool-call limit now hands the model its partial output along with the error, where everything it had written was lost, and the error now reads as a plain message in both foreground and background. [#33269](https://github.com/open-webui/open-webui/pull/33269), [#33267](https://github.com/open-webui/open-webui/issues/33267), [Commit](https://github.com/open-webui/open-webui/commit/e77204559bd92b43b7320ab128aac768e9be23db)

> 🔃 **Cut-off replies stay finished.** A reply cut off by a server restart no longer goes back to the loading dots when the connection comes back later. [#33277](https://github.com/open-webui/open-webui/issues/33277), [Commit](https://github.com/open-webui/open-webui/commit/7b4d4b51f6d40587a6de94bc09cfd145f71dea2f)

> 🐢 **Slow chat loads.** Opening a chat on a slow connection or switching chats quickly now shows the chat you opened, where a slower earlier load could replace it with an old copy and the next message forked the chat. [#33180](https://github.com/open-webui/open-webui/issues/33180), [Commit](https://github.com/open-webui/open-webui/commit/193cf225f377ccc021b5128b80e5370e93895b2f)

> 👁️ **Tool images with Vision off.** Models with Vision turned off now get a short "[image]" note in place of each image a tool returns, where the reply failed with an error and every later message in that chat failed the same way. [#33345](https://github.com/open-webui/open-webui/pull/33345), [#32720](https://github.com/open-webui/open-webui/issues/32720), [Commit](https://github.com/open-webui/open-webui/commit/63ca4237eb43d64911af9b4a0e3ab7501c25560f)

> ✋ **Stop button on others' replies.** In a chat shared with Allow replies, the Stop button no longer shows on someone else's running reply, where it showed but did nothing. [#33343](https://github.com/open-webui/open-webui/issues/33343), [Commit](https://github.com/open-webui/open-webui/commit/d6610adaa9ffebaa4fb2058d1116debc4e47d5f4)

> 🔌 **Tool server Headers reset.** Adding another connection in External Tool Servers now starts with empty Headers, where it kept the previous connection's Headers and saved them on the new one. [#33201](https://github.com/open-webui/open-webui/pull/33201), [#33200](https://github.com/open-webui/open-webui/issues/33200), [Commit](https://github.com/open-webui/open-webui/commit/8889e8d6affd487b9dae5df7f0c971fc30ae58b3)

> 🧰 **OpenAPI tools listed.** The Available Tools window in a chat now lists the tools of an OpenAPI tool server, where it said "No tools found". [#33205](https://github.com/open-webui/open-webui/pull/33205), [#33204](https://github.com/open-webui/open-webui/issues/33204), [Commit](https://github.com/open-webui/open-webui/commit/722f71f2cca9ad5cf7def62452eeddfea9248e2e)

> 🗂️ **Local knowledge filter.** Picking Local in the source filter on Workspace > Knowledge now lists knowledge bases made with Create, where it showed "No knowledge found". [#33199](https://github.com/open-webui/open-webui/pull/33199), [#33198](https://github.com/open-webui/open-webui/issues/33198), [Commit](https://github.com/open-webui/open-webui/commit/6635a45df49eef925fc2c4949c445d197a81e6e9)

> 🪣 **Large S3 Vectors deletes.** Removing a file or knowledge base with more than 500 chunks from S3 Vectors now works, where the delete request went over the service's limit of 500 keys and failed. [Commit](https://github.com/open-webui/open-webui/commit/58536b65038dc7ff17d02dd78c60cc71ce110f92)

> 🔉 **Kokoro.js without a GPU.** Kokoro.js (Browser) now runs on the CPU in browsers that offer WebGPU but have no GPU available, where its voices never finished loading and Read Aloud kept spinning without speaking. [#33233](https://github.com/open-webui/open-webui/pull/33233), [#33232](https://github.com/open-webui/open-webui/issues/33232), [Commit](https://github.com/open-webui/open-webui/commit/bafe181330dc8cb3c54afd78cc3e2901a448ea3f)

> 📋 **Shift paste in channels.** Holding Shift while pasting long text into a channel message or thread reply now keeps it as text when Paste Large Text as File is on, as it already did in chats. [#33190](https://github.com/open-webui/open-webui/pull/33190), [#33189](https://github.com/open-webui/open-webui/issues/33189), [Commit](https://github.com/open-webui/open-webui/commit/eb2bcba2154a27d76f1bad6deda78d1ff90ec2fc)

> 👥 **Analytics model chats by group.** A model's Chats tab in Admin Analytics now follows the User group filter, where it listed every user's chats with that model. [#33207](https://github.com/open-webui/open-webui/pull/33207), [#33206](https://github.com/open-webui/open-webui/issues/33206), [Commit](https://github.com/open-webui/open-webui/commit/02821c50584193377da4e0320cf8a14652ab2327)

> 🙈 **Hidden files in folder counts.** The item count under a folder in a chat's terminal file browser now leaves out hidden files while Show Hidden Files is off. [#33213](https://github.com/open-webui/open-webui/pull/33213), [#33212](https://github.com/open-webui/open-webui/issues/33212), [Commit](https://github.com/open-webui/open-webui/commit/4cb37dd539f94f2d80fae9f1448f317553430872)

> 📌 **Pins kept in shared folders.** A member's chat now keeps its pin when the owner of a shared folder moves it to another folder inside that folder, where it dropped out of the member's Pinned list. [#33342](https://github.com/open-webui/open-webui/pull/33342), [#33341](https://github.com/open-webui/open-webui/issues/33341), [Commit](https://github.com/open-webui/open-webui/commit/226dca18cdd79cac04bc36888ea0f834762b90cc)

> 🌙 **Overnight calendar events.** A calendar event that ends after midnight, such as 8:00 PM to 1:00 AM, now keeps its end time on the next day, where saving dropped it and stored the event as ending at its start time. [#33290](https://github.com/open-webui/open-webui/pull/33290), [#33289](https://github.com/open-webui/open-webui/issues/33289), [Commit](https://github.com/open-webui/open-webui/commit/a8e8e7e792201346553c6e911c3f81306f23d60f)

> 🗓️ **Midnight calendar events.** A calendar event that ends at midnight now shows only on its own day in Month view, where it also showed on the next day. [#33292](https://github.com/open-webui/open-webui/pull/33292), [#33291](https://github.com/open-webui/open-webui/issues/33291), [Commit](https://github.com/open-webui/open-webui/commit/1b92d9848488dd2402686c2da25b16c6382c1520)

> 🪝 **Old webhook removable.** A notification webhook carried over from before v0.11 now stays removed from Settings > Notifications, where it came right back after Remove. [#33295](https://github.com/open-webui/open-webui/pull/33295), [#33294](https://github.com/open-webui/open-webui/issues/33294), [Commit](https://github.com/open-webui/open-webui/commit/0ac55c8e7205aed414c1f265ca8e7047a772c08d)

> 🔔 **New default notification target.** A notification target added after removing the last one now becomes the default, where it never did. [#33284](https://github.com/open-webui/open-webui/pull/33284), [#33283](https://github.com/open-webui/open-webui/issues/33283), [Commit](https://github.com/open-webui/open-webui/commit/77398eba3126eb6b3614e8bc868a268aff668e44)

> 📎 **Note attachments in pages.** Files attached to a note now sit inside the page where they were added, and the attached files of existing notes move to the end of the note's first page. [Commit](https://github.com/open-webui/open-webui/commit/b34885efc639c10cbf06c35cd2d4ff6055e36b45)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-29-improved-ui-accessibility-screen-reader-and-keyboard-users-can-now-move-through|♿ Improved UI accessibility. Screen reader and keyboard users can now move…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-10-29-provider-details-for-models-administrators-editing-a-model-now-see-a-provider-de|📇 Provider details for models. Administrators editing a model now see a Provider…]] · Context Window
- [[Changes/Open WebUI/2026-10-29-2-memory-and-personalization-changes-in-v0-12-5|2 Memory and Personalization changes in v0.12.5]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-29-2-automation-and-scheduling-changes-in-v0-12-5|2 Automation and Scheduling changes in v0.12.5]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-29-photos-for-sub-agents-models-can-now-hand-a-photo-attached-in-the-chat-to-a-sub|🤖 Photos for sub-agents. Models can now hand a photo attached in the chat…]] · Agent Mode
- [[Changes/Open WebUI/2026-10-29-knowledge-base-api-responses-trimmed-adding-updating-or-removing-knowledge-base|📃 Knowledge base API responses trimmed. Adding, updating or removing knowledge…]] · Collaboration
- [[Changes/Open WebUI/2026-10-29-2-reliability-and-performance-changes-in-v0-12-5|2 Reliability and Performance changes in v0.12.5]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-29-7-model-support-changes-in-v0-12-5|7 Model Support changes in v0.12.5]] · Model Support
- [[Changes/Open WebUI/2026-10-29-admins-manage-user-api-keys-administrators-can-now-rotate-or-delete-a-user-s-api|🗝️ Admins manage user API keys. Administrators can now rotate or delete a user's…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-29-2-image-generation-changes-in-v0-12-5|2 Image Generation changes in v0.12.5]] · Image Generation
- [[Changes/Open WebUI/2026-10-29-2-files-and-data-changes-in-v0-12-5|2 Files and Data changes in v0.12.5]] · Files and Data
- [[Changes/Open WebUI/2026-10-29-2-apps-and-integrations-changes-in-v0-12-5|2 Apps and Integrations changes in v0.12.5]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-29-security-advisory-this-release-contains-security-fixes-we-strongly-recommend-upd|🛡️ Security Advisory: This release contains security fixes]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-29-2-interface-experience-changes-in-v0-12-5|2 Interface Experience changes in v0.12.5]] · Interface Experience
- [[Changes/Open WebUI/2026-10-29-read-aloud-with-kokoro-js-read-aloud-now-speaks-with-the-chosen-kokoro-voice-whe|🔊 Read Aloud with Kokoro.js. Read Aloud now speaks with the chosen Kokoro voice…]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-29-6-editor-experience-changes-in-v0-12-5|6 Editor Experience changes in v0.12.5]] · Editor Experience
- [[Changes/Open WebUI/2026-10-29-translation-updates-translations-for-portuguese-brazil-catalan-italian-azerbaija|🌐 Translation updates. Translations for Portuguese (Brazil), Catalan, Italian…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-10-29 · Codex CLI · [[Changes/Codex CLI/2026-10-29-10-developer-workflow-changes-in-rust-v0-166-0|10 Developer Workflow changes in rust-v0.166.0]]
- Later: 2026-10-30 · Claude Code · [[Changes/Claude Code/2026-10-30-4-developer-workflow-changes-in-v2-1-314|4 Developer Workflow changes in v2.1.314]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-29-4f0bd6&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-29-35-developer-workflow-changes-in-v0-12-5.md%0ACard%20ID%3A%20open-webui-2026-10-29-4f0bd6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->