---
card_id: open-webui-2026-02-12-64ec1d
date: '2026-02-12'
description: "Open WebUI · 2026-02-12 · Context Window: 5 changes in v0.8.0 — \U0001F3AF
  **Experimental support for Skills.** Open WebUI now supports the Skill standard
  — allowing…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2339
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 356b03c299f989b7ce2cad1280728d05377157cc9f058a94649b8209cb17fb67
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-12-64ec1d
  comparison: ''
  date: '2026-02-12'
  description: 'Open WebUI — v0.8.0: 5 Context Window changes'
  evidence:
  - quote: "\U0001F3AF **Experimental support for Skills.** Open WebUI now supports
      the Skill standard — allowing users to create and manage reusable AI skills
      with detailed instructions, reference them in chats using the \"$\" command,
      or attach them to specific models for automatic context in conversations. [#21312](https://github.com/open-webui/open-webui/pull/21312)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F9EA **Experimental support for Open Responses protocol.** Connections
      can now be configured to use the experimental Open Responses protocol instead
      of Chat Completions, enabling native support for extended thinking, streaming
      reasoning tokens, and richer tool call handling for compatible providers. [Commit](https://github.com/open-webui/open-webui/commit/d2c695eb11ddca9fc93499bb0c3fcafcff7099b5),
      [Commit](https://github.com/open-webui/open-webui/commit/90a057f4005c000bda6ff8703e13e529190af73a),
      [Commit](https://github.com/open-webui/open-webui/commit/0dc74a8a2e7adb76fb503ef0cd3c02daddd2f4bb),
      [Commit](https://github.com/open-webui/open-webui/commit/ea9c58ea80646cef05e06d0beaf5e81cc2f78cb1),
      [Commit](https://github.com/open-webui/open-webui/commit/6ffce4bccdc13b8b61a8b286e34094c981932eda),
      [Commit](https://github.com/open-webui/open-webui/commit/6719558150920f570d8febe021da65903e53c976),
      [Commit](https://github.com/open-webui/open-webui/commit/117c091b95a1b1a76a31c31b97304bac289d6f18),
      [Commit](https://github.com/open-webui/open-webui/commit/aa8c2959ca8476f269786e1317fb6d2938abd3f9),
      [Commit](https://github.com/open-webui/open-webui/commit/e2d09ac36174de48a7d85bafc8d3291c9ffe44cd)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F6E0️ **Dynamic dropdown valve fields.** Tool and function developers
      can now create dropdown fields with dynamically-generated options that update
      based on runtime context, such as available models or user permissions. [Commit](https://github.com/open-webui/open-webui/commit/474427c67e953bb9f7d122757a756a639214e0b2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4BE **Inline image context exhaustion fix.** Inline images no longer
      exhaust the model's context window by including their full base64 data in chat
      metadata, preventing premature context exhaustion with image-heavy conversations.
      [#20916](https://github.com/open-webui/open-webui/pull/20916)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F4BE **Duplicate inline image context fix.** Inline images no longer
      exhaust the model's context window by including their full base64 data in chat
      metadata, preventing premature context exhaustion with image-heavy conversations.
      [#20916](https://github.com/open-webui/open-webui/pull/20916)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-context-window-changes-in-v0-8-0
  source_release: open-webui-2026-02-12-v0-8-0-github-285910626-490914ba
  source_type: github_releases
  theme: context-window
  title: 5 Context Window changes in v0.8.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-02-11-add-additional-context-overflow-cases-and-remove-overcorrecting-ones|Add
  additional context overflow cases and remove overcorrecting ones]]'
- '[[Changes/OpenCode/2026-02-11-terminal-add-mode-specific-input-placeholders-to-improve-context-aware-prompts|Terminal
  Add mode-specific input placeholders to improve context-aware prompts]]'
- '[[Changes/Codex CLI/2026-02-12-3-context-window-changes-in-rust-v0-100-0|3 Context
  Window changes in rust-v0.100.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|open-webui-2026-02-12-v0-8-0-github-285910626-490914ba]]'
source_type: github_releases
theme: context-window
title: 5 Context Window changes in v0.8.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Context Window changes in v0.8.0

**Open WebUI** · 2026-02-12 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.0) · from [[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|v0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎯 **Experimental support for Skills.** Open WebUI now supports the Skill standard — allowing users to create and manage reusable AI skills with detailed instructions, reference them in chats using the "$" command, or attach them to specific models for automatic context in conversations. [#21312](https://github.com/open-webui/open-webui/pull/21312)

> 🧪 **Experimental support for Open Responses protocol.** Connections can now be configured to use the experimental Open Responses protocol instead of Chat Completions, enabling native support for extended thinking, streaming reasoning tokens, and richer tool call handling for compatible providers. [Commit](https://github.com/open-webui/open-webui/commit/d2c695eb11ddca9fc93499bb0c3fcafcff7099b5), [Commit](https://github.com/open-webui/open-webui/commit/90a057f4005c000bda6ff8703e13e529190af73a), [Commit](https://github.com/open-webui/open-webui/commit/0dc74a8a2e7adb76fb503ef0cd3c02daddd2f4bb), [Commit](https://github.com/open-webui/open-webui/commit/ea9c58ea80646cef05e06d0beaf5e81cc2f78cb1), [Commit](https://github.com/open-webui/open-webui/commit/6ffce4bccdc13b8b61a8b286e34094c981932eda), [Commit](https://github.com/open-webui/open-webui/commit/6719558150920f570d8febe021da65903e53c976), [Commit](https://github.com/open-webui/open-webui/commit/117c091b95a1b1a76a31c31b97304bac289d6f18), [Commit](https://github.com/open-webui/open-webui/commit/aa8c2959ca8476f269786e1317fb6d2938abd3f9), [Commit](https://github.com/open-webui/open-webui/commit/e2d09ac36174de48a7d85bafc8d3291c9ffe44cd)

> 🛠️ **Dynamic dropdown valve fields.** Tool and function developers can now create dropdown fields with dynamically-generated options that update based on runtime context, such as available models or user permissions. [Commit](https://github.com/open-webui/open-webui/commit/474427c67e953bb9f7d122757a756a639214e0b2)

> 💾 **Inline image context exhaustion fix.** Inline images no longer exhaust the model's context window by including their full base64 data in chat metadata, preventing premature context exhaustion with image-heavy conversations. [#20916](https://github.com/open-webui/open-webui/pull/20916)

> 💾 **Duplicate inline image context fix.** Inline images no longer exhaust the model's context window by including their full base64 data in chat metadata, preventing premature context exhaustion with image-heavy conversations. [#20916](https://github.com/open-webui/open-webui/pull/20916)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-12-16-reliability-and-performance-changes-in-v0-8-0|16 Reliability and Performance changes in v0.8.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-12-audio-service-timeout-handling-audio-transcription-and-text-to-speech-requests-n|🔌 Audio service timeout handling. Audio transcription and text-to-speech…]] · Voice and Audio
- [[Changes/Open WebUI/2026-02-12-2-editor-experience-changes-in-v0-8-0|2 Editor Experience changes in v0.8.0]] · Editor Experience
- [[Changes/Open WebUI/2026-02-12-5-safety-and-privacy-changes-in-v0-8-0|5 Safety and Privacy changes in v0.8.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-12-19-model-support-changes-in-v0-8-0|19 Model Support changes in v0.8.0]] · Model Support
- [[Changes/Open WebUI/2026-02-12-27-developer-workflow-changes-in-v0-8-0|27 Developer Workflow changes in v0.8.0]] · Developer Workflow
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
## Nearby in Context Window

- Earlier: 2026-02-12 · Codex CLI · [[Changes/Codex CLI/2026-02-12-3-context-window-changes-in-rust-v0-100-0|3 Context Window changes in rust-v0.100.0]]
- Later: 2026-02-12 · OpenCode · [[Changes/OpenCode/2026-02-12-desktop-more-defensive-session-context-metrics-handling-in-app|Desktop More defensive session context metrics handling in app]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-12-64ec1d&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-12-5-context-window-changes-in-v0-8-0.md%0ACard%20ID%3A%20open-webui-2026-02-12-64ec1d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->