---
card_id: openclaw-2026-07-13-f95707
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Files and Data: 13 changes in v2026.7.1 — Assistant
  documents downloaded from the Control UI now keep recognizable original filenames…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode
    offset]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2490
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e7193ece329594f0bc96fb74b40bb5ee4a3b65903e2b3b67dccfba9ee529215c
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-f95707
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 13 Files and Data changes'
  evidence:
  - quote: 'Assistant documents downloaded from the Control UI now keep recognizable
      original filenames instead of exposing UUID-suffixed staging names. #100743'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Assistant-sent documents in WebChat now download with their original server-provided
      filename, including Unicode names, instead of opening as an unnamed browser
      document. #100728 Thanks @lptrichor.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'When an interactive command button falls back to text, users now receive
      the command they can copy, with Feishu document comments explaining the manual
      step. #94385 Related #69754 . Thanks @1yihui, @xialonglee.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram documents received through a containerized local Bot API now
      arrive with their actual contents when its mounted data path differs between
      containers. #91984 Thanks @ailucasdz, @dizesales.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram documents sent near a Gateway restart now retry after recovery
      instead of disappearing silently, while permanent failures still request a resend.
      #98102 Related #98076 . Thanks @davearcher18, @luoyanglang, @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Google Meet document processing now rejects oversized Google Drive exports
      before they can destabilize OpenClaw, while ordinary documents still export
      as text. #97620 Thanks @alix-007, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'MiniMax VLM and native PDF provider errors now remain readable when emoji
      or other supplementary characters land at the diagnostic snippet limit. #101728
      Thanks @wings1029.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Canvas content can no longer navigate to device-local web services,
      while normal remote and Gateway-hosted pages continue to work. #99874 Thanks
      @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Multi-page scanned PDFs now keep later pages at a usable image size during
      fallback extraction, allowing vision models to read the full document. #96390
      Thanks @cls3389, @vincentkoc, @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Requesting nonexistent PDF pages now returns a clear range error instead
      of accidentally sending the entire document to a native provider. #97698 Thanks
      @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Fractional PDF page selections such as 1.5 now fail immediately with a
      clear validation error instead of silently omitting requested content. #99399
      Thanks @qingminglong.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Canvas embed replies now retain their visible message text when a self-closing
      embed shortcode is followed by an extra closing marker. #96449 Thanks @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Kept Canvas implementation details private so its supported developer
      surface remains clear. #101915 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 13-files-and-data-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: file-data
  title: 13 Files and Data changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/Raycast/2026-07-03-file-search-you-can-now-search-contents-of-text-documents-from-within-file-searc-8dbcea|File
  Search : You can now search contents of text documents from within File Search…]]'
- '[[Changes/OpenHands/2026-07-06-docs-bring-readme-md-over-from-agent-canvas-by-rbren-in-https-github-com-openhan|docs:
  Bring README.md over from Agent Canvas]]'
- '[[Changes/Codex CLI/2026-07-08-27714-app-server-document-thread-and-turn-ids-are-uuid7-owenlin0|♯27714
  app-server: document thread and turn IDs are UUID7 @owenlin0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: file-data
title: 13 Files and Data changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Files and Data changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Assistant documents downloaded from the Control UI now keep recognizable original filenames instead of exposing UUID-suffixed staging names. #100743

> Assistant-sent documents in WebChat now download with their original server-provided filename, including Unicode names, instead of opening as an unnamed browser document. #100728 Thanks @lptrichor.

> When an interactive command button falls back to text, users now receive the command they can copy, with Feishu document comments explaining the manual step. #94385 Related #69754 . Thanks @1yihui, @xialonglee.

> Telegram documents received through a containerized local Bot API now arrive with their actual contents when its mounted data path differs between containers. #91984 Thanks @ailucasdz, @dizesales.

> Telegram documents sent near a Gateway restart now retry after recovery instead of disappearing silently, while permanent failures still request a resend. #98102 Related #98076 . Thanks @davearcher18, @luoyanglang, @obviyus.

> Google Meet document processing now rejects oversized Google Drive exports before they can destabilize OpenClaw, while ordinary documents still export as text. #97620 Thanks @alix-007, @vincentkoc.

> MiniMax VLM and native PDF provider errors now remain readable when emoji or other supplementary characters land at the diagnostic snippet limit. #101728 Thanks @wings1029.

> Android Canvas content can no longer navigate to device-local web services, while normal remote and Gateway-hosted pages continue to work. #99874 Thanks @ly85206559.

> Multi-page scanned PDFs now keep later pages at a usable image size during fallback extraction, allowing vision models to read the full document. #96390 Thanks @cls3389, @vincentkoc, @zengwen-dt.

> Requesting nonexistent PDF pages now returns a clear range error instead of accidentally sending the entire document to a native provider. #97698 Thanks @zhangguiping-xydt.

> Fractional PDF page selections such as 1.5 now fail immediately with a clear validation error instead of silently omitting requested content. #99399 Thanks @qingminglong.

> Canvas embed replies now retain their visible message text when a self-closing embed shortcode is followed by an extra closing marker. #96449 Thanks @ly-wang19.

> Kept Canvas implementation details private so its supported developer surface remains clear. #101915 Thanks @vincentkoc.

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
- [[Changes/OpenClaw/2026-07-13-8-search-and-browsing-changes-in-v2026-7-1|8 Search and Browsing changes in v2026.7.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-07-13-20-collaboration-changes-in-v2026-7-1|20 Collaboration changes in v2026.7.1]] · Collaboration
- [[Changes/OpenClaw/2026-07-13-19-multimodal-input-changes-in-v2026-7-1|19 Multimodal Input changes in v2026.7.1]] · Multimodal Input
- [[Changes/OpenClaw/2026-07-13-38-reliability-and-performance-changes-in-v2026-7-1|38 Reliability and Performance changes in v2026.7.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-07-13-686-other-changes-in-v2026-7-1|686 other changes in v2026.7.1]] · Other changes
- [[Changes/OpenClaw/2026-07-13-official-openclaw-container-images-are-now-available-from-docker-hub-as-well-as|Official OpenClaw container images are now available from Docker Hub as well…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-07-08 · Codex CLI · [[Changes/Codex CLI/2026-07-08-27714-app-server-document-thread-and-turn-ids-are-uuid7-owenlin0|♯27714 app-server: document thread and turn IDs are UUID7 @owenlin0]]
- Later: 2026-07-13 · Superwhisper · [[Changes/Superwhisper/2026-07-13-new-installations-now-use-superwhisper-instead-of-documents-superwhisper-as-thei|New installations now use ~/superwhisper instead of ~/Documents/superwhisper…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode offset]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-f95707&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-13-files-and-data-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-f95707%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->