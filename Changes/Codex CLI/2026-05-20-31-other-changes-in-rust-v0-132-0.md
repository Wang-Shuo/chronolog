---
card_id: codex-cli-2026-05-20-243c39
date: '2026-05-20'
description: 'Codex CLI · 2026-05-20 · Other changes: 31 changes in 0.132.0 — Python
  turn APIs are easier to use for text-only workflows: you can pass a plain string
  as…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 42fd5038f783853ce9f04d0322b660940cffa2a080ca0c6742ad9d74c63311ab
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-20-243c39
  comparison: ''
  date: '2026-05-20'
  description: 'Codex CLI — 0.132.0: 31 other changes'
  evidence:
  - quote: 'Python turn APIs are easier to use for text-only workflows: you can pass
      a plain string as input, and handle-based runs now return a richer `TurnResult`
      with collected items, timing, and usage data. (#23151, #23162)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: Remote executor registration can now use standard Codex auth instead of
      a separate registry credential flow. (#22769)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: App-server turns can preserve requested image fidelity, including original-resolution
      local images, across user inputs and image-producing tools. (#20693)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: 'TUI polish fixes include immediate shutdown feedback on exit, hiding the
      ChatGPT usage link for non-OpenAI providers, and keeping a cleared Fast tier
      from reappearing after side-thread resume. (#23323, #23127, #23121)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#20693 Preserve image detail in app-server inputs @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#22924 app-server-protocol: remove PermissionProfile from API @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#22967 Fix Windows doctor npm root probe @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#22769 exec-server: support auth-backed remote executor registration @miz-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#22913 [1 of 4] tui: route primary settings writes through app server
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23151 [codex] Return TurnResult from Python turn handles @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23162 [codex] Accept string input for Python turns @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23226 Add exec-server websocket keepalive @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23288 chore: goal ext skeleton @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23293 feat: add extension event sink capability @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23295 chore: isolate thread goal storage behind GoalStore @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23301 chore: goal resumed metrics @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23305 chore: make token usage async @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23306 Emit goal update events from goal extension tools @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23121 tui: keep cleared Fast tier from reappearing after side-thread
      resume @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23123 Support --output-schema for exec resume @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23128 Fix TUI stream cleanup after turn errors @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23127 Hide ChatGPT usage link for non-OpenAI status @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23332 nit: read prompt @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#22905 windows: link MSVC release binaries with static CRT @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23323 fix(tui): show shutdown feedback on exit @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23273 Upload rust full CI JUnit reports @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23094 goal: pause continuation loops on usage limits and blockers @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23234 Clarify resume hints for renamed threads @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23241 TUI: route elicitation responses to request thread @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23088 goals: keep pause transitions explicit @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23335 feat(app-server): add optional thread_id to experimentalFeature/list
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 31-other-changes-in-rust-v0-132-0
  source_release: codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4
  source_type: github_releases
  theme: uncategorized
  title: 31 other changes in rust-v0.132.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4|codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4]]'
source_type: github_releases
theme: uncategorized
title: 31 other changes in rust-v0.132.0
type: change
---

<!-- chronolog:begin region="header" -->
# 31 other changes in rust-v0.132.0

**Codex CLI** · 2026-05-20 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.132.0) · from [[Releases/Codex CLI/codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4|0.132.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Python turn APIs are easier to use for text-only workflows: you can pass a plain string as input, and handle-based runs now return a richer `TurnResult` with collected items, timing, and usage data. (#23151, #23162)

> Remote executor registration can now use standard Codex auth instead of a separate registry credential flow. (#22769)

> App-server turns can preserve requested image fidelity, including original-resolution local images, across user inputs and image-producing tools. (#20693)

> TUI polish fixes include immediate shutdown feedback on exit, hiding the ChatGPT usage link for non-OpenAI providers, and keeping a cleared Fast tier from reappearing after side-thread resume. (#23323, #23127, #23121)

> #20693 Preserve image detail in app-server inputs @fjord-oai

> #22924 app-server-protocol: remove PermissionProfile from API @bolinfest

> #22967 Fix Windows doctor npm root probe @etraut-openai

> #22769 exec-server: support auth-backed remote executor registration @miz-openai

> #22913 [1 of 4] tui: route primary settings writes through app server @etraut-openai

> #23151 [codex] Return TurnResult from Python turn handles @aibrahim-oai

> #23162 [codex] Accept string input for Python turns @aibrahim-oai

> #23226 Add exec-server websocket keepalive @starr-openai

> #23288 chore: goal ext skeleton @jif-oai

> #23293 feat: add extension event sink capability @jif-oai

> #23295 chore: isolate thread goal storage behind GoalStore @jif-oai

> #23301 chore: goal resumed metrics @jif-oai

> #23305 chore: make token usage async @jif-oai

> #23306 Emit goal update events from goal extension tools @jif-oai

> #23121 tui: keep cleared Fast tier from reappearing after side-thread resume @etraut-openai

> #23123 Support --output-schema for exec resume @etraut-openai

> #23128 Fix TUI stream cleanup after turn errors @etraut-openai

> #23127 Hide ChatGPT usage link for non-OpenAI status @etraut-openai

> #23332 nit: read prompt @jif-oai

> #22905 windows: link MSVC release binaries with static CRT @iceweasel-oai

> #23323 fix(tui): show shutdown feedback on exit @fcoury-oai

> #23273 Upload rust full CI JUnit reports @starr-openai

> #23094 goal: pause continuation loops on usage limits and blockers @etraut-openai

> #23234 Clarify resume hints for renamed threads @etraut-openai

> #23241 TUI: route elicitation responses to request thread @etraut-openai

> #23088 goals: keep pause transitions explicit @etraut-openai

> #23335 feat(app-server): add optional thread_id to experimentalFeature/list @owenlin0

Source: https://github.com/openai/codex/releases/tag/rust-v0.132.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-20-3-interface-experience-changes-in-rust-v0-132-0|3 Interface Experience changes in rust-v0.132.0]] · Interface Experience
- [[Changes/Codex CLI/2026-05-20-5-safety-and-privacy-changes-in-rust-v0-132-0|5 Safety and Privacy changes in rust-v0.132.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-20-codex-exec-resume-now-accepts-output-schema-so-resumed-automations-can-keep-sess|codex exec resume now accepts --output-schema, so resumed automations can keep…]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-05-20-23069-multiagent-trim-model-visible-description-cap-to-5-models-sayan-oai|♯23069 multiagent: trim model-visible description, cap to 5 models @sayan-oai]] · Model Support
- [[Changes/Codex CLI/2026-05-20-windows-installs-are-more-robust-codex-doctor-now-detects-npm-managed-installs-c|Windows installs are more robust]] · Reliability and Performance
- [[Changes/Codex CLI/2026-05-20-9-apps-and-integrations-changes-in-rust-v0-132-0|9 Apps and Integrations changes in rust-v0.132.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-20-2-account-and-access-changes-in-rust-v0-132-0|2 Account and Access changes in rust-v0.132.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-20-3-developer-workflow-changes-in-rust-v0-132-0|3 Developer Workflow changes in rust-v0.132.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-20-2-memory-and-personalization-changes-in-rust-v0-132-0|2 Memory and Personalization changes in rust-v0.132.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-20-23147-make-multi-agent-v2-tool-namespace-configurable-jif-oai|♯23147 Make multi-agent v2 tool namespace configurable @jif-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-05-20-3-editor-experience-changes-in-rust-v0-132-0|3 Editor Experience changes in rust-v0.132.0]] · Editor Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-20-243c39&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-20-31-other-changes-in-rust-v0-132-0.md%0ACard%20ID%3A%20codex-cli-2026-05-20-243c39%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.132.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->