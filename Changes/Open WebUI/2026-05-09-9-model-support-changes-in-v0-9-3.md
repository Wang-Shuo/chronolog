---
card_id: open-webui-2026-05-09-dbff1c
date: '2026-05-09'
description: "Open WebUI · 2026-05-09 · Model Support: 9 changes in v0.9.3 — \U0001F9ED
  **Unified model unload controls.** Administrators can now unload running models
  from the model…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1216
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e85bcae16dae8d8319b600f0b740333ce02a4dc39adbd1ea8267f5b066f3a316
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-09-dbff1c
  comparison: ''
  date: '2026-05-09'
  description: 'Open WebUI — v0.9.3: 9 Model Support changes'
  evidence:
  - quote: "\U0001F9ED **Unified model unload controls.** Administrators can now unload
      running models from the model selector across supported providers, with loaded-state
      indicators shown for Ollama and llama.cpp models. [Commit](https://github.com/open-webui/open-webui/commit/4fe2de78643c2213652190d2820f4e8d9f4f89cc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F39B️ **Playground controls panel.** The Playground now includes
      a dedicated Controls toggle so you can adjust parameters like temperature and
      related settings per chat run without changing model-level defaults. [Commit](https://github.com/open-webui/open-webui/commit/c6763521c00f042a28829e33fb6f1b7355054046),
      [#24103](https://github.com/open-webui/open-webui/issues/24103)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F5BC️ **Arena model profile images.** Arena models can now reliably
      display configured profile images instead of falling back to the default icon.
      [Commit](https://github.com/open-webui/open-webui/commit/1dee67b64d0b34e70bac949682b216c0aaec8152),
      [#24412](https://github.com/open-webui/open-webui/issues/24412)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9E0 **Direct-connection task generation reliability.** Title, tags,
      follow-up, emoji, query, and related task-generation endpoints now work correctly
      when chats use direct-connection models instead of failing with model-not-found
      errors. [Commit](https://github.com/open-webui/open-webui/commit/1b4cd705d0b9a51a5e3a7851ec012fb3141eb0a9),
      [Commit](https://github.com/open-webui/open-webui/commit/005df577fec16733a64edbec8a1b46f42f4e9a43),
      [#24092](https://github.com/open-webui/open-webui/issues/24092)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F527 **Parameterized URL tool readiness.** New chats now wait for
      model defaults to finish applying before auto-submit, preventing early requests
      that can miss configured external tools. [Commit](https://github.com/open-webui/open-webui/commit/212bb68a66435dc1803a6d67cb4ea584d3455fb7),
      [#24176](https://github.com/open-webui/open-webui/issues/24176)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F4C8 **Imported chat analytics coverage.** Imported ChatGPT conversations
      now carry proper model and timestamp metadata and reliably write imported messages
      into analytics-backed storage, so imported chats are reflected correctly in
      Admin Analytics totals and model usage views. [Commit](https://github.com/open-webui/open-webui/commit/4d766a3edfa116abcefe7168f1d1284683b860b2),
      [#24263](https://github.com/open-webui/open-webui/issues/24263)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9F1 **Channel embed rendering guard.** Channel message embeds now
      appear only for model-generated messages and are suppressed in reply previews,
      preventing unintended embed expansion in regular user posts. [Commit](https://github.com/open-webui/open-webui/commit/e1dce9914745de9b4d2c67b1deddde3472ce4dfa)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9E9 **Default model metadata env parsing.** The \"DEFAULT_MODEL_METADATA\"
      environment setting is now parsed and applied correctly, including when persistent
      config is disabled, so configured model capability defaults are no longer ignored
      at startup. [Commit](https://github.com/open-webui/open-webui/commit/0103d7e82cccbd5c4b1c8daabcb3e5160fa74a97),
      [#24319](https://github.com/open-webui/open-webui/issues/24319)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9E0 **Reasoning content leakage prevention.** Tool-call round-trip
      messages no longer wrap reasoning text in `<think>` tags inside the content
      field, preventing raw markup from leaking into chat output for models whose
      templates don't strip think tags (e.g. Gemma 4). [#23844](https://github.com/open-webui/open-webui/issues/23844)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 9-model-support-changes-in-v0-9-3
  source_release: open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca
  source_type: github_releases
  theme: model-support
  title: 9 Model Support changes in v0.9.3
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-07-4-model-support-changes-in-rust-v0-129-0|4 Model
  Support changes in rust-v0.129.0]]'
- '[[Changes/Cursor/2026-05-07-added-support-for-general-model-names-for-subagent-configuration-i-e-set-model-o|Added
  support for general model names for subagent configuration (i.e., set model]]'
- '[[Changes/GitHub Copilot CLI/2026-05-08-3-model-support-changes-in-v1-0-44|3 Model
  Support changes in v1.0.44]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca]]'
source_type: github_releases
theme: model-support
title: 9 Model Support changes in v0.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Model Support changes in v0.9.3

**Open WebUI** · 2026-05-09 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.3) · from [[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|v0.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧭 **Unified model unload controls.** Administrators can now unload running models from the model selector across supported providers, with loaded-state indicators shown for Ollama and llama.cpp models. [Commit](https://github.com/open-webui/open-webui/commit/4fe2de78643c2213652190d2820f4e8d9f4f89cc)

> 🎛️ **Playground controls panel.** The Playground now includes a dedicated Controls toggle so you can adjust parameters like temperature and related settings per chat run without changing model-level defaults. [Commit](https://github.com/open-webui/open-webui/commit/c6763521c00f042a28829e33fb6f1b7355054046), [#24103](https://github.com/open-webui/open-webui/issues/24103)

> 🖼️ **Arena model profile images.** Arena models can now reliably display configured profile images instead of falling back to the default icon. [Commit](https://github.com/open-webui/open-webui/commit/1dee67b64d0b34e70bac949682b216c0aaec8152), [#24412](https://github.com/open-webui/open-webui/issues/24412)

> 🧠 **Direct-connection task generation reliability.** Title, tags, follow-up, emoji, query, and related task-generation endpoints now work correctly when chats use direct-connection models instead of failing with model-not-found errors. [Commit](https://github.com/open-webui/open-webui/commit/1b4cd705d0b9a51a5e3a7851ec012fb3141eb0a9), [Commit](https://github.com/open-webui/open-webui/commit/005df577fec16733a64edbec8a1b46f42f4e9a43), [#24092](https://github.com/open-webui/open-webui/issues/24092)

> 🔧 **Parameterized URL tool readiness.** New chats now wait for model defaults to finish applying before auto-submit, preventing early requests that can miss configured external tools. [Commit](https://github.com/open-webui/open-webui/commit/212bb68a66435dc1803a6d67cb4ea584d3455fb7), [#24176](https://github.com/open-webui/open-webui/issues/24176)

> 📈 **Imported chat analytics coverage.** Imported ChatGPT conversations now carry proper model and timestamp metadata and reliably write imported messages into analytics-backed storage, so imported chats are reflected correctly in Admin Analytics totals and model usage views. [Commit](https://github.com/open-webui/open-webui/commit/4d766a3edfa116abcefe7168f1d1284683b860b2), [#24263](https://github.com/open-webui/open-webui/issues/24263)

> 🧱 **Channel embed rendering guard.** Channel message embeds now appear only for model-generated messages and are suppressed in reply previews, preventing unintended embed expansion in regular user posts. [Commit](https://github.com/open-webui/open-webui/commit/e1dce9914745de9b4d2c67b1deddde3472ce4dfa)

> 🧩 **Default model metadata env parsing.** The "DEFAULT_MODEL_METADATA" environment setting is now parsed and applied correctly, including when persistent config is disabled, so configured model capability defaults are no longer ignored at startup. [Commit](https://github.com/open-webui/open-webui/commit/0103d7e82cccbd5c4b1c8daabcb3e5160fa74a97), [#24319](https://github.com/open-webui/open-webui/issues/24319)

> 🧠 **Reasoning content leakage prevention.** Tool-call round-trip messages no longer wrap reasoning text in `<think>` tags inside the content field, preventing raw markup from leaking into chat output for models whose templates don't strip think tags (e.g. Gemma 4). [#23844](https://github.com/open-webui/open-webui/issues/23844)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-09-5-search-and-browsing-changes-in-v0-9-3|5 Search and Browsing changes in v0.9.3]] · Search and Browsing
- [[Changes/Open WebUI/2026-05-09-10-voice-and-audio-changes-in-v0-9-3|10 Voice and Audio changes in v0.9.3]] · Voice and Audio
- [[Changes/Open WebUI/2026-05-09-5-editor-experience-changes-in-v0-9-3|5 Editor Experience changes in v0.9.3]] · Editor Experience
- [[Changes/Open WebUI/2026-05-09-8-interface-experience-changes-in-v0-9-3|8 Interface Experience changes in v0.9.3]] · Interface Experience
- [[Changes/Open WebUI/2026-05-09-4-context-window-changes-in-v0-9-3|4 Context Window changes in v0.9.3]] · Context Window
- [[Changes/Open WebUI/2026-05-09-3-apps-and-integrations-changes-in-v0-9-3|3 Apps and Integrations changes in v0.9.3]] · Apps and Integrations
- [[Changes/Open WebUI/2026-05-09-2-automation-and-scheduling-changes-in-v0-9-3|2 Automation and Scheduling changes in v0.9.3]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-05-09-22-developer-workflow-changes-in-v0-9-3|22 Developer Workflow changes in v0.9.3]] · Developer Workflow
- [[Changes/Open WebUI/2026-05-09-4-reliability-and-performance-changes-in-v0-9-3|4 Reliability and Performance changes in v0.9.3]] · Reliability and Performance
- [[Changes/Open WebUI/2026-05-09-4-account-and-access-changes-in-v0-9-3|4 Account and Access changes in v0.9.3]] · Account and Access
- [[Changes/Open WebUI/2026-05-09-sanitized-spreadsheet-html-previews-spreadsheet-previews-now-sanitize-generated|🛡️ Sanitized spreadsheet HTML previews. Spreadsheet previews now sanitize…]] · Files and Data
- [[Changes/Open WebUI/2026-05-09-3-safety-and-privacy-changes-in-v0-9-3|3 Safety and Privacy changes in v0.9.3]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-09-faster-memory-query-performance-per-user-memory-lookups-and-deletions-now-run-mu|⚡ Faster memory query performance. Per-user memory lookups and deletions now run…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-05-09-5-other-changes-in-v0-9-3|5 other changes in v0.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-05-08 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-08-3-model-support-changes-in-v1-0-44|3 Model Support changes in v1.0.44]]
- Later: 2026-05-10 · Open WebUI · [[Changes/Open WebUI/2026-05-10-3-model-support-changes-in-v0-9-5|3 Model Support changes in v0.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-09-dbff1c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-09-9-model-support-changes-in-v0-9-3.md%0ACard%20ID%3A%20open-webui-2026-05-09-dbff1c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->