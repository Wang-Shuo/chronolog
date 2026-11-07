---
card_id: open-webui-2026-10-16-0c1a77
date: '2026-10-16'
description: "Open WebUI · 2026-10-16 · Developer Workflow: 20 changes in v0.12.3
  — \U0001F4E1 **Much lighter streaming with Redis.** With Redis, a streaming reply
  is now stored…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1308
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 98fa316e951fe3f19201fa154144cf2ef3b9d48e618819d03c3838bb2fe22e1e
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-16-0c1a77
  comparison: ''
  date: '2026-10-16'
  description: 'Open WebUI — v0.12.3: 20 Developer Workflow changes'
  evidence:
  - quote: "\U0001F4E1 **Much lighter streaming with Redis.** With Redis, a streaming
      reply is now stored under its own key and new text is appended to it instead
      of rewriting the whole reply into a shared hash on every update, and replies
      started on older instances are still read during an upgrade; with room channels
      on, each instance now only subscribes to the rooms of people connected to it,
      so Redis no longer sends it live updates for chats it does not serve. [Commit](https://github.com/open-webui/open-webui/commit/f5a26f53a089eeb9683ead687a1fd3e9125132a6)
      [Commit](https://github.com/open-webui/open-webui/commit/362b01d0b2ba677858a5af85caf3dd8544c5e6df)
      [#32478](https://github.com/open-webui/open-webui/issues/32478)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F4DD **Richer Markdown file previews.** Markdown files opened in
      the terminal file browser now render with the same renderer as chat replies,
      including math, footnotes, highlighted code blocks, alerts and Mermaid diagrams,
      as well as HTML blocks mixed with Markdown, laid out as a compact document,
      and task list checkboxes in an editable file can be ticked to save the change
      to the file. [Commit](https://github.com/open-webui/open-webui/commit/c9a52208da9e8deeac6f2df7fcacbe519c2acb29)
      [Commit](https://github.com/open-webui/open-webui/commit/7c3980338b72c5faa7e7f3a088deb477644fef40)
      [Commit](https://github.com/open-webui/open-webui/commit/15ac5163ea00a934ec0c68d2bb7f6bc5c655223e)
      [#32514](https://github.com/open-webui/open-webui/issues/32514)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F440 **Live collaborators in shared chats.** The top bar of a chat
      now shows the pictures of the other people who have the same chat open at that
      moment, up to three and a count for the rest, with a Collaborators list that
      opens their profile cards. [Commit](https://github.com/open-webui/open-webui/commit/4dedaaf6e2292c2c4fb48668eee1292cfd7de2d0),
      [Commit](https://github.com/open-webui/open-webui/commit/8191ac30dd79b4a39130fe83ffc16035776be484),
      [Commit](https://github.com/open-webui/open-webui/commit/8e9519240fcdcd568a9b951ba06e523c58e68350)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F50E **Workspace search.** The search window now searches your chats,
      chats in folders shared with you, chats shared with you, channel and direct
      messages and notes in one place, with filters for content type, a folder or
      channel, and whether something was created by you or shared with you, highlighted
      matches, a preview of each result with Ctrl/Cmd + Enter, Copy link, and channel
      results that open the thread scrolled to the matching message. [Commit](https://github.com/open-webui/open-webui/commit/b4db56ae96651d926adb4aefc6ec1275f35c6b6f),
      [Commit](https://github.com/open-webui/open-webui/commit/ef28e99e587a2845a2852bb6ab8c182dc1588980),
      [Commit](https://github.com/open-webui/open-webui/commit/1a1a81d8e09330900ac74e4bc97a48e1e0d52a8a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F4DC **Full text of long status lines.** Status lines above a reply,
      such as a token usage summary sent by a function, can now be clicked to show
      their full text, and with several status lines the history shows every entry
      in full. [#32532](https://github.com/open-webui/open-webui/pull/32532) [Commit](https://github.com/open-webui/open-webui/commit/291b57bec24ec670050b996ede45ea6dd56c7f9f)
      [#30056](https://github.com/open-webui/open-webui/issues/30056)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F9FE **API key header requests in the audit log.** Requests authenticated
      with an API key in the x-api-key header, as Anthropic SDKs send it, or in a
      header set with \"CUSTOM_API_KEY_HEADER\" now appear in the audit log under
      the key's owner, and failed attempts with a wrong key are logged without a user,
      where these requests were missing from the audit log. [#32443](https://github.com/open-webui/open-webui/pull/32443),
      [Commit](https://github.com/open-webui/open-webui/commit/f7c8ad012ddcf458c39cdf8a96b41c410655196c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F3F7️ **Tags of imported chats.** Imported chats now show their
      tags and the tags appear in tag suggestions, where tags missing from the account
      were not created on import. [#32454](https://github.com/open-webui/open-webui/pull/32454),
      [Commit](https://github.com/open-webui/open-webui/commit/fd47370e851c3fcb55ba69aec39488aaec7f4b02),
      [#32453](https://github.com/open-webui/open-webui/issues/32453)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: ⌨️ **Input methods in channels.** Pressing Enter to confirm a word while
      typing with an input method, such as for Japanese, Chinese or Korean, no longer
      sends and clears a channel message before the word is in. [Commit](https://github.com/open-webui/open-webui/commit/9d0aa791ad70ef2a7771c74955e2c9304021609e)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F5B1️ **Scroll error after leaving a chat.** Scrolling a chat right
      before opening Notes no longer logs a TypeError in the browser console. [#32458](https://github.com/open-webui/open-webui/pull/32458),
      [Commit](https://github.com/open-webui/open-webui/commit/9245e31ccba8e464054297b1f3660ab3e7f77969),
      [#32457](https://github.com/open-webui/open-webui/issues/32457)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F4D0 **Steady first turn in new chats.** The latest message and
      reply in a new chat now keep their real height when the chat gets saved and
      the message list reloads, so the view no longer jumps on the first turn. [Commit](https://github.com/open-webui/open-webui/commit/bbccff89c1cf318c21cd9eeb4228f98882a33736)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F4AC **Sending in channels.** Your own channel message now stays
      in place when the server confirms it instead of being redrawn, and the channel
      scrolls to your new message as you send it, where it could jump or keep the
      old scroll position. [Commit](https://github.com/open-webui/open-webui/commit/99457b373e6b81fe50df0d18a75d126706237841)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F4C2 **Terminal folder in new chats.** In a new chat, files you
      attach are uploaded to the folder open in the terminal file browser and the
      file browser stays in that folder once the chat is created, where uploads could
      go to the default folder and the browser jumped back to it. [Commit](https://github.com/open-webui/open-webui/commit/7ca62fdf93f6177e929cca20c712f3d958e1d935)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F4C1 **Shared folder settings and access.** Editing a shared folder's
      models, system prompt or files no longer resets its sharing mode, and a subfolder
      in a folder shared with write access stays writable when it is also shared directly
      with read access. [Commit](https://github.com/open-webui/open-webui/commit/f4557ca06b8331c8914bac9e8f54ce63b0445c21),
      [Commit](https://github.com/open-webui/open-webui/commit/4a70253bc8586ad1d2a97241665b2060324bab37)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F50A **Read aloud with slow speech.** Read aloud no longer stops
      after the first sentence when the speech engine takes longer to produce the
      next one than the current one takes to play. [#32484](https://github.com/open-webui/open-webui/pull/32484),
      [Commit](https://github.com/open-webui/open-webui/commit/7da8653e71cda807609d9ec64912cd319c0d6ccf),
      [#32446](https://github.com/open-webui/open-webui/issues/32446)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F9F5 **Replies in channel threads.** A reply started in one channel
      thread no longer carries over to the next thread you open, where messages could
      quote a message from the other thread. [#32490](https://github.com/open-webui/open-webui/pull/32490),
      [Commit](https://github.com/open-webui/open-webui/commit/0696bfdf276fe6331c6dfaf50c53676d08b1574a),
      [#32489](https://github.com/open-webui/open-webui/issues/32489)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: ↩️ **Right-to-left lists.** Bullets, numbers and task checkboxes of Markdown
      lists now sit on the correct side for right-to-left text in replies and file
      previews. [Commit](https://github.com/open-webui/open-webui/commit/6768f52aca633945292da08ff9450fd4dc62705f),
      [#32444](https://github.com/open-webui/open-webui/issues/32444)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F501 **Regenerate in cloned shared chats.** Regenerate now works
      in a chat you cloned or forked from someone else's share, where it failed with
      \"You can only regenerate your own messages\". [#32508](https://github.com/open-webui/open-webui/pull/32508),
      [Commit](https://github.com/open-webui/open-webui/commit/ad3e5a6c425f7b4af8a66f2e8dc42a7625526f95),
      [#32505](https://github.com/open-webui/open-webui/issues/32505)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F5D1️ **Delete hidden for repliers in shared chats.** People replying
      in a shared chat no longer see a Delete button the server refuses, which made
      a deleted reply come back on reload; Delete shows to the chat's owner and to
      administrators when \"ENABLE_ADMIN_CHAT_ACCESS\" is on. [#32480](https://github.com/open-webui/open-webui/pull/32480),
      [Commit](https://github.com/open-webui/open-webui/commit/493b10630b0c19ee5a60f9de0fc5d997bb82bbb1),
      [#32479](https://github.com/open-webui/open-webui/issues/32479)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F3E0 **Refresh with Landing Page Mode set to Chat.** Refreshing
      a new chat when Landing Page Mode is Chat no longer hides the message field
      and opens the model menu in the top left corner. [#32510](https://github.com/open-webui/open-webui/pull/32510),
      [Commit](https://github.com/open-webui/open-webui/commit/5d4f16bcc9af1afac55dc0ffb4dced96041531a5),
      [#32509](https://github.com/open-webui/open-webui/issues/32509)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F50C **Tool servers back after an outage.** With Redis, tools from
      OpenAPI tool servers now come back once the servers are reachable again, where
      an empty list cached while every server was down kept them missing until a restart
      or a save in the tool server settings. [#32533](https://github.com/open-webui/open-webui/pull/32533)
      [Commit](https://github.com/open-webui/open-webui/commit/51a4d582706311502ae53a6c11876b87a49f5400)
      [#29573](https://github.com/open-webui/open-webui/issues/29573)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 20-developer-workflow-changes-in-v0-12-3
  source_release: open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d
  source_type: github_releases
  theme: developer-workflow
  title: 20 Developer Workflow changes in v0.12.3
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-15-2-developer-workflow-changes-in-v2-1-301|2 Developer
  Workflow changes in v2.1.301]]'
- '[[Changes/Codex CLI/2026-10-15-15-developer-workflow-changes-in-rust-v0-163-0|15
  Developer Workflow changes in rust-v0.163.0]]'
- '[[Changes/Google Antigravity/2026-10-15-mark-all-as-read-is-now-available-from-the-command-palette-whenever-you-have-unr|Mark
  All as Read is now available from the command palette whenever you have unread…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d|open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d]]'
source_type: github_releases
theme: developer-workflow
title: 20 Developer Workflow changes in v0.12.3
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Developer Workflow changes in v0.12.3

**Open WebUI** · 2026-10-16 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.3) · from [[Releases/Open WebUI/open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d|v0.12.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📡 **Much lighter streaming with Redis.** With Redis, a streaming reply is now stored under its own key and new text is appended to it instead of rewriting the whole reply into a shared hash on every update, and replies started on older instances are still read during an upgrade; with room channels on, each instance now only subscribes to the rooms of people connected to it, so Redis no longer sends it live updates for chats it does not serve. [Commit](https://github.com/open-webui/open-webui/commit/f5a26f53a089eeb9683ead687a1fd3e9125132a6) [Commit](https://github.com/open-webui/open-webui/commit/362b01d0b2ba677858a5af85caf3dd8544c5e6df) [#32478](https://github.com/open-webui/open-webui/issues/32478)

> 📝 **Richer Markdown file previews.** Markdown files opened in the terminal file browser now render with the same renderer as chat replies, including math, footnotes, highlighted code blocks, alerts and Mermaid diagrams, as well as HTML blocks mixed with Markdown, laid out as a compact document, and task list checkboxes in an editable file can be ticked to save the change to the file. [Commit](https://github.com/open-webui/open-webui/commit/c9a52208da9e8deeac6f2df7fcacbe519c2acb29) [Commit](https://github.com/open-webui/open-webui/commit/7c3980338b72c5faa7e7f3a088deb477644fef40) [Commit](https://github.com/open-webui/open-webui/commit/15ac5163ea00a934ec0c68d2bb7f6bc5c655223e) [#32514](https://github.com/open-webui/open-webui/issues/32514)

> 👀 **Live collaborators in shared chats.** The top bar of a chat now shows the pictures of the other people who have the same chat open at that moment, up to three and a count for the rest, with a Collaborators list that opens their profile cards. [Commit](https://github.com/open-webui/open-webui/commit/4dedaaf6e2292c2c4fb48668eee1292cfd7de2d0), [Commit](https://github.com/open-webui/open-webui/commit/8191ac30dd79b4a39130fe83ffc16035776be484), [Commit](https://github.com/open-webui/open-webui/commit/8e9519240fcdcd568a9b951ba06e523c58e68350)

> 🔎 **Workspace search.** The search window now searches your chats, chats in folders shared with you, chats shared with you, channel and direct messages and notes in one place, with filters for content type, a folder or channel, and whether something was created by you or shared with you, highlighted matches, a preview of each result with Ctrl/Cmd + Enter, Copy link, and channel results that open the thread scrolled to the matching message. [Commit](https://github.com/open-webui/open-webui/commit/b4db56ae96651d926adb4aefc6ec1275f35c6b6f), [Commit](https://github.com/open-webui/open-webui/commit/ef28e99e587a2845a2852bb6ab8c182dc1588980), [Commit](https://github.com/open-webui/open-webui/commit/1a1a81d8e09330900ac74e4bc97a48e1e0d52a8a)

> 📜 **Full text of long status lines.** Status lines above a reply, such as a token usage summary sent by a function, can now be clicked to show their full text, and with several status lines the history shows every entry in full. [#32532](https://github.com/open-webui/open-webui/pull/32532) [Commit](https://github.com/open-webui/open-webui/commit/291b57bec24ec670050b996ede45ea6dd56c7f9f) [#30056](https://github.com/open-webui/open-webui/issues/30056)

> 🧾 **API key header requests in the audit log.** Requests authenticated with an API key in the x-api-key header, as Anthropic SDKs send it, or in a header set with "CUSTOM_API_KEY_HEADER" now appear in the audit log under the key's owner, and failed attempts with a wrong key are logged without a user, where these requests were missing from the audit log. [#32443](https://github.com/open-webui/open-webui/pull/32443), [Commit](https://github.com/open-webui/open-webui/commit/f7c8ad012ddcf458c39cdf8a96b41c410655196c)

> 🏷️ **Tags of imported chats.** Imported chats now show their tags and the tags appear in tag suggestions, where tags missing from the account were not created on import. [#32454](https://github.com/open-webui/open-webui/pull/32454), [Commit](https://github.com/open-webui/open-webui/commit/fd47370e851c3fcb55ba69aec39488aaec7f4b02), [#32453](https://github.com/open-webui/open-webui/issues/32453)

> ⌨️ **Input methods in channels.** Pressing Enter to confirm a word while typing with an input method, such as for Japanese, Chinese or Korean, no longer sends and clears a channel message before the word is in. [Commit](https://github.com/open-webui/open-webui/commit/9d0aa791ad70ef2a7771c74955e2c9304021609e)

> 🖱️ **Scroll error after leaving a chat.** Scrolling a chat right before opening Notes no longer logs a TypeError in the browser console. [#32458](https://github.com/open-webui/open-webui/pull/32458), [Commit](https://github.com/open-webui/open-webui/commit/9245e31ccba8e464054297b1f3660ab3e7f77969), [#32457](https://github.com/open-webui/open-webui/issues/32457)

> 📐 **Steady first turn in new chats.** The latest message and reply in a new chat now keep their real height when the chat gets saved and the message list reloads, so the view no longer jumps on the first turn. [Commit](https://github.com/open-webui/open-webui/commit/bbccff89c1cf318c21cd9eeb4228f98882a33736)

> 💬 **Sending in channels.** Your own channel message now stays in place when the server confirms it instead of being redrawn, and the channel scrolls to your new message as you send it, where it could jump or keep the old scroll position. [Commit](https://github.com/open-webui/open-webui/commit/99457b373e6b81fe50df0d18a75d126706237841)

> 📂 **Terminal folder in new chats.** In a new chat, files you attach are uploaded to the folder open in the terminal file browser and the file browser stays in that folder once the chat is created, where uploads could go to the default folder and the browser jumped back to it. [Commit](https://github.com/open-webui/open-webui/commit/7ca62fdf93f6177e929cca20c712f3d958e1d935)

> 📁 **Shared folder settings and access.** Editing a shared folder's models, system prompt or files no longer resets its sharing mode, and a subfolder in a folder shared with write access stays writable when it is also shared directly with read access. [Commit](https://github.com/open-webui/open-webui/commit/f4557ca06b8331c8914bac9e8f54ce63b0445c21), [Commit](https://github.com/open-webui/open-webui/commit/4a70253bc8586ad1d2a97241665b2060324bab37)

> 🔊 **Read aloud with slow speech.** Read aloud no longer stops after the first sentence when the speech engine takes longer to produce the next one than the current one takes to play. [#32484](https://github.com/open-webui/open-webui/pull/32484), [Commit](https://github.com/open-webui/open-webui/commit/7da8653e71cda807609d9ec64912cd319c0d6ccf), [#32446](https://github.com/open-webui/open-webui/issues/32446)

> 🧵 **Replies in channel threads.** A reply started in one channel thread no longer carries over to the next thread you open, where messages could quote a message from the other thread. [#32490](https://github.com/open-webui/open-webui/pull/32490), [Commit](https://github.com/open-webui/open-webui/commit/0696bfdf276fe6331c6dfaf50c53676d08b1574a), [#32489](https://github.com/open-webui/open-webui/issues/32489)

> ↩️ **Right-to-left lists.** Bullets, numbers and task checkboxes of Markdown lists now sit on the correct side for right-to-left text in replies and file previews. [Commit](https://github.com/open-webui/open-webui/commit/6768f52aca633945292da08ff9450fd4dc62705f), [#32444](https://github.com/open-webui/open-webui/issues/32444)

> 🔁 **Regenerate in cloned shared chats.** Regenerate now works in a chat you cloned or forked from someone else's share, where it failed with "You can only regenerate your own messages". [#32508](https://github.com/open-webui/open-webui/pull/32508), [Commit](https://github.com/open-webui/open-webui/commit/ad3e5a6c425f7b4af8a66f2e8dc42a7625526f95), [#32505](https://github.com/open-webui/open-webui/issues/32505)

> 🗑️ **Delete hidden for repliers in shared chats.** People replying in a shared chat no longer see a Delete button the server refuses, which made a deleted reply come back on reload; Delete shows to the chat's owner and to administrators when "ENABLE_ADMIN_CHAT_ACCESS" is on. [#32480](https://github.com/open-webui/open-webui/pull/32480), [Commit](https://github.com/open-webui/open-webui/commit/493b10630b0c19ee5a60f9de0fc5d997bb82bbb1), [#32479](https://github.com/open-webui/open-webui/issues/32479)

> 🏠 **Refresh with Landing Page Mode set to Chat.** Refreshing a new chat when Landing Page Mode is Chat no longer hides the message field and opens the model menu in the top left corner. [#32510](https://github.com/open-webui/open-webui/pull/32510), [Commit](https://github.com/open-webui/open-webui/commit/5d4f16bcc9af1afac55dc0ffb4dced96041531a5), [#32509](https://github.com/open-webui/open-webui/issues/32509)

> 🔌 **Tool servers back after an outage.** With Redis, tools from OpenAPI tool servers now come back once the servers are reachable again, where an empty list cached while every server was down kept them missing until a restart or a save in the tool server settings. [#32533](https://github.com/open-webui/open-webui/pull/32533) [Commit](https://github.com/open-webui/open-webui/commit/51a4d582706311502ae53a6c11876b87a49f5400) [#29573](https://github.com/open-webui/open-webui/issues/29573)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-16-built-in-tools-turned-back-on-stay-on-a-built-in-tool-such-as-memory-that-is-off|🧰 Built-in tools turned back on stay on. A built-in tool such as Memory…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-16-4-files-and-data-changes-in-v0-12-3|4 Files and Data changes in v0.12.3]] · Files and Data
- [[Changes/Open WebUI/2026-10-16-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-16-3-model-support-changes-in-v0-12-3|3 Model Support changes in v0.12.3]] · Model Support
- [[Changes/Open WebUI/2026-10-16-2-account-and-access-changes-in-v0-12-3|2 Account and Access changes in v0.12.3]] · Account and Access
- [[Changes/Open WebUI/2026-10-16-2-enterprise-and-administration-changes-in-v0-12-3|2 Enterprise and Administration changes in v0.12.3]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-16-2-context-window-changes-in-v0-12-3|2 Context Window changes in v0.12.3]] · Context Window
- [[Changes/Open WebUI/2026-10-16-clear-input-selections-shortcut-clearing-the-model-override-selected-tools-and-f|🧹 Clear Input Selections shortcut. Clearing the model override, selected tools…]] · Image Generation
- [[Changes/Open WebUI/2026-10-16-built-in-tools-with-a-custom-tools-parameter-a-model-with-a-custom-parameter-nam|🧩 Built-in tools with a custom tools parameter. A model with a custom parameter…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-16-4-interface-experience-changes-in-v0-12-3|4 Interface Experience changes in v0.12.3]] · Interface Experience
- [[Changes/Open WebUI/2026-10-16-2-editor-experience-changes-in-v0-12-3|2 Editor Experience changes in v0.12.3]] · Editor Experience
- [[Changes/Open WebUI/2026-10-16-2-safety-and-privacy-changes-in-v0-12-3|2 Safety and Privacy changes in v0.12.3]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-16-2-collaboration-changes-in-v0-12-3|2 Collaboration changes in v0.12.3]] · Collaboration
- [[Changes/Open WebUI/2026-10-16-translation-updates-translations-for-portuguese-brazil-chinese-traditional-arabi|🌐 Translation updates. Translations for Portuguese (Brazil), Chinese…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-10-15 · Google Antigravity · [[Changes/Google Antigravity/2026-10-15-mark-all-as-read-is-now-available-from-the-command-palette-whenever-you-have-unr|Mark All as Read is now available from the command palette whenever you have unread…]]
- Later: 2026-10-16 · OpenClaw · [[Changes/OpenClaw/2026-10-16-3-developer-workflow-changes-in-v2026-10-4|3 Developer Workflow changes in v2026.10.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-16-0c1a77&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-16-20-developer-workflow-changes-in-v0-12-3.md%0ACard%20ID%3A%20open-webui-2026-10-16-0c1a77%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->