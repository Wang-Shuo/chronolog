---
card_id: dify-2026-07-28-53612d
date: '2026-07-28'
description: 'Dify · 2026-07-28 · Interface Experience: 10 changes in v1.16.1 - Bug
  Fixes and Security Enhancements — The block selector panel now features improved
  keyboard…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1296
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f602193817da532ce405cece6b57add3b1a712e182b2d1ce4adec875d3ebb2d0
product: dify
product_name: Dify
record:
  card_id: dify-2026-07-28-53612d
  comparison: ''
  date: '2026-07-28'
  description: 'Dify — v1.16.1 - Bug Fixes and Security Enhancements: 10 Interface
    Experience changes'
  evidence:
  - quote: The block selector panel now features improved keyboard navigation, category
      previews, and a more intuitive search experience when adding nodes to workflows.
      (#39212)
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: '**Export Agent DSL from Sidebar**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: Agent apps can now be exported as DSL YAML directly from the app sidebar
      menu, making it easy to back up or version-control agent configurations. (#39299)
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: Prevent build reset from clearing preview chat history (#39490)
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: Switched Jinja2 template rendering to use `SandboxedEnvironment`, preventing
      template injection attacks in workflow code nodes (#39609)
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'refactor(web): align integrations sidebar components by @lyzno1 in https://github.com/langgenius/dify/pull/39202'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'feat(workflow): improve block selector navigation and previews by @lyzno1
      in https://github.com/langgenius/dify/pull/39212'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'feat: support export agent dsl in sidebar by @iamjoel in https://github.com/langgenius/dify/pull/39299'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'feat(dataset): add crawl source selection by @hyoban in https://github.com/langgenius/dify/pull/39325'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'test(e2e): wait for app list before menu interaction by @lyzno1 in https://github.com/langgenius/dify/pull/39538'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 10-interface-experience-changes-in-1-16-1
  source_release: dify-2026-07-28-1-16-1-github-360820489-855a9365
  source_type: github_releases
  theme: interface-experience
  title: 10 Interface Experience changes in 1.16.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-24-2-interface-experience-changes-in-v2-1-219|2 Interface
  Experience changes in v2.1.219]]'
- '[[Changes/Open WebUI/2026-07-27-19-interface-experience-changes-in-v0-11-0|19 Interface
  Experience changes in v0.11.0]]'
- '[[Changes/Cursor/2026-07-28-existing-free-users-in-india-can-upgrade-their-plan-from-the-dashboard-new-users-aeb811|Existing
  Free users in India can upgrade their plan from the dashboard]]'
source_release: '[[Releases/Dify/dify-2026-07-28-1-16-1-github-360820489-855a9365|dify-2026-07-28-1-16-1-github-360820489-855a9365]]'
source_type: github_releases
theme: interface-experience
title: 10 Interface Experience changes in 1.16.1
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Interface Experience changes in 1.16.1

**Dify** · 2026-07-28 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.16.1) · from [[Releases/Dify/dify-2026-07-28-1-16-1-github-360820489-855a9365|v1.16.1 - Bug Fixes and Security Enhancements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The block selector panel now features improved keyboard navigation, category previews, and a more intuitive search experience when adding nodes to workflows. (#39212)

> **Export Agent DSL from Sidebar**

> Agent apps can now be exported as DSL YAML directly from the app sidebar menu, making it easy to back up or version-control agent configurations. (#39299)

> Prevent build reset from clearing preview chat history (#39490)

> Switched Jinja2 template rendering to use `SandboxedEnvironment`, preventing template injection attacks in workflow code nodes (#39609)

> refactor(web): align integrations sidebar components by @lyzno1 in https://github.com/langgenius/dify/pull/39202

> feat(workflow): improve block selector navigation and previews by @lyzno1 in https://github.com/langgenius/dify/pull/39212

> feat: support export agent dsl in sidebar by @iamjoel in https://github.com/langgenius/dify/pull/39299

> feat(dataset): add crawl source selection by @hyoban in https://github.com/langgenius/dify/pull/39325

> test(e2e): wait for app list before menu interaction by @lyzno1 in https://github.com/langgenius/dify/pull/39538

Source: https://github.com/langgenius/dify/releases/tag/1.16.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-07-28-11-safety-and-privacy-changes-in-1-16-1|11 Safety and Privacy changes in 1.16.1]] · Safety and Privacy
- [[Changes/Dify/2026-07-28-6-model-support-changes-in-1-16-1|6 Model Support changes in 1.16.1]] · Model Support
- [[Changes/Dify/2026-07-28-refactor-agents-simplify-repository-context-by-lyzno1-in-https-github-com-langge|refactor(agents): simplify repository context]] · Context Window
- [[Changes/Dify/2026-07-28-3-files-and-data-changes-in-1-16-1|3 Files and Data changes in 1.16.1]] · Files and Data
- [[Changes/Dify/2026-07-28-3-collaboration-changes-in-1-16-1|3 Collaboration changes in 1.16.1]] · Collaboration
- [[Changes/Dify/2026-07-28-2-accessibility-and-localization-changes-in-1-16-1|2 Accessibility and Localization changes in 1.16.1]] · Accessibility and Localization
- [[Changes/Dify/2026-07-28-4-developer-workflow-changes-in-1-16-1|4 Developer Workflow changes in 1.16.1]] · Developer Workflow
- [[Changes/Dify/2026-07-28-lightweight-recent-apps-endpoint-new-get-console-api-apps-recent-endpoint-reduce|Lightweight recent apps endpoint]] · Reliability and Performance
- [[Changes/Dify/2026-07-28-feat-web-locate-workflow-nodes-by-node-id-in-the-workflow-editor-by-ruanimal-in|feat(web): locate workflow nodes by node_id in the workflow editor]] · Editor Experience
- [[Changes/Dify/2026-07-28-6-account-and-access-changes-in-1-16-1|6 Account and Access changes in 1.16.1]] · Account and Access
- [[Changes/Dify/2026-07-28-test-use-sqlite-sessions-in-core-memory-by-asukaminato0721-in-https-github-com-l|test: use SQLite sessions in core memory]] · Memory and Personalization
- [[Changes/Dify/2026-07-28-you-can-now-click-a-node-id-in-workflow-run-logs-or-error-messages-to-locate-and|Click a node_id in workflow run logs or error messages to locate and highlight…]] · Files and Data
- [[Changes/Dify/2026-07-28-10-apps-and-integrations-changes-in-1-16-1|10 Apps and Integrations changes in 1.16.1]] · Apps and Integrations
- [[Changes/Dify/2026-07-28-returned-400-instead-of-500-when-file-field-is-missing-from-audio-to-text-endpoi|Returned 400 instead of 500 when file field is missing from audio-to-text…]] · Voice and Audio
- [[Changes/Dify/2026-07-28-24-agent-mode-changes-in-1-16-1|24 Agent Mode changes in 1.16.1]] · Agent Mode
- [[Changes/Dify/2026-07-28-2-pricing-model-changes-in-1-16-1|2 Pricing Model changes in 1.16.1]] · Pricing Model
- [[Changes/Dify/2026-07-28-2-enterprise-and-administration-changes-in-1-16-1|2 Enterprise and Administration changes in 1.16.1]] · Enterprise and Administration
- [[Changes/Dify/2026-07-28-167-other-changes-in-1-16-1|167 other changes in 1.16.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-07-28 · Cursor · [[Changes/Cursor/2026-07-28-existing-free-users-in-india-can-upgrade-their-plan-from-the-dashboard-new-users-aeb811|Existing Free users in India can upgrade their plan from the dashboard]]
- Later: 2026-07-29 · Codex CLI · [[Changes/Codex CLI/2026-07-29-8-interface-experience-changes-in-rust-v0-146-0|8 Interface Experience changes in rust-v0.146.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-07-28-53612d&body=Card%3A%20Changes%2FDify%2F2026-07-28-10-interface-experience-changes-in-1-16-1.md%0ACard%20ID%3A%20dify-2026-07-28-53612d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.16.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->