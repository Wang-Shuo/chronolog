---
card_id: openclaw-2026-10-10-6d19de
date: '2026-10-10'
description: 'OpenClaw · 2026-10-10 · Search and Browsing: 3 changes in v2026.10.1
  — On iOS you can browse cached Active and Snoozed lists offline, while archives
  and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1297
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 84a27038aba0168bfb337cb9d3c74fa20ab94aec44dc5382cf87f488b869b2d6
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-10-6d19de
  comparison: ''
  date: '2026-10-10'
  description: 'OpenClaw — v2026.10.1: 3 Search and Browsing changes'
  evidence:
  - quote: On iOS you can browse cached Active and Snoozed lists offline, while archives
      and changes require a connection. Android may briefly show an old snoozed row
      when starting offline. See iOS conversation controls and the Mac chat guide
      .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Agents API operators can choose which supported native tools a hosted conversation
      uses, including web-search options . Restart the Gateway and start or reset
      a session after changing them. Your list replaces native defaults, leaving OpenClaw
      and MCP permissions separate. An empty list removes web search but leaves programmatic
      calling enabled; disable it explicitly using the programmatic tool-calling guide
      .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: You can check whether a skill was found, meets its prerequisites, and is
      actually visible to the agent using skill troubleshooting . After the next agent
      turn, /context list shows the catalog that reached the prompt. Browsing and
      choosing from your personal skill library also moves database queries into the
      background.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 3-search-and-browsing-changes-in-v2026-10-1
  source_release: openclaw-2026-10-10-v2026-10-1-d64e4e93
  source_type: openclaw_changelog
  theme: search-browsing
  title: 3 Search and Browsing changes in v2026.10.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-05-changed-the-interactive-session-s-websearch-budget-to-refill-over-time-100-calls|Changed
  the interactive session''s WebSearch budget to refill over time (100 calls/hour]]'
- '[[Changes/Codex CLI/2026-10-07-3-search-and-browsing-changes-in-rust-v0-161-0|3
  Search and Browsing changes in rust-v0.161.0]]'
- '[[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search
  and Browsing changes in v0.12.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|openclaw-2026-10-10-v2026-10-1-d64e4e93]]'
source_type: openclaw_changelog
theme: search-browsing
title: 3 Search and Browsing changes in v2026.10.1
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Search and Browsing changes in v2026.10.1

**OpenClaw** · 2026-10-10 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.1) · from [[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> On iOS you can browse cached Active and Snoozed lists offline, while archives and changes require a connection. Android may briefly show an old snoozed row when starting offline. See iOS conversation controls and the Mac chat guide .

> Agents API operators can choose which supported native tools a hosted conversation uses, including web-search options . Restart the Gateway and start or reset a session after changing them. Your list replaces native defaults, leaving OpenClaw and MCP permissions separate. An empty list removes web search but leaves programmatic calling enabled; disable it explicitly using the programmatic tool-calling guide .

> You can check whether a skill was found, meets its prerequisites, and is actually visible to the agent using skill troubleshooting . After the next agent turn, /context list shows the catalog that reached the prompt. Browsing and choosing from your personal skill library also moves database queries into the background.

Source: https://docs.openclaw.ai/releases/2026.10.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-10-2-reliability-and-performance-changes-in-v2026-10-1|2 Reliability and Performance changes in v2026.10.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1|13 Memory and Personalization changes in v2026.10.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-10-96-apps-and-integrations-changes-in-v2026-10-1|96 Apps and Integrations changes in v2026.10.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-10-15-mobile-and-desktop-changes-in-v2026-10-1|15 Mobile and Desktop changes in v2026.10.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-10-12-context-window-changes-in-v2026-10-1|12 Context Window changes in v2026.10.1]] · Context Window
- [[Changes/OpenClaw/2026-10-10-4-pricing-model-changes-in-v2026-10-1|4 Pricing Model changes in v2026.10.1]] · Pricing Model
- [[Changes/OpenClaw/2026-10-10-18-account-and-access-changes-in-v2026-10-1|18 Account and Access changes in v2026.10.1]] · Account and Access
- [[Changes/OpenClaw/2026-10-10-18-model-support-changes-in-v2026-10-1|18 Model Support changes in v2026.10.1]] · Model Support
- [[Changes/OpenClaw/2026-10-10-20-safety-and-privacy-changes-in-v2026-10-1|20 Safety and Privacy changes in v2026.10.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-10-plugin-authors-can-await-session-history-extension-changes-and-replay-metadata-t|Plugin authors can await session history, extension changes and replay metadata]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-10-2-accessibility-and-localization-changes-in-v2026-10-1|2 Accessibility and Localization changes in v2026.10.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-10-10-image-generation-with-oauth-can-retry-using-a-supported-openai-chat-model-in-age|Image generation with OAuth can retry using a supported OpenAI chat model…]] · Image Generation
- [[Changes/OpenClaw/2026-10-10-10-editor-experience-changes-in-v2026-10-1|10 Editor Experience changes in v2026.10.1]] · Editor Experience
- [[Changes/OpenClaw/2026-10-10-2-files-and-data-changes-in-v2026-10-1|2 Files and Data changes in v2026.10.1]] · Files and Data
- [[Changes/OpenClaw/2026-10-10-8-voice-and-audio-changes-in-v2026-10-1|8 Voice and Audio changes in v2026.10.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-10-27-agent-mode-changes-in-v2026-10-1|27 Agent Mode changes in v2026.10.1]] · Agent Mode
- [[Changes/OpenClaw/2026-10-10-12-collaboration-changes-in-v2026-10-1|12 Collaboration changes in v2026.10.1]] · Collaboration
- [[Changes/OpenClaw/2026-10-10-video-previews-new-video-previews-can-download-media-before-play|Video previews: New video previews can download media before Play]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-10-11-developer-workflow-changes-in-v2026-10-1|11 Developer Workflow changes in v2026.10.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-10-5-enterprise-and-administration-changes-in-v2026-10-1|5 Enterprise and Administration changes in v2026.10.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-10-20-interface-experience-changes-in-v2026-10-1|20 Interface Experience changes in v2026.10.1]] · Interface Experience
- [[Changes/OpenClaw/2026-10-10-10-automation-and-scheduling-changes-in-v2026-10-1|10 Automation and Scheduling changes in v2026.10.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-10-112-other-changes-in-v2026-10-1|112 other changes in v2026.10.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-10-10 · Open WebUI · [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]]
- Later: 2026-10-14 · Open WebUI · [[Changes/Open WebUI/2026-10-14-tools-picked-in-new-chats-tools-picked-from-the-integrations-menu-the-web-search|🧰 Tools picked in new chats. Tools picked from the Integrations menu, the Web…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-10-6d19de&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-10-3-search-and-browsing-changes-in-v2026-10-1.md%0ACard%20ID%3A%20openclaw-2026-10-10-6d19de%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->