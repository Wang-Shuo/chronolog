---
card_id: dify-2026-03-17-f79294
date: '2026-03-17'
description: 'Dify · 2026-03-17 · Developer Workflow: 8 changes in v1.13.1 — Added
  a new `export-app-messages` CLI command to export application messages and related…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2744
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a4af178589a2746fede06443aae170f93611150ef971b29c05a60f757a75c2ff
product: dify
product_name: Dify
record:
  card_id: dify-2026-03-17-f79294
  comparison: ''
  date: '2026-03-17'
  description: 'Dify — v1.13.1: 8 Developer Workflow changes'
  evidence:
  - quote: Added a new `export-app-messages` CLI command to export application messages
      and related feedback to `JSONL.GZ` (local or cloud storage).
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: Added telemetry metrics for retention cleanup tasks (messages/workflow
      runs), plus flush behavior for short-lived command jobs.
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: '> Please use the following command instead. For details, please read this
      https://github.com/langgenius/dify/issues/28706'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'chore(deps-dev): bump import-linter from 2.7 to 2.10 in /api by @dependabot[bot]
      in https://github.com/langgenius/dify/pull/32403'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'feat: add backend-code-review skill by @hj24 in https://github.com/langgenius/dify/pull/32719'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'feat: support relative mode for message clean command by @hj24 in https://github.com/langgenius/dify/pull/32834'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'docs: use docker compose command consistently in README by @haosenwang1018
      in https://github.com/langgenius/dify/pull/33077'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  - quote: 'chore: skip pre commit check for merge by @hyoban in https://github.com/langgenius/dify/pull/33287'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 8-developer-workflow-changes-in-1-13-1
  source_release: dify-2026-03-17-1-13-1-github-297876307-84187197
  source_type: github_releases
  theme: developer-workflow
  title: 8 Developer Workflow changes in 1.13.1
  type: change
related_changes:
- '[[Changes/v0/2026-03-16-added-v0-label-to-pull-requests-created-by-v0|Added "v0"
  label to pull requests created by v0]]'
- '[[Changes/Claude Code/2026-03-17-background-bash-tasks-are-now-killed-if-output-exceeds-5gb-preventing-runaway-pr|Background
  bash tasks are now killed if output exceeds 5GB, preventing runaway…]]'
- '[[Changes/Claude Code/2026-03-17-terminal-notifications-iterm2-kitty-ghostty-popups-progress-bar-now-reach-the-ou|Terminal
  notifications (iTerm2/Kitty/Ghostty popups, progress bar) now reach…]]'
source_release: '[[Releases/Dify/dify-2026-03-17-1-13-1-github-297876307-84187197|dify-2026-03-17-1-13-1-github-297876307-84187197]]'
source_type: github_releases
theme: developer-workflow
title: 8 Developer Workflow changes in 1.13.1
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Developer Workflow changes in 1.13.1

**Dify** · 2026-03-17 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.13.1) · from [[Releases/Dify/dify-2026-03-17-1-13-1-github-297876307-84187197|v1.13.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a new `export-app-messages` CLI command to export application messages and related feedback to `JSONL.GZ` (local or cloud storage).

> Added telemetry metrics for retention cleanup tasks (messages/workflow runs), plus flush behavior for short-lived command jobs.

> > Please use the following command instead. For details, please read this https://github.com/langgenius/dify/issues/28706

> chore(deps-dev): bump import-linter from 2.7 to 2.10 in /api by @dependabot[bot] in https://github.com/langgenius/dify/pull/32403

> feat: add backend-code-review skill by @hj24 in https://github.com/langgenius/dify/pull/32719

> feat: support relative mode for message clean command by @hj24 in https://github.com/langgenius/dify/pull/32834

> docs: use docker compose command consistently in README by @haosenwang1018 in https://github.com/langgenius/dify/pull/33077

> chore: skip pre commit check for merge by @hyoban in https://github.com/langgenius/dify/pull/33287

Source: https://github.com/langgenius/dify/releases/tag/1.13.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-03-17-test-add-comprehensive-unit-and-integration-tests-for-billing-components-by-codi|test: add comprehensive unit and integration tests for billing components]] · Pricing Model
- [[Changes/Dify/2026-03-17-refactor-web-split-share-text-generation-and-add-high-coverage-tests-by-codingon|refactor(web): split share text-generation and add high-coverage tests]] · Collaboration
- [[Changes/Dify/2026-03-17-16-files-and-data-changes-in-1-13-1|16 Files and Data changes in 1.13.1]] · Files and Data
- [[Changes/Dify/2026-03-17-3-safety-and-privacy-changes-in-1-13-1|3 Safety and Privacy changes in 1.13.1]] · Safety and Privacy
- [[Changes/Dify/2026-03-17-5-agent-mode-changes-in-1-13-1|5 Agent Mode changes in 1.13.1]] · Agent Mode
- [[Changes/Dify/2026-03-17-2-reliability-and-performance-changes-in-1-13-1|2 Reliability and Performance changes in 1.13.1]] · Reliability and Performance
- [[Changes/Dify/2026-03-17-ci-add-weekly-schedule-for-pip-and-uv-ecosystems-by-asukaminato0721-in-https-git|ci: Add weekly schedule for pip and uv ecosystems]] · Automation and Scheduling
- [[Changes/Dify/2026-03-17-9-context-window-changes-in-1-13-1|9 Context Window changes in 1.13.1]] · Context Window
- [[Changes/Dify/2026-03-17-18-model-support-changes-in-1-13-1|18 Model Support changes in 1.13.1]] · Model Support
- [[Changes/Dify/2026-03-17-27-apps-and-integrations-changes-in-1-13-1|27 Apps and Integrations changes in 1.13.1]] · Apps and Integrations
- [[Changes/Dify/2026-03-17-7-interface-experience-changes-in-1-13-1|7 Interface Experience changes in 1.13.1]] · Interface Experience
- [[Changes/Dify/2026-03-17-8-editor-experience-changes-in-1-13-1|8 Editor Experience changes in 1.13.1]] · Editor Experience
- [[Changes/Dify/2026-03-17-4-memory-and-personalization-changes-in-1-13-1|4 Memory and Personalization changes in 1.13.1]] · Memory and Personalization
- [[Changes/Dify/2026-03-17-test-add-integration-tests-for-app-card-operations-list-browsing-and-create-app|test: add integration tests for app card operations, list browsing, and create app flows]] · Search and Browsing
- [[Changes/Dify/2026-03-17-2-enterprise-and-administration-changes-in-1-13-1|2 Enterprise and Administration changes in 1.13.1]] · Enterprise and Administration
- [[Changes/Dify/2026-03-17-295-other-changes-in-1-13-1|295 other changes in 1.13.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-17 · Claude Code · [[Changes/Claude Code/2026-03-17-terminal-notifications-iterm2-kitty-ghostty-popups-progress-bar-now-reach-the-ou|Terminal notifications (iTerm2/Kitty/Ghostty popups, progress bar) now reach…]]
- Later: 2026-03-17 · Gemini CLI · [[Changes/Gemini CLI/2026-03-17-9-developer-workflow-changes-in-v0-34-0|9 Developer Workflow changes in v0.34.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-03-17-f79294&body=Card%3A%20Changes%2FDify%2F2026-03-17-8-developer-workflow-changes-in-1-13-1.md%0ACard%20ID%3A%20dify-2026-03-17-f79294%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.13.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->