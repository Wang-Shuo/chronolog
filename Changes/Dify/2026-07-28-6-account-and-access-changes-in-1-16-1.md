---
card_id: dify-2026-07-28-7e792c
date: '2026-07-28'
description: 'Dify · 2026-07-28 · Account and Access: 6 changes in v1.16.1 - Bug Fixes
  and Security Enhancements — Communication between the Dify API and the agent backend…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1216
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cff47e71b114d7d2dbe3fb279955bedac2b27940dd8b78ab5ec42d506074396b
product: dify
product_name: Dify
record:
  card_id: dify-2026-07-28-7e792c
  comparison: ''
  date: '2026-07-28'
  description: 'Dify — v1.16.1 - Bug Fixes and Security Enhancements: 6 Account and
    Access changes'
  evidence:
  - quote: Communication between the Dify API and the agent backend now uses token-based
      authentication via `DIFY_AGENT_API_TOKEN` / `AGENT_BACKEND_API_TOKEN`, hardening
      the internal service boundary. (#39622)
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: '| `DIFY_AGENT_API_TOKEN` | `dify-agent-run-token-for-dev-only` | Shared
      bearer token for API → agent_backend authentication. **Change this in production.**
      |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'refactor(web): use generated OAuth query options by @lyzno1 in https://github.com/langgenius/dify/pull/39204'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'test: move console OAuth coverage to unit tests by @asukaminato0721 in
      https://github.com/langgenius/dify/pull/38923'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'feat(oauth): expose stable account id on provider account endpoint by
      @samzong in https://github.com/langgenius/dify/pull/39470'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'test: use caplog in ext login tests by @EvanYao826 in https://github.com/langgenius/dify/pull/39542'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 6-account-and-access-changes-in-1-16-1
  source_release: dify-2026-07-28-1-16-1-github-360820489-855a9365
  source_type: github_releases
  theme: account-access
  title: 6 Account and Access changes in 1.16.1
  type: change
related_changes:
- '[[Changes/Lovable/2026-07-24-report-abuse-and-submit-appeals-with-guided-forms|Report
  abuse and submit appeals with guided forms]]'
- '[[Changes/Open WebUI/2026-07-27-15-account-and-access-changes-in-v0-11-0|15 Account
  and Access changes in v0.11.0]]'
- '[[Changes/OpenCode/2026-07-27-desktop-fixed-provider-lists-not-refreshing-after-connecting-a-provider-or-finis|Desktop
  Fixed provider lists not refreshing after connecting a provider or finishing…]]'
source_release: '[[Releases/Dify/dify-2026-07-28-1-16-1-github-360820489-855a9365|dify-2026-07-28-1-16-1-github-360820489-855a9365]]'
source_type: github_releases
theme: account-access
title: 6 Account and Access changes in 1.16.1
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Account and Access changes in 1.16.1

**Dify** · 2026-07-28 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.16.1) · from [[Releases/Dify/dify-2026-07-28-1-16-1-github-360820489-855a9365|v1.16.1 - Bug Fixes and Security Enhancements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Communication between the Dify API and the agent backend now uses token-based authentication via `DIFY_AGENT_API_TOKEN` / `AGENT_BACKEND_API_TOKEN`, hardening the internal service boundary. (#39622)

> | `DIFY_AGENT_API_TOKEN` | `dify-agent-run-token-for-dev-only` | Shared bearer token for API → agent_backend authentication. **Change this in production.** |

> refactor(web): use generated OAuth query options by @lyzno1 in https://github.com/langgenius/dify/pull/39204

> test: move console OAuth coverage to unit tests by @asukaminato0721 in https://github.com/langgenius/dify/pull/38923

> feat(oauth): expose stable account id on provider account endpoint by @samzong in https://github.com/langgenius/dify/pull/39470

> test: use caplog in ext login tests by @EvanYao826 in https://github.com/langgenius/dify/pull/39542

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
- [[Changes/Dify/2026-07-28-10-interface-experience-changes-in-1-16-1|10 Interface Experience changes in 1.16.1]] · Interface Experience
- [[Changes/Dify/2026-07-28-4-developer-workflow-changes-in-1-16-1|4 Developer Workflow changes in 1.16.1]] · Developer Workflow
- [[Changes/Dify/2026-07-28-lightweight-recent-apps-endpoint-new-get-console-api-apps-recent-endpoint-reduce|Lightweight recent apps endpoint]] · Reliability and Performance
- [[Changes/Dify/2026-07-28-feat-web-locate-workflow-nodes-by-node-id-in-the-workflow-editor-by-ruanimal-in|feat(web): locate workflow nodes by node_id in the workflow editor]] · Editor Experience
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
## Nearby in Account and Access

- Earlier: 2026-07-27 · OpenCode · [[Changes/OpenCode/2026-07-27-desktop-fixed-provider-lists-not-refreshing-after-connecting-a-provider-or-finis|Desktop Fixed provider lists not refreshing after connecting a provider or finishing…]]
- Later: 2026-07-28 · Google Antigravity · [[Changes/Google Antigravity/2026-07-28-improved-authentication-error-messages-to-show-the-specific-failure-reason|Improved authentication error messages to show the specific failure reason]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-07-28-7e792c&body=Card%3A%20Changes%2FDify%2F2026-07-28-6-account-and-access-changes-in-1-16-1.md%0ACard%20ID%3A%20dify-2026-07-28-7e792c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.16.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->