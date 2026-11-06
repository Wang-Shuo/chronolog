---
card_id: codex-cli-2026-01-22-215271
date: '2026-01-22'
description: 'Codex CLI · 2026-01-22 · Other changes: 29 changes in 0.89.0 — Added
  a `/skill` UI to enable or disable individual skills. (#9627)'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 040b50ef0f97f776ea9a97d3d23ccea5e1f8a0e4d874fd7b0dc96d6f015abdfc
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-22-215271
  comparison: ''
  date: '2026-01-22'
  description: 'Codex CLI — 0.89.0: 29 other changes'
  evidence:
  - quote: Added a `/skill` UI to enable or disable individual skills. (#9627)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: 'App server now supports `thread/read` and can filter archived threads
      in `thread/list`. (#9569, #9571)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: App server clients now support layered `config.toml` resolution and `config/read`
      can compute effective config from a given cwd. (#9510)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: Release artifacts now include a stable URL for the published config schema.
      (#9572)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: Prevented tilde expansion from escaping HOME on paths like `~//...`. (#9621)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: TUI turn timing now resets between assistant messages so elapsed time reflects
      the latest response. (#9599)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: Refreshed the `skills/list` protocol README example to match the latest
      response shape. (#9623)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9576 [bazel] Upgrade to bazel9 @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9606 nit: ui on interruption @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9621 fix: Fix tilde expansion to avoid absolute-path escape @tiffanycitra'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9623 Update skills/list protocol readme @gverma-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9616 [bazel] Upgrade llvm toolchain and enable remote repo cache @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9633 Add websockets logging @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9592 Chore: update plan mode output in prompt @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9510 Add layered config.toml support to app server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9599 fix(tui) turn timing incremental @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9572 feat: publish config schema on release @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9549 Reduce burst testing flake @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9640 feat(tui): retire the tui2 experiment @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9627 Add UI for skill enable/disable. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9656 Add tui.experimental_mode setting @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9561 feat(tui) /permissions flow @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9653 Fix: Lower log level for closed-channel send @Kbediako'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9659 Chore: add cmd related info to exec approval request @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9693 Revert "feat: support proxy for ws connection" @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9698 Support end_turn flag @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9645 Modes label below textarea @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9569 feat(app-server): thread/read API @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  - quote: '#9571 feat(app-server): support archived threads in thread/list @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.89.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 29-other-changes-in-rust-v0-89-0
  source_release: codex-cli-2026-01-22-rust-v0-89-0-github-279171728-1aea28c3
  source_type: github_releases
  theme: uncategorized
  title: 29 other changes in rust-v0.89.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-22-rust-v0-89-0-github-279171728-1aea28c3|codex-cli-2026-01-22-rust-v0-89-0-github-279171728-1aea28c3]]'
source_type: github_releases
theme: uncategorized
title: 29 other changes in rust-v0.89.0
type: change
---

<!-- chronolog:begin region="header" -->
# 29 other changes in rust-v0.89.0

**Codex CLI** · 2026-01-22 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.89.0) · from [[Releases/Codex CLI/codex-cli-2026-01-22-rust-v0-89-0-github-279171728-1aea28c3|0.89.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a `/skill` UI to enable or disable individual skills. (#9627)

> App server now supports `thread/read` and can filter archived threads in `thread/list`. (#9569, #9571)

> App server clients now support layered `config.toml` resolution and `config/read` can compute effective config from a given cwd. (#9510)

> Release artifacts now include a stable URL for the published config schema. (#9572)

> Prevented tilde expansion from escaping HOME on paths like `~//...`. (#9621)

> TUI turn timing now resets between assistant messages so elapsed time reflects the latest response. (#9599)

> Refreshed the `skills/list` protocol README example to match the latest response shape. (#9623)

> #9576 [bazel] Upgrade to bazel9 @zbarsky-openai

> #9606 nit: ui on interruption @jif-oai

> #9621 fix: Fix tilde expansion to avoid absolute-path escape @tiffanycitra

> #9623 Update skills/list protocol readme @gverma-openai

> #9616 [bazel] Upgrade llvm toolchain and enable remote repo cache @zbarsky-openai

> #9633 Add websockets logging @pakrym-oai

> #9592 Chore: update plan mode output in prompt @shijie-oai

> #9510 Add layered config.toml support to app server @etraut-openai

> #9599 fix(tui) turn timing incremental @dylan-hurd-oai

> #9572 feat: publish config schema on release @sayan-oai

> #9549 Reduce burst testing flake @charley-oai

> #9640 feat(tui): retire the tui2 experiment @joshka-oai

> #9627 Add UI for skill enable/disable. @xl-openai

> #9656 Add tui.experimental_mode setting @pakrym-oai

> #9561 feat(tui) /permissions flow @dylan-hurd-oai

> #9653 Fix: Lower log level for closed-channel send @Kbediako

> #9659 Chore: add cmd related info to exec approval request @shijie-oai

> #9693 Revert "feat: support proxy for ws connection" @pakrym-oai

> #9698 Support end_turn flag @pakrym-oai

> #9645 Modes label below textarea @charley-oai

> #9569 feat(app-server): thread/read API @owenlin0

> #9571 feat(app-server): support archived threads in thread/list @owenlin0

Source: https://github.com/openai/codex/releases/tag/rust-v0.89.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-22-improved-slash-command-selection-by-prioritizing-exact-and-prefix-matches-over-f|Improved slash-command selection by prioritizing exact and prefix matches over fuzzy…]] · Interface Experience
- [[Changes/Codex CLI/2026-01-22-9650-chore-tweak-agents-md-dylan-hurd-oai|♯9650 chore: tweak AGENTS.md @dylan-hurd-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-01-22-2-apps-and-integrations-changes-in-rust-v0-89-0|2 Apps and Integrations changes in rust-v0.89.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-22-2-safety-and-privacy-changes-in-rust-v0-89-0|2 Safety and Privacy changes in rust-v0.89.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-22-9644-feat-core-update-personality-on-turn-dylan-hurd-oai|♯9644 feat(core) update Personality on turn @dylan-hurd-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-01-22-4-developer-workflow-changes-in-rust-v0-89-0|4 Developer Workflow changes in rust-v0.89.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-22-9597-feat-core-modelinfo-model-instructions-template-dylan-hurd-oai|♯9597 feat(core) ModelInfo.model_instructions_template @dylan-hurd-oai]] · Model Support
- [[Changes/Codex CLI/2026-01-22-9583-add-collaboration-mode-to-turncontextitem-charley-oai|♯9583 Add collaboration_mode to TurnContextItem @charley-oai]] · Collaboration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-22-215271&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-22-29-other-changes-in-rust-v0-89-0.md%0ACard%20ID%3A%20codex-cli-2026-01-22-215271%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.89.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->