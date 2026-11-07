---
card_id: open-webui-2026-02-23-ebb92c
date: '2026-02-23'
description: 'Open WebUI · 2026-02-23 · Model Support: 16 changes in v0.8.4 — ☁️ **Anthropic
  model fetching.** The system now properly fetches available models from the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1141
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 992dbb6e8c39ec66998241b369c4e3574858d4d15fd7138cd7c4cfc77f2fe3af
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-23-ebb92c
  comparison: ''
  date: '2026-02-23'
  description: 'Open WebUI — v0.8.4: 16 Model Support changes'
  evidence:
  - quote: ☁️ **Anthropic model fetching.** The system now properly fetches available
      models from the Anthropic API, ensuring all Anthropic models are accessible.
      [Commit](https://github.com/open-webui/open-webui/commit/e9d852545cc17f0eeb8bdcfa77575a80fed8706d)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F4A1 **No models prompt.** When no models are available, a helpful
      prompt now guides users to manage their provider connections. [Commit](https://github.com/open-webui/open-webui/commit/a0195cd5ae9b9915295839cd0a5fbac5a1b0bfa2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F517 **Anthropic Messages API proxy.** A new API endpoint now supports
      the Anthropic Messages API format, allowing tools like Claude Code to authenticate
      through Open WebUI and access configured models. Tool calls are now properly
      supported in streaming responses with correct multi-block indexing, and error
      status from tools is propagated correctly. The endpoint converts requests to
      OpenAI format internally, routes them through the existing chat pipeline, and
      returns responses in Anthropic format. [#21390](https://github.com/open-webui/open-webui/discussions/21390),
      [Commit](https://github.com/open-webui/open-webui/commit/91a0301c9e22e93295a7c471d83592a802560795),
      [Commit](https://github.com/open-webui/open-webui/commit/a9312d25373d3aa161788598f87180b8db11c5b6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F5C4️ **Batch access grants for multiple resources.** Loading channels,
      knowledge bases, models, notes, prompts, skills, and tools now uses batch database
      queries for access grants instead of individual queries per item, significantly
      reducing database load. For 30 items, this reduces approximately 31 queries
      to just 3. [#21616](https://github.com/open-webui/open-webui/pull/21616)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F4CA **Analytics sorting enhancement.** The Analytics dashboard
      now supports sorting by Tokens column for both Model Usage and User Usage tables,
      and the Share/Percentage columns are now clickable for sorting. Administrators
      can more easily identify the most token-consuming models and users. [Commit](https://github.com/open-webui/open-webui/commit/053a33631f575ae1ad3123190a9e820b4057f62d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F3F7️ **Model visibility badges.** The Admin Settings Models page
      now displays Public or Private badges directly on each model, making it easy
      to identify model access levels at a glance without opening the edit screen.
      [#21732](https://github.com/open-webui/open-webui/issues/21732), [Commit](https://github.com/open-webui/open-webui/commit/29217cb430bd47827ebb20782b264ae7b0f233bb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F6E0️ **Global model defaults.** Administrators can now configure
      default metadata and parameters that automatically apply to all models, reducing
      manual configuration for newly discovered models. Default capabilities (like
      vision, web search, code interpreter) and parameters (like temperature, max_tokens)
      can be set globally in Admin Settings, with per-model overrides still available.
      [#20658](https://github.com/open-webui/open-webui/issues/20658), [Commit](https://github.com/open-webui/open-webui/commit/c341f97cfe15510b7d128bd84f1e607b5289b957)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F500 **Model fallback routing fix.** Custom model fallback now works
      correctly across all model types, preventing \"Model not found\" errors when
      the fallback model uses a different backend (pipe, Ollama, or OpenAI). [#21736](https://github.com/open-webui/open-webui/pull/21736)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F41B **Default model selection fix.** Admin-configured default models
      are now properly respected when starting new chats instead of being overwritten
      by the first available model. [#21736](https://github.com/open-webui/open-webui/pull/21736)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F50D **RAG template mutation fix.** Fixed a bug where RAG template
      text was recursively injected into user messages during multiple sequential
      tool calls, causing message content to grow exponentially and potentially confuse
      the model. The system now preserves the original user message before tool-calling
      loops and correctly accumulates citation sources. [#21663](https://github.com/open-webui/open-webui/issues/21663),
      [#21668](https://github.com/open-webui/open-webui/pull/21668), [Commit](https://github.com/open-webui/open-webui/commit/becac2b2b7af8aacadbfc9b7cee2024cf7ed6acc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F5C4️ **PostgreSQL workspace cloning.** Cloning workspace models
      now works correctly on PostgreSQL databases by generating proper unique IDs
      for access grants instead of using potentially duplicate or invalid IDs. [Commit](https://github.com/open-webui/open-webui/commit/3dd44c4f1931d13bfd46062291c6f23b33dde003)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F50D **Model selector typing fix.** The model selector list no longer
      disappears or becomes grayed out when typing quickly in the search field, thanks
      to improved virtual scroll handling. [#21659](https://github.com/open-webui/open-webui/pull/21659)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: ⛔ **Disabled model cloning prevention.** Disabled models can no longer
      be cloned as workspace models, preventing invalid empty configurations from
      being created. The Clone option is now hidden for inactive models. [#21724](https://github.com/open-webui/open-webui/pull/21724)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F41B **Firefox avatar overflow fix.** Fixed a visual bug in Firefox
      where broken model or user avatar images would display overflowing alt text
      that overlapped adjacent labels on the Analytics and Leaderboard pages. Failed
      avatar images now properly show fallback icons instead. [#21730](https://github.com/open-webui/open-webui/pull/21730)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F527 **Ollama reasoning effort fix.** Reasoning effort now works
      correctly with Ollama models that require string values (\"low\", \"medium\",
      \"high\") instead of boolean, fixing \"invalid option provided\" errors when
      using models like GPT-OSS. [#20921](https://github.com/open-webui/open-webui/issues/20921),
      [#20928](https://github.com/open-webui/open-webui/pull/20928), [Commit](https://github.com/open-webui/open-webui/commit/30a13b9b2fb2c6da7e1ddbf52edb93a58d09cc56)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  - quote: "\U0001F3AF **Prompt suggestions relocated.** Prompt suggestions have been
      moved from Admin Panel - Settings - Interface to Admin Panel - Settings - Models,
      where they can now be configured per-model or globally via the new model defaults."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 16-model-support-changes-in-v0-8-4
  source_release: open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c
  source_type: github_releases
  theme: model-support
  title: 16 Model Support changes in v0.8.4
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-02-23-plan-approval-menu-shows-model-curated-actions-with-a-recommended-option-highlig|Plan
  approval menu shows model-curated actions with a recommended option highlighted…]]'
- '[[Changes/Lovable/2026-02-23-opus-4-6|Opus 4.6]]'
- "[[Changes/Open WebUI/2026-02-23-model-access-keyerror-fix-the-api-models-endpoint-no-longer-crashes-with-a-500-e|\U0001F6AB
  Model access KeyError fix. The /api/models endpoint no longer crashes…]]"
source_release: '[[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c]]'
source_type: github_releases
theme: model-support
title: 16 Model Support changes in v0.8.4
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Model Support changes in v0.8.4

**Open WebUI** · 2026-02-23 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.4) · from [[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|v0.8.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ☁️ **Anthropic model fetching.** The system now properly fetches available models from the Anthropic API, ensuring all Anthropic models are accessible. [Commit](https://github.com/open-webui/open-webui/commit/e9d852545cc17f0eeb8bdcfa77575a80fed8706d)

> 💡 **No models prompt.** When no models are available, a helpful prompt now guides users to manage their provider connections. [Commit](https://github.com/open-webui/open-webui/commit/a0195cd5ae9b9915295839cd0a5fbac5a1b0bfa2)

> 🔗 **Anthropic Messages API proxy.** A new API endpoint now supports the Anthropic Messages API format, allowing tools like Claude Code to authenticate through Open WebUI and access configured models. Tool calls are now properly supported in streaming responses with correct multi-block indexing, and error status from tools is propagated correctly. The endpoint converts requests to OpenAI format internally, routes them through the existing chat pipeline, and returns responses in Anthropic format. [#21390](https://github.com/open-webui/open-webui/discussions/21390), [Commit](https://github.com/open-webui/open-webui/commit/91a0301c9e22e93295a7c471d83592a802560795), [Commit](https://github.com/open-webui/open-webui/commit/a9312d25373d3aa161788598f87180b8db11c5b6)

> 🗄️ **Batch access grants for multiple resources.** Loading channels, knowledge bases, models, notes, prompts, skills, and tools now uses batch database queries for access grants instead of individual queries per item, significantly reducing database load. For 30 items, this reduces approximately 31 queries to just 3. [#21616](https://github.com/open-webui/open-webui/pull/21616)

> 📊 **Analytics sorting enhancement.** The Analytics dashboard now supports sorting by Tokens column for both Model Usage and User Usage tables, and the Share/Percentage columns are now clickable for sorting. Administrators can more easily identify the most token-consuming models and users. [Commit](https://github.com/open-webui/open-webui/commit/053a33631f575ae1ad3123190a9e820b4057f62d)

> 🏷️ **Model visibility badges.** The Admin Settings Models page now displays Public or Private badges directly on each model, making it easy to identify model access levels at a glance without opening the edit screen. [#21732](https://github.com/open-webui/open-webui/issues/21732), [Commit](https://github.com/open-webui/open-webui/commit/29217cb430bd47827ebb20782b264ae7b0f233bb)

> 🛠️ **Global model defaults.** Administrators can now configure default metadata and parameters that automatically apply to all models, reducing manual configuration for newly discovered models. Default capabilities (like vision, web search, code interpreter) and parameters (like temperature, max_tokens) can be set globally in Admin Settings, with per-model overrides still available. [#20658](https://github.com/open-webui/open-webui/issues/20658), [Commit](https://github.com/open-webui/open-webui/commit/c341f97cfe15510b7d128bd84f1e607b5289b957)

> 🔀 **Model fallback routing fix.** Custom model fallback now works correctly across all model types, preventing "Model not found" errors when the fallback model uses a different backend (pipe, Ollama, or OpenAI). [#21736](https://github.com/open-webui/open-webui/pull/21736)

> 🐛 **Default model selection fix.** Admin-configured default models are now properly respected when starting new chats instead of being overwritten by the first available model. [#21736](https://github.com/open-webui/open-webui/pull/21736)

> 🔍 **RAG template mutation fix.** Fixed a bug where RAG template text was recursively injected into user messages during multiple sequential tool calls, causing message content to grow exponentially and potentially confuse the model. The system now preserves the original user message before tool-calling loops and correctly accumulates citation sources. [#21663](https://github.com/open-webui/open-webui/issues/21663), [#21668](https://github.com/open-webui/open-webui/pull/21668), [Commit](https://github.com/open-webui/open-webui/commit/becac2b2b7af8aacadbfc9b7cee2024cf7ed6acc)

> 🗄️ **PostgreSQL workspace cloning.** Cloning workspace models now works correctly on PostgreSQL databases by generating proper unique IDs for access grants instead of using potentially duplicate or invalid IDs. [Commit](https://github.com/open-webui/open-webui/commit/3dd44c4f1931d13bfd46062291c6f23b33dde003)

> 🔍 **Model selector typing fix.** The model selector list no longer disappears or becomes grayed out when typing quickly in the search field, thanks to improved virtual scroll handling. [#21659](https://github.com/open-webui/open-webui/pull/21659)

> ⛔ **Disabled model cloning prevention.** Disabled models can no longer be cloned as workspace models, preventing invalid empty configurations from being created. The Clone option is now hidden for inactive models. [#21724](https://github.com/open-webui/open-webui/pull/21724)

> 🐛 **Firefox avatar overflow fix.** Fixed a visual bug in Firefox where broken model or user avatar images would display overflowing alt text that overlapped adjacent labels on the Analytics and Leaderboard pages. Failed avatar images now properly show fallback icons instead. [#21730](https://github.com/open-webui/open-webui/pull/21730)

> 🔧 **Ollama reasoning effort fix.** Reasoning effort now works correctly with Ollama models that require string values ("low", "medium", "high") instead of boolean, fixing "invalid option provided" errors when using models like GPT-OSS. [#20921](https://github.com/open-webui/open-webui/issues/20921), [#20928](https://github.com/open-webui/open-webui/pull/20928), [Commit](https://github.com/open-webui/open-webui/commit/30a13b9b2fb2c6da7e1ddbf52edb93a58d09cc56)

> 🎯 **Prompt suggestions relocated.** Prompt suggestions have been moved from Admin Panel - Settings - Interface to Admin Panel - Settings - Models, where they can now be configured per-model or globally via the new model defaults.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-23-12-developer-workflow-changes-in-v0-8-4|12 Developer Workflow changes in v0.8.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-23-10-reliability-and-performance-changes-in-v0-8-4|10 Reliability and Performance changes in v0.8.4]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-23-text-file-type-detection-fix-typescript-and-other-text-files-that-were-mis-detec|📄 Text file type detection fix. TypeScript and other text files…]] · Multimodal Input
- [[Changes/Open WebUI/2026-02-23-2-memory-and-personalization-changes-in-v0-8-4|2 Memory and Personalization changes in v0.8.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-23-ui-accessibility-improvements-screen-reader-users-can-now-navigate-the-interface|♿ UI accessibility improvements. Screen reader users can now navigate…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-02-23-8-interface-experience-changes-in-v0-8-4|8 Interface Experience changes in v0.8.4]] · Interface Experience
- [[Changes/Open WebUI/2026-02-23-2-editor-experience-changes-in-v0-8-4|2 Editor Experience changes in v0.8.4]] · Editor Experience
- [[Changes/Open WebUI/2026-02-23-4-search-and-browsing-changes-in-v0-8-4|4 Search and Browsing changes in v0.8.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-23-mcp-ssl-verification-fix-mcp-tool-connections-now-properly-respect-the-aiohttp-c|🔓 MCP SSL verification fix. MCP tool connections now properly respect…]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-23-file-access-control-respect-the-files-list-and-search-endpoints-now-properly-res|🗄️ File access control respect. The files list and search endpoints now properly…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-02-23-3-account-and-access-changes-in-v0-8-4|3 Account and Access changes in v0.8.4]] · Account and Access
- [[Changes/Open WebUI/2026-02-23-3-safety-and-privacy-changes-in-v0-8-4|3 Safety and Privacy changes in v0.8.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-23-api-tools-fix-the-api-v1-chat-completions-endpoint-now-properly-respects-caller|🛠️ API tools fix. The /api/v1/chat/completions endpoint now properly respects…]] · Agent Mode
- [[Changes/Open WebUI/2026-02-23-15-other-changes-in-v0-8-4|15 other changes in v0.8.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-02-23 · Open WebUI · [[Changes/Open WebUI/2026-02-23-model-access-keyerror-fix-the-api-models-endpoint-no-longer-crashes-with-a-500-e|🚫 Model access KeyError fix. The /api/models endpoint no longer crashes…]]
- Later: 2026-02-23 · Superwhisper · [[Changes/Superwhisper/2026-02-23-added-search-field-to-language-model-dropdown|Added search field to language model dropdown]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-23-ebb92c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-23-16-model-support-changes-in-v0-8-4.md%0ACard%20ID%3A%20open-webui-2026-02-23-ebb92c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->