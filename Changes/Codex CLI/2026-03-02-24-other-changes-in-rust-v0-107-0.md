---
card_id: codex-cli-2026-03-02-5a8f2f
date: '2026-03-02'
description: 'Codex CLI · 2026-03-02 · Other changes: 24 changes in 0.107.0 — Reconnecting
  with `thread/resume` now restores pending approval and input requests instead of…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 090c298e333ef8acca1321d1628029eb352cab9fbcc61e9f4e1e45ad64fe4028
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-02-5a8f2f
  comparison: ''
  date: '2026-03-02'
  description: 'Codex CLI — 0.107.0: 24 other changes'
  evidence:
  - quote: Reconnecting with `thread/resume` now restores pending approval and input
      requests instead of leaving clients out of sync. (#12560)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12925 chore: calm down awaiter @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12837 Log js_repl nested tool responses in rollout history @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12929 Remove noisy log @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12727 tui: use thread_id for resume/fork cwd resolution @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12950 Allow clients not to send summary as an option @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12944 fix: sort codex features list alphabetically @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12957 test: move unix_escalation tests into sibling file @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12936 Add a background job to refresh the requirements local cache @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12981 Add realtime websocket tracing @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12968 notify: include client in legacy hook payload @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#13001 chore: tmp remove awaiter @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#13011 fix: more stable notify script @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#13047 app-server: deflake running thread resume tests @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12560 app-server: Replay pending item requests on `thread/resume` @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#13055 fix: disable Bazel builds in CI on ubuntu-24.04-arm until we can
      stabilize them @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12964 execpolicy: add host_executable() path mappings @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12612 Unify rollout reconstruction with resume/fork TurnContext hydration
      @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#13072 Handle missing plan info for ChatGPT accounts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#13080 app-server: Add an ability to watch events in the test client @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#13082 Suppress duplicate assistant output on stdout in interactive sessions
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#13033 fix(app-server): make thread/start non-blocking @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#13046 core: adopt host_executable() rules in zsh-fork @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#13084 app-server: Add `ephemeral` field to `Thread` object @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 24-other-changes-in-rust-v0-107-0
  source_release: codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f
  source_type: github_releases
  theme: uncategorized
  title: 24 other changes in rust-v0.107.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f|codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f]]'
source_type: github_releases
theme: uncategorized
title: 24 other changes in rust-v0.107.0
type: change
---

<!-- chronolog:begin region="header" -->
# 24 other changes in rust-v0.107.0

**Codex CLI** · 2026-03-02 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.107.0) · from [[Releases/Codex CLI/codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f|0.107.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Reconnecting with `thread/resume` now restores pending approval and input requests instead of leaving clients out of sync. (#12560)

> #12925 chore: calm down awaiter @jif-oai

> #12837 Log js_repl nested tool responses in rollout history @fjord-oai

> #12929 Remove noisy log @pakrym-oai

> #12727 tui: use thread_id for resume/fork cwd resolution @charley-oai

> #12950 Allow clients not to send summary as an option @pakrym-oai

> #12944 fix: sort codex features list alphabetically @bolinfest

> #12957 test: move unix_escalation tests into sibling file @bolinfest

> #12936 Add a background job to refresh the requirements local cache @alexsong-oai

> #12981 Add realtime websocket tracing @aibrahim-oai

> #12968 notify: include client in legacy hook payload @bolinfest

> #13001 chore: tmp remove awaiter @jif-oai

> #13011 fix: more stable notify script @jif-oai

> #13047 app-server: deflake running thread resume tests @bolinfest

> #12560 app-server: Replay pending item requests on `thread/resume` @euroelessar

> #13055 fix: disable Bazel builds in CI on ubuntu-24.04-arm until we can stabilize them @bolinfest

> #12964 execpolicy: add host_executable() path mappings @bolinfest

> #12612 Unify rollout reconstruction with resume/fork TurnContext hydration @charley-oai

> #13072 Handle missing plan info for ChatGPT accounts @etraut-openai

> #13080 app-server: Add an ability to watch events in the test client @euroelessar

> #13082 Suppress duplicate assistant output on stdout in interactive sessions @etraut-openai

> #13033 fix(app-server): make thread/start non-blocking @owenlin0

> #13046 core: adopt host_executable() rules in zsh-fork @bolinfest

> #13084 app-server: Add `ephemeral` field to `Thread` object @euroelessar

Source: https://github.com/openai/codex/releases/tag/rust-v0.107.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-02-2-multimodal-input-changes-in-rust-v0-107-0|2 Multimodal Input changes in rust-v0.107.0]] · Multimodal Input
- [[Changes/Codex CLI/2026-03-02-you-can-now-fork-a-thread-into-sub-agents-making-it-easier-to-branch-work-withou|Fork a thread into sub-agents, making it easier to branch work without leaving…]] · Agent Mode
- [[Changes/Codex CLI/2026-03-02-3-apps-and-integrations-changes-in-rust-v0-107-0|3 Apps and Integrations changes in rust-v0.107.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-02-3-account-and-access-changes-in-rust-v0-107-0|3 Account and Access changes in rust-v0.107.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-02-3-developer-workflow-changes-in-rust-v0-107-0|3 Developer Workflow changes in rust-v0.107.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-02-12947-feat-add-local-date-timezone-to-turn-environment-context-celia-oai|♯12947 feat: add local date/timezone to turn environment context @celia-oai]] · Context Window
- [[Changes/Codex CLI/2026-03-02-2-agent-mode-changes-in-rust-v0-107-0|2 Agent Mode changes in rust-v0.107.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-02-4-model-support-changes-in-rust-v0-107-0|4 Model Support changes in rust-v0.107.0]] · Model Support
- [[Changes/Codex CLI/2026-03-02-3-editor-experience-changes-in-rust-v0-107-0|3 Editor Experience changes in rust-v0.107.0]] · Editor Experience
- [[Changes/Codex CLI/2026-03-02-6-memory-and-personalization-changes-in-rust-v0-107-0|6 Memory and Personalization changes in rust-v0.107.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-02-5-voice-and-audio-changes-in-rust-v0-107-0|5 Voice and Audio changes in rust-v0.107.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-02-8-safety-and-privacy-changes-in-rust-v0-107-0|8 Safety and Privacy changes in rust-v0.107.0]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-02-5a8f2f&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-02-24-other-changes-in-rust-v0-107-0.md%0ACard%20ID%3A%20codex-cli-2026-03-02-5a8f2f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.107.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->