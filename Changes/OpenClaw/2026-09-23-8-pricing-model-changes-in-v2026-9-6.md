---
card_id: openclaw-2026-09-23-884524
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Pricing Model: 8 changes in v2026.9.6 — GPT-6
  Sol and Luna give you two new choices for text, images, and tool use through the
  OpenAI…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer
    Invoices]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2996
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 340a92e5513f6685ba75fded35a80a291a9ae484811d44d1f7b557aadb76eb8a
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-884524
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 8 Pricing Model changes'
  evidence:
  - quote: GPT-6 Sol and Luna give you two new choices for text, images, and tool
      use through the OpenAI Responses API or ChatGPT sign-in. For embedded ChatGPT
      use, explicitly choose the OpenClaw runtime ; setting the model alone does not
      select it. Existing selections and the Astra setup default stay unchanged. Luna
      has lower standard API rates in the shipped catalog, at $0.10 input and $0.50
      output per million tokens compared with Sol's $2 input and $10 output. Different
      pricing tiers apply above 272,000 input tokens.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Bundled Codex 0.155.1 also lets eligible ChatGPT accounts discover and
      use both models through native Codex. After starting or upgrading OpenClaw,
      /codex models shows your account's choices . Embedded reasoning supports none
      through max, with medium as the default when supported; native effort choices
      depend on the account. The separate Luna Reserve route and its billing distinction
      remain unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Budget errors no longer trigger futile retries merely because a billing-help
      URL contains limit-related wording. Upstream server failures also report as
      server errors instead of misleading timeouts, while genuine rate limits, timing
      failures, and overload retain their existing handling.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Unknown model costs are now left unavailable instead of appearing as free
      usage, while explicitly free rates and provider-billed zero totals remain zero.
      Recorded charges retain their request-time pricing. Plugin consumers should
      handle the optional usage.costUsd field being absent.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Codex usage views now label Luna Reserve as a separate route. Unused Reserve
      quota does not cover ordinary Luna requests, including with Fast off, and ordinary
      Luna may still consume credits. This clarifies the display without enabling
      Reserve routing; account counters are not per-request billing receipts.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Portable cloud workers now include the browser assets needed for provisioning
      and the SQLite executable needed for authorized shell commands, at the cost
      of a larger runtime download. After a Gateway restart, unstarted submissions
      can wait up to two minutes for retained workers to reconnect, capped by the
      turn timeout, with one retry and Stop still available. Work already handed off
      is not resent, and incompatible worker runtimes still need an update.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Brave, Exa, paid Parallel, and Perplexity Search honor the requested number
      of structured results, including cached replies, and Brave’s LLM-context cache
      keeps different requested counts separate. Local trimming does not reduce upstream
      billing. Canceled or timed-out xAI searches stop waiting for credentials without
      later sending the search, while already-owned credential refresh and cleanup
      may finish independently. Search results also omit impossible calendar dates
      without dropping or reordering the results.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: This release includes 1175 maintainer and internal changes covering tests,
      development tools and implementation upkeep. The topics below keep the full
      change list and contributor credits available for people working on OpenClaw.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 8-pricing-model-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: pricing-model
  title: 8 Pricing Model changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/Lovable/2026-09-23-image-and-video-generation-now-appear-in-usage-details|Image
  and video generation now appear in Usage details]]'
- '[[Changes/Lovable/2026-09-23-see-the-estimated-monthly-cloud-cost-of-each-database-size|See
  the estimated monthly Cloud cost of each database size]]'
- '[[Changes/Microsoft 365 Copilot/2026-09-23-github-copilot-ai-cost-dashboard-in-insights-web-microsoft-365-copilot|GitHub
  Copilot AI cost dashboard in Insights Web (Microsoft 365 Copilot)]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: pricing-model
title: 8 Pricing Model changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Pricing Model changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/pricing-model|Pricing Model]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> GPT-6 Sol and Luna give you two new choices for text, images, and tool use through the OpenAI Responses API or ChatGPT sign-in. For embedded ChatGPT use, explicitly choose the OpenClaw runtime ; setting the model alone does not select it. Existing selections and the Astra setup default stay unchanged. Luna has lower standard API rates in the shipped catalog, at $0.10 input and $0.50 output per million tokens compared with Sol's $2 input and $10 output. Different pricing tiers apply above 272,000 input tokens.

> Bundled Codex 0.155.1 also lets eligible ChatGPT accounts discover and use both models through native Codex. After starting or upgrading OpenClaw, /codex models shows your account's choices . Embedded reasoning supports none through max, with medium as the default when supported; native effort choices depend on the account. The separate Luna Reserve route and its billing distinction remain unchanged.

> Budget errors no longer trigger futile retries merely because a billing-help URL contains limit-related wording. Upstream server failures also report as server errors instead of misleading timeouts, while genuine rate limits, timing failures, and overload retain their existing handling.

> Unknown model costs are now left unavailable instead of appearing as free usage, while explicitly free rates and provider-billed zero totals remain zero. Recorded charges retain their request-time pricing. Plugin consumers should handle the optional usage.costUsd field being absent.

> Codex usage views now label Luna Reserve as a separate route. Unused Reserve quota does not cover ordinary Luna requests, including with Fast off, and ordinary Luna may still consume credits. This clarifies the display without enabling Reserve routing; account counters are not per-request billing receipts.

> Portable cloud workers now include the browser assets needed for provisioning and the SQLite executable needed for authorized shell commands, at the cost of a larger runtime download. After a Gateway restart, unstarted submissions can wait up to two minutes for retained workers to reconnect, capped by the turn timeout, with one retry and Stop still available. Work already handed off is not resent, and incompatible worker runtimes still need an update.

> Brave, Exa, paid Parallel, and Perplexity Search honor the requested number of structured results, including cached replies, and Brave’s LLM-context cache keeps different requested counts separate. Local trimming does not reduce upstream billing. Canceled or timed-out xAI searches stop waiting for credentials without later sending the search, while already-owned credential refresh and cleanup may finish independently. Search results also omit impossible calendar dates without dropping or reordering the results.

> This release includes 1175 maintainer and internal changes covering tests, development tools and implementation upkeep. The topics below keep the full change list and contributor credits available for people working on OpenClaw.

Source: https://docs.openclaw.ai/releases/2026.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-23-50-safety-and-privacy-changes-in-v2026-9-6|50 Safety and Privacy changes in v2026.9.6]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-23-localization-maintenance-removes-entries-whose-interface-text-has-already-been-r|Localization maintenance removes entries whose interface text has already been…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-23-5-reliability-and-performance-changes-in-v2026-9-6|5 Reliability and Performance changes in v2026.9.6]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-23-2-image-generation-changes-in-v2026-9-6|2 Image Generation changes in v2026.9.6]] · Image Generation
- [[Changes/OpenClaw/2026-09-23-18-voice-and-audio-changes-in-v2026-9-6|18 Voice and Audio changes in v2026.9.6]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-23-25-context-window-changes-in-v2026-9-6|25 Context Window changes in v2026.9.6]] · Context Window
- [[Changes/OpenClaw/2026-09-23-16-mobile-and-desktop-changes-in-v2026-9-6|16 Mobile and Desktop changes in v2026.9.6]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-23-41-agent-mode-changes-in-v2026-9-6|41 Agent Mode changes in v2026.9.6]] · Agent Mode
- [[Changes/OpenClaw/2026-09-23-16-collaboration-changes-in-v2026-9-6|16 Collaboration changes in v2026.9.6]] · Collaboration
- [[Changes/OpenClaw/2026-09-23-15-editor-experience-changes-in-v2026-9-6|15 Editor Experience changes in v2026.9.6]] · Editor Experience
- [[Changes/OpenClaw/2026-09-23-2-enterprise-and-administration-changes-in-v2026-9-6|2 Enterprise and Administration changes in v2026.9.6]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-23-31-developer-workflow-changes-in-v2026-9-6|31 Developer Workflow changes in v2026.9.6]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-23-plugin-requested-answer-revisions-wait-for-session-history-to-become-available-a|Plugin-requested answer revisions wait for session history to become available…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-23-6-files-and-data-changes-in-v2026-9-6|6 Files and Data changes in v2026.9.6]] · Files and Data
- [[Changes/OpenClaw/2026-09-23-58-apps-and-integrations-changes-in-v2026-9-6|58 Apps and Integrations changes in v2026.9.6]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-23-17-account-and-access-changes-in-v2026-9-6|17 Account and Access changes in v2026.9.6]] · Account and Access
- [[Changes/OpenClaw/2026-09-23-background-image-video-and-music-generation-can-complete-independently-of-the-re|Background image, video, and music generation can complete independently…]] · Music Generation
- [[Changes/OpenClaw/2026-09-23-23-memory-and-personalization-changes-in-v2026-9-6|23 Memory and Personalization changes in v2026.9.6]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-23-3-search-and-browsing-changes-in-v2026-9-6|3 Search and Browsing changes in v2026.9.6]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-23-19-interface-experience-changes-in-v2026-9-6|19 Interface Experience changes in v2026.9.6]] · Interface Experience
- [[Changes/OpenClaw/2026-09-23-9-automation-and-scheduling-changes-in-v2026-9-6|9 Automation and Scheduling changes in v2026.9.6]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-23-22-model-support-changes-in-v2026-9-6|22 Model Support changes in v2026.9.6]] · Model Support
- [[Changes/OpenClaw/2026-09-23-119-other-changes-in-v2026-9-6|119 other changes in v2026.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-09-23 · Microsoft 365 Copilot · [[Changes/Microsoft 365 Copilot/2026-09-23-github-copilot-ai-cost-dashboard-in-insights-web-microsoft-365-copilot|GitHub Copilot AI cost dashboard in Insights Web (Microsoft 365 Copilot)]]
- Later: 2026-09-24 · Claude Code · [[Changes/Claude Code/2026-09-24-updated-the-claude-api-skill-pre-output-refusal-billing-now-links-to-the-how-ref|Updated the claude-api skill]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-11 · Descript · [[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer Invoices]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-884524&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-8-pricing-model-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-884524%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->