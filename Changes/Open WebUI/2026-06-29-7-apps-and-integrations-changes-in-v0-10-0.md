---
card_id: open-webui-2026-06-29-a85e1b
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Apps and Integrations: 7 changes in v0.10.0
  — \U0001F9E9 **New plugin primitive: the Event function.** Where pipe, filter, and
  action…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1194
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5969ae9b7137663a4b4e419a0bb6dcbfb9858977f328f713ce65e42ab578802f
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-a85e1b
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 7 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F9E9 **New plugin primitive: the Event function.** Where pipe, filter,
      and action functions all run inside a conversation, the new Event function is
      the first primitive that hooks into the system itself: it runs your own Python
      in response to events emitted across the whole application — sign-ups, configuration
      changes, file uploads, role changes, deletions, startup and shutdown, and more.
      That makes a new class of behavior possible directly inside Open WebUI, from
      onboarding and access control to auditing, lifecycle automation, and external
      integrations. Comes with starter boilerplate in the function editor. [Commit](https://github.com/open-webui/open-webui/commit/e124c2656a4c2092b070e570e35b2f0fb7f584de),
      [Docs](https://docs.openwebui.com/features/extensibility/plugin/functions/event)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F50C **Control the OAuth resource parameter for MCP connectors.**
      MCP connectors can now be set to always send, never send, or automatically decide
      whether to include the OAuth resource parameter, so they work with providers
      that reject it. [Commit](https://github.com/open-webui/open-webui/commit/5576e6ed8a80a4032b7c6cb3ee0cda0254019355)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001FAAA **MCP connectors request least-privilege scopes.** MCP connectors
      that register dynamically over OAuth now request only the scopes for the specific
      resource rather than the authorization server's full catalog. [#25958](https://github.com/open-webui/open-webui/pull/25958)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F517 **Whitespace in names no longer breaks MCP connections.** User
      name and info headers are now trimmed before being forwarded, fixing MCP connection
      failures when a display name contained leading or trailing whitespace. [#26182](https://github.com/open-webui/open-webui/pull/26182),
      [#26181](https://github.com/open-webui/open-webui/issues/26181)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F9E9 **MCP resource results come through.** Tool results that return
      resource content — including binary blobs and URI references — are no longer
      silently dropped, and image results are attached as files. [#25260](https://github.com/open-webui/open-webui/pull/25260),
      [#24038](https://github.com/open-webui/open-webui/issues/24038), [Commit](https://github.com/open-webui/open-webui/commit/783205a965c556815fae84b64d74f26a2e5e5729)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F50C **Cancelling an MCP request no longer errors.** Stopping a
      response that was using MCP tools now shuts the connection down cleanly instead
      of surfacing a server error. [Commit](https://github.com/open-webui/open-webui/commit/ff5cec43bd360829cfdcc6a5253d1ba63f236b7f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001FAAA **Static MCP connectors recover missing OAuth details.** MCP
      connectors configured with static OAuth credentials now fill in a missing scope
      or resource from the server's published metadata, so they connect correctly
      instead of failing when those values were left out. [Commit](https://github.com/open-webui/open-webui/commit/88901bfa041ddcceab1cd4a97f08f0b43835eb05),
      [#25898](https://github.com/open-webui/open-webui/issues/25898)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-apps-and-integrations-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: apps-integrations
  title: 7 Apps and Integrations changes in v0.10.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-29-remote-control-is-now-disabled-when-anthropic-base-url-points-at-a-non-anthropic|Remote
  Control is now disabled when ANTHROPIC_BASE_URL points at a non-Anthropic…]]'
- '[[Changes/ElevenLabs/2026-06-29-sdk-releases|SDK Releases]]'
- '[[Changes/Lovable/2026-06-29-app-connector-x|App connector: X]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: apps-integrations
title: 7 Apps and Integrations changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Apps and Integrations changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧩 **New plugin primitive: the Event function.** Where pipe, filter, and action functions all run inside a conversation, the new Event function is the first primitive that hooks into the system itself: it runs your own Python in response to events emitted across the whole application — sign-ups, configuration changes, file uploads, role changes, deletions, startup and shutdown, and more. That makes a new class of behavior possible directly inside Open WebUI, from onboarding and access control to auditing, lifecycle automation, and external integrations. Comes with starter boilerplate in the function editor. [Commit](https://github.com/open-webui/open-webui/commit/e124c2656a4c2092b070e570e35b2f0fb7f584de), [Docs](https://docs.openwebui.com/features/extensibility/plugin/functions/event)

> 🔌 **Control the OAuth resource parameter for MCP connectors.** MCP connectors can now be set to always send, never send, or automatically decide whether to include the OAuth resource parameter, so they work with providers that reject it. [Commit](https://github.com/open-webui/open-webui/commit/5576e6ed8a80a4032b7c6cb3ee0cda0254019355)

> 🪪 **MCP connectors request least-privilege scopes.** MCP connectors that register dynamically over OAuth now request only the scopes for the specific resource rather than the authorization server's full catalog. [#25958](https://github.com/open-webui/open-webui/pull/25958)

> 🔗 **Whitespace in names no longer breaks MCP connections.** User name and info headers are now trimmed before being forwarded, fixing MCP connection failures when a display name contained leading or trailing whitespace. [#26182](https://github.com/open-webui/open-webui/pull/26182), [#26181](https://github.com/open-webui/open-webui/issues/26181)

> 🧩 **MCP resource results come through.** Tool results that return resource content — including binary blobs and URI references — are no longer silently dropped, and image results are attached as files. [#25260](https://github.com/open-webui/open-webui/pull/25260), [#24038](https://github.com/open-webui/open-webui/issues/24038), [Commit](https://github.com/open-webui/open-webui/commit/783205a965c556815fae84b64d74f26a2e5e5729)

> 🔌 **Cancelling an MCP request no longer errors.** Stopping a response that was using MCP tools now shuts the connection down cleanly instead of surfacing a server error. [Commit](https://github.com/open-webui/open-webui/commit/ff5cec43bd360829cfdcc6a5253d1ba63f236b7f)

> 🪪 **Static MCP connectors recover missing OAuth details.** MCP connectors configured with static OAuth credentials now fill in a missing scope or resource from the server's published metadata, so they connect correctly instead of failing when those values were left out. [Commit](https://github.com/open-webui/open-webui/commit/88901bfa041ddcceab1cd4a97f08f0b43835eb05), [#25898](https://github.com/open-webui/open-webui/issues/25898)

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
- [[Changes/Open WebUI/2026-06-29-9-account-and-access-changes-in-v0-10-0|9 Account and Access changes in v0.10.0]] · Account and Access
- [[Changes/Open WebUI/2026-06-29-usable-chat-input-on-mobile-with-many-tools-when-skills-tools-terminal-web-searc|📱 Usable chat input on mobile with many tools. When skills, tools, terminal, web…]] · Image Generation
- [[Changes/Open WebUI/2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0|6 Automation and Scheduling changes in v0.10.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-29-3-context-window-changes-in-v0-10-0|3 Context Window changes in v0.10.0]] · Context Window
- [[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer Workflow changes in v0.10.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-29-10-editor-experience-changes-in-v0-10-0|10 Editor Experience changes in v0.10.0]] · Editor Experience
- [[Changes/Open WebUI/2026-06-29-29-other-changes-in-v0-10-0|29 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-06-29 · Lovable · [[Changes/Lovable/2026-06-29-app-connector-x|App connector: X]]
- Later: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-9-apps-and-integrations-changes-in-v1-0-66|9 Apps and Integrations changes in v1.0.66]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-a85e1b&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-7-apps-and-integrations-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-a85e1b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->