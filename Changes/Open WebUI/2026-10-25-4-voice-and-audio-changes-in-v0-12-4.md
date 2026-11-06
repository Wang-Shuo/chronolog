---
card_id: open-webui-2026-10-25-6d1569
date: '2026-10-25'
description: "Open WebUI · 2026-10-25 · Voice and Audio: 4 changes in v0.12.4 — \U0001F5C2️
  **File browser grid view.** The terminal file browser can now switch between a list
  and a…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1203
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 59eec8e3cf24fdcb7d2bbb02cb4cc09b0bec309ae6ca2752efa4fcfa87f22566
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-25-6d1569
  comparison: ''
  date: '2026-10-25'
  description: 'Open WebUI — v0.12.4: 4 Voice and Audio changes'
  evidence:
  - quote: "\U0001F5C2️ **File browser grid view.** The terminal file browser can
      now switch between a list and a grid view from its menu, folders show how many
      items they hold, and on larger screens hovering a file shows a preview, up to
      1 MB for text files and 20 MB for images, audio, video and documents. [Commit](https://github.com/open-webui/open-webui/commit/a76c02e58ec81621cf3c6ca38eb0d09eccee694f),
      [Commit](https://github.com/open-webui/open-webui/commit/fefa31fae22a8eb9d39aaf17063373c27fd5a61e),
      [Commit](https://github.com/open-webui/open-webui/commit/fa50081e67bfa9883bbc92fd47b20d3f3974c927)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4E8 **Voice call user headers.** With \"ENABLE_FORWARD_USER_INFO_HEADERS\"
      on, Realtime voice calls now also send the user info headers, or the signed
      user JWT when configured, to the realtime provider, like chat requests do. [#32733](https://github.com/open-webui/open-webui/pull/32733),
      [Commit](https://github.com/open-webui/open-webui/commit/c7e159bdd66a1d05331e6a579e627004bc3c51d1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F50A **Voice from Settings > Audio.** Read Aloud and voice mode
      now use the voice picked in Settings > Audio, which in Firefox fell back to
      the default voice. [#32705](https://github.com/open-webui/open-webui/pull/32705),
      [Commit](https://github.com/open-webui/open-webui/commit/5edbd12bc9ba29eb0753d9bc888165d23171b0d8),
      [#32704](https://github.com/open-webui/open-webui/issues/32704)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4DE **Ended Realtime calls named correctly.** When the voice provider
      ends a Realtime call, the call now shows \"Voice provider connection closed\"
      instead of sometimes showing \"Voice connection failed\". [#32730](https://github.com/open-webui/open-webui/pull/32730),
      [Commit](https://github.com/open-webui/open-webui/commit/cd74e6d1266c5a623f9c143d7efa6cb4d6f3f0c9),
      [#32729](https://github.com/open-webui/open-webui/issues/32729)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-voice-and-audio-changes-in-v0-12-4
  source_release: open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79
  source_type: github_releases
  theme: voice
  title: 4 Voice and Audio changes in v0.12.4
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-22-vscode-added-a-log-warning-that-says-what-to-do-when-dictation-or-the-extension|VSCode
  Added a log warning that says what to do when dictation or the extension''s…]]'
- '[[Changes/Codex CLI/2026-10-23-3-voice-and-audio-changes-in-rust-v0-164-0|3 Voice
  and Audio changes in rust-v0.164.0]]'
- '[[Changes/Ollama/2026-10-24-ollama-can-now-generate-speech-https-docs-ollama-com-capabilities-speech-on-maco|Ollama
  can now generate speech((source link) on macOS]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79]]'
source_type: github_releases
theme: voice
title: 4 Voice and Audio changes in v0.12.4
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Voice and Audio changes in v0.12.4

**Open WebUI** · 2026-10-25 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.4) · from [[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|v0.12.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗂️ **File browser grid view.** The terminal file browser can now switch between a list and a grid view from its menu, folders show how many items they hold, and on larger screens hovering a file shows a preview, up to 1 MB for text files and 20 MB for images, audio, video and documents. [Commit](https://github.com/open-webui/open-webui/commit/a76c02e58ec81621cf3c6ca38eb0d09eccee694f), [Commit](https://github.com/open-webui/open-webui/commit/fefa31fae22a8eb9d39aaf17063373c27fd5a61e), [Commit](https://github.com/open-webui/open-webui/commit/fa50081e67bfa9883bbc92fd47b20d3f3974c927)

> 📨 **Voice call user headers.** With "ENABLE_FORWARD_USER_INFO_HEADERS" on, Realtime voice calls now also send the user info headers, or the signed user JWT when configured, to the realtime provider, like chat requests do. [#32733](https://github.com/open-webui/open-webui/pull/32733), [Commit](https://github.com/open-webui/open-webui/commit/c7e159bdd66a1d05331e6a579e627004bc3c51d1)

> 🔊 **Voice from Settings > Audio.** Read Aloud and voice mode now use the voice picked in Settings > Audio, which in Firefox fell back to the default voice. [#32705](https://github.com/open-webui/open-webui/pull/32705), [Commit](https://github.com/open-webui/open-webui/commit/5edbd12bc9ba29eb0753d9bc888165d23171b0d8), [#32704](https://github.com/open-webui/open-webui/issues/32704)

> 📞 **Ended Realtime calls named correctly.** When the voice provider ends a Realtime call, the call now shows "Voice provider connection closed" instead of sometimes showing "Voice connection failed". [#32730](https://github.com/open-webui/open-webui/pull/32730), [Commit](https://github.com/open-webui/open-webui/commit/cd74e6d1266c5a623f9c143d7efa6cb4d6f3f0c9), [#32729](https://github.com/open-webui/open-webui/issues/32729)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-25-16-model-support-changes-in-v0-12-4|16 Model Support changes in v0.12.4]] · Model Support
- [[Changes/Open WebUI/2026-10-25-10-safety-and-privacy-changes-in-v0-12-4|10 Safety and Privacy changes in v0.12.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-25-13-interface-experience-changes-in-v0-12-4|13 Interface Experience changes in v0.12.4]] · Interface Experience
- [[Changes/Open WebUI/2026-10-25-images-settings-save-admins-can-now-save-images-settings-while-image-generation|🖌️ Images settings save. Admins can now save Images settings while Image…]] · Image Generation
- [[Changes/Open WebUI/2026-10-25-4-context-window-changes-in-v0-12-4|4 Context Window changes in v0.12.4]] · Context Window
- [[Changes/Open WebUI/2026-10-25-5-apps-and-integrations-changes-in-v0-12-4|5 Apps and Integrations changes in v0.12.4]] · Apps and Integrations
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
## Nearby in Voice and Audio

- Earlier: 2026-10-24 · Ollama · [[Changes/Ollama/2026-10-24-ollama-can-now-generate-speech-https-docs-ollama-com-capabilities-speech-on-maco|Ollama can now generate speech((source link) on macOS]]
- Later: 2026-10-26 · ElevenLabs · [[Changes/ElevenLabs/2026-10-26-python-sdk|Python SDK]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-25-6d1569&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-25-4-voice-and-audio-changes-in-v0-12-4.md%0ACard%20ID%3A%20open-webui-2026-10-25-6d1569%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->