---
card_id: open-webui-2026-03-08-f27167
date: '2026-03-08'
description: "Open WebUI · 2026-03-08 · Model Support: 9 changes in v0.8.9 — \U0001F4C1
  **Pyodide file system support.** Users can now upload files for Python code execution
  in the…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1154
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5a730d71f3812ce16a1f30c5bd296db761e430e7ffe990cc78266182cb6fe280
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-08-f27167
  comparison: ''
  date: '2026-03-08'
  description: 'Open WebUI — v0.8.9: 9 Model Support changes'
  evidence:
  - quote: "\U0001F4C1 **Pyodide file system support.** Users can now upload files
      for Python code execution in the code interpreter. Uploaded files are available
      in the `/mnt/uploads/` directory, and code can write output files there for
      download. The file system persists across code executions within the same session.
      The code interpreter now also informs models that pip install is not available
      in the Pyodide environment, guiding them to use alternative approaches with
      available modules. [#3583](https://github.com/open-webui/open-webui/issues/3583),
      [Commit](https://github.com/open-webui/open-webui/commit/ce0ca894fea8a2904bc6f832ff186d5fe53dd0b9),
      [Commit](https://github.com/open-webui/open-webui/commit/989938856fdb4b4afa584ae2d18c88d5be614ae2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F6E0️ **Parameterless tool calls.** Fixed parameterless tool calls
      failing during streaming by correcting the default arguments initialization,
      eliminating unnecessary model retries. [#22189](https://github.com/open-webui/open-webui/pull/22189)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F527 **Tool call streaming fixes.** Fixed two bugs where streaming
      tool calls failed silently for models like GPT-5: function names were incorrectly
      duplicated when sent in multiple delta chunks, and arguments containing multiple
      JSON objects were not properly split. Tools now execute correctly instead of
      failing without explanation. [#22177](https://github.com/open-webui/open-webui/issues/22177),
      [Commit](https://github.com/open-webui/open-webui/commit/d7efdcce2b1cdbe1637a469294bf9d52dbacab53),
      [Commit](https://github.com/open-webui/open-webui/commit/459a60a24240eab33441ed50f4f68cc27e65a037)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F9E9 **Artifact thinking block fix.** Fixed a bug where HTML preview
      rendered code blocks inside thinking blocks for certain models like Mistral
      and Z.ai, causing stray code with \">\" symbols to appear before the actual
      artifact. The fix strips thinking blocks before extracting code for artifact
      rendering. [#22267](https://github.com/open-webui/open-webui/issues/22267),
      [Commit](https://github.com/open-webui/open-webui/commit/35bc8310772c222fd8a466f7d00113a84e0402d0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4AC **Floating Quick Actions availability.** Fixed an issue where
      the \"Ask\" and \"Explain\" Floating Quick Actions were missing when selecting
      text in chats that used a model that is no longer available. [#22149](https://github.com/open-webui/open-webui/pull/22149),
      [#22139](https://github.com/open-webui/open-webui/issues/22139)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4A1 **Follow-up suggestions.** Fixed follow-up suggestions not
      appearing by correcting contradictory format instructions in the prompt template,
      ensuring the LLM returns the correct JSON object format. [#22212](https://github.com/open-webui/open-webui/pull/22212)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4CC **Stale pinned models cleanup.** Pinned models that are deleted
      or hidden are now automatically unpinned, keeping your pinned models list up
      to date. [Commit](https://github.com/open-webui/open-webui/commit/af4500e5040c8343d339cd88dd1d2fb6138c7a72)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F916 **Ollama model unload fix.** Fixed a bug where unloading a
      model from Ollama via the Open WebUI proxy failed with a \"Field required\"
      error for the prompt field. The proxy now correctly allows omitting the prompt
      when using keep_alive: 0 to unload models. [#22260](https://github.com/open-webui/open-webui/issues/22260),
      [Commit](https://github.com/open-webui/open-webui/commit/95b65ff751f91131b633cb128ff2decdd87c4a85)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  - quote: "\U0001F4C8 **Analytics URL encoding fix.** Fixed a bug where the Analytics
      page failed to load data for models with slashes in their ID, such as \"anthropic/claude-opus-4.6\".
      The frontend now properly URL-encodes forward slashes, allowing model analytics
      to load correctly. [#22380](https://github.com/open-webui/open-webui/issues/22380),
      [#22382](https://github.com/open-webui/open-webui/pull/22382)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 9-model-support-changes-in-v0-8-9
  source_release: open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb
  source_type: github_releases
  theme: model-support
  title: 9 Model Support changes in v0.8.9
  type: change
related_changes:
- '[[Changes/Ollama/2026-03-05-allow-thinking-levels-such-as-medium-to-correctly-interpreted-in-ollama-s-api-fo|Allow
  thinking levels such as "medium" to correctly interpreted in Ollama''s API…]]'
- '[[Changes/Cline/2026-03-06-added-gpt-5-4-models-for-chatgpt-subscription-users|Added
  GPT-5.4 models for ChatGPT subscription users]]'
- '[[Changes/Codex CLI/2026-03-08-13617-update-models-json-aibrahim-oai|♯13617 Update
  models.json @aibrahim-oai]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb|open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb]]'
source_type: github_releases
theme: model-support
title: 9 Model Support changes in v0.8.9
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Model Support changes in v0.8.9

**Open WebUI** · 2026-03-08 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.9) · from [[Releases/Open WebUI/open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb|v0.8.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📁 **Pyodide file system support.** Users can now upload files for Python code execution in the code interpreter. Uploaded files are available in the `/mnt/uploads/` directory, and code can write output files there for download. The file system persists across code executions within the same session. The code interpreter now also informs models that pip install is not available in the Pyodide environment, guiding them to use alternative approaches with available modules. [#3583](https://github.com/open-webui/open-webui/issues/3583), [Commit](https://github.com/open-webui/open-webui/commit/ce0ca894fea8a2904bc6f832ff186d5fe53dd0b9), [Commit](https://github.com/open-webui/open-webui/commit/989938856fdb4b4afa584ae2d18c88d5be614ae2)

> 🛠️ **Parameterless tool calls.** Fixed parameterless tool calls failing during streaming by correcting the default arguments initialization, eliminating unnecessary model retries. [#22189](https://github.com/open-webui/open-webui/pull/22189)

> 🔧 **Tool call streaming fixes.** Fixed two bugs where streaming tool calls failed silently for models like GPT-5: function names were incorrectly duplicated when sent in multiple delta chunks, and arguments containing multiple JSON objects were not properly split. Tools now execute correctly instead of failing without explanation. [#22177](https://github.com/open-webui/open-webui/issues/22177), [Commit](https://github.com/open-webui/open-webui/commit/d7efdcce2b1cdbe1637a469294bf9d52dbacab53), [Commit](https://github.com/open-webui/open-webui/commit/459a60a24240eab33441ed50f4f68cc27e65a037)

> 🧩 **Artifact thinking block fix.** Fixed a bug where HTML preview rendered code blocks inside thinking blocks for certain models like Mistral and Z.ai, causing stray code with ">" symbols to appear before the actual artifact. The fix strips thinking blocks before extracting code for artifact rendering. [#22267](https://github.com/open-webui/open-webui/issues/22267), [Commit](https://github.com/open-webui/open-webui/commit/35bc8310772c222fd8a466f7d00113a84e0402d0)

> 💬 **Floating Quick Actions availability.** Fixed an issue where the "Ask" and "Explain" Floating Quick Actions were missing when selecting text in chats that used a model that is no longer available. [#22149](https://github.com/open-webui/open-webui/pull/22149), [#22139](https://github.com/open-webui/open-webui/issues/22139)

> 💡 **Follow-up suggestions.** Fixed follow-up suggestions not appearing by correcting contradictory format instructions in the prompt template, ensuring the LLM returns the correct JSON object format. [#22212](https://github.com/open-webui/open-webui/pull/22212)

> 📌 **Stale pinned models cleanup.** Pinned models that are deleted or hidden are now automatically unpinned, keeping your pinned models list up to date. [Commit](https://github.com/open-webui/open-webui/commit/af4500e5040c8343d339cd88dd1d2fb6138c7a72)

> 🤖 **Ollama model unload fix.** Fixed a bug where unloading a model from Ollama via the Open WebUI proxy failed with a "Field required" error for the prompt field. The proxy now correctly allows omitting the prompt when using keep_alive: 0 to unload models. [#22260](https://github.com/open-webui/open-webui/issues/22260), [Commit](https://github.com/open-webui/open-webui/commit/95b65ff751f91131b633cb128ff2decdd87c4a85)

> 📈 **Analytics URL encoding fix.** Fixed a bug where the Analytics page failed to load data for models with slashes in their ID, such as "anthropic/claude-opus-4.6". The frontend now properly URL-encodes forward slashes, allowing model analytics to load correctly. [#22380](https://github.com/open-webui/open-webui/issues/22380), [#22382](https://github.com/open-webui/open-webui/pull/22382)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-08-image-generation-in-temporary-chats-generated-images-now-display-correctly-in-te|🖌️ Image generation in temporary chats. Generated images now display correctly…]] · Image Generation
- [[Changes/Open WebUI/2026-03-08-2-context-window-changes-in-v0-8-9|2 Context Window changes in v0.8.9]] · Context Window
- [[Changes/Open WebUI/2026-03-08-microsoft-oauth-refresh-token-fix-fixed-a-bug-where-microsoft-oauth-refresh-toke|🔐 Microsoft OAuth refresh token fix. Fixed a bug where Microsoft OAuth refresh…]] · Account and Access
- [[Changes/Open WebUI/2026-03-08-17-developer-workflow-changes-in-v0-8-9|17 Developer Workflow changes in v0.8.9]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-08-5-interface-experience-changes-in-v0-8-9|5 Interface Experience changes in v0.8.9]] · Interface Experience
- [[Changes/Open WebUI/2026-03-08-2-voice-and-audio-changes-in-v0-8-9|2 Voice and Audio changes in v0.8.9]] · Voice and Audio
- [[Changes/Open WebUI/2026-03-08-android-photo-capture-fixed-an-issue-where-the-first-photo-taken-in-chat-appeare|📷 Android photo capture. Fixed an issue where the first photo taken in chat…]] · Files and Data
- [[Changes/Open WebUI/2026-03-08-2-search-and-browsing-changes-in-v0-8-9|2 Search and Browsing changes in v0.8.9]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-08-open-terminal-html-editing-users-can-now-edit-html-source-files-in-open-terminal|✏️ Open Terminal HTML editing. Users can now edit HTML source files in Open…]] · Editor Experience
- [[Changes/Open WebUI/2026-03-08-system-metrics-via-opentelemetry-administrators-can-now-monitor-python-runtime-a|📡 System metrics via OpenTelemetry. Administrators can now monitor Python…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-03-08-artifacts-reactive-loop-fix-fixed-an-infinite-reactive-loop-in-chat-when-artifac|♾️ Artifacts reactive loop fix. Fixed an infinite reactive loop in chat…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-03-08-13-reliability-and-performance-changes-in-v0-8-9|13 Reliability and Performance changes in v0.8.9]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-08-open-terminal-permission-fix-open-terminal-is-now-visible-without-requiring-allo|🖥️ Open Terminal permission fix. Open Terminal is now visible without requiring…]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-08-14-other-changes-in-v0-8-9|14 other changes in v0.8.9]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-03-08 · Codex CLI · [[Changes/Codex CLI/2026-03-08-13617-update-models-json-aibrahim-oai|♯13617 Update models.json @aibrahim-oai]]
- Later: 2026-03-09 · ElevenLabs · [[Changes/ElevenLabs/2026-03-09-elevenagents|ElevenAgents]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-08-f27167&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-08-9-model-support-changes-in-v0-8-9.md%0ACard%20ID%3A%20open-webui-2026-03-08-f27167%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->