---
card_id: codex-cli-2026-03-16-f1ebe6
date: '2026-03-16'
description: 'Codex CLI · 2026-03-16 · Other changes: 70 changes in 0.115.0 — `js_repl`
  now exposes `codex.cwd` and `codex.homeDir`, and saved `codex.tool(...)` /…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4d01950ed5e1eb22445ab1209355fd46d61c47c8377950dbb86d7ae96b99321e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-16-f1ebe6
  comparison: ''
  date: '2026-03-16'
  description: 'Codex CLI — 0.115.0: 70 other changes'
  evidence:
  - quote: '`js_repl` now exposes `codex.cwd` and `codex.homeDir`, and saved `codex.tool(...)`
      / `codex.emitImage(...)` references keep working across cells. (#14385, #14503)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '`js_repl` no longer hangs when dynamic tool responses contain literal
      U+2028 or U+2029 characters. (#14421)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '`codex exec --profile` once again preserves profile-scoped settings when
      starting or resuming a thread. (#14524)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: The local network proxy now serves CONNECT traffic as explicit HTTP/1,
      improving compatibility with HTTP proxy clients. (#14395)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14395 fix(network-proxy): serve HTTP proxy listener as HTTP/1 @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14385 Add js_repl cwd and homeDir helpers @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14382 check for large binaries in CI @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14392 chore(app-server): stop emitting codex/event/ notifications @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14274 feat: search_tool migrate to bring you own tool of Responses API
      @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14174 refactor: centralize filesystem permissions precedence @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14394 chore(app-server): delete unused rpc methods from v1.rs @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14387 feat(app-server): propagate traces across tasks and core ops @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14295 Support waiting for code_mode sessions @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14431 Handle pre-approved permissions in zsh fork @mousseau-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14403 [elicitation] User-friendly tool call messages. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14429 Use granted permissions when invoking apply_patch @mousseau-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14471 Updated out-of-date tip about availability on free and go plans
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14444 fix: move inline codex-rs/core unit tests into sibling files @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14437 Dispatch tools when code mode is not awaited directly @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#13882 Fix stdio-to-uds peer-close flake @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14476 Move code mode tool files under tools/code_mode and split functionality
      @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14475 rename spawn_csv feature flag to enable_fanout @daveaitel-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14480 Cleanup code_mode tool descriptions @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14484 Add default code-mode yield timeout @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14494 Add parallel tool call test @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14478 chore(app-server): stop exporting EventMsg schemas @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14490 fix turn_start_jsonrpc_span_parents_core_turn_spans flakiness @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14496 Reuse tool runtime for code mode worker @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14421 Fix js_repl hangs on U+2028/U+2029 dynamic tool responses @aaronl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14510 Rename exec session IDs to cell IDs @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14500 Update tool search prompts @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14426 Decouple request permissions feature and tool @mousseau-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14503 Persist js_repl codex helpers across cells @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14517 Expose code-mode tools through globals @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14524 Fix `codex exec --profile` handling @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14516 Rename reject approval policy to granular @mousseau-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#13329 [js_repl] Hard-stop active js_repl execs on explicit user interrupts
      @aaronl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14239 client: extend custom CA handling across HTTPS and websocket clients
      @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14514 fix: reopen writable linux carveouts under denied parents @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14511 code_mode: Move exec params from runtime declarations to @pragma
      @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14504 Refactor cloud requirements error and surface in JSON-RPC error
      @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14537 Add realtime v2 event parser behind feature flag @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14529 Simplify permissions available in request permissions tool @mousseau-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14522 feat: support skill-scoped managed network domain overrides in
      skill config @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14554 Add codex tool support for realtime v2 handoff @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14518 Add diagnostics for read_only_unless_trusted timeout flake @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14526 code mode: single line tool declarations @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14558 sending back imagaegencall response back to responseapi @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14553 Improve granular approval policy prompt @mousseau-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14542 [bazel] Bump up cc and rust toolchains @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14512 Start TUI on embedded app server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14606 Unify realtime v1/v2 session config @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14527 app-server: Add platform os and family to init response @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14479 feat(app-server, core): add more spans @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#13644 fix: preserve zsh-fork escalation fds across unified-exec spawn
      paths @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14617 Add code_mode_only feature @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14245 app-server: add v2 filesystem APIs @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#13860 Add Smart Approvals guardian review across core, app-server, and
      TUI @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14639 Fix stale create_wait_tool reference @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14633 refactor: make unified-exec zsh-fork state explicit @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#12031 Add openai_base_url config override for built-in provider @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14645 Fix Windows CI assertions for guardian and Smart Approvals @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14619 fix: persist future network host approvals across sessions @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14649 make defaultPrompt an array, keep backcompat @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14501 dynamic tool calls: add param `exposeToContext` to optionally hide
      tool @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14651 Add argument-comment Dylint runner @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14611 Add auth 401 recovery observability to client bug reports @ccy-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14668 Reuse guardian session across approvals @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14769 fix(core): preserve tool_params for elicitations @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14806 feat: improve skills cache key to take into account config layering
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 70-other-changes-in-rust-v0-115-0
  source_release: codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db
  source_type: github_releases
  theme: uncategorized
  title: 70 other changes in rust-v0.115.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db|codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db]]'
source_type: github_releases
theme: uncategorized
title: 70 other changes in rust-v0.115.0
type: change
---

<!-- chronolog:begin region="header" -->
# 70 other changes in rust-v0.115.0

**Codex CLI** · 2026-03-16 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.115.0) · from [[Releases/Codex CLI/codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db|0.115.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `js_repl` now exposes `codex.cwd` and `codex.homeDir`, and saved `codex.tool(...)` / `codex.emitImage(...)` references keep working across cells. (#14385, #14503)

> `js_repl` no longer hangs when dynamic tool responses contain literal U+2028 or U+2029 characters. (#14421)

> `codex exec --profile` once again preserves profile-scoped settings when starting or resuming a thread. (#14524)

> The local network proxy now serves CONNECT traffic as explicit HTTP/1, improving compatibility with HTTP proxy clients. (#14395)

> #14395 fix(network-proxy): serve HTTP proxy listener as HTTP/1 @viyatb-oai

> #14385 Add js_repl cwd and homeDir helpers @fjord-oai

> #14382 check for large binaries in CI @owenlin0

> #14392 chore(app-server): stop emitting codex/event/ notifications @owenlin0

> #14274 feat: search_tool migrate to bring you own tool of Responses API @apanasenko-oai

> #14174 refactor: centralize filesystem permissions precedence @viyatb-oai

> #14394 chore(app-server): delete unused rpc methods from v1.rs @owenlin0

> #14387 feat(app-server): propagate traces across tasks and core ops @owenlin0

> #14295 Support waiting for code_mode sessions @pakrym-oai

> #14431 Handle pre-approved permissions in zsh fork @mousseau-oai

> #14403 [elicitation] User-friendly tool call messages. @mzeng-openai

> #14429 Use granted permissions when invoking apply_patch @mousseau-oai

> #14471 Updated out-of-date tip about availability on free and go plans @etraut-openai

> #14444 fix: move inline codex-rs/core unit tests into sibling files @bolinfest

> #14437 Dispatch tools when code mode is not awaited directly @pakrym-oai

> #13882 Fix stdio-to-uds peer-close flake @aibrahim-oai

> #14476 Move code mode tool files under tools/code_mode and split functionality @pakrym-oai

> #14475 rename spawn_csv feature flag to enable_fanout @daveaitel-openai

> #14480 Cleanup code_mode tool descriptions @pakrym-oai

> #14484 Add default code-mode yield timeout @pakrym-oai

> #14494 Add parallel tool call test @pakrym-oai

> #14478 chore(app-server): stop exporting EventMsg schemas @owenlin0

> #14490 fix turn_start_jsonrpc_span_parents_core_turn_spans flakiness @owenlin0

> #14496 Reuse tool runtime for code mode worker @pakrym-oai

> #14421 Fix js_repl hangs on U+2028/U+2029 dynamic tool responses @aaronl-openai

> #14510 Rename exec session IDs to cell IDs @pakrym-oai

> #14500 Update tool search prompts @mzeng-openai

> #14426 Decouple request permissions feature and tool @mousseau-oai

> #14503 Persist js_repl codex helpers across cells @fjord-oai

> #14517 Expose code-mode tools through globals @pakrym-oai

> #14524 Fix `codex exec --profile` handling @etraut-openai

> #14516 Rename reject approval policy to granular @mousseau-oai

> #13329 [js_repl] Hard-stop active js_repl execs on explicit user interrupts @aaronl-openai

> #14239 client: extend custom CA handling across HTTPS and websocket clients @joshka-oai

> #14514 fix: reopen writable linux carveouts under denied parents @viyatb-oai

> #14511 code_mode: Move exec params from runtime declarations to @pragma @cconger

> #14504 Refactor cloud requirements error and surface in JSON-RPC error @alexsong-oai

> #14537 Add realtime v2 event parser behind feature flag @aibrahim-oai

> #14529 Simplify permissions available in request permissions tool @mousseau-oai

> #14522 feat: support skill-scoped managed network domain overrides in skill config @celia-oai

> #14554 Add codex tool support for realtime v2 handoff @aibrahim-oai

> #14518 Add diagnostics for read_only_unless_trusted timeout flake @aibrahim-oai

> #14526 code mode: single line tool declarations @pakrym-oai

> #14558 sending back imagaegencall response back to responseapi @won-openai

> #14553 Improve granular approval policy prompt @mousseau-oai

> #14542 [bazel] Bump up cc and rust toolchains @zbarsky-openai

> #14512 Start TUI on embedded app server @etraut-openai

> #14606 Unify realtime v1/v2 session config @aibrahim-oai

> #14527 app-server: Add platform os and family to init response @euroelessar

> #14479 feat(app-server, core): add more spans @owenlin0

> #13644 fix: preserve zsh-fork escalation fds across unified-exec spawn paths @bolinfest

> #14617 Add code_mode_only feature @pakrym-oai

> #14245 app-server: add v2 filesystem APIs @euroelessar

> #13860 Add Smart Approvals guardian review across core, app-server, and TUI @charley-oai

> #14639 Fix stale create_wait_tool reference @charley-oai

> #14633 refactor: make unified-exec zsh-fork state explicit @bolinfest

> #12031 Add openai_base_url config override for built-in provider @etraut-openai

> #14645 Fix Windows CI assertions for guardian and Smart Approvals @aibrahim-oai

> #14619 fix: persist future network host approvals across sessions @viyatb-oai

> #14649 make defaultPrompt an array, keep backcompat @sayan-oai

> #14501 dynamic tool calls: add param `exposeToContext` to optionally hide tool @cconger

> #14651 Add argument-comment Dylint runner @bolinfest

> #14611 Add auth 401 recovery observability to client bug reports @ccy-oai

> #14668 Reuse guardian session across approvals @charley-oai

> #14769 fix(core): preserve tool_params for elicitations @mzeng-openai

> #14806 feat: improve skills cache key to take into account config layering @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.115.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-16-17-apps-and-integrations-changes-in-rust-v0-115-0|17 Apps and Integrations changes in rust-v0.115.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-16-2-context-window-changes-in-rust-v0-115-0|2 Context Window changes in rust-v0.115.0]] · Context Window
- [[Changes/Codex CLI/2026-03-16-16-agent-mode-changes-in-rust-v0-115-0|16 Agent Mode changes in rust-v0.115.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-16-2-mobile-and-desktop-changes-in-rust-v0-115-0|2 Mobile and Desktop changes in rust-v0.115.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-16-4-voice-and-audio-changes-in-rust-v0-115-0|4 Voice and Audio changes in rust-v0.115.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-16-14493-memories-focus-write-prompts-on-user-preferences-andi-oai|♯14493 memories: focus write prompts on user preferences @andi-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-16-9-safety-and-privacy-changes-in-rust-v0-115-0|9 Safety and Privacy changes in rust-v0.115.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-16-5-model-support-changes-in-rust-v0-115-0|5 Model Support changes in rust-v0.115.0]] · Model Support
- [[Changes/Codex CLI/2026-03-16-2-account-and-access-changes-in-rust-v0-115-0|2 Account and Access changes in rust-v0.115.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-16-2-developer-workflow-changes-in-rust-v0-115-0|2 Developer Workflow changes in rust-v0.115.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-16-14410-make-collab-model-metadata-accurate-on-completion-aibrahim-oai|♯14410 Make collab model metadata accurate on completion @aibrahim-oai]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-16-f1ebe6&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-16-70-other-changes-in-rust-v0-115-0.md%0ACard%20ID%3A%20codex-cli-2026-03-16-f1ebe6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.115.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->