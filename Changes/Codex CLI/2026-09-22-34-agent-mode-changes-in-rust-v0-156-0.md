---
card_id: codex-cli-2026-09-22-87ba16
date: '2026-09-22'
description: 'Codex CLI · 2026-09-22 · Agent Mode: 34 changes in 0.156.0 — #44631
  Focus the task list when reopening the agent command center @etraut-openai'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1174
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b17989c5c8b414c858c0bc8403a791d473da0ec33aa73c2856abcb8326387e14
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-22-87ba16
  comparison: ''
  date: '2026-09-22'
  description: 'Codex CLI — 0.156.0: 34 Agent Mode changes'
  evidence:
  - quote: '#44631 Focus the task list when reopening the agent command center @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44659 Preserve turn triggers across delegated agent work @joeytrasatti-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44752 Render Markdown in agent overview task details @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45112 Use blueberry in the realtime background-agent test fixture @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45491 Remove Guardian subagent-spawner plumbing @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45669 Centralize child agent configuration in the agent module @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45670 Move V2 agent message delivery into `AgentControl` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45676 Move spawned-agent interruption rules into `AgentControl` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45978 Keep selection adjacent when hiding tasks in the agents overview
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45983 Show a loading message when opening tasks from the agents overview
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46075 Use captured step settings when spawning subagents @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46104 Pause TUI events in the agents overview regression test @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46123 Allow model catalogs to override the V2 `spawn_agent` description
      @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46264 Relax delegation guidance in the v2 `spawn_agent` description @surajs-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46297 Support catalog descriptions for all multi-agent V2 tools @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46505 Support catalog parameter schemas for Multi-Agent V2 tools @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46547 Expose a backend-independent agent control contract @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46553 Return `LiveAgent` records from agent listing @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46577 Allow thread instruction providers to share updates with subagents
      @vinh-gpt'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46579 Limit the agent command center to 10 recent sessions on startup
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46838 Refine the agent command center layout and metadata editing @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46839 Add status filter tabs to the agent command center @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46867 Preserve streamed answers when subagents finish @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46882 Streamline agent command-center shortcuts and layout @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46946 Populate the agents overview from background tool responses @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46959 Add shared agent message-board extension interfaces @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46966 Add SQLite storage for local agent message boards @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46978 Implement paginated queries for the local agent message board @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46994 Route agent delivery through captured send requests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#47010 Add agent inspection without restoring unloaded runtimes @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#47017 Wire agent message boards into persistent multi-agent runtimes
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#47028 Align message-board tools with the multi-agent namespace @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#47038 Cache OS discovery for user agents and telemetry @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#47049 Share SQLite pools across local agent message-board handles @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 34-agent-mode-changes-in-rust-v0-156-0
  source_release: codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4
  source_type: github_releases
  theme: agent-mode
  title: 34 Agent Mode changes in rust-v0.156.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-09-21-show-live-elapsed-time-for-execution-subagents-in-timeline-entries|Show
  live elapsed time for execution subagents in timeline entries]]'
- '[[Changes/Claude Code/2026-09-22-2-agent-mode-changes-in-v2-1-280|2 Agent Mode
  changes in v2.1.280]]'
- '[[Changes/Cline/2026-09-22-2-agent-mode-changes-in-v4-1-20|2 Agent Mode changes
  in v4.1.20]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4]]'
source_type: github_releases
theme: agent-mode
title: 34 Agent Mode changes in rust-v0.156.0
type: change
---

<!-- chronolog:begin region="header" -->
# 34 Agent Mode changes in rust-v0.156.0

**Codex CLI** · 2026-09-22 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.156.0) · from [[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #44631 Focus the task list when reopening the agent command center @etraut-openai

> #44659 Preserve turn triggers across delegated agent work @joeytrasatti-openai

> #44752 Render Markdown in agent overview task details @etraut-openai

> #45112 Use blueberry in the realtime background-agent test fixture @anp-oai

> #45491 Remove Guardian subagent-spawner plumbing @felixxia-oai

> #45669 Centralize child agent configuration in the agent module @jif-oai

> #45670 Move V2 agent message delivery into `AgentControl` @jif-oai

> #45676 Move spawned-agent interruption rules into `AgentControl` @jif-oai

> #45978 Keep selection adjacent when hiding tasks in the agents overview @etraut-openai

> #45983 Show a loading message when opening tasks from the agents overview @etraut-openai

> #46075 Use captured step settings when spawning subagents @rhan-oai

> #46104 Pause TUI events in the agents overview regression test @etraut-openai

> #46123 Allow model catalogs to override the V2 `spawn_agent` description @rhan-oai

> #46264 Relax delegation guidance in the v2 `spawn_agent` description @surajs-oai

> #46297 Support catalog descriptions for all multi-agent V2 tools @rhan-oai

> #46505 Support catalog parameter schemas for Multi-Agent V2 tools @rhan-oai

> #46547 Expose a backend-independent agent control contract @jif-oai

> #46553 Return `LiveAgent` records from agent listing @jif-oai

> #46577 Allow thread instruction providers to share updates with subagents @vinh-gpt

> #46579 Limit the agent command center to 10 recent sessions on startup @etraut-openai

> #46838 Refine the agent command center layout and metadata editing @etraut-openai

> #46839 Add status filter tabs to the agent command center @etraut-openai

> #46867 Preserve streamed answers when subagents finish @fcoury-oai

> #46882 Streamline agent command-center shortcuts and layout @etraut-openai

> #46946 Populate the agents overview from background tool responses @etraut-openai

> #46959 Add shared agent message-board extension interfaces @jif-oai

> #46966 Add SQLite storage for local agent message boards @jif-oai

> #46978 Implement paginated queries for the local agent message board @jif-oai

> #46994 Route agent delivery through captured send requests @jif-oai

> #47010 Add agent inspection without restoring unloaded runtimes @jif-oai

> #47017 Wire agent message boards into persistent multi-agent runtimes @jif-oai

> #47028 Align message-board tools with the multi-agent namespace @jif-oai

> #47038 Cache OS discovery for user agents and telemetry @charliemarsh-oai

> #47049 Share SQLite pools across local agent message-board handles @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.156.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-22-13-account-and-access-changes-in-rust-v0-156-0|13 Account and Access changes in rust-v0.156.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-22-32-interface-experience-changes-in-rust-v0-156-0|32 Interface Experience changes in rust-v0.156.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-22-2-search-and-browsing-changes-in-rust-v0-156-0|2 Search and Browsing changes in rust-v0.156.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-09-22-46027-document-and-test-wildcards-in-network-proxy-domain-patterns-viyatb-oai|♯46027 Document and test ? wildcards in network proxy domain patterns @viyatb-oai]] · Files and Data
- [[Changes/Codex CLI/2026-09-22-42-apps-and-integrations-changes-in-rust-v0-156-0|42 Apps and Integrations changes in rust-v0.156.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-22-45544-discourage-logging-full-image-generation-results-gan-tu|♯45544 Discourage logging full image generation results @Gan-Tu]] · Image Generation
- [[Changes/Codex CLI/2026-09-22-17-context-window-changes-in-rust-v0-156-0|17 Context Window changes in rust-v0.156.0]] · Context Window
- [[Changes/Codex CLI/2026-09-22-45849-preserve-the-app-server-shutdown-signal-future-across-loop-iterations-jger|♯45849 Preserve the app-server shutdown signal future across loop iterations @jgershen-oai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-09-22-11-mobile-and-desktop-changes-in-rust-v0-156-0|11 Mobile and Desktop changes in rust-v0.156.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-22-46040-default-tui-animations-off-when-a-screen-reader-is-detected-etraut-openai|♯46040 Default TUI animations off when a screen reader is detected @etraut-openai]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-09-22-9-collaboration-changes-in-rust-v0-156-0|9 Collaboration changes in rust-v0.156.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-22-6-memory-and-personalization-changes-in-rust-v0-156-0|6 Memory and Personalization changes in rust-v0.156.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-22-6-editor-experience-changes-in-rust-v0-156-0|6 Editor Experience changes in rust-v0.156.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-22-17-voice-and-audio-changes-in-rust-v0-156-0|17 Voice and Audio changes in rust-v0.156.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-22-25-model-support-changes-in-rust-v0-156-0|25 Model Support changes in rust-v0.156.0]] · Model Support
- [[Changes/Codex CLI/2026-09-22-50-safety-and-privacy-changes-in-rust-v0-156-0|50 Safety and Privacy changes in rust-v0.156.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-22-45960-tag-memory-usage-telemetry-with-the-memory-version-jif-oai|♯45960 Tag memory usage telemetry with the memory version @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-22-22-developer-workflow-changes-in-rust-v0-156-0|22 Developer Workflow changes in rust-v0.156.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-22-248-other-changes-in-rust-v0-156-0|248 other changes in rust-v0.156.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-22 · Cline · [[Changes/Cline/2026-09-22-2-agent-mode-changes-in-v4-1-20|2 Agent Mode changes in v4.1.20]]
- Later: 2026-09-22 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-22-2-agent-mode-changes-in-v1-0-88|2 Agent Mode changes in v1.0.88]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-22-87ba16&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-22-34-agent-mode-changes-in-rust-v0-156-0.md%0ACard%20ID%3A%20codex-cli-2026-09-22-87ba16%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.156.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->