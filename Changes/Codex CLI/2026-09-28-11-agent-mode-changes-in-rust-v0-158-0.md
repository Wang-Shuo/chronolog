---
card_id: codex-cli-2026-09-28-db454f
date: '2026-09-28'
description: 'Codex CLI · 2026-09-28 · Agent Mode: 11 changes in 0.158.0 — #47520
  Route session agent operations through `AgentControl` @jif-oai'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1180
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 53ec6d3db68f1022d73dc93a7d462c3a31f75d754396fb0cbaef7285fd755391
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-28-db454f
  comparison: ''
  date: '2026-09-28'
  description: 'Codex CLI — 0.158.0: 11 Agent Mode changes'
  evidence:
  - quote: '#47520 Route session agent operations through `AgentControl` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47540 Add an option to disable multi-agent v2 direct messaging @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47633 Route message board agent resolution through the selected controller
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47649 Add opt-in OTLP logging for final agent responses @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47670 Support model-specific descriptions for agent message board tools
      @eknight-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47691 Materialize rollout persistence for pending inter-agent messages
      @dermanyang-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47808 Allow hosts to provide agent controllers through ThreadManager
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47824 Allow four concurrent threads in the multi-agent resume test @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47964 Preserve the client-agent header for Amazon Bedrock Runtime @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48077 Add Serde support to agent message board request types @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48100 Add an HTTP client for remote agent message boards @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-agent-mode-changes-in-rust-v0-158-0
  source_release: codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7
  source_type: github_releases
  theme: agent-mode
  title: 11 Agent Mode changes in rust-v0.158.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-25-13-agent-mode-changes-in-rust-v0-157-0|13 Agent
  Mode changes in rust-v0.157.0]]'
- '[[Changes/OpenHands/2026-09-25-docs-correct-outdated-cloud-proxy-rule-2-in-agents-md-by-juanmichelini-in-https|docs:
  correct outdated cloud-proxy Rule 2 in AGENTS.md]]'
- '[[Changes/Claude Code/2026-09-28-added-a-yes-but-ask-again-next-time-answer-to-auto-mode-s-prompt-before-a-read-o|Added
  a "Yes, but ask again next time" answer to auto mode''s prompt before a read…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7]]'
source_type: github_releases
theme: agent-mode
title: 11 Agent Mode changes in rust-v0.158.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Agent Mode changes in rust-v0.158.0

**Codex CLI** · 2026-09-28 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.158.0) · from [[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|0.158.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #47520 Route session agent operations through `AgentControl` @jif-oai

> #47540 Add an option to disable multi-agent v2 direct messaging @jif-oai

> #47633 Route message board agent resolution through the selected controller @jif-oai

> #47649 Add opt-in OTLP logging for final agent responses @xli-oai

> #47670 Support model-specific descriptions for agent message board tools @eknight-oai

> #47691 Materialize rollout persistence for pending inter-agent messages @dermanyang-oai

> #47808 Allow hosts to provide agent controllers through ThreadManager @jif-oai

> #47824 Allow four concurrent threads in the multi-agent resume test @felixxia-oai

> #47964 Preserve the client-agent header for Amazon Bedrock Runtime @celia-oai

> #48077 Add Serde support to agent message board request types @jif-oai

> #48100 Add an HTTP client for remote agent message boards @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.158.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-28-9-safety-and-privacy-changes-in-rust-v0-158-0|9 Safety and Privacy changes in rust-v0.158.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-28-47975-prevent-stale-voice-answers-from-reappearing-during-speech-recovery-etraut|♯47975 Prevent stale voice answers from reappearing during speech recovery @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-28-13-apps-and-integrations-changes-in-rust-v0-158-0|13 Apps and Integrations changes in rust-v0.158.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-28-8-account-and-access-changes-in-rust-v0-158-0|8 Account and Access changes in rust-v0.158.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-28-3-mobile-and-desktop-changes-in-rust-v0-158-0|3 Mobile and Desktop changes in rust-v0.158.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-28-3-memory-and-personalization-changes-in-rust-v0-158-0|3 Memory and Personalization changes in rust-v0.158.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-28-2-collaboration-changes-in-rust-v0-158-0|2 Collaboration changes in rust-v0.158.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-28-7-model-support-changes-in-rust-v0-158-0|7 Model Support changes in rust-v0.158.0]] · Model Support
- [[Changes/Codex CLI/2026-09-28-3-image-generation-changes-in-rust-v0-158-0|3 Image Generation changes in rust-v0.158.0]] · Image Generation
- [[Changes/Codex CLI/2026-09-28-4-editor-experience-changes-in-rust-v0-158-0|4 Editor Experience changes in rust-v0.158.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-28-6-interface-experience-changes-in-rust-v0-158-0|6 Interface Experience changes in rust-v0.158.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-28-47984-add-multi-agent-spawn-latency-and-failure-metrics-owenlin0|♯47984 Add multi-agent spawn latency and failure metrics @owenlin0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-28-14-developer-workflow-changes-in-rust-v0-158-0|14 Developer Workflow changes in rust-v0.158.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-28-17-context-window-changes-in-rust-v0-158-0|17 Context Window changes in rust-v0.158.0]] · Context Window
- [[Changes/Codex CLI/2026-09-28-96-other-changes-in-rust-v0-158-0|96 other changes in rust-v0.158.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-28 · Claude Code · [[Changes/Claude Code/2026-09-28-added-a-yes-but-ask-again-next-time-answer-to-auto-mode-s-prompt-before-a-read-o|Added a "Yes, but ask again next time" answer to auto mode's prompt before a read…]]
- Later: 2026-09-28 · ElevenLabs · [[Changes/ElevenLabs/2026-09-28-elevenagents|ElevenAgents]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-28-db454f&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-28-11-agent-mode-changes-in-rust-v0-158-0.md%0ACard%20ID%3A%20codex-cli-2026-09-28-db454f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.158.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->