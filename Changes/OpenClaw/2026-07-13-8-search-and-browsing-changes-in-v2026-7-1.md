---
card_id: openclaw-2026-07-13-e25c69
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Search and Browsing: 8 changes in v2026.7.1
  — iPhone and iPad chat now opens with the last known conversation and lets users
  browse…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1208
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b3833cd9c8ed74ed47244b5cc5ce0f897c7e18418ebe5c6f138e9bdbe73f3572
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-e25c69
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 8 Search and Browsing changes'
  evidence:
  - quote: 'iPhone and iPad chat now opens with the last known conversation and lets
      users browse recent cached sessions while the Gateway is unavailable. #100219'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Trusted Gateway clients can now browse workspace directories and preview
      supported files, enabling the iOS and Android apps to inspect and share agent
      output without SSH. #100738'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Android Files card now lets users browse the active agent workspace,
      preview text and images, and share output directly from their phone. #100776'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Supported non-English native apps now translate workspace file browsing
      and sharing, image preview failures, offline status, and custom Gateway header
      controls. 6b99fd9
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS chat now lets users browse, filter, and select available commands
      and skills from the composer instead of memorizing exact slash commands. #99426
      Thanks @solvely-colin, @viczhang6.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iPhone and iPad users can now browse an agent workspace, preview generated
      files, logs, and configuration, and share a file without returning to the host
      computer. #100767'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Scheduled jobs that permit web_search now report that no usable search
      provider is selected instead of completing with an unusable result. #97677 Thanks
      @lilan0125, @riazrahaman.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agent-side web_search now sees the configured provider in the active runtime,
      so Gateway and channel sessions can keep using providers such as Brave without
      a restart. #88684 Thanks @alexzhu0, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 8-search-and-browsing-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: search-browsing
  title: 8 Search and Browsing changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-01-browse-resume-and-switch-between-sessions-from-the-agents-screen|Browse,
  resume, and switch between sessions from the agents screen]]'
- "[[Changes/Open WebUI/2026-07-01-web-search-domain-filtering-domain-allow-and-block-rules-for-web-search-results|\U0001F512
  Web search domain filtering. Domain allow and block rules for web search…]]"
- '[[Changes/Codex CLI/2026-07-09-31525-core-migrate-standalone-web-search-to-extension-owned-turn-items-owenlin0|♯31525
  core: migrate standalone web search to extension-owned turn items @owenlin0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: search-browsing
title: 8 Search and Browsing changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Search and Browsing changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> iPhone and iPad chat now opens with the last known conversation and lets users browse recent cached sessions while the Gateway is unavailable. #100219

> Trusted Gateway clients can now browse workspace directories and preview supported files, enabling the iOS and Android apps to inspect and share agent output without SSH. #100738

> The Android Files card now lets users browse the active agent workspace, preview text and images, and share output directly from their phone. #100776

> Supported non-English native apps now translate workspace file browsing and sharing, image preview failures, offline status, and custom Gateway header controls. 6b99fd9

> iOS chat now lets users browse, filter, and select available commands and skills from the composer instead of memorizing exact slash commands. #99426 Thanks @solvely-colin, @viczhang6.

> iPhone and iPad users can now browse an agent workspace, preview generated files, logs, and configuration, and share a file without returning to the host computer. #100767

> Scheduled jobs that permit web_search now report that no usable search provider is selected instead of completing with an unusable result. #97677 Thanks @lilan0125, @riazrahaman.

> Agent-side web_search now sees the configured provider in the active runtime, so Gateway and channel sessions can keep using providers such as Brave without a restart. #88684 Thanks @alexzhu0, @vincentkoc.

Source: https://docs.openclaw.ai/releases/2026.7.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-07-13-5-projects-and-workspaces-changes-in-v2026-7-1|5 Projects and Workspaces changes in v2026.7.1]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-07-13-99-developer-workflow-changes-in-v2026-7-1|99 Developer Workflow changes in v2026.7.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-07-13-69-context-window-changes-in-v2026-7-1|69 Context Window changes in v2026.7.1]] · Context Window
- [[Changes/OpenClaw/2026-07-13-10-accessibility-and-localization-changes-in-v2026-7-1|10 Accessibility and Localization changes in v2026.7.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-07-13-64-interface-experience-changes-in-v2026-7-1|64 Interface Experience changes in v2026.7.1]] · Interface Experience
- [[Changes/OpenClaw/2026-07-13-whatsapp-and-telegram-default-account-routing-warnings-are-now-available-through|WhatsApp and Telegram default-account routing warnings are now available through…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-07-13-132-agent-mode-changes-in-v2026-7-1|132 Agent Mode changes in v2026.7.1]] · Agent Mode
- [[Changes/OpenClaw/2026-07-13-after-one-generated-video-clip-is-ready-a-different-next-clip-can-start-immediat|After one generated video clip is ready, a different next clip can start immediately…]] · Video Generation
- [[Changes/OpenClaw/2026-07-13-79-automation-and-scheduling-changes-in-v2026-7-1|79 Automation and Scheduling changes in v2026.7.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-07-13-130-model-support-changes-in-v2026-7-1|130 Model Support changes in v2026.7.1]] · Model Support
- [[Changes/OpenClaw/2026-07-13-69-account-and-access-changes-in-v2026-7-1|69 Account and Access changes in v2026.7.1]] · Account and Access
- [[Changes/OpenClaw/2026-07-13-59-safety-and-privacy-changes-in-v2026-7-1|59 Safety and Privacy changes in v2026.7.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-07-13-224-mobile-and-desktop-changes-in-v2026-7-1|224 Mobile and Desktop changes in v2026.7.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-07-13-83-voice-and-audio-changes-in-v2026-7-1|83 Voice and Audio changes in v2026.7.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-07-13-18-pricing-model-changes-in-v2026-7-1|18 Pricing Model changes in v2026.7.1]] · Pricing Model
- [[Changes/OpenClaw/2026-07-13-21-editor-experience-changes-in-v2026-7-1|21 Editor Experience changes in v2026.7.1]] · Editor Experience
- [[Changes/OpenClaw/2026-07-13-7-image-generation-changes-in-v2026-7-1|7 Image Generation changes in v2026.7.1]] · Image Generation
- [[Changes/OpenClaw/2026-07-13-channel-setup-warnings-are-now-available-as-structured-doctor-lint-findings-with|Channel setup warnings are now available as structured Doctor lint findings…]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-07-13-4-enterprise-and-administration-changes-in-v2026-7-1|4 Enterprise and Administration changes in v2026.7.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-07-13-2-presentation-creation-changes-in-v2026-7-1|2 Presentation Creation changes in v2026.7.1]] · Presentation Creation
- [[Changes/OpenClaw/2026-07-13-136-memory-and-personalization-changes-in-v2026-7-1|136 Memory and Personalization changes in v2026.7.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-07-13-213-apps-and-integrations-changes-in-v2026-7-1|213 Apps and Integrations changes in v2026.7.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-07-13-20-collaboration-changes-in-v2026-7-1|20 Collaboration changes in v2026.7.1]] · Collaboration
- [[Changes/OpenClaw/2026-07-13-13-files-and-data-changes-in-v2026-7-1|13 Files and Data changes in v2026.7.1]] · Files and Data
- [[Changes/OpenClaw/2026-07-13-19-multimodal-input-changes-in-v2026-7-1|19 Multimodal Input changes in v2026.7.1]] · Multimodal Input
- [[Changes/OpenClaw/2026-07-13-38-reliability-and-performance-changes-in-v2026-7-1|38 Reliability and Performance changes in v2026.7.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-07-13-686-other-changes-in-v2026-7-1|686 other changes in v2026.7.1]] · Other changes
- [[Changes/OpenClaw/2026-07-13-official-openclaw-container-images-are-now-available-from-docker-hub-as-well-as|Official OpenClaw container images are now available from Docker Hub as well…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-07-09 · Codex CLI · [[Changes/Codex CLI/2026-07-09-31525-core-migrate-standalone-web-search-to-extension-owned-turn-items-owenlin0|♯31525 core: migrate standalone web search to extension-owned turn items @owenlin0]]
- Later: 2026-07-13 · OpenCode · [[Changes/OpenCode/2026-07-13-desktop-updated-the-review-panel-with-persistent-file-browsing-better-file-tabs|Desktop Updated the review panel with persistent file browsing, better file tabs…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-e25c69&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-8-search-and-browsing-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-e25c69%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->