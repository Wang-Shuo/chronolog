---
card_id: codex-cli-2026-04-10-333272
date: '2026-04-10'
description: 'Codex CLI · 2026-04-10 · Agent Mode: 13 changes in 0.119.0 — The TUI
  can copy the latest agent response with `Ctrl+O`, including better clipboard behavior
  over…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1009
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 047ca12c81dd659f730315d2886e5cd21a79bb103f456d3fbc7a03486fe16cae
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-10-333272
  comparison: ''
  date: '2026-04-10'
  description: 'Codex CLI — 0.119.0: 13 Agent Mode changes'
  evidence:
  - quote: The TUI can copy the latest agent response with `Ctrl+O`, including better
      clipboard behavior over SSH and across platforms (#16966).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16325 feat: restrict spawn_agent v2 to messages @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16406 Use message string in v2 spawn_agent @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16424 feat: tasks can''t be assigned to root agent @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16375 docs: update argument_comment_lint instructions in AGENTS.md @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#15915 [codex-analytics] subagent analytics @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16876 [codex] add response proxy subagent header test @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#15826 Make AGENTS.md discovery FS-aware @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17005 feat: drop agent ID from v2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17009 chore: keep request_user_input tool to persist cache on multi-agents
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16739 Stabilize flaky multi-agent followup interrupt test @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17071 Configure multi_agent_v2 spawn agent hints @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17091 Show global AGENTS.md in /status @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 13-agent-mode-changes-in-rust-v0-119-0
  source_release: codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1
  source_type: github_releases
  theme: agent-mode
  title: 13 Agent Mode changes in rust-v0.119.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-09-3-agent-mode-changes-in-v2-1-98|3 Agent Mode changes
  in v2.1.98]]'
- '[[Changes/GitHub Copilot CLI/2026-04-09-3-agent-mode-changes-in-v1-0-22|3 Agent
  Mode changes in v1.0.22]]'
- '[[Changes/Claude Code/2026-04-10-ultraplan-and-other-remote-session-features-now-auto-create-a-default-cloud-envi|/ultraplan
  and other remote-session features now auto-create a default cloud…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1|codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1]]'
source_type: github_releases
theme: agent-mode
title: 13 Agent Mode changes in rust-v0.119.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Agent Mode changes in rust-v0.119.0

**Codex CLI** · 2026-04-10 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.119.0) · from [[Releases/Codex CLI/codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1|0.119.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The TUI can copy the latest agent response with `Ctrl+O`, including better clipboard behavior over SSH and across platforms (#16966).

> #16325 feat: restrict spawn_agent v2 to messages @jif-oai

> #16406 Use message string in v2 spawn_agent @jif-oai

> #16424 feat: tasks can't be assigned to root agent @jif-oai

> #16375 docs: update argument_comment_lint instructions in AGENTS.md @bolinfest

> #15915 [codex-analytics] subagent analytics @rhan-oai

> #16876 [codex] add response proxy subagent header test @tibo-openai

> #15826 Make AGENTS.md discovery FS-aware @pakrym-oai

> #17005 feat: drop agent ID from v2 @jif-oai

> #17009 chore: keep request_user_input tool to persist cache on multi-agents @jif-oai

> #16739 Stabilize flaky multi-agent followup interrupt test @etraut-openai

> #17071 Configure multi_agent_v2 spawn agent hints @pakrym-oai

> #17091 Show global AGENTS.md in /status @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.119.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-10-4-context-window-changes-in-rust-v0-119-0|4 Context Window changes in rust-v0.119.0]] · Context Window
- [[Changes/Codex CLI/2026-04-10-8-safety-and-privacy-changes-in-rust-v0-119-0|8 Safety and Privacy changes in rust-v0.119.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-10-28-developer-workflow-changes-in-rust-v0-119-0|28 Developer Workflow changes in rust-v0.119.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-10-2-memory-and-personalization-changes-in-rust-v0-119-0|2 Memory and Personalization changes in rust-v0.119.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-10-the-readme-now-uses-the-current-chatgpt-business-plan-name-16348|The README now uses the current ChatGPT Business plan name (♯16348)]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-04-10-3-voice-and-audio-changes-in-rust-v0-119-0|3 Voice and Audio changes in rust-v0.119.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-04-10-19-apps-and-integrations-changes-in-rust-v0-119-0|19 Apps and Integrations changes in rust-v0.119.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-10-2-account-and-access-changes-in-rust-v0-119-0|2 Account and Access changes in rust-v0.119.0]] · Account and Access
- [[Changes/Codex CLI/2026-04-10-17256-app-server-use-shared-receivers-for-app-server-message-processors-euroeles|♯17256 app-server: Use shared receivers for app-server message processors @euroelessar]] · Collaboration
- [[Changes/Codex CLI/2026-04-10-10-interface-experience-changes-in-rust-v0-119-0|10 Interface Experience changes in rust-v0.119.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-10-16202-fix-paste-driven-bottom-pane-completion-teardown-etraut-openai|♯16202 Fix paste-driven bottom pane completion teardown @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-04-10-2-reliability-and-performance-changes-in-rust-v0-119-0|2 Reliability and Performance changes in rust-v0.119.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-10-5-model-support-changes-in-rust-v0-119-0|5 Model Support changes in rust-v0.119.0]] · Model Support
- [[Changes/Codex CLI/2026-04-10-6-mobile-and-desktop-changes-in-rust-v0-119-0|6 Mobile and Desktop changes in rust-v0.119.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-10-187-other-changes-in-rust-v0-119-0|187 other changes in rust-v0.119.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-10 · Claude Code · [[Changes/Claude Code/2026-04-10-ultraplan-and-other-remote-session-features-now-auto-create-a-default-cloud-envi|/ultraplan and other remote-session features now auto-create a default cloud…]]
- Later: 2026-04-10 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-10-add-mode-autopilot-and-plan-flags-to-start-the-cli-directly-in-a-specific-agent|Add --mode, --autopilot, and --plan flags to start the CLI directly in a specific…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-10-333272&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-10-13-agent-mode-changes-in-rust-v0-119-0.md%0ACard%20ID%3A%20codex-cli-2026-04-10-333272%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.119.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->