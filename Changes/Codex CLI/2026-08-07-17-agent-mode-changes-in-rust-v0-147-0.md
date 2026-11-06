---
card_id: codex-cli-2026-08-07-7b70f2
date: '2026-08-07'
description: 'Codex CLI · 2026-08-07 · Agent Mode: 17 changes in 0.147.0 — #35594
  Recommend longer waits in the v2 wait_agent schema @copyberry'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1128
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 782c247d71f7044a5b766decd6452dcc2fc5e18dd0f9b8e68525c5d1a0d6c4a5
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-07-7b70f2
  comparison: ''
  date: '2026-08-07'
  description: 'Codex CLI — 0.147.0: 17 Agent Mode changes'
  evidence:
  - quote: '#35594 Recommend longer waits in the v2 wait_agent schema @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35653 Test developer instruction inheritance for multi-agent workers
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35656 Preserve multi-agent settings across config representations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35708 Add configurable developer instructions for v2 subagents @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35744 Keep agent registry identities consistent @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35870 Include session titles in external agent import history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35895 Inherit ready step environments when spawning agents @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35944 Report direct input capability for listed subagents @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35992 Group external agent config migration into a module @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36329 Restrict `shell_command` to a single local environment @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36336 Detect connectors used in external agent sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36356 Sync updates to imported external agent sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36544 Support portable Agent Plugins throughout installation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36732 Stabilize the cloud environment HTTP test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36892 Support leaf models in multi-agent v2 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36959 Track connectors detected in external agent sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37189 Track multi-agent usage hints in world state @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 17-agent-mode-changes-in-rust-v0-147-0
  source_release: codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2
  source_type: github_releases
  theme: agent-mode
  title: 17 Agent Mode changes in rust-v0.147.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-06-2-agent-mode-changes-in-v2-1-223|2 Agent Mode
  changes in v2.1.223]]'
- '[[Changes/Gemini CLI/2026-08-06-feat-pr-generator-agent-implement-antigravity-agent-runner-and-prompt-templates|feat(pr-generator-agent):
  implement Antigravity agent runner and prompt templates …]]'
- '[[Changes/Claude Code/2026-08-07-removed-the-200-subagent-per-session-spawn-cap-long-running-sessions-no-longer-r|Removed
  the 200-subagent-per-session spawn cap]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2|codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2]]'
source_type: github_releases
theme: agent-mode
title: 17 Agent Mode changes in rust-v0.147.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Agent Mode changes in rust-v0.147.0

**Codex CLI** · 2026-08-07 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.147.0) · from [[Releases/Codex CLI/codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2|0.147.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #35594 Recommend longer waits in the v2 wait_agent schema @copyberry

> #35653 Test developer instruction inheritance for multi-agent workers @copyberry

> #35656 Preserve multi-agent settings across config representations @copyberry

> #35708 Add configurable developer instructions for v2 subagents @copyberry

> #35744 Keep agent registry identities consistent @copyberry

> #35870 Include session titles in external agent import history @copyberry

> #35895 Inherit ready step environments when spawning agents @copyberry

> #35944 Report direct input capability for listed subagents @copyberry

> #35992 Group external agent config migration into a module @copyberry

> #36329 Restrict `shell_command` to a single local environment @copyberry

> #36336 Detect connectors used in external agent sessions @copyberry

> #36356 Sync updates to imported external agent sessions @copyberry

> #36544 Support portable Agent Plugins throughout installation @copyberry

> #36732 Stabilize the cloud environment HTTP test @copyberry

> #36892 Support leaf models in multi-agent v2 @copyberry

> #36959 Track connectors detected in external agent sessions @copyberry

> #37189 Track multi-agent usage hints in world state @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.147.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-07-10-collaboration-changes-in-rust-v0-147-0|10 Collaboration changes in rust-v0.147.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-07-8-account-and-access-changes-in-rust-v0-147-0|8 Account and Access changes in rust-v0.147.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-07-36140-wait-for-memory-consolidation-shutdown-before-finishing-jobs-copyberry|♯36140 Wait for memory consolidation shutdown before finishing jobs @copyberry]] · Memory and Personalization
- [[Changes/Codex CLI/2026-08-07-65-apps-and-integrations-changes-in-rust-v0-147-0|65 Apps and Integrations changes in rust-v0.147.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-07-15-developer-workflow-changes-in-rust-v0-147-0|15 Developer Workflow changes in rust-v0.147.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-07-36043-document-the-responses-api-proxy-reqwest-exception-copyberry|♯36043 Document the Responses API proxy reqwest exception @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-08-07-36228-support-enterprise-automation-account-plans-copyberry|♯36228 Support Enterprise automation account plans @copyberry]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-08-07-3-search-and-browsing-changes-in-rust-v0-147-0|3 Search and Browsing changes in rust-v0.147.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-08-07-13-model-support-changes-in-rust-v0-147-0|13 Model Support changes in rust-v0.147.0]] · Model Support
- [[Changes/Codex CLI/2026-08-07-36807-extract-audio-preparation-into-a-utility-crate-copyberry|♯36807 Extract audio preparation into a utility crate @copyberry]] · Voice and Audio
- [[Changes/Codex CLI/2026-08-07-4-mobile-and-desktop-changes-in-rust-v0-147-0|4 Mobile and Desktop changes in rust-v0.147.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-07-9-safety-and-privacy-changes-in-rust-v0-147-0|9 Safety and Privacy changes in rust-v0.147.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-07-10-context-window-changes-in-rust-v0-147-0|10 Context Window changes in rust-v0.147.0]] · Context Window
- [[Changes/Codex CLI/2026-08-07-6-interface-experience-changes-in-rust-v0-147-0|6 Interface Experience changes in rust-v0.147.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-07-196-other-changes-in-rust-v0-147-0|196 other changes in rust-v0.147.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-07 · Claude Code · [[Changes/Claude Code/2026-08-07-removed-the-200-subagent-per-session-spawn-cap-long-running-sessions-no-longer-r|Removed the 200-subagent-per-session spawn cap]]
- Later: 2026-08-07 · OpenHands · [[Changes/OpenHands/2026-08-07-feat-add-a-typed-agent-action-for-launching-local-or-cloud-child-conversations-b|feat: add a typed agent action for launching local or Cloud child conversations]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-07-7b70f2&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-07-17-agent-mode-changes-in-rust-v0-147-0.md%0ACard%20ID%3A%20codex-cli-2026-08-07-7b70f2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.147.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->