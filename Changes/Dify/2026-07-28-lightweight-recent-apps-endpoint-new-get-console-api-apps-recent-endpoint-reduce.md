---
card_id: dify-2026-07-28-718758
date: '2026-07-28'
description: 'Dify · 2026-07-28 · Reliability and Performance: **Lightweight recent
  apps endpoint** — New `GET /console/api/apps/recent` endpoint reduces the home page…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2808
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: feaa473ac460040efc131715112727bc5237b91b7053ad105c6bb89ef9c4b531
product: dify
product_name: Dify
record:
  ai_generated: true
  card_id: dify-2026-07-28-718758
  comparison: ''
  confidence: low
  date: '2026-07-28'
  description: 'Dify — v1.16.1 - Bug Fixes and Security Enhancements: **Lightweight
    recent apps endpoint** — New `GET /console/api/apps/recent` endpoint reduces the
    home page "Continue Work" section latency by ~69% (3.2× faster), cutting SQL queries
    from 19+ to 1 projection SELECT and response size by ~50% (#39625)'
  evidence:
  - quote: '**Lightweight recent apps endpoint** — New `GET /console/api/apps/recent`
      endpoint reduces the home page "Continue Work" section latency by ~69% (3.2×
      faster), cutting SQL queries from 19+ to 1 projection SELECT and response size
      by ~50% (#39625)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.1
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: dify
  product_name: Dify
  slug: lightweight-recent-apps-endpoint-new-get-console-api-apps-recent-endpoint-reduce
  source_release: dify-2026-07-28-1-16-1-github-360820489-855a9365
  source_type: github_releases
  theme: reliability-performance
  title: '**Lightweight recent apps endpoint**'
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-07-22-improve-tui-performance-and-resume-speed-for-long-running-sessions|Improve
  TUI performance and resume speed for long-running sessions]]'
- '[[Changes/Ollama/2026-07-23-expanded-gpu-support-with-cuda-on-windows-arm64-b200-support-through-cuda-12-and|Expanded
  GPU support with CUDA on Windows ARM64, B200 support through CUDA 12…]]'
- '[[Changes/Open WebUI/2026-07-27-12-reliability-and-performance-changes-in-v0-11-0|12
  Reliability and Performance changes in v0.11.0]]'
source_release: '[[Releases/Dify/dify-2026-07-28-1-16-1-github-360820489-855a9365|dify-2026-07-28-1-16-1-github-360820489-855a9365]]'
source_type: github_releases
theme: reliability-performance
title: Lightweight recent apps endpoint
type: change
---

<!-- chronolog:begin region="header" -->
# **Lightweight recent apps endpoint**

**Dify** · 2026-07-28 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/langgenius/dify/releases/tag/1.16.1) · from [[Releases/Dify/dify-2026-07-28-1-16-1-github-360820489-855a9365|v1.16.1 - Bug Fixes and Security Enhancements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Lightweight recent apps endpoint** — New `GET /console/api/apps/recent` endpoint reduces the home page "Continue Work" section latency by ~69% (3.2× faster), cutting SQL queries from 19+ to 1 projection SELECT and response size by ~50% (#39625)
>
> Source: https://github.com/langgenius/dify/releases/tag/1.16.1
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
## Nearby in Reliability and Performance

- Earlier: 2026-07-27 · Open WebUI · [[Changes/Open WebUI/2026-07-27-12-reliability-and-performance-changes-in-v0-11-0|12 Reliability and Performance changes in v0.11.0]]
- Later: 2026-07-28 · Google Antigravity · [[Changes/Google Antigravity/2026-07-28-3-reliability-and-performance-changes-in-hub-v2-4-3-preview-tabs-mcp|3 Reliability and Performance changes in HUB v2.4.3 — Preview tabs, MCP…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-07-28-718758&body=Card%3A%20Changes%2FDify%2F2026-07-28-lightweight-recent-apps-endpoint-new-get-console-api-apps-recent-endpoint-reduce.md%0ACard%20ID%3A%20dify-2026-07-28-718758%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.16.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->