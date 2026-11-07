---
card_id: openclaw-2026-09-08-56b109
date: '2026-09-08'
description: 'OpenClaw · 2026-09-08 · Multimodal Input: Provider adapters preserve
  initial Anthropic text and thinking, keep images with the tool results they came
  from, and…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-16-descript-now-supports-video|Video
    Playback]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2853
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: multimodal
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: e49ff78ab463b4d554c39bee675bfad1fc965ac374e2ec71e0b327aeadf183e3
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-08-56b109
  comparison: ''
  date: '2026-09-08'
  description: 'OpenClaw — v2026.9.3: Provider adapters preserve initial Anthropic
    text and thinking, keep images with the tool results they came from, and retain
    tool-schema constraints. Generated-video downloads reject malformed responses,
    while image setup stops after cancellation or timeout. If an OpenCode Go or compatible
    completion stream ends after its tools have finished, OpenClaw can recover a final
    summary without replaying those tools. Several streaming paths also reduce repeated
    local parsing or copying without changing the provider’s generation speed.'
  evidence:
  - quote: Provider adapters preserve initial Anthropic text and thinking, keep images
      with the tool results they came from, and retain tool-schema constraints. Generated-video
      downloads reject malformed responses, while image setup stops after cancellation
      or timeout. If an OpenCode Go or compatible completion stream ends after its
      tools have finished, OpenClaw can recover a final summary without replaying
      those tools. Several streaming paths also reduce repeated local parsing or copying
      without changing the provider’s generation speed.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: openclaw
  product_name: OpenClaw
  slug: provider-adapters-preserve-initial-anthropic-text-and-thinking-keep-images-with
  source_release: openclaw-2026-09-08-v2026-9-3-dfcfef48
  source_type: openclaw_changelog
  theme: multimodal
  theme_matches:
  - matched_terms:
    - generated video
    score: 60
    theme: video-generation
  - matched_terms:
    - completion
    score: 50
    theme: editor-experience
  - matched_terms:
    - speed
    score: 50
    theme: reliability-performance
  theme_resolution: manual-semantic-rule-v1
  title: Provider adapters preserve initial Anthropic text and thinking, keep images…
  type: change
related_changes:
- '[[Changes/HeyGen/2026-09-04-brand-system-styling-moves-from-templates-to-ai-studio|Brand
  System styling moves from Templates to AI Studio]]'
- '[[Changes/HeyGen/2026-09-04-in-ai-studio|In AI Studio]]'
- '[[Changes/Krea/2026-09-07-realtime-director|Realtime Director]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|openclaw-2026-09-08-v2026-9-3-dfcfef48]]'
source_type: openclaw_changelog
theme: multimodal
title: Provider adapters preserve initial Anthropic text and thinking, keep images…
type: change
---

<!-- chronolog:begin region="header" -->
# Provider adapters preserve initial Anthropic text and thinking, keep images…

**OpenClaw** · 2026-09-08 · [[Themes/multimodal|Multimodal Input]] · [Official source](https://docs.openclaw.ai/releases/2026.9.3) · from [[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Provider adapters preserve initial Anthropic text and thinking, keep images with the tool results they came from, and retain tool-schema constraints. Generated-video downloads reject malformed responses, while image setup stops after cancellation or timeout. If an OpenCode Go or compatible completion stream ends after its tools have finished, OpenClaw can recover a final summary without replaying those tools. Several streaming paths also reduce repeated local parsing or copying without changing the provider’s generation speed.
>
> Source: https://docs.openclaw.ai/releases/2026.9.3
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
- [[Changes/OpenClaw/2026-09-08-8-editor-experience-changes-in-v2026-9-3|8 Editor Experience changes in v2026.9.3]] · Editor Experience
- [[Changes/OpenClaw/2026-09-08-8-voice-and-audio-changes-in-v2026-9-3|8 Voice and Audio changes in v2026.9.3]] · Voice and Audio
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
## Nearby in Multimodal Input

- Earlier: 2026-09-07 · Krea · [[Changes/Krea/2026-09-07-realtime-director|Realtime Director]]
- Later: 2026-09-10 · DeepSeek API · [[Changes/DeepSeek API/2026-09-10-deepseek-v4-1-flash-release|DeepSeek-V4.1-Flash Release]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-16 · Descript · [[Changes/Descript/2018-11-16-descript-now-supports-video|Video Playback]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-08-56b109&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-08-provider-adapters-preserve-initial-anthropic-text-and-thinking-keep-images-with.md%0ACard%20ID%3A%20openclaw-2026-09-08-56b109%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->