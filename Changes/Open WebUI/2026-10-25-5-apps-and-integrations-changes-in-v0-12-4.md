---
card_id: open-webui-2026-10-25-7c1230
date: '2026-10-25'
description: "Open WebUI · 2026-10-25 · Apps and Integrations: 5 changes in v0.12.4
  — \U0001FA83 **Questions survive reconnects.** When the page reloads or loses its
  connection while…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1312
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4920a6ed838f01478c38ce87764eb6db7d7a7df4867f9daa4862a44374fe4417
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-25-7c1230
  comparison: ''
  date: '2026-10-25'
  description: 'Open WebUI — v0.12.4: 5 Apps and Integrations changes'
  evidence:
  - quote: "\U0001FA83 **Questions survive reconnects.** When the page reloads or
      loses its connection while Ask User, a tool approval, an MCP server's input
      request or a function's confirmation or input dialog waits for you, the question
      now comes back once you reopen that chat within a minute, so the request no
      longer waits without an answer. [Commit](https://github.com/open-webui/open-webui/commit/c596d40bd4f554057738ba779b38781a7c2de108)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F6F0️ **MCP protocol 2026-07-28.** MCP connections now also work
      with servers that speak the stateless 2026-07-28 protocol version, while older
      servers still connect through the earlier handshake. [#33087](https://github.com/open-webui/open-webui/pull/33087),
      [Commit](https://github.com/open-webui/open-webui/commit/8151826483163877cec837b35ba7c1affdd1fb5a),
      [#29778](https://github.com/open-webui/open-webui/issues/29778)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001FAA2 **MCP tools with alternative inputs.** MCP tools that describe
      their input as alternatives, such as a page by ID or by path, now receive the
      arguments the model sends, where they were called with none and the server rejected
      the call. [#32903](https://github.com/open-webui/open-webui/pull/32903), [Commit](https://github.com/open-webui/open-webui/commit/f3f9af594f3c9a20b1f46f846eb8393630733f6c),
      [#32898](https://github.com/open-webui/open-webui/discussions/32898)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001FA7A **Readable MCP tool errors.** When an MCP tool returns an error,
      the model now gets the server's error text as written instead of an unreadable
      dump of the whole result, so it can correct the call where it tended to retry
      the same broken one. [#32942](https://github.com/open-webui/open-webui/pull/32942),
      [Commit](https://github.com/open-webui/open-webui/commit/37af63b6496d545f6f2d4e8067ea01de209e218b),
      [#32918](https://github.com/open-webui/open-webui/issues/32918)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F6A6 **Stricter MCP timeouts and redirects.** \"MCP_INITIALIZE_TIMEOUT\",
      10 seconds by default, now also limits listing tools and reading resources on
      MCP servers, so slow servers may need a higher value, and MCP connections now
      only follow redirects that stay on the same address. [#33087](https://github.com/open-webui/open-webui/pull/33087),
      [Commit](https://github.com/open-webui/open-webui/commit/8151826483163877cec837b35ba7c1affdd1fb5a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-apps-and-integrations-changes-in-v0-12-4
  source_release: open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79
  source_type: github_releases
  theme: apps-integrations
  title: 5 Apps and Integrations changes in v0.12.4
  type: change
related_changes:
- '[[Changes/OpenHands/2026-10-23-2-apps-and-integrations-changes-in-v1-32-0|2 Apps
  and Integrations changes in v1.32.0]]'
- '[[Changes/Replit/2026-10-23-keep-your-apps-running-when-credits-run-out|Keep your
  apps running when credits run out]]'
- '[[Changes/Windsurf/2026-10-23-5-apps-and-integrations-changes-in-v3-11-212|5 Apps
  and Integrations changes in v3.11.212]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79]]'
source_type: github_releases
theme: apps-integrations
title: 5 Apps and Integrations changes in v0.12.4
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Apps and Integrations changes in v0.12.4

**Open WebUI** · 2026-10-25 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.4) · from [[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|v0.12.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🪃 **Questions survive reconnects.** When the page reloads or loses its connection while Ask User, a tool approval, an MCP server's input request or a function's confirmation or input dialog waits for you, the question now comes back once you reopen that chat within a minute, so the request no longer waits without an answer. [Commit](https://github.com/open-webui/open-webui/commit/c596d40bd4f554057738ba779b38781a7c2de108)

> 🛰️ **MCP protocol 2026-07-28.** MCP connections now also work with servers that speak the stateless 2026-07-28 protocol version, while older servers still connect through the earlier handshake. [#33087](https://github.com/open-webui/open-webui/pull/33087), [Commit](https://github.com/open-webui/open-webui/commit/8151826483163877cec837b35ba7c1affdd1fb5a), [#29778](https://github.com/open-webui/open-webui/issues/29778)

> 🪢 **MCP tools with alternative inputs.** MCP tools that describe their input as alternatives, such as a page by ID or by path, now receive the arguments the model sends, where they were called with none and the server rejected the call. [#32903](https://github.com/open-webui/open-webui/pull/32903), [Commit](https://github.com/open-webui/open-webui/commit/f3f9af594f3c9a20b1f46f846eb8393630733f6c), [#32898](https://github.com/open-webui/open-webui/discussions/32898)

> 🩺 **Readable MCP tool errors.** When an MCP tool returns an error, the model now gets the server's error text as written instead of an unreadable dump of the whole result, so it can correct the call where it tended to retry the same broken one. [#32942](https://github.com/open-webui/open-webui/pull/32942), [Commit](https://github.com/open-webui/open-webui/commit/37af63b6496d545f6f2d4e8067ea01de209e218b), [#32918](https://github.com/open-webui/open-webui/issues/32918)

> 🚦 **Stricter MCP timeouts and redirects.** "MCP_INITIALIZE_TIMEOUT", 10 seconds by default, now also limits listing tools and reading resources on MCP servers, so slow servers may need a higher value, and MCP connections now only follow redirects that stay on the same address. [#33087](https://github.com/open-webui/open-webui/pull/33087), [Commit](https://github.com/open-webui/open-webui/commit/8151826483163877cec837b35ba7c1affdd1fb5a)

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
- [[Changes/Open WebUI/2026-10-25-49-developer-workflow-changes-in-v0-12-4|49 Developer Workflow changes in v0.12.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-25-4-editor-experience-changes-in-v0-12-4|4 Editor Experience changes in v0.12.4]] · Editor Experience
- [[Changes/Open WebUI/2026-10-25-3-reliability-and-performance-changes-in-v0-12-4|3 Reliability and Performance changes in v0.12.4]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-25-5-account-and-access-changes-in-v0-12-4|5 Account and Access changes in v0.12.4]] · Account and Access
- [[Changes/Open WebUI/2026-10-25-3-files-and-data-changes-in-v0-12-4|3 Files and Data changes in v0.12.4]] · Files and Data
- [[Changes/Open WebUI/2026-10-25-shared-chat-pages-load-once-chats-opened-under-s-through-a-share-link-or-by-an-a|🔗 Shared chat pages load once. Chats opened under /s/, through a share link…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-25-web-search-settings-save-admins-can-now-save-web-search-settings-such-as-the-web|🌍 Web Search settings save. Admins can now save Web Search settings such…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-25-translation-updates-translations-for-korean-cebuano-thai-german-japanese-vietnam|🌐 Translation updates. Translations for Korean, Cebuano, Thai, German, Japanese…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-23 · Windsurf · [[Changes/Windsurf/2026-10-23-5-apps-and-integrations-changes-in-v3-11-212|5 Apps and Integrations changes in v3.11.212]]
- Later: 2026-10-26 · Claude Code · [[Changes/Claude Code/2026-10-26-3-apps-and-integrations-changes-in-v2-1-311|3 Apps and Integrations changes in v2.1.311]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-25-7c1230&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-25-5-apps-and-integrations-changes-in-v0-12-4.md%0ACard%20ID%3A%20open-webui-2026-10-25-7c1230%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->