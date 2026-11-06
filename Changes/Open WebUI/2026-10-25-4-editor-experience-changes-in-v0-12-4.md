---
card_id: open-webui-2026-10-25-9d483e
date: '2026-10-25'
description: "Open WebUI · 2026-10-25 · Editor Experience: 4 changes in v0.12.4 —
  \U0001F39A️ **Chat Controls saved per setting.** A change in a chat's Controls,
  such as its system…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1321
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f89ecc093930a6ee5b44793ae29ba61abe8cb6e25eabbed87b104628195a8b76
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-25-9d483e
  comparison: ''
  date: '2026-10-25'
  description: 'Open WebUI — v0.12.4: 4 Editor Experience changes'
  evidence:
  - quote: "\U0001F39A️ **Chat Controls saved per setting.** A change in a chat's
      Controls, such as its system prompt or a parameter, now saves only that setting,
      so a copy of the chat open in another tab or on another device no longer wipes
      it with older settings. [Commit](https://github.com/open-webui/open-webui/commit/b4a58be193031827f2fc19b943646136d1e43575),
      [#32755](https://github.com/open-webui/open-webui/issues/32755)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F304 **WebP image editing.** Editing a WebP image with Image Edit
      now works in the Docker image, where the image reached the provider without
      an image type and was rejected. [#32902](https://github.com/open-webui/open-webui/pull/32902),
      [Commit](https://github.com/open-webui/open-webui/commit/f6f42b0111054123d6811270feca35bf9ce6d19d),
      [#32899](https://github.com/open-webui/open-webui/issues/32899)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4C7 **Knowledge file text edits.** The Preview of a text file in
      a knowledge base now shows its indexed text and refreshes after you save an
      edit, where it kept showing the original upload, and saving empty content is
      now refused. [Commit](https://github.com/open-webui/open-webui/commit/82d6f230b4e701e85863c01b1992a25a767696bf)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F500 **Sharing changed only in Access.** Saving a model, prompt,
      tool, skill, knowledge base, note, channel or calendar no longer changes who
      it is shared with, which is now changed only in the item's Access settings,
      saved right away in the model editor, channel settings and external knowledge
      sources, or through the access endpoints that channels and calendars now also
      have. [Commit](https://github.com/open-webui/open-webui/commit/5f95008abdfbbbfbe5c080de0347deb70eb507b6),
      [Commit](https://github.com/open-webui/open-webui/commit/c7e34e0fa9bdd34f798ab197e1e21aca2234ed2b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-editor-experience-changes-in-v0-12-4
  source_release: open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79
  source_type: github_releases
  theme: editor-experience
  title: 4 Editor Experience changes in v0.12.4
  type: change
related_changes:
- '[[Changes/Dify/2026-10-23-3-editor-experience-changes-in-1-18-0|3 Editor Experience
  changes in 1.18.0]]'
- '[[Changes/OpenHands/2026-10-23-chore-verify-openhands-time-network-responses-and-order-them-by-completion-by-en|chore(verify-openhands):
  time network responses and order them by completion]]'
- '[[Changes/Windsurf/2026-10-23-in-ide-mode-a-chat-tab-whose-agent-could-not-start-a-session-says-why-and-offers|In
  IDE mode, a chat tab whose agent could not start a session says why and offers…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79]]'
source_type: github_releases
theme: editor-experience
title: 4 Editor Experience changes in v0.12.4
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Editor Experience changes in v0.12.4

**Open WebUI** · 2026-10-25 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.4) · from [[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|v0.12.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎚️ **Chat Controls saved per setting.** A change in a chat's Controls, such as its system prompt or a parameter, now saves only that setting, so a copy of the chat open in another tab or on another device no longer wipes it with older settings. [Commit](https://github.com/open-webui/open-webui/commit/b4a58be193031827f2fc19b943646136d1e43575), [#32755](https://github.com/open-webui/open-webui/issues/32755)

> 🌄 **WebP image editing.** Editing a WebP image with Image Edit now works in the Docker image, where the image reached the provider without an image type and was rejected. [#32902](https://github.com/open-webui/open-webui/pull/32902), [Commit](https://github.com/open-webui/open-webui/commit/f6f42b0111054123d6811270feca35bf9ce6d19d), [#32899](https://github.com/open-webui/open-webui/issues/32899)

> 📇 **Knowledge file text edits.** The Preview of a text file in a knowledge base now shows its indexed text and refreshes after you save an edit, where it kept showing the original upload, and saving empty content is now refused. [Commit](https://github.com/open-webui/open-webui/commit/82d6f230b4e701e85863c01b1992a25a767696bf)

> 🔀 **Sharing changed only in Access.** Saving a model, prompt, tool, skill, knowledge base, note, channel or calendar no longer changes who it is shared with, which is now changed only in the item's Access settings, saved right away in the model editor, channel settings and external knowledge sources, or through the access endpoints that channels and calendars now also have. [Commit](https://github.com/open-webui/open-webui/commit/5f95008abdfbbbfbe5c080de0347deb70eb507b6), [Commit](https://github.com/open-webui/open-webui/commit/c7e34e0fa9bdd34f798ab197e1e21aca2234ed2b)

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
- [[Changes/Open WebUI/2026-10-25-49-developer-workflow-changes-in-v0-12-4|49 Developer Workflow changes in v0.12.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-25-3-reliability-and-performance-changes-in-v0-12-4|3 Reliability and Performance changes in v0.12.4]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-25-5-account-and-access-changes-in-v0-12-4|5 Account and Access changes in v0.12.4]] · Account and Access
- [[Changes/Open WebUI/2026-10-25-3-files-and-data-changes-in-v0-12-4|3 Files and Data changes in v0.12.4]] · Files and Data
- [[Changes/Open WebUI/2026-10-25-shared-chat-pages-load-once-chats-opened-under-s-through-a-share-link-or-by-an-a|🔗 Shared chat pages load once. Chats opened under /s/, through a share link…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-25-web-search-settings-save-admins-can-now-save-web-search-settings-such-as-the-web|🌍 Web Search settings save. Admins can now save Web Search settings such…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-25-translation-updates-translations-for-korean-cebuano-thai-german-japanese-vietnam|🌐 Translation updates. Translations for Korean, Cebuano, Thai, German, Japanese…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-10-23 · Windsurf · [[Changes/Windsurf/2026-10-23-in-ide-mode-a-chat-tab-whose-agent-could-not-start-a-session-says-why-and-offers|In IDE mode, a chat tab whose agent could not start a session says why and offers…]]
- Later: 2026-10-26 · Claude Code · [[Changes/Claude Code/2026-10-26-vscode-changed-the-session-list-side-bar-to-load-web-sessions-when-the-web-tab-i|VSCode Changed the session list side bar to load Web sessions when the Web tab…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-25-9d483e&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-25-4-editor-experience-changes-in-v0-12-4.md%0ACard%20ID%3A%20open-webui-2026-10-25-9d483e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->