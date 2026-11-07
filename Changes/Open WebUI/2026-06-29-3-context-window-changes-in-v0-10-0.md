---
card_id: open-webui-2026-06-29-daae68
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Context Window: 3 changes in v0.10.0 — \U0001F5DC️
  **Automatic context compaction for long chats.** Conversations that grow past a…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1152
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 562166d2b5ae07cdb6b4a1214b5090c989636a2e374884c39b0ac16e6716d6e0
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-daae68
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 3 Context Window changes'
  evidence:
  - quote: "\U0001F5DC️ **Automatic context compaction for long chats.** Conversations
      that grow past a configurable token threshold can now be summarized automatically
      so they stay within a model's context window, with a notification shown while
      it happens; administrators can enable it, set the threshold, customize the summarization
      prompt, and lower the threshold per model. It is off by default. [Commit](https://github.com/open-webui/open-webui/commit/3f0c0e0a0ddff841b015f96f9649c6999a435c73),
      [Commit](https://github.com/open-webui/open-webui/commit/7f08376f0c06e1a7fba983a2fa93deb8dfbe7cb0),
      [Commit](https://github.com/open-webui/open-webui/commit/8934bfb04bf366aece872028944e280c25e36d3e),
      [#19594](https://github.com/open-webui/open-webui/issues/19594)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F50E **Chat actions in search.** The search dialog now offers a
      context menu on each result, so you can act on a chat directly from search.
      [#25490](https://github.com/open-webui/open-webui/pull/25490)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F39A️ **Default model parameters apply to requests.** Default model
      parameters are now applied to outbound requests, so settings like temperature
      and the context window take effect as configured. [Commit](https://github.com/open-webui/open-webui/commit/cd6cc39c6d),
      [Commit](https://github.com/open-webui/open-webui/commit/19db873603215773f9a64e03785a1a076dc6c8a8),
      [#24930](https://github.com/open-webui/open-webui/issues/24930), [#26209](https://github.com/open-webui/open-webui/issues/26209)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-context-window-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: context-window
  title: 3 Context Window changes in v0.10.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-06-25-2-context-window-changes-in-rust-v0-142-2|2 Context
  Window changes in rust-v0.142.2]]'
- '[[Changes/Dify/2026-06-25-3-context-window-changes-in-1-15-0|3 Context Window changes
  in 1.15.0]]'
- '[[Changes/Google Antigravity/2026-06-25-improved-readability-of-context-pills-by-truncating-long-labels-and-adding-hover|Improved
  readability of context pills by truncating long labels and adding hover…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: context-window
title: 3 Context Window changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Context Window changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗜️ **Automatic context compaction for long chats.** Conversations that grow past a configurable token threshold can now be summarized automatically so they stay within a model's context window, with a notification shown while it happens; administrators can enable it, set the threshold, customize the summarization prompt, and lower the threshold per model. It is off by default. [Commit](https://github.com/open-webui/open-webui/commit/3f0c0e0a0ddff841b015f96f9649c6999a435c73), [Commit](https://github.com/open-webui/open-webui/commit/7f08376f0c06e1a7fba983a2fa93deb8dfbe7cb0), [Commit](https://github.com/open-webui/open-webui/commit/8934bfb04bf366aece872028944e280c25e36d3e), [#19594](https://github.com/open-webui/open-webui/issues/19594)

> 🔎 **Chat actions in search.** The search dialog now offers a context menu on each result, so you can act on a chat directly from search. [#25490](https://github.com/open-webui/open-webui/pull/25490)

> 🎚️ **Default model parameters apply to requests.** Default model parameters are now applied to outbound requests, so settings like temperature and the context window take effect as configured. [Commit](https://github.com/open-webui/open-webui/commit/cd6cc39c6d), [Commit](https://github.com/open-webui/open-webui/commit/19db873603215773f9a64e03785a1a076dc6c8a8), [#24930](https://github.com/open-webui/open-webui/issues/24930), [#26209](https://github.com/open-webui/open-webui/issues/26209)

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
- [[Changes/Open WebUI/2026-06-29-25-model-support-changes-in-v0-10-0|25 Model Support changes in v0.10.0]] · Model Support
- [[Changes/Open WebUI/2026-06-29-6-reliability-and-performance-changes-in-v0-10-0|6 Reliability and Performance changes in v0.10.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-29-4-mobile-and-desktop-changes-in-v0-10-0|4 Mobile and Desktop changes in v0.10.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-29-better-screen-reader-labels-on-toggles-integration-and-switch-toggles-now-expose|♿ Better screen-reader labels on toggles. Integration and switch toggles now…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-29-16-safety-and-privacy-changes-in-v0-10-0|16 Safety and Privacy changes in v0.10.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-29-2-pricing-model-changes-in-v0-10-0|2 Pricing Model changes in v0.10.0]] · Pricing Model
- [[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-29-9-account-and-access-changes-in-v0-10-0|9 Account and Access changes in v0.10.0]] · Account and Access
- [[Changes/Open WebUI/2026-06-29-usable-chat-input-on-mobile-with-many-tools-when-skills-tools-terminal-web-searc|📱 Usable chat input on mobile with many tools. When skills, tools, terminal, web…]] · Image Generation
- [[Changes/Open WebUI/2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0|6 Automation and Scheduling changes in v0.10.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer Workflow changes in v0.10.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-29-10-editor-experience-changes-in-v0-10-0|10 Editor Experience changes in v0.10.0]] · Editor Experience
- [[Changes/Open WebUI/2026-06-29-29-other-changes-in-v0-10-0|29 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-06-25 · Google Antigravity · [[Changes/Google Antigravity/2026-06-25-improved-readability-of-context-pills-by-truncating-long-labels-and-adding-hover|Improved readability of context pills by truncating long labels and adding hover…]]
- Later: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-keep-session-store-searches-and-context-lookups-responsive|Keep session-store searches and context lookups responsive]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-daae68&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-3-context-window-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-daae68%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->