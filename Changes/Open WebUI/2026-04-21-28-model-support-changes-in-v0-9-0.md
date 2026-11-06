---
card_id: open-webui-2026-04-21-2e3dec
date: '2026-04-21'
description: "Open WebUI · 2026-04-21 · Model Support: 28 changes in v0.9.0 — \U0001F4CB
  **Task management tool.** AI models can now create, update, and track tasks within
  a chat…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1198
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f4e0b1f9c865a9236edd95aca35f6c15f1583c328cd047e513ec1eddf18d59e1
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-2e3dec
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 28 Model Support changes'
  evidence:
  - quote: "\U0001F4CB **Task management tool.** AI models can now create, update,
      and track tasks within a chat conversation, breaking down complex requests into
      manageable steps with real-time status updates. [Commit](https://github.com/open-webui/open-webui/commit/bcb71bb5206ac01d97a39fde8ecf0e0541dde636)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F916 **Ollama responses support.** The Ollama proxy now supports
      the Responses API, letting clients use \"/v1/responses\" directly with Ollama-hosted
      models through Open WebUI. [#23483](https://github.com/open-webui/open-webui/pull/23483)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F399️ **Mistral TTS support.** Mistral can now be used as a text-to-speech
      provider, with admin settings for the API key, base URL, voices, and model selection.
      [Commit](https://github.com/open-webui/open-webui/commit/4cee67e2be0c80a0b501073ea49a80d13efd1c41)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5D1️ **Admin model deletion.** Administrators can now delete Ollama
      models directly from the model selector menu, making it easier to clean up unused
      or unwanted models. [Commit](https://github.com/open-webui/open-webui/commit/2388dd7dc3530b5dd5419c5d0bb1bcdcb7544099)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5C2️ **Model selector focus.** The model selector now resets its
      search only when it opens, making the popup feel more predictable while still
      focusing the search field automatically. [Commit](https://github.com/open-webui/open-webui/commit/b89019a8e1f96e01dc8e19a81ef8fb4f4eae3eef)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5BC️ **Model image lookup efficiency.** Model profile image requests
      now reuse the current request database session, reducing per-request overhead
      and improving response efficiency. [#23796](https://github.com/open-webui/open-webui/pull/23796)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5C2️ **Feedback filtering.** Administrators can now filter feedback
      history by model and export only the feedback they need. [Commit](https://github.com/open-webui/open-webui/commit/60e4d7517463690b3a87de38babc9ac561897c61)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F552 **Model access updates.** Changing a model’s access grants
      now updates its timestamp, so recently modified models stay easier to find and
      sort correctly. [Commit](https://github.com/open-webui/open-webui/commit/53eadb7df7281f5661cbe22c8b26b5aedaba3083)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9EE **Usage analytics accuracy.** Token usage is now normalized
      before chat messages are saved, so model and user usage reports stay accurate
      across OpenAI-compatible providers. [Commit](https://github.com/open-webui/open-webui/commit/4dea4fdf54e00ebaba8e3178128bf8709453d2a2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6E1️ **Model description XSS protection.** Model descriptions shown
      in chat placeholders are now sanitized before rendering, preventing malicious
      links from executing scripts and helping protect user sessions from takeover.
      [#23621](https://github.com/open-webui/open-webui/pull/23621)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4CA **Shared chat analytics consistency.** Usage and message-count
      analytics now count assistant activity consistently across regular and shared
      chats, improving accuracy in model, user, chat, and time-based reporting views.
      [Commit](https://github.com/open-webui/open-webui/commit/e29d145a1cff23122de16123a4cfda1b84abffbb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F511 **Anthropic x-api-key model access.** Anthropic-compatible
      clients can now authenticate with the \"x-api-key\" header across all relevant
      API routes, so model listing requests like GET \"/api/v1/models\" no longer
      fail with unauthorized errors. [#23319](https://github.com/open-webui/open-webui/issues/23319),
      [Commit](https://github.com/open-webui/open-webui/commit/611fe0c8a938539b73b559e84964f40c30bf436d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9E9 **Ollama thinking field preservation.** Messages modified by
      filters now keep the Ollama \"thinking\" field when sent to the model, so reasoning-aware
      workflows and custom filter-based passthrough setups work reliably. [Commit](https://github.com/open-webui/open-webui/commit/8bd23b91459914eb7df5b5a66567d3544e0da168),
      [#22508](https://github.com/open-webui/open-webui/issues/22508)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9FE **Reasoning content preservation.** Assistant tool-call messages
      now retain reasoning content across turns, improving reliability for reasoning-heavy
      model workflows. [Commit](https://github.com/open-webui/open-webui/commit/3dd8255816898467246c81cba3c9bc48bc18d86d),
      [#23175](https://github.com/open-webui/open-webui/issues/23175), [#23742](https://github.com/open-webui/open-webui/pull/23742)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9ED **Background task scoping for new chats.** Chat title and auto-tag
      generation now run only for the first message of a new conversation and only
      once in multi-model responses, preventing duplicate or incorrectly triggered
      background tasks in follow-up flows. [Commit](https://github.com/open-webui/open-webui/commit/f102060a6d85db4acd3d0bf5c25e976f36cd5533..a4ed16999eec9a654a37c2bb4c15ba5ecd1fa3b7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5BC️ **Image URL conversion reliability.** Sending image URLs to
      AI models no longer fails with \"cannot pickle 'coroutine' object\" errors,
      so image inputs now convert to base64 reliably during request processing. [#23685](https://github.com/open-webui/open-webui/pull/23685#issuecomment-4240424635)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F30D **Non-ASCII tag filtering.** Prompt and model tag filters now
      handle non-Latin tags more reliably across SQLite and PostgreSQL, so tags like
      Cyrillic values return the expected items in Workspace lists. [#23381](https://github.com/open-webui/open-webui/issues/23381),
      [#23427](https://github.com/open-webui/open-webui/pull/23427), [Commit](https://github.com/open-webui/open-webui/commit/57784706e4fee75dec67e20b0d89a97351ac6256)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9F7 **Responses model access control.** The OpenAI-compatible Responses
      endpoint now enforces per-model permissions, preventing non-admin users from
      accessing models they are not allowed to use. [#23481](https://github.com/open-webui/open-webui/pull/23481)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F517 **Chained base model access checks.** Chained base model execution
      now enforces per-model access rules to prevent unauthorized model usage. [Commit](https://github.com/open-webui/open-webui/commit/8acce144f99992b75c25f0e5038b16881ce9f066),
      [Commit](https://github.com/open-webui/open-webui/commit/50363ba66b19613a2fc0cab6a3f7f724a825135e),
      [#23647](https://github.com/open-webui/open-webui/pull/23647)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4E5 **Model import ownership validation.** Model import now enforces
      ownership and access grant checks to prevent unauthorized imports. [Commit](https://github.com/open-webui/open-webui/commit/499129625bf96b2c03a6d057a2f91fdf07fd1c49),
      [#23628](https://github.com/open-webui/open-webui/pull/23628)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F39B️ **Ollama endpoint model permissions.** Restricted models are
      now protected on Ollama show, generate, embed, and embeddings endpoints, preventing
      authenticated users from using private models without read access. [#23631](https://github.com/open-webui/open-webui/pull/23631)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9ED **Azure deployment path validation.** Azure model names are
      now validated and safely encoded before request URL construction, preventing
      path traversal attempts from reaching unintended Azure endpoints. [#23629](https://github.com/open-webui/open-webui/pull/23629)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F50F **Ollama SSL handling.** Ollama model management and file uploads
      now respect the configured SSL verification setting, so self-signed certificates
      work when SSL verification is disabled. [#23503](https://github.com/open-webui/open-webui/issues/23503),
      [Commit](https://github.com/open-webui/open-webui/commit/e51b661af0e71a24f041428f328fcc6e97a15262)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4BE **Error message persistence.** LLM errors that occur during
      streaming are now saved to the database even if the connection drops, so users
      can see what went wrong when they reconnect. [#23231](https://github.com/open-webui/open-webui/pull/23231)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6DF **Task model fallback safety.** Task routing now handles missing
      default model entries safely, preventing task execution failures when the previously
      selected model is no longer available. [#23169](https://github.com/open-webui/open-webui/pull/23169)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: ✂️ **Citation spacing cleanup.** When citations are disabled for a model,
      citation markers and their leftover spacing are now removed together so punctuation
      and copied text remain cleanly formatted. [#23141](https://github.com/open-webui/open-webui/issues/23141)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: ⚙️ **Default model parameter loading.** The "DEFAULT_MODEL_PARAMS" environment
      variable is now parsed and applied correctly, so default generation settings
      are honored reliably without being ignored at startup. [#23223](https://github.com/open-webui/open-webui/pull/23223)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F4F2 **Mobile model selector positioning.** The mobile model selector
      dropdown now applies a constrained viewport width and left offset, preventing
      overflow and making model selection easier on small screens. [#23310](https://github.com/open-webui/open-webui/pull/23310)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 28-model-support-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: model-support
  title: 28 Model Support changes in v0.9.0
  type: change
related_changes:
- '[[Changes/Replit/2026-04-17-claude-opus-4-7-powers-power-mode|Claude Opus 4.7 powers
  Power mode]]'
- '[[Changes/Codex CLI/2026-04-20-6-model-support-changes-in-rust-v0-122-0|6 Model
  Support changes in rust-v0.122.0]]'
- '[[Changes/GitHub Copilot CLI/2026-04-20-ctrl-t-to-toggle-reasoning-display-is-now-listed-in-the-help-and-overlay|ctrl+t
  to toggle reasoning display is now listed in the /help and ? overlay]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: model-support
title: 28 Model Support changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 28 Model Support changes in v0.9.0

**Open WebUI** · 2026-04-21 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📋 **Task management tool.** AI models can now create, update, and track tasks within a chat conversation, breaking down complex requests into manageable steps with real-time status updates. [Commit](https://github.com/open-webui/open-webui/commit/bcb71bb5206ac01d97a39fde8ecf0e0541dde636)

> 🤖 **Ollama responses support.** The Ollama proxy now supports the Responses API, letting clients use "/v1/responses" directly with Ollama-hosted models through Open WebUI. [#23483](https://github.com/open-webui/open-webui/pull/23483)

> 🎙️ **Mistral TTS support.** Mistral can now be used as a text-to-speech provider, with admin settings for the API key, base URL, voices, and model selection. [Commit](https://github.com/open-webui/open-webui/commit/4cee67e2be0c80a0b501073ea49a80d13efd1c41)

> 🗑️ **Admin model deletion.** Administrators can now delete Ollama models directly from the model selector menu, making it easier to clean up unused or unwanted models. [Commit](https://github.com/open-webui/open-webui/commit/2388dd7dc3530b5dd5419c5d0bb1bcdcb7544099)

> 🗂️ **Model selector focus.** The model selector now resets its search only when it opens, making the popup feel more predictable while still focusing the search field automatically. [Commit](https://github.com/open-webui/open-webui/commit/b89019a8e1f96e01dc8e19a81ef8fb4f4eae3eef)

> 🖼️ **Model image lookup efficiency.** Model profile image requests now reuse the current request database session, reducing per-request overhead and improving response efficiency. [#23796](https://github.com/open-webui/open-webui/pull/23796)

> 🗂️ **Feedback filtering.** Administrators can now filter feedback history by model and export only the feedback they need. [Commit](https://github.com/open-webui/open-webui/commit/60e4d7517463690b3a87de38babc9ac561897c61)

> 🕒 **Model access updates.** Changing a model’s access grants now updates its timestamp, so recently modified models stay easier to find and sort correctly. [Commit](https://github.com/open-webui/open-webui/commit/53eadb7df7281f5661cbe22c8b26b5aedaba3083)

> 🧮 **Usage analytics accuracy.** Token usage is now normalized before chat messages are saved, so model and user usage reports stay accurate across OpenAI-compatible providers. [Commit](https://github.com/open-webui/open-webui/commit/4dea4fdf54e00ebaba8e3178128bf8709453d2a2)

> 🛡️ **Model description XSS protection.** Model descriptions shown in chat placeholders are now sanitized before rendering, preventing malicious links from executing scripts and helping protect user sessions from takeover. [#23621](https://github.com/open-webui/open-webui/pull/23621)

> 📊 **Shared chat analytics consistency.** Usage and message-count analytics now count assistant activity consistently across regular and shared chats, improving accuracy in model, user, chat, and time-based reporting views. [Commit](https://github.com/open-webui/open-webui/commit/e29d145a1cff23122de16123a4cfda1b84abffbb)

> 🔑 **Anthropic x-api-key model access.** Anthropic-compatible clients can now authenticate with the "x-api-key" header across all relevant API routes, so model listing requests like GET "/api/v1/models" no longer fail with unauthorized errors. [#23319](https://github.com/open-webui/open-webui/issues/23319), [Commit](https://github.com/open-webui/open-webui/commit/611fe0c8a938539b73b559e84964f40c30bf436d)

> 🧩 **Ollama thinking field preservation.** Messages modified by filters now keep the Ollama "thinking" field when sent to the model, so reasoning-aware workflows and custom filter-based passthrough setups work reliably. [Commit](https://github.com/open-webui/open-webui/commit/8bd23b91459914eb7df5b5a66567d3544e0da168), [#22508](https://github.com/open-webui/open-webui/issues/22508)

> 🧾 **Reasoning content preservation.** Assistant tool-call messages now retain reasoning content across turns, improving reliability for reasoning-heavy model workflows. [Commit](https://github.com/open-webui/open-webui/commit/3dd8255816898467246c81cba3c9bc48bc18d86d), [#23175](https://github.com/open-webui/open-webui/issues/23175), [#23742](https://github.com/open-webui/open-webui/pull/23742)

> 🧭 **Background task scoping for new chats.** Chat title and auto-tag generation now run only for the first message of a new conversation and only once in multi-model responses, preventing duplicate or incorrectly triggered background tasks in follow-up flows. [Commit](https://github.com/open-webui/open-webui/commit/f102060a6d85db4acd3d0bf5c25e976f36cd5533..a4ed16999eec9a654a37c2bb4c15ba5ecd1fa3b7)

> 🖼️ **Image URL conversion reliability.** Sending image URLs to AI models no longer fails with "cannot pickle 'coroutine' object" errors, so image inputs now convert to base64 reliably during request processing. [#23685](https://github.com/open-webui/open-webui/pull/23685#issuecomment-4240424635)

> 🌍 **Non-ASCII tag filtering.** Prompt and model tag filters now handle non-Latin tags more reliably across SQLite and PostgreSQL, so tags like Cyrillic values return the expected items in Workspace lists. [#23381](https://github.com/open-webui/open-webui/issues/23381), [#23427](https://github.com/open-webui/open-webui/pull/23427), [Commit](https://github.com/open-webui/open-webui/commit/57784706e4fee75dec67e20b0d89a97351ac6256)

> 🧷 **Responses model access control.** The OpenAI-compatible Responses endpoint now enforces per-model permissions, preventing non-admin users from accessing models they are not allowed to use. [#23481](https://github.com/open-webui/open-webui/pull/23481)

> 🔗 **Chained base model access checks.** Chained base model execution now enforces per-model access rules to prevent unauthorized model usage. [Commit](https://github.com/open-webui/open-webui/commit/8acce144f99992b75c25f0e5038b16881ce9f066), [Commit](https://github.com/open-webui/open-webui/commit/50363ba66b19613a2fc0cab6a3f7f724a825135e), [#23647](https://github.com/open-webui/open-webui/pull/23647)

> 📥 **Model import ownership validation.** Model import now enforces ownership and access grant checks to prevent unauthorized imports. [Commit](https://github.com/open-webui/open-webui/commit/499129625bf96b2c03a6d057a2f91fdf07fd1c49), [#23628](https://github.com/open-webui/open-webui/pull/23628)

> 🎛️ **Ollama endpoint model permissions.** Restricted models are now protected on Ollama show, generate, embed, and embeddings endpoints, preventing authenticated users from using private models without read access. [#23631](https://github.com/open-webui/open-webui/pull/23631)

> 🧭 **Azure deployment path validation.** Azure model names are now validated and safely encoded before request URL construction, preventing path traversal attempts from reaching unintended Azure endpoints. [#23629](https://github.com/open-webui/open-webui/pull/23629)

> 🔏 **Ollama SSL handling.** Ollama model management and file uploads now respect the configured SSL verification setting, so self-signed certificates work when SSL verification is disabled. [#23503](https://github.com/open-webui/open-webui/issues/23503), [Commit](https://github.com/open-webui/open-webui/commit/e51b661af0e71a24f041428f328fcc6e97a15262)

> 💾 **Error message persistence.** LLM errors that occur during streaming are now saved to the database even if the connection drops, so users can see what went wrong when they reconnect. [#23231](https://github.com/open-webui/open-webui/pull/23231)

> 🛟 **Task model fallback safety.** Task routing now handles missing default model entries safely, preventing task execution failures when the previously selected model is no longer available. [#23169](https://github.com/open-webui/open-webui/pull/23169)

> ✂️ **Citation spacing cleanup.** When citations are disabled for a model, citation markers and their leftover spacing are now removed together so punctuation and copied text remain cleanly formatted. [#23141](https://github.com/open-webui/open-webui/issues/23141)

> ⚙️ **Default model parameter loading.** The "DEFAULT_MODEL_PARAMS" environment variable is now parsed and applied correctly, so default generation settings are honored reliably without being ignored at startup. [#23223](https://github.com/open-webui/open-webui/pull/23223)

> 📲 **Mobile model selector positioning.** The mobile model selector dropdown now applies a constrained viewport width and left offset, preventing overflow and making model selection easier on small screens. [#23310](https://github.com/open-webui/open-webui/pull/23310)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-3-files-and-data-changes-in-v0-9-0|3 Files and Data changes in v0.9.0]] · Files and Data
- [[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation changes in v0.9.0]] · Image Generation
- [[Changes/Open WebUI/2026-04-21-5-editor-experience-changes-in-v0-9-0|5 Editor Experience changes in v0.9.0]] · Editor Experience
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-8-context-window-changes-in-v0-9-0|8 Context Window changes in v0.9.0]] · Context Window
- [[Changes/Open WebUI/2026-04-21-24-reliability-and-performance-changes-in-v0-9-0|24 Reliability and Performance changes in v0.9.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-21-4-apps-and-integrations-changes-in-v0-9-0|4 Apps and Integrations changes in v0.9.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-21-46-developer-workflow-changes-in-v0-9-0|46 Developer Workflow changes in v0.9.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-04-21-8-automation-and-scheduling-changes-in-v0-9-0|8 Automation and Scheduling changes in v0.9.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-21-7-memory-and-personalization-changes-in-v0-9-0|7 Memory and Personalization changes in v0.9.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-21-2-mobile-and-desktop-changes-in-v0-9-0|2 Mobile and Desktop changes in v0.9.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-04-21-17-interface-experience-changes-in-v0-9-0|17 Interface Experience changes in v0.9.0]] · Interface Experience
- [[Changes/Open WebUI/2026-04-21-11-safety-and-privacy-changes-in-v0-9-0|11 Safety and Privacy changes in v0.9.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-04-21-4-search-and-browsing-changes-in-v0-9-0|4 Search and Browsing changes in v0.9.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-04-21-shared-chat-access-controls-you-can-now-control-who-has-access-to-a-shared-chat|🔗 Shared chat access controls. You can now control who has access to a shared…]] · Collaboration
- [[Changes/Open WebUI/2026-04-21-4-voice-and-audio-changes-in-v0-9-0|4 Voice and Audio changes in v0.9.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-04-21-17-account-and-access-changes-in-v0-9-0|17 Account and Access changes in v0.9.0]] · Account and Access
- [[Changes/Open WebUI/2026-04-21-21-other-changes-in-v0-9-0|21 other changes in v0.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-04-20 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-20-ctrl-t-to-toggle-reasoning-display-is-now-listed-in-the-help-and-overlay|ctrl+t to toggle reasoning display is now listed in the /help and ? overlay]]
- Later: 2026-04-22 · Claude Code · [[Changes/Claude Code/2026-04-22-2-model-support-changes-in-v2-1-117|2 Model Support changes in v2.1.117]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-2e3dec&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-28-model-support-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-2e3dec%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->