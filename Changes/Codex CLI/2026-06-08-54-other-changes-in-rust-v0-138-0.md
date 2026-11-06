---
card_id: codex-cli-2026-06-08-a61246
date: '2026-06-08'
description: 'Codex CLI · 2026-06-08 · Other changes: 54 changes in 0.138.0 — App-server
  integrations can now read account token usage, and Codex auth supports v2 personal…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a34c396c991f8bbc419a862911e92b4ed65606846584b6bd08e4665572065929
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-08-a61246
  comparison: ''
  date: '2026-06-08'
  description: 'Codex CLI — 0.138.0: 54 other changes'
  evidence:
  - quote: 'App-server integrations can now read account token usage, and Codex auth
      supports v2 personal access tokens in CLI and app-server flows. (#25344, #25731)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: Forked threads now keep user-renamed titles instead of falling back to
      the original first-prompt name. (#26075)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: 'The TUI no longer adds extra blank space while streaming, and cancelled
      prompts reopen with the cursor at the end so you can keep editing naturally.
      (#26636, #26457)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: TUI config write failures now show the underlying cause, making validation
      problems and read-only filesystem issues much easier to diagnose. (#26537)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: The CLI README was refreshed to remove stale guidance and better match
      the current documentation flow. (#26313)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '`resume --last` now finds the newest matching session through the state
      DB first, which speeds up restore on large local histories. (#26462)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26179 nit: small prompt update for MAv2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#25700 core: stop threading SandboxPolicy through exec @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#25925 [codex] Copy user Bazel settings into Codex worktrees @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#25469 [profile-switcher][rust] -- [1/2] Add app-server account session
      protocol @dhruvgupta-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26075 Fix forked thread name inheritance @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26226 [codex] Split Python runtime release workflow @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26260 codex-pr-body: avoid confidential references @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26367 chore: calm down @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26147 Gate automatic idle turns in Plan mode @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26172 Bridge host-loaded skills into the skills extension @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26265 Optimize unbounded byte scans with memchr @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26313 Simplify Codex CLI README @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26436 app-server: support -c config overrides @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26248 [codex-analytics] emit forked thread id on initialization @kbazzi'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26320 core: allow excluding tool namespaces from code mode @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#25945 Use Azure artifact signing environment secrets @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#23710 build: use ThinLTO for release binaries @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26447 Remove response.processed websocket request @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26312 Cleanup experimentalFeature/enablement/set @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26466 Use Winget release environment secret @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26473 Add skill for pushing CI configuration changes @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#25000 ci: test windows cross build @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26487 [codex] Add use_responses_lite ''override'' logic @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26256 [codex] Keep Bazel startup options stable across commands @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26499 core: derive exec policy filesystem policy from profile @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26566 nit: doc @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#25710 [codex] Forward turn moderation metadata through app-server @carlc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26599 [codex] Keep v1 spawn metadata visible @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#25344 feat(app-server): expose account token usage [1 of 2] @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26553 [codex] Fix long proxy socket paths @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26537 Surface TUI config write error causes @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26551 Fix `/goal` usage text for control commands @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26554 Render code comment directives in TUI replay @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26532 Require absolute cwd in thread settings @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26636 fix(tui): avoid doubled blank rows while streaming @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26335 Clean up Rust release workflow @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26547 [1 of 2] Align goal extension with core behavior @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26181 fix(tui): Windows composer background @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26457 fix(tui): restore cancelled prompt cursor at end @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26484 [codex] Add turn profiling analytics @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26552 Make runtime workspace roots absolute in app-server API @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26462 Use state DB first for `resume --last` @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26548 [2 of 2] Finish moving goal runtime to extension @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26674 protocol: remove submission-side serde from Op @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26490 [codex] Use standalone tools for Responses Lite @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26542 [codex] Send Responses Lite transport header @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26698 [codex] Deduplicate skill load warnings @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26716 Remove `just bench-smoke` from `just test`. @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 54-other-changes-in-rust-v0-138-0
  source_release: codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a
  source_type: github_releases
  theme: uncategorized
  title: 54 other changes in rust-v0.138.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a|codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a]]'
source_type: github_releases
theme: uncategorized
title: 54 other changes in rust-v0.138.0
type: change
---

<!-- chronolog:begin region="header" -->
# 54 other changes in rust-v0.138.0

**Codex CLI** · 2026-06-08 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.138.0) · from [[Releases/Codex CLI/codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a|0.138.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server integrations can now read account token usage, and Codex auth supports v2 personal access tokens in CLI and app-server flows. (#25344, #25731)

> Forked threads now keep user-renamed titles instead of falling back to the original first-prompt name. (#26075)

> The TUI no longer adds extra blank space while streaming, and cancelled prompts reopen with the cursor at the end so you can keep editing naturally. (#26636, #26457)

> TUI config write failures now show the underlying cause, making validation problems and read-only filesystem issues much easier to diagnose. (#26537)

> The CLI README was refreshed to remove stale guidance and better match the current documentation flow. (#26313)

> `resume --last` now finds the newest matching session through the state DB first, which speeds up restore on large local histories. (#26462)

> #26179 nit: small prompt update for MAv2 @jif-oai

> #25700 core: stop threading SandboxPolicy through exec @bolinfest

> #25925 [codex] Copy user Bazel settings into Codex worktrees @anp-oai

> #25469 [profile-switcher][rust] -- [1/2] Add app-server account session protocol @dhruvgupta-oai

> #26075 Fix forked thread name inheritance @etraut-openai

> #26226 [codex] Split Python runtime release workflow @aibrahim-oai

> #26260 codex-pr-body: avoid confidential references @anp-oai

> #26367 chore: calm down @jif-oai

> #26147 Gate automatic idle turns in Plan mode @jif-oai

> #26172 Bridge host-loaded skills into the skills extension @jif-oai

> #26265 Optimize unbounded byte scans with memchr @charliemarsh-oai

> #26313 Simplify Codex CLI README @etraut-openai

> #26436 app-server: support -c config overrides @bolinfest

> #26248 [codex-analytics] emit forked thread id on initialization @kbazzi

> #26320 core: allow excluding tool namespaces from code mode @sayan-oai

> #25945 Use Azure artifact signing environment secrets @shijie-oai

> #23710 build: use ThinLTO for release binaries @anp-oai

> #26447 Remove response.processed websocket request @pakrym-oai

> #26312 Cleanup experimentalFeature/enablement/set @mzeng-openai

> #26466 Use Winget release environment secret @shijie-oai

> #26473 Add skill for pushing CI configuration changes @anp-oai

> #25000 ci: test windows cross build @cconger

> #26487 [codex] Add use_responses_lite 'override' logic @rka-oai

> #26256 [codex] Keep Bazel startup options stable across commands @anp-oai

> #26499 core: derive exec policy filesystem policy from profile @bolinfest

> #26566 nit: doc @jif-oai

> #25710 [codex] Forward turn moderation metadata through app-server @carlc-oai

> #26599 [codex] Keep v1 spawn metadata visible @jif-oai

> #25344 feat(app-server): expose account token usage [1 of 2] @fcoury-oai

> #26553 [codex] Fix long proxy socket paths @viyatb-oai

> #26537 Surface TUI config write error causes @etraut-openai

> #26551 Fix `/goal` usage text for control commands @etraut-openai

> #26554 Render code comment directives in TUI replay @etraut-openai

> #26532 Require absolute cwd in thread settings @pakrym-oai

> #26636 fix(tui): avoid doubled blank rows while streaming @fcoury-oai

> #26335 Clean up Rust release workflow @shijie-oai

> #26547 [1 of 2] Align goal extension with core behavior @etraut-openai

> #26181 fix(tui): Windows composer background @fcoury-oai

> #26457 fix(tui): restore cancelled prompt cursor at end @fcoury-oai

> #26484 [codex] Add turn profiling analytics @aibrahim-oai

> #26552 Make runtime workspace roots absolute in app-server API @pakrym-oai

> #26462 Use state DB first for `resume --last` @charliemarsh-oai

> #26548 [2 of 2] Finish moving goal runtime to extension @etraut-openai

> #26674 protocol: remove submission-side serde from Op @pakrym-oai

> #26490 [codex] Use standalone tools for Responses Lite @rka-oai

> #26542 [codex] Send Responses Lite transport header @rka-oai

> #26698 [codex] Deduplicate skill load warnings @xl-openai

> #26716 Remove `just bench-smoke` from `just test`. @anp-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.138.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-08-6-safety-and-privacy-changes-in-rust-v0-138-0|6 Safety and Privacy changes in rust-v0.138.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-08-2-image-generation-changes-in-rust-v0-138-0|2 Image Generation changes in rust-v0.138.0]] · Image Generation
- [[Changes/Codex CLI/2026-06-08-4-mobile-and-desktop-changes-in-rust-v0-138-0|4 Mobile and Desktop changes in rust-v0.138.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-08-2-account-and-access-changes-in-rust-v0-138-0|2 Account and Access changes in rust-v0.138.0]] · Account and Access
- [[Changes/Codex CLI/2026-06-08-7-developer-workflow-changes-in-rust-v0-138-0|7 Developer Workflow changes in rust-v0.138.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-08-19-apps-and-integrations-changes-in-rust-v0-138-0|19 Apps and Integrations changes in rust-v0.138.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-08-6-model-support-changes-in-rust-v0-138-0|6 Model Support changes in rust-v0.138.0]] · Model Support
- [[Changes/Codex CLI/2026-06-08-4-context-window-changes-in-rust-v0-138-0|4 Context Window changes in rust-v0.138.0]] · Context Window
- [[Changes/Codex CLI/2026-06-08-8-agent-mode-changes-in-rust-v0-138-0|8 Agent Mode changes in rust-v0.138.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-08-3-editor-experience-changes-in-rust-v0-138-0|3 Editor Experience changes in rust-v0.138.0]] · Editor Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-08-a61246&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-08-54-other-changes-in-rust-v0-138-0.md%0ACard%20ID%3A%20codex-cli-2026-06-08-a61246%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.138.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->