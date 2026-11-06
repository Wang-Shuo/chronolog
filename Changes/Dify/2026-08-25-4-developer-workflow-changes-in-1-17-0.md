---
card_id: dify-2026-08-25-8167e0
date: '2026-08-25'
description: 'Dify · 2026-08-25 · Developer Workflow: 4 changes in v1.17.0 — No manual
  backfill command is required for these migrations. Run `flask db upgrade` as part
  of…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1256
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1e2f4108d9af656811419197c23178a869d931e144f096bc81facae2c68b486d
product: dify
product_name: Dify
record:
  card_id: dify-2026-08-25-8167e0
  comparison: ''
  date: '2026-08-25'
  description: 'Dify — v1.17.0: 4 Developer Workflow changes'
  evidence:
  - quote: No manual backfill command is required for these migrations. Run `flask
      db upgrade` as part of the upgrade.
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: '> Back up the database before applying the migration. The command runs
      in dry-run mode by default; review the output before rerunning it with `--apply`.
      The migration is idempotent and can be safely rerun.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'chore(deps): bump wandb to 0.28.2 (go-git, grpc, x/text, Go stdlib CVEs)
      by @GareArc in https://github.com/langgenius/dify/pull/40753'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  - quote: 'test: migrate app service accounts and commit failures to real ORM by
      @asukaminato0721 in https://github.com/langgenius/dify/pull/40655'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 4-developer-workflow-changes-in-1-17-0
  source_release: dify-2026-08-25-1-17-0-github-376348099-66c16161
  source_type: github_releases
  theme: developer-workflow
  title: 4 Developer Workflow changes in 1.17.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-08-21-deepseek-harness-launcher-now-falls-back-to-npx-when-the-global-npm-install-fail|DeepSeek
  Harness launcher now falls back to npx when the global npm install fails…]]'
- '[[Changes/ChatGPT/2026-08-25-plus-and-pro-users-can-ask-work-on-web-ios-and-android-to-respond-when-a-new-gma|Create
  webhook-triggered tasks]]'
- '[[Changes/Claude Code/2026-08-25-2-developer-workflow-changes-in-v2-1-246|2 Developer
  Workflow changes in v2.1.246]]'
source_release: '[[Releases/Dify/dify-2026-08-25-1-17-0-github-376348099-66c16161|dify-2026-08-25-1-17-0-github-376348099-66c16161]]'
source_type: github_releases
theme: developer-workflow
title: 4 Developer Workflow changes in 1.17.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Developer Workflow changes in 1.17.0

**Dify** · 2026-08-25 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.0) · from [[Releases/Dify/dify-2026-08-25-1-17-0-github-376348099-66c16161|v1.17.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> No manual backfill command is required for these migrations. Run `flask db upgrade` as part of the upgrade.

> > Back up the database before applying the migration. The command runs in dry-run mode by default; review the output before rerunning it with `--apply`. The migration is idempotent and can be safely rerun.

> chore(deps): bump wandb to 0.28.2 (go-git, grpc, x/text, Go stdlib CVEs) by @GareArc in https://github.com/langgenius/dify/pull/40753

> test: migrate app service accounts and commit failures to real ORM by @asukaminato0721 in https://github.com/langgenius/dify/pull/40655

Source: https://github.com/langgenius/dify/releases/tag/1.17.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-08-25-2-enterprise-and-administration-changes-in-1-17-0|2 Enterprise and Administration changes in 1.17.0]] · Enterprise and Administration
- [[Changes/Dify/2026-08-25-audio-asr-now-accepts-audio-x-m4a-and-audio-mime-types-are-validated-more-accura|Audio ASR now accepts audio/x-m4a, and audio MIME types are validated more…]] · Voice and Audio
- [[Changes/Dify/2026-08-25-5-collaboration-changes-in-1-17-0|5 Collaboration changes in 1.17.0]] · Collaboration
- [[Changes/Dify/2026-08-25-16-safety-and-privacy-changes-in-1-17-0|16 Safety and Privacy changes in 1.17.0]] · Safety and Privacy
- [[Changes/Dify/2026-08-25-feat-workflow-support-human-input-in-loop-and-iteration-by-laipz8200-in-https-gi|feat(workflow): support human input in loop and iteration]] · Automation and Scheduling
- [[Changes/Dify/2026-08-25-4-editor-experience-changes-in-1-17-0|4 Editor Experience changes in 1.17.0]] · Editor Experience
- [[Changes/Dify/2026-08-25-3-multimodal-input-changes-in-1-17-0|3 Multimodal Input changes in 1.17.0]] · Multimodal Input
- [[Changes/Dify/2026-08-25-53-agent-mode-changes-in-1-17-0|53 Agent Mode changes in 1.17.0]] · Agent Mode
- [[Changes/Dify/2026-08-25-93-model-support-changes-in-1-17-0|93 Model Support changes in 1.17.0]] · Model Support
- [[Changes/Dify/2026-08-25-13-account-and-access-changes-in-1-17-0|13 Account and Access changes in 1.17.0]] · Account and Access
- [[Changes/Dify/2026-08-25-28-apps-and-integrations-changes-in-1-17-0|28 Apps and Integrations changes in 1.17.0]] · Apps and Integrations
- [[Changes/Dify/2026-08-25-7-pricing-model-changes-in-1-17-0|7 Pricing Model changes in 1.17.0]] · Pricing Model
- [[Changes/Dify/2026-08-25-5-files-and-data-changes-in-1-17-0|5 Files and Data changes in 1.17.0]] · Files and Data
- [[Changes/Dify/2026-08-25-workflow-runtime-stability|Workflow & Runtime Stability]] · Reliability and Performance
- [[Changes/Dify/2026-08-25-8-context-window-changes-in-1-17-0|8 Context Window changes in 1.17.0]] · Context Window
- [[Changes/Dify/2026-08-25-9-interface-experience-changes-in-1-17-0|9 Interface Experience changes in 1.17.0]] · Interface Experience
- [[Changes/Dify/2026-08-25-3-accessibility-and-localization-changes-in-1-17-0|3 Accessibility and Localization changes in 1.17.0]] · Accessibility and Localization
- [[Changes/Dify/2026-08-25-351-other-changes-in-1-17-0|351 other changes in 1.17.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-08-25 · Claude Code · [[Changes/Claude Code/2026-08-25-2-developer-workflow-changes-in-v2-1-246|2 Developer Workflow changes in v2.1.246]]
- Later: 2026-08-25 · Gemini CLI · [[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-24935-force-terminal-buffer-rerender-after-exiting-external|SSR Agent Issue Fix (24935)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-08-25-8167e0&body=Card%3A%20Changes%2FDify%2F2026-08-25-4-developer-workflow-changes-in-1-17-0.md%0ACard%20ID%3A%20dify-2026-08-25-8167e0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->