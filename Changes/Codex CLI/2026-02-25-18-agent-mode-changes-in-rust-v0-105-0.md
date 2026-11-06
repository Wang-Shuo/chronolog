---
card_id: codex-cli-2026-02-25-14044c
date: '2026-02-25'
description: 'Codex CLI · 2026-02-25 · Agent Mode: 18 changes in 0.105.0 — Multi-agent
  workflows are easier to run and track: `spawn_agents_on_csv` can fan out work from
  a…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 965
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9d333387eeb0b935b9a40fe69d2410f1d7a3c0ffc76bbafb79bab69864ef139e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-25-14044c
  comparison: ''
  date: '2026-02-25'
  description: 'Codex CLI — 0.105.0: 18 Agent Mode changes'
  evidence:
  - quote: 'Multi-agent workflows are easier to run and track: `spawn_agents_on_csv`
      can fan out work from a CSV with built-in progress/ETA, and sub-agents are easier
      to follow with nicknames, a cleaner picker, and visible child-thread approval
      prompts. (#10935, #12320, #12327, #12332, #12570, #12767)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12072 Add message phase to agent message thread item @mousseau-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12133 feat: validate agent config file paths @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12152 feat: sub-agent injection @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12251 Add configurable agent spawn depth @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12320 feat: add nick name to sub-agents @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12328 chore: better agent names @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12327 feat: cleaner TUI for sub-agents @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12474 fix: make skills loader tests hermetic with ~/.agents skills @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12570 feat: keep dead agents in the agent picker @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12575 feat: agent nick names to model @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12579 feat: role metrics multi-agent @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12667 feat: mutli agents persist config overrides @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12663 fix: replay after `/agent` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12697 Ensure shell command skills trigger approval @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12639 Honor `project_root_markers` when discovering `AGENTS.md` @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#10935 Agent jobs (spawn_agents_on_csv) + progress UI @daveaitel-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12660 Support external agent config detect and import @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 18-agent-mode-changes-in-rust-v0-105-0
  source_release: codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed
  source_type: github_releases
  theme: agent-mode
  title: 18 Agent Mode changes in rust-v0.105.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-02-23-2-agent-mode-changes-in-v0-0-415|2 Agent
  Mode changes in v0.0.415]]'
- '[[Changes/Cline/2026-02-24-3-agent-mode-changes-in-v3-67-0|3 Agent Mode changes
  in v3.67.0]]'
- '[[Changes/Cursor/2026-02-24-cloud-agents-can-now-use-the-software-they-create-to-test-changes-and-demo-their-c922e9|Cloud
  Agents with Computer Use]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed|codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed]]'
source_type: github_releases
theme: agent-mode
title: 18 Agent Mode changes in rust-v0.105.0
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Agent Mode changes in rust-v0.105.0

**Codex CLI** · 2026-02-25 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.105.0) · from [[Releases/Codex CLI/codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed|0.105.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Multi-agent workflows are easier to run and track: `spawn_agents_on_csv` can fan out work from a CSV with built-in progress/ETA, and sub-agents are easier to follow with nicknames, a cleaner picker, and visible child-thread approval prompts. (#10935, #12320, #12327, #12332, #12570, #12767)

> #12072 Add message phase to agent message thread item @mousseau-oai

> #12133 feat: validate agent config file paths @jif-oai

> #12152 feat: sub-agent injection @jif-oai

> #12251 Add configurable agent spawn depth @jif-oai

> #12320 feat: add nick name to sub-agents @jif-oai

> #12328 chore: better agent names @jif-oai

> #12327 feat: cleaner TUI for sub-agents @jif-oai

> #12474 fix: make skills loader tests hermetic with ~/.agents skills @bolinfest

> #12570 feat: keep dead agents in the agent picker @jif-oai

> #12575 feat: agent nick names to model @jif-oai

> #12579 feat: role metrics multi-agent @jif-oai

> #12667 feat: mutli agents persist config overrides @jif-oai

> #12663 fix: replay after `/agent` @jif-oai

> #12697 Ensure shell command skills trigger approval @pakrym-oai

> #12639 Honor `project_root_markers` when discovering `AGENTS.md` @etraut-openai

> #10935 Agent jobs (spawn_agents_on_csv) + progress UI @daveaitel-openai

> #12660 Support external agent config detect and import @alexsong-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.105.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-25-13-apps-and-integrations-changes-in-rust-v0-105-0|13 Apps and Integrations changes in rust-v0.105.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-25-15-developer-workflow-changes-in-rust-v0-105-0|15 Developer Workflow changes in rust-v0.105.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-25-12028-remove-feature-flag-collaboration-modes-aibrahim-oai|♯12028 remove feature flag collaboration modes @aibrahim-oai]] · Collaboration
- [[Changes/Codex CLI/2026-02-25-9-memory-and-personalization-changes-in-rust-v0-105-0|9 Memory and Personalization changes in rust-v0.105.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-25-3-reliability-and-performance-changes-in-rust-v0-105-0|3 Reliability and Performance changes in rust-v0.105.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-02-25-you-can-now-dictate-prompts-by-holding-the-spacebar-to-record-and-transcribe-voi|Dictate prompts by holding the spacebar to record and transcribe voice input…]] · Voice and Audio
- [[Changes/Codex CLI/2026-02-25-3-account-and-access-changes-in-rust-v0-105-0|3 Account and Access changes in rust-v0.105.0]] · Account and Access
- [[Changes/Codex CLI/2026-02-25-8-interface-experience-changes-in-rust-v0-105-0|8 Interface Experience changes in rust-v0.105.0]] · Interface Experience
- [[Changes/Codex CLI/2026-02-25-2-editor-experience-changes-in-rust-v0-105-0|2 Editor Experience changes in rust-v0.105.0]] · Editor Experience
- [[Changes/Codex CLI/2026-02-25-9-safety-and-privacy-changes-in-rust-v0-105-0|9 Safety and Privacy changes in rust-v0.105.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-25-5-context-window-changes-in-rust-v0-105-0|5 Context Window changes in rust-v0.105.0]] · Context Window
- [[Changes/Codex CLI/2026-02-25-6-model-support-changes-in-rust-v0-105-0|6 Model Support changes in rust-v0.105.0]] · Model Support
- [[Changes/Codex CLI/2026-02-25-2-mobile-and-desktop-changes-in-rust-v0-105-0|2 Mobile and Desktop changes in rust-v0.105.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-25-2-voice-and-audio-changes-in-rust-v0-105-0|2 Voice and Audio changes in rust-v0.105.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-02-25-156-other-changes-in-rust-v0-105-0|156 other changes in rust-v0.105.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-02-24 · Cursor · [[Changes/Cursor/2026-02-24-cloud-agents-can-now-use-the-software-they-create-to-test-changes-and-demo-their-c922e9|Cloud Agents with Computer Use]]
- Later: 2026-02-25 · Gemini CLI · [[Changes/Gemini CLI/2026-02-25-4-agent-mode-changes-in-v0-30-0|4 Agent Mode changes in v0.30.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-25-14044c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-25-18-agent-mode-changes-in-rust-v0-105-0.md%0ACard%20ID%3A%20codex-cli-2026-02-25-14044c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.105.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->