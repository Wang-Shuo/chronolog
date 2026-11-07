---
card_id: dify-2026-04-29-9872e8
date: '2026-04-29'
description: 'Dify · 2026-04-29 · Safety and Privacy: 7 changes in v1.14.0 — chore:
  try to avoid supply chain security by @hyoban in…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2101
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6d673c5b701bb2e6c8a881c4f4c0c81d9bb93bce83847cc980ba6965d158b24e
product: dify
product_name: Dify
record:
  card_id: dify-2026-04-29-9872e8
  comparison: ''
  date: '2026-04-29'
  description: 'Dify — v1.14.0: 7 Safety and Privacy changes'
  evidence:
  - quote: 'chore: try to avoid supply chain security by @hyoban in https://github.com/langgenius/dify/pull/34317'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): replace json.loads with Pydantic validation in security
      and tools layers by @eureka0928 in https://github.com/langgenius/dify/pull/34380'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: remove dataset permission mock tests superseded by testcontainers
      by @bittoby in https://github.com/langgenius/dify/pull/34936'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'test: migrate BillingService permission-check tests to Testcontainers
      integration tests by @wdeveloper16 in https://github.com/langgenius/dify/pull/34993'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): improve type safety in MCPToolManageService.execute_auth_actions
      by @dev-miro26 in https://github.com/langgenius/dify/pull/34824'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor: convert plugin permission if/elif to match/case (#30001) by
      @aether-png in https://github.com/langgenius/dify/pull/35140'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  - quote: 'refactor(api): add null safety to extractor_processor and firecrawl by
      @tmimmanuel in https://github.com/langgenius/dify/pull/35209'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 7-safety-and-privacy-changes-in-1-14-0
  source_release: dify-2026-04-29-1-14-0-github-314986233-63073e86
  source_type: github_releases
  theme: safety-privacy
  title: 7 Safety and Privacy changes in 1.14.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-04-27-location-based-permission-persistence-is-now-enabled-by-default-so-approvals-car|Location-based
  permission persistence is now enabled by default, so approvals carry…]]'
- '[[Changes/Gemini CLI/2026-04-28-feat-sandbox-resolve-custom-seatbelt-profiles-from-home-gemini-first-by-mvanhorn|feat(sandbox):
  resolve custom seatbelt profiles from $HOME/.gemini first]]'
- '[[Changes/GitHub Copilot CLI/2026-04-28-allow-acp-clients-to-toggle-allow-all-permission-mode-via-session-configuration|Allow
  ACP clients to toggle allow-all permission mode via session configuration]]'
source_release: '[[Releases/Dify/dify-2026-04-29-1-14-0-github-314986233-63073e86|dify-2026-04-29-1-14-0-github-314986233-63073e86]]'
source_type: github_releases
theme: safety-privacy
title: 7 Safety and Privacy changes in 1.14.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in 1.14.0

**Dify** · 2026-04-29 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.14.0) · from [[Releases/Dify/dify-2026-04-29-1-14-0-github-314986233-63073e86|v1.14.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> chore: try to avoid supply chain security by @hyoban in https://github.com/langgenius/dify/pull/34317

> refactor(api): replace json.loads with Pydantic validation in security and tools layers by @eureka0928 in https://github.com/langgenius/dify/pull/34380

> test: remove dataset permission mock tests superseded by testcontainers by @bittoby in https://github.com/langgenius/dify/pull/34936

> test: migrate BillingService permission-check tests to Testcontainers integration tests by @wdeveloper16 in https://github.com/langgenius/dify/pull/34993

> refactor(api): improve type safety in MCPToolManageService.execute_auth_actions by @dev-miro26 in https://github.com/langgenius/dify/pull/34824

> refactor: convert plugin permission if/elif to match/case (#30001) by @aether-png in https://github.com/langgenius/dify/pull/35140

> refactor(api): add null safety to extractor_processor and firecrawl by @tmimmanuel in https://github.com/langgenius/dify/pull/35209

Source: https://github.com/langgenius/dify/releases/tag/1.14.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-04-29-13-files-and-data-changes-in-1-14-0|13 Files and Data changes in 1.14.0]] · Files and Data
- [[Changes/Dify/2026-04-29-2-developer-workflow-changes-in-1-14-0|2 Developer Workflow changes in 1.14.0]] · Developer Workflow
- [[Changes/Dify/2026-04-29-10-interface-experience-changes-in-1-14-0|10 Interface Experience changes in 1.14.0]] · Interface Experience
- [[Changes/Dify/2026-04-29-27-model-support-changes-in-1-14-0|27 Model Support changes in 1.14.0]] · Model Support
- [[Changes/Dify/2026-04-29-2-accessibility-and-localization-changes-in-1-14-0|2 Accessibility and Localization changes in 1.14.0]] · Accessibility and Localization
- [[Changes/Dify/2026-04-29-6-editor-experience-changes-in-1-14-0|6 Editor Experience changes in 1.14.0]] · Editor Experience
- [[Changes/Dify/2026-04-29-7-pricing-model-changes-in-1-14-0|7 Pricing Model changes in 1.14.0]] · Pricing Model
- [[Changes/Dify/2026-04-29-48-apps-and-integrations-changes-in-1-14-0|48 Apps and Integrations changes in 1.14.0]] · Apps and Integrations
- [[Changes/Dify/2026-04-29-13-collaboration-changes-in-1-14-0|13 Collaboration changes in 1.14.0]] · Collaboration
- [[Changes/Dify/2026-04-29-8-account-and-access-changes-in-1-14-0|8 Account and Access changes in 1.14.0]] · Account and Access
- [[Changes/Dify/2026-04-29-2-agent-mode-changes-in-1-14-0|2 Agent Mode changes in 1.14.0]] · Agent Mode
- [[Changes/Dify/2026-04-29-3-automation-and-scheduling-changes-in-1-14-0|3 Automation and Scheduling changes in 1.14.0]] · Automation and Scheduling
- [[Changes/Dify/2026-04-29-2-enterprise-and-administration-changes-in-1-14-0|2 Enterprise and Administration changes in 1.14.0]] · Enterprise and Administration
- [[Changes/Dify/2026-04-29-3-context-window-changes-in-1-14-0|3 Context Window changes in 1.14.0]] · Context Window
- [[Changes/Dify/2026-04-29-3-reliability-and-performance-changes-in-1-14-0|3 Reliability and Performance changes in 1.14.0]] · Reliability and Performance
- [[Changes/Dify/2026-04-29-520-other-changes-in-1-14-0|520 other changes in 1.14.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-28 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-28-allow-acp-clients-to-toggle-allow-all-permission-mode-via-session-configuration|Allow ACP clients to toggle allow-all permission mode via session configuration]]
- Later: 2026-04-30 · Codex CLI · [[Changes/Codex CLI/2026-04-30-21-safety-and-privacy-changes-in-rust-v0-128-0|21 Safety and Privacy changes in rust-v0.128.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-04-29-9872e8&body=Card%3A%20Changes%2FDify%2F2026-04-29-7-safety-and-privacy-changes-in-1-14-0.md%0ACard%20ID%3A%20dify-2026-04-29-9872e8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.14.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->