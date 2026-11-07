---
card_id: codex-cli-2026-10-23-5bc19e
date: '2026-10-23'
description: 'Codex CLI · 2026-10-23 · Agent Mode: 13 changes in 0.164.0 — #53804
  Keep the Agent command center visible during archive and delete @etraut-openai'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1205
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b23ce1021d2c5220e84382c698f074914f8c45abece8fefa255a7cbdec4db591
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-23-5bc19e
  comparison: ''
  date: '2026-10-23'
  description: 'Codex CLI — 0.164.0: 13 Agent Mode changes'
  evidence:
  - quote: '#53804 Keep the Agent command center visible during archive and delete
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53895 Resume unloaded subagent threads when selected in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53908 Keep the agent dashboard browsable during task removal @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54048 Defer folder trust checks until starting a task from agents overview
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54961 Allow agent messages to wake idle root sessions behind a feature
      flag @alishobeiri-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55327 Add configured thread environment inheritance for subagents @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55331 Use step environment snapshots for subagent inheritance @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55375 Add configured thread environment inheritance for subagents @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55398 Add wire types for runtime agent registration @cooper-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55548 Preserve parent history by default in full agent forks @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55644 Make pending injections interrupt agent waits and sleep @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55657 Add lifecycle hooks for inter-agent messages @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55667 Enable app routing for remote curated Agent Plugins @tsarlandie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 13-agent-mode-changes-in-rust-v0-164-0
  source_release: codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d
  source_type: github_releases
  theme: agent-mode
  title: 13 Agent Mode changes in rust-v0.164.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-22-3-agent-mode-changes-in-v2026-10-6|3 Agent Mode changes
  in v2026.10.6]]'
- '[[Changes/OpenHands/2026-10-22-chore-bump-agent-server-to-1-57-0-by-all-hands-bot-in-https-github-com-openhands|chore:
  bump agent-server to 1.57.0]]'
- '[[Changes/Claude Code/2026-10-23-2-agent-mode-changes-in-v2-1-310|2 Agent Mode
  changes in v2.1.310]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d|codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d]]'
source_type: github_releases
theme: agent-mode
title: 13 Agent Mode changes in rust-v0.164.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Agent Mode changes in rust-v0.164.0

**Codex CLI** · 2026-10-23 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.164.0) · from [[Releases/Codex CLI/codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d|0.164.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #53804 Keep the Agent command center visible during archive and delete @etraut-openai

> #53895 Resume unloaded subagent threads when selected in the TUI @etraut-openai

> #53908 Keep the agent dashboard browsable during task removal @etraut-openai

> #54048 Defer folder trust checks until starting a task from agents overview @etraut-openai

> #54961 Allow agent messages to wake idle root sessions behind a feature flag @alishobeiri-oai

> #55327 Add configured thread environment inheritance for subagents @jif-oai

> #55331 Use step environment snapshots for subagent inheritance @jif-oai

> #55375 Add configured thread environment inheritance for subagents @jif-oai

> #55398 Add wire types for runtime agent registration @cooper-oai

> #55548 Preserve parent history by default in full agent forks @jif-oai

> #55644 Make pending injections interrupt agent waits and sleep @jif-oai

> #55657 Add lifecycle hooks for inter-agent messages @euroelessar

> #55667 Enable app routing for remote curated Agent Plugins @tsarlandie-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.164.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-23-24-account-and-access-changes-in-rust-v0-164-0|24 Account and Access changes in rust-v0.164.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-23-2-reliability-and-performance-changes-in-rust-v0-164-0|2 Reliability and Performance changes in rust-v0.164.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-10-23-8-collaboration-changes-in-rust-v0-164-0|8 Collaboration changes in rust-v0.164.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-23-4-memory-and-personalization-changes-in-rust-v0-164-0|4 Memory and Personalization changes in rust-v0.164.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-23-15-safety-and-privacy-changes-in-rust-v0-164-0|15 Safety and Privacy changes in rust-v0.164.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-23-2-image-generation-changes-in-rust-v0-164-0|2 Image Generation changes in rust-v0.164.0]] · Image Generation
- [[Changes/Codex CLI/2026-10-23-8-mobile-and-desktop-changes-in-rust-v0-164-0|8 Mobile and Desktop changes in rust-v0.164.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-23-18-context-window-changes-in-rust-v0-164-0|18 Context Window changes in rust-v0.164.0]] · Context Window
- [[Changes/Codex CLI/2026-10-23-30-apps-and-integrations-changes-in-rust-v0-164-0|30 Apps and Integrations changes in rust-v0.164.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-23-the-amazon-bedrock-setup-wizard-is-now-enabled-by-default-with-api-key-entry-gro|The Amazon Bedrock setup wizard is now enabled by default, with API key entry…]] · Account and Access
- [[Changes/Codex CLI/2026-10-23-9-interface-experience-changes-in-rust-v0-164-0|9 Interface Experience changes in rust-v0.164.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-23-9-model-support-changes-in-rust-v0-164-0|9 Model Support changes in rust-v0.164.0]] · Model Support
- [[Changes/Codex CLI/2026-10-23-14-developer-workflow-changes-in-rust-v0-164-0|14 Developer Workflow changes in rust-v0.164.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-23-3-voice-and-audio-changes-in-rust-v0-164-0|3 Voice and Audio changes in rust-v0.164.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-23-183-other-changes-in-rust-v0-164-0|183 other changes in rust-v0.164.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-23 · Claude Code · [[Changes/Claude Code/2026-10-23-2-agent-mode-changes-in-v2-1-310|2 Agent Mode changes in v2.1.310]]
- Later: 2026-10-23 · Devin · [[Changes/Devin/2026-10-23-choose-your-own-default-agent|Choose Your Own Default Agent]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-23-5bc19e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-23-13-agent-mode-changes-in-rust-v0-164-0.md%0ACard%20ID%3A%20codex-cli-2026-10-23-5bc19e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.164.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->