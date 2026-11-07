---
card_id: open-webui-2026-06-29-634415
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Model Support: 25 changes in v0.10.0 — \U0001F3B0
  **Last model pre-selected for new slots.** When you add another model to a multi-model
  chat…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1267
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b1462d54e529e76dc7b63c901663f5c23f6399f235cd486fe31b053265633702
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-634415
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 25 Model Support changes'
  evidence:
  - quote: "\U0001F3B0 **Last model pre-selected for new slots.** When you add another
      model to a multi-model chat, the slot now defaults to the model you last picked
      instead of starting empty. [#25974](https://github.com/open-webui/open-webui/pull/25974)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F3DF️ **Arena evaluation models configurable via environment.**
      Arena evaluation models can now be defined through an environment variable,
      which previously could not be set that way. [Commit](https://github.com/open-webui/open-webui/commit/fd56086e793a0eceb07a55ff972a5492d8f8a285)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F3F7️ **Filter admin models by tag.** The admin Models settings
      page now has a tag filter for narrowing the model list by base-model tags. [Commit](https://github.com/open-webui/open-webui/commit/2bdd2ab94eefd3d75dd6511c445e302f82221b5d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4CA **Sortable analytics chat list.** The model chat list in analytics
      now has sortable column headers, so you can order it by title, last updated,
      or user. [Commit](https://github.com/open-webui/open-webui/commit/3730a9eaac68dff60b3ae5b4ed160b91480d66eb),
      [#26168](https://github.com/open-webui/open-webui/pull/26168)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F513 **Automatic auth for models with OAuth 2.1 tools.** When a
      model uses tools that require OAuth 2.1, Open WebUI now initiates the authorization
      flow automatically instead of failing the request. [Commit](https://github.com/open-webui/open-webui/commit/ae5d23f2267845922c2acb507a4a432908d03b41),
      [#23325](https://github.com/open-webui/open-webui/pull/23325), [#23272](https://github.com/open-webui/open-webui/issues/23272)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F524 **Custom tokenizer for token-based text splitting.** Token-based
      document splitting can now use a configurable Hugging Face tokenizer model,
      so chunking can match the tokenizer of the model you use. [Commit](https://github.com/open-webui/open-webui/commit/bb6b2db88b1e82395531f67db4f6accd49d8b9eb),
      [#24139](https://github.com/open-webui/open-webui/pull/24139)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F9F1 **Structured model output rendered on the client.** Reasoning,
      tool calls, and server-side tool steps such as web and file search are now rendered
      in the browser from the model's structured output instead of being flattened
      into the message text on the server, giving more accurate and editable rendering
      of these items. [Commit](https://github.com/open-webui/open-webui/commit/0443ab3a61492799f1aaa449f89cbd8aa5912f57),
      [Commit](https://github.com/open-webui/open-webui/commit/c33fadc26671190c94d86485e6e2ef2f6fd486a3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Non-blocking audio model loading.** Loading speech models no longer
      blocks the server, keeping it responsive while they initialize. [#25806](https://github.com/open-webui/open-webui/pull/25806)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Non-blocking model downloads.** Downloading large Ollama models no
      longer blocks the server on file reads and checksums, keeping it responsive
      during big downloads. [#25829](https://github.com/open-webui/open-webui/pull/25829)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Unreachable backends don't stall model loading.** Loading models and
      tool servers no longer blocks on backends that are down or slow to respond,
      so the model list stays responsive when one connection is unreachable. [#26289](https://github.com/open-webui/open-webui/pull/26289)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F3B2 **Model access enforced on arena fallback.** Reaching a model
      indirectly through an arena model on background and task requests now enforces
      that model's access rules, closing a path that could otherwise bypass them.
      [#26046](https://github.com/open-webui/open-webui/pull/26046)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4C2 **File write access requires real ownership.** Editing or deleting
      a file through a knowledge base or workspace model now requires that the object's
      owner actually owns the file, so a read-only file can no longer gain write access
      by being referenced from an object you control. [#26032](https://github.com/open-webui/open-webui/pull/26032)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F46F **Side-by-side chat with the same model.** Running two panes
      with the same model no longer leaves one pane stuck waiting or showing the other
      pane's reply after a reload, since each pane's messages are now tracked separately.
      [Commit](https://github.com/open-webui/open-webui/commit/56ae99e96a845289b5787d2dd26a3d828f2295e7),
      [#25982](https://github.com/open-webui/open-webui/issues/25982)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4BE **Model edits no longer lost when changing access.** Adjusting
      a model's access no longer auto-saves on its own and discards your other unsaved
      changes to that model. [#26004](https://github.com/open-webui/open-webui/pull/26004)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F527 **Parallel tool calls over the Anthropic-compatible API.**
      External Anthropic-compatible clients calling Open WebUI's messages endpoint
      now receive tool calls reliably when a model issues several at once or returns
      them in its final message. [Commit](https://github.com/open-webui/open-webui/commit/4210cae68e30173d7902582d32128dd699d5628a),
      [#25963](https://github.com/open-webui/open-webui/pull/25963), [#25964](https://github.com/open-webui/open-webui/discussions/25964)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4DD **Model system prompt preserved with knowledge.** A model's
      system prompt is no longer dropped when knowledge retrieval runs with native
      tool calling. [Commit](https://github.com/open-webui/open-webui/commit/cfb49c4c181a96d5df07fbfacd819639baef0bab),
      [#26217](https://github.com/open-webui/open-webui/pull/26217)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F504 **Edited models refresh in the admin list.** After editing
      a model in the admin settings, the models list now updates right away instead
      of needing a manual reload. [Commit](https://github.com/open-webui/open-webui/commit/b34d6c836ee43d0e9721fa4fd6457d934e3e2a17)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5C2️ **Workspace model bulk actions and search work across pages.**
      Bulk actions on workspace models now apply across all of them, and search results
      paginate correctly. [#26274](https://github.com/open-webui/open-webui/pull/26274)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F9E0 **Model skills load on demand instead of filling the prompt.**
      A model's attached skills are now presented to the model as a manifest it can
      load when needed, rather than having their full content inserted into the system
      prompt; skills you mention inline still get their content included directly.
      [Commit](https://github.com/open-webui/open-webui/commit/e6d35fc4cca4f4b1e5cad97d7b7e3089ef832018),
      [Commit](https://github.com/open-webui/open-webui/commit/44b9463498085741669e6f5d92e21b5ecc5fd795),
      [#25592](https://github.com/open-webui/open-webui/issues/25592), [#25599](https://github.com/open-webui/open-webui/pull/25599)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4C2 **Knowledge file listing includes attached files.** Listing
      files through the knowledge tools now also shows files attached directly to
      a model, not only those inside a knowledge base, fixing cases where listing
      returned no results for a model with a single attached file. [Commit](https://github.com/open-webui/open-webui/commit/40b655e99e2c6dd802654ec0cdac38a4bcda08b3),
      [#26301](https://github.com/open-webui/open-webui/issues/26301)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F9E0 **Reasoning details preserved across turns.** Models that return
      structured or encrypted reasoning data, such as Gemini, no longer have their
      assistant message split mid-stream, keeping reasoning continuity across turns.
      [Commit](https://github.com/open-webui/open-webui/commit/75db531c1238af113bb2b211882713e5e2f459cf),
      [#23852](https://github.com/open-webui/open-webui/pull/23852)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F522 **Built-in tools accept numeric arguments.** Built-in tools
      no longer crash when a model passes a number or a string where a specific scalar
      type is expected; values are now coerced to the declared type. [Commit](https://github.com/open-webui/open-webui/commit/c4688b958d7f7929f5f4303493ca311c2c121683),
      [#25638](https://github.com/open-webui/open-webui/pull/25638), [#25731](https://github.com/open-webui/open-webui/pull/25731),
      [#25641](https://github.com/open-webui/open-webui/issues/25641)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F441️ **Workspace base model selector respects visibility.** The
      base model selector in the workspace now hides models you don't have access
      to, matching their visibility settings. [#25668](https://github.com/open-webui/open-webui/pull/25668)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001FA79 **Missing local embedding model no longer blocks startup.**
      A missing local embedding model now surfaces as a deferred error instead of
      preventing the server from starting. [#25683](https://github.com/open-webui/open-webui/pull/25683)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F500 **Native tool calling is now the default.** Every chat and
      model that had not explicitly chosen a tool-calling mode now runs Native, which
      relies on a model's built-in tool support, while the old behavior has been renamed
      \"Legacy\" and made the explicit opt-out; if your models depend on the previous
      approach you must switch them back to \"Legacy\" per chat, per model, or globally
      in your default model parameters to preserve their behavior. [Commit](https://github.com/open-webui/open-webui/commit/b1d40f340921c27eb9a965b9feeb2563856e25e2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 25-model-support-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: model-support
  title: 25 Model Support changes in v0.10.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-06-29-text-to-speech|Text to Speech]]'
- '[[Changes/ElevenLabs/2026-06-29-workspaces-e487d5|Workspaces]]'
- '[[Changes/Kimi Code/2026-06-29-route-kimi-code-models-on-the-anthropic-compatible-protocol-through-the-beta-mes|Route
  Kimi Code models on the Anthropic-compatible protocol through the beta Messages
  API]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: model-support
title: 25 Model Support changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 25 Model Support changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎰 **Last model pre-selected for new slots.** When you add another model to a multi-model chat, the slot now defaults to the model you last picked instead of starting empty. [#25974](https://github.com/open-webui/open-webui/pull/25974)

> 🏟️ **Arena evaluation models configurable via environment.** Arena evaluation models can now be defined through an environment variable, which previously could not be set that way. [Commit](https://github.com/open-webui/open-webui/commit/fd56086e793a0eceb07a55ff972a5492d8f8a285)

> 🏷️ **Filter admin models by tag.** The admin Models settings page now has a tag filter for narrowing the model list by base-model tags. [Commit](https://github.com/open-webui/open-webui/commit/2bdd2ab94eefd3d75dd6511c445e302f82221b5d)

> 📊 **Sortable analytics chat list.** The model chat list in analytics now has sortable column headers, so you can order it by title, last updated, or user. [Commit](https://github.com/open-webui/open-webui/commit/3730a9eaac68dff60b3ae5b4ed160b91480d66eb), [#26168](https://github.com/open-webui/open-webui/pull/26168)

> 🔓 **Automatic auth for models with OAuth 2.1 tools.** When a model uses tools that require OAuth 2.1, Open WebUI now initiates the authorization flow automatically instead of failing the request. [Commit](https://github.com/open-webui/open-webui/commit/ae5d23f2267845922c2acb507a4a432908d03b41), [#23325](https://github.com/open-webui/open-webui/pull/23325), [#23272](https://github.com/open-webui/open-webui/issues/23272)

> 🔤 **Custom tokenizer for token-based text splitting.** Token-based document splitting can now use a configurable Hugging Face tokenizer model, so chunking can match the tokenizer of the model you use. [Commit](https://github.com/open-webui/open-webui/commit/bb6b2db88b1e82395531f67db4f6accd49d8b9eb), [#24139](https://github.com/open-webui/open-webui/pull/24139)

> 🧱 **Structured model output rendered on the client.** Reasoning, tool calls, and server-side tool steps such as web and file search are now rendered in the browser from the model's structured output instead of being flattened into the message text on the server, giving more accurate and editable rendering of these items. [Commit](https://github.com/open-webui/open-webui/commit/0443ab3a61492799f1aaa449f89cbd8aa5912f57), [Commit](https://github.com/open-webui/open-webui/commit/c33fadc26671190c94d86485e6e2ef2f6fd486a3)

> ⚡ **Non-blocking audio model loading.** Loading speech models no longer blocks the server, keeping it responsive while they initialize. [#25806](https://github.com/open-webui/open-webui/pull/25806)

> ⚡ **Non-blocking model downloads.** Downloading large Ollama models no longer blocks the server on file reads and checksums, keeping it responsive during big downloads. [#25829](https://github.com/open-webui/open-webui/pull/25829)

> ⚡ **Unreachable backends don't stall model loading.** Loading models and tool servers no longer blocks on backends that are down or slow to respond, so the model list stays responsive when one connection is unreachable. [#26289](https://github.com/open-webui/open-webui/pull/26289)

> 🎲 **Model access enforced on arena fallback.** Reaching a model indirectly through an arena model on background and task requests now enforces that model's access rules, closing a path that could otherwise bypass them. [#26046](https://github.com/open-webui/open-webui/pull/26046)

> 📂 **File write access requires real ownership.** Editing or deleting a file through a knowledge base or workspace model now requires that the object's owner actually owns the file, so a read-only file can no longer gain write access by being referenced from an object you control. [#26032](https://github.com/open-webui/open-webui/pull/26032)

> 👯 **Side-by-side chat with the same model.** Running two panes with the same model no longer leaves one pane stuck waiting or showing the other pane's reply after a reload, since each pane's messages are now tracked separately. [Commit](https://github.com/open-webui/open-webui/commit/56ae99e96a845289b5787d2dd26a3d828f2295e7), [#25982](https://github.com/open-webui/open-webui/issues/25982)

> 💾 **Model edits no longer lost when changing access.** Adjusting a model's access no longer auto-saves on its own and discards your other unsaved changes to that model. [#26004](https://github.com/open-webui/open-webui/pull/26004)

> 🔧 **Parallel tool calls over the Anthropic-compatible API.** External Anthropic-compatible clients calling Open WebUI's messages endpoint now receive tool calls reliably when a model issues several at once or returns them in its final message. [Commit](https://github.com/open-webui/open-webui/commit/4210cae68e30173d7902582d32128dd699d5628a), [#25963](https://github.com/open-webui/open-webui/pull/25963), [#25964](https://github.com/open-webui/open-webui/discussions/25964)

> 📝 **Model system prompt preserved with knowledge.** A model's system prompt is no longer dropped when knowledge retrieval runs with native tool calling. [Commit](https://github.com/open-webui/open-webui/commit/cfb49c4c181a96d5df07fbfacd819639baef0bab), [#26217](https://github.com/open-webui/open-webui/pull/26217)

> 🔄 **Edited models refresh in the admin list.** After editing a model in the admin settings, the models list now updates right away instead of needing a manual reload. [Commit](https://github.com/open-webui/open-webui/commit/b34d6c836ee43d0e9721fa4fd6457d934e3e2a17)

> 🗂️ **Workspace model bulk actions and search work across pages.** Bulk actions on workspace models now apply across all of them, and search results paginate correctly. [#26274](https://github.com/open-webui/open-webui/pull/26274)

> 🧠 **Model skills load on demand instead of filling the prompt.** A model's attached skills are now presented to the model as a manifest it can load when needed, rather than having their full content inserted into the system prompt; skills you mention inline still get their content included directly. [Commit](https://github.com/open-webui/open-webui/commit/e6d35fc4cca4f4b1e5cad97d7b7e3089ef832018), [Commit](https://github.com/open-webui/open-webui/commit/44b9463498085741669e6f5d92e21b5ecc5fd795), [#25592](https://github.com/open-webui/open-webui/issues/25592), [#25599](https://github.com/open-webui/open-webui/pull/25599)

> 📂 **Knowledge file listing includes attached files.** Listing files through the knowledge tools now also shows files attached directly to a model, not only those inside a knowledge base, fixing cases where listing returned no results for a model with a single attached file. [Commit](https://github.com/open-webui/open-webui/commit/40b655e99e2c6dd802654ec0cdac38a4bcda08b3), [#26301](https://github.com/open-webui/open-webui/issues/26301)

> 🧠 **Reasoning details preserved across turns.** Models that return structured or encrypted reasoning data, such as Gemini, no longer have their assistant message split mid-stream, keeping reasoning continuity across turns. [Commit](https://github.com/open-webui/open-webui/commit/75db531c1238af113bb2b211882713e5e2f459cf), [#23852](https://github.com/open-webui/open-webui/pull/23852)

> 🔢 **Built-in tools accept numeric arguments.** Built-in tools no longer crash when a model passes a number or a string where a specific scalar type is expected; values are now coerced to the declared type. [Commit](https://github.com/open-webui/open-webui/commit/c4688b958d7f7929f5f4303493ca311c2c121683), [#25638](https://github.com/open-webui/open-webui/pull/25638), [#25731](https://github.com/open-webui/open-webui/pull/25731), [#25641](https://github.com/open-webui/open-webui/issues/25641)

> 👁️ **Workspace base model selector respects visibility.** The base model selector in the workspace now hides models you don't have access to, matching their visibility settings. [#25668](https://github.com/open-webui/open-webui/pull/25668)

> 🩹 **Missing local embedding model no longer blocks startup.** A missing local embedding model now surfaces as a deferred error instead of preventing the server from starting. [#25683](https://github.com/open-webui/open-webui/pull/25683)

> 🔀 **Native tool calling is now the default.** Every chat and model that had not explicitly chosen a tool-calling mode now runs Native, which relies on a model's built-in tool support, while the old behavior has been renamed "Legacy" and made the explicit opt-out; if your models depend on the previous approach you must switch them back to "Legacy" per chat, per model, or globally in your default model parameters to preserve their behavior. [Commit](https://github.com/open-webui/open-webui/commit/b1d40f340921c27eb9a965b9feeb2563856e25e2)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-29-5-files-and-data-changes-in-v0-10-0|5 Files and Data changes in v0.10.0]] · Files and Data
- [[Changes/Open WebUI/2026-06-29-5-memory-and-personalization-changes-in-v0-10-0|5 Memory and Personalization changes in v0.10.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-29-3-voice-and-audio-changes-in-v0-10-0|3 Voice and Audio changes in v0.10.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-29-14-interface-experience-changes-in-v0-10-0|14 Interface Experience changes in v0.10.0]] · Interface Experience
- [[Changes/Open WebUI/2026-06-29-4-collaboration-changes-in-v0-10-0|4 Collaboration changes in v0.10.0]] · Collaboration
- [[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|🪪 Client User-Agent forwarded to model backends. The browser's User-Agent is now…]] · Agent Mode
- [[Changes/Open WebUI/2026-06-29-scim-sync-can-t-demote-an-admin-a-scim-provisioning-sync-that-marks-a-user-inact|🛟 SCIM sync can't demote an admin. A SCIM provisioning sync that marks a user…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-29-8-search-and-browsing-changes-in-v0-10-0|8 Search and Browsing changes in v0.10.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-29-6-reliability-and-performance-changes-in-v0-10-0|6 Reliability and Performance changes in v0.10.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-29-4-mobile-and-desktop-changes-in-v0-10-0|4 Mobile and Desktop changes in v0.10.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-29-better-screen-reader-labels-on-toggles-integration-and-switch-toggles-now-expose|♿ Better screen-reader labels on toggles. Integration and switch toggles now…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-29-16-safety-and-privacy-changes-in-v0-10-0|16 Safety and Privacy changes in v0.10.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-29-2-pricing-model-changes-in-v0-10-0|2 Pricing Model changes in v0.10.0]] · Pricing Model
- [[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-29-9-account-and-access-changes-in-v0-10-0|9 Account and Access changes in v0.10.0]] · Account and Access
- [[Changes/Open WebUI/2026-06-29-usable-chat-input-on-mobile-with-many-tools-when-skills-tools-terminal-web-searc|📱 Usable chat input on mobile with many tools. When skills, tools, terminal, web…]] · Image Generation
- [[Changes/Open WebUI/2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0|6 Automation and Scheduling changes in v0.10.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-29-3-context-window-changes-in-v0-10-0|3 Context Window changes in v0.10.0]] · Context Window
- [[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer Workflow changes in v0.10.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-29-10-editor-experience-changes-in-v0-10-0|10 Editor Experience changes in v0.10.0]] · Editor Experience
- [[Changes/Open WebUI/2026-06-29-29-other-changes-in-v0-10-0|29 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-06-29 · Kimi Code · [[Changes/Kimi Code/2026-06-29-route-kimi-code-models-on-the-anthropic-compatible-protocol-through-the-beta-mes|Route Kimi Code models on the Anthropic-compatible protocol through the beta Messages API]]
- Later: 2026-06-30 · Claude · [[Changes/Claude/2026-06-30-claude-sonnet-5-launch|Claude Sonnet 5 launch]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-634415&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-25-model-support-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-634415%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->