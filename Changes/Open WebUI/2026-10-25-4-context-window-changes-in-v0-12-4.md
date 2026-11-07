---
card_id: open-webui-2026-10-25-6d6885
date: '2026-10-25'
description: "Open WebUI · 2026-10-25 · Context Window: 4 changes in v0.12.4 — \U0001F4CD
  **Compaction shown in chats.** A \"Context compacted\" line now marks the message
  where older…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2594
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0078341e73597079f5b536622146cca8b8b34770c0162eeba74610237483306a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-25-6d6885
  comparison: ''
  date: '2026-10-25'
  description: 'Open WebUI — v0.12.4: 4 Context Window changes'
  evidence:
  - quote: "\U0001F4CD **Compaction shown in chats.** A \"Context compacted\" line
      now marks the message where older messages were summarized, opens to show the
      summary and also appears inside a reply when compaction ran between its tool
      calls, Chat Controls > Overview tags that message, and compaction progress and
      errors now show in the chat instead of as pop-up notices. [Commit](https://github.com/open-webui/open-webui/commit/f465a4be11c0c64969da70f1f5b770bd21088b8a),
      [Commit](https://github.com/open-webui/open-webui/commit/c8786f426ad263ea4113652ed576d3c15ee341d6),
      [Commit](https://github.com/open-webui/open-webui/commit/3311f999928964ca1f7870fefb407553197dc2d5),
      [Commit](https://github.com/open-webui/open-webui/commit/3855acf02d44b78e7969599155896865fd362123),
      [#31324](https://github.com/open-webui/open-webui/issues/31324)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F5DC️ **Compaction in more chats.** Context compaction now also
      runs in temporary chats and in short chats that are already over the threshold,
      such as one question with a reply full of tool output, so the follow-up and
      any regenerate or edit of it no longer fail with a context length error. [#32794](https://github.com/open-webui/open-webui/pull/32794),
      [Commit](https://github.com/open-webui/open-webui/commit/56eca192ab7d98dd9d1a9811e4452dc32145848d),
      [#32781](https://github.com/open-webui/open-webui/issues/32781), [Commit](https://github.com/open-webui/open-webui/commit/d5cd7f4907f9a6832dc5b52520a1381ef50a663c),
      [#32600](https://github.com/open-webui/open-webui/issues/32600)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: ♻️ **Prompt cache survives restarts.** Tools from tool servers, Open Terminal
      included, now reach the model in the same form after every restart, so the provider's
      prompt cache keeps working and long chats are no longer processed again from
      scratch. [#33000](https://github.com/open-webui/open-webui/pull/33000), [Commit](https://github.com/open-webui/open-webui/commit/ee7c9ff5c19d7d8c24c991028b08ff6672c6e653)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F321️ **Context gauge uses model threshold.** The context usage
      gauge now measures against the compaction threshold set on the model or in the
      default model parameters, the same one compaction uses, where it ignored a lower
      threshold on the model and showed a chat as far from compaction. [Commit](https://github.com/open-webui/open-webui/commit/c9415a688ea469144ab2a7796d5eef71947af0b8),
      [#32821](https://github.com/open-webui/open-webui/issues/32821)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-context-window-changes-in-v0-12-4
  source_release: open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79
  source_type: github_releases
  theme: context-window
  title: 4 Context Window changes in v0.12.4
  type: change
related_changes:
- '[[Changes/Dify/2026-10-23-3-context-window-changes-in-1-18-0|3 Context Window changes
  in 1.18.0]]'
- '[[Changes/Ollama/2026-10-23-nemotron-3-5-bolt-e4b-https-ollama-com-library-nemotron-3-5-bolt-is-nvidia-s-sma|Nemotron
  3.5 Bolt E4B((source link) is NVIDIA’s…]]'
- '[[Changes/OpenClaw/2026-10-24-4-context-window-changes-in-v2026-10-7|4 Context
  Window changes in v2026.10.7]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79]]'
source_type: github_releases
theme: context-window
title: 4 Context Window changes in v0.12.4
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Context Window changes in v0.12.4

**Open WebUI** · 2026-10-25 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.4) · from [[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|v0.12.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📍 **Compaction shown in chats.** A "Context compacted" line now marks the message where older messages were summarized, opens to show the summary and also appears inside a reply when compaction ran between its tool calls, Chat Controls > Overview tags that message, and compaction progress and errors now show in the chat instead of as pop-up notices. [Commit](https://github.com/open-webui/open-webui/commit/f465a4be11c0c64969da70f1f5b770bd21088b8a), [Commit](https://github.com/open-webui/open-webui/commit/c8786f426ad263ea4113652ed576d3c15ee341d6), [Commit](https://github.com/open-webui/open-webui/commit/3311f999928964ca1f7870fefb407553197dc2d5), [Commit](https://github.com/open-webui/open-webui/commit/3855acf02d44b78e7969599155896865fd362123), [#31324](https://github.com/open-webui/open-webui/issues/31324)

> 🗜️ **Compaction in more chats.** Context compaction now also runs in temporary chats and in short chats that are already over the threshold, such as one question with a reply full of tool output, so the follow-up and any regenerate or edit of it no longer fail with a context length error. [#32794](https://github.com/open-webui/open-webui/pull/32794), [Commit](https://github.com/open-webui/open-webui/commit/56eca192ab7d98dd9d1a9811e4452dc32145848d), [#32781](https://github.com/open-webui/open-webui/issues/32781), [Commit](https://github.com/open-webui/open-webui/commit/d5cd7f4907f9a6832dc5b52520a1381ef50a663c), [#32600](https://github.com/open-webui/open-webui/issues/32600)

> ♻️ **Prompt cache survives restarts.** Tools from tool servers, Open Terminal included, now reach the model in the same form after every restart, so the provider's prompt cache keeps working and long chats are no longer processed again from scratch. [#33000](https://github.com/open-webui/open-webui/pull/33000), [Commit](https://github.com/open-webui/open-webui/commit/ee7c9ff5c19d7d8c24c991028b08ff6672c6e653)

> 🌡️ **Context gauge uses model threshold.** The context usage gauge now measures against the compaction threshold set on the model or in the default model parameters, the same one compaction uses, where it ignored a lower threshold on the model and showed a chat as far from compaction. [Commit](https://github.com/open-webui/open-webui/commit/c9415a688ea469144ab2a7796d5eef71947af0b8), [#32821](https://github.com/open-webui/open-webui/issues/32821)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-25-16-model-support-changes-in-v0-12-4|16 Model Support changes in v0.12.4]] · Model Support
- [[Changes/Open WebUI/2026-10-25-10-safety-and-privacy-changes-in-v0-12-4|10 Safety and Privacy changes in v0.12.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-25-13-interface-experience-changes-in-v0-12-4|13 Interface Experience changes in v0.12.4]] · Interface Experience
- [[Changes/Open WebUI/2026-10-25-images-settings-save-admins-can-now-save-images-settings-while-image-generation|🖌️ Images settings save. Admins can now save Images settings while Image…]] · Image Generation
- [[Changes/Open WebUI/2026-10-25-4-voice-and-audio-changes-in-v0-12-4|4 Voice and Audio changes in v0.12.4]] · Voice and Audio
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
## Nearby in Context Window

- Earlier: 2026-10-24 · OpenClaw · [[Changes/OpenClaw/2026-10-24-4-context-window-changes-in-v2026-10-7|4 Context Window changes in v2026.10.7]]
- Later: 2026-10-26 · AnythingLLM · [[Changes/AnythingLLM/2026-10-26-2-context-window-changes-in-v1-19-0|2 Context Window changes in v1.19.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-25-6d6885&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-25-4-context-window-changes-in-v0-12-4.md%0ACard%20ID%3A%20open-webui-2026-10-25-6d6885%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->