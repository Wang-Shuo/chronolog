---
card_id: codex-cli-2026-03-19-8be797
date: '2026-03-19'
description: 'Codex CLI · 2026-03-19 · Other changes: 34 changes in 0.116.0 — Added
  a `userpromptsubmit` hook so prompts can be blocked or augmented before execution
  and…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1fb2f3713ea9cce78e020a0b077b59aac6b5849d261cd896e1d595159b43a3e1
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-19-8be797
  comparison: ''
  date: '2026-03-19'
  description: 'Codex CLI — 0.116.0: 34 other changes'
  evidence:
  - quote: Added a `userpromptsubmit` hook so prompts can be blocked or augmented
      before execution and before they enter history. (#14626)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: 'Restored conversation history for remote resume/fork in the app-server
      TUI and stopped duplicate live transcript output from legacy stream events.
      (#14930, #14892)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: Pinned the `setup-zig` GitHub Action to an immutable SHA for more reproducible
      CI. (#14858)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14717 Move TUI on top of app server (parallel code) @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14826 Fixed build failures related to PR 14717 @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14833 fix(core): fix sanitize name to use ''_'' everywhere @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14851 Add exit helper to code mode scripts @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14828 [stack 1/4] Split realtime websocket methods by version @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14652 Apply argument comment lint across codex-rs @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14837 skill-creator: default new skills to ~/.codex/skills @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14830 [stack 2/4] Align main realtime v2 wire and runtime flow @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14886 fix: align marketplace display name with existing interface conventions
      @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14827 [stack 4/4] Reduce realtime self-interruptions during playback
      @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14892 Fix tui_app_server: ignore duplicate legacy stream events @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14899 Revert tui code so it does not rely on in-process app server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14920 feat: centralize package manager version @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14838 fix(core): prevent hanging turn/start due to websocket warming
      issues @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14930 fix(tui): restore remote resume and fork history @fcoury'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14955 Fix fuzzy search notification buffering in app-server tests @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14959 Fix code mode yield startup race @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14434 generate an internal json schema for `RolloutLine` @keyz'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14983 Rename exec_wait tool to wait @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14905 Add auth env observability @ccy-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14977 Cleanup skills/remote/xxx endpoints. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14902 Unify realtime shutdown in core @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14995 app-server: reject websocket requests with Origin headers @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14960 Add FS abstraction and use in view_image @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#13592 Prefer websockets when providers support them @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14903 Handle realtime conversation end in the TUI @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14727 Use workspace requirements for guardian prompt override @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14858 Pin setup-zig GitHub Action to immutable SHA @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14947 feat: adapt artifacts to new packaging and 2.5.6 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14942 Removed remaining core events from tui_app_server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14842 Add notify to code-mode @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 34-other-changes-in-rust-v0-116-0
  source_release: codex-cli-2026-03-19-rust-v0-116-0-github-299083035-eb74e2fd
  source_type: github_releases
  theme: uncategorized
  title: 34 other changes in rust-v0.116.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-19-rust-v0-116-0-github-299083035-eb74e2fd|codex-cli-2026-03-19-rust-v0-116-0-github-299083035-eb74e2fd]]'
source_type: github_releases
theme: uncategorized
title: 34 other changes in rust-v0.116.0
type: change
---

<!-- chronolog:begin region="header" -->
# 34 other changes in rust-v0.116.0

**Codex CLI** · 2026-03-19 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.116.0) · from [[Releases/Codex CLI/codex-cli-2026-03-19-rust-v0-116-0-github-299083035-eb74e2fd|0.116.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a `userpromptsubmit` hook so prompts can be blocked or augmented before execution and before they enter history. (#14626)

> Restored conversation history for remote resume/fork in the app-server TUI and stopped duplicate live transcript output from legacy stream events. (#14930, #14892)

> Pinned the `setup-zig` GitHub Action to an immutable SHA for more reproducible CI. (#14858)

> #14717 Move TUI on top of app server (parallel code) @etraut-openai

> #14826 Fixed build failures related to PR 14717 @etraut-openai

> #14833 fix(core): fix sanitize name to use '_' everywhere @apanasenko-oai

> #14851 Add exit helper to code mode scripts @pakrym-oai

> #14828 [stack 1/4] Split realtime websocket methods by version @aibrahim-oai

> #14652 Apply argument comment lint across codex-rs @bolinfest

> #14837 skill-creator: default new skills to ~/.codex/skills @xl-openai

> #14830 [stack 2/4] Align main realtime v2 wire and runtime flow @aibrahim-oai

> #14886 fix: align marketplace display name with existing interface conventions @xl-openai

> #14827 [stack 4/4] Reduce realtime self-interruptions during playback @aibrahim-oai

> #14892 Fix tui_app_server: ignore duplicate legacy stream events @etraut-openai

> #14899 Revert tui code so it does not rely on in-process app server @etraut-openai

> #14920 feat: centralize package manager version @jif-oai

> #14838 fix(core): prevent hanging turn/start due to websocket warming issues @owenlin0

> #14930 fix(tui): restore remote resume and fork history @fcoury

> #14955 Fix fuzzy search notification buffering in app-server tests @aibrahim-oai

> #14959 Fix code mode yield startup race @aibrahim-oai

> #14434 generate an internal json schema for `RolloutLine` @keyz

> #14983 Rename exec_wait tool to wait @pakrym-oai

> #14905 Add auth env observability @ccy-oai

> #14977 Cleanup skills/remote/xxx endpoints. @xl-openai

> #14902 Unify realtime shutdown in core @aibrahim-oai

> #14995 app-server: reject websocket requests with Origin headers @maxj-oai

> #14960 Add FS abstraction and use in view_image @pakrym-oai

> #13592 Prefer websockets when providers support them @pakrym-oai

> #14903 Handle realtime conversation end in the TUI @aibrahim-oai

> #14727 Use workspace requirements for guardian prompt override @charley-oai

> #14858 Pin setup-zig GitHub Action to immutable SHA @viyatb-oai

> #14947 feat: adapt artifacts to new packaging and 2.5.6 @jif-oai

> #14942 Removed remaining core events from tui_app_server @etraut-openai

> #14842 Add notify to code-mode @pakrym-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.116.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-19-2-model-support-changes-in-rust-v0-116-0|2 Model Support changes in rust-v0.116.0]] · Model Support
- [[Changes/Codex CLI/2026-03-19-10-apps-and-integrations-changes-in-rust-v0-116-0|10 Apps and Integrations changes in rust-v0.116.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-19-2-voice-and-audio-changes-in-rust-v0-116-0|2 Voice and Audio changes in rust-v0.116.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-19-14986-temporarily-disable-private-desktop-until-it-works-with-elevated-ipc-path|♯14986 temporarily disable private desktop until it works with elevated IPC path…]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-19-14829-stack-3-4-add-current-thread-context-to-realtime-startup-aibrahim-oai|♯14829 stack 3/4 Add current thread context to realtime startup @aibrahim-oai]] · Context Window
- [[Changes/Codex CLI/2026-03-19-8-safety-and-privacy-changes-in-rust-v0-116-0|8 Safety and Privacy changes in rust-v0.116.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-19-app-server-tui-now-supports-device-code-chatgpt-sign-in-during-onboarding-and-ca|App-server TUI now supports device-code ChatGPT sign-in during onboarding and can…]] · Account and Access
- [[Changes/Codex CLI/2026-03-19-5-agent-mode-changes-in-rust-v0-116-0|5 Agent Mode changes in rust-v0.116.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-19-2-interface-experience-changes-in-rust-v0-116-0|2 Interface Experience changes in rust-v0.116.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-19-4-memory-and-personalization-changes-in-rust-v0-116-0|4 Memory and Personalization changes in rust-v0.116.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-19-5-developer-workflow-changes-in-rust-v0-116-0|5 Developer Workflow changes in rust-v0.116.0]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-19-8be797&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-19-34-other-changes-in-rust-v0-116-0.md%0ACard%20ID%3A%20codex-cli-2026-03-19-8be797%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.116.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->