---
card_id: codex-cli-2026-09-25-eb9808
date: '2026-09-25'
description: 'Codex CLI · 2026-09-25 · Agent Mode: 13 changes in 0.157.0 — #47063
  Add a partial index for agent message board root posts @jif-oai'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1177
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fb2e57a2f0db2213fafe57f3640756980cc1b33d40495b9703ede53299a82ff2
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-25-eb9808
  comparison: ''
  date: '2026-09-25'
  description: 'Codex CLI — 0.157.0: 13 Agent Mode changes'
  evidence:
  - quote: '#47063 Add a partial index for agent message board root posts @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47075 Include attributed previews in agent message board notifications
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47235 Route multi-agent spawning through `SpawnRequest` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47236 Suppress agent message board notifications to the post author @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47240 Prevent V2 agent eviction from racing with queued messages @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47244 Centralize agent resume handling in `LocalAgentControl` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47252 Return agent snapshots from `close_agent` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47267 Stream agent snapshots from local status subscriptions @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47292 Consolidate agent operations in the `AgentControl` implementation
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47301 Separate local agent runtime state from controller handles @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47319 Match agent status symbols to the selected row style @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47348 Overlap subagent spawn persistence and clean up cancelled children
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  - quote: '#47369 Overlap agent metadata reads when resuming a V2 root @vkg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.157.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 13-agent-mode-changes-in-rust-v0-157-0
  source_release: codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3
  source_type: github_releases
  theme: agent-mode
  title: 13 Agent Mode changes in rust-v0.157.0
  type: change
related_changes:
- '[[Changes/Cursor/2026-09-23-when-rollouts-detects-a-regression-it-names-the-change-it-suspects-and-notifies|When
  Rollouts detects a regression, it names the change it suspects and notifies…]]'
- '[[Changes/Claude Code/2026-09-24-2-agent-mode-changes-in-v2-1-282|2 Agent Mode
  changes in v2.1.282]]'
- '[[Changes/Claude Code/2026-09-25-improved-startup-claude-p-and-claude-code-remote-no-longer-load-the-interactive|Improved
  startup: claude -p and Claude Code Remote no longer load the interactive…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3|codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3]]'
source_type: github_releases
theme: agent-mode
title: 13 Agent Mode changes in rust-v0.157.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Agent Mode changes in rust-v0.157.0

**Codex CLI** · 2026-09-25 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.157.0) · from [[Releases/Codex CLI/codex-cli-2026-09-25-rust-v0-157-0-github-396234532-e8248ab3|0.157.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #47063 Add a partial index for agent message board root posts @jif-oai

> #47075 Include attributed previews in agent message board notifications @jif-oai

> #47235 Route multi-agent spawning through `SpawnRequest` @jif-oai

> #47236 Suppress agent message board notifications to the post author @jif-oai

> #47240 Prevent V2 agent eviction from racing with queued messages @jif-oai

> #47244 Centralize agent resume handling in `LocalAgentControl` @jif-oai

> #47252 Return agent snapshots from `close_agent` @jif-oai

> #47267 Stream agent snapshots from local status subscriptions @jif-oai

> #47292 Consolidate agent operations in the `AgentControl` implementation @jif-oai

> #47301 Separate local agent runtime state from controller handles @jif-oai

> #47319 Match agent status symbols to the selected row style @etraut-openai

> #47348 Overlap subagent spawn persistence and clean up cancelled children @owenlin0

> #47369 Overlap agent metadata reads when resuming a V2 root @vkg-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.157.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-25-9-apps-and-integrations-changes-in-rust-v0-157-0|9 Apps and Integrations changes in rust-v0.157.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-25-47411-apply-shared-network-policy-throughout-embedded-codex-startup-acrognale-oa|♯47411 Apply shared network policy throughout embedded Codex startup @acrognale-oai]] · Collaboration
- [[Changes/Codex CLI/2026-09-25-6-context-window-changes-in-rust-v0-157-0|6 Context Window changes in rust-v0.157.0]] · Context Window
- [[Changes/Codex CLI/2026-09-25-47086-format-analytics-credit-usage-with-consistent-decimal-precision-fcoury-oai|♯47086 Format analytics credit usage with consistent decimal precision @fcoury-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-09-25-2-safety-and-privacy-changes-in-rust-v0-157-0|2 Safety and Privacy changes in rust-v0.157.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-25-8-model-support-changes-in-rust-v0-157-0|8 Model Support changes in rust-v0.157.0]] · Model Support
- [[Changes/Codex CLI/2026-09-25-9-interface-experience-changes-in-rust-v0-157-0|9 Interface Experience changes in rust-v0.157.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-25-added-retries-for-transient-file-upload-failures-and-increased-the-upload-timeou|Added retries for transient file-upload failures and increased the upload timeout…]] · Files and Data
- [[Changes/Codex CLI/2026-09-25-47327-preserve-image-generation-request-ids-on-failure-chrisdong-oai|♯47327 Preserve image generation request IDs on failure @chrisdong-oai]] · Image Generation
- [[Changes/Codex CLI/2026-09-25-5-voice-and-audio-changes-in-rust-v0-157-0|5 Voice and Audio changes in rust-v0.157.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-25-4-developer-workflow-changes-in-rust-v0-157-0|4 Developer Workflow changes in rust-v0.157.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-25-2-search-and-browsing-changes-in-rust-v0-157-0|2 Search and Browsing changes in rust-v0.157.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-09-25-5-account-and-access-changes-in-rust-v0-157-0|5 Account and Access changes in rust-v0.157.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-25-70-other-changes-in-rust-v0-157-0|70 other changes in rust-v0.157.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-25 · Claude Code · [[Changes/Claude Code/2026-09-25-improved-startup-claude-p-and-claude-code-remote-no-longer-load-the-interactive|Improved startup: claude -p and Claude Code Remote no longer load the interactive…]]
- Later: 2026-09-25 · OpenHands · [[Changes/OpenHands/2026-09-25-docs-correct-outdated-cloud-proxy-rule-2-in-agents-md-by-juanmichelini-in-https|docs: correct outdated cloud-proxy Rule 2 in AGENTS.md]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-25-eb9808&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-25-13-agent-mode-changes-in-rust-v0-157-0.md%0ACard%20ID%3A%20codex-cli-2026-09-25-eb9808%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.157.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->