---
card_id: ollama-2026-03-17-b094b1
date: '2026-03-17'
description: 'Ollama · 2026-03-17 · Search and Browsing: 3 changes in v0.18.1 — Ollama
  now ships with web search and web fetch plugin for OpenClaw. This allows Ollama''s…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1090
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 885846bcbbcb4222ccf0c78ea333e46493ff865d839e2059c01aba350ca6009c
product: ollama
product_name: Ollama
record:
  card_id: ollama-2026-03-17-b094b1
  comparison: ''
  date: '2026-03-17'
  description: 'Ollama — v0.18.1: 3 Search and Browsing changes'
  evidence:
  - quote: Ollama now ships with web search and web fetch plugin for OpenClaw. This
      allows Ollama's models (local or cloud) to search the web for the latest content
      and news. This also allows OpenClaw with Ollama to be able to fetch the web
      and extract readable content for processing. This feature does not execute JavaScript.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.18.1
  - quote: When using local models with web search in OpenClaw, ensure you are signed
      into Ollama with `ollama signin`
    source_release: https://github.com/ollama/ollama/releases/tag/v0.18.1
  - quote: 'You can install web search directly into OpenClaw as a plugin if you already
      have OpenClaw configured and working:'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.18.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 3-search-and-browsing-changes-in-v0-18-1
  source_release: ollama-2026-03-17-v0-18-1-github-297703079-c31fed11
  source_type: github_releases
  theme: search-browsing
  title: 3 Search and Browsing changes in v0.18.1
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-03-11-14136-fix-core-use-dedicated-types-for-responsesapi-web-search-tool-config-owenl|♯14136
  fix(core): use dedicated types for responsesapi web search tool config @owenlin0]]'
- '[[Changes/GitHub Copilot CLI/2026-03-13-changelog-supports-last-n-since-version-and-summarize-to-browse-and-summarize-mu|/changelog
  supports last N, since version, and summarize to browse…]]'
- '[[Changes/Dify/2026-03-17-test-add-integration-tests-for-app-card-operations-list-browsing-and-create-app|test:
  add integration tests for app card operations, list browsing, and create app flows]]'
source_release: '[[Releases/Ollama/ollama-2026-03-17-v0-18-1-github-297703079-c31fed11|ollama-2026-03-17-v0-18-1-github-297703079-c31fed11]]'
source_type: github_releases
theme: search-browsing
title: 3 Search and Browsing changes in v0.18.1
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Search and Browsing changes in v0.18.1

**Ollama** · 2026-03-17 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.18.1) · from [[Releases/Ollama/ollama-2026-03-17-v0-18-1-github-297703079-c31fed11|v0.18.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Ollama now ships with web search and web fetch plugin for OpenClaw. This allows Ollama's models (local or cloud) to search the web for the latest content and news. This also allows OpenClaw with Ollama to be able to fetch the web and extract readable content for processing. This feature does not execute JavaScript.

> When using local models with web search in OpenClaw, ensure you are signed into Ollama with `ollama signin`

> You can install web search directly into OpenClaw as a plugin if you already have OpenClaw configured and working:

Source: https://github.com/ollama/ollama/releases/tag/v0.18.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2026-03-17-docker-containers-spin-up-an-integration-as-a-pipeline-step-to-run-evals-test-pr|Docker/containers: spin up an integration as a pipeline step to run evals, test…]] · Apps and Integrations
- [[Changes/Ollama/2026-03-17-ci-cd-generate-code-reviews-security-checks-and-other-tasks-within-your-ci|CI/CD: Generate code reviews, security checks, and other tasks within your CI]] · Safety and Privacy
- [[Changes/Ollama/2026-03-17-4-model-support-changes-in-v0-18-1|4 Model Support changes in v0.18.1]] · Model Support
- [[Changes/Ollama/2026-03-17-scripts-automation-kick-off-automated-tasks-with-ollama-and-claude-code|Scripts/automation: Kick off automated tasks with Ollama and claude code]] · Automation and Scheduling
- [[Changes/Ollama/2026-03-17-you-can-ask-your-openclaw-to-run-tasks-using-claude-with-subagents|You can ask your OpenClaw to run tasks using claude with subagents]] · Agent Mode
- [[Changes/Ollama/2026-03-17-4-other-changes-in-v0-18-1|4 other changes in v0.18.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2026-03-17 · Dify · [[Changes/Dify/2026-03-17-test-add-integration-tests-for-app-card-operations-list-browsing-and-create-app|test: add integration tests for app card operations, list browsing, and create app flows]]
- Later: 2026-03-19 · ChatGPT · [[Changes/ChatGPT/2026-03-19-the-legacy-deep-research-mode-will-be-removed-on-thursday-march-26-2026-this-cha|Legacy deep research mode deprecation notice]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2026-03-17-b094b1&body=Card%3A%20Changes%2FOllama%2F2026-03-17-3-search-and-browsing-changes-in-v0-18-1.md%0ACard%20ID%3A%20ollama-2026-03-17-b094b1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.18.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->