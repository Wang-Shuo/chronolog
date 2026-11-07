---
card_id: open-webui-2026-05-09-34b32b
date: '2026-05-09'
description: "Open WebUI · 2026-05-09 · Editor Experience: 5 changes in v0.9.3 — \U0001F4DD
  **System prompt editor scroll stability.** Editing large system prompts no longer
  jumps…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2736
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6b4ab30d686dcb117dc996526f40128993cbffcac2bb5d21e3e2c567063a1556
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-09-34b32b
  comparison: ''
  date: '2026-05-09'
  description: 'Open WebUI — v0.9.3: 5 Editor Experience changes'
  evidence:
  - quote: "\U0001F4DD **System prompt editor scroll stability.** Editing large system
      prompts no longer jumps the page back to the top, so you can continue editing
      long model prompts without losing your place. [Commit](https://github.com/open-webui/open-webui/commit/c978a788c8315e37357c93c1b605a2831fc77485),
      [#23999](https://github.com/open-webui/open-webui/issues/23999)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F4C2 **File modal open-link behavior.** Clicking a file name in
      the file details modal now opens the correct file content in a new tab for uploaded
      file items instead of failing to open. [#24125](https://github.com/open-webui/open-webui/pull/24125)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F9F0 **Multi-worker tool update consistency.** Updated tool code
      now refreshes correctly across workers without requiring a full service restart,
      so chats no longer run stale tool versions after edits. [Commit](https://github.com/open-webui/open-webui/commit/3309f5d9f11f521c0ee97b64c59a83e3cf390bde),
      [#24400](https://github.com/open-webui/open-webui/issues/24400), [#24433](https://github.com/open-webui/open-webui/pull/24433)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F4CA **Streaming token analytics accuracy.** Admin Analytics now
      records and aggregates token usage correctly for streaming chats across Responses
      API and OpenAI-compatible providers, including fallback handling for provider
      usage formats that use prompt and completion token keys. [Commit](https://github.com/open-webui/open-webui/commit/989d5fd4e2ce285edf4475a1e13f0981a78d3821),
      [Commit](https://github.com/open-webui/open-webui/commit/a32d26e61d24d9f63650faed5cb8909ed90af661),
      [#24217](https://github.com/open-webui/open-webui/issues/24217), [#24294](https://github.com/open-webui/open-webui/issues/24294),
      [#24241](https://github.com/open-webui/open-webui/issues/24241)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F4BE **Chat control autosave persistence.** Changes to chat controls
      like system prompt, parameters, and attached files are now autosaved on existing
      chats, so edits are no longer lost when you refresh or navigate away before
      sending a message. [Commit](https://github.com/open-webui/open-webui/commit/a938c8ae2e45a00d2f06151fdaeaee94e54a8095),
      [#23897](https://github.com/open-webui/open-webui/pull/23897)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-editor-experience-changes-in-v0-9-3
  source_release: open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca
  source_type: github_releases
  theme: editor-experience
  title: 5 Editor Experience changes in v0.9.3
  type: change
related_changes:
- '[[Changes/Devin/2026-05-08-ask-devin-in-pr-discussions|Ask Devin in PR Discussions]]'
- '[[Changes/GitHub Copilot CLI/2026-05-08-2-editor-experience-changes-in-v1-0-44|2
  Editor Experience changes in v1.0.44]]'
- '[[Changes/Raycast/2026-05-08-quick-ai-gets-a-major-refresh-in-this-release-bringing-it-closer-to-the-ai-chat|Quick
  AI gets a major refresh in this release, bringing it closer to the AI Chat…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca]]'
source_type: github_releases
theme: editor-experience
title: 5 Editor Experience changes in v0.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Editor Experience changes in v0.9.3

**Open WebUI** · 2026-05-09 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.3) · from [[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|v0.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📝 **System prompt editor scroll stability.** Editing large system prompts no longer jumps the page back to the top, so you can continue editing long model prompts without losing your place. [Commit](https://github.com/open-webui/open-webui/commit/c978a788c8315e37357c93c1b605a2831fc77485), [#23999](https://github.com/open-webui/open-webui/issues/23999)

> 📂 **File modal open-link behavior.** Clicking a file name in the file details modal now opens the correct file content in a new tab for uploaded file items instead of failing to open. [#24125](https://github.com/open-webui/open-webui/pull/24125)

> 🧰 **Multi-worker tool update consistency.** Updated tool code now refreshes correctly across workers without requiring a full service restart, so chats no longer run stale tool versions after edits. [Commit](https://github.com/open-webui/open-webui/commit/3309f5d9f11f521c0ee97b64c59a83e3cf390bde), [#24400](https://github.com/open-webui/open-webui/issues/24400), [#24433](https://github.com/open-webui/open-webui/pull/24433)

> 📊 **Streaming token analytics accuracy.** Admin Analytics now records and aggregates token usage correctly for streaming chats across Responses API and OpenAI-compatible providers, including fallback handling for provider usage formats that use prompt and completion token keys. [Commit](https://github.com/open-webui/open-webui/commit/989d5fd4e2ce285edf4475a1e13f0981a78d3821), [Commit](https://github.com/open-webui/open-webui/commit/a32d26e61d24d9f63650faed5cb8909ed90af661), [#24217](https://github.com/open-webui/open-webui/issues/24217), [#24294](https://github.com/open-webui/open-webui/issues/24294), [#24241](https://github.com/open-webui/open-webui/issues/24241)

> 💾 **Chat control autosave persistence.** Changes to chat controls like system prompt, parameters, and attached files are now autosaved on existing chats, so edits are no longer lost when you refresh or navigate away before sending a message. [Commit](https://github.com/open-webui/open-webui/commit/a938c8ae2e45a00d2f06151fdaeaee94e54a8095), [#23897](https://github.com/open-webui/open-webui/pull/23897)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-09-5-search-and-browsing-changes-in-v0-9-3|5 Search and Browsing changes in v0.9.3]] · Search and Browsing
- [[Changes/Open WebUI/2026-05-09-10-voice-and-audio-changes-in-v0-9-3|10 Voice and Audio changes in v0.9.3]] · Voice and Audio
- [[Changes/Open WebUI/2026-05-09-8-interface-experience-changes-in-v0-9-3|8 Interface Experience changes in v0.9.3]] · Interface Experience
- [[Changes/Open WebUI/2026-05-09-4-context-window-changes-in-v0-9-3|4 Context Window changes in v0.9.3]] · Context Window
- [[Changes/Open WebUI/2026-05-09-3-apps-and-integrations-changes-in-v0-9-3|3 Apps and Integrations changes in v0.9.3]] · Apps and Integrations
- [[Changes/Open WebUI/2026-05-09-2-automation-and-scheduling-changes-in-v0-9-3|2 Automation and Scheduling changes in v0.9.3]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-05-09-22-developer-workflow-changes-in-v0-9-3|22 Developer Workflow changes in v0.9.3]] · Developer Workflow
- [[Changes/Open WebUI/2026-05-09-4-reliability-and-performance-changes-in-v0-9-3|4 Reliability and Performance changes in v0.9.3]] · Reliability and Performance
- [[Changes/Open WebUI/2026-05-09-4-account-and-access-changes-in-v0-9-3|4 Account and Access changes in v0.9.3]] · Account and Access
- [[Changes/Open WebUI/2026-05-09-sanitized-spreadsheet-html-previews-spreadsheet-previews-now-sanitize-generated|🛡️ Sanitized spreadsheet HTML previews. Spreadsheet previews now sanitize…]] · Files and Data
- [[Changes/Open WebUI/2026-05-09-9-model-support-changes-in-v0-9-3|9 Model Support changes in v0.9.3]] · Model Support
- [[Changes/Open WebUI/2026-05-09-3-safety-and-privacy-changes-in-v0-9-3|3 Safety and Privacy changes in v0.9.3]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-09-faster-memory-query-performance-per-user-memory-lookups-and-deletions-now-run-mu|⚡ Faster memory query performance. Per-user memory lookups and deletions now run…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-05-09-5-other-changes-in-v0-9-3|5 other changes in v0.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-05-08 · Raycast · [[Changes/Raycast/2026-05-08-quick-ai-gets-a-major-refresh-in-this-release-bringing-it-closer-to-the-ai-chat|Quick AI gets a major refresh in this release, bringing it closer to the AI Chat…]]
- Later: 2026-05-10 · Open WebUI · [[Changes/Open WebUI/2026-05-10-url-parser-ssrf-bypass-url-validation-now-rejects-backslash-tab-cr-and-lf-charac|🛡️ URL parser SSRF bypass. URL validation now rejects backslash, tab, CR, and LF…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-09-34b32b&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-09-5-editor-experience-changes-in-v0-9-3.md%0ACard%20ID%3A%20open-webui-2026-05-09-34b32b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->