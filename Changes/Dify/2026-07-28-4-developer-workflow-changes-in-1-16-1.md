---
card_id: dify-2026-07-28-5c0e8b
date: '2026-07-28'
description: 'Dify · 2026-07-28 · Developer Workflow: 4 changes in v1.16.1 - Bug Fixes
  and Security Enhancements — Used `flush()` instead of `commit()` in dataset service
  to…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1228
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dcccd4325fbb505ecde27644b0b0fd622286a3a22a97efa94667b0330bd3fe34
product: dify
product_name: Dify
record:
  card_id: dify-2026-07-28-5c0e8b
  comparison: ''
  date: '2026-07-28'
  description: 'Dify — v1.16.1 - Bug Fixes and Security Enhancements: 4 Developer
    Workflow changes'
  evidence:
  - quote: Used `flush()` instead of `commit()` in dataset service to preserve caller
      transaction boundaries (#39223)
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: '> Back up the database before applying the migration. The command runs
      in dry-run mode by default; review the output before rerunning it with `--apply`.
      The migration is idempotent and can be safely rerun.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'feat(web): add step-by-step tour shell by @Jingyi-Dify in https://github.com/langgenius/dify/pull/38785'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  - quote: 'chore: add web shell code owners by @lyzno1 in https://github.com/langgenius/dify/pull/39526'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 4-developer-workflow-changes-in-1-16-1
  source_release: dify-2026-07-28-1-16-1-github-360820489-855a9365
  source_type: github_releases
  theme: developer-workflow
  title: 4 Developer Workflow changes in 1.16.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-22-changed-code-review-to-run-as-a-background-subagent-so-review-work-no-longer-fil|Changed
  /code-review to run as a background subagent, so review work no longer…]]'
- '[[Changes/GitHub Copilot CLI/2026-07-23-2-developer-workflow-changes-in-v1-0-74|2
  Developer Workflow changes in v1.0.74]]'
- '[[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer
  Workflow changes in v0.11.0]]'
source_release: '[[Releases/Dify/dify-2026-07-28-1-16-1-github-360820489-855a9365|dify-2026-07-28-1-16-1-github-360820489-855a9365]]'
source_type: github_releases
theme: developer-workflow
title: 4 Developer Workflow changes in 1.16.1
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Developer Workflow changes in 1.16.1

**Dify** · 2026-07-28 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.16.1) · from [[Releases/Dify/dify-2026-07-28-1-16-1-github-360820489-855a9365|v1.16.1 - Bug Fixes and Security Enhancements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Used `flush()` instead of `commit()` in dataset service to preserve caller transaction boundaries (#39223)

> > Back up the database before applying the migration. The command runs in dry-run mode by default; review the output before rerunning it with `--apply`. The migration is idempotent and can be safely rerun.

> feat(web): add step-by-step tour shell by @Jingyi-Dify in https://github.com/langgenius/dify/pull/38785

> chore: add web shell code owners by @lyzno1 in https://github.com/langgenius/dify/pull/39526

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
## Nearby in Developer Workflow

- Earlier: 2026-07-27 · Open WebUI · [[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer Workflow changes in v0.11.0]]
- Later: 2026-07-28 · Gemini CLI · [[Changes/Gemini CLI/2026-07-28-feat-evals-add-eval-coverage-report-command-by-ved015-in-https-github-com-google|feat(evals): add eval coverage report command]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-07-28-5c0e8b&body=Card%3A%20Changes%2FDify%2F2026-07-28-4-developer-workflow-changes-in-1-16-1.md%0ACard%20ID%3A%20dify-2026-07-28-5c0e8b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.16.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->