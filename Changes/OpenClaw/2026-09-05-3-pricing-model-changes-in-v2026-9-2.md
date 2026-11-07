---
card_id: openclaw-2026-09-05-1e770f
date: '2026-09-05'
description: 'OpenClaw · 2026-09-05 · Pricing Model: 3 changes in v2026.9.2 — Usage
  now keeps selected-day totals within the active session filters, while daily charts
  and…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer
    Invoices]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2978
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e32d78863e7ca9434f676cd00d822c2953875593f13b8f7b291a64e6b323c6a9
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-05-1e770f
  comparison: ''
  date: '2026-09-05'
  description: 'OpenClaw — v2026.9.2: 3 Pricing Model changes'
  evidence:
  - quote: Usage now keeps selected-day totals within the active session filters,
      while daily charts and daily exports retain those matching sessions across the
      requested date range. Provider, model, and tool filters select matching whole
      sessions, so their totals can include other usage within those sessions, and
      the costs remain estimates rather than provider billing records.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: For a new billing failure, the initial wait falls from five hours to ten
      minutes, although upgrading does not shorten an already-active window or detect
      a top-up immediately. Explicitly ordered preferred credentials can also be retried
      on a later real request after their cooldown. Repeated rate-limit failures without
      a provider reset time can progressively delay those attempts up to 24 hours,
      so returning from a paid fallback is subject to successful recovery.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Checking usage and costs no longer loads large saved skill or system prompts
      just to prepare the metrics, avoiding the associated history-processing stalls
      while leaving full context available where it is needed. Turn completion and
      usage displays also skip fallback price lookups when recorded costs already
      suffice, or when only token counts are being shown. The pricing calculation
      and displayed costs are unchanged, and estimated costs remain estimates.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 3-pricing-model-changes-in-v2026-9-2
  source_release: openclaw-2026-09-05-v2026-9-2-377f6d77
  source_type: openclaw_changelog
  theme: pricing-model
  title: 3 Pricing Model changes in v2026.9.2
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-01-usage-and-status-views-now-carry-cumulative-output-token-totals-through-tool-cal|Usage
  and status views now carry cumulative output-token totals through tool calls…]]'
- '[[Changes/Cline/2026-09-02-cost-estimates-no-longer-appear-in-task-history-for-subscription-billed-tasks-cl|Cost
  estimates no longer appear in task history for subscription-billed tasks…]]'
- '[[Changes/Codex CLI/2026-09-03-41944-https-github-com-openai-codex-pull-41944-emit-turn-cost-telemetry-for-chat|♯41944((source
  link) Emit turn cost telemetry…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|openclaw-2026-09-05-v2026-9-2-377f6d77]]'
source_type: openclaw_changelog
theme: pricing-model
title: 3 Pricing Model changes in v2026.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Pricing Model changes in v2026.9.2

**OpenClaw** · 2026-09-05 · [[Themes/pricing-model|Pricing Model]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.2) · from [[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Usage now keeps selected-day totals within the active session filters, while daily charts and daily exports retain those matching sessions across the requested date range. Provider, model, and tool filters select matching whole sessions, so their totals can include other usage within those sessions, and the costs remain estimates rather than provider billing records.

> For a new billing failure, the initial wait falls from five hours to ten minutes, although upgrading does not shorten an already-active window or detect a top-up immediately. Explicitly ordered preferred credentials can also be retried on a later real request after their cooldown. Repeated rate-limit failures without a provider reset time can progressively delay those attempts up to 24 hours, so returning from a paid fallback is subject to successful recovery.

> Checking usage and costs no longer loads large saved skill or system prompts just to prepare the metrics, avoiding the associated history-processing stalls while leaving full context available where it is needed. Turn completion and usage displays also skip fallback price lookups when recorded costs already suffice, or when only token counts are being shown. The pricing calculation and displayed costs are unchanged, and estimated costs remain estimates.

Source: https://docs.openclaw.ai/releases/2026.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-05-24-safety-and-privacy-changes-in-v2026-9-2|24 Safety and Privacy changes in v2026.9.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-05-8-editor-experience-changes-in-v2026-9-2|8 Editor Experience changes in v2026.9.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-05-progress-mode-can-stay-quiet-about-routine-tool-calls-while-keeping-the-updates|Progress mode can stay quiet about routine tool calls while keeping the updates…]] · Presentation Creation
- [[Changes/OpenClaw/2026-09-05-swarm-is-now-available-to-eligible-agents-without-a-separate-enablement-step-so|Swarm is now available to eligible agents without a separate enablement step…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-a-rejected-send-can-keep-its-original-attachments-and-retry-action-when-you-leav|A rejected send can keep its original attachments and Retry action when you leave…]] · Files and Data
- [[Changes/OpenClaw/2026-09-05-20-account-and-access-changes-in-v2026-9-2|20 Account and Access changes in v2026.9.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-05-17-model-support-changes-in-v2026-9-2|17 Model Support changes in v2026.9.2]] · Model Support
- [[Changes/OpenClaw/2026-09-05-16-developer-workflow-changes-in-v2026-9-2|16 Developer Workflow changes in v2026.9.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2|21 Memory and Personalization changes in v2026.9.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-05-4-enterprise-and-administration-changes-in-v2026-9-2|4 Enterprise and Administration changes in v2026.9.2]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-05-if-background-image-video-or-music-generation-finishes-but-final-delivery-fails|If background image, video or music generation finishes but final delivery fails…]] · Music Generation
- [[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode changes in v2026.9.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2|35 Apps and Integrations changes in v2026.9.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2|8 Automation and Scheduling changes in v2026.9.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-05-9-collaboration-changes-in-v2026-9-2|9 Collaboration changes in v2026.9.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-05-10-mobile-and-desktop-changes-in-v2026-9-2|10 Mobile and Desktop changes in v2026.9.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-05-15-context-window-changes-in-v2026-9-2|15 Context Window changes in v2026.9.2]] · Context Window
- [[Changes/OpenClaw/2026-09-05-4-search-and-browsing-changes-in-v2026-9-2|4 Search and Browsing changes in v2026.9.2]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-05-17-voice-and-audio-changes-in-v2026-9-2|17 Voice and Audio changes in v2026.9.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-05-21-interface-experience-changes-in-v2026-9-2|21 Interface Experience changes in v2026.9.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-05-3-reliability-and-performance-changes-in-v2026-9-2|3 Reliability and Performance changes in v2026.9.2]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-05-you-can-now-put-the-part-of-a-task-you-are-working-on-in-the-main-view-and-keep|Put the part of a task you are working on in the main view and keep the conversation…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-72-other-changes-in-v2026-9-2|72 other changes in v2026.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-09-03 · Codex CLI · [[Changes/Codex CLI/2026-09-03-41944-https-github-com-openai-codex-pull-41944-emit-turn-cost-telemetry-for-chat|♯41944((source link) Emit turn cost telemetry…]]
- Later: 2026-09-07 · Lovable · [[Changes/Lovable/2026-09-07-transfer-primary-ownership-of-your-workspace|Transfer primary ownership of your workspace]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-11 · Descript · [[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer Invoices]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-05-1e770f&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-05-3-pricing-model-changes-in-v2026-9-2.md%0ACard%20ID%3A%20openclaw-2026-09-05-1e770f%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->