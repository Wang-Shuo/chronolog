---
card_id: lovable-2026-07-08-e6b6e4
date: '2026-07-08'
description: 'Lovable · 2026-07-08 · Interface Experience: You can now ask Lovable
  in chat to [resize your project''s Lovable Cloud compute…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1276
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 08301e55577929546e0a2fadb06d4836030fe31c079714812149467da4409fc5
product: lovable
product_name: Lovable
record:
  card_id: lovable-2026-07-08-e6b6e4
  comparison: ''
  date: '2026-07-08'
  description: 'Lovable — Lovable updates — 2026-07-08: You can now ask Lovable in
    chat to [resize your project''s Lovable Cloud compute instance](https://docs.lovable.dev/features/database-performance.md#ask-lovable-to-resize-your-instance),
    instead of opening Advanced settings yourself. Describe the problem, such as a
    backend that is slow under load, and Lovable offers a size picker (Tiny through
    Large) with your current size preselected.'
  evidence:
  - quote: You can now ask Lovable in chat to [resize your project's Lovable Cloud
      compute instance](https://docs.lovable.dev/features/database-performance.md#ask-lovable-to-resize-your-instance),
      instead of opening Advanced settings yourself. Describe the problem, such as
      a backend that is slow under load, and Lovable offers a size picker (Tiny through
      Large) with your current size preselected.
    source_release: https://docs.lovable.dev/changelog
  - quote: Resizing changes the compute instance, its CPU and memory, not your database
      storage. A larger instance handles more traffic and heavier database work and
      increases your ongoing Cloud usage, and a smaller instance reduces it. Resizing
      takes a few minutes, during which the backend is briefly unavailable.
    source_release: https://docs.lovable.dev/changelog
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: lovable
  product_name: Lovable
  slug: resize-your-cloud-instance-from-chat
  source_release: lovable-2026-07-08-2026-07-08-6cd655f7
  source_type: lovable_changelog
  theme: interface-experience
  theme_matches:
  - matched_terms:
    - picker
    score: 50
    theme: interface-experience
  - matched_terms:
    - performance
    score: 50
    theme: reliability-performance
  theme_resolution: manual-semantic-rule-v1
  title: Resize your Cloud instance from chat
  type: change
related_changes:
- '[[Changes/OpenCode/2026-07-07-restore-model-details-tooltips-in-the-model-picker|Restore
  model details tooltips in the model picker]]'
- '[[Changes/v0/2026-07-07-3-interface-experience-changes-in-grouped-tool-approvals-richer-mcp|3
  Interface Experience changes in Grouped tool approvals, richer MCP…]]'
- '[[Changes/Lovable/2026-07-08-search-your-settings|Search your settings]]'
source_release: '[[Releases/Lovable/lovable-2026-07-08-2026-07-08-6cd655f7|lovable-2026-07-08-2026-07-08-6cd655f7]]'
source_type: lovable_changelog
theme: interface-experience
title: Resize your Cloud instance from chat
type: change
---

<!-- chronolog:begin region="header" -->
# Resize your Cloud instance from chat

**Lovable** · 2026-07-08 · [[Themes/interface-experience|Interface Experience]] · Launch · [Official source](https://docs.lovable.dev/changelog) · from [[Releases/Lovable/lovable-2026-07-08-2026-07-08-6cd655f7|Lovable updates — 2026-07-08]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> You can now ask Lovable in chat to [resize your project's Lovable Cloud compute instance](https://docs.lovable.dev/features/database-performance.md#ask-lovable-to-resize-your-instance), instead of opening Advanced settings yourself. Describe the problem, such as a backend that is slow under load, and Lovable offers a size picker (Tiny through Large) with your current size preselected.
>
> Resizing changes the compute instance, its CPU and memory, not your database storage. A larger instance handles more traffic and heavier database work and increases your ongoing Cloud usage, and a smaller instance reduces it. Resizing takes a few minutes, during which the backend is briefly unavailable.
>
> Source: https://docs.lovable.dev/changelog
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Lovable/2026-07-08-pause-a-lovable-cloud-project|Pause a Lovable Cloud project]] · Editor Experience
- [[Changes/Lovable/2026-07-08-reference-a-connector-in-chat|Reference a connector in chat]] · Apps and Integrations
- [[Changes/Lovable/2026-07-08-search-your-settings|Search your settings]] · Interface Experience
- [[Changes/Lovable/2026-07-08-configure-sso-just-in-time-provisioning-from-settings|Configure SSO Just-in-Time provisioning from settings]] · Account and Access
- [[Changes/Lovable/2026-07-08-images-lovable-generates-are-labeled-as-ai-generated|Images Lovable generates are labeled as AI-generated]] · Image Generation
- [[Changes/Lovable/2026-07-08-workspace-insights-now-on-business-plans|Workspace insights now on Business plans]] · Enterprise and Administration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-07-07 · v0 · [[Changes/v0/2026-07-07-3-interface-experience-changes-in-grouped-tool-approvals-richer-mcp|3 Interface Experience changes in Grouped tool approvals, richer MCP…]]
- Later: 2026-07-09 · Cline · [[Changes/Cline/2026-07-09-2-interface-experience-changes-in-v4-0-7|2 Interface Experience changes in v4.0.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20lovable-2026-07-08-e6b6e4&body=Card%3A%20Changes%2FLovable%2F2026-07-08-resize-your-cloud-instance-from-chat.md%0ACard%20ID%3A%20lovable-2026-07-08-e6b6e4%0ASource%3A%20https%3A%2F%2Fdocs.lovable.dev%2Fchangelog%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->