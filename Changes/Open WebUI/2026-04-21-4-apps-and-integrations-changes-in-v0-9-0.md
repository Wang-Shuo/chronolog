---
card_id: open-webui-2026-04-21-8015fc
date: '2026-04-21'
description: 'Open WebUI · 2026-04-21 · Apps and Integrations: 4 changes in v0.9.0
  — ☁️ **Azure responses support.** Azure OpenAI connections now support the newer…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2685
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8bf00237c937135ad99f13a727a8f1be6a3657ec1bc5b5319935081b8777d84a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-8015fc
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 4 Apps and Integrations changes'
  evidence:
  - quote: ☁️ **Azure responses support.** Azure OpenAI connections now support the
      newer "/openai/v1" format, enabling chat, responses, and proxy calls to work
      correctly with that endpoint style. [#23484](https://github.com/open-webui/open-webui/pull/23484)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: ⏱️ **MCP tool server timeout configuration.** Administrators can now configure
      request timeouts for MCP tool server connections via the AIOHTTP_CLIENT_TIMEOUT_TOOL_SERVER
      environment variable. [Commit](https://github.com/open-webui/open-webui/commit/10b4b86ada93cd62d994c3179ff14dfd1a6e56f0)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6D1 **Interrupted MCP cleanup stability.** Interrupted MCP tool
      calls no longer leave runaway cleanup behavior that can drive container CPU
      usage to 100%, keeping instances stable after cancellations or dropped connections.
      [#23143](https://github.com/open-webui/open-webui/issues/23143)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9E8 **Plugin async migration required.** Custom plugins for Tools,
      Functions, and Pipelines may require migration to the new async backend signatures
      after upgrading, so plugin maintainers should update handlers and database call
      patterns for compatibility and follow the 0.9.0 plugin migration guide. [Migration
      Guide](https://docs.openwebui.com/features/extensibility/plugin/migration/to-0.9.0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-apps-and-integrations-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v0.9.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-20-2-apps-and-integrations-changes-in-v2-1-116|2
  Apps and Integrations changes in v2.1.116]]'
- '[[Changes/Codex CLI/2026-04-20-28-apps-and-integrations-changes-in-rust-v0-122-0|28
  Apps and Integrations changes in rust-v0.122.0]]'
- '[[Changes/ElevenLabs/2026-04-20-sdk-releases|SDK Releases]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v0.9.0

**Open WebUI** · 2026-04-21 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ☁️ **Azure responses support.** Azure OpenAI connections now support the newer "/openai/v1" format, enabling chat, responses, and proxy calls to work correctly with that endpoint style. [#23484](https://github.com/open-webui/open-webui/pull/23484)

> ⏱️ **MCP tool server timeout configuration.** Administrators can now configure request timeouts for MCP tool server connections via the AIOHTTP_CLIENT_TIMEOUT_TOOL_SERVER environment variable. [Commit](https://github.com/open-webui/open-webui/commit/10b4b86ada93cd62d994c3179ff14dfd1a6e56f0)

> 🛑 **Interrupted MCP cleanup stability.** Interrupted MCP tool calls no longer leave runaway cleanup behavior that can drive container CPU usage to 100%, keeping instances stable after cancellations or dropped connections. [#23143](https://github.com/open-webui/open-webui/issues/23143)

> 🧨 **Plugin async migration required.** Custom plugins for Tools, Functions, and Pipelines may require migration to the new async backend signatures after upgrading, so plugin maintainers should update handlers and database call patterns for compatibility and follow the 0.9.0 plugin migration guide. [Migration Guide](https://docs.openwebui.com/features/extensibility/plugin/migration/to-0.9.0)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-3-files-and-data-changes-in-v0-9-0|3 Files and Data changes in v0.9.0]] · Files and Data
- [[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation changes in v0.9.0]] · Image Generation
- [[Changes/Open WebUI/2026-04-21-28-model-support-changes-in-v0-9-0|28 Model Support changes in v0.9.0]] · Model Support
- [[Changes/Open WebUI/2026-04-21-5-editor-experience-changes-in-v0-9-0|5 Editor Experience changes in v0.9.0]] · Editor Experience
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-8-context-window-changes-in-v0-9-0|8 Context Window changes in v0.9.0]] · Context Window
- [[Changes/Open WebUI/2026-04-21-24-reliability-and-performance-changes-in-v0-9-0|24 Reliability and Performance changes in v0.9.0]] · Reliability and Performance
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
## Nearby in Apps and Integrations

- Earlier: 2026-04-20 · ElevenLabs · [[Changes/ElevenLabs/2026-04-20-sdk-releases|SDK Releases]]
- Later: 2026-04-21 · OpenCode · [[Changes/OpenCode/2026-04-21-2-apps-and-integrations-changes-in-v1-14-20|2 Apps and Integrations changes in v1.14.20]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-8015fc&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-4-apps-and-integrations-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-8015fc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->