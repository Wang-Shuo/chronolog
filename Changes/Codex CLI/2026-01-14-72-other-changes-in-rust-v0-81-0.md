---
card_id: codex-cli-2026-01-14-2245a5
date: '2026-01-14'
description: 'Codex CLI · 2026-01-14 · Other changes: 72 changes in 0.81.0 — Alternate-screen
  handling now avoids breaking Zellij scrollback and adds a config/flag to…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e2919e52c9ce6b7744db57e0f7fffc41276c610e34e8a15a93478e5b72099d7c
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-14-2245a5
  comparison: ''
  date: '2026-01-14'
  description: 'Codex CLI — 0.81.0: 72 other changes'
  evidence:
  - quote: Alternate-screen handling now avoids breaking Zellij scrollback and adds
      a config/flag to control it. (#8555)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: 'Config.toml and rules parsing errors are reported to app-server clients/TUI
      instead of failing silently. (#9182, #9011)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: Invalid user image uploads now surface an error instead of being silently
      replaced. (#9146)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: Published a generated JSON Schema for `config.toml` in `docs/` to validate
      configs. (#8956)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: Documented the TUI paste-burst state machine for terminals without reliable
      bracketed paste. (#9020)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: 'Added Bazel build support plus a `just bazel-codex` helper for contributors.
      (#8875, #9177)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8930 feat: first pass on clb tool @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8966 nit: rename session metric @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8969 chore: non mutable btree when building specs @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8968 chore: move otel provider outside of trace module @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8970 chore: add approval metric @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8975 chore: metrics tool call @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8901 chore: update metrics temporality @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8954 Work around crash in system-configuration library @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8873 fix(app-server): set originator header from initialize JSON-RPC
      request @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8909 Add config to disable /feedback @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8985 chore: nuke telemetry file @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8986 Revert "fix(app-server): set originator header from initialize JSON-RPC
      request" @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8978 nit: rename to analytics_enabled @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8963 renaming: task to turn @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8555 fix: add tui.alternate_screen config and --no-alt-screen CLI flag
      for Zellij scrollback @hjanuschka'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8875 feat: add support for building with Bazel @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8988 fix(app-server): set originator header from initialize (re-revert)
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8766 fix: harden arg0 helper PATH handling @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8949 Log unhandled sse events @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9003 Delete announcement_tip.toml @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8984 Add URL to responses error messages @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9032 Revert "Delete announcement_tip.toml" @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9018 fix: support remote arm64 builds, as well @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8983 feat: testing harness for collab 1 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9088 feat: add wait tool implementation for collab @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9090 feat: add close tool implementation for collab @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9099 nit: add docstring @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8994 feat: wire fork to codex cli @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9072 chore(deps): bump ts-rs from 11.0.1 to 11.1.0 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9074 chore(deps): bump which from 6.0.3 to 8.0.0 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9075 chore(deps): bump clap from 4.5.53 to 4.5.54 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9076 chore(deps): bump tokio-util from 0.7.16 to 0.7.18 in /codex-rs
      @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9107 Remove unused conversation_id header @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9080 Add some tests for image attachments @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9114 Extract single responses SSE event parsing @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8246 fix(tui): show in-flight coalesced tool calls in transcript overlay
      @Chriss4123'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9127 Reuse websocket connection @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9128 Websocket append support @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9049 Handle image paste from empty paste events @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8952 Use markdown for migration screen @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9109 Updated heuristic for tool call summary to detect file modifications
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9140 Use thread rollback for Esc backtrack @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9143 chore: better error handling on collab tools @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9147 nit: collab send input cleaning @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8798 ollama: default to Responses API for built-ins @drifkin'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8956 add generated jsonschema for config.toml @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9122 Fix queued messages during /review @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9126 fix: drop session span at end of the session @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9118 feat(app-server): add an --analytics-default-enabled flag @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9130 Fresh tooltips @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9121 test(tui): add deterministic paste-burst tests @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9165 Allow close skill popup with esc. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9169 Fix flakiness in WebSocket tests @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9011 fix: report an appropriate error in the TUI for malformed rules
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9177 feat: add bazel-codex entry to justfile @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9175 WebSocket test server script @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8933 [CODEX-4427] improve parsed commands @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9174 Renew cache ttl on etag match @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9124 fix(tui): harden paste-burst state transitions @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9186 Use offline cache for tui migrations @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9182 Improve handling of config and rules errors for app server clients
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9146 feat: return an error if the image sent by the user is a bad image
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9145 fix: drop double waiting header in TUI @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9194 Render exec output deltas inline @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9156 chore: clamp min yield time for empty write_stdin @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9105 feat: add auto refresh on thread listeners @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 72-other-changes-in-rust-v0-81-0
  source_release: codex-cli-2026-01-14-rust-v0-81-0-github-276819252-cf63dc40
  source_type: github_releases
  theme: uncategorized
  title: 72 other changes in rust-v0.81.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-14-rust-v0-81-0-github-276819252-cf63dc40|codex-cli-2026-01-14-rust-v0-81-0-github-276819252-cf63dc40]]'
source_type: github_releases
theme: uncategorized
title: 72 other changes in rust-v0.81.0
type: change
---

<!-- chronolog:begin region="header" -->
# 72 other changes in rust-v0.81.0

**Codex CLI** · 2026-01-14 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.81.0) · from [[Releases/Codex CLI/codex-cli-2026-01-14-rust-v0-81-0-github-276819252-cf63dc40|0.81.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Alternate-screen handling now avoids breaking Zellij scrollback and adds a config/flag to control it. (#8555)

> Config.toml and rules parsing errors are reported to app-server clients/TUI instead of failing silently. (#9182, #9011)

> Invalid user image uploads now surface an error instead of being silently replaced. (#9146)

> Published a generated JSON Schema for `config.toml` in `docs/` to validate configs. (#8956)

> Documented the TUI paste-burst state machine for terminals without reliable bracketed paste. (#9020)

> Added Bazel build support plus a `just bazel-codex` helper for contributors. (#8875, #9177)

> #8930 feat: first pass on clb tool @jif-oai

> #8966 nit: rename session metric @jif-oai

> #8969 chore: non mutable btree when building specs @jif-oai

> #8968 chore: move otel provider outside of trace module @jif-oai

> #8970 chore: add approval metric @jif-oai

> #8975 chore: metrics tool call @jif-oai

> #8901 chore: update metrics temporality @jif-oai

> #8954 Work around crash in system-configuration library @etraut-openai

> #8873 fix(app-server): set originator header from initialize JSON-RPC request @owenlin0

> #8909 Add config to disable /feedback @gt-oai

> #8985 chore: nuke telemetry file @jif-oai

> #8986 Revert "fix(app-server): set originator header from initialize JSON-RPC request" @jif-oai

> #8978 nit: rename to analytics_enabled @jif-oai

> #8963 renaming: task to turn @jif-oai

> #8555 fix: add tui.alternate_screen config and --no-alt-screen CLI flag for Zellij scrollback @hjanuschka

> #8875 feat: add support for building with Bazel @zbarsky-openai

> #8988 fix(app-server): set originator header from initialize (re-revert) @owenlin0

> #8766 fix: harden arg0 helper PATH handling @viyatb-oai

> #8949 Log unhandled sse events @pakrym-oai

> #9003 Delete announcement_tip.toml @pakrym-oai

> #8984 Add URL to responses error messages @gt-oai

> #9032 Revert "Delete announcement_tip.toml" @jif-oai

> #9018 fix: support remote arm64 builds, as well @zbarsky-openai

> #8983 feat: testing harness for collab 1 @jif-oai

> #9088 feat: add wait tool implementation for collab @jif-oai

> #9090 feat: add close tool implementation for collab @jif-oai

> #9099 nit: add docstring @jif-oai

> #8994 feat: wire fork to codex cli @apanasenko-oai

> #9072 chore(deps): bump ts-rs from 11.0.1 to 11.1.0 in /codex-rs @dependabot

> #9074 chore(deps): bump which from 6.0.3 to 8.0.0 in /codex-rs @dependabot

> #9075 chore(deps): bump clap from 4.5.53 to 4.5.54 in /codex-rs @dependabot

> #9076 chore(deps): bump tokio-util from 0.7.16 to 0.7.18 in /codex-rs @dependabot

> #9107 Remove unused conversation_id header @pakrym-oai

> #9080 Add some tests for image attachments @charley-oai

> #9114 Extract single responses SSE event parsing @pakrym-oai

> #8246 fix(tui): show in-flight coalesced tool calls in transcript overlay @Chriss4123

> #9127 Reuse websocket connection @pakrym-oai

> #9128 Websocket append support @pakrym-oai

> #9049 Handle image paste from empty paste events @aibrahim-oai

> #8952 Use markdown for migration screen @aibrahim-oai

> #9109 Updated heuristic for tool call summary to detect file modifications @etraut-openai

> #9140 Use thread rollback for Esc backtrack @aibrahim-oai

> #9143 chore: better error handling on collab tools @jif-oai

> #9147 nit: collab send input cleaning @jif-oai

> #8798 ollama: default to Responses API for built-ins @drifkin

> #8956 add generated jsonschema for config.toml @sayan-oai

> #9122 Fix queued messages during /review @charley-oai

> #9126 fix: drop session span at end of the session @apanasenko-oai

> #9118 feat(app-server): add an --analytics-default-enabled flag @owenlin0

> #9130 Fresh tooltips @mzeng-openai

> #9121 test(tui): add deterministic paste-burst tests @joshka-oai

> #9165 Allow close skill popup with esc. @xl-openai

> #9169 Fix flakiness in WebSocket tests @pakrym-oai

> #9011 fix: report an appropriate error in the TUI for malformed rules @bolinfest

> #9177 feat: add bazel-codex entry to justfile @bolinfest

> #9175 WebSocket test server script @pakrym-oai

> #8933 [CODEX-4427] improve parsed commands @aibrahim-oai

> #9174 Renew cache ttl on etag match @aibrahim-oai

> #9124 fix(tui): harden paste-burst state transitions @joshka-oai

> #9186 Use offline cache for tui migrations @aibrahim-oai

> #9182 Improve handling of config and rules errors for app server clients @etraut-openai

> #9146 feat: return an error if the image sent by the user is a bad image @jif-oai

> #9145 fix: drop double waiting header in TUI @jif-oai

> #9194 Render exec output deltas inline @aibrahim-oai

> #9156 chore: clamp min yield time for empty write_stdin @jif-oai

> #9105 feat: add auto refresh on thread listeners @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.81.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-14-2-agent-mode-changes-in-rust-v0-81-0|2 Agent Mode changes in rust-v0.81.0]] · Agent Mode
- [[Changes/Codex CLI/2026-01-14-2-interface-experience-changes-in-rust-v0-81-0|2 Interface Experience changes in rust-v0.81.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-14-10-apps-and-integrations-changes-in-rust-v0-81-0|10 Apps and Integrations changes in rust-v0.81.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-14-5-developer-workflow-changes-in-rust-v0-81-0|5 Developer Workflow changes in rust-v0.81.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-14-2-account-and-access-changes-in-rust-v0-81-0|2 Account and Access changes in rust-v0.81.0]] · Account and Access
- [[Changes/Codex CLI/2026-01-14-5-safety-and-privacy-changes-in-rust-v0-81-0|5 Safety and Privacy changes in rust-v0.81.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-14-2-mobile-and-desktop-changes-in-rust-v0-81-0|2 Mobile and Desktop changes in rust-v0.81.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-14-9020-fix-tui-document-paste-burst-state-machine-joshka-oai|♯9020 fix(tui): document paste-burst state machine @joshka-oai]] · Files and Data
- [[Changes/Codex CLI/2026-01-14-8-model-support-changes-in-rust-v0-81-0|8 Model Support changes in rust-v0.81.0]] · Model Support
- [[Changes/Codex CLI/2026-01-14-2-editor-experience-changes-in-rust-v0-81-0|2 Editor Experience changes in rust-v0.81.0]] · Editor Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-14-2245a5&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-14-72-other-changes-in-rust-v0-81-0.md%0ACard%20ID%3A%20codex-cli-2026-01-14-2245a5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.81.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->