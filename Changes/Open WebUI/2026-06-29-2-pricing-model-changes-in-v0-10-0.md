---
card_id: open-webui-2026-06-29-857242
date: '2026-06-29'
description: 'Open WebUI · 2026-06-29 · Pricing Model: 2 changes in v0.10.0 — ⚡ **Hidden
  tool-call details cost nothing.** When tool-call arguments are collapsed, they are…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily
    limit: To ensure a high-quality experience for all ChatGPT users, we…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1292
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1d99f90998b9e69f40bef465bb742b30c410df3b2b2cb62df648325ac584521b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-857242
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 2 Pricing Model changes'
  evidence:
  - quote: ⚡ **Hidden tool-call details cost nothing.** When tool-call arguments are
      collapsed, they are no longer rendered behind the scenes, noticeably speeding
      up chats with heavy tool use. [Commit](https://github.com/open-webui/open-webui/commit/b7934e918223ec0a9e972accd647a8654e503156),
      [#26147](https://github.com/open-webui/open-webui/pull/26147)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4CA **Token usage and cost stats no longer wiped by background
      tasks.** A response's token usage and cost are now preserved when background
      tasks like title, tag, and follow-up generation run on the same chat, instead
      of being overwritten. [Commit](https://github.com/open-webui/open-webui/commit/95391221dfabbfcd9090ab472b1c02a4c75c0387)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-pricing-model-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: pricing-model
  title: 2 Pricing Model changes in v0.10.0
  type: change
related_changes:
- '[[Changes/Lovable/2026-06-25-let-lovable-debug-and-improve-your-app-s-ai-features|Let
  Lovable debug and improve your app''s AI features]]'
- '[[Changes/Cline/2026-06-26-add-clinepass-to-the-vs-code-extension-including-onboarding-provider-selection-s|Add
  ClinePass to the VS Code extension, including onboarding, provider selection…]]'
- '[[Changes/v0/2026-06-26-2-pricing-model-changes-in-platform-api-v2-mcp-chat-tools|2
  Pricing Model changes in Platform API v2, MCP chat tools…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: pricing-model
title: 2 Pricing Model changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Pricing Model changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/pricing-model|Pricing Model]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⚡ **Hidden tool-call details cost nothing.** When tool-call arguments are collapsed, they are no longer rendered behind the scenes, noticeably speeding up chats with heavy tool use. [Commit](https://github.com/open-webui/open-webui/commit/b7934e918223ec0a9e972accd647a8654e503156), [#26147](https://github.com/open-webui/open-webui/pull/26147)

> 📊 **Token usage and cost stats no longer wiped by background tasks.** A response's token usage and cost are now preserved when background tasks like title, tag, and follow-up generation run on the same chat, instead of being overwritten. [Commit](https://github.com/open-webui/open-webui/commit/95391221dfabbfcd9090ab472b1c02a4c75c0387)

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
- [[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-29-9-account-and-access-changes-in-v0-10-0|9 Account and Access changes in v0.10.0]] · Account and Access
- [[Changes/Open WebUI/2026-06-29-usable-chat-input-on-mobile-with-many-tools-when-skills-tools-terminal-web-searc|📱 Usable chat input on mobile with many tools. When skills, tools, terminal, web…]] · Image Generation
- [[Changes/Open WebUI/2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0|6 Automation and Scheduling changes in v0.10.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-29-3-context-window-changes-in-v0-10-0|3 Context Window changes in v0.10.0]] · Context Window
- [[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer Workflow changes in v0.10.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-29-10-editor-experience-changes-in-v0-10-0|10 Editor Experience changes in v0.10.0]] · Editor Experience
- [[Changes/Open WebUI/2026-06-29-29-other-changes-in-v0-10-0|29 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-06-26 · v0 · [[Changes/v0/2026-06-26-2-pricing-model-changes-in-platform-api-v2-mcp-chat-tools|2 Pricing Model changes in Platform API v2, MCP chat tools…]]
- Later: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-configure-subagent-concurrency-and-depth-limits-in-settings-usage-based-billing|Configure subagent concurrency and depth limits in /settings (usage-based billing users)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily limit: To ensure a high-quality experience for all ChatGPT users, we…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-857242&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-2-pricing-model-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-857242%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->