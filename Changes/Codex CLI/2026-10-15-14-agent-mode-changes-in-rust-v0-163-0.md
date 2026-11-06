---
card_id: codex-cli-2026-10-15-dcb0b0
date: '2026-10-15'
description: 'Codex CLI · 2026-10-15 · Agent Mode: 14 changes in 0.163.0 — #51652
  Record telemetry for AGENTS.md changes made by apply_patch @jif-oai'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1197
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a01d2b0aae677ed272fd11d3466cb64bf8c9192c6564557df62ba40894a47d4e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-15-dcb0b0
  comparison: ''
  date: '2026-10-15'
  description: 'Codex CLI — 0.163.0: 14 Agent Mode changes'
  evidence:
  - quote: '#51652 Record telemetry for AGENTS.md changes made by apply_patch @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52034 Preserve agent state when unloading idle multi-agent v2 children
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52040 Add regression coverage for cancelled agent reloads @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52081 Fix idle cleanup for disconnected multi-agent v2 children @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52177 Set a User-Agent for package archive downloads @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52183 Add optional descriptions to agent message board channels @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52241 Preserve subagent capabilities independently of forked history
      @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52535 Add opt-in history prefix preservation for full agent forks @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52621 Add template setup for local agent message boards @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52946 Keep agent command center rows stable across progress updates @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53369 Allow turns when the agent message board is unavailable @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53617 Allow hiding native tools while retaining the multi-agent V2 runtime
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53660 Extract shared multi-agent v2 thread spawning @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53706 Preserve URLs and email addresses during external agent migration
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 14-agent-mode-changes-in-rust-v0-163-0
  source_release: codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6
  source_type: github_releases
  theme: agent-mode
  title: 14 Agent Mode changes in rust-v0.163.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-13-3-agent-mode-changes-in-v1-0-97|3 Agent
  Mode changes in v1.0.97]]'
- '[[Changes/Claude Code/2026-10-14-5-agent-mode-changes-in-v2-1-299|5 Agent Mode
  changes in v2.1.299]]'
- '[[Changes/Claude Code/2026-10-14-3-agent-mode-changes-in-v2-1-300|3 Agent Mode
  changes in v2.1.300]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6|codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6]]'
source_type: github_releases
theme: agent-mode
title: 14 Agent Mode changes in rust-v0.163.0
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Agent Mode changes in rust-v0.163.0

**Codex CLI** · 2026-10-15 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.163.0) · from [[Releases/Codex CLI/codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6|0.163.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #51652 Record telemetry for AGENTS.md changes made by apply_patch @jif-oai

> #52034 Preserve agent state when unloading idle multi-agent v2 children @jif-oai

> #52040 Add regression coverage for cancelled agent reloads @jif-oai

> #52081 Fix idle cleanup for disconnected multi-agent v2 children @jif-oai

> #52177 Set a User-Agent for package archive downloads @bolinfest

> #52183 Add optional descriptions to agent message board channels @jif-oai

> #52241 Preserve subagent capabilities independently of forked history @anp-oai

> #52535 Add opt-in history prefix preservation for full agent forks @jif-oai

> #52621 Add template setup for local agent message boards @jif-oai

> #52946 Keep agent command center rows stable across progress updates @fcoury-oai

> #53369 Allow turns when the agent message board is unavailable @jif-oai

> #53617 Allow hiding native tools while retaining the multi-agent V2 runtime @jif-oai

> #53660 Extract shared multi-agent v2 thread spawning @jif-oai

> #53706 Preserve URLs and email addresses during external agent migration @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.163.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-15-3-mobile-and-desktop-changes-in-rust-v0-163-0|3 Mobile and Desktop changes in rust-v0.163.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-15-6-model-support-changes-in-rust-v0-163-0|6 Model Support changes in rust-v0.163.0]] · Model Support
- [[Changes/Codex CLI/2026-10-15-15-apps-and-integrations-changes-in-rust-v0-163-0|15 Apps and Integrations changes in rust-v0.163.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-15-18-safety-and-privacy-changes-in-rust-v0-163-0|18 Safety and Privacy changes in rust-v0.163.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-15-4-collaboration-changes-in-rust-v0-163-0|4 Collaboration changes in rust-v0.163.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-15-codex-can-run-independent-read-only-tools-in-parallel-including-skill-memory-and|Codex can run independent read-only tools in parallel, including skill, memory…]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-15-15-developer-workflow-changes-in-rust-v0-163-0|15 Developer Workflow changes in rust-v0.163.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-15-4-voice-and-audio-changes-in-rust-v0-163-0|4 Voice and Audio changes in rust-v0.163.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-15-4-editor-experience-changes-in-rust-v0-163-0|4 Editor Experience changes in rust-v0.163.0]] · Editor Experience
- [[Changes/Codex CLI/2026-10-15-16-context-window-changes-in-rust-v0-163-0|16 Context Window changes in rust-v0.163.0]] · Context Window
- [[Changes/Codex CLI/2026-10-15-8-interface-experience-changes-in-rust-v0-163-0|8 Interface Experience changes in rust-v0.163.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-15-53389-use-cached-login-credentials-for-guardian-decisions-swastik-oai|♯53389 Use cached login credentials for Guardian decisions @swastik-oai]] · Account and Access
- [[Changes/Codex CLI/2026-10-15-134-other-changes-in-rust-v0-163-0|134 other changes in rust-v0.163.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-3-agent-mode-changes-in-v2-1-300|3 Agent Mode changes in v2.1.300]]
- Later: 2026-10-16 · ChatGPT · [[Changes/ChatGPT/2026-10-16-multiple-agents-that-can-work-on-different-parts-of-a-task-in-parallel-you-can-f|Multiple agents that can work on different parts of a task in parallel]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-15-dcb0b0&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-15-14-agent-mode-changes-in-rust-v0-163-0.md%0ACard%20ID%3A%20codex-cli-2026-10-15-dcb0b0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.163.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->