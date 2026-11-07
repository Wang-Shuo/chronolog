---
card_id: open-webui-2026-03-25-e28891
date: '2026-03-25'
description: "Open WebUI · 2026-03-25 · Model Support: 23 changes in v0.8.11 — \U0001F500
  **Responses API streaming improvements.** The OpenAI proxy now properly handles
  tool call…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1171
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5276cdaa16a3a0d254de84f232165b101781abb0172063f9e256216bf1f97bcc
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-25-e28891
  comparison: ''
  date: '2026-03-25'
  description: 'Open WebUI — v0.8.11: 23 Model Support changes'
  evidence:
  - quote: "\U0001F500 **Responses API streaming improvements.** The OpenAI proxy
      now properly handles tool call streaming and re-invocations in the Responses
      API, preventing duplicate tool calls and preserving output during model re-invocations.
      [Commit](https://github.com/open-webui/open-webui/commit/93415a48e8893139db13d02d0a6d24e8604a2ac5),
      [Commit](https://github.com/open-webui/open-webui/commit/f8b3a32caf00dad76687fd8fe698b86f304f3997),
      [Commit](https://github.com/open-webui/open-webui/commit/2ae47cf20057e92a83fd618b938f3ee9bb124e5b),
      [Commit](https://github.com/open-webui/open-webui/commit/adcbba34f8bbfbab3e4041269a084f2b71c076d9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4C4 **File viewing pagination.** The view_file and view_knowledge_file
      tools now support pagination with offset and max_chars parameters, allowing
      models to read large files in chunks. [Commit](https://github.com/open-webui/open-webui/commit/5d7766e1b6f7ca7749c5a5a780d7b1bb2da28a2f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F5FA️ **Knowledge search scoping.** The search_knowledge_files tool
      now respects model-attached knowledge, searching only within attached knowledge
      bases and files when available. [Commit](https://github.com/open-webui/open-webui/commit/0f0ba7dadd043460d205477fd3b57556aa970847)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4A8 **Chat render throttling.** Chat message rendering now uses
      requestAnimationFrame batching to stay smooth during rapid model responses,
      preventing dropped frames when fast models send many events per second. [#22947](https://github.com/open-webui/open-webui/pull/22947)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F354 **Model bulk actions menu.** Users can now quickly enable,
      disable, show, or hide multiple models at once using a new hamburger menu on
      the workspace Models page filter bar, with actions respecting the current search
      and filter settings. [#22484](https://github.com/open-webui/open-webui/pull/22484)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4DD **Writing block rendering.** Responses from OpenAI models that
      include :::writing blocks are now rendered as formatted content in a styled
      container with a copy button, instead of displaying raw marker text. [#22672](https://github.com/open-webui/open-webui/issues/22672),
      [Commit](https://github.com/open-webui/open-webui/commit/53b8a1f71bd0cb0a0122175ad5210da492018728)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4D3 **Multi-artifact HTML rendering.** Code blocks with multiple
      HTML sections now render as separate artifacts instead of merging into one,
      allowing models to display distinct interactive components. [Commit](https://github.com/open-webui/open-webui/commit/9a6bf78e14a13864e72db87426da4f5996abe716)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F36A **Model list auth cookie forwarding.** Model list requests
      to backends that require cookie-based authentication now properly forward auth
      headers and cookies, preventing \"Unauthorized\" errors when loading models.
      [Commit](https://github.com/open-webui/open-webui/commit/76ece4049e96bd6890593f17a946a9af6b082fab)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F531 **Model lookup race condition.** Fixed a race condition in
      Redis model storage that caused intermittent \"model not found\" errors in multi-replica
      deployments under heavy load, by eliminating the window between hash deletion
      and updates. [Commit](https://github.com/open-webui/open-webui/commit/ee901fcd2ca82d7a7dad48170c64df782d3e040a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F39A️ **Bulk model action reliability.** Bulk enable, disable, show,
      and hide operations in the admin Models settings now properly refresh the model
      list after completion, ensuring changes are reflected immediately and correct
      toast notifications are shown. [#22962](https://github.com/open-webui/open-webui/pull/22962),
      [Commit](https://github.com/open-webui/open-webui/commit/75932be880f3b86f78f00b4352b9f1350b8f53fa),
      [Commit](https://github.com/open-webui/open-webui/commit/15ae3f588b1aa4ddb686ae68afebd6064036a201)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001FA9B **Function list API crash fix.** Fixed a 500 error on the functions
      list API endpoint that was introduced by the recent optimization, by adding
      proper model configuration for SQLAlchemy ORM objects. [#22924](https://github.com/open-webui/open-webui/pull/22924)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F3F7️ **Channel @mentions.** Direct connection models no longer
      appear in channel @mention suggestions, preventing confusion since they don't
      work in channels. [#22553](https://github.com/open-webui/open-webui/issues/22553),
      [Commit](https://github.com/open-webui/open-webui/commit/0a87c1ecd078320a08c4cc62d41fe8727fb3b5f7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F5E3️ **Image-only message handling.** Models like Gemini and Claude
      no longer fail when receiving messages with only file or image attachments and
      no text, by stripping empty text content blocks before sending to the API. [Commit](https://github.com/open-webui/open-webui/commit/ea515fa26e11faac146c48a5e3a2a284e1792bb3),
      [#22880](https://github.com/open-webui/open-webui/issues/22880)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4AC **Skill and model mention persistence.** Skills selected via
      $ and models selected via @ in the chat input are now properly restored after
      a page refresh, instead of reverting to plain text while losing their interactive
      state. [#22913](https://github.com/open-webui/open-webui/issues/22913), [Commit](https://github.com/open-webui/open-webui/commit/be21db706993c0db95ac09509dfdb023de64daff)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F517 **Multi-system message merging.** Models with strict chat templates
      like Qwen no longer fail when multiple pipeline stages inject separate system
      messages, as all system messages are now merged into one at the start. [#22505](https://github.com/open-webui/open-webui/issues/22505),
      [Commit](https://github.com/open-webui/open-webui/commit/631bd20c3537ce85bbaec02f9e0049c88fa8fdd4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F527 **Model list drag-and-drop.** Fixed drag-and-drop reordering
      of models in admin settings, preventing UI glitches and state synchronization
      issues. [Commit](https://github.com/open-webui/open-webui/commit/753589e51ccbbe5c4f78a7d13e19c67e6c0000d7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F5BC️ **Model profile image fallbacks.** Model profile images now
      display a fallback icon when they fail to load, and model icons no longer disappear
      on paginated Models pages in admin and workspace settings. [#22485](https://github.com/open-webui/open-webui/pull/22485)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F5BC️ **Profile image fallbacks.** Added fallback handlers for model
      and user profile images throughout the chat interface, preventing broken image
      icons when avatars fail to load. [#22486](https://github.com/open-webui/open-webui/pull/22486)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F9F2 **RAG thinking model support.** Knowledge base queries now
      correctly parse JSON responses from thinking models like GLM-5 and DeepSeek-R1
      by stripping their reasoning blocks before JSON extraction. [#22400](https://github.com/open-webui/open-webui/pull/22400)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F504 **Ollama embedding retry logic.** Embedding requests to Ollama
      now retry with exponential backoff when encountering 503 errors (such as when
      the model reloads mid-processing), preventing files from being silently dropped
      from knowledge bases. [#22571](https://github.com/open-webui/open-webui/issues/22571),
      [Commit](https://github.com/open-webui/open-webui/commit/8b6fa1f4ab6099a305de08706621075c205f65c4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F4CA **Model tag normalization.** Model tags from backends that
      return them as string arrays are now properly normalized to object format, preventing
      crashes when filtering models by tag in the admin and workspace models pages.
      [#20819](https://github.com/open-webui/open-webui/issues/20819), [Commit](https://github.com/open-webui/open-webui/commit/90ca2e9b0f15cc9be7cf298fbefacaa45074cae9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F3AF **Arena model sub-model settings.** Arena models now properly
      use the selected sub-model's settings — including RAG knowledge bases, web access,
      code interpreter, and tool capabilities — instead of the arena wrapper's empty
      defaults. [#16950](https://github.com/open-webui/open-webui/issues/16950), [Commit](https://github.com/open-webui/open-webui/commit/857d7e6f373d26a7a8989417c3a7fe99cdc03f20)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  - quote: "\U0001F9E9 **Model editor default metadata.** The Model Editor now loads
      admin-configured default model metadata instead of hardcoded values, preventing
      admin defaults from being silently overwritten when users save models without
      realizing they were overriding system-wide settings. [#22996](https://github.com/open-webui/open-webui/issues/22996),
      [Commit](https://github.com/open-webui/open-webui/commit/cdc2b3bf850044051aafcd46f22fb25a1899788c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 23-model-support-changes-in-v0-8-11
  source_release: open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69
  source_type: github_releases
  theme: model-support
  title: 23 Model Support changes in v0.8.11
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-03-24-7-model-support-changes-in-v0-35-0|7 Model Support
  changes in v0.35.0]]'
- '[[Changes/Google Antigravity/2026-03-25-added-support-for-reading-rules-from-agents-md-in-addition-to-gemini-md|Added
  support for reading rules from AGENTS.md in addition to GEMINI.md]]'
- '[[Changes/Ollama/2026-03-25-if-you-have-ollama-installed-any-local-or-cloud-model-from-ollama-can-be-selecte|If
  you have Ollama installed, any local or cloud model from Ollama can be selected…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69]]'
source_type: github_releases
theme: model-support
title: 23 Model Support changes in v0.8.11
type: change
---

<!-- chronolog:begin region="header" -->
# 23 Model Support changes in v0.8.11

**Open WebUI** · 2026-03-25 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.11) · from [[Releases/Open WebUI/open-webui-2026-03-25-v0-8-11-github-301478856-55ceba69|v0.8.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔀 **Responses API streaming improvements.** The OpenAI proxy now properly handles tool call streaming and re-invocations in the Responses API, preventing duplicate tool calls and preserving output during model re-invocations. [Commit](https://github.com/open-webui/open-webui/commit/93415a48e8893139db13d02d0a6d24e8604a2ac5), [Commit](https://github.com/open-webui/open-webui/commit/f8b3a32caf00dad76687fd8fe698b86f304f3997), [Commit](https://github.com/open-webui/open-webui/commit/2ae47cf20057e92a83fd618b938f3ee9bb124e5b), [Commit](https://github.com/open-webui/open-webui/commit/adcbba34f8bbfbab3e4041269a084f2b71c076d9)

> 📄 **File viewing pagination.** The view_file and view_knowledge_file tools now support pagination with offset and max_chars parameters, allowing models to read large files in chunks. [Commit](https://github.com/open-webui/open-webui/commit/5d7766e1b6f7ca7749c5a5a780d7b1bb2da28a2f)

> 🗺️ **Knowledge search scoping.** The search_knowledge_files tool now respects model-attached knowledge, searching only within attached knowledge bases and files when available. [Commit](https://github.com/open-webui/open-webui/commit/0f0ba7dadd043460d205477fd3b57556aa970847)

> 💨 **Chat render throttling.** Chat message rendering now uses requestAnimationFrame batching to stay smooth during rapid model responses, preventing dropped frames when fast models send many events per second. [#22947](https://github.com/open-webui/open-webui/pull/22947)

> 🍔 **Model bulk actions menu.** Users can now quickly enable, disable, show, or hide multiple models at once using a new hamburger menu on the workspace Models page filter bar, with actions respecting the current search and filter settings. [#22484](https://github.com/open-webui/open-webui/pull/22484)

> 📝 **Writing block rendering.** Responses from OpenAI models that include :::writing blocks are now rendered as formatted content in a styled container with a copy button, instead of displaying raw marker text. [#22672](https://github.com/open-webui/open-webui/issues/22672), [Commit](https://github.com/open-webui/open-webui/commit/53b8a1f71bd0cb0a0122175ad5210da492018728)

> 📓 **Multi-artifact HTML rendering.** Code blocks with multiple HTML sections now render as separate artifacts instead of merging into one, allowing models to display distinct interactive components. [Commit](https://github.com/open-webui/open-webui/commit/9a6bf78e14a13864e72db87426da4f5996abe716)

> 🍪 **Model list auth cookie forwarding.** Model list requests to backends that require cookie-based authentication now properly forward auth headers and cookies, preventing "Unauthorized" errors when loading models. [Commit](https://github.com/open-webui/open-webui/commit/76ece4049e96bd6890593f17a946a9af6b082fab)

> 🔱 **Model lookup race condition.** Fixed a race condition in Redis model storage that caused intermittent "model not found" errors in multi-replica deployments under heavy load, by eliminating the window between hash deletion and updates. [Commit](https://github.com/open-webui/open-webui/commit/ee901fcd2ca82d7a7dad48170c64df782d3e040a)

> 🎚️ **Bulk model action reliability.** Bulk enable, disable, show, and hide operations in the admin Models settings now properly refresh the model list after completion, ensuring changes are reflected immediately and correct toast notifications are shown. [#22962](https://github.com/open-webui/open-webui/pull/22962), [Commit](https://github.com/open-webui/open-webui/commit/75932be880f3b86f78f00b4352b9f1350b8f53fa), [Commit](https://github.com/open-webui/open-webui/commit/15ae3f588b1aa4ddb686ae68afebd6064036a201)

> 🪛 **Function list API crash fix.** Fixed a 500 error on the functions list API endpoint that was introduced by the recent optimization, by adding proper model configuration for SQLAlchemy ORM objects. [#22924](https://github.com/open-webui/open-webui/pull/22924)

> 🏷️ **Channel @mentions.** Direct connection models no longer appear in channel @mention suggestions, preventing confusion since they don't work in channels. [#22553](https://github.com/open-webui/open-webui/issues/22553), [Commit](https://github.com/open-webui/open-webui/commit/0a87c1ecd078320a08c4cc62d41fe8727fb3b5f7)

> 🗣️ **Image-only message handling.** Models like Gemini and Claude no longer fail when receiving messages with only file or image attachments and no text, by stripping empty text content blocks before sending to the API. [Commit](https://github.com/open-webui/open-webui/commit/ea515fa26e11faac146c48a5e3a2a284e1792bb3), [#22880](https://github.com/open-webui/open-webui/issues/22880)

> 💬 **Skill and model mention persistence.** Skills selected via $ and models selected via @ in the chat input are now properly restored after a page refresh, instead of reverting to plain text while losing their interactive state. [#22913](https://github.com/open-webui/open-webui/issues/22913), [Commit](https://github.com/open-webui/open-webui/commit/be21db706993c0db95ac09509dfdb023de64daff)

> 🔗 **Multi-system message merging.** Models with strict chat templates like Qwen no longer fail when multiple pipeline stages inject separate system messages, as all system messages are now merged into one at the start. [#22505](https://github.com/open-webui/open-webui/issues/22505), [Commit](https://github.com/open-webui/open-webui/commit/631bd20c3537ce85bbaec02f9e0049c88fa8fdd4)

> 🔧 **Model list drag-and-drop.** Fixed drag-and-drop reordering of models in admin settings, preventing UI glitches and state synchronization issues. [Commit](https://github.com/open-webui/open-webui/commit/753589e51ccbbe5c4f78a7d13e19c67e6c0000d7)

> 🖼️ **Model profile image fallbacks.** Model profile images now display a fallback icon when they fail to load, and model icons no longer disappear on paginated Models pages in admin and workspace settings. [#22485](https://github.com/open-webui/open-webui/pull/22485)

> 🖼️ **Profile image fallbacks.** Added fallback handlers for model and user profile images throughout the chat interface, preventing broken image icons when avatars fail to load. [#22486](https://github.com/open-webui/open-webui/pull/22486)

> 🧲 **RAG thinking model support.** Knowledge base queries now correctly parse JSON responses from thinking models like GLM-5 and DeepSeek-R1 by stripping their reasoning blocks before JSON extraction. [#22400](https://github.com/open-webui/open-webui/pull/22400)

> 🔄 **Ollama embedding retry logic.** Embedding requests to Ollama now retry with exponential backoff when encountering 503 errors (such as when the model reloads mid-processing), preventing files from being silently dropped from knowledge bases. [#22571](https://github.com/open-webui/open-webui/issues/22571), [Commit](https://github.com/open-webui/open-webui/commit/8b6fa1f4ab6099a305de08706621075c205f65c4)

> 📊 **Model tag normalization.** Model tags from backends that return them as string arrays are now properly normalized to object format, preventing crashes when filtering models by tag in the admin and workspace models pages. [#20819](https://github.com/open-webui/open-webui/issues/20819), [Commit](https://github.com/open-webui/open-webui/commit/90ca2e9b0f15cc9be7cf298fbefacaa45074cae9)

> 🎯 **Arena model sub-model settings.** Arena models now properly use the selected sub-model's settings — including RAG knowledge bases, web access, code interpreter, and tool capabilities — instead of the arena wrapper's empty defaults. [#16950](https://github.com/open-webui/open-webui/issues/16950), [Commit](https://github.com/open-webui/open-webui/commit/857d7e6f373d26a7a8989417c3a7fe99cdc03f20)

> 🧩 **Model editor default metadata.** The Model Editor now loads admin-configured default model metadata instead of hardcoded values, preventing admin defaults from being silently overwritten when users save models without realizing they were overriding system-wide settings. [#22996](https://github.com/open-webui/open-webui/issues/22996), [Commit](https://github.com/open-webui/open-webui/commit/cdc2b3bf850044051aafcd46f22fb25a1899788c)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-25-4-editor-experience-changes-in-v0-8-11|4 Editor Experience changes in v0.8.11]] · Editor Experience
- [[Changes/Open WebUI/2026-03-25-rag-query-generation-robustness-the-rag-query-generation-web-search-and-image-ge|🔍 RAG query generation robustness. The RAG query generation, web search…]] · Image Generation
- [[Changes/Open WebUI/2026-03-25-shared-chat-viewing-crash-shared-chats-can-now-be-viewed-by-unauthenticated-user|🐛 Shared chat viewing crash. Shared chats can now be viewed by unauthenticated…]] · Collaboration
- [[Changes/Open WebUI/2026-03-25-11-account-and-access-changes-in-v0-8-11|11 Account and Access changes in v0.8.11]] · Account and Access
- [[Changes/Open WebUI/2026-03-25-3-context-window-changes-in-v0-8-11|3 Context Window changes in v0.8.11]] · Context Window
- [[Changes/Open WebUI/2026-03-25-2-search-and-browsing-changes-in-v0-8-11|2 Search and Browsing changes in v0.8.11]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-25-2-files-and-data-changes-in-v0-8-11|2 Files and Data changes in v0.8.11]] · Files and Data
- [[Changes/Open WebUI/2026-03-25-4-memory-and-personalization-changes-in-v0-8-11|4 Memory and Personalization changes in v0.8.11]] · Memory and Personalization
- [[Changes/Open WebUI/2026-03-25-3-apps-and-integrations-changes-in-v0-8-11|3 Apps and Integrations changes in v0.8.11]] · Apps and Integrations
- [[Changes/Open WebUI/2026-03-25-17-interface-experience-changes-in-v0-8-11|17 Interface Experience changes in v0.8.11]] · Interface Experience
- [[Changes/Open WebUI/2026-03-25-5-reliability-and-performance-changes-in-v0-8-11|5 Reliability and Performance changes in v0.8.11]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-25-tool-binary-response-handling-tool-servers-can-now-return-binary-data-such-as-im|🏮 Tool binary response handling. Tool servers can now return binary data such…]] · Multimodal Input
- [[Changes/Open WebUI/2026-03-25-4-safety-and-privacy-changes-in-v0-8-11|4 Safety and Privacy changes in v0.8.11]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-25-34-developer-workflow-changes-in-v0-8-11|34 Developer Workflow changes in v0.8.11]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-25-metrics-export-interval-configuration-administrators-can-now-control-opentelemet|📊 Metrics export interval configuration. Administrators can now control…]] · Pricing Model
- [[Changes/Open WebUI/2026-03-25-19-other-changes-in-v0-8-11|19 other changes in v0.8.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-03-25 · Ollama · [[Changes/Ollama/2026-03-25-if-you-have-ollama-installed-any-local-or-cloud-model-from-ollama-can-be-selecte|If you have Ollama installed, any local or cloud model from Ollama can be selected…]]
- Later: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef|Added ANTHROPIC_DEFAULT{OPUS,SONNET,HAIKU}MODEL_SUPPORTS env vars to override…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-25-e28891&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-25-23-model-support-changes-in-v0-8-11.md%0ACard%20ID%3A%20open-webui-2026-03-25-e28891%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->