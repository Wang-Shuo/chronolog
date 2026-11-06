---
card_id: ollama-2026-03-17-c92791
date: '2026-03-17'
description: 'Ollama · 2026-03-17 · Model Support: 4 changes in v0.18.1 — `--model`
  must be specified to run in headless mode'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1163
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2c329bf92aedd60b93fc12722be7ff7d8cee75b9b9eb2cf036936f0c66d3322f
product: ollama
product_name: Ollama
record:
  card_id: ollama-2026-03-17-c92791
  comparison: ''
  date: '2026-03-17'
  description: 'Ollama — v0.18.1: 4 Model Support changes'
  evidence:
  - quote: '`--model` must be specified to run in headless mode'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.18.1
  - quote: '`--yes` flag will auto-pull the model and skip any selectors'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.18.1
  - quote: 'Try with: `ollama launch claude --model kimi-k2.5:cloud --yes -- -p "how
      does this repository work?"`'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.18.1
  - quote: '`ollama launch openclaw` will now use the official Ollama auth and model
      provider for OpenClaw'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.18.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 4-model-support-changes-in-v0-18-1
  source_release: ollama-2026-03-17-v0-18-1-github-297703079-c31fed11
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in v0.18.1
  type: change
related_changes:
- '[[Changes/Dify/2026-03-17-18-model-support-changes-in-1-13-1|18 Model Support changes
  in 1.13.1]]'
- '[[Changes/Gemini CLI/2026-03-17-5-model-support-changes-in-v0-34-0|5 Model Support
  changes in v0.34.0]]'
- '[[Changes/GitHub Copilot CLI/2026-03-17-2-model-support-changes-in-v1-0-7|2 Model
  Support changes in v1.0.7]]'
source_release: '[[Releases/Ollama/ollama-2026-03-17-v0-18-1-github-297703079-c31fed11|ollama-2026-03-17-v0-18-1-github-297703079-c31fed11]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in v0.18.1
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v0.18.1

**Ollama** · 2026-03-17 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.18.1) · from [[Releases/Ollama/ollama-2026-03-17-v0-18-1-github-297703079-c31fed11|v0.18.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `--model` must be specified to run in headless mode

> `--yes` flag will auto-pull the model and skip any selectors

> Try with: `ollama launch claude --model kimi-k2.5:cloud --yes -- -p "how does this repository work?"`

> `ollama launch openclaw` will now use the official Ollama auth and model provider for OpenClaw

Source: https://github.com/ollama/ollama/releases/tag/v0.18.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2026-03-17-docker-containers-spin-up-an-integration-as-a-pipeline-step-to-run-evals-test-pr|Docker/containers: spin up an integration as a pipeline step to run evals, test…]] · Apps and Integrations
- [[Changes/Ollama/2026-03-17-ci-cd-generate-code-reviews-security-checks-and-other-tasks-within-your-ci|CI/CD: Generate code reviews, security checks, and other tasks within your CI]] · Safety and Privacy
- [[Changes/Ollama/2026-03-17-3-search-and-browsing-changes-in-v0-18-1|3 Search and Browsing changes in v0.18.1]] · Search and Browsing
- [[Changes/Ollama/2026-03-17-scripts-automation-kick-off-automated-tasks-with-ollama-and-claude-code|Scripts/automation: Kick off automated tasks with Ollama and claude code]] · Automation and Scheduling
- [[Changes/Ollama/2026-03-17-you-can-ask-your-openclaw-to-run-tasks-using-claude-with-subagents|You can ask your OpenClaw to run tasks using claude with subagents]] · Agent Mode
- [[Changes/Ollama/2026-03-17-4-other-changes-in-v0-18-1|4 other changes in v0.18.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-03-17 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-17-2-model-support-changes-in-v1-0-7|2 Model Support changes in v1.0.7]]
- Later: 2026-03-18 · ChatGPT · [[Changes/ChatGPT/2026-03-18-we-re-rolling-out-gpt-5-4-mini-in-chatgpt-gpt-5-4-mini-is-available-to-free-and|GPT-5.4 mini in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2026-03-17-c92791&body=Card%3A%20Changes%2FOllama%2F2026-03-17-4-model-support-changes-in-v0-18-1.md%0ACard%20ID%3A%20ollama-2026-03-17-c92791%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.18.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->