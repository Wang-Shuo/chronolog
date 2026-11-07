---
card_id: openclaw-2026-06-30-a53c24
date: '2026-06-30'
description: 'OpenClaw · 2026-06-30 · Pricing Model: When a Codex subscription reaches
  its usage limit, OpenClaw now moves to configured fallback models instead of stopping…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer
    Invoices]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2911
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: policy
machine_hash: 063566147377831e052970ce0b71aa420431bf6e71bc13d5925d0134eb69ce59
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-06-30-a53c24
  comparison: ''
  date: '2026-06-30'
  description: 'OpenClaw — v2026.6.11: When a Codex subscription reaches its usage
    limit, OpenClaw now moves to configured fallback models instead of stopping on
    the failed result, and it does not retry runs that already produced visible output.
    #95400 Thanks @jason-allen-oneal, @sallyom.'
  evidence:
  - quote: 'When a Codex subscription reaches its usage limit, OpenClaw now moves
      to configured fallback models instead of stopping on the failed result, and
      it does not retry runs that already produced visible output. #95400 Thanks @jason-allen-oneal,
      @sallyom.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  extractor_version: fallback-v5
  impact: incremental
  kind: policy
  product: openclaw
  product_name: OpenClaw
  slug: when-a-codex-subscription-reaches-its-usage-limit-openclaw-now-moves-to-configur
  source_release: openclaw-2026-06-30-v2026-6-11-23cb95a9
  source_type: openclaw_changelog
  theme: pricing-model
  theme_matches:
  - matched_terms:
    - models
    score: 50
    theme: model-support
  - matched_terms:
    - subscription
    score: 50
    theme: pricing-model
  theme_resolution: manual-semantic-rule-v1
  title: When a Codex subscription reaches its usage limit, OpenClaw now moves to
    configured…
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-06-29-2-pricing-model-changes-in-v0-10-0|2 Pricing Model
  changes in v0.10.0]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-configure-subagent-concurrency-and-depth-limits-in-settings-usage-based-billing|Configure
  subagent concurrency and depth limits in /settings (usage-based billing users)]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-require-session-limits-to-be-at-least-30-ai-credits|Require
  session limits to be at least 30 AI credits]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|openclaw-2026-06-30-v2026-6-11-23cb95a9]]'
source_type: openclaw_changelog
theme: pricing-model
title: When a Codex subscription reaches its usage limit, OpenClaw now moves to configured…
type: change
---

<!-- chronolog:begin region="header" -->
# When a Codex subscription reaches its usage limit, OpenClaw now moves to configured…

**OpenClaw** · 2026-06-30 · [[Themes/pricing-model|Pricing Model]] · Policy · [Official source](https://docs.openclaw.ai/releases/2026.6.11) · from [[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|v2026.6.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> When a Codex subscription reaches its usage limit, OpenClaw now moves to configured fallback models instead of stopping on the failed result, and it does not retry runs that already produced visible output. #95400 Thanks @jason-allen-oneal, @sallyom.
>
> Source: https://docs.openclaw.ai/releases/2026.6.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-06-30-7-editor-experience-changes-in-v2026-6-11|7 Editor Experience changes in v2026.6.11]] · Editor Experience
- [[Changes/OpenClaw/2026-06-30-canvas-a2ui-now-serves-only-the-current-app-assets-after-each-build-so-outdated|Canvas A2UI now serves only the current app assets after each build, so outdated…]] · Files and Data
- [[Changes/OpenClaw/2026-06-30-word-powerpoint-and-excel-document-reads-and-writes-now-use-the-intended-docx-pp|Word, PowerPoint, and Excel document reads and writes now use the intended .docx…]] · Presentation Creation
- [[Changes/OpenClaw/2026-06-30-20-context-window-changes-in-v2026-6-11|20 Context Window changes in v2026.6.11]] · Context Window
- [[Changes/OpenClaw/2026-06-30-32-agent-mode-changes-in-v2026-6-11|32 Agent Mode changes in v2026.6.11]] · Agent Mode
- [[Changes/OpenClaw/2026-06-30-15-mobile-and-desktop-changes-in-v2026-6-11|15 Mobile and Desktop changes in v2026.6.11]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-06-30-5-collaboration-changes-in-v2026-6-11|5 Collaboration changes in v2026.6.11]] · Collaboration
- [[Changes/OpenClaw/2026-06-30-26-memory-and-personalization-changes-in-v2026-6-11|26 Memory and Personalization changes in v2026.6.11]] · Memory and Personalization
- [[Changes/OpenClaw/2026-06-30-34-apps-and-integrations-changes-in-v2026-6-11|34 Apps and Integrations changes in v2026.6.11]] · Apps and Integrations
- [[Changes/OpenClaw/2026-06-30-6-voice-and-audio-changes-in-v2026-6-11|6 Voice and Audio changes in v2026.6.11]] · Voice and Audio
- [[Changes/OpenClaw/2026-06-30-32-model-support-changes-in-v2026-6-11|32 Model Support changes in v2026.6.11]] · Model Support
- [[Changes/OpenClaw/2026-06-30-qqbot-group-admins-can-choose-how-broadly-slash-commands-are-available-and-priva|QQBot group admins can choose how broadly slash commands are available…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-06-30-4-reliability-and-performance-changes-in-v2026-6-11|4 Reliability and Performance changes in v2026.6.11]] · Reliability and Performance
- [[Changes/OpenClaw/2026-06-30-3-interface-experience-changes-in-v2026-6-11|3 Interface Experience changes in v2026.6.11]] · Interface Experience
- [[Changes/OpenClaw/2026-06-30-15-automation-and-scheduling-changes-in-v2026-6-11|15 Automation and Scheduling changes in v2026.6.11]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-06-30-9-developer-workflow-changes-in-v2026-6-11|9 Developer Workflow changes in v2026.6.11]] · Developer Workflow
- [[Changes/OpenClaw/2026-06-30-6-safety-and-privacy-changes-in-v2026-6-11|6 Safety and Privacy changes in v2026.6.11]] · Safety and Privacy
- [[Changes/OpenClaw/2026-06-30-more-official-channel-provider-and-web-search-plugins-can-now-be-installed-or-re|More official channel, provider, and web-search plugins can now be installed…]] · Search and Browsing
- [[Changes/OpenClaw/2026-06-30-generated-images-from-a-remote-codex-app-server-now-arrive-as-attachments-instea|Generated images from a remote Codex app-server now arrive as attachments instead…]] · Image Generation
- [[Changes/OpenClaw/2026-06-30-background-image-video-and-music-results-now-return-to-the-chat-that-requested-t|Background image, video, and music results now return to the chat that requested…]] · Music Generation
- [[Changes/OpenClaw/2026-06-30-2-account-and-access-changes-in-v2026-6-11|2 Account and Access changes in v2026.6.11]] · Account and Access
- [[Changes/OpenClaw/2026-06-30-96-other-changes-in-v2026-6-11|96 other changes in v2026.6.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-require-session-limits-to-be-at-least-30-ai-credits|Require session limits to be at least 30 AI credits]]
- Later: 2026-06-30 · OpenCode · [[Changes/OpenCode/2026-06-30-sdk-add-a-live-event-subscription-stream|SDK Add a live event subscription stream]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-11 · Descript · [[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer Invoices]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-06-30-a53c24&body=Card%3A%20Changes%2FOpenClaw%2F2026-06-30-when-a-codex-subscription-reaches-its-usage-limit-openclaw-now-moves-to-configur.md%0ACard%20ID%3A%20openclaw-2026-06-30-a53c24%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.6.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->