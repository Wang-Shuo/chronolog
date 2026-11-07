---
card_id: open-webui-2026-07-01-9ca58f
date: '2026-07-01'
description: "Open WebUI · 2026-07-01 · Model Support: 5 changes in v0.10.2 — \U0001F4AD
  **Streamed reasoning display.** Models that emit thinking or reasoning now show
  that content…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1269
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1a845c1cb30f0d3021ad59772ac412855ffaca3d742d7dc0ba61813c4fdb5188
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-01-9ca58f
  comparison: ''
  date: '2026-07-01'
  description: 'Open WebUI — v0.10.2: 5 Model Support changes'
  evidence:
  - quote: "\U0001F4AD **Streamed reasoning display.** Models that emit thinking or
      reasoning now show that content as it streams, and it renders correctly in the
      chat overview and in exported conversations. [Commit](https://github.com/open-webui/open-webui/commit/0b75445ff9a42e37640c034812d0de9b84039e60),
      [Commit](https://github.com/open-webui/open-webui/commit/af1c0eee89810fa4c36e3eb7e4eba6de685bd7ca),
      [Commit](https://github.com/open-webui/open-webui/commit/4b08d65597e5b634b7191b0bd6d28feeafcc2a48),
      [Commit](https://github.com/open-webui/open-webui/commit/fa2abe4cb6a085a4c9045bf8d8ff4b6beffdef6a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
  - quote: "\U0001F3DF️ **Arena models via environment.** Administrators can now define
      evaluation arena models through the \"EVALUATION_ARENA_MODELS\" environment
      variable. [#26174](https://github.com/open-webui/open-webui/issues/26174)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
  - quote: ⚙️ **Saving settings as a non-admin.** Non-admin users can once again save
      their interface settings, such as the default model and theme, which previously
      failed with a server error while the interface incorrectly reported success.
      [#26627](https://github.com/open-webui/open-webui/issues/26627), [Commit](https://github.com/open-webui/open-webui/commit/9866a02863c12c466100aed832f0006225759493)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
  - quote: "\U0001F3AF **Default model after refresh.** Your selected model is no
      longer cleared when you reload the page, as model selection now waits for the
      model list to finish loading. [Commit](https://github.com/open-webui/open-webui/commit/b6d4baeb7ea9bc83e5486ca98b3cae07d3869aa7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
  - quote: "\U0001F9EC **Editing derived models.** Editing a workspace model no longer
      clears its base model, including when that base is a preset or the model itself.
      [Commit](https://github.com/open-webui/open-webui/commit/092b5857bbda01be53619e26f42b1fa9b64a2b44),
      [Commit](https://github.com/open-webui/open-webui/commit/54f31c630afa75e9c81acaa048e1bd901254ba92)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-model-support-changes-in-v0-10-2
  source_release: open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in v0.10.2
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-01-add-support-for-the-kimi-k2-7-code-model|Add
  support for the kimi-k2.7-code model]]'
- '[[Changes/Kimi Code/2026-07-01-merge-consecutive-user-turns-for-strict-providers-gemini-vertex-fixing-an-http-4|Merge
  consecutive user turns for strict providers (Gemini/Vertex), fixing an HTTP…]]'
- '[[Changes/Notion/2026-07-01-more-models-without-the-lock-in|More models, without
  the lock-in]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f|open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in v0.10.2
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in v0.10.2

**Open WebUI** · 2026-07-01 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.2) · from [[Releases/Open WebUI/open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f|v0.10.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 💭 **Streamed reasoning display.** Models that emit thinking or reasoning now show that content as it streams, and it renders correctly in the chat overview and in exported conversations. [Commit](https://github.com/open-webui/open-webui/commit/0b75445ff9a42e37640c034812d0de9b84039e60), [Commit](https://github.com/open-webui/open-webui/commit/af1c0eee89810fa4c36e3eb7e4eba6de685bd7ca), [Commit](https://github.com/open-webui/open-webui/commit/4b08d65597e5b634b7191b0bd6d28feeafcc2a48), [Commit](https://github.com/open-webui/open-webui/commit/fa2abe4cb6a085a4c9045bf8d8ff4b6beffdef6a)

> 🏟️ **Arena models via environment.** Administrators can now define evaluation arena models through the "EVALUATION_ARENA_MODELS" environment variable. [#26174](https://github.com/open-webui/open-webui/issues/26174)

> ⚙️ **Saving settings as a non-admin.** Non-admin users can once again save their interface settings, such as the default model and theme, which previously failed with a server error while the interface incorrectly reported success. [#26627](https://github.com/open-webui/open-webui/issues/26627), [Commit](https://github.com/open-webui/open-webui/commit/9866a02863c12c466100aed832f0006225759493)

> 🎯 **Default model after refresh.** Your selected model is no longer cleared when you reload the page, as model selection now waits for the model list to finish loading. [Commit](https://github.com/open-webui/open-webui/commit/b6d4baeb7ea9bc83e5486ca98b3cae07d3869aa7)

> 🧬 **Editing derived models.** Editing a workspace model no longer clears its base model, including when that base is a preset or the model itself. [Commit](https://github.com/open-webui/open-webui/commit/092b5857bbda01be53619e26f42b1fa9b64a2b44), [Commit](https://github.com/open-webui/open-webui/commit/54f31c630afa75e9c81acaa048e1bd901254ba92)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-01-speech-to-text-request-format-openai-compatible-speech-to-text-can-now-send-audi|🎙️ Speech-to-text request format. OpenAI-compatible speech-to-text can now send…]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-01-web-search-domain-filtering-domain-allow-and-block-rules-for-web-search-results|🔒 Web search domain filtering. Domain allow and block rules for web search…]] · Search and Browsing
- [[Changes/Open WebUI/2026-07-01-2-interface-experience-changes-in-v0-10-2|2 Interface Experience changes in v0.10.2]] · Interface Experience
- [[Changes/Open WebUI/2026-07-01-2-memory-and-personalization-changes-in-v0-10-2|2 Memory and Personalization changes in v0.10.2]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-01-models-with-null-capabilities-chatting-with-a-model-whose-capabilities-are-unset|🤖 Models with null capabilities. Chatting with a model whose capabilities…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-01-5-developer-workflow-changes-in-v0-10-2|5 Developer Workflow changes in v0.10.2]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-01-2-editor-experience-changes-in-v0-10-2|2 Editor Experience changes in v0.10.2]] · Editor Experience
- [[Changes/Open WebUI/2026-07-01-2-account-and-access-changes-in-v0-10-2|2 Account and Access changes in v0.10.2]] · Account and Access
- [[Changes/Open WebUI/2026-07-01-3-safety-and-privacy-changes-in-v0-10-2|3 Safety and Privacy changes in v0.10.2]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-01-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-07-01-2-other-changes-in-v0-10-2|2 other changes in v0.10.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-07-01 · Notion · [[Changes/Notion/2026-07-01-more-models-without-the-lock-in|More models, without the lock-in]]
- Later: 2026-07-01 · OpenCode · [[Changes/OpenCode/2026-07-01-core-force-reasoning-mode-for-openai-compatible-reasoning-models-so-reasoning-se|Core Force reasoning mode for OpenAI-compatible reasoning models so reasoning…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-01-9ca58f&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-01-5-model-support-changes-in-v0-10-2.md%0ACard%20ID%3A%20open-webui-2026-07-01-9ca58f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->