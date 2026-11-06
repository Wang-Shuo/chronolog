---
card_id: codex-cli-2026-03-05-b313be
date: '2026-03-05'
description: 'Codex CLI · 2026-03-05 · Memory and Personalization: 5 changes in 0.110.0
  — Improved memories with workspace-scoped writes, renamed memory settings, and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 959
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6ff53c7ba36646b4a73ccc4e53a71d36c9fb349d46fba1164ca1521d9685a769
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-05-b313be
  comparison: ''
  date: '2026-03-05'
  description: 'Codex CLI — 0.110.0: 5 Memory and Personalization changes'
  evidence:
  - quote: 'Improved memories with workspace-scoped writes, renamed memory settings,
      and guardrails against saving stale or polluted facts. (#13008, #13088, #13237,
      #13467)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13088 Tune memory read-path for stale facts @andi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13008 feat: polluted memories @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13237 feat: update memories config names @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13467 feat: memories in workspace write @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-memory-and-personalization-changes-in-rust-v0-110-0
  source_release: codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302
  source_type: github_releases
  theme: memory
  title: 5 Memory and Personalization changes in rust-v0.110.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-02-26-3-memory-and-personalization-changes-in-rust-v0-106-0|3
  Memory and Personalization changes in rust-v0.106.0]]'
- '[[Changes/Claude Code/2026-02-28-project-configs-auto-memory-now-shared-across-git-worktrees-of-the-same-reposito|Project
  configs & auto memory now shared across git worktrees of the same repository]]'
- '[[Changes/Codex CLI/2026-03-02-6-memory-and-personalization-changes-in-rust-v0-107-0|6
  Memory and Personalization changes in rust-v0.107.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302|codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302]]'
source_type: github_releases
theme: memory
title: 5 Memory and Personalization changes in rust-v0.110.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Memory and Personalization changes in rust-v0.110.0

**Codex CLI** · 2026-03-05 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.110.0) · from [[Releases/Codex CLI/codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302|0.110.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved memories with workspace-scoped writes, renamed memory settings, and guardrails against saving stale or polluted facts. (#13008, #13088, #13237, #13467)

> #13088 Tune memory read-path for stale facts @andi-oai

> #13008 feat: polluted memories @jif-oai

> #13237 feat: update memories config names @jif-oai

> #13467 feat: memories in workspace write @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.110.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-05-12935-speed-up-subagent-startup-daveaitel-openai|♯12935 Speed up subagent startup @daveaitel-openai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-03-05-2-model-support-changes-in-rust-v0-110-0|2 Model Support changes in rust-v0.110.0]] · Model Support
- [[Changes/Codex CLI/2026-03-05-13127-nit-disable-on-windows-jif-oai|♯13127 nit: disable on windows @jif-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-05-13-agent-mode-changes-in-rust-v0-110-0|13 Agent Mode changes in rust-v0.110.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-05-13313-renaming-team-to-business-plan-during-tui-onboarding-bwanner-oai|♯13313 Renaming Team to Business plan during TUI onboarding @bwanner-oai]] · Interface Experience
- [[Changes/Codex CLI/2026-03-05-12383-add-new-scopes-to-login-adaley-openai|♯12383 add new scopes to login @adaley-openai]] · Account and Access
- [[Changes/Codex CLI/2026-03-05-4-files-and-data-changes-in-rust-v0-110-0|4 Files and Data changes in rust-v0.110.0]] · Files and Data
- [[Changes/Codex CLI/2026-03-05-13388-config-enforce-enterprise-feature-requirements-bolinfest|♯13388 config: enforce enterprise feature requirements @bolinfest]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-03-05-7-apps-and-integrations-changes-in-rust-v0-110-0|7 Apps and Integrations changes in rust-v0.110.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-05-7-developer-workflow-changes-in-rust-v0-110-0|7 Developer Workflow changes in rust-v0.110.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-05-4-safety-and-privacy-changes-in-rust-v0-110-0|4 Safety and Privacy changes in rust-v0.110.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-05-3-context-window-changes-in-rust-v0-110-0|3 Context Window changes in rust-v0.110.0]] · Context Window
- [[Changes/Codex CLI/2026-03-05-71-other-changes-in-rust-v0-110-0|71 other changes in rust-v0.110.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-03-02 · Codex CLI · [[Changes/Codex CLI/2026-03-02-6-memory-and-personalization-changes-in-rust-v0-107-0|6 Memory and Personalization changes in rust-v0.107.0]]
- Later: 2026-03-10 · Codex CLI · [[Changes/Codex CLI/2026-03-10-13734-feat-prune-old-memories-in-db-jif-oai|♯13734 feat: prune old memories in DB @jif-oai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-05-b313be&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-05-5-memory-and-personalization-changes-in-rust-v0-110-0.md%0ACard%20ID%3A%20codex-cli-2026-03-05-b313be%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.110.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->