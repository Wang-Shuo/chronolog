---
card_id: open-webui-2026-07-27-a5eb33
date: '2026-07-27'
description: "Open WebUI · 2026-07-27 · Apps and Integrations: 6 changes in v0.11.0
  — \U0001FAAA **User identity forwarded to Mistral OCR.** Document extraction through
  Mistral OCR…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1222
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 66f8629499effbff31ac654246d79f4055164f5f874c6c94f4eb6c62b410f590
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-27-a5eb33
  comparison: ''
  date: '2026-07-27'
  description: 'Open WebUI — v0.11.0: 6 Apps and Integrations changes'
  evidence:
  - quote: "\U0001FAAA **User identity forwarded to Mistral OCR.** Document extraction
      through Mistral OCR now carries the requesting user's identity when user info
      forwarding is enabled, so a gateway in front of it can attribute requests per
      user like other outbound integrations already do. [#27253](https://github.com/open-webui/open-webui/pull/27253),
      [#27250](https://github.com/open-webui/open-webui/issues/27250)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4A8 **Leaner filter handling while streaming.** Filters applied
      to a streaming reply no longer re-read their settings and each plugin's full
      source from the database for every chunk, so responses with filters enabled
      cost the server far less work. [#27228](https://github.com/open-webui/open-webui/pull/27228),
      [#27372](https://github.com/open-webui/open-webui/pull/27372), [Commit](https://github.com/open-webui/open-webui/commit/f9107edeebc7ee545d7e3c1f1b7d449c123ab398),
      [Commit](https://github.com/open-webui/open-webui/commit/f578d8d67ec2c109b0d8c38d90eaeb4448f83610),
      [Commit](https://github.com/open-webui/open-webui/commit/9acbe3aa0f258a3bda593bb98ec81c6acc458d20),
      [#27392](https://github.com/open-webui/open-webui/pull/27392)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F3D7️ **Fewer queries when building the model list.** Assembling
      the model list now makes fewer database round trips and no longer fetches every
      plugin's source code along the way, so it comes together faster. [Commit](https://github.com/open-webui/open-webui/commit/6b655689ccbdf2111620d005a8e6dedb8fb673f8),
      [#27389](https://github.com/open-webui/open-webui/pull/27389)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F51B **Multiple choice settings in plugins.** A tool or function
      can now offer a setting where you tick several options from a list, fixed or
      worked out at the time it is shown, instead of asking you to type a comma-separated
      list of allowed values. [#26884](https://github.com/open-webui/open-webui/pull/26884),
      [#26848](https://github.com/open-webui/open-webui/issues/26848)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F50C **Disable plugins entirely.** Administrators can now completely
      turn off the built-in Tools and Functions plugin surfaces through a new \"ENABLE_PLUGINS\"
      setting, which hides them across the workspace and admin areas and removes their
      execution paths. [Commit](https://github.com/open-webui/open-webui/commit/bd6e0b61c2ae073aba9556ae46c345f4749acb84),
      [Commit](https://github.com/open-webui/open-webui/commit/8e46450acd7ae11a4dee166d19a7c9833d991e79),
      [Commit](https://github.com/open-webui/open-webui/commit/951f96021a970fbd4837a4ee441565c0cf3d2824),
      [Commit](https://github.com/open-webui/open-webui/commit/252e6fd855099e1c880f4def18aa09aedbe1733a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FAA2 **Tool servers with cross-referencing types.** A tool server
      whose description defines types that refer to each other now loads its tools
      instead of failing outright, so the integration appears in model and tool selection
      again. [#27413](https://github.com/open-webui/open-webui/pull/27413), [#27239](https://github.com/open-webui/open-webui/issues/27239)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-apps-and-integrations-changes-in-v0-11-0
  source_release: open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in v0.11.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-07-27-sdk-releases|SDK Releases]]'
- '[[Changes/Lovable/2026-07-27-connect-your-app-to-posthog|Connect your app to PostHog]]'
- '[[Changes/Lovable/2026-07-27-pick-your-shopify-store-from-a-list|Pick your Shopify
  store from a list]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in v0.11.0

**Open WebUI** · 2026-07-27 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) · from [[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🪪 **User identity forwarded to Mistral OCR.** Document extraction through Mistral OCR now carries the requesting user's identity when user info forwarding is enabled, so a gateway in front of it can attribute requests per user like other outbound integrations already do. [#27253](https://github.com/open-webui/open-webui/pull/27253), [#27250](https://github.com/open-webui/open-webui/issues/27250)

> 💨 **Leaner filter handling while streaming.** Filters applied to a streaming reply no longer re-read their settings and each plugin's full source from the database for every chunk, so responses with filters enabled cost the server far less work. [#27228](https://github.com/open-webui/open-webui/pull/27228), [#27372](https://github.com/open-webui/open-webui/pull/27372), [Commit](https://github.com/open-webui/open-webui/commit/f9107edeebc7ee545d7e3c1f1b7d449c123ab398), [Commit](https://github.com/open-webui/open-webui/commit/f578d8d67ec2c109b0d8c38d90eaeb4448f83610), [Commit](https://github.com/open-webui/open-webui/commit/9acbe3aa0f258a3bda593bb98ec81c6acc458d20), [#27392](https://github.com/open-webui/open-webui/pull/27392)

> 🏗️ **Fewer queries when building the model list.** Assembling the model list now makes fewer database round trips and no longer fetches every plugin's source code along the way, so it comes together faster. [Commit](https://github.com/open-webui/open-webui/commit/6b655689ccbdf2111620d005a8e6dedb8fb673f8), [#27389](https://github.com/open-webui/open-webui/pull/27389)

> 🔛 **Multiple choice settings in plugins.** A tool or function can now offer a setting where you tick several options from a list, fixed or worked out at the time it is shown, instead of asking you to type a comma-separated list of allowed values. [#26884](https://github.com/open-webui/open-webui/pull/26884), [#26848](https://github.com/open-webui/open-webui/issues/26848)

> 🔌 **Disable plugins entirely.** Administrators can now completely turn off the built-in Tools and Functions plugin surfaces through a new "ENABLE_PLUGINS" setting, which hides them across the workspace and admin areas and removes their execution paths. [Commit](https://github.com/open-webui/open-webui/commit/bd6e0b61c2ae073aba9556ae46c345f4749acb84), [Commit](https://github.com/open-webui/open-webui/commit/8e46450acd7ae11a4dee166d19a7c9833d991e79), [Commit](https://github.com/open-webui/open-webui/commit/951f96021a970fbd4837a4ee441565c0cf3d2824), [Commit](https://github.com/open-webui/open-webui/commit/252e6fd855099e1c880f4def18aa09aedbe1733a)

> 🪢 **Tool servers with cross-referencing types.** A tool server whose description defines types that refer to each other now loads its tools instead of failing outright, so the integration appears in model and tool selection again. [#27413](https://github.com/open-webui/open-webui/pull/27413), [#27239](https://github.com/open-webui/open-webui/issues/27239)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-27-9-automation-and-scheduling-changes-in-v0-11-0|9 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-27-4-voice-and-audio-changes-in-v0-11-0|4 Voice and Audio changes in v0.11.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer Workflow changes in v0.11.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-27-19-interface-experience-changes-in-v0-11-0|19 Interface Experience changes in v0.11.0]] · Interface Experience
- [[Changes/Open WebUI/2026-07-27-7-memory-and-personalization-changes-in-v0-11-0|7 Memory and Personalization changes in v0.11.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|🤖 Sub-agents. Administrators can now enable sub-agents, which let a model hand…]] · Agent Mode
- [[Changes/Open WebUI/2026-07-27-media-types-an-extraction-engine-may-handle-administrators-can-now-list-which-im|🖼️ Media types an extraction engine may handle. Administrators can now list…]] · Multimodal Input
- [[Changes/Open WebUI/2026-07-27-15-account-and-access-changes-in-v0-11-0|15 Account and Access changes in v0.11.0]] · Account and Access
- [[Changes/Open WebUI/2026-07-27-shared-image-checkpoint-changes-only-administrators-can-now-change-the-instance|🖌️ Shared image checkpoint changes. Only administrators can now change…]] · Image Generation
- [[Changes/Open WebUI/2026-07-27-7-search-and-browsing-changes-in-v0-11-0|7 Search and Browsing changes in v0.11.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-07-27-2-collaboration-changes-in-v0-11-0|2 Collaboration changes in v0.11.0]] · Collaboration
- [[Changes/Open WebUI/2026-07-27-3-enterprise-and-administration-changes-in-v0-11-0|3 Enterprise and Administration changes in v0.11.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-07-27-9-context-window-changes-in-v0-11-0|9 Context Window changes in v0.11.0]] · Context Window
- [[Changes/Open WebUI/2026-07-27-12-reliability-and-performance-changes-in-v0-11-0|12 Reliability and Performance changes in v0.11.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-07-27-2-pricing-model-changes-in-v0-11-0|2 Pricing Model changes in v0.11.0]] · Pricing Model
- [[Changes/Open WebUI/2026-07-27-9-files-and-data-changes-in-v0-11-0|9 Files and Data changes in v0.11.0]] · Files and Data
- [[Changes/Open WebUI/2026-07-27-39-model-support-changes-in-v0-11-0|39 Model Support changes in v0.11.0]] · Model Support
- [[Changes/Open WebUI/2026-07-27-7-editor-experience-changes-in-v0-11-0|7 Editor Experience changes in v0.11.0]] · Editor Experience
- [[Changes/Open WebUI/2026-07-27-2-mobile-and-desktop-changes-in-v0-11-0|2 Mobile and Desktop changes in v0.11.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-07-27-42-other-changes-in-v0-11-0|42 other changes in v0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-07-27 · Lovable · [[Changes/Lovable/2026-07-27-pick-your-shopify-store-from-a-list|Pick your Shopify store from a list]]
- Later: 2026-07-28 · Cursor · [[Changes/Cursor/2026-07-28-plugins-mcp-servers-hooks-and-skills-to-extend-cursor-across-your-workflows|Plugins, MCP servers, hooks, and skills to extend Cursor across your workflows]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-27-a5eb33&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-27-6-apps-and-integrations-changes-in-v0-11-0.md%0ACard%20ID%3A%20open-webui-2026-07-27-a5eb33%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->