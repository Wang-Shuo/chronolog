---
card_id: dify-2026-01-13-e0a73c
date: '2026-01-13'
description: 'Dify · 2026-01-13 · Reliability and Performance: 4 changes in v1.11.3
  — Our latest release, v1.11.3, brings to you a slew of bug fixes and features focused
  on…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1125
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 25a52bb3648334818dabbeec36516054d2835904a55256c5210e8c7683c19e90
product: dify
product_name: Dify
record:
  card_id: dify-2026-01-13-e0a73c
  comparison: ''
  date: '2026-01-13'
  description: 'Dify — v1.11.3: 4 Reliability and Performance changes'
  evidence:
  - quote: 'Our latest release, v1.11.3, brings to you a slew of bug fixes and features
      focused on performance, functionality, and user experience. Here''s a look at
      what''s changed:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  - quote: '**Redis and Cache**: Used pipelines to optimize Redis cache deletions,
      enhancing speed and reliability by @fatelei in #30159.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  - quote: '**Performance**: Released runtime state references under high load to
      prevent potential memory leaks by @SherlockShemol in #30236.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  - quote: '**Code & Query Optimization**: Addressed inefficiencies in SQL queries
      and data handling in workflows and the API, improving overall stability.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.11.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 4-reliability-and-performance-changes-in-1-11-3
  source_release: dify-2026-01-13-1-11-3-github-276298566-1fe35168
  source_type: github_releases
  theme: reliability-performance
  title: 4 Reliability and Performance changes in 1.11.3
  type: change
related_changes:
- '[[Changes/Ollama/2026-01-10-for-older-models-ollama-will-avoid-an-integer-underflow-on-low-vram-systems-duri|For
  older models, Ollama will avoid an integer underflow on low VRAM systems during…]]'
- "[[Changes/Open WebUI/2026-01-10-the-evaluations-page-now-loads-faster-by-eliminating-duplicate-api-calls-to-the|\U0001F4CA
  The Evaluations page now loads faster by eliminating duplicate API calls…]]"
- '[[Changes/OpenCode/2026-01-10-terminal-fix-instance-disposal-to-prevent-memory-leaks-and-dangling-references|Terminal
  Fix instance disposal to prevent memory leaks and dangling references]]'
source_release: '[[Releases/Dify/dify-2026-01-13-1-11-3-github-276298566-1fe35168|dify-2026-01-13-1-11-3-github-276298566-1fe35168]]'
source_type: github_releases
theme: reliability-performance
title: 4 Reliability and Performance changes in 1.11.3
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Reliability and Performance changes in 1.11.3

**Dify** · 2026-01-13 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.11.3) · from [[Releases/Dify/dify-2026-01-13-1-11-3-github-276298566-1fe35168|v1.11.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Our latest release, v1.11.3, brings to you a slew of bug fixes and features focused on performance, functionality, and user experience. Here's a look at what's changed:

> **Redis and Cache**: Used pipelines to optimize Redis cache deletions, enhancing speed and reliability by @fatelei in #30159.

> **Performance**: Released runtime state references under high load to prevent potential memory leaks by @SherlockShemol in #30236.

> **Code & Query Optimization**: Addressed inefficiencies in SQL queries and data handling in workflows and the API, improving overall stability.

Source: https://github.com/langgenius/dify/releases/tag/1.11.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-01-13-13-apps-and-integrations-changes-in-1-11-3|13 Apps and Integrations changes in 1.11.3]] · Apps and Integrations
- [[Changes/Dify/2026-01-13-4-account-and-access-changes-in-1-11-3|4 Account and Access changes in 1.11.3]] · Account and Access
- [[Changes/Dify/2026-01-13-chore-deps-bump-scheduler-from-0-26-0-to-0-27-0-in-web-by-dependabot-bot-in-http|chore(deps): bump scheduler from 0.26.0 to 0.27.0 in /web…]] · Automation and Scheduling
- [[Changes/Dify/2026-01-13-8-model-support-changes-in-1-11-3|8 Model Support changes in 1.11.3]] · Model Support
- [[Changes/Dify/2026-01-13-5-developer-workflow-changes-in-1-11-3|5 Developer Workflow changes in 1.11.3]] · Developer Workflow
- [[Changes/Dify/2026-01-13-3-agent-mode-changes-in-1-11-3|3 Agent Mode changes in 1.11.3]] · Agent Mode
- [[Changes/Dify/2026-01-13-2-accessibility-and-localization-changes-in-1-11-3|2 Accessibility and Localization changes in 1.11.3]] · Accessibility and Localization
- [[Changes/Dify/2026-01-13-5-safety-and-privacy-changes-in-1-11-3|5 Safety and Privacy changes in 1.11.3]] · Safety and Privacy
- [[Changes/Dify/2026-01-13-4-files-and-data-changes-in-1-11-3|4 Files and Data changes in 1.11.3]] · Files and Data
- [[Changes/Dify/2026-01-13-124-other-changes-in-1-11-3|124 other changes in 1.11.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-01-10 · OpenCode · [[Changes/OpenCode/2026-01-10-terminal-fix-instance-disposal-to-prevent-memory-leaks-and-dangling-references|Terminal Fix instance disposal to prevent memory leaks and dangling references]]
- Later: 2026-01-13 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-01-13-sessions-with-large-conversation-history-load-faster-on-startup|Sessions with large conversation history load faster on startup]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-01-13-e0a73c&body=Card%3A%20Changes%2FDify%2F2026-01-13-4-reliability-and-performance-changes-in-1-11-3.md%0ACard%20ID%3A%20dify-2026-01-13-e0a73c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.11.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->