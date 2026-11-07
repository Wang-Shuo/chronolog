---
card_id: codex-cli-2026-06-18-12d4ec
date: '2026-06-18'
description: 'Codex CLI · 2026-06-18 · Agent Mode: 5 changes in 0.141.0 — App-server
  clients can list immediate child threads, correlate external-agent imports with
  detailed…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1078
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 65e3bc02a878edd3f25433ccd30d4ba67ab265100035e0ae1ebf4243a8e45c0c
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-18-12d4ec
  comparison: ''
  date: '2026-06-18'
  description: 'Codex CLI — 0.141.0: 5 Agent Mode changes'
  evidence:
  - quote: 'App-server clients can list immediate child threads, correlate external-agent
      imports with detailed results, and read or redeem rate-limit reset credits.
      (#26662, #28008, #28143)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: 'Idle exec-server relays remain connected, and steered user input immediately
      interrupts `wait_agent`. (#28286, #28341)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28283 [codex] update multi-agent v2 prompts @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28341 core: let steer interrupt wait_agent @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  - quote: '#28008 [codex] Add external agent import result accounting @charlesgong-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.141.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-agent-mode-changes-in-rust-v0-141-0
  source_release: codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75
  source_type: github_releases
  theme: agent-mode
  title: 5 Agent Mode changes in rust-v0.141.0
  type: change
related_changes:
- '[[Changes/Cursor/2026-06-17-this-release-introduces-updates-to-cloud-agents-in-the-agents-window-of-the-curs|Cursor
  introduces updates to cloud agents in the Agents Window of the Cursor desktop app]]'
- '[[Changes/Cursor/2026-06-17-cloud-subagents-with-in-cloud-eb7958|Cloud subagents
  with /in-cloud]]'
- '[[Changes/Devin/2026-06-17-slack-agent-bang-command|Slack: !agent Bang Command]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75|codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75]]'
source_type: github_releases
theme: agent-mode
title: 5 Agent Mode changes in rust-v0.141.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Agent Mode changes in rust-v0.141.0

**Codex CLI** · 2026-06-18 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.141.0) · from [[Releases/Codex CLI/codex-cli-2026-06-18-rust-v0-141-0-github-341160952-94bdbd75|0.141.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server clients can list immediate child threads, correlate external-agent imports with detailed results, and read or redeem rate-limit reset credits. (#26662, #28008, #28143)

> Idle exec-server relays remain connected, and steered user input immediately interrupts `wait_agent`. (#28286, #28341)

> #28283 [codex] update multi-agent v2 prompts @jif-oai

> #28341 core: let steer interrupt wait_agent @jif-oai

> #28008 [codex] Add external agent import result accounting @charlesgong-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.141.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-18-7-safety-and-privacy-changes-in-rust-v0-141-0|7 Safety and Privacy changes in rust-v0.141.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-18-7-developer-workflow-changes-in-rust-v0-141-0|7 Developer Workflow changes in rust-v0.141.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-18-tls-connections-now-support-p-521-certificate-signatures-commonly-used-by-enterp|TLS connections now support P-521 certificate signatures commonly used by enterprise…]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-06-18-28257-support-staging-oauth-client-id-overrides-apanasenko-oai|♯28257 Support staging OAuth client ID overrides @apanasenko-oai]] · Account and Access
- [[Changes/Codex CLI/2026-06-18-2-context-window-changes-in-rust-v0-141-0|2 Context Window changes in rust-v0.141.0]] · Context Window
- [[Changes/Codex CLI/2026-06-18-17-apps-and-integrations-changes-in-rust-v0-141-0|17 Apps and Integrations changes in rust-v0.141.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-18-3-memory-and-personalization-changes-in-rust-v0-141-0|3 Memory and Personalization changes in rust-v0.141.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-06-18-28143-feat-app-server-expose-rate-limit-reset-credits-jayp-oai|♯28143 feat(app-server): expose rate-limit reset credits @jayp-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-06-18-42-other-changes-in-rust-v0-141-0|42 other changes in rust-v0.141.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-17 · Devin · [[Changes/Devin/2026-06-17-slack-agent-bang-command|Slack: !agent Bang Command]]
- Later: 2026-06-18 · Gemini CLI · [[Changes/Gemini CLI/2026-06-18-2-agent-mode-changes-in-v0-47-0|2 Agent Mode changes in v0.47.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-18-12d4ec&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-18-5-agent-mode-changes-in-rust-v0-141-0.md%0ACard%20ID%3A%20codex-cli-2026-06-18-12d4ec%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.141.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->