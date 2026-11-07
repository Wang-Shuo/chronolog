---
card_id: dify-2026-09-10-15c1e0
date: '2026-09-10'
description: 'Dify · 2026-09-10 · Pricing Model: 4 changes in v1.17.1 - Bug Fixes
  and Improvements — **Lease-based triggers stopped working after about a week.**…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily
    limit: To ensure a high-quality experience for all ChatGPT users, we…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1365
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: aa6cfd47647449ef91e7713ed9086f765ecc014a964ac3951101daaf3a819216
product: dify
product_name: Dify
record:
  card_id: dify-2026-09-10-15c1e0
  comparison: ''
  date: '2026-09-10'
  description: 'Dify — v1.17.1 - Bug Fixes and Improvements: 4 Pricing Model changes'
  evidence:
  - quote: '**Lease-based triggers stopped working after about a week.** Subscription
      creation persisted the builder''s placeholder `expires_at` of `-1` instead of
      the real lease returned by the provider, and the refresh scanner skips `-1`
      — so providers like Gmail `users.watch` silently expired. The provider-supplied
      expiry is now stored. (#41773)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(web): simplify pricing components by @lyzno1 in https://github.com/langgenius/dify/pull/41416'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(api): remove legacy billing enabled state by @lyzno1 in https://github.com/langgenius/dify/pull/41917'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(web): isolate pricing modal state and lifecycle by @lyzno1 in
      https://github.com/langgenius/dify/pull/41960'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 4-pricing-model-changes-in-1-17-1
  source_release: dify-2026-09-10-1-17-1-github-386157159-e472b6fe
  source_type: github_releases
  theme: pricing-model
  title: 4 Pricing Model changes in 1.17.1
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-09-pro-200-month-unlimited-gpt-live-1-usage|Pro ($200/month):
  Unlimited GPT-Live-1 usage]]'
- '[[Changes/ChatGPT/2026-09-09-pro-100-month-up-to-15-hours-with-gpt-live-1|Pro ($100/month):
  Up to 15 hours with GPT-Live-1]]'
- '[[Changes/Claude Code/2026-09-10-2-pricing-model-changes-in-v2-1-268|2 Pricing
  Model changes in v2.1.268]]'
source_release: '[[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|dify-2026-09-10-1-17-1-github-386157159-e472b6fe]]'
source_type: github_releases
theme: pricing-model
title: 4 Pricing Model changes in 1.17.1
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Pricing Model changes in 1.17.1

**Dify** · 2026-09-10 · [[Themes/pricing-model|Pricing Model]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.1) · from [[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|v1.17.1 - Bug Fixes and Improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Lease-based triggers stopped working after about a week.** Subscription creation persisted the builder's placeholder `expires_at` of `-1` instead of the real lease returned by the provider, and the refresh scanner skips `-1` — so providers like Gmail `users.watch` silently expired. The provider-supplied expiry is now stored. (#41773)

> refactor(web): simplify pricing components by @lyzno1 in https://github.com/langgenius/dify/pull/41416

> refactor(api): remove legacy billing enabled state by @lyzno1 in https://github.com/langgenius/dify/pull/41917

> refactor(web): isolate pricing modal state and lifecycle by @lyzno1 in https://github.com/langgenius/dify/pull/41960

Source: https://github.com/langgenius/dify/releases/tag/1.17.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-09-10-3-automation-and-scheduling-changes-in-1-17-1|3 Automation and Scheduling changes in 1.17.1]] · Automation and Scheduling
- [[Changes/Dify/2026-09-10-8-interface-experience-changes-in-1-17-1|8 Interface Experience changes in 1.17.1]] · Interface Experience
- [[Changes/Dify/2026-09-10-76-model-support-changes-in-1-17-1|76 Model Support changes in 1.17.1]] · Model Support
- [[Changes/Dify/2026-09-10-42-agent-mode-changes-in-1-17-1|42 Agent Mode changes in 1.17.1]] · Agent Mode
- [[Changes/Dify/2026-09-10-4-developer-workflow-changes-in-1-17-1|4 Developer Workflow changes in 1.17.1]] · Developer Workflow
- [[Changes/Dify/2026-09-10-3-collaboration-changes-in-1-17-1|3 Collaboration changes in 1.17.1]] · Collaboration
- [[Changes/Dify/2026-09-10-2-memory-and-personalization-changes-in-1-17-1|2 Memory and Personalization changes in 1.17.1]] · Memory and Personalization
- [[Changes/Dify/2026-09-10-16-safety-and-privacy-changes-in-1-17-1|16 Safety and Privacy changes in 1.17.1]] · Safety and Privacy
- [[Changes/Dify/2026-09-10-13-files-and-data-changes-in-1-17-1|13 Files and Data changes in 1.17.1]] · Files and Data
- [[Changes/Dify/2026-09-10-skill-packages-built-on-windows-failed-with-a-misleading-error-a-skill-md-using|Skill packages built on Windows failed with a misleading error. A SKILL.md…]] · Mobile and Desktop
- [[Changes/Dify/2026-09-10-12-apps-and-integrations-changes-in-1-17-1|12 Apps and Integrations changes in 1.17.1]] · Apps and Integrations
- [[Changes/Dify/2026-09-10-6-account-and-access-changes-in-1-17-1|6 Account and Access changes in 1.17.1]] · Account and Access
- [[Changes/Dify/2026-09-10-3-multimodal-input-changes-in-1-17-1|3 Multimodal Input changes in 1.17.1]] · Multimodal Input
- [[Changes/Dify/2026-09-10-6-editor-experience-changes-in-1-17-1|6 Editor Experience changes in 1.17.1]] · Editor Experience
- [[Changes/Dify/2026-09-10-3-accessibility-and-localization-changes-in-1-17-1|3 Accessibility and Localization changes in 1.17.1]] · Accessibility and Localization
- [[Changes/Dify/2026-09-10-a-plugin-could-exhaust-worker-memory-with-one-declared-number-the-blob-chunk-mer|A plugin could exhaust worker memory with one declared number. The blob chunk…]] · Reliability and Performance
- [[Changes/Dify/2026-09-10-6-context-window-changes-in-1-17-1|6 Context Window changes in 1.17.1]] · Context Window
- [[Changes/Dify/2026-09-10-205-other-changes-in-1-17-1|205 other changes in 1.17.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-09-10 · Claude Code · [[Changes/Claude Code/2026-09-10-2-pricing-model-changes-in-v2-1-268|2 Pricing Model changes in v2.1.268]]
- Later: 2026-09-10 · Lovable · [[Changes/Lovable/2026-09-10-share-your-lovable-invite-link-from-your-phone|Share your Lovable invite link from your phone]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily limit: To ensure a high-quality experience for all ChatGPT users, we…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-09-10-15c1e0&body=Card%3A%20Changes%2FDify%2F2026-09-10-4-pricing-model-changes-in-1-17-1.md%0ACard%20ID%3A%20dify-2026-09-10-15c1e0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->