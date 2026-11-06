---
card_id: codex-cli-2026-07-08-85d38d
date: '2026-07-08'
description: 'Codex CLI · 2026-07-08 · Other changes: 145 changes in 0.143.0 — App-server
  clients can inspect environments, list descendant threads, and fork history through…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c244efc73b19fe22a3df68a4930773f80436ce290f87143304da10fe12ea2997
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-08-85d38d
  comparison: ''
  date: '2026-07-08'
  description: 'Codex CLI — 0.143.0: 145 other changes'
  evidence:
  - quote: 'App-server clients can inspect environments, list descendant threads,
      and fork history through a specific turn. (#30291, #29591, #30277)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: Improved incremental WebSocket request success by ignoring response metadata
      during comparisons. (#30770)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: Reduced installer failures from GitHub API rate limits by reusing release
      metadata. (#31056)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#26708 PAC 3 - Add Windows system proxy resolver @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#28769 Register full CDP requirements feature @syuan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29487 Upgrade bundled OpenSSL to 3.6.3 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29489 [codex] Update esbuild to 0.28.1 @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#28360 feat(core): store turn_id on ResponseItem metadata @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29501 path-uri: clarify host-native path conversion @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29504 fix: world state response item test @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29419 [codex] reject remote images at app-server ingress @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#28992 chore: improve expired Bedrock credential errors @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29467 Make formatter output quiet on success @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#24092 [codex] Reject unlowered PowerShell AST regions @bookholt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29068 [codex] stylistic changes @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#27946 [codex] Use input items for Responses Lite tools @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29577 Handle additional tools in image URL validation @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29599 Stop persisting bridged log events @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29614 path-uri: add lexical containment @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29634 Update rmcp to 1.8.0 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29650 Update vulnerable Hono and fast-uri dependencies @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29498 [codex] Instrument rollout persistence bytes @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29659 [core] debounce current-time reminders by elapsed time @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29672 [codex] Handle additional tools in rollout persistence metrics
      @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29669 Handle additional tools in rollout persistence metrics @winston-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29680 Revert "Handle additional tools in rollout persistence metrics"
      @rasmusrygaard'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#28418 chore(core) rm AskForApproval::OnFailure @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29675 core: add extra metadata field to Thread struct @kumquatexpress'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29526 core: resolve view_image paths in selected environment @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29547 core: use current step environments for tools @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#27045 feat(guardian): include connected account email in app reviews
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29666 [codex] Report the exec-server working directory @rasmusrygaard'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29705 feat(app-server): thread/turns/items/list -> thread/items/list
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29716 code-mode: Rename codex_code_mode::CodeModeService @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29712 test: branch on target OS instead of runner flavor @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29728 core tests: rename automatic environment builder @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29158 path-uri: remove legacy path deserialization @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29515 [codex] define code mode host handshake protocol @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29715 [codex] surface rollout budget exhaustion @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29732 code-mode: Remove Session::is_alive() @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29626 Load executor skills without host path conversion @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29714 protocol: separate app and exec RPC ownership @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29744 [codex] rename rollout budget error to session budget error @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29477 Support thread-level originator overrides @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29745 core: add wait_for_environment for starting environments @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29746 test: add app-server auto environment helper @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29768 [codex] Update bundled skill installer guidance @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29767 [codex] Assign response item IDs in forked history @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29721 auth: move domain mode below app wire types @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29722 config: own layer provenance types @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29731 [codex] Emit implicit skill usage for support reads @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29841 Add a bounded filesystem walk RPC @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29842 Use fs/walk for environment skill discovery @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29567 [codex] show external import result counts @charlesgong-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29887 Fix environment skill discovery after merge @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29734 [codex] fix Windows ConPTY input handling @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#27466 [codex] Trace exec-server JSON-RPC requests @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29844 Follow directory symlinks in filesystem walks @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29637 Skip credential refresh for WindowsApps launch failures @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29591 feat(app-server): list descendant threads by ancestor @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#28034 feat(network-proxy): experimental local credential broker @winston-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29903 path-uri: normalize parent segments in absolute joins @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29907 [codex] namespace sleep under clock @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29910 [codex] nest sleep config under current time reminder @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29833 [1/3] core: make world state snapshots serializable @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29919 TUI support for buffer experience @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29804 code-mode: define process host wire protocol @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29835 [2/3] core: persist world state in rollouts @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29837 [3/3] core: replay persisted world state @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29970 core: raise token budget message limits @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29973 [codex] route sleep through time providers @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29997 core: reconcile legacy WorldState sections @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29990 Parallelize environment skill loading @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29928 chore(app-server): mark thread/rollback as deprecated @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#27467 [codex] Record exec-server lifecycle metrics @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30029 [codex] current time reminder interval to be set to 0 @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30031 [codex] add current time reminder delivery mode config @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30098 [codex] Retry temporarily offline exec-server recovery @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30033 [codex] impl delivery_mode: current time reminders on response
      boundaries @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30108 [codex] extend code-mode host IPC transport @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#27470 [codex] Observe remote exec-server lifecycle @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30113 [codex] poll external clock during sleep @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30114 release: publish standalone zsh artifacts @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30116 release: consume standalone zsh artifacts @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30124 fix(app-server): suppress TUI rollback warning @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30088 Project executor skills through World State @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30117 [codex] Propagate traces through exec-server HTTP @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30134 ci: narrow Windows test skips @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30145 Reuse walk inventory for environment skill metadata @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30111 [codex] implement standalone code-mode process host @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29935 [codex] Attribute app-server analytics by thread originator @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30152 Reinject missing World State fragments on resume @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30157 Test selected capabilities across availability and resume @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30112 [codex] add process-owned code-mode session client @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30142 [codex] wire process-owned code mode host into core @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30198 [codex] fix CreateThreadParams test initializer @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30215 Test selected capabilities across unavailable resume @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29991 [codex] narrow unused skills intro export @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29927 feat(app-server): add history_mode to thread @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30276 fix main @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30225 Overlap executor skill reads with namespace discovery @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30147 [codex] Use managed defaults for TUI threads @hefuc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30261 ensure thread.history_mode is immutable @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30277 feat(app-server): add optional turn_id to thread/fork @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30173 Close thread persistence when submission channel closes @alfozan'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30146 [codex] group blocking and postmerge CI workflows @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30282 feat(protocol): define missing rollout turn items @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30273 [codex] consume pushed exec-server process events @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30314 app-server: structure and test JSON shutdown logs @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30302 Preserve namespaces on custom tool calls @nhamidi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30327 core: stabilize synthesized call output IDs @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30291 [app-server] expose environment info RPC @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30384 [app-server] increase currentTime/read timeout @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30511 [codex] Restore v1 delegation guidance @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30607 [codex] auto-label AWS Bedrock issues @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30269 [codex] disable Nagle on Rendezvous WebSockets @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30757 fix(core) Remove full text websocket trace @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30643 [codex] bound Rendezvous WebSocket liveness @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30770 fix(websockets) ignore metadata for incremental requests @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30334 telemetry: log structured direct tool-call timing @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30796 Fix MIME types for path-backed feedback attachments @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31056 fix(install): reuse GitHub release metadata @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31064 [codex] Read buffering metadata from response events @fc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30876 [core] Support interleaved response items @alexi-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31261 Revert "[core] Support interleaved response items" @alexi-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31253 Emit exec-policy warnings for freshly loaded thread config @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31179 Remove TUI exec-policy core exports @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29959 Conditional codex_home dotenv @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30318 core: trace executor skill discovery @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31276 Revert "Conditional codex_home dotenv" @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30956 refactor(protocol): isolate legacy item fanout @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30395 [app-server] Include reset-credit details in rate limits @jayp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29918 [codex] Flush trailing realtime transcript tail @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29697 fix: attribut network requests to the exact exec on linux @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31303 feat(code-mode): allow disabling V8 JIT @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31271 chore: use .worktreeinclude for user Bazel config @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31308 fix: update crossbeam-epoch for RUSTSEC-2026-0204 @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30202 [codex] bundle code mode host in release packages @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31284 Warn when configured service tiers are unsupported @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31331 Migrate direct HTTP consumers to codex-http-client @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31337 fix: restore Codex environment setup table @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31188 Preserve managed exec policy after rules parse errors @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31344 exec-server: use virtual time in Noise relay test @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31296 refactor(protocol): map canonical tool items to legacy events @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31335 core: route Responses API through system proxy @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 145-other-changes-in-rust-v0-143-0
  source_release: codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c
  source_type: github_releases
  theme: uncategorized
  title: 145 other changes in rust-v0.143.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c|codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c]]'
source_type: github_releases
theme: uncategorized
title: 145 other changes in rust-v0.143.0
type: change
---

<!-- chronolog:begin region="header" -->
# 145 other changes in rust-v0.143.0

**Codex CLI** · 2026-07-08 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.143.0) · from [[Releases/Codex CLI/codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c|0.143.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server clients can inspect environments, list descendant threads, and fork history through a specific turn. (#30291, #29591, #30277)

> Improved incremental WebSocket request success by ignoring response metadata during comparisons. (#30770)

> Reduced installer failures from GitHub API rate limits by reusing release metadata. (#31056)

> #26708 PAC 3 - Add Windows system proxy resolver @canvrno-oai

> #28769 Register full CDP requirements feature @syuan-oai

> #29487 Upgrade bundled OpenSSL to 3.6.3 @jif-oai

> #29489 [codex] Update esbuild to 0.28.1 @pakrym-oai

> #28360 feat(core): store turn_id on ResponseItem metadata @owenlin0

> #29501 path-uri: clarify host-native path conversion @anp-oai

> #29504 fix: world state response item test @celia-oai

> #29419 [codex] reject remote images at app-server ingress @rka-oai

> #28992 chore: improve expired Bedrock credential errors @celia-oai

> #29467 Make formatter output quiet on success @anp-oai

> #24092 [codex] Reject unlowered PowerShell AST regions @bookholt-oai

> #29068 [codex] stylistic changes @rka-oai

> #27946 [codex] Use input items for Responses Lite tools @rka-oai

> #29577 Handle additional tools in image URL validation @aibrahim-oai

> #29599 Stop persisting bridged log events @jif-oai

> #29614 path-uri: add lexical containment @jif-oai

> #29634 Update rmcp to 1.8.0 @jif-oai

> #29650 Update vulnerable Hono and fast-uri dependencies @jif-oai

> #29498 [codex] Instrument rollout persistence bytes @wiltzius-openai

> #29659 [core] debounce current-time reminders by elapsed time @rka-oai

> #29672 [codex] Handle additional tools in rollout persistence metrics @rka-oai

> #29669 Handle additional tools in rollout persistence metrics @winston-openai

> #29680 Revert "Handle additional tools in rollout persistence metrics" @rasmusrygaard

> #28418 chore(core) rm AskForApproval::OnFailure @dylan-hurd-oai

> #29675 core: add extra metadata field to Thread struct @kumquatexpress

> #29526 core: resolve view_image paths in selected environment @anp-oai

> #29547 core: use current step environments for tools @sayan-oai

> #27045 feat(guardian): include connected account email in app reviews @viyatb-oai

> #29666 [codex] Report the exec-server working directory @rasmusrygaard

> #29705 feat(app-server): thread/turns/items/list -> thread/items/list @owenlin0

> #29716 code-mode: Rename codex_code_mode::CodeModeService @cconger

> #29712 test: branch on target OS instead of runner flavor @anp-oai

> #29728 core tests: rename automatic environment builder @anp-oai

> #29158 path-uri: remove legacy path deserialization @anp-oai

> #29515 [codex] define code mode host handshake protocol @cconger

> #29715 [codex] surface rollout budget exhaustion @rka-oai

> #29732 code-mode: Remove Session::is_alive() @cconger

> #29626 Load executor skills without host path conversion @jif-oai

> #29714 protocol: separate app and exec RPC ownership @anp-oai

> #29744 [codex] rename rollout budget error to session budget error @rka-oai

> #29477 Support thread-level originator overrides @alexsong-oai

> #29745 core: add wait_for_environment for starting environments @sayan-oai

> #29746 test: add app-server auto environment helper @anp-oai

> #29768 [codex] Update bundled skill installer guidance @sayan-oai

> #29767 [codex] Assign response item IDs in forked history @pakrym-oai

> #29721 auth: move domain mode below app wire types @anp-oai

> #29722 config: own layer provenance types @anp-oai

> #29731 [codex] Emit implicit skill usage for support reads @alexsong-oai

> #29841 Add a bounded filesystem walk RPC @jif-oai

> #29842 Use fs/walk for environment skill discovery @jif-oai

> #29567 [codex] show external import result counts @charlesgong-openai

> #29887 Fix environment skill discovery after merge @jif-oai

> #29734 [codex] fix Windows ConPTY input handling @iceweasel-oai

> #27466 [codex] Trace exec-server JSON-RPC requests @richardopenai

> #29844 Follow directory symlinks in filesystem walks @jif-oai

> #29637 Skip credential refresh for WindowsApps launch failures @jif-oai

> #29591 feat(app-server): list descendant threads by ancestor @btraut-openai

> #28034 feat(network-proxy): experimental local credential broker @winston-openai

> #29903 path-uri: normalize parent segments in absolute joins @anp-oai

> #29907 [codex] namespace sleep under clock @rka-oai

> #29910 [codex] nest sleep config under current time reminder @rka-oai

> #29833 [1/3] core: make world state snapshots serializable @sayan-oai

> #29919 TUI support for buffer experience @etraut-openai

> #29804 code-mode: define process host wire protocol @cconger

> #29835 [2/3] core: persist world state in rollouts @sayan-oai

> #29837 [3/3] core: replay persisted world state @sayan-oai

> #29970 core: raise token budget message limits @bolinfest

> #29973 [codex] route sleep through time providers @rka-oai

> #29997 core: reconcile legacy WorldState sections @sayan-oai

> #29990 Parallelize environment skill loading @anp-oai

> #29928 chore(app-server): mark thread/rollback as deprecated @owenlin0

> #27467 [codex] Record exec-server lifecycle metrics @richardopenai

> #30029 [codex] current time reminder interval to be set to 0 @rka-oai

> #30031 [codex] add current time reminder delivery mode config @rka-oai

> #30098 [codex] Retry temporarily offline exec-server recovery @richardopenai

> #30033 [codex] impl delivery_mode: current time reminders on response boundaries @rka-oai

> #30108 [codex] extend code-mode host IPC transport @cconger

> #27470 [codex] Observe remote exec-server lifecycle @richardopenai

> #30113 [codex] poll external clock during sleep @rka-oai

> #30114 release: publish standalone zsh artifacts @bolinfest

> #30116 release: consume standalone zsh artifacts @bolinfest

> #30124 fix(app-server): suppress TUI rollback warning @fcoury-oai

> #30088 Project executor skills through World State @jif-oai

> #30117 [codex] Propagate traces through exec-server HTTP @wiltzius-openai

> #30134 ci: narrow Windows test skips @anp-oai

> #30145 Reuse walk inventory for environment skill metadata @jif-oai

> #30111 [codex] implement standalone code-mode process host @cconger

> #29935 [codex] Attribute app-server analytics by thread originator @alexsong-oai

> #30152 Reinject missing World State fragments on resume @jif-oai

> #30157 Test selected capabilities across availability and resume @jif-oai

> #30112 [codex] add process-owned code-mode session client @cconger

> #30142 [codex] wire process-owned code mode host into core @cconger

> #30198 [codex] fix CreateThreadParams test initializer @anp-oai

> #30215 Test selected capabilities across unavailable resume @jif-oai

> #29991 [codex] narrow unused skills intro export @aibrahim-oai

> #29927 feat(app-server): add history_mode to thread @owenlin0

> #30276 fix main @owenlin0

> #30225 Overlap executor skill reads with namespace discovery @jif-oai

> #30147 [codex] Use managed defaults for TUI threads @hefuc-oai

> #30261 ensure thread.history_mode is immutable @owenlin0

> #30277 feat(app-server): add optional turn_id to thread/fork @owenlin0

> #30173 Close thread persistence when submission channel closes @alfozan

> #30146 [codex] group blocking and postmerge CI workflows @anp-oai

> #30282 feat(protocol): define missing rollout turn items @owenlin0

> #30273 [codex] consume pushed exec-server process events @richardopenai

> #30314 app-server: structure and test JSON shutdown logs @bolinfest

> #30302 Preserve namespaces on custom tool calls @nhamidi-oai

> #30327 core: stabilize synthesized call output IDs @bolinfest

> #30291 [app-server] expose environment info RPC @maxj-oai

> #30384 [app-server] increase currentTime/read timeout @rka-oai

> #30511 [codex] Restore v1 delegation guidance @aibrahim-oai

> #30607 [codex] auto-label AWS Bedrock issues @etraut-openai

> #30269 [codex] disable Nagle on Rendezvous WebSockets @richardopenai

> #30757 fix(core) Remove full text websocket trace @dylan-hurd-oai

> #30643 [codex] bound Rendezvous WebSocket liveness @richardopenai

> #30770 fix(websockets) ignore metadata for incremental requests @dylan-hurd-oai

> #30334 telemetry: log structured direct tool-call timing @bolinfest

> #30796 Fix MIME types for path-backed feedback attachments @btraut-openai

> #31056 fix(install): reuse GitHub release metadata @bolinfest

> #31064 [codex] Read buffering metadata from response events @fc-oai

> #30876 [core] Support interleaved response items @alexi-openai

> #31261 Revert "[core] Support interleaved response items" @alexi-openai

> #31253 Emit exec-policy warnings for freshly loaded thread config @etraut-openai

> #31179 Remove TUI exec-policy core exports @etraut-openai

> #29959 Conditional codex_home dotenv @canvrno-oai

> #30318 core: trace executor skill discovery @anp-oai

> #31276 Revert "Conditional codex_home dotenv" @canvrno-oai

> #30956 refactor(protocol): isolate legacy item fanout @owenlin0

> #30395 [app-server] Include reset-credit details in rate limits @jayp-oai

> #29918 [codex] Flush trailing realtime transcript tail @guinness-oai

> #29697 fix: attribut network requests to the exact exec on linux @jif-oai

> #31303 feat(code-mode): allow disabling V8 JIT @cconger

> #31271 chore: use .worktreeinclude for user Bazel config @anp-oai

> #31308 fix: update crossbeam-epoch for RUSTSEC-2026-0204 @cconger

> #30202 [codex] bundle code mode host in release packages @cconger

> #31284 Warn when configured service tiers are unsupported @etraut-openai

> #31331 Migrate direct HTTP consumers to codex-http-client @bolinfest

> #31337 fix: restore Codex environment setup table @anp-oai

> #31188 Preserve managed exec policy after rules parse errors @etraut-openai

> #31344 exec-server: use virtual time in Noise relay test @bolinfest

> #31296 refactor(protocol): map canonical tool items to legacy events @owenlin0

> #31335 core: route Responses API through system proxy @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.143.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-08-5-collaboration-changes-in-rust-v0-143-0|5 Collaboration changes in rust-v0.143.0]] · Collaboration
- [[Changes/Codex CLI/2026-07-08-5-account-and-access-changes-in-rust-v0-143-0|5 Account and Access changes in rust-v0.143.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-08-66-apps-and-integrations-changes-in-rust-v0-143-0|66 Apps and Integrations changes in rust-v0.143.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-08-14-model-support-changes-in-rust-v0-143-0|14 Model Support changes in rust-v0.143.0]] · Model Support
- [[Changes/Codex CLI/2026-07-08-10-agent-mode-changes-in-rust-v0-143-0|10 Agent Mode changes in rust-v0.143.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-08-27714-app-server-document-thread-and-turn-ids-are-uuid7-owenlin0|♯27714 app-server: document thread and turn IDs are UUID7 @owenlin0]] · Files and Data
- [[Changes/Codex CLI/2026-07-08-13-safety-and-privacy-changes-in-rust-v0-143-0|13 Safety and Privacy changes in rust-v0.143.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-08-28593-codex-suppress-low-usage-remaining-warnings-when-credits-are-available-bro|♯28593 codex suppress low usage remaining warnings when credits are available…]] · Pricing Model
- [[Changes/Codex CLI/2026-07-08-12-context-window-changes-in-rust-v0-143-0|12 Context Window changes in rust-v0.143.0]] · Context Window
- [[Changes/Codex CLI/2026-07-08-30508-revert-make-auto-review-on-request-prompt-more-proactive-dylan-hurd-oai|♯30508 Revert "Make auto-review on-request prompt more proactive" @dylan-hurd-oai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-07-08-2-mobile-and-desktop-changes-in-rust-v0-143-0|2 Mobile and Desktop changes in rust-v0.143.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-08-3-editor-experience-changes-in-rust-v0-143-0|3 Editor Experience changes in rust-v0.143.0]] · Editor Experience
- [[Changes/Codex CLI/2026-07-08-7-developer-workflow-changes-in-rust-v0-143-0|7 Developer Workflow changes in rust-v0.143.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-08-3-image-generation-changes-in-rust-v0-143-0|3 Image Generation changes in rust-v0.143.0]] · Image Generation
- [[Changes/Codex CLI/2026-07-08-2-memory-and-personalization-changes-in-rust-v0-143-0|2 Memory and Personalization changes in rust-v0.143.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-08-remote-plugins-are-now-enabled-by-default-with-richer-catalog-rows-npm-marketpla|Remote plugins are now enabled by default, with richer catalog rows, npm marketplace…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-08-85d38d&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-08-145-other-changes-in-rust-v0-143-0.md%0ACard%20ID%3A%20codex-cli-2026-07-08-85d38d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.143.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->