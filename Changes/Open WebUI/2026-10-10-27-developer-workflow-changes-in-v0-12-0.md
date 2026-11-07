---
card_id: open-webui-2026-10-10-3a0531
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Developer Workflow: 27 changes in v0.12.0
  — \U0001F531 **Fork shared chats.** Shared chat links and chats you can only read,
  such as ones in a…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2951
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c97d0206ebd5731eb0667c6f2c310d9c68f01fdbbe59ab38f60681b07b419de0
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-3a0531
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 27 Developer Workflow changes'
  evidence:
  - quote: "\U0001F531 **Fork shared chats.** Shared chat links and chats you can
      only read, such as ones in a folder shared with you, now have a fork action
      on each finished reply, which makes your own copy of the conversation up to
      that message; a fork from a share link holds only what was shared, and a fork
      of someone else's chat leaves out their folder, pin and chat variables. [Commit](https://github.com/open-webui/open-webui/commit/5de5bf235b1dc7a6f139ef5d66d4339c6de973af),
      [Commit](https://github.com/open-webui/open-webui/commit/f0233e1e3a1c19b1771f67721b6ebc59db4a36aa),
      [Commit](https://github.com/open-webui/open-webui/commit/930f8c3640aa3c8bd7eee2becee85f93a668cc29)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F510 **Access from the list.** The menu of each item in the Models,
      Knowledge, Prompts, Skills, Tools and Notes lists now has an Access entry, so
      who can use an item can be changed without opening it. [Commit](https://github.com/open-webui/open-webui/commit/b3ce7de8d3ab59f99f0006775dc3158ea079deda),
      [Commit](https://github.com/open-webui/open-webui/commit/d4f01d7344fdec082c956b7b0c9c650a2e63485b),
      [Commit](https://github.com/open-webui/open-webui/commit/784b72f19ef2ebf894480ab5e303bc995d3d4b59)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4EC **Message queue in channels.** Messages sent in a channel or
      thread while an earlier one is still sending or a file is still uploading now
      wait in a queue above the message box, where each can be sent right away, edited
      or removed, and they go out in order once their files are ready, where a message
      sent during an upload went out with a broken attachment. [Commit](https://github.com/open-webui/open-webui/commit/8a4547104c4f88c02b607ad7b6849dc22f377c28),
      [#31587](https://github.com/open-webui/open-webui/issues/31587)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FAA3 **S3 file storage on the slim image.** The slim image can now
      keep files in an S3 bucket with \"STORAGE_PROVIDER\" set to s3, where it only
      supported local storage; Google Cloud and Azure storage still need the standard
      image. [Commit](https://github.com/open-webui/open-webui/commit/425da8b6cc14144895c6eba19a70cf5c8881d3cf)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FA9E **Cloning chats you can only read.** A chat you open read only,
      such as one in a folder shared with you, now shows a Clone Chat button that
      copies it into your own chats from the message you are viewing, for anyone allowed
      to import chats. [Commit](https://github.com/open-webui/open-webui/commit/c6dd9a451abef12e93e19624a64cfb8a9a1f6465)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F516 **Build shown next to the version.** The version in Settings
      shows \"dev\" and the commit for development builds and the commit for other
      non-release builds, and update checks and the update notification now only run
      on release builds. [Commit](https://github.com/open-webui/open-webui/commit/51f0e01258b92c77952d4534bb8ce8c618b2700c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F319 **Local time and last seen on profile cards.** The profile
      card that opens on a person's name in channels or on an @mention now shows their
      local time and when they were last active, and it reloads each time it opens
      so the status stays current. [Commit](https://github.com/open-webui/open-webui/commit/538f9c9090dab742b4d8e3a1b3a058956ea8f39b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4A1 **Custom parameter suggestions.** Custom parameter fields now
      suggest common parameter names such as reasoning_effort, service_tier, num_ctx
      or response_format as you type, along with typical values for many of them,
      and a new row starts empty instead of with a placeholder name. [Commit](https://github.com/open-webui/open-webui/commit/10fdca6e36fd616d611cadbf95aee956eb823ca2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F39B️ **Tool approval mode no longer restored from drafts.** Restoring
      a saved message draft no longer switches the chat's tool approval mode, which
      could save settings and approve tools without asking. [Commit](https://github.com/open-webui/open-webui/commit/332237662f446f8264cd4db10a1b4513ba5fb76b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6C2 **Forwarded headers trust for open-webui serve.** Starting
      Open WebUI with \"open-webui serve\" or \"open-webui dev\" now honors \"FORWARDED_ALLOW_IPS\",
      where it trusted forwarded headers from every connection regardless of the setting.
      [Commit](https://github.com/open-webui/open-webui/commit/24e30d1cbdaab624dfe20f479f805e6791cf0226)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F575️ **Shared chats keep the owner's settings private.** Opening
      a chat shared with you, by link or through a shared folder, no longer hands
      you the owner's chat settings such as the system prompt and other parameters,
      chosen tools, filters and tool servers, filled-in chat variables or message
      details, and cloning a shared chat no longer copies the owner's chat variables
      or files the clone under the owner's folder. [Commit](https://github.com/open-webui/open-webui/commit/de73bb830aeb150bc5bb4707566d3969f70408b0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6C3 **Administrators read other users' chats without writing to
      them.** With \"ENABLE_ADMIN_CHAT_ACCESS\" on, administrators can now only read
      other users' chats, where they could also send messages into them, stop their
      replies or answer their tool approvals through direct API requests even though
      the chat page only showed them read only. [Commit](https://github.com/open-webui/open-webui/commit/6cfd6987e5b220040c2e476105779dcc10d3d14b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4BB **Skills from personal terminals.** Skills and the AGENTS.md
      instructions file from a terminal you added in your own settings are now read
      through your browser, so they reach the model even when only your browser can
      reach that terminal, such as one running on your own machine. [Commit](https://github.com/open-webui/open-webui/commit/7ad0ae46873511723f59c7f78bfd59f7c3982e1f),
      [#30410](https://github.com/open-webui/open-webui/issues/30410)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FA86 **Sub-agents get personal tools.** Sub-agents and chats resuming
      after a tool approval now get the same personal tool servers, such as Open Terminal,
      as the main model, where they received none of them. [#31424](https://github.com/open-webui/open-webui/pull/31424),
      [#29893](https://github.com/open-webui/open-webui/issues/29893)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ⏩ **Send now on queued messages.** Clicking Send now on one queued message
      sends only that message, where it could send the whole queue at once and leave
      two replies mixed together in the chat until a reload. [Commit](https://github.com/open-webui/open-webui/commit/aea7d34f456e5a6621c7daa6e74a586c65488b45),
      [#30027](https://github.com/open-webui/open-webui/issues/30027)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4B2 **Clipboard variable keeps dollar signs.** The clipboard variable
      in prompts now pastes text exactly as copied, where a pair of dollar signs turned
      into one and broke shell commands and math formulas. [#31364](https://github.com/open-webui/open-webui/pull/31364),
      [#31363](https://github.com/open-webui/open-webui/issues/31363)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F446 **Clicking outside menus.** Clicking outside the model selector
      or another open menu now only closes it, where the click also went through to
      whatever was underneath, such as a suggested prompt. [Commit](https://github.com/open-webui/open-webui/commit/8fc416ee78bd8264f7a716f147d4000c466ae646),
      [#29878](https://github.com/open-webui/open-webui/issues/29878)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FAA7 **Chat title with title generation off.** With title generation
      turned off, a new chat now shows its first message as the title in the header
      and browser tab right away, where it showed \"New Chat\" until a reload and
      a note's chat panel showed the whole model reply as its title; a title that
      arrives before the new chat has finished opening is no longer dropped either.
      [#31355](https://github.com/open-webui/open-webui/pull/31355), [#31348](https://github.com/open-webui/open-webui/issues/31348),
      [Commit](https://github.com/open-webui/open-webui/commit/82b51813721d171f0e347c9348be1042f9b010e8),
      [#31492](https://github.com/open-webui/open-webui/issues/31492)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4D1 **Copy Last Code Block with Artifacts open.** The Copy Last
      Code Block shortcut now copies the last code block in the chat, where it copied
      the Artifacts pane's full HTML whenever the pane was open. [#31613](https://github.com/open-webui/open-webui/pull/31613),
      [#31476](https://github.com/open-webui/open-webui/issues/31476)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ♿ **Sort order for screen readers in the user list.** The column headings
      of the admin user list now tell screen readers the current sort order after
      it changes, where they kept announcing the initial one. [Commit](https://github.com/open-webui/open-webui/commit/dc713a68a4ba0e1691892d8f53ebe1e9a877721c),
      [#31581](https://github.com/open-webui/open-webui/issues/31581)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FAC2 **Access grants of deleted groups.** Deleting a group now also
      removes its access grants, and the Access dialog lists grants left behind by
      groups deleted earlier under their ID so they can be removed, where they were
      hidden from the list but saved again, leaving the item marked Shared with no
      way to undo it. [Commit](https://github.com/open-webui/open-webui/commit/dd576bade3449057803248450ac453b29e6a60a5),
      [#31923](https://github.com/open-webui/open-webui/issues/31923)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ⏭️ **Chats open at their latest reply.** Opening a chat whose saved position
      points to an earlier message on the current branch now moves to the newest reply
      on that branch, where only compacted chats were moved forward, and broken or
      stale message links are skipped while finding it. [Commit](https://github.com/open-webui/open-webui/commit/d8659c237c7819d114a5d70db25ec6aed86b9bbf),
      [#27618](https://github.com/open-webui/open-webui/issues/27618)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4C2 **File browser stays in your folder.** When the agent runs
      a command in the terminal, the file browser panel now stays in the folder you
      picked and keeps the open file in view, where it jumped back to the top folder
      after every command, so the next command also ran there. [#31878](https://github.com/open-webui/open-webui/pull/31878),
      [#30051](https://github.com/open-webui/open-webui/issues/30051)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5C4️ **Fresh PostgreSQL installs with a custom schema.** With \"DATABASE_SCHEMA\"
      set, a fresh PostgreSQL install now creates its tables in that schema and starts,
      where the migrations created them in the public schema and startup failed with
      a \"relation does not exist\" error; a schema that does not exist, or one that
      already holds tables without migration history, now stops startup with a clear
      message instead. [Commit](https://github.com/open-webui/open-webui/commit/65f44053d20c9a70c6edb9d59f965c09754c29dd),
      [#31526](https://github.com/open-webui/open-webui/issues/31526)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FAA2 **Plain web addresses in chat.** Web addresses written without
      link text now show \"&\" instead of \"&amp;\", and addresses written in angle
      brackets open the address as written, where they pointed to a different address
      with the wrong parameters. [Commit](https://github.com/open-webui/open-webui/commit/652d0cff073632f8d4adeaf2b994a786fb8a317b),
      [#31902](https://github.com/open-webui/open-webui/issues/31902)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5D3️ **Calendar days from another month.** Clicking a day of the
      previous or next month in the calendar now also loads that month's events, where
      the view switched months and stayed empty. [Commit](https://github.com/open-webui/open-webui/commit/34abd6e121b8fee25936d312752e1c6da16f4ae9),
      [#30972](https://github.com/open-webui/open-webui/issues/30972)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4E5 **Downloading files whose upload is gone.** Downloading a file
      whose original upload is missing from storage now gives its extracted text as
      a text file, where the download failed with not found. [Commit](https://github.com/open-webui/open-webui/commit/33dd7dd224d4fc4031185a4dd589242681f24af7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 27-developer-workflow-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: developer-workflow
  title: 27 Developer Workflow changes in v0.12.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-08-12-developer-workflow-changes-in-rust-v0-162-0|12
  Developer Workflow changes in rust-v0.162.0]]'
- '[[Changes/OpenClaw/2026-10-08-3-developer-workflow-changes-in-v2026-9-9|3 Developer
  Workflow changes in v2026.9.9]]'
- '[[Changes/Claude Code/2026-10-09-3-developer-workflow-changes-in-v2-1-296|3 Developer
  Workflow changes in v2.1.296]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: developer-workflow
title: 27 Developer Workflow changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 27 Developer Workflow changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔱 **Fork shared chats.** Shared chat links and chats you can only read, such as ones in a folder shared with you, now have a fork action on each finished reply, which makes your own copy of the conversation up to that message; a fork from a share link holds only what was shared, and a fork of someone else's chat leaves out their folder, pin and chat variables. [Commit](https://github.com/open-webui/open-webui/commit/5de5bf235b1dc7a6f139ef5d66d4339c6de973af), [Commit](https://github.com/open-webui/open-webui/commit/f0233e1e3a1c19b1771f67721b6ebc59db4a36aa), [Commit](https://github.com/open-webui/open-webui/commit/930f8c3640aa3c8bd7eee2becee85f93a668cc29)

> 🔐 **Access from the list.** The menu of each item in the Models, Knowledge, Prompts, Skills, Tools and Notes lists now has an Access entry, so who can use an item can be changed without opening it. [Commit](https://github.com/open-webui/open-webui/commit/b3ce7de8d3ab59f99f0006775dc3158ea079deda), [Commit](https://github.com/open-webui/open-webui/commit/d4f01d7344fdec082c956b7b0c9c650a2e63485b), [Commit](https://github.com/open-webui/open-webui/commit/784b72f19ef2ebf894480ab5e303bc995d3d4b59)

> 📬 **Message queue in channels.** Messages sent in a channel or thread while an earlier one is still sending or a file is still uploading now wait in a queue above the message box, where each can be sent right away, edited or removed, and they go out in order once their files are ready, where a message sent during an upload went out with a broken attachment. [Commit](https://github.com/open-webui/open-webui/commit/8a4547104c4f88c02b607ad7b6849dc22f377c28), [#31587](https://github.com/open-webui/open-webui/issues/31587)

> 🪣 **S3 file storage on the slim image.** The slim image can now keep files in an S3 bucket with "STORAGE_PROVIDER" set to s3, where it only supported local storage; Google Cloud and Azure storage still need the standard image. [Commit](https://github.com/open-webui/open-webui/commit/425da8b6cc14144895c6eba19a70cf5c8881d3cf)

> 🪞 **Cloning chats you can only read.** A chat you open read only, such as one in a folder shared with you, now shows a Clone Chat button that copies it into your own chats from the message you are viewing, for anyone allowed to import chats. [Commit](https://github.com/open-webui/open-webui/commit/c6dd9a451abef12e93e19624a64cfb8a9a1f6465)

> 🔖 **Build shown next to the version.** The version in Settings shows "dev" and the commit for development builds and the commit for other non-release builds, and update checks and the update notification now only run on release builds. [Commit](https://github.com/open-webui/open-webui/commit/51f0e01258b92c77952d4534bb8ce8c618b2700c)

> 🌙 **Local time and last seen on profile cards.** The profile card that opens on a person's name in channels or on an @mention now shows their local time and when they were last active, and it reloads each time it opens so the status stays current. [Commit](https://github.com/open-webui/open-webui/commit/538f9c9090dab742b4d8e3a1b3a058956ea8f39b)

> 💡 **Custom parameter suggestions.** Custom parameter fields now suggest common parameter names such as reasoning_effort, service_tier, num_ctx or response_format as you type, along with typical values for many of them, and a new row starts empty instead of with a placeholder name. [Commit](https://github.com/open-webui/open-webui/commit/10fdca6e36fd616d611cadbf95aee956eb823ca2)

> 🎛️ **Tool approval mode no longer restored from drafts.** Restoring a saved message draft no longer switches the chat's tool approval mode, which could save settings and approve tools without asking. [Commit](https://github.com/open-webui/open-webui/commit/332237662f446f8264cd4db10a1b4513ba5fb76b)

> 🛂 **Forwarded headers trust for open-webui serve.** Starting Open WebUI with "open-webui serve" or "open-webui dev" now honors "FORWARDED_ALLOW_IPS", where it trusted forwarded headers from every connection regardless of the setting. [Commit](https://github.com/open-webui/open-webui/commit/24e30d1cbdaab624dfe20f479f805e6791cf0226)

> 🕵️ **Shared chats keep the owner's settings private.** Opening a chat shared with you, by link or through a shared folder, no longer hands you the owner's chat settings such as the system prompt and other parameters, chosen tools, filters and tool servers, filled-in chat variables or message details, and cloning a shared chat no longer copies the owner's chat variables or files the clone under the owner's folder. [Commit](https://github.com/open-webui/open-webui/commit/de73bb830aeb150bc5bb4707566d3969f70408b0)

> 🛃 **Administrators read other users' chats without writing to them.** With "ENABLE_ADMIN_CHAT_ACCESS" on, administrators can now only read other users' chats, where they could also send messages into them, stop their replies or answer their tool approvals through direct API requests even though the chat page only showed them read only. [Commit](https://github.com/open-webui/open-webui/commit/6cfd6987e5b220040c2e476105779dcc10d3d14b)

> 💻 **Skills from personal terminals.** Skills and the AGENTS.md instructions file from a terminal you added in your own settings are now read through your browser, so they reach the model even when only your browser can reach that terminal, such as one running on your own machine. [Commit](https://github.com/open-webui/open-webui/commit/7ad0ae46873511723f59c7f78bfd59f7c3982e1f), [#30410](https://github.com/open-webui/open-webui/issues/30410)

> 🪆 **Sub-agents get personal tools.** Sub-agents and chats resuming after a tool approval now get the same personal tool servers, such as Open Terminal, as the main model, where they received none of them. [#31424](https://github.com/open-webui/open-webui/pull/31424), [#29893](https://github.com/open-webui/open-webui/issues/29893)

> ⏩ **Send now on queued messages.** Clicking Send now on one queued message sends only that message, where it could send the whole queue at once and leave two replies mixed together in the chat until a reload. [Commit](https://github.com/open-webui/open-webui/commit/aea7d34f456e5a6621c7daa6e74a586c65488b45), [#30027](https://github.com/open-webui/open-webui/issues/30027)

> 💲 **Clipboard variable keeps dollar signs.** The clipboard variable in prompts now pastes text exactly as copied, where a pair of dollar signs turned into one and broke shell commands and math formulas. [#31364](https://github.com/open-webui/open-webui/pull/31364), [#31363](https://github.com/open-webui/open-webui/issues/31363)

> 👆 **Clicking outside menus.** Clicking outside the model selector or another open menu now only closes it, where the click also went through to whatever was underneath, such as a suggested prompt. [Commit](https://github.com/open-webui/open-webui/commit/8fc416ee78bd8264f7a716f147d4000c466ae646), [#29878](https://github.com/open-webui/open-webui/issues/29878)

> 🪧 **Chat title with title generation off.** With title generation turned off, a new chat now shows its first message as the title in the header and browser tab right away, where it showed "New Chat" until a reload and a note's chat panel showed the whole model reply as its title; a title that arrives before the new chat has finished opening is no longer dropped either. [#31355](https://github.com/open-webui/open-webui/pull/31355), [#31348](https://github.com/open-webui/open-webui/issues/31348), [Commit](https://github.com/open-webui/open-webui/commit/82b51813721d171f0e347c9348be1042f9b010e8), [#31492](https://github.com/open-webui/open-webui/issues/31492)

> 📑 **Copy Last Code Block with Artifacts open.** The Copy Last Code Block shortcut now copies the last code block in the chat, where it copied the Artifacts pane's full HTML whenever the pane was open. [#31613](https://github.com/open-webui/open-webui/pull/31613), [#31476](https://github.com/open-webui/open-webui/issues/31476)

> ♿ **Sort order for screen readers in the user list.** The column headings of the admin user list now tell screen readers the current sort order after it changes, where they kept announcing the initial one. [Commit](https://github.com/open-webui/open-webui/commit/dc713a68a4ba0e1691892d8f53ebe1e9a877721c), [#31581](https://github.com/open-webui/open-webui/issues/31581)

> 🫂 **Access grants of deleted groups.** Deleting a group now also removes its access grants, and the Access dialog lists grants left behind by groups deleted earlier under their ID so they can be removed, where they were hidden from the list but saved again, leaving the item marked Shared with no way to undo it. [Commit](https://github.com/open-webui/open-webui/commit/dd576bade3449057803248450ac453b29e6a60a5), [#31923](https://github.com/open-webui/open-webui/issues/31923)

> ⏭️ **Chats open at their latest reply.** Opening a chat whose saved position points to an earlier message on the current branch now moves to the newest reply on that branch, where only compacted chats were moved forward, and broken or stale message links are skipped while finding it. [Commit](https://github.com/open-webui/open-webui/commit/d8659c237c7819d114a5d70db25ec6aed86b9bbf), [#27618](https://github.com/open-webui/open-webui/issues/27618)

> 📂 **File browser stays in your folder.** When the agent runs a command in the terminal, the file browser panel now stays in the folder you picked and keeps the open file in view, where it jumped back to the top folder after every command, so the next command also ran there. [#31878](https://github.com/open-webui/open-webui/pull/31878), [#30051](https://github.com/open-webui/open-webui/issues/30051)

> 🗄️ **Fresh PostgreSQL installs with a custom schema.** With "DATABASE_SCHEMA" set, a fresh PostgreSQL install now creates its tables in that schema and starts, where the migrations created them in the public schema and startup failed with a "relation does not exist" error; a schema that does not exist, or one that already holds tables without migration history, now stops startup with a clear message instead. [Commit](https://github.com/open-webui/open-webui/commit/65f44053d20c9a70c6edb9d59f965c09754c29dd), [#31526](https://github.com/open-webui/open-webui/issues/31526)

> 🪢 **Plain web addresses in chat.** Web addresses written without link text now show "&" instead of "&amp;", and addresses written in angle brackets open the address as written, where they pointed to a different address with the wrong parameters. [Commit](https://github.com/open-webui/open-webui/commit/652d0cff073632f8d4adeaf2b994a786fb8a317b), [#31902](https://github.com/open-webui/open-webui/issues/31902)

> 🗓️ **Calendar days from another month.** Clicking a day of the previous or next month in the calendar now also loads that month's events, where the view switched months and stayed empty. [Commit](https://github.com/open-webui/open-webui/commit/34abd6e121b8fee25936d312752e1c6da16f4ae9), [#30972](https://github.com/open-webui/open-webui/issues/30972)

> 📥 **Downloading files whose upload is gone.** Downloading a file whose original upload is missing from storage now gives its extracted text as a text file, where the download failed with not found. [Commit](https://github.com/open-webui/open-webui/commit/33dd7dd224d4fc4031185a4dd589242681f24af7)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-reliability-and-performance-changes-in-v0-12-0|5 Reliability and Performance changes in v0.12.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5 Enterprise and Administration changes in v0.12.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]] · Voice and Audio
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
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-10-09 · Claude Code · [[Changes/Claude Code/2026-10-09-3-developer-workflow-changes-in-v2-1-296|3 Developer Workflow changes in v2.1.296]]
- Later: 2026-10-10 · OpenClaw · [[Changes/OpenClaw/2026-10-10-11-developer-workflow-changes-in-v2026-10-1|11 Developer Workflow changes in v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-3a0531&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-27-developer-workflow-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-3a0531%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->