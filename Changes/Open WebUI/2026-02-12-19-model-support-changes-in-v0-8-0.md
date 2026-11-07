---
card_id: open-webui-2026-02-12-41f721
date: '2026-02-12'
description: "Open WebUI · 2026-02-12 · Model Support: 19 changes in v0.8.0 — \U0001F4CA
  **Analytics dashboard.** Administrators now have access to an Analytics dashboard
  showing…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1130
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d628b377953146b4d57ae5724772f1a2fe97f5d1a852dc6a388e178b855b3582
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-12-41f721
  comparison: ''
  date: '2026-02-12'
  description: 'Open WebUI — v0.8.0: 19 Model Support changes'
  evidence:
  - quote: "\U0001F4CA **Analytics dashboard.** Administrators now have access to
      an Analytics dashboard showing model usage statistics, token consumption by
      model and user, user activity rankings, and time-series charts with hourly or
      daily granularity; clicking any model opens a detail view with feedback history,
      associated tags, and chat browser, and results can be filtered by user group.
      [#21106](https://github.com/open-webui/open-webui/pull/21106), [Commit](https://github.com/open-webui/open-webui/commit/68a1e87b66a7ec8831d5ed52940c4ef110e3e264),
      [Commit](https://github.com/open-webui/open-webui/commit/e62649f94044abfed4d7d60647a2050383a67e3d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F30D **Community model reviews.** Users can now access community
      reviews for models directly from the model selector menu and are prompted to
      leave reviews after rating responses, with administrators able to disable this
      via the \"Community Sharing\" setting. [Commit](https://github.com/open-webui/open-webui/commit/bc90463ea60c9a66accb1fd242cf1853910ca838)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F441️ **Model list status filtering.** Administrators can now filter
      the model list by status (enabled, disabled, visible, hidden) and bulk enable
      or disable all filtered models at once. [#20553](https://github.com/open-webui/open-webui/issues/20553),
      [#20774](https://github.com/open-webui/open-webui/issues/20774), [Commit](https://github.com/open-webui/open-webui/commit/96a9696383d450dad2cbb230f3756ebfa258e029)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4D1 **Model Settings pagination.** Administrators can now navigate
      large model lists more efficiently in Model Settings, with pagination displaying
      30 models per page for smoother navigation. [Commit](https://github.com/open-webui/open-webui/commit/2f584c9f88aeb34ece07b10d05794020d1d656b8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4CC **Pin read-only models.** Users can now pin read-only models
      from the workspace. [#21308](https://github.com/open-webui/open-webui/issues/21308),
      [Commit](https://github.com/open-webui/open-webui/commit/97331bf11d41ca54e47f86777fb8dbd73988c631)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: ⚡ **Smoother model selector dropdown.** The model selector dropdown now
      renders smoothly even with hundreds of models, eliminating the lag and freezing
      that occurred when opening the dropdown with large model lists. [Commit](https://github.com/open-webui/open-webui/commit/4331029926245b7b74fa8e254610c91400b239b0)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F41B **Ollama model name suffix fix.** Ollama-compatible providers
      that do not use \":latest\" in model names can now successfully chat, fixing
      errors where model names were incorrectly appended with \":latest\" suffixes.
      [#21331](https://github.com/open-webui/open-webui/issues/21331), [Commit](https://github.com/open-webui/open-webui/commit/05ae44b98dc279ee12cc8eab17278ccbfec60301)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4BB **Markdown fence code execution fix.** Code execution now works
      reliably when models wrap code in markdown fences, automatically stripping the
      backticks before execution to prevent syntax errors that affected most non-GPT
      models. [#20941](https://github.com/open-webui/open-webui/issues/20941), [Commit](https://github.com/open-webui/open-webui/commit/4a5516775927aaf002212f2e09c55a17c699bc46),
      [Commit](https://github.com/open-webui/open-webui/commit/683438b418fb3b453a8ad88c1ba1a9944eac3593)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F5E8️ **Incomplete model metadata crash fix.** Starting chats with
      models that have incomplete metadata information no longer crashes the application.
      [#20565](https://github.com/open-webui/open-webui/issues/20565), [Commit](https://github.com/open-webui/open-webui/commit/14f6747dfc66fb7e942b930650286012121e5262)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4AC **Unavailable model crash fix.** Adding message pairs with
      Ctrl+Shift+Enter no longer crashes when the chat's model is unavailable, showing
      a helpful error message instead. [#20663](https://github.com/open-webui/open-webui/pull/20663)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F9E0 **Knowledge base query type fix.** Knowledge base queries no
      longer fail intermittently when models send tool call parameters as strings
      instead of their expected types. [#20705](https://github.com/open-webui/open-webui/pull/20705)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F5BC️ **Reasoning section artifact rendering fix.** Code blocks
      within model reasoning sections no longer incorrectly render as interactive
      artifacts, ensuring only intended output displays as previews. [#20801](https://github.com/open-webui/open-webui/issues/20801),
      [#20877](https://github.com/open-webui/open-webui/pull/20877), [Commit](https://github.com/open-webui/open-webui/commit/4c6f100b5fe2145a3d676b70b5f7c0e7f07cee20)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F3A8 **Long model name truncation.** Long model names and IDs in
      the admin panel now truncate properly to prevent visual overflow, with full
      names visible on hover. [#20696](https://github.com/open-webui/open-webui/pull/20696)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F50E **Username search on workspace pages.** Searching for users
      by username now works correctly on Models, Knowledge, and Functions workspace
      pages, making it easier to find resources owned by specific users. [#20780](https://github.com/open-webui/open-webui/pull/20780)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4DD **Workspace duplicate API request fix.** The prompts, knowledge,
      and models workspaces no longer make duplicate API requests when loading. [Commit](https://github.com/open-webui/open-webui/commit/ab5dfbda54664c9278b0d807ba06cad94edd798f),
      [Commit](https://github.com/open-webui/open-webui/commit/e5dbfc420dd3e7f6ba047a3e11584449ff0742b4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4AC **Channel model mention crash fix.** Mentioning a model in
      channels no longer crashes when older thread messages have missing data. [#21112](https://github.com/open-webui/open-webui/pull/21112)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F527 **Tool call HTML entity fix.** Models now receive properly
      formatted tool call results in multi-turn conversations, fixing an issue where
      HTML entities caused malformed content that was hard to parse. [#20755](https://github.com/open-webui/open-webui/pull/20755)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F41B **OpenAI model cache lookup fix.** The OpenAI API router model
      lookup was corrected to use the proper model identifier when checking the cache,
      ensuring consistent and correct model retrieval during chat completions. [#21327](https://github.com/open-webui/open-webui/pull/21327)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F41B **Ollama latest suffix fix.** Ollama-compatible providers that
      don't use \":latest\" in model names can now successfully chat, fixing errors
      where model names were incorrectly appended with \":latest\" suffixes. [#21331](https://github.com/open-webui/open-webui/issues/21331),
      [Commit](https://github.com/open-webui/open-webui/commit/05ae44b98dc279ee12cc8eab17278ccbfec60301)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 19-model-support-changes-in-v0-8-0
  source_release: open-webui-2026-02-12-v0-8-0-github-285910626-490914ba
  source_type: github_releases
  theme: model-support
  title: 19 Model Support changes in v0.8.0
  type: change
related_changes:
- '[[Changes/Gemini/2026-02-12-solve-modern-science-research-and-engineering-challenges-with-gemini-3-deep-thin|Solve
  modern science, research and engineering challenges with Gemini 3 Deep Think]]'
- '[[Changes/GitHub Copilot CLI/2026-02-12-add-streamer-mode-to-hide-preview-model-names-and-quota-details-for-streaming|Add
  /streamer-mode to hide preview model names and quota details for streaming]]'
- '[[Changes/Ollama/2026-02-12-3-model-support-changes-in-v0-16-0|3 Model Support
  changes in v0.16.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|open-webui-2026-02-12-v0-8-0-github-285910626-490914ba]]'
source_type: github_releases
theme: model-support
title: 19 Model Support changes in v0.8.0
type: change
---

<!-- chronolog:begin region="header" -->
# 19 Model Support changes in v0.8.0

**Open WebUI** · 2026-02-12 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.0) · from [[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|v0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📊 **Analytics dashboard.** Administrators now have access to an Analytics dashboard showing model usage statistics, token consumption by model and user, user activity rankings, and time-series charts with hourly or daily granularity; clicking any model opens a detail view with feedback history, associated tags, and chat browser, and results can be filtered by user group. [#21106](https://github.com/open-webui/open-webui/pull/21106), [Commit](https://github.com/open-webui/open-webui/commit/68a1e87b66a7ec8831d5ed52940c4ef110e3e264), [Commit](https://github.com/open-webui/open-webui/commit/e62649f94044abfed4d7d60647a2050383a67e3d)

> 🌍 **Community model reviews.** Users can now access community reviews for models directly from the model selector menu and are prompted to leave reviews after rating responses, with administrators able to disable this via the "Community Sharing" setting. [Commit](https://github.com/open-webui/open-webui/commit/bc90463ea60c9a66accb1fd242cf1853910ca838)

> 👁️ **Model list status filtering.** Administrators can now filter the model list by status (enabled, disabled, visible, hidden) and bulk enable or disable all filtered models at once. [#20553](https://github.com/open-webui/open-webui/issues/20553), [#20774](https://github.com/open-webui/open-webui/issues/20774), [Commit](https://github.com/open-webui/open-webui/commit/96a9696383d450dad2cbb230f3756ebfa258e029)

> 📑 **Model Settings pagination.** Administrators can now navigate large model lists more efficiently in Model Settings, with pagination displaying 30 models per page for smoother navigation. [Commit](https://github.com/open-webui/open-webui/commit/2f584c9f88aeb34ece07b10d05794020d1d656b8)

> 📌 **Pin read-only models.** Users can now pin read-only models from the workspace. [#21308](https://github.com/open-webui/open-webui/issues/21308), [Commit](https://github.com/open-webui/open-webui/commit/97331bf11d41ca54e47f86777fb8dbd73988c631)

> ⚡ **Smoother model selector dropdown.** The model selector dropdown now renders smoothly even with hundreds of models, eliminating the lag and freezing that occurred when opening the dropdown with large model lists. [Commit](https://github.com/open-webui/open-webui/commit/4331029926245b7b74fa8e254610c91400b239b0)

> 🐛 **Ollama model name suffix fix.** Ollama-compatible providers that do not use ":latest" in model names can now successfully chat, fixing errors where model names were incorrectly appended with ":latest" suffixes. [#21331](https://github.com/open-webui/open-webui/issues/21331), [Commit](https://github.com/open-webui/open-webui/commit/05ae44b98dc279ee12cc8eab17278ccbfec60301)

> 💻 **Markdown fence code execution fix.** Code execution now works reliably when models wrap code in markdown fences, automatically stripping the backticks before execution to prevent syntax errors that affected most non-GPT models. [#20941](https://github.com/open-webui/open-webui/issues/20941), [Commit](https://github.com/open-webui/open-webui/commit/4a5516775927aaf002212f2e09c55a17c699bc46), [Commit](https://github.com/open-webui/open-webui/commit/683438b418fb3b453a8ad88c1ba1a9944eac3593)

> 🗨️ **Incomplete model metadata crash fix.** Starting chats with models that have incomplete metadata information no longer crashes the application. [#20565](https://github.com/open-webui/open-webui/issues/20565), [Commit](https://github.com/open-webui/open-webui/commit/14f6747dfc66fb7e942b930650286012121e5262)

> 💬 **Unavailable model crash fix.** Adding message pairs with Ctrl+Shift+Enter no longer crashes when the chat's model is unavailable, showing a helpful error message instead. [#20663](https://github.com/open-webui/open-webui/pull/20663)

> 🧠 **Knowledge base query type fix.** Knowledge base queries no longer fail intermittently when models send tool call parameters as strings instead of their expected types. [#20705](https://github.com/open-webui/open-webui/pull/20705)

> 🖼️ **Reasoning section artifact rendering fix.** Code blocks within model reasoning sections no longer incorrectly render as interactive artifacts, ensuring only intended output displays as previews. [#20801](https://github.com/open-webui/open-webui/issues/20801), [#20877](https://github.com/open-webui/open-webui/pull/20877), [Commit](https://github.com/open-webui/open-webui/commit/4c6f100b5fe2145a3d676b70b5f7c0e7f07cee20)

> 🎨 **Long model name truncation.** Long model names and IDs in the admin panel now truncate properly to prevent visual overflow, with full names visible on hover. [#20696](https://github.com/open-webui/open-webui/pull/20696)

> 🔎 **Username search on workspace pages.** Searching for users by username now works correctly on Models, Knowledge, and Functions workspace pages, making it easier to find resources owned by specific users. [#20780](https://github.com/open-webui/open-webui/pull/20780)

> 📝 **Workspace duplicate API request fix.** The prompts, knowledge, and models workspaces no longer make duplicate API requests when loading. [Commit](https://github.com/open-webui/open-webui/commit/ab5dfbda54664c9278b0d807ba06cad94edd798f), [Commit](https://github.com/open-webui/open-webui/commit/e5dbfc420dd3e7f6ba047a3e11584449ff0742b4)

> 💬 **Channel model mention crash fix.** Mentioning a model in channels no longer crashes when older thread messages have missing data. [#21112](https://github.com/open-webui/open-webui/pull/21112)

> 🔧 **Tool call HTML entity fix.** Models now receive properly formatted tool call results in multi-turn conversations, fixing an issue where HTML entities caused malformed content that was hard to parse. [#20755](https://github.com/open-webui/open-webui/pull/20755)

> 🐛 **OpenAI model cache lookup fix.** The OpenAI API router model lookup was corrected to use the proper model identifier when checking the cache, ensuring consistent and correct model retrieval during chat completions. [#21327](https://github.com/open-webui/open-webui/pull/21327)

> 🐛 **Ollama latest suffix fix.** Ollama-compatible providers that don't use ":latest" in model names can now successfully chat, fixing errors where model names were incorrectly appended with ":latest" suffixes. [#21331](https://github.com/open-webui/open-webui/issues/21331), [Commit](https://github.com/open-webui/open-webui/commit/05ae44b98dc279ee12cc8eab17278ccbfec60301)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-12-16-reliability-and-performance-changes-in-v0-8-0|16 Reliability and Performance changes in v0.8.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-12-audio-service-timeout-handling-audio-transcription-and-text-to-speech-requests-n|🔌 Audio service timeout handling. Audio transcription and text-to-speech…]] · Voice and Audio
- [[Changes/Open WebUI/2026-02-12-2-editor-experience-changes-in-v0-8-0|2 Editor Experience changes in v0.8.0]] · Editor Experience
- [[Changes/Open WebUI/2026-02-12-5-safety-and-privacy-changes-in-v0-8-0|5 Safety and Privacy changes in v0.8.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-12-27-developer-workflow-changes-in-v0-8-0|27 Developer Workflow changes in v0.8.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-12-5-context-window-changes-in-v0-8-0|5 Context Window changes in v0.8.0]] · Context Window
- [[Changes/Open WebUI/2026-02-12-2-image-generation-changes-in-v0-8-0|2 Image Generation changes in v0.8.0]] · Image Generation
- [[Changes/Open WebUI/2026-02-12-2-memory-and-personalization-changes-in-v0-8-0|2 Memory and Personalization changes in v0.8.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-12-gboard-multi-line-paste-fix-multi-line-text-pasted-from-gboard-on-android-now-in|📱 Gboard multi-line paste fix. Multi-line text pasted from Gboard on Android now…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-02-12-2-collaboration-changes-in-v0-8-0|2 Collaboration changes in v0.8.0]] · Collaboration
- [[Changes/Open WebUI/2026-02-12-6-account-and-access-changes-in-v0-8-0|6 Account and Access changes in v0.8.0]] · Account and Access
- [[Changes/Open WebUI/2026-02-12-async-pipeline-operations-pipeline-operations-now-run-asynchronously-instead-of|🔧 Async pipeline operations. Pipeline operations now run asynchronously instead…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-02-12-5-search-and-browsing-changes-in-v0-8-0|5 Search and Browsing changes in v0.8.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-12-8-interface-experience-changes-in-v0-8-0|8 Interface Experience changes in v0.8.0]] · Interface Experience
- [[Changes/Open WebUI/2026-02-12-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-02-12-screen-reader-accessibility-screen-reader-users-now-hear-the-password-field-labe|♿ Screen reader accessibility. Screen reader users now hear the password field…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-02-12-10-files-and-data-changes-in-v0-8-0|10 Files and Data changes in v0.8.0]] · Files and Data
- [[Changes/Open WebUI/2026-02-12-6-apps-and-integrations-changes-in-v0-8-0|6 Apps and Integrations changes in v0.8.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-12-29-other-changes-in-v0-8-0|29 other changes in v0.8.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-02-12 · Ollama · [[Changes/Ollama/2026-02-12-3-model-support-changes-in-v0-16-0|3 Model Support changes in v0.16.0]]
- Later: 2026-02-12 · OpenCode · [[Changes/OpenCode/2026-02-12-2-model-support-changes-in-v1-1-60|2 Model Support changes in v1.1.60]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-12-41f721&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-12-19-model-support-changes-in-v0-8-0.md%0ACard%20ID%3A%20open-webui-2026-02-12-41f721%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->