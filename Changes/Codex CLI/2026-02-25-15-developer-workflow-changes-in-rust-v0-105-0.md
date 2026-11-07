---
card_id: codex-cli-2026-02-25-274ba7
date: '2026-02-25'
description: 'Codex CLI · 2026-02-25 · Developer Workflow: 15 changes in 0.105.0 —
  #12233 feat: add shell snapshot failure reason @jif-oai'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2724
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4cafe40efd2b4f38a2fe7403f34391f6321cd6469e8c1208b63e2cc6a28bb88d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-25-274ba7
  comparison: ''
  date: '2026-02-25'
  description: 'Codex CLI — 0.105.0: 15 Developer Workflow changes'
  evidence:
  - quote: '#12233 feat: add shell snapshot failure reason @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12432 chore: remove codex-core public protocol/shell re-exports @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12476 Make shell detection tests'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: robust to Nix shell paths @rupurt
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12541 Allow exec resume to parse output-last-message flag after command
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12520 tweaked /clear to support clear + new chat, also fix minor bug
      for macos terminal @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12556 refactor: normalize unix module layout for exec-server and shell-escalation
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12549 fix: show command running in background terminal in details under
      status indicator @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12632 refactor: delete exec-server and move execve wrapper into shell-escalation
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12638 refactor: decouple shell-escalation from codex-core @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12628 ctrl-L (clears terminal but does not start a new chat) @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12649 feat: run zsh fork shell tool via shell-escalation @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12724 fix: make EscalateServer public and remove shell escalation wrappers
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12737 feat: add experimental additionalPermissions to v2 command execution
      approval requests @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12750 fix: keep shell escalation exec paths absolute @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 15-developer-workflow-changes-in-rust-v0-105-0
  source_release: codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed
  source_type: github_releases
  theme: developer-workflow
  title: 15 Developer Workflow changes in rust-v0.105.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-02-24-status-line-automatically-switches-to-a-two-line-layout-on-narrow-terminals-keep|Status
  line automatically switches to a two-line layout on narrow terminals, keeping…]]'
- '[[Changes/OpenCode/2026-02-24-add-workspace-serve-command-experimental|Add workspace-serve
  command (experimental)]]'
- '[[Changes/OpenCode/2026-02-24-3-developer-workflow-changes-in-v1-2-11|3 Developer
  Workflow changes in v1.2.11]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed|codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed]]'
source_type: github_releases
theme: developer-workflow
title: 15 Developer Workflow changes in rust-v0.105.0
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Developer Workflow changes in rust-v0.105.0

**Codex CLI** · 2026-02-25 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.105.0) · from [[Releases/Codex CLI/codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed|0.105.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #12233 feat: add shell snapshot failure reason @jif-oai

> #12432 chore: remove codex-core public protocol/shell re-exports @bolinfest

> #12476 Make shell detection tests

> robust to Nix shell paths @rupurt

> #12541 Allow exec resume to parse output-last-message flag after command @etraut-openai

> #12520 tweaked /clear to support clear + new chat, also fix minor bug for macos terminal @won-openai

> #12556 refactor: normalize unix module layout for exec-server and shell-escalation @bolinfest

> #12549 fix: show command running in background terminal in details under status indicator @sayan-oai

> #12632 refactor: delete exec-server and move execve wrapper into shell-escalation @bolinfest

> #12638 refactor: decouple shell-escalation from codex-core @bolinfest

> #12628 ctrl-L (clears terminal but does not start a new chat) @won-openai

> #12649 feat: run zsh fork shell tool via shell-escalation @bolinfest

> #12724 fix: make EscalateServer public and remove shell escalation wrappers @bolinfest

> #12737 feat: add experimental additionalPermissions to v2 command execution approval requests @celia-oai

> #12750 fix: keep shell escalation exec paths absolute @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.105.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-25-13-apps-and-integrations-changes-in-rust-v0-105-0|13 Apps and Integrations changes in rust-v0.105.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-25-18-agent-mode-changes-in-rust-v0-105-0|18 Agent Mode changes in rust-v0.105.0]] · Agent Mode
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
## Nearby in Developer Workflow

- Earlier: 2026-02-24 · OpenCode · [[Changes/OpenCode/2026-02-24-3-developer-workflow-changes-in-v1-2-11|3 Developer Workflow changes in v1.2.11]]
- Later: 2026-02-25 · Gemini CLI · [[Changes/Gemini CLI/2026-02-25-3-developer-workflow-changes-in-v0-30-0|3 Developer Workflow changes in v0.30.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-25-274ba7&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-25-15-developer-workflow-changes-in-rust-v0-105-0.md%0ACard%20ID%3A%20codex-cli-2026-02-25-274ba7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.105.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->