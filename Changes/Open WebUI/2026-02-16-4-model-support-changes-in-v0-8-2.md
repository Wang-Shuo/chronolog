---
card_id: open-webui-2026-02-16-6d52d2
date: '2026-02-16'
description: "Open WebUI · 2026-02-16 · Model Support: 4 changes in v0.8.2 — \U0001F9E0
  **Skill content handling.** User-selected skills now have their full content injected
  into the…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1134
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3ddc43f1246aeeb165f00707403c9d7d032a1b0bb801906daa06985301abf2b7
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-16-6d52d2
  comparison: ''
  date: '2026-02-16'
  description: 'Open WebUI — v0.8.2: 4 Model Support changes'
  evidence:
  - quote: "\U0001F9E0 **Skill content handling.** User-selected skills now have their
      full content injected into the chat, while model-attached skills only display
      name and description in the available skills list. This allows users to override
      skill behavior while model-attached skills remain flexible. [Commit](https://github.com/open-webui/open-webui/commit/393c0071dc612c5ac982fb37dfc0288cb9911439)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.2
  - quote: "\U0001F41B **Task model selector validation.** The task model selector
      in admin settings now correctly accepts models based on the new access grants
      system instead of rejecting all models with an incorrect error. [Commit](https://github.com/open-webui/open-webui/commit/9a2595f0706d0c9d809ae7746001cf799f98db1d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.2
  - quote: "\U0001F517 **Tool call message preservation.** Models no longer hallucinate
      tool outputs in multi-turn conversations because tool call history is now properly
      preserved instead of being merged into assistant messages. [#21098](https://github.com/open-webui/open-webui/discussions/21098),
      [#20600](https://github.com/open-webui/open-webui/issues/20600), [Commit](https://github.com/open-webui/open-webui/commit/f2aca781c87244cffc130aa2722e700c19a81d66)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.2
  - quote: "\U0001F527 **Tool call finish_reason fix.** API responses now correctly
      set finish_reason to \"tool_calls\" instead of \"stop\" when tool calls are
      present, fixing an issue where external API clients (such as OpenCode) would
      halt prematurely after tool execution when routing Ollama models through the
      Open WebUI API. [#20896](https://github.com/open-webui/open-webui/issues/20896)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-model-support-changes-in-v0-8-2
  source_release: open-webui-2026-02-16-v0-8-2-github-286715828-a462c4be
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in v0.8.2
  type: change
related_changes:
- '[[Changes/OpenCode/2026-02-15-2-model-support-changes-in-v1-2-5-1|2 Model Support
  changes in v1.2.5 + 1]]'
- '[[Changes/ElevenLabs/2026-02-16-new-schemas|New Schemas]]'
- '[[Changes/Midjourney/2026-02-16-your-ratings-are-already-helping-the-v8-model-and-we-really-appreciate-your-time|Your
  ratings are already helping the V8 model and we really appreciate your time…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-16-v0-8-2-github-286715828-a462c4be|open-webui-2026-02-16-v0-8-2-github-286715828-a462c4be]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in v0.8.2
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v0.8.2

**Open WebUI** · 2026-02-16 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.2) · from [[Releases/Open WebUI/open-webui-2026-02-16-v0-8-2-github-286715828-a462c4be|v0.8.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧠 **Skill content handling.** User-selected skills now have their full content injected into the chat, while model-attached skills only display name and description in the available skills list. This allows users to override skill behavior while model-attached skills remain flexible. [Commit](https://github.com/open-webui/open-webui/commit/393c0071dc612c5ac982fb37dfc0288cb9911439)

> 🐛 **Task model selector validation.** The task model selector in admin settings now correctly accepts models based on the new access grants system instead of rejecting all models with an incorrect error. [Commit](https://github.com/open-webui/open-webui/commit/9a2595f0706d0c9d809ae7746001cf799f98db1d)

> 🔗 **Tool call message preservation.** Models no longer hallucinate tool outputs in multi-turn conversations because tool call history is now properly preserved instead of being merged into assistant messages. [#21098](https://github.com/open-webui/open-webui/discussions/21098), [#20600](https://github.com/open-webui/open-webui/issues/20600), [Commit](https://github.com/open-webui/open-webui/commit/f2aca781c87244cffc130aa2722e700c19a81d66)

> 🔧 **Tool call finish_reason fix.** API responses now correctly set finish_reason to "tool_calls" instead of "stop" when tool calls are present, fixing an issue where external API clients (such as OpenCode) would halt prematurely after tool execution when routing Ollama models through the Open WebUI API. [#20896](https://github.com/open-webui/open-webui/issues/20896)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-16-resource-handle-cleanup-file-handles-are-now-properly-closed-during-audio-transc|♻️ Resource handle cleanup. File handles are now properly closed during audio…]] · Voice and Audio
- [[Changes/Open WebUI/2026-02-16-chat-toggles-now-control-built-in-tools-users-can-now-disable-web-search-image-g|⚙️ Chat toggles now control built-in tools. Users can now disable web search…]] · Image Generation
- [[Changes/Open WebUI/2026-02-16-long-content-truncation-in-preview-modals-citation-and-file-content-modals-now-t|⚡ Long content truncation in preview modals. Citation and file content modals…]] · Files and Data
- [[Changes/Open WebUI/2026-02-16-skills-sharing-permissions-administrators-can-now-control-skills-sharing-and-pub|🔐 Skills sharing permissions. Administrators can now control skills sharing…]] · Collaboration
- [[Changes/Open WebUI/2026-02-16-strikethrough-shortcut-conflict-fix-pressing-ctrl-shift-s-to-toggle-the-sidebar|⌨️ Strikethrough shortcut conflict fix. Pressing Ctrl+Shift+S to toggle…]] · Interface Experience
- [[Changes/Open WebUI/2026-02-16-4-developer-workflow-changes-in-v0-8-2|4 Developer Workflow changes in v0.8.2]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-16-oauth-session-error-handling-corrupted-oauth-sessions-are-now-gracefully-handled|🔐 OAuth session error handling. Corrupted OAuth sessions are now gracefully…]] · Account and Access
- [[Changes/Open WebUI/2026-02-16-translation-updates-translations-for-spanish-and-german-were-enhanced-and-expand|🌐 Translation updates. Translations for Spanish and German were enhanced and expanded]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-02-16 · Midjourney · [[Changes/Midjourney/2026-02-16-your-ratings-are-already-helping-the-v8-model-and-we-really-appreciate-your-time|Your ratings are already helping the V8 model and we really appreciate your time…]]
- Later: 2026-02-16 · OpenCode · [[Changes/OpenCode/2026-02-16-core-remove-unnecessary-per-message-title-llm-calls|Core Remove unnecessary per-message title LLM calls]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-16-6d52d2&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-16-4-model-support-changes-in-v0-8-2.md%0ACard%20ID%3A%20open-webui-2026-02-16-6d52d2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->