---
card_id: codex-cli-2026-03-31-09fb0f
date: '2026-03-31'
description: 'Codex CLI · 2026-03-31 · Other changes: 51 changes in 0.118.0 — Project-local
  `.codex` files are now protected even on first creation, closing a gap where the…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 871349bfa44ee26c9867cf5dc146ada7e0a12a6bf286ced6d607857aed6adeb1
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-31-09fb0f
  comparison: ''
  date: '2026-03-31'
  description: 'Codex CLI — 0.118.0: 51 other changes'
  evidence:
  - quote: Project-local `.codex` files are now protected even on first creation,
      closing a gap where the initial write could bypass normal approval checks. (#15067)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15791 fix: resolve bwrap from trusted PATH entry @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15811 app-server: Split transport module @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15897 sandboxing: use OsString for SandboxCommand.program @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15898 chore: move bwrap config helpers into dedicated module @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15909 fix(network-proxy): fail closed on network-proxy DNS lookup errors
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#14495 Preserve bazel repository cache in github actions @siggisim'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15522 bazel: re-organize bazelrc @sluongng'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15933 fix: use matrix.target instead of matrix.os for actions/cache build
      action @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15948 fix: increase timeout for rust-ci to 45 minutes for now @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15921 [app-server-protocol] introduce generic ClientResponse for app-server-protocol
      @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15120 chore: refactor network permissions to use explicit domain and
      unix socket rule maps @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15876 chore: drop useless stuff @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15986 feat: spawn v2 make task name as mandatory @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16001 Use codex-utils-template for review prompts @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15996 Use codex-utils-template for search tool descriptions @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15999 Use codex-utils-template for review exit XML @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15944 codex-tools: extract dynamic tool adapters @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15955 ci: add Bazel clippy workflow for codex-rs @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15953 codex-tools: introduce named tool definitions @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16027 fix: fix Windows CI regression introduced in #15999 @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16030 don''t include redundant write roots in apply_patch @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15922 Remove the legacy TUI split @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15828 [codex] Pin GitHub Actions workflow references @hintz-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16050 Fix tui_app_server resume-by-name lookup regression @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15917 Support Codex CLI stdin piping for `codex exec` @jliccini'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16063 refactor: rewrite argument-comment lint wrappers in Python @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15952 bazel: enable the full Windows gnullvm CI path @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16071 fix: clean up remaining Windows argument-comment-lint violations
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16072 ci: split fast PR Rust CI from full post-merge Cargo CI @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16074 bazel: add Windows gnullvm stack flags to unit test binaries @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16112 Update PR babysitter skill for review replies and resolution @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16104 Rename tui_app_server to tui @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16106 build: migrate argument-comment-lint to a native Bazel aspect @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16115 Remove remaining custom prompt support @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16116 Remove the codex-tui app-server originator workaround @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16129 codex-tools: extract configured tool specs @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16130 ci: keep rust-ci-full Windows argument-comment-lint on packaged
      wrapper @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16132 codex-tools: extract code mode tool spec adapters @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16136 ci: use BuildBuddy for rust-ci-full non-Windows argument-comment-lint
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16137 exec: make review-policy tests hermetic @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16138 codex-tools: extract local host tool specs @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16154 codex-tools: extract utility tool specs @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16010 feat: add mailbox concept for wait @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16237 fix: ma1 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16193 codex-tools: extract discovery tool specs @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16253 fix: close Bazel argument-comment-lint CI gaps @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16225 [codex-analytics] refactor analytics to use reducer architecture
      @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16279 Update code mode exec() instructions @andmis'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16120 ci: run Windows argument-comment-lint via native Bazel @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16287 auth: let AuthManager own external bearer auth @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 51-other-changes-in-rust-v0-118-0
  source_release: codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6
  source_type: github_releases
  theme: uncategorized
  title: 51 other changes in rust-v0.118.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6|codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6]]'
source_type: github_releases
theme: uncategorized
title: 51 other changes in rust-v0.118.0
type: change
---

<!-- chronolog:begin region="header" -->
# 51 other changes in rust-v0.118.0

**Codex CLI** · 2026-03-31 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.118.0) · from [[Releases/Codex CLI/codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6|0.118.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Project-local `.codex` files are now protected even on first creation, closing a gap where the initial write could bypass normal approval checks. (#15067)

> #15791 fix: resolve bwrap from trusted PATH entry @viyatb-oai

> #15811 app-server: Split transport module @euroelessar

> #15897 sandboxing: use OsString for SandboxCommand.program @bolinfest

> #15898 chore: move bwrap config helpers into dedicated module @viyatb-oai

> #15909 fix(network-proxy): fail closed on network-proxy DNS lookup errors @viyatb-oai

> #14495 Preserve bazel repository cache in github actions @siggisim

> #15522 bazel: re-organize bazelrc @sluongng

> #15933 fix: use matrix.target instead of matrix.os for actions/cache build action @bolinfest

> #15948 fix: increase timeout for rust-ci to 45 minutes for now @bolinfest

> #15921 [app-server-protocol] introduce generic ClientResponse for app-server-protocol @rhan-oai

> #15120 chore: refactor network permissions to use explicit domain and unix socket rule maps @celia-oai

> #15876 chore: drop useless stuff @jif-oai

> #15986 feat: spawn v2 make task name as mandatory @jif-oai

> #16001 Use codex-utils-template for review prompts @jif-oai

> #15996 Use codex-utils-template for search tool descriptions @jif-oai

> #15999 Use codex-utils-template for review exit XML @jif-oai

> #15944 codex-tools: extract dynamic tool adapters @bolinfest

> #15955 ci: add Bazel clippy workflow for codex-rs @bolinfest

> #15953 codex-tools: introduce named tool definitions @bolinfest

> #16027 fix: fix Windows CI regression introduced in #15999 @bolinfest

> #16030 don't include redundant write roots in apply_patch @iceweasel-oai

> #15922 Remove the legacy TUI split @etraut-openai

> #15828 [codex] Pin GitHub Actions workflow references @hintz-openai

> #16050 Fix tui_app_server resume-by-name lookup regression @etraut-openai

> #15917 Support Codex CLI stdin piping for `codex exec` @jliccini

> #16063 refactor: rewrite argument-comment lint wrappers in Python @bolinfest

> #15952 bazel: enable the full Windows gnullvm CI path @bolinfest

> #16071 fix: clean up remaining Windows argument-comment-lint violations @bolinfest

> #16072 ci: split fast PR Rust CI from full post-merge Cargo CI @bolinfest

> #16074 bazel: add Windows gnullvm stack flags to unit test binaries @bolinfest

> #16112 Update PR babysitter skill for review replies and resolution @etraut-openai

> #16104 Rename tui_app_server to tui @etraut-openai

> #16106 build: migrate argument-comment-lint to a native Bazel aspect @bolinfest

> #16115 Remove remaining custom prompt support @etraut-openai

> #16116 Remove the codex-tui app-server originator workaround @etraut-openai

> #16129 codex-tools: extract configured tool specs @bolinfest

> #16130 ci: keep rust-ci-full Windows argument-comment-lint on packaged wrapper @bolinfest

> #16132 codex-tools: extract code mode tool spec adapters @bolinfest

> #16136 ci: use BuildBuddy for rust-ci-full non-Windows argument-comment-lint @bolinfest

> #16137 exec: make review-policy tests hermetic @bolinfest

> #16138 codex-tools: extract local host tool specs @bolinfest

> #16154 codex-tools: extract utility tool specs @bolinfest

> #16010 feat: add mailbox concept for wait @jif-oai

> #16237 fix: ma1 @jif-oai

> #16193 codex-tools: extract discovery tool specs @bolinfest

> #16253 fix: close Bazel argument-comment-lint CI gaps @bolinfest

> #16225 [codex-analytics] refactor analytics to use reducer architecture @rhan-oai

> #16279 Update code mode exec() instructions @andmis

> #16120 ci: run Windows argument-comment-lint via native Bazel @bolinfest

> #16287 auth: let AuthManager own external bearer auth @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.118.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-31-16286-auth-generalize-external-auth-tokens-for-bearer-only-sources-bolinfest|♯16286 auth: generalize external auth tokens for bearer-only sources @bolinfest]] · Context Window
- [[Changes/Codex CLI/2026-03-31-16021-fix-copy-regression-in-tui-app-server-turn-completion-etraut-openai|♯16021 Fix /copy regression in tui_app_server turn completion @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-03-31-12-apps-and-integrations-changes-in-rust-v0-118-0|12 Apps and Integrations changes in rust-v0.118.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-31-16114-remove-tui-voice-transcription-feature-etraut-openai|♯16114 Remove TUI voice transcription feature @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-31-3-interface-experience-changes-in-rust-v0-118-0|3 Interface Experience changes in rust-v0.118.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-31-4-account-and-access-changes-in-rust-v0-118-0|4 Account and Access changes in rust-v0.118.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-31-3-developer-workflow-changes-in-rust-v0-118-0|3 Developer Workflow changes in rust-v0.118.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-31-15934-add-usage-based-business-plan-types-bwanner-oai|♯15934 Add usage-based business plan types @bwanner-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-03-31-7-safety-and-privacy-changes-in-rust-v0-118-0|7 Safety and Privacy changes in rust-v0.118.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-31-4-agent-mode-changes-in-rust-v0-118-0|4 Agent Mode changes in rust-v0.118.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-31-7-mobile-and-desktop-changes-in-rust-v0-118-0|7 Mobile and Desktop changes in rust-v0.118.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-31-4-collaboration-changes-in-rust-v0-118-0|4 Collaboration changes in rust-v0.118.0]] · Collaboration
- [[Changes/Codex CLI/2026-03-31-5-model-support-changes-in-rust-v0-118-0|5 Model Support changes in rust-v0.118.0]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-31-09fb0f&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-31-51-other-changes-in-rust-v0-118-0.md%0ACard%20ID%3A%20codex-cli-2026-03-31-09fb0f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.118.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->