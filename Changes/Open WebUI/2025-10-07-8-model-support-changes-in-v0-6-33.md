---
card_id: open-webui-2025-10-07-205d31
date: '2025-10-07'
description: "Open WebUI · 2025-10-07 · Model Support: 8 changes in v0.6.33 — \U0001F3A8
  Workspace interface received a comprehensive redesign across Models, Knowledge,
  Prompts, and…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1002
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 16d5e4b0d04ef4376ce73a5d1df758c8dbda413273b660938379b548733ba79b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-10-07-205d31
  comparison: ''
  date: '2025-10-07'
  description: 'Open WebUI — v0.6.33: 8 Model Support changes'
  evidence:
  - quote: "\U0001F3A8 Workspace interface received a comprehensive redesign across
      Models, Knowledge, Prompts, and Tools sections, featuring reorganized controls,
      view filters for created vs shared items, tag selectors, improved visual hierarchy,
      and streamlined import/export functionality. [Commit](https://github.com/open-webui/open-webui/commit/2c59a288603d8c5f004f223ee00fef37cc763a8e),
      [Commit](https://github.com/open-webui/open-webui/commit/6050c86ab6ef6b8c96dd3f99c62a6867011b67a4),
      [Commit](https://github.com/open-webui/open-webui/commit/96ecb47bc71c072aa34ef2be10781b042bef4e8c),
      [Commit](https://github.com/open-webui/open-webui/commit/2250d102b28075a9611696e911536547abb8b38a),
      [Commit](https://github.com/open-webui/open-webui/commit/23c8f6d507bfee75ab0015a3e2972d5c26f7e9bf),
      [Commit](https://github.com/open-webui/open-webui/commit/a743b16728c6ae24b8befbc2d7f24eb9e20c4ad5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F916 Ollama model management modal now features individual model
      update cancellation, comprehensive tooltips for all buttons, and streamlined
      notification behavior to reduce toast spam. [#16863](https://github.com/open-webui/open-webui/pull/16863)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F4C1 Folders now remember the last selected model, automatically
      applying it when starting new chats within that folder. [#17836](https://github.com/open-webui/open-webui/issues/17836)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F4AC System prompts are no longer duplicated in chat requests, eliminating
      confusion and excessive token usage caused by repeated instructions being sent
      to models. [#17198](https://github.com/open-webui/open-webui/issues/17198),
      [#16855](https://github.com/open-webui/open-webui/issues/16855)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F916 Reasoning models that return reasoning_content instead of content
      no longer cause NoneType errors during chat title generation, follow-up suggestions,
      and tag generation. [#18080](https://github.com/open-webui/open-webui/pull/18080)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F50D Model selector search now correctly returns results for non-admin
      users by dynamically updating the search index when the model list changes,
      fixing a race condition that caused empty search results. [#17996](https://github.com/open-webui/open-webui/pull/17996),
      [#17960](https://github.com/open-webui/open-webui/pull/17960)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F916 Text selection \"Ask\" action now correctly recognizes and
      uses local models configured via direct connections instead of only showing
      external provider models. [#17896](https://github.com/open-webui/open-webui/issues/17896)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  - quote: "\U0001F3A8 Workspace filter dropdown now correctly renders model tags
      as strings instead of displaying individual characters, fixing broken filtering
      interface when models have multiple tags. [#18034](https://github.com/open-webui/open-webui/issues/18034)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 8-model-support-changes-in-v0-6-33
  source_release: open-webui-2025-10-07-v0-6-33-github-252853067-e907999d
  source_type: github_releases
  theme: model-support
  title: 8 Model Support changes in v0.6.33
  type: change
related_changes:
- '[[Changes/Lovable/2025-10-06-lovable-ai|Lovable AI]]'
- '[[Changes/ElevenLabs/2025-10-07-new-llm-models|New LLM Models]]'
- '[[Changes/Gemini CLI/2025-10-07-5-model-support-changes-in-v0-8-0|5 Model Support
  changes in v0.8.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-10-07-v0-6-33-github-252853067-e907999d|open-webui-2025-10-07-v0-6-33-github-252853067-e907999d]]'
source_type: github_releases
theme: model-support
title: 8 Model Support changes in v0.6.33
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Model Support changes in v0.6.33

**Open WebUI** · 2025-10-07 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.33) · from [[Releases/Open WebUI/open-webui-2025-10-07-v0-6-33-github-252853067-e907999d|v0.6.33]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎨 Workspace interface received a comprehensive redesign across Models, Knowledge, Prompts, and Tools sections, featuring reorganized controls, view filters for created vs shared items, tag selectors, improved visual hierarchy, and streamlined import/export functionality. [Commit](https://github.com/open-webui/open-webui/commit/2c59a288603d8c5f004f223ee00fef37cc763a8e), [Commit](https://github.com/open-webui/open-webui/commit/6050c86ab6ef6b8c96dd3f99c62a6867011b67a4), [Commit](https://github.com/open-webui/open-webui/commit/96ecb47bc71c072aa34ef2be10781b042bef4e8c), [Commit](https://github.com/open-webui/open-webui/commit/2250d102b28075a9611696e911536547abb8b38a), [Commit](https://github.com/open-webui/open-webui/commit/23c8f6d507bfee75ab0015a3e2972d5c26f7e9bf), [Commit](https://github.com/open-webui/open-webui/commit/a743b16728c6ae24b8befbc2d7f24eb9e20c4ad5)

> 🤖 Ollama model management modal now features individual model update cancellation, comprehensive tooltips for all buttons, and streamlined notification behavior to reduce toast spam. [#16863](https://github.com/open-webui/open-webui/pull/16863)

> 📁 Folders now remember the last selected model, automatically applying it when starting new chats within that folder. [#17836](https://github.com/open-webui/open-webui/issues/17836)

> 💬 System prompts are no longer duplicated in chat requests, eliminating confusion and excessive token usage caused by repeated instructions being sent to models. [#17198](https://github.com/open-webui/open-webui/issues/17198), [#16855](https://github.com/open-webui/open-webui/issues/16855)

> 🤖 Reasoning models that return reasoning_content instead of content no longer cause NoneType errors during chat title generation, follow-up suggestions, and tag generation. [#18080](https://github.com/open-webui/open-webui/pull/18080)

> 🔍 Model selector search now correctly returns results for non-admin users by dynamically updating the search index when the model list changes, fixing a race condition that caused empty search results. [#17996](https://github.com/open-webui/open-webui/pull/17996), [#17960](https://github.com/open-webui/open-webui/pull/17960)

> 🤖 Text selection "Ask" action now correctly recognizes and uses local models configured via direct connections instead of only showing external provider models. [#17896](https://github.com/open-webui/open-webui/issues/17896)

> 🎨 Workspace filter dropdown now correctly renders model tags as strings instead of displaying individual characters, fixing broken filtering interface when models have multiple tags. [#18034](https://github.com/open-webui/open-webui/issues/18034)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.33
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-10-07-10-account-and-access-changes-in-v0-6-33|10 Account and Access changes in v0.6.33]] · Account and Access
- [[Changes/Open WebUI/2025-10-07-2-files-and-data-changes-in-v0-6-33|2 Files and Data changes in v0.6.33]] · Files and Data
- [[Changes/Open WebUI/2025-10-07-tab-characters-are-now-preserved-when-pasting-code-or-formatted-text-into-the-ch|⌨️ Tab characters are now preserved when pasting code or formatted text…]] · Editor Experience
- [[Changes/Open WebUI/2025-10-07-2-search-and-browsing-changes-in-v0-6-33|2 Search and Browsing changes in v0.6.33]] · Search and Browsing
- [[Changes/Open WebUI/2025-10-07-6-reliability-and-performance-changes-in-v0-6-33|6 Reliability and Performance changes in v0.6.33]] · Reliability and Performance
- [[Changes/Open WebUI/2025-10-07-redis-session-storage-is-now-available-as-an-experimental-option-for-oauth-authe|🗄️ Redis session storage is now available as an experimental option for OAuth…]] · Account and Access
- [[Changes/Open WebUI/2025-10-07-8-interface-experience-changes-in-v0-6-33|8 Interface Experience changes in v0.6.33]] · Interface Experience
- [[Changes/Open WebUI/2025-10-07-azure-text-to-speech-now-properly-escapes-special-characters-like-ampersands-in|🔊 Azure Text-to-Speech now properly escapes special characters like ampersands…]] · Voice and Audio
- [[Changes/Open WebUI/2025-10-07-3-developer-workflow-changes-in-v0-6-33|3 Developer Workflow changes in v0.6.33]] · Developer Workflow
- [[Changes/Open WebUI/2025-10-07-3-apps-and-integrations-changes-in-v0-6-33|3 Apps and Integrations changes in v0.6.33]] · Apps and Integrations
- [[Changes/Open WebUI/2025-10-07-13-other-changes-in-v0-6-33|13 other changes in v0.6.33]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-10-07 · Gemini CLI · [[Changes/Gemini CLI/2025-10-07-5-model-support-changes-in-v0-8-0|5 Model Support changes in v0.8.0]]
- Later: 2025-10-08 · Cline · [[Changes/Cline/2025-10-08-update-local-models-docs-remove-emojis-from-docs-by-nickbaumann98-in-https-githu|Update local models docs & remove emojis from Docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-10-07-205d31&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-10-07-8-model-support-changes-in-v0-6-33.md%0ACard%20ID%3A%20open-webui-2025-10-07-205d31%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.33%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->