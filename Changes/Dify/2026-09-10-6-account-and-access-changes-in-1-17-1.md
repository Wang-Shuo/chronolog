---
card_id: dify-2026-09-10-c9bf00
date: '2026-09-10'
description: 'Dify · 2026-09-10 · Account and Access: 6 changes in v1.17.1 - Bug Fixes
  and Improvements — **Gmail addresses that differ only by dots or a `+alias` registered…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2235
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 10ba513efd57e168e7ae76651fbfe4a332be14673d82a917f134746336087cdd
product: dify
product_name: Dify
record:
  card_id: dify-2026-09-10-c9bf00
  comparison: ''
  date: '2026-09-10'
  description: 'Dify — v1.17.1 - Bug Fixes and Improvements: 6 Account and Access
    changes'
  evidence:
  - quote: '**Gmail addresses that differ only by dots or a `+alias` registered as
      separate accounts.** Registration now stores and checks a normalized email —
      dots stripped, `+alias` removed, `googlemail.com` folded to `gmail.com` — across
      self-registration, OAuth registration, email-code account creation, CLI registration,
      and new workspace-invite accounts, with a dedicated `normalized_email_already_in_use`
      error. Existing login and account-update lookups are deliberately unchanged,
      and existing equivalent accounts are preserved. (#41249)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'The console and web apps received a broad pass targeting the parts that
      made them unusable without a mouse or a screen reader: form controls got correct
      labels and programmatically associated validation feedback (#42096); sortable
      lists and panel/node resizing became keyboard-operable (#41974, #41963); focus
      is restored to its origin after overlays and comment threads close instead of
      being dropped to the document (#42068, #41978); page landmarks and heading structure
      were corrected so screen-reader users can navigate by region (#41938); button-styled
      navigation kept its link semantics so it still works with middle-click and modifier-click
      (#41312); decorative content and redundant list semantics were hidden from assistive
      technology (#42060); and clickable `div`s were replaced with native buttons
      in dataset lists (#41319). The apps list, home page, and login/signup flows
      were each covered as a whole (#41393, #41310, #41301).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(api): thin OAuth controllers and extract application services
      by @41tair in https://github.com/langgenius/dify/pull/40692'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(api): extract account login service and consolidate adapters
      by @41tair in https://github.com/langgenius/dify/pull/41184'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(api): decouple console OAuth flow from legacy account services
      by @41tair in https://github.com/langgenius/dify/pull/41188'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(api): move OpenAPI account access behind application services
      by @41tair in https://github.com/langgenius/dify/pull/41308'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 6-account-and-access-changes-in-1-17-1
  source_release: dify-2026-09-10-1-17-1-github-386157159-e472b6fe
  source_type: github_releases
  theme: account-access
  title: 6 Account and Access changes in 1.17.1
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-08-8-account-and-access-changes-in-v2026-9-3|8 Account
  and Access changes in v2026.9.3]]'
- '[[Changes/Codex CLI/2026-09-09-5-account-and-access-changes-in-rust-v0-154-0|5
  Account and Access changes in rust-v0.154.0]]'
- '[[Changes/Claude Code/2026-09-10-2-account-and-access-changes-in-v2-1-268|2 Account
  and Access changes in v2.1.268]]'
source_release: '[[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|dify-2026-09-10-1-17-1-github-386157159-e472b6fe]]'
source_type: github_releases
theme: account-access
title: 6 Account and Access changes in 1.17.1
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Account and Access changes in 1.17.1

**Dify** · 2026-09-10 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.1) · from [[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|v1.17.1 - Bug Fixes and Improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Gmail addresses that differ only by dots or a `+alias` registered as separate accounts.** Registration now stores and checks a normalized email — dots stripped, `+alias` removed, `googlemail.com` folded to `gmail.com` — across self-registration, OAuth registration, email-code account creation, CLI registration, and new workspace-invite accounts, with a dedicated `normalized_email_already_in_use` error. Existing login and account-update lookups are deliberately unchanged, and existing equivalent accounts are preserved. (#41249)

> The console and web apps received a broad pass targeting the parts that made them unusable without a mouse or a screen reader: form controls got correct labels and programmatically associated validation feedback (#42096); sortable lists and panel/node resizing became keyboard-operable (#41974, #41963); focus is restored to its origin after overlays and comment threads close instead of being dropped to the document (#42068, #41978); page landmarks and heading structure were corrected so screen-reader users can navigate by region (#41938); button-styled navigation kept its link semantics so it still works with middle-click and modifier-click (#41312); decorative content and redundant list semantics were hidden from assistive technology (#42060); and clickable `div`s were replaced with native buttons in dataset lists (#41319). The apps list, home page, and login/signup flows were each covered as a whole (#41393, #41310, #41301).

> refactor(api): thin OAuth controllers and extract application services by @41tair in https://github.com/langgenius/dify/pull/40692

> refactor(api): extract account login service and consolidate adapters by @41tair in https://github.com/langgenius/dify/pull/41184

> refactor(api): decouple console OAuth flow from legacy account services by @41tair in https://github.com/langgenius/dify/pull/41188

> refactor(api): move OpenAPI account access behind application services by @41tair in https://github.com/langgenius/dify/pull/41308

Source: https://github.com/langgenius/dify/releases/tag/1.17.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-09-10-4-pricing-model-changes-in-1-17-1|4 Pricing Model changes in 1.17.1]] · Pricing Model
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
- [[Changes/Dify/2026-09-10-3-multimodal-input-changes-in-1-17-1|3 Multimodal Input changes in 1.17.1]] · Multimodal Input
- [[Changes/Dify/2026-09-10-6-editor-experience-changes-in-1-17-1|6 Editor Experience changes in 1.17.1]] · Editor Experience
- [[Changes/Dify/2026-09-10-3-accessibility-and-localization-changes-in-1-17-1|3 Accessibility and Localization changes in 1.17.1]] · Accessibility and Localization
- [[Changes/Dify/2026-09-10-a-plugin-could-exhaust-worker-memory-with-one-declared-number-the-blob-chunk-mer|A plugin could exhaust worker memory with one declared number. The blob chunk…]] · Reliability and Performance
- [[Changes/Dify/2026-09-10-6-context-window-changes-in-1-17-1|6 Context Window changes in 1.17.1]] · Context Window
- [[Changes/Dify/2026-09-10-205-other-changes-in-1-17-1|205 other changes in 1.17.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-10 · Claude Code · [[Changes/Claude Code/2026-09-10-2-account-and-access-changes-in-v2-1-268|2 Account and Access changes in v2.1.268]]
- Later: 2026-09-11 · Lovable · [[Changes/Lovable/2026-09-11-require-two-factor-authentication-for-your-workspace|Require two-factor authentication for your workspace]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-09-10-c9bf00&body=Card%3A%20Changes%2FDify%2F2026-09-10-6-account-and-access-changes-in-1-17-1.md%0ACard%20ID%3A%20dify-2026-09-10-c9bf00%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->