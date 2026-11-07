---
card_id: openclaw-2026-07-13-3bf497
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Accessibility and Localization: 10 changes in
  v2026.7.1 — The Control UI now puts search, sidebar access, theme choice, and macOS…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-09-11-chatgpt-now-supports-a-limited-selection-of-languages-in-the-interface|ChatGPT
    now supports a limited selection of languages in the interface]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1036
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: accessibility-localization
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 85ea549e51ac191e0d750475c4b684e8968c7256371ba7dc857529db2110817f
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-3bf497
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 10 Accessibility and Localization changes'
  evidence:
  - quote: 'The Control UI now puts search, sidebar access, theme choice, and macOS
      branding in clearer, more predictable locations with accurate screen-reader
      labels. #101497'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Temporary Gateway disconnects now use a calmer, dashboard-native reconnect
      pill with the same Retry and accessibility behavior. #101844'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Localized macOS builds now translate the new GitHub link label, including
      its accessibility-facing text, instead of falling back to English. 8be1d36
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenClaw now uses consistent branded typography throughout its iOS, Watch,
      and Live Activity interfaces while retaining Dynamic Type and accessibility
      support. #99246 Thanks @joelnishanth, @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'On iOS 26, affected Settings switches now respond when users tap anywhere
      on the labeled row, with accessibility labels and values preserved. #99888 Thanks
      @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Windows now detects active Gateway listeners reliably from localized netstat
      output, improving port diagnostics and gateway --force cleanup without confusing
      established connections for listeners. #100012 Thanks @qingminglong, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made Control UI localization checks run reliably on Windows without changing
      translated content. #95534 Thanks @ooiuuii.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored clean localization, documentation, and lint validation for the
      Crestodian onboarding flow. #100223'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Refreshed native localization tracking after source movement to prevent
      false validation failures. #101232'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Corrected native localization references so app-related validation remains
      accurate. #101233 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 10-accessibility-and-localization-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: accessibility-localization
  title: 10 Accessibility and Localization changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-06-25-improved-accessibility-and-usability-of-the-artifact-review-dialog-including-con|Improved
  accessibility and usability of the artifact review dialog, including…]]'
- '[[Changes/Open WebUI/2026-06-29-better-screen-reader-labels-on-toggles-integration-and-switch-toggles-now-expose|♿
  Better screen-reader labels on toggles. Integration and switch toggles now…]]'
- '[[Changes/Claude Code/2026-07-03-improved-screen-reader-output-decorative-glyphs-are-now-hidden-transcript-symbol|Improved
  screen-reader output]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: accessibility-localization
title: 10 Accessibility and Localization changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Accessibility and Localization changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/accessibility-localization|Accessibility and Localization]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The Control UI now puts search, sidebar access, theme choice, and macOS branding in clearer, more predictable locations with accurate screen-reader labels. #101497

> Temporary Gateway disconnects now use a calmer, dashboard-native reconnect pill with the same Retry and accessibility behavior. #101844

> Localized macOS builds now translate the new GitHub link label, including its accessibility-facing text, instead of falling back to English. 8be1d36

> OpenClaw now uses consistent branded typography throughout its iOS, Watch, and Live Activity interfaces while retaining Dynamic Type and accessibility support. #99246 Thanks @joelnishanth, @joshavant.

> On iOS 26, affected Settings switches now respond when users tap anywhere on the labeled row, with accessibility labels and values preserved. #99888 Thanks @ly85206559.

> Windows now detects active Gateway listeners reliably from localized netstat output, improving port diagnostics and gateway --force cleanup without confusing established connections for listeners. #100012 Thanks @qingminglong, @vincentkoc.

> Made Control UI localization checks run reliably on Windows without changing translated content. #95534 Thanks @ooiuuii.

> Restored clean localization, documentation, and lint validation for the Crestodian onboarding flow. #100223

> Refreshed native localization tracking after source movement to prevent false validation failures. #101232

> Corrected native localization references so app-related validation remains accurate. #101233 Thanks @vincentkoc.

Source: https://docs.openclaw.ai/releases/2026.7.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-07-13-5-projects-and-workspaces-changes-in-v2026-7-1|5 Projects and Workspaces changes in v2026.7.1]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-07-13-99-developer-workflow-changes-in-v2026-7-1|99 Developer Workflow changes in v2026.7.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-07-13-69-context-window-changes-in-v2026-7-1|69 Context Window changes in v2026.7.1]] · Context Window
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
- [[Changes/OpenClaw/2026-07-13-8-search-and-browsing-changes-in-v2026-7-1|8 Search and Browsing changes in v2026.7.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-07-13-20-collaboration-changes-in-v2026-7-1|20 Collaboration changes in v2026.7.1]] · Collaboration
- [[Changes/OpenClaw/2026-07-13-13-files-and-data-changes-in-v2026-7-1|13 Files and Data changes in v2026.7.1]] · Files and Data
- [[Changes/OpenClaw/2026-07-13-19-multimodal-input-changes-in-v2026-7-1|19 Multimodal Input changes in v2026.7.1]] · Multimodal Input
- [[Changes/OpenClaw/2026-07-13-38-reliability-and-performance-changes-in-v2026-7-1|38 Reliability and Performance changes in v2026.7.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-07-13-686-other-changes-in-v2026-7-1|686 other changes in v2026.7.1]] · Other changes
- [[Changes/OpenClaw/2026-07-13-official-openclaw-container-images-are-now-available-from-docker-hub-as-well-as|Official OpenClaw container images are now available from Docker Hub as well…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Accessibility and Localization

- Earlier: 2026-07-03 · Claude Code · [[Changes/Claude Code/2026-07-03-improved-screen-reader-output-decorative-glyphs-are-now-hidden-transcript-symbol|Improved screen-reader output]]
- Later: 2026-07-14 · Claude Code · [[Changes/Claude Code/2026-07-14-added-screen-reader-mode-opt-in-plain-text-rendering-for-screen-reader-users-run|Added screen reader mode: opt-in plain-text rendering for screen reader users]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-09-11 · ChatGPT · [[Changes/ChatGPT/2023-09-11-chatgpt-now-supports-a-limited-selection-of-languages-in-the-interface|ChatGPT now supports a limited selection of languages in the interface]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-3bf497&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-10-accessibility-and-localization-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-3bf497%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->