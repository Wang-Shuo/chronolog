---
card_id: codex-cli-2026-10-27-59d34b
date: '2026-10-27'
description: 'Codex CLI · 2026-10-27 · Agent Mode: 4 changes in 0.165.0 — Prevented
  queued agent messages from restarting work after an interrupt or a switch to Plan
  mode…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1209
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 620ada9ba47f8723159de3b309260a00d234c39ed1f879a99d75dc53d4f9985e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-27-59d34b
  comparison: ''
  date: '2026-10-27'
  description: 'Codex CLI — 0.165.0: 4 Agent Mode changes'
  evidence:
  - quote: Prevented queued agent messages from restarting work after an interrupt
      or a switch to Plan mode. (#56330)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56133 Defer agent mail after empty final answers @eknight-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56330 Make agent-message wakes respect interrupts and Plan mode @alishobeiri-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56453 Make the Realtime V2 background-agent steering test deterministic
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-agent-mode-changes-in-rust-v0-165-0
  source_release: codex-cli-2026-10-27-rust-v0-165-0-github-425927431-1fa685eb
  source_type: github_releases
  theme: agent-mode
  title: 4 Agent Mode changes in rust-v0.165.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-26-2-agent-mode-changes-in-v2-1-311|2 Agent Mode
  changes in v2.1.311]]'
- '[[Changes/Windsurf/2026-10-26-the-status-bar-no-longer-disappears-after-you-switch-from-agent-mode-to-ide-mode|The
  status bar no longer disappears after you switch from Agent mode to IDE mode]]'
- '[[Changes/Claude Code/2026-10-27-2-agent-mode-changes-in-v2-1-312|2 Agent Mode
  changes in v2.1.312]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-27-rust-v0-165-0-github-425927431-1fa685eb|codex-cli-2026-10-27-rust-v0-165-0-github-425927431-1fa685eb]]'
source_type: github_releases
theme: agent-mode
title: 4 Agent Mode changes in rust-v0.165.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in rust-v0.165.0

**Codex CLI** · 2026-10-27 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.165.0) · from [[Releases/Codex CLI/codex-cli-2026-10-27-rust-v0-165-0-github-425927431-1fa685eb|0.165.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Prevented queued agent messages from restarting work after an interrupt or a switch to Plan mode. (#56330)

> #56133 Defer agent mail after empty final answers @eknight-oai

> #56330 Make agent-message wakes respect interrupts and Plan mode @alishobeiri-oai

> #56453 Make the Realtime V2 background-agent steering test deterministic @felixxia-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.165.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-27-9-model-support-changes-in-rust-v0-165-0|9 Model Support changes in rust-v0.165.0]] · Model Support
- [[Changes/Codex CLI/2026-10-27-added-a-repository-filter-to-the-session-picker-and-directory-grouping-to-the-ag|Added a repository filter to the session picker and directory grouping to the agent…]] · Interface Experience
- [[Changes/Codex CLI/2026-10-27-3-safety-and-privacy-changes-in-rust-v0-165-0|3 Safety and Privacy changes in rust-v0.165.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-27-2-context-window-changes-in-rust-v0-165-0|2 Context Window changes in rust-v0.165.0]] · Context Window
- [[Changes/Codex CLI/2026-10-27-10-apps-and-integrations-changes-in-rust-v0-165-0|10 Apps and Integrations changes in rust-v0.165.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-27-3-developer-workflow-changes-in-rust-v0-165-0|3 Developer Workflow changes in rust-v0.165.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-27-5-memory-and-personalization-changes-in-rust-v0-165-0|5 Memory and Personalization changes in rust-v0.165.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-27-3-account-and-access-changes-in-rust-v0-165-0|3 Account and Access changes in rust-v0.165.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-27-39-other-changes-in-rust-v0-165-0|39 other changes in rust-v0.165.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-27 · Claude Code · [[Changes/Claude Code/2026-10-27-2-agent-mode-changes-in-v2-1-312|2 Agent Mode changes in v2.1.312]]
- Later: 2026-10-27 · OpenHands · [[Changes/OpenHands/2026-10-27-feat-verify-stand-in-for-digitalocean-so-managed-agents-can-be-verified-by-enyst|feat(verify): stand in for DigitalOcean so Managed Agents can be verified]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-27-59d34b&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-27-4-agent-mode-changes-in-rust-v0-165-0.md%0ACard%20ID%3A%20codex-cli-2026-10-27-59d34b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.165.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->