---
card_id: codex-cli-2026-01-31-95e942
date: '2026-01-31'
description: 'Codex CLI · 2026-01-31 · Other changes: 97 changes in 0.93.0 — Added
  an optional SOCKS5 proxy listener with policy enforcement and config gating. (#9803)'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f50dd9632d466cb910a60fab42574d45019e459e9bc5ccaf04f293efffa0dd2f
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-31-95e942
  comparison: ''
  date: '2026-01-31'
  description: 'Codex CLI — 0.93.0: 97 other changes'
  evidence:
  - quote: Added an optional SOCKS5 proxy listener with policy enforcement and config
      gating. (#9803)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: 'Plan mode now streams proposed plans into a dedicated TUI view, plus a
      feature-gated `/plan` shortcut for quick mode switching. (#9786, #10103)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: 'Introduced a SQLite-backed log database with an improved logs client,
      thread-id filtering, retention, and heuristic coloring. (#10086, #10087, #10150,
      #10151, #10229, #10228)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: Input history recall now restores local image attachments and rich text
      elements. (#9628)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: Resuming a thread no longer updates `updated_at` until the first turn actually
      starts. (#9950)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: Connections fall back to HTTP when WebSocket proxies fail. (#10139)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: Documented app-server AuthMode usage and behavior. (#10191)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: Upgraded the Rust toolchain to 1.93. (#10080)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: 'Updated pnpm versions used in the repo. (#9992, #10161)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: 'Bazel build and runfiles handling improvements, including remote cache
      compression. (#10079, #10098, #10102, #10104)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9988 nit: better tool description @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9991 nit: better unused prompt @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9994 chore: clean orchestrator prompt @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10001 backend-client: add get_config_requirements_file @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9993 description in role type @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9803 feat(network-proxy): add a SOCKS5 proxy with policy enforcement
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10009 chore: introduce *Args types for new() methods @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10007 Remove load from SKILL.toml fallback @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9949 Ask user question UI footer improvements @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10041 fix: allow unknown fields on Notice in schema @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9628 Restore image attachments/text elements when recalling input history
      (Up/Down) @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9986 fix(core) info cleanup @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9941 error code/msg details for failed elevated setup @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9489 feat(core) RequestRule @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10026 Add exec policy TOML representation @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9821 feat: codex exec auto-subscribe to new threads @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10004 feat: sqlite 1 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10083 feat: sort metadata by date @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10079 [bazel] Enable remote cache compression @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10025 Refine request_user_input TUI interactions and option UX @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10080 Upgrade to rust 1.93 @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9939 file-search: improve file query perf @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10043 Added `tui.notifications_method` config option @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10104 [bazel] Fix the build @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10102 default enable compression, update test helpers @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10098 [bazel] Improve runfiles handling @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10125 emit a metric when we can''t spawn powershell @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10138 fix: remove references to corepack @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10086 feat: add log db @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10089 feat: async backfill @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10087 feat: log db client @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10149 chore: improve client @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10161 nit: update npm @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10150 feat: adding thread ID to logs + filter in the client @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10151 feat: add log retention and delete them after 90 days @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10152 chore: unify log queries @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10171 feat: reduce span exposition @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10139 Fall back to http when websockets fail @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10140 chore: ensure pnpm-workspace.yaml is up-to-date @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9017 Better handling skill depdenencies on ENV VAR. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10180 Add features enable/disable subcommands @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10184 fix: /approvals -> /permissions @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10179 Remove WebSocket wire format @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10012 feat(app-server): support external auth mode @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10130 [feat] persist dynamic tools in session rollout file @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10181 add error messages for the go plan type @willwang-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10198 feat(tui): route employee feedback follow-ups to internal link
      @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10194 load from yaml @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10154 feat: add output to `/ps` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10217 nit: actually run tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10177 Add community links to startup tooltips @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10210 Chore: plan mode do not include free form question and always include
      isOther @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10218 feat: backfill timing metric @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10220 chore: unify metric @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#8991 Conversation naming @pap-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10167 Fetch Requirements from cloud @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10225 explorer prompt @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10232 chore: do not clean the DB anymore @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10229 feat: improve logs client @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10228 feat: heuristic coloring of logs @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10237 nit: fix db with multiple metadata lines @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10208 feat: refactor CodexAuth so invalid state cannot be represented
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10211 chore(feature) Experimental: Smart Approvals @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10190 Load exec policy rules from requirements @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10195 plan mode: add TL;DR checkpoint and client behavior note @baumann-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10239 chore: fix the build breakage that came from a merge race @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9786 Plan mode: stream proposed plans, emit plan items, and render in
      TUI @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10063 Tui: hide Code mode footer label @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10244 chore: rename ChatGpt -> Chatgpt in type names @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10238 Plan mode prompt @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10251 Fix deploy @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10255 plan prompt @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10253 Make plan highlight use popup grey background @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10207 Skip loading codex home as project layer @daniel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10256 Update copy @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10262 Fix main @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10267 Update announcement_tip.toml @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10240 file-search: multi-root walk @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#9279 fix: update file search directory when session CWD changes @yuvrajangadsingh'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10249 Validate CODEX_HOME before resolving @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10272 chore: implement Mul for TruncationPolicy @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10241 Wire up cloud reqs in exec, app-server @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10263 Add enforce_residency to requirements @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10276 add missing fields to WebSearchAction and update app-server types
      @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10283 Turn on cloud requirements for business too @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10287 Fix minor typos in comments and documentation @ruyut'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  - quote: '#10286 feat(core) Smart approvals on @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.93.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 97-other-changes-in-rust-v0-93-0
  source_release: codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8
  source_type: github_releases
  theme: uncategorized
  title: 97 other changes in rust-v0.93.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8|codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8]]'
source_type: github_releases
theme: uncategorized
title: 97 other changes in rust-v0.93.0
type: change
---

<!-- chronolog:begin region="header" -->
# 97 other changes in rust-v0.93.0

**Codex CLI** · 2026-01-31 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.93.0) · from [[Releases/Codex CLI/codex-cli-2026-01-31-rust-v0-93-0-github-281755443-684a63d8|0.93.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added an optional SOCKS5 proxy listener with policy enforcement and config gating. (#9803)

> Plan mode now streams proposed plans into a dedicated TUI view, plus a feature-gated `/plan` shortcut for quick mode switching. (#9786, #10103)

> Introduced a SQLite-backed log database with an improved logs client, thread-id filtering, retention, and heuristic coloring. (#10086, #10087, #10150, #10151, #10229, #10228)

> Input history recall now restores local image attachments and rich text elements. (#9628)

> Resuming a thread no longer updates `updated_at` until the first turn actually starts. (#9950)

> Connections fall back to HTTP when WebSocket proxies fail. (#10139)

> Documented app-server AuthMode usage and behavior. (#10191)

> Upgraded the Rust toolchain to 1.93. (#10080)

> Updated pnpm versions used in the repo. (#9992, #10161)

> Bazel build and runfiles handling improvements, including remote cache compression. (#10079, #10098, #10102, #10104)

> #9988 nit: better tool description @jif-oai

> #9991 nit: better unused prompt @jif-oai

> #9994 chore: clean orchestrator prompt @jif-oai

> #10001 backend-client: add get_config_requirements_file @gt-oai

> #9993 description in role type @jif-oai

> #9803 feat(network-proxy): add a SOCKS5 proxy with policy enforcement @viyatb-oai

> #10009 chore: introduce *Args types for new() methods @bolinfest

> #10007 Remove load from SKILL.toml fallback @alexsong-oai

> #9949 Ask user question UI footer improvements @charley-oai

> #10041 fix: allow unknown fields on Notice in schema @sayan-oai

> #9628 Restore image attachments/text elements when recalling input history (Up/Down) @charley-oai

> #9986 fix(core) info cleanup @dylan-hurd-oai

> #9941 error code/msg details for failed elevated setup @iceweasel-oai

> #9489 feat(core) RequestRule @dylan-hurd-oai

> #10026 Add exec policy TOML representation @gt-oai

> #9821 feat: codex exec auto-subscribe to new threads @jif-oai

> #10004 feat: sqlite 1 @jif-oai

> #10083 feat: sort metadata by date @jif-oai

> #10079 [bazel] Enable remote cache compression @zbarsky-openai

> #10025 Refine request_user_input TUI interactions and option UX @charley-oai

> #10080 Upgrade to rust 1.93 @zbarsky-openai

> #9939 file-search: improve file query perf @nornagon-openai

> #10043 Added `tui.notifications_method` config option @etraut-openai

> #10104 [bazel] Fix the build @zbarsky-openai

> #10102 default enable compression, update test helpers @sayan-oai

> #10098 [bazel] Improve runfiles handling @zbarsky-openai

> #10125 emit a metric when we can't spawn powershell @iceweasel-oai

> #10138 fix: remove references to corepack @bolinfest

> #10086 feat: add log db @jif-oai

> #10089 feat: async backfill @jif-oai

> #10087 feat: log db client @jif-oai

> #10149 chore: improve client @jif-oai

> #10161 nit: update npm @jif-oai

> #10150 feat: adding thread ID to logs + filter in the client @jif-oai

> #10151 feat: add log retention and delete them after 90 days @jif-oai

> #10152 chore: unify log queries @jif-oai

> #10171 feat: reduce span exposition @jif-oai

> #10139 Fall back to http when websockets fail @pakrym-oai

> #10140 chore: ensure pnpm-workspace.yaml is up-to-date @bolinfest

> #9017 Better handling skill depdenencies on ENV VAR. @xl-openai

> #10180 Add features enable/disable subcommands @joshka-oai

> #10184 fix: /approvals -> /permissions @bolinfest

> #10179 Remove WebSocket wire format @pakrym-oai

> #10012 feat(app-server): support external auth mode @owenlin0

> #10130 [feat] persist dynamic tools in session rollout file @celia-oai

> #10181 add error messages for the go plan type @willwang-openai

> #10198 feat(tui): route employee feedback follow-ups to internal link @joshka-oai

> #10194 load from yaml @alexsong-oai

> #10154 feat: add output to `/ps` @jif-oai

> #10217 nit: actually run tests @jif-oai

> #10177 Add community links to startup tooltips @joshka-oai

> #10210 Chore: plan mode do not include free form question and always include isOther @shijie-oai

> #10218 feat: backfill timing metric @jif-oai

> #10220 chore: unify metric @jif-oai

> #8991 Conversation naming @pap-openai

> #10167 Fetch Requirements from cloud @gt-oai

> #10225 explorer prompt @jif-oai

> #10232 chore: do not clean the DB anymore @jif-oai

> #10229 feat: improve logs client @jif-oai

> #10228 feat: heuristic coloring of logs @jif-oai

> #10237 nit: fix db with multiple metadata lines @jif-oai

> #10208 feat: refactor CodexAuth so invalid state cannot be represented @bolinfest

> #10211 chore(feature) Experimental: Smart Approvals @dylan-hurd-oai

> #10190 Load exec policy rules from requirements @gt-oai

> #10195 plan mode: add TL;DR checkpoint and client behavior note @baumann-oai

> #10239 chore: fix the build breakage that came from a merge race @bolinfest

> #9786 Plan mode: stream proposed plans, emit plan items, and render in TUI @charley-oai

> #10063 Tui: hide Code mode footer label @charley-oai

> #10244 chore: rename ChatGpt -> Chatgpt in type names @bolinfest

> #10238 Plan mode prompt @aibrahim-oai

> #10251 Fix deploy @charley-oai

> #10255 plan prompt @aibrahim-oai

> #10253 Make plan highlight use popup grey background @charley-oai

> #10207 Skip loading codex home as project layer @daniel-oai

> #10256 Update copy @pakrym-oai

> #10262 Fix main @pakrym-oai

> #10267 Update announcement_tip.toml @pakrym-oai

> #10240 file-search: multi-root walk @nornagon-openai

> #9279 fix: update file search directory when session CWD changes @yuvrajangadsingh

> #10249 Validate CODEX_HOME before resolving @etraut-openai

> #10272 chore: implement Mul for TruncationPolicy @bolinfest

> #10241 Wire up cloud reqs in exec, app-server @gt-oai

> #10263 Add enforce_residency to requirements @gt-oai

> #10276 add missing fields to WebSearchAction and update app-server types @sayan-oai

> #10283 Turn on cloud requirements for business too @gt-oai

> #10287 Fix minor typos in comments and documentation @ruyut

> #10286 feat(core) Smart approvals on @dylan-hurd-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.93.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-31-6-context-window-changes-in-rust-v0-93-0|6 Context Window changes in rust-v0.93.0]] · Context Window
- [[Changes/Codex CLI/2026-01-31-6-memory-and-personalization-changes-in-rust-v0-93-0|6 Memory and Personalization changes in rust-v0.93.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-01-31-10191-chore-app-server-document-authmode-owenlin0|♯10191 chore(app-server): document AuthMode @owenlin0]] · Files and Data
- [[Changes/Codex CLI/2026-01-31-10011-really-fix-pwd-for-windows-codex-zip-iceweasel-oai|♯10011 really fix pwd for windows codex zip @iceweasel-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-31-9654-show-oauth-error-descriptions-in-callback-responses-blevy-oai|♯9654 Show OAuth error descriptions in callback responses @blevy-oai]] · Account and Access
- [[Changes/Codex CLI/2026-01-31-3-interface-experience-changes-in-rust-v0-93-0|3 Interface Experience changes in rust-v0.93.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-31-3-reliability-and-performance-changes-in-rust-v0-93-0|3 Reliability and Performance changes in rust-v0.93.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-01-31-10118-codex-cli-show-model-capacity-guidance-on-429-ccy-oai|♯10118 CodexCLI Show model-capacity guidance on 429 @ccy-oai]] · Model Support
- [[Changes/Codex CLI/2026-01-31-6-developer-workflow-changes-in-rust-v0-93-0|6 Developer Workflow changes in rust-v0.93.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-31-10030-clarify-external-editor-env-var-message-joshka-oai|♯10030 Clarify external editor env var message @joshka-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-01-31-smart-approvals-are-now-enabled-by-default-with-explicit-approval-prompts-for-mc|Smart approvals are now enabled by default, with explicit approval prompts for MCP…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-31-4-safety-and-privacy-changes-in-rust-v0-93-0|4 Safety and Privacy changes in rust-v0.93.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-31-14-apps-and-integrations-changes-in-rust-v0-93-0|14 Apps and Integrations changes in rust-v0.93.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-31-3-search-and-browsing-changes-in-rust-v0-93-0|3 Search and Browsing changes in rust-v0.93.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-01-31-added-apps-to-browse-connectors-in-tui-and-insertion-for-app-prompts-9728|Added /apps to browse connectors in TUI and $ insertion for app prompts]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-31-95e942&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-31-97-other-changes-in-rust-v0-93-0.md%0ACard%20ID%3A%20codex-cli-2026-01-31-95e942%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.93.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->