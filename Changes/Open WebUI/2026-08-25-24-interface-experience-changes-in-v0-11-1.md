---
card_id: open-webui-2026-08-25-d77415
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Interface Experience: 24 changes in v0.11.1
  — \U0001F4CD **Sidebar folders fetched once.** Refreshing the sidebar now asks for
  your folders…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2690
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bdaa1dc9228a77cbc34e4e8dab03b8710f65559ea3f78bb705e6f06cec6812c5
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-d77415
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 24 Interface Experience changes'
  evidence:
  - quote: "\U0001F4CD **Sidebar folders fetched once.** Refreshing the sidebar now
      asks for your folders once rather than three times, on page load and on every
      action that refreshes it. [#28662](https://github.com/open-webui/open-webui/pull/28662),
      [#28661](https://github.com/open-webui/open-webui/issues/28661)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F321 **Faster chat list and unread counts.** Opening the sidebar,
      and the unread markers on folders, no longer read through your whole chat history
      to produce a short list, which on an instance with 15000 chats took 2 to 4 seconds.
      [#27663](https://github.com/open-webui/open-webui/pull/27663), [#27622](https://github.com/open-webui/open-webui/issues/27622),
      [#27745](https://github.com/open-webui/open-webui/issues/27745)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⌨️ **Model switching from the message box.** Typing "/model" now tells
      you which model you are on, switching to another by name with "/model" followed
      by its id, or opening the model picker straight from the slash menu without
      reaching for the mouse. [Commit](https://github.com/open-webui/open-webui/commit/29eeda9f9abeaedf77176908cb036ace7f175e76),
      [Commit](https://github.com/open-webui/open-webui/commit/9c7ce154e79a3baea3a8223ab1e5b1371ce80dbb)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9ED **More from the message box.** The slash menu now offers settings
      and, in a new chat, a toggle for temporary chat, alongside the commands that
      were already there. [Commit](https://github.com/open-webui/open-webui/commit/a5ea732c1e3d0d1f70a7e4b6a20c30c336114784)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F520 **Interface scaling throughout.** The UI Scale setting and
      your browser's own text size now resize the whole interface consistently, including
      the sidebar, menus, dialogs, and file browser, rather than leaving parts of
      it fixed. [Commit](https://github.com/open-webui/open-webui/commit/30d08a42f8b0c32cc64dccd81203cc760651584a),
      [Commit](https://github.com/open-webui/open-webui/commit/b5f86e6a433b519e30a5a6f1b0a5bf985939c9a8),
      [Commit](https://github.com/open-webui/open-webui/commit/ec03e8814403422a6ab3dc62f4239fd7af439361),
      [Commit](https://github.com/open-webui/open-webui/commit/72a909fd2f3ac8d67554f6c85bc1723934454e2d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4F1 **Smoother sidebar on mobile.** The sidebar now follows your
      finger as you swipe it open or closed, responds to a quick flick, dims the page
      behind it as it moves, and gives every chat row a menu button you can reach
      without a hover you cannot perform on a touchscreen. [Commit](https://github.com/open-webui/open-webui/commit/b20bcdbba72707e3b0cf2b9a6a5f3168b464ba3c),
      [Commit](https://github.com/open-webui/open-webui/commit/178ccb30e1253ea727fe5ccbb5cc3ca3832dc70b),
      [Commit](https://github.com/open-webui/open-webui/commit/943294df9a03d45e2708b330e876967af3463282),
      [Commit](https://github.com/open-webui/open-webui/commit/d6679082e5c6b0b54ca00a99a88e66a53a30c7d9),
      [Commit](https://github.com/open-webui/open-webui/commit/d8ae7ed40551362922925d9d6e47ba65d3658cfd),
      [Commit](https://github.com/open-webui/open-webui/commit/be4afd75452361ead376d9977cf2ca8cb93e55eb),
      [Commit](https://github.com/open-webui/open-webui/commit/ab41dcc487d1517f7c8c5d0b02a02cdaadedb03d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6AA **Sidebar that stays put.** Opening and closing the sidebar
      is now a smooth transition that keeps your chat list loaded, instead of rebuilding
      the list each time. [Commit](https://github.com/open-webui/open-webui/commit/3c010951db2cc349466658d3b52234cc22dad327),
      [Commit](https://github.com/open-webui/open-webui/commit/8edab5020eaa5d47b12a572eb632a891aa29440a),
      [Commit](https://github.com/open-webui/open-webui/commit/3e9b075954b7fc9d492a7ec832550b10b0bf80ed),
      [Commit](https://github.com/open-webui/open-webui/commit/3793b0c886f57630dc31320d3c0257c933c6eca1),
      [Commit](https://github.com/open-webui/open-webui/commit/0b4b7ae5ff3c0a17b58e8e85a5fddf190e3bda14)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F441️ **Turning off chat previews.** A new setting under Settings
      and Interface lets you switch off the preview card that appears when you hover
      a chat in the sidebar, useful for a quieter sidebar, for sharing your screen,
      or on a slow connection. [#27632](https://github.com/open-webui/open-webui/pull/27632),
      [#27639](https://github.com/open-webui/open-webui/issues/27639)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F39B️ **Chat Controls staying put.** Hovering a chat in the sidebar
      whose preview contains an artifact no longer forces the Chat Controls pane open
      and fills it with that artifact, over the chat you currently have open. [#27773](https://github.com/open-webui/open-webui/pull/27773),
      [#27772](https://github.com/open-webui/open-webui/issues/27772)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F465 **Sharing with people already added.** The access picker no
      longer offers people and groups that already have access, and the Users heading
      no longer appears above an empty list. [Commit](https://github.com/open-webui/open-webui/commit/385d08bea5899bcb160391db466662b0a0a6f801),
      [#28253](https://github.com/open-webui/open-webui/issues/28253)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FAE5 **Deactivating a model.** Turning a model off no longer removes
      the wrong entry from the model list, or fails the list outright and leaves the
      model picker empty for everyone until the model is turned back on. [Commit](https://github.com/open-webui/open-webui/commit/5cecb7dbfad3994228ee53d19232650400462332),
      [#28202](https://github.com/open-webui/open-webui/issues/28202)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5BC️ **Images that no longer exist.** A message whose image file
      has been deleted now shows a small unavailable placeholder that cannot be opened,
      rather than a broken image that spilled the whole reply text into the picture
      frame and still opened full screen. [#27730](https://github.com/open-webui/open-webui/pull/27730),
      [#27728](https://github.com/open-webui/open-webui/issues/27728), [Commit](https://github.com/open-webui/open-webui/commit/f8c5fda283e6206d92e81ae3b83ffe5d7a144b03)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5D1️ **Delete offered only when allowed.** The chat deletion controls
      in the sidebar, the chat menu, search, archived chats, and data controls no
      longer appear for people whose permissions do not allow deleting, where using
      them produced an access denied error. [#27714](https://github.com/open-webui/open-webui/pull/27714),
      [#27713](https://github.com/open-webui/open-webui/issues/27713)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9F2 **The page staying still when typing.** Returning focus to
      the message box no longer scrolls the conversation, so switching chats, running
      a command, or picking something from a menu leaves your place on screen alone.
      [Commit](https://github.com/open-webui/open-webui/commit/9122c24ea2d506aad50384ca8aba1616d1bed626)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⌨️ **Reaching the download options by keyboard.** In the model picker,
      arrowing past the last result now moves through the options to fetch that model
      from each server that can supply it, so they can be chosen with the keyboard
      instead of only by clicking. [Commit](https://github.com/open-webui/open-webui/commit/4e03d89414a7be1203579f45225ca64f1221205f),
      [Commit](https://github.com/open-webui/open-webui/commit/25802c048e6123fa602182949ad2a9f349e1e863)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4C2 **Opening a folder in the sidebar.** Selecting a folder now
      refreshes just that folder's chats rather than rebuilding the whole folder tree,
      and a folder that is empty or still loading says so instead of showing nothing.
      [Commit](https://github.com/open-webui/open-webui/commit/2e939874904e1ae54d02b8bc6d745931a8e1f673),
      [Commit](https://github.com/open-webui/open-webui/commit/86b7bf1f7e11109816b0d16ada708c637b50c520)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4CE **Default pinned models taking effect.** Changing the default
      pinned models now reaches people who have never chosen their own, where simply
      having opened the interface once was enough to freeze the list they first saw,
      and reordering a pin no longer moves the wrong one or reopens the sidebar section
      afterwards. [#28069](https://github.com/open-webui/open-webui/pull/28069), [#28067](https://github.com/open-webui/open-webui/discussions/28067)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F3D7️ **Editing a folder from its page.** Renaming a folder, changing
      its icon, creating a subfolder, or deleting it from the folder's own page now
      updates the sidebar straight away, instead of leaving the old name and icon
      there, and the new subfolder missing, until a reload. [Commit](https://github.com/open-webui/open-webui/commit/a40f6f2860b49b4c7f11e369f11bd46e9451eabf),
      [Commit](https://github.com/open-webui/open-webui/commit/736e38338ede1fca5af0829e35585a72f8517d32),
      [#28692](https://github.com/open-webui/open-webui/pull/28692), [#28690](https://github.com/open-webui/open-webui/issues/28690)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4E3 **Long channel names in the sidebar.** A channel with a long
      name no longer squeezes its own menu button out of the row. [Commit](https://github.com/open-webui/open-webui/commit/b5da50f3df51786972010c75c7736d5f95362e58),
      [#28671](https://github.com/open-webui/open-webui/pull/28671), [#28670](https://github.com/open-webui/open-webui/issues/28670)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4EC **Mark as unread in chat search.** Marking a chat unread from
      the search dialog now works and updates the sidebar, where the menu entry looked
      normal but did nothing at all. [#28136](https://github.com/open-webui/open-webui/pull/28136),
      [#28135](https://github.com/open-webui/open-webui/issues/28135)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5B2️ **Losing the collapsed sidebar.** With the sidebar collapsed,
      opening a chat no longer pushes the narrow sidebar strip off the edge of the
      screen, which left no way to reopen the sidebar short of shrinking the window
      to phone size. [#28501](https://github.com/open-webui/open-webui/pull/28501),
      [#28500](https://github.com/open-webui/open-webui/issues/28500)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5B1 **Clicking inside a chat preview.** Clicking an image or a
      source in the preview that appears when you hover a chat in the sidebar no longer
      flashes a viewer open and shut, since the preview is meant only to be read.
      [#27770](https://github.com/open-webui/open-webui/pull/27770), [#27769](https://github.com/open-webui/open-webui/issues/27769)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FAF3 **Dropping a chat where it already was.** Dragging a chat in
      the sidebar and releasing it where it started no longer reloads the whole sidebar,
      which took around a dozen requests for a move that changed nothing. [#28664](https://github.com/open-webui/open-webui/pull/28664),
      [#28663](https://github.com/open-webui/open-webui/issues/28663)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6E4 **The terminal picker vanishing mid-reply.** The terminal picker
      now stays in place while a reply is being written, greyed out until it finishes,
      where it disappeared from the message box entirely and took the name of the
      selected terminal with it. [Commit](https://github.com/open-webui/open-webui/commit/7a533d0d5b85981f8c5668636f931f8b4a97d604)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 24-interface-experience-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: interface-experience
  title: 24 Interface Experience changes in v0.11.1
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-23954-add-trailing-space-to-autocomplete-suggestions-by-jone|SSR
  Agent Issue Fix (23954): Add trailing space to autocomplete suggestions]]'
- '[[Changes/Lovable/2026-08-25-see-time-and-cost-while-lovable-works|See time and
  cost while Lovable works]]'
- '[[Changes/Microsoft 365 Copilot/2026-08-25-simplified-design-for-the-microsoft-365-copilot-app-windows-mac-web-microsoft-36|Simplified
  design for the Microsoft 365 Copilot app Windows, Mac…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: interface-experience
title: 24 Interface Experience changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 24 Interface Experience changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📍 **Sidebar folders fetched once.** Refreshing the sidebar now asks for your folders once rather than three times, on page load and on every action that refreshes it. [#28662](https://github.com/open-webui/open-webui/pull/28662), [#28661](https://github.com/open-webui/open-webui/issues/28661)

> 🌡 **Faster chat list and unread counts.** Opening the sidebar, and the unread markers on folders, no longer read through your whole chat history to produce a short list, which on an instance with 15000 chats took 2 to 4 seconds. [#27663](https://github.com/open-webui/open-webui/pull/27663), [#27622](https://github.com/open-webui/open-webui/issues/27622), [#27745](https://github.com/open-webui/open-webui/issues/27745)

> ⌨️ **Model switching from the message box.** Typing "/model" now tells you which model you are on, switching to another by name with "/model" followed by its id, or opening the model picker straight from the slash menu without reaching for the mouse. [Commit](https://github.com/open-webui/open-webui/commit/29eeda9f9abeaedf77176908cb036ace7f175e76), [Commit](https://github.com/open-webui/open-webui/commit/9c7ce154e79a3baea3a8223ab1e5b1371ce80dbb)

> 🧭 **More from the message box.** The slash menu now offers settings and, in a new chat, a toggle for temporary chat, alongside the commands that were already there. [Commit](https://github.com/open-webui/open-webui/commit/a5ea732c1e3d0d1f70a7e4b6a20c30c336114784)

> 🔠 **Interface scaling throughout.** The UI Scale setting and your browser's own text size now resize the whole interface consistently, including the sidebar, menus, dialogs, and file browser, rather than leaving parts of it fixed. [Commit](https://github.com/open-webui/open-webui/commit/30d08a42f8b0c32cc64dccd81203cc760651584a), [Commit](https://github.com/open-webui/open-webui/commit/b5f86e6a433b519e30a5a6f1b0a5bf985939c9a8), [Commit](https://github.com/open-webui/open-webui/commit/ec03e8814403422a6ab3dc62f4239fd7af439361), [Commit](https://github.com/open-webui/open-webui/commit/72a909fd2f3ac8d67554f6c85bc1723934454e2d)

> 📱 **Smoother sidebar on mobile.** The sidebar now follows your finger as you swipe it open or closed, responds to a quick flick, dims the page behind it as it moves, and gives every chat row a menu button you can reach without a hover you cannot perform on a touchscreen. [Commit](https://github.com/open-webui/open-webui/commit/b20bcdbba72707e3b0cf2b9a6a5f3168b464ba3c), [Commit](https://github.com/open-webui/open-webui/commit/178ccb30e1253ea727fe5ccbb5cc3ca3832dc70b), [Commit](https://github.com/open-webui/open-webui/commit/943294df9a03d45e2708b330e876967af3463282), [Commit](https://github.com/open-webui/open-webui/commit/d6679082e5c6b0b54ca00a99a88e66a53a30c7d9), [Commit](https://github.com/open-webui/open-webui/commit/d8ae7ed40551362922925d9d6e47ba65d3658cfd), [Commit](https://github.com/open-webui/open-webui/commit/be4afd75452361ead376d9977cf2ca8cb93e55eb), [Commit](https://github.com/open-webui/open-webui/commit/ab41dcc487d1517f7c8c5d0b02a02cdaadedb03d)

> 🚪 **Sidebar that stays put.** Opening and closing the sidebar is now a smooth transition that keeps your chat list loaded, instead of rebuilding the list each time. [Commit](https://github.com/open-webui/open-webui/commit/3c010951db2cc349466658d3b52234cc22dad327), [Commit](https://github.com/open-webui/open-webui/commit/8edab5020eaa5d47b12a572eb632a891aa29440a), [Commit](https://github.com/open-webui/open-webui/commit/3e9b075954b7fc9d492a7ec832550b10b0bf80ed), [Commit](https://github.com/open-webui/open-webui/commit/3793b0c886f57630dc31320d3c0257c933c6eca1), [Commit](https://github.com/open-webui/open-webui/commit/0b4b7ae5ff3c0a17b58e8e85a5fddf190e3bda14)

> 👁️ **Turning off chat previews.** A new setting under Settings and Interface lets you switch off the preview card that appears when you hover a chat in the sidebar, useful for a quieter sidebar, for sharing your screen, or on a slow connection. [#27632](https://github.com/open-webui/open-webui/pull/27632), [#27639](https://github.com/open-webui/open-webui/issues/27639)

> 🎛️ **Chat Controls staying put.** Hovering a chat in the sidebar whose preview contains an artifact no longer forces the Chat Controls pane open and fills it with that artifact, over the chat you currently have open. [#27773](https://github.com/open-webui/open-webui/pull/27773), [#27772](https://github.com/open-webui/open-webui/issues/27772)

> 👥 **Sharing with people already added.** The access picker no longer offers people and groups that already have access, and the Users heading no longer appears above an empty list. [Commit](https://github.com/open-webui/open-webui/commit/385d08bea5899bcb160391db466662b0a0a6f801), [#28253](https://github.com/open-webui/open-webui/issues/28253)

> 🫥 **Deactivating a model.** Turning a model off no longer removes the wrong entry from the model list, or fails the list outright and leaves the model picker empty for everyone until the model is turned back on. [Commit](https://github.com/open-webui/open-webui/commit/5cecb7dbfad3994228ee53d19232650400462332), [#28202](https://github.com/open-webui/open-webui/issues/28202)

> 🖼️ **Images that no longer exist.** A message whose image file has been deleted now shows a small unavailable placeholder that cannot be opened, rather than a broken image that spilled the whole reply text into the picture frame and still opened full screen. [#27730](https://github.com/open-webui/open-webui/pull/27730), [#27728](https://github.com/open-webui/open-webui/issues/27728), [Commit](https://github.com/open-webui/open-webui/commit/f8c5fda283e6206d92e81ae3b83ffe5d7a144b03)

> 🗑️ **Delete offered only when allowed.** The chat deletion controls in the sidebar, the chat menu, search, archived chats, and data controls no longer appear for people whose permissions do not allow deleting, where using them produced an access denied error. [#27714](https://github.com/open-webui/open-webui/pull/27714), [#27713](https://github.com/open-webui/open-webui/issues/27713)

> 🧲 **The page staying still when typing.** Returning focus to the message box no longer scrolls the conversation, so switching chats, running a command, or picking something from a menu leaves your place on screen alone. [Commit](https://github.com/open-webui/open-webui/commit/9122c24ea2d506aad50384ca8aba1616d1bed626)

> ⌨️ **Reaching the download options by keyboard.** In the model picker, arrowing past the last result now moves through the options to fetch that model from each server that can supply it, so they can be chosen with the keyboard instead of only by clicking. [Commit](https://github.com/open-webui/open-webui/commit/4e03d89414a7be1203579f45225ca64f1221205f), [Commit](https://github.com/open-webui/open-webui/commit/25802c048e6123fa602182949ad2a9f349e1e863)

> 📂 **Opening a folder in the sidebar.** Selecting a folder now refreshes just that folder's chats rather than rebuilding the whole folder tree, and a folder that is empty or still loading says so instead of showing nothing. [Commit](https://github.com/open-webui/open-webui/commit/2e939874904e1ae54d02b8bc6d745931a8e1f673), [Commit](https://github.com/open-webui/open-webui/commit/86b7bf1f7e11109816b0d16ada708c637b50c520)

> 📎 **Default pinned models taking effect.** Changing the default pinned models now reaches people who have never chosen their own, where simply having opened the interface once was enough to freeze the list they first saw, and reordering a pin no longer moves the wrong one or reopens the sidebar section afterwards. [#28069](https://github.com/open-webui/open-webui/pull/28069), [#28067](https://github.com/open-webui/open-webui/discussions/28067)

> 🏗️ **Editing a folder from its page.** Renaming a folder, changing its icon, creating a subfolder, or deleting it from the folder's own page now updates the sidebar straight away, instead of leaving the old name and icon there, and the new subfolder missing, until a reload. [Commit](https://github.com/open-webui/open-webui/commit/a40f6f2860b49b4c7f11e369f11bd46e9451eabf), [Commit](https://github.com/open-webui/open-webui/commit/736e38338ede1fca5af0829e35585a72f8517d32), [#28692](https://github.com/open-webui/open-webui/pull/28692), [#28690](https://github.com/open-webui/open-webui/issues/28690)

> 📣 **Long channel names in the sidebar.** A channel with a long name no longer squeezes its own menu button out of the row. [Commit](https://github.com/open-webui/open-webui/commit/b5da50f3df51786972010c75c7736d5f95362e58), [#28671](https://github.com/open-webui/open-webui/pull/28671), [#28670](https://github.com/open-webui/open-webui/issues/28670)

> 📬 **Mark as unread in chat search.** Marking a chat unread from the search dialog now works and updates the sidebar, where the menu entry looked normal but did nothing at all. [#28136](https://github.com/open-webui/open-webui/pull/28136), [#28135](https://github.com/open-webui/open-webui/issues/28135)

> 🖲️ **Losing the collapsed sidebar.** With the sidebar collapsed, opening a chat no longer pushes the narrow sidebar strip off the edge of the screen, which left no way to reopen the sidebar short of shrinking the window to phone size. [#28501](https://github.com/open-webui/open-webui/pull/28501), [#28500](https://github.com/open-webui/open-webui/issues/28500)

> 🖱 **Clicking inside a chat preview.** Clicking an image or a source in the preview that appears when you hover a chat in the sidebar no longer flashes a viewer open and shut, since the preview is meant only to be read. [#27770](https://github.com/open-webui/open-webui/pull/27770), [#27769](https://github.com/open-webui/open-webui/issues/27769)

> 🫳 **Dropping a chat where it already was.** Dragging a chat in the sidebar and releasing it where it started no longer reloads the whole sidebar, which took around a dozen requests for a move that changed nothing. [#28664](https://github.com/open-webui/open-webui/pull/28664), [#28663](https://github.com/open-webui/open-webui/issues/28663)

> 🛤 **The terminal picker vanishing mid-reply.** The terminal picker now stays in place while a reply is being written, greyed out until it finishes, where it disappeared from the message box entirely and took the name of the selected terminal with it. [Commit](https://github.com/open-webui/open-webui/commit/7a533d0d5b85981f8c5668636f931f8b4a97d604)

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
- [[Changes/Open WebUI/2026-08-25-5-search-and-browsing-changes-in-v0-11-1|5 Search and Browsing changes in v0.11.1]] · Search and Browsing
- [[Changes/Open WebUI/2026-08-25-4-voice-and-audio-changes-in-v0-11-1|4 Voice and Audio changes in v0.11.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-08-25-56-model-support-changes-in-v0-11-1|56 Model Support changes in v0.11.1]] · Model Support
- [[Changes/Open WebUI/2026-08-25-39-other-changes-in-v0-11-1|39 other changes in v0.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-08-25 · Microsoft 365 Copilot · [[Changes/Microsoft 365 Copilot/2026-08-25-simplified-design-for-the-microsoft-365-copilot-app-windows-mac-web-microsoft-36|Simplified design for the Microsoft 365 Copilot app Windows, Mac…]]
- Later: 2026-08-25 · Raycast · [[Changes/Raycast/2026-08-25-window-management-center-hotkey-now-truly-centers-a-window-when-respect-stage-ma|Window Management : Center hotkey now truly centers a window…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-d77415&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-24-interface-experience-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-d77415%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->