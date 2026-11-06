---
card_id: codex-cli-2026-03-26-b03781
date: '2026-03-26'
description: 'Codex CLI · 2026-03-26 · Agent Mode: 19 changes in 0.117.0 — Sub-agents
  now use readable path-based addresses like `/root/agent_a`, with structured inter-agent…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 994
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8837b2762cfac0a998280c092e4a8dca77a288b6fd62abc26d9755f213a1ee78
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-26-b03781
  comparison: ''
  date: '2026-03-26'
  description: 'Codex CLI — 0.117.0: 19 Agent Mode changes'
  evidence:
  - quote: 'Sub-agents now use readable path-based addresses like `/root/agent_a`,
      with structured inter-agent messaging and agent listing for multi-agent v2 workflows.
      (#15313, #15515, #15556, #15570, #15621, #15647)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: 'Remote multi-agent sessions now show agent names instead of raw IDs and
      recover more gracefully from stale turn-steering races. (#15513, #15714, #15163)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15056 feat: add graph representation of agent network @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15163 fix: case where agent is already closed @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15313 feat: change multi-agent to use path-like system instead of uuids
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15515 feat: structured multi-agent output @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15540 chore: split sub-agent v2 implementation @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15556 feat: new op type for sub-agents communication @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15560 feat: use serde to differenciate inter agent communication @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15570 feat: custom watcher for multi-agent v2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15575 feat: custom watcher for multi-agent v2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15576 feat: custom watcher for multi-agent v2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15621 feat: list agents for sub-agent v2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15623 nit: optim on list agents @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15624 feat: disable notifier v2 and start turn on agent interaction @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15513 fix(tui_app_server): fix remote subagent switching and agent names
      @fcoury'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15877 chore: ask agents md not to play with PIDs @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15880 fix: max depth agent still has v2 tools @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15881 fix: root as std agent @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 19-agent-mode-changes-in-rust-v0-117-0
  source_release: codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6
  source_type: github_releases
  theme: agent-mode
  title: 19 Agent Mode changes in rust-v0.117.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-25-agents-can-now-declare-initialprompt-in-frontmatter-to-auto-submit-a-first-turn|Agents
  can now declare initialPrompt in frontmatter to auto-submit a first turn]]'
- '[[Changes/Cursor/2026-03-25-cursor-now-supports-self-hosted-cloud-agents-that-keep-your-code-and-tool-execut-e411f3|Self-hosted
  Cloud Agents]]'
- '[[Changes/Claude Code/2026-03-26-2-agent-mode-changes-in-v2-1-84|2 Agent Mode changes
  in v2.1.84]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6]]'
source_type: github_releases
theme: agent-mode
title: 19 Agent Mode changes in rust-v0.117.0
type: change
---

<!-- chronolog:begin region="header" -->
# 19 Agent Mode changes in rust-v0.117.0

**Codex CLI** · 2026-03-26 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.117.0) · from [[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|0.117.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Sub-agents now use readable path-based addresses like `/root/agent_a`, with structured inter-agent messaging and agent listing for multi-agent v2 workflows. (#15313, #15515, #15556, #15570, #15621, #15647)

> Remote multi-agent sessions now show agent names instead of raw IDs and recover more gracefully from stale turn-steering races. (#15513, #15714, #15163)

> #15056 feat: add graph representation of agent network @jif-oai

> #15163 fix: case where agent is already closed @jif-oai

> #15313 feat: change multi-agent to use path-like system instead of uuids @jif-oai

> #15515 feat: structured multi-agent output @jif-oai

> #15540 chore: split sub-agent v2 implementation @jif-oai

> #15556 feat: new op type for sub-agents communication @jif-oai

> #15560 feat: use serde to differenciate inter agent communication @jif-oai

> #15570 feat: custom watcher for multi-agent v2 @jif-oai

> #15575 feat: custom watcher for multi-agent v2 @jif-oai

> #15576 feat: custom watcher for multi-agent v2 @jif-oai

> #15621 feat: list agents for sub-agent v2 @jif-oai

> #15623 nit: optim on list agents @jif-oai

> #15624 feat: disable notifier v2 and start turn on agent interaction @jif-oai

> #15513 fix(tui_app_server): fix remote subagent switching and agent names @fcoury

> #15877 chore: ask agents md not to play with PIDs @jif-oai

> #15880 fix: max depth agent still has v2 tools @jif-oai

> #15881 fix: root as std agent @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.117.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-26-19-developer-workflow-changes-in-rust-v0-117-0|19 Developer Workflow changes in rust-v0.117.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-26-15789-treat-chatgpt-hc-plan-as-enterprise-arnavdugar-openai|♯15789 Treat ChatGPT hc plan as Enterprise @arnavdugar-openai]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-03-26-the-app-server-backed-tui-is-now-enabled-by-default-and-the-plugin-app-rollout-f|The app-server-backed TUI is now enabled by default, and the plugin/app rollout…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-26-plugins-are-now-a-first-class-workflow-codex-can-sync-product-scoped-plugins-at|Plugins are now a first-class workflow]] · Search and Browsing
- [[Changes/Codex CLI/2026-03-26-2-image-generation-changes-in-rust-v0-117-0|2 Image Generation changes in rust-v0.117.0]] · Image Generation
- [[Changes/Codex CLI/2026-03-26-15579-increase-voice-space-hold-timeout-to-1s-aibrahim-oai|♯15579 Increase voice space hold timeout to 1s @aibrahim-oai]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-26-2-automation-and-scheduling-changes-in-rust-v0-117-0|2 Automation and Scheduling changes in rust-v0.117.0]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-03-26-5-context-window-changes-in-rust-v0-117-0|5 Context Window changes in rust-v0.117.0]] · Context Window
- [[Changes/Codex CLI/2026-03-26-14945-feat-tui-restore-composer-history-in-app-server-tui-fcoury|♯14945 feat(tui): restore composer history in app-server tui @fcoury]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-03-26-15480-use-shift-left-to-edit-queued-messages-in-tmux-charley-oai|♯15480 Use Shift+Left to edit queued messages in tmux @charley-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-03-26-3-interface-experience-changes-in-rust-v0-117-0|3 Interface Experience changes in rust-v0.117.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-26-4-account-and-access-changes-in-rust-v0-117-0|4 Account and Access changes in rust-v0.117.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-26-57-apps-and-integrations-changes-in-rust-v0-117-0|57 Apps and Integrations changes in rust-v0.117.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-26-3-mobile-and-desktop-changes-in-rust-v0-117-0|3 Mobile and Desktop changes in rust-v0.117.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-26-5-safety-and-privacy-changes-in-rust-v0-117-0|5 Safety and Privacy changes in rust-v0.117.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-26-3-model-support-changes-in-rust-v0-117-0|3 Model Support changes in rust-v0.117.0]] · Model Support
- [[Changes/Codex CLI/2026-03-26-15175-chore-morpheus-does-not-generate-memories-jif-oai|♯15175 chore: morpheus does not generate memories @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-26-117-other-changes-in-rust-v0-117-0|117 other changes in rust-v0.117.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-2-agent-mode-changes-in-v2-1-84|2 Agent Mode changes in v2.1.84]]
- Later: 2026-03-26 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-26-resume-session-restores-the-previously-selected-custom-agent|Resume session restores the previously selected custom agent]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-26-b03781&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-26-19-agent-mode-changes-in-rust-v0-117-0.md%0ACard%20ID%3A%20codex-cli-2026-03-26-b03781%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.117.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->