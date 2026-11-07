---
card_id: codex-cli-2026-04-23-a36157
date: '2026-04-23'
description: 'Codex CLI · 2026-04-23 · Agent Mode: 11 changes in 0.124.0 — #18757
  fix: fully revert agent identity runtime wiring @efrazer-oai'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1022
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3bf70d4962fc7d29b6411413772ede8557dd63719c5e04dc8e3588d66da540b2
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-23-a36157
  comparison: ''
  date: '2026-04-23'
  description: 'Codex CLI — 0.124.0: 11 Agent Mode changes'
  evidence:
  - quote: '#18757 fix: fully revert agent identity runtime wiring @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18915 fix: windows snapshot for external_agent_config_migration::tests::prompt_snapshot
      did not match windows output @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18871 refactor: add agent identity crate @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18968 fix: wait_agent timeout for queued mailbox mail @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18959 feat(auto-review) policy config @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18955 Add plumbing to approve stored Auto-Review denials @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18890 feat(auto-review) short-circuit @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#18504 Rebrand approvals reviewer config to auto-review @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19056 Rename approvals reviewer variant to auto-review @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19059 core: box multi-agent wrapper futures @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  - quote: '#19063 chore(auto-review) feature => stable @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.124.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-agent-mode-changes-in-rust-v0-124-0
  source_release: codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b
  source_type: github_releases
  theme: agent-mode
  title: 11 Agent Mode changes in rust-v0.124.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-23-2-agent-mode-changes-in-v2-1-118|2 Agent Mode
  changes in v2.1.118]]'
- '[[Changes/Claude Code/2026-04-23-2-agent-mode-changes-in-v2-1-119|2 Agent Mode
  changes in v2.1.119]]'
- '[[Changes/Codex CLI/2026-04-23-8-agent-mode-changes-in-rust-v0-123-0|8 Agent Mode
  changes in rust-v0.123.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b|codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b]]'
source_type: github_releases
theme: agent-mode
title: 11 Agent Mode changes in rust-v0.124.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Agent Mode changes in rust-v0.124.0

**Codex CLI** · 2026-04-23 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.124.0) · from [[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-124-0-github-312880358-5864635b|0.124.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #18757 fix: fully revert agent identity runtime wiring @efrazer-oai

> #18915 fix: windows snapshot for external_agent_config_migration::tests::prompt_snapshot did not match windows output @bolinfest

> #18871 refactor: add agent identity crate @efrazer-oai

> #18968 fix: wait_agent timeout for queued mailbox mail @jif-oai

> #18959 feat(auto-review) policy config @dylan-hurd-oai

> #18955 Add plumbing to approve stored Auto-Review denials @won-openai

> #18890 feat(auto-review) short-circuit @dylan-hurd-oai

> #18504 Rebrand approvals reviewer config to auto-review @won-openai

> #19056 Rename approvals reviewer variant to auto-review @won-openai

> #19059 core: box multi-agent wrapper futures @bolinfest

> #19063 chore(auto-review) feature => stable @dylan-hurd-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.124.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-23-17-safety-and-privacy-changes-in-rust-v0-124-0|17 Safety and Privacy changes in rust-v0.124.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-23-12-apps-and-integrations-changes-in-rust-v0-124-0|12 Apps and Integrations changes in rust-v0.124.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-23-2-developer-workflow-changes-in-rust-v0-124-0|2 Developer Workflow changes in rust-v0.124.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-23-18973-chore-prep-memories-for-ab-jif-oai|♯18973 chore: prep memories for AB @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-23-2-context-window-changes-in-rust-v0-124-0|2 Context Window changes in rust-v0.124.0]] · Context Window
- [[Changes/Codex CLI/2026-04-23-4-model-support-changes-in-rust-v0-124-0|4 Model Support changes in rust-v0.124.0]] · Model Support
- [[Changes/Codex CLI/2026-04-23-45-other-changes-in-rust-v0-124-0|45 other changes in rust-v0.124.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-23 · Codex CLI · [[Changes/Codex CLI/2026-04-23-8-agent-mode-changes-in-rust-v0-123-0|8 Agent Mode changes in rust-v0.123.0]]
- Later: 2026-04-23 · Gemini CLI · [[Changes/Gemini CLI/2026-04-23-6-agent-mode-changes-in-v0-39-0|6 Agent Mode changes in v0.39.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-23-a36157&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-23-11-agent-mode-changes-in-rust-v0-124-0.md%0ACard%20ID%3A%20codex-cli-2026-04-23-a36157%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.124.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->