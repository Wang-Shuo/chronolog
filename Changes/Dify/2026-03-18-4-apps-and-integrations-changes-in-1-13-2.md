---
card_id: dify-2026-03-18-192bc5
date: '2026-03-18'
description: 'Dify · 2026-03-18 · Apps and Integrations: 4 changes in v1.13.2 — a
  severe regression in prompt message transformation that caused multiple LLM-plugin…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2651
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 33283d68451c04109f617fb99af98d027fa8748e71857fad42c9959400d42333
product: dify
product_name: Dify
record:
  card_id: dify-2026-03-18-192bc5
  comparison: ''
  date: '2026-03-18'
  description: 'Dify — v1.13.2: 4 Apps and Integrations changes'
  evidence:
  - quote: a severe regression in prompt message transformation that caused multiple
      LLM-plugin invocation failures across
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.2
  - quote: '> [error] failed to initialize database, got error failed to connect to
      `host=db_postgres user=postgres database=dify_plugin`: hostname resolving error
      (lookup db_postgres on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.2
  - quote: '> 2025/11/26 11:37:57 init.go:99: [PANIC]failed to init dify plugin db:
      failed to connect to `host=db_postgres user=postgres database=postgres`: hostname
      resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.2
  - quote: '> panic: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres
      user=postgres database=postgres`: hostname resolving error (lookup db_postgres
      on 127.0.0.11:53: server misbehaving)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.13.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 4-apps-and-integrations-changes-in-1-13-2
  source_release: dify-2026-03-18-1-13-2-github-298465611-74009894
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in 1.13.2
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-03-17-add-experimental-sdk-session-apis-to-list-and-manage-skills-mcp-servers-and-plug|Add
  experimental SDK session APIs to list and manage skills, MCP servers…]]'
- '[[Changes/Ollama/2026-03-17-docker-containers-spin-up-an-integration-as-a-pipeline-step-to-run-evals-test-pr|Docker/containers:
  spin up an integration as a pipeline step to run evals, test…]]'
- '[[Changes/Claude Code/2026-03-18-2-apps-and-integrations-changes-in-v2-1-79|2 Apps
  and Integrations changes in v2.1.79]]'
source_release: '[[Releases/Dify/dify-2026-03-18-1-13-2-github-298465611-74009894|dify-2026-03-18-1-13-2-github-298465611-74009894]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in 1.13.2
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in 1.13.2

**Dify** · 2026-03-18 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.13.2) · from [[Releases/Dify/dify-2026-03-18-1-13-2-github-298465611-74009894|v1.13.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> a severe regression in prompt message transformation that caused multiple LLM-plugin invocation failures across

> > [error] failed to initialize database, got error failed to connect to `host=db_postgres user=postgres database=dify_plugin`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> > 2025/11/26 11:37:57 init.go:99: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

> > panic: [PANIC]failed to init dify plugin db: failed to connect to `host=db_postgres user=postgres database=postgres`: hostname resolving error (lookup db_postgres on 127.0.0.11:53: server misbehaving)

Source: https://github.com/langgenius/dify/releases/tag/1.13.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-03-18-this-patch-release-fixes-several-critical-regressions-and-stability-issues-intro|This patch release fixes several critical regressions and stability issues…]] · Reliability and Performance
- [[Changes/Dify/2026-03-18-please-use-the-following-command-instead-for-details-please-read-this-https-gith| Please use the following command instead]] · Developer Workflow
- [[Changes/Dify/2026-03-18-llm-related-nodes-including-llm-and-question-classifier|LLM-related nodes, including LLM and Question Classifier]] · Model Support
- [[Changes/Dify/2026-03-18-23-other-changes-in-1-13-2|23 other changes in 1.13.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-18 · Claude Code · [[Changes/Claude Code/2026-03-18-2-apps-and-integrations-changes-in-v2-1-79|2 Apps and Integrations changes in v2.1.79]]
- Later: 2026-03-18 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-18-3-apps-and-integrations-changes-in-v1-0-8|3 Apps and Integrations changes in v1.0.8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-03-18-192bc5&body=Card%3A%20Changes%2FDify%2F2026-03-18-4-apps-and-integrations-changes-in-1-13-2.md%0ACard%20ID%3A%20dify-2026-03-18-192bc5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.13.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->