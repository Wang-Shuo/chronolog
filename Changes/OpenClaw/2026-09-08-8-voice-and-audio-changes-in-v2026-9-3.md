---
card_id: openclaw-2026-09-08-614730
date: '2026-09-08'
description: 'OpenClaw · 2026-09-08 · Voice and Audio: 8 changes in v2026.9.3 — Discord
  recordings stay independent of voice-conversation work. For full room transcription…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1156
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 60f301bd06f0f84c9119b6de062a9cf609aa7d8a7dea569af6086a187e177288
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-08-614730
  comparison: ''
  date: '2026-09-08'
  description: 'OpenClaw — v2026.9.3: 8 Voice and Audio changes'
  evidence:
  - quote: Discord recordings stay independent of voice-conversation work. For full
      room transcription coverage, use batch transcription; realtime-only capture
      remains limited. Occupancy capture only reopens recent transcripts whose stored
      origin confirms a generated ID, preserving supplied-ID and unknown legacy history.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Voice recordings remain available until transcription finishes. Supported
      English voice requests that mention farewells can take the request path while
      recognized closing phrases stay quiet.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Video attachments with non-square pixels display at their intended proportions,
      while one-off speech follows the destination channel’s final voice-versus-audio
      choice.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Android makes better use of folding screens and small windows, while Apple
      apps improve conversation history, connection controls, and the path into a
      live voice conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: On iOS, saved app-local Talk provider, voice and language overrides are
      retired in favor of the Gateway’s Talk configuration. The old default share
      instruction is also retired; instructions supplied with an individual share
      remain available.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Discord, llama.cpp, and Voice Call preserve their declared 2026.9.2 host
      support through scoped optional-helper and local transport fallbacks. Those
      accommodations do not restore intentionally retired SDK exports.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Affected Gateway, worker, voice-call, and ClickClack connections use their
      declared transport implementations under Bun, preserving the options and payload
      behavior those integrations expect. The fixes are scoped to those paths and
      do not establish complete Bun compatibility across OpenClaw.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Realtime transcription retains its payload limits on the affected Bun transport
      path.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 8-voice-and-audio-changes-in-v2026-9-3
  source_release: openclaw-2026-09-08-v2026-9-3-dfcfef48
  source_type: openclaw_changelog
  theme: voice
  title: 8 Voice and Audio changes in v2026.9.3
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-03-12-voice-and-audio-changes-in-v2026-9-1|12 Voice
  and Audio changes in v2026.9.1]]'
- '[[Changes/OpenClaw/2026-09-05-17-voice-and-audio-changes-in-v2026-9-2|17 Voice
  and Audio changes in v2026.9.2]]'
- '[[Changes/ElevenLabs/2026-09-07-workspaces|Workspaces]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|openclaw-2026-09-08-v2026-9-3-dfcfef48]]'
source_type: openclaw_changelog
theme: voice
title: 8 Voice and Audio changes in v2026.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Voice and Audio changes in v2026.9.3

**OpenClaw** · 2026-09-08 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.3) · from [[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Discord recordings stay independent of voice-conversation work. For full room transcription coverage, use batch transcription; realtime-only capture remains limited. Occupancy capture only reopens recent transcripts whose stored origin confirms a generated ID, preserving supplied-ID and unknown legacy history.

> Voice recordings remain available until transcription finishes. Supported English voice requests that mention farewells can take the request path while recognized closing phrases stay quiet.

> Video attachments with non-square pixels display at their intended proportions, while one-off speech follows the destination channel’s final voice-versus-audio choice.

> Android makes better use of folding screens and small windows, while Apple apps improve conversation history, connection controls, and the path into a live voice conversation.

> On iOS, saved app-local Talk provider, voice and language overrides are retired in favor of the Gateway’s Talk configuration. The old default share instruction is also retired; instructions supplied with an individual share remain available.

> Discord, llama.cpp, and Voice Call preserve their declared 2026.9.2 host support through scoped optional-helper and local transport fallbacks. Those accommodations do not restore intentionally retired SDK exports.

> Affected Gateway, worker, voice-call, and ClickClack connections use their declared transport implementations under Bun, preserving the options and payload behavior those integrations expect. The fixes are scoped to those paths and do not establish complete Bun compatibility across OpenClaw.

> Realtime transcription retains its payload limits on the affected Bun transport path.

Source: https://docs.openclaw.ai/releases/2026.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-08-7-automation-and-scheduling-changes-in-v2026-9-3|7 Automation and Scheduling changes in v2026.9.3]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-08-10-memory-and-personalization-changes-in-v2026-9-3|10 Memory and Personalization changes in v2026.9.3]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-08-2-files-and-data-changes-in-v2026-9-3|2 Files and Data changes in v2026.9.3]] · Files and Data
- [[Changes/OpenClaw/2026-09-08-12-context-window-changes-in-v2026-9-3|12 Context Window changes in v2026.9.3]] · Context Window
- [[Changes/OpenClaw/2026-09-08-23-apps-and-integrations-changes-in-v2026-9-3|23 Apps and Integrations changes in v2026.9.3]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-08-ordinary-model-changes-now-apply-to-the-current-chat-by-default-including-admini|Ordinary model changes now apply to the current chat by default, including…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-08-10-mobile-and-desktop-changes-in-v2026-9-3|10 Mobile and Desktop changes in v2026.9.3]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-08-4-reliability-and-performance-changes-in-v2026-9-3|4 Reliability and Performance changes in v2026.9.3]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-08-provider-adapters-preserve-initial-anthropic-text-and-thinking-keep-images-with|Provider adapters preserve initial Anthropic text and thinking, keep images…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-08-8-editor-experience-changes-in-v2026-9-3|8 Editor Experience changes in v2026.9.3]] · Editor Experience
- [[Changes/OpenClaw/2026-09-08-15-model-support-changes-in-v2026-9-3|15 Model Support changes in v2026.9.3]] · Model Support
- [[Changes/OpenClaw/2026-09-08-3-search-and-browsing-changes-in-v2026-9-3|3 Search and Browsing changes in v2026.9.3]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-08-16-agent-mode-changes-in-v2026-9-3|16 Agent Mode changes in v2026.9.3]] · Agent Mode
- [[Changes/OpenClaw/2026-09-08-11-interface-experience-changes-in-v2026-9-3|11 Interface Experience changes in v2026.9.3]] · Interface Experience
- [[Changes/OpenClaw/2026-09-08-slack-delivers-valid-structured-sections-intact-even-when-their-accessibility-te|Slack delivers valid structured sections intact even when their accessibility text…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-08-4-collaboration-changes-in-v2026-9-3|4 Collaboration changes in v2026.9.3]] · Collaboration
- [[Changes/OpenClaw/2026-09-08-14-safety-and-privacy-changes-in-v2026-9-3|14 Safety and Privacy changes in v2026.9.3]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-08-4-pricing-model-changes-in-v2026-9-3|4 Pricing Model changes in v2026.9.3]] · Pricing Model
- [[Changes/OpenClaw/2026-09-08-8-account-and-access-changes-in-v2026-9-3|8 Account and Access changes in v2026.9.3]] · Account and Access
- [[Changes/OpenClaw/2026-09-08-22-developer-workflow-changes-in-v2026-9-3|22 Developer Workflow changes in v2026.9.3]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-08-77-other-changes-in-v2026-9-3|77 other changes in v2026.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-09-07 · ElevenLabs · [[Changes/ElevenLabs/2026-09-07-workspaces|Workspaces]]
- Later: 2026-09-09 · Codex CLI · [[Changes/Codex CLI/2026-09-09-20-voice-and-audio-changes-in-rust-v0-154-0|20 Voice and Audio changes in rust-v0.154.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-08-614730&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-08-8-voice-and-audio-changes-in-v2026-9-3.md%0ACard%20ID%3A%20openclaw-2026-09-08-614730%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->