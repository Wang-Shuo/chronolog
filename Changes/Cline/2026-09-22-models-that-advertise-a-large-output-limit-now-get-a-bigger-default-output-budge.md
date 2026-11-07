---
card_id: cline-2026-09-22-37e0c8
date: '2026-09-22'
description: 'Cline · 2026-09-22 · Pricing Model: Models that advertise a large output
  limit now get a bigger default output budget — 30% of the limit rather than a flat…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily
    limit: To ensure a high-quality experience for all ChatGPT users, we…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1377
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: pricing
machine_hash: 7845317acac6eee8a0d90b09a525eda917472331846581fb9d3c29640c013376
product: cline
product_name: Cline
record:
  card_id: cline-2026-09-22-37e0c8
  comparison: ''
  date: '2026-09-22'
  description: 'Cline — v4.1.20: Models that advertise a large output limit now get
    a bigger default output budget — 30% of the limit rather than a flat 32,000 tokens,
    whichever is larger. Nothing changes for models under roughly 107k output tokens;
    longer responses can mean higher per-turn cost and latency.'
  evidence:
  - quote: Models that advertise a large output limit now get a bigger default output
      budget — 30% of the limit rather than a flat 32,000 tokens, whichever is larger.
      Nothing changes for models under roughly 107k output tokens; longer responses
      can mean higher per-turn cost and latency.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.20
  extractor_version: fallback-v5
  impact: incremental
  kind: pricing
  product: cline
  product_name: Cline
  slug: models-that-advertise-a-large-output-limit-now-get-a-bigger-default-output-budge
  source_release: cline-2026-09-22-v4-1-20-github-394105689-95df91cb
  source_type: github_releases
  theme: pricing-model
  theme_matches:
  - matched_terms:
    - tokens
    score: 50
    theme: context-window
  - matched_terms:
    - models
    score: 50
    theme: model-support
  - matched_terms:
    - latency
    score: 50
    theme: reliability-performance
  theme_resolution: manual-semantic-rule-v1
  title: Models that advertise a large output limit now get a bigger default output
    budget
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-19-6-pricing-model-changes-in-v2026-9-5|6 Pricing Model
  changes in v2026.9.5]]'
- '[[Changes/ElevenLabs/2026-09-21-user|User]]'
- '[[Changes/Claude Code/2026-09-22-improved-cost-cache-miss-causes-to-name-thinking-mode-and-thinking-display-chang|Improved
  /cost cache-miss causes to name thinking mode and thinking display changes]]'
source_release: '[[Releases/Cline/cline-2026-09-22-v4-1-20-github-394105689-95df91cb|cline-2026-09-22-v4-1-20-github-394105689-95df91cb]]'
source_type: github_releases
theme: pricing-model
title: Models that advertise a large output limit now get a bigger default output
  budget
type: change
---

<!-- chronolog:begin region="header" -->
# Models that advertise a large output limit now get a bigger default output budget

**Cline** · 2026-09-22 · [[Themes/pricing-model|Pricing Model]] · Pricing · [Official source](https://github.com/cline/cline/releases/tag/v4.1.20) · from [[Releases/Cline/cline-2026-09-22-v4-1-20-github-394105689-95df91cb|v4.1.20]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Models that advertise a large output limit now get a bigger default output budget — 30% of the limit rather than a flat 32,000 tokens, whichever is larger. Nothing changes for models under roughly 107k output tokens; longer responses can mean higher per-turn cost and latency.
>
> Source: https://github.com/cline/cline/releases/tag/v4.1.20
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-09-22-3-model-support-changes-in-v4-1-20|3 Model Support changes in v4.1.20]] · Model Support
- [[Changes/Cline/2026-09-22-output-from-background-commands-now-streams-into-the-command-row-while-the-comma|Output from background commands now streams into the command row while the command…]] · Developer Workflow
- [[Changes/Cline/2026-09-22-2-agent-mode-changes-in-v4-1-20|2 Agent Mode changes in v4.1.20]] · Agent Mode
- [[Changes/Cline/2026-09-22-rules-are-found-and-shown-consistently-the-rules-panel-listed-only-clinerules-an|Rules are found and shown consistently]] · Mobile and Desktop
- [[Changes/Cline/2026-09-22-2-context-window-changes-in-v4-1-20|2 Context Window changes in v4.1.20]] · Context Window
- [[Changes/Cline/2026-09-22-2-other-changes-in-v4-1-20|2 other changes in v4.1.20]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-improved-cost-cache-miss-causes-to-name-thinking-mode-and-thinking-display-chang|Improved /cost cache-miss causes to name thinking mode and thinking display changes]]
- Later: 2026-09-23 · Cursor · [[Changes/Cursor/2026-09-23-for-the-next-10-days-we-re-including-usage-credits-so-teams-can-try-rollouts-on|For the next 10 days, we're including usage credits so teams can try Rollouts…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily limit: To ensure a high-quality experience for all ChatGPT users, we…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-09-22-37e0c8&body=Card%3A%20Changes%2FCline%2F2026-09-22-models-that-advertise-a-large-output-limit-now-get-a-bigger-default-output-budge.md%0ACard%20ID%3A%20cline-2026-09-22-37e0c8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.20%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->