---
card_id: codex-cli-2026-01-27-3f84b6
date: '2026-01-27'
description: 'Codex CLI · 2026-01-27 · Other changes: 48 changes in 0.92.0 — API v2
  threads can now inject dynamic tools at startup and route their calls/responses…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a65c4dd1f39d258d95a545124dbd0e0c5b948fe10362e9d2b118ef30ee2da49e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-27-3f84b6
  comparison: ''
  date: '2026-01-27'
  description: 'Codex CLI — 0.92.0: 48 other changes'
  evidence:
  - quote: API v2 threads can now inject dynamic tools at startup and route their
      calls/responses end-to-end through the server and core tool pipeline. (#9539)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: Introduced a `thread/unarchive` RPC to restore archived rollouts back into
      active sessions. (#9843)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '`request_user_input` is now rejected outside Plan/Pair modes to prevent
      invalid tool calls. (#9955)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: Release packaging now consistently writes the bundle zip to `dist/`. (#9934)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: 'Updated key dependencies in the Rust workspace (including `axum`, `tracing`,
      `globset`, and `tokio-test`). (#9880, #9882, #9883, #9884)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: 'Aligned feature stage naming with public maturity stages and added clearer
      warnings for underdevelopment features. (#9929, #9954)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9850 chore: remove extra newline in println @SohailRaoufi'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9868 Adjust modes masks @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9874 Prompt @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9877 Plan prompt @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9539 feat: dynamic tools injection @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9789 Fix flakey resume test @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9784 Fix flakey conversation flow test @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9918 feat: explorer collab @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9899 feat: disable collab at max depth @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9916 Fix up config disabled err msg @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9890 Feat: add isOther to question returned by request user input tool
      @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9817 feat: codex exec mapping of collab tools @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9776 fix: attempt to reduce high cpu usage when using collab @eugeneoden'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9928 prompt @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9925 chore: update interrupt message @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9843 Add thread/unarchive to restore archived rollouts @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9929 Aligned feature stage names with public feature maturity stages
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9934 ensure codex bundle zip is created in dist/ @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9897 [app-server] feat: add filtering on thread list @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9943 plan prompt @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9880 chore(deps): bump tracing from 0.1.43 to 0.1.44 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9882 chore(deps): bump tokio-test from 0.4.4 to 0.4.5 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9883 chore(deps): bump axum from 0.8.4 to 0.8.8 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9884 chore(deps): bump globset from 0.4.16 to 0.4.18 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9823 fix: use `brew upgrade --cask codex` to avoid warnings and ambiguity
      @JBallin'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9951 fix: try to fix freezes 2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9955 Reject request_user_input outside Plan/Pair @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9933 Updated contribution guidelines @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9892 Reuse ChatComposer in request_user_input overlay @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9957 NIT larger buffer @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9953 feat: load interface metadata from SKILL.json @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9954 Warn users on enabling underdevelopment features @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9961 Use test_codex more @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9966 plan prompt v7 @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9968 Improve plan mode prompt @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9969 prompt final @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9475 Fix `resume --last` with `--json` option @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9970 prompt @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9975 plan prompt @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9971 tui: wrapping user input questions @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9977 make plan prompt less detailed @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  - quote: '#9759 Fix: cap aggregated exec output consistently @Kbediako'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.92.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 48-other-changes-in-rust-v0-92-0
  source_release: codex-cli-2026-01-27-rust-v0-92-0-github-280265755-5634ff7c
  source_type: github_releases
  theme: uncategorized
  title: 48 other changes in rust-v0.92.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-27-rust-v0-92-0-github-280265755-5634ff7c|codex-cli-2026-01-27-rust-v0-92-0-github-280265755-5634ff7c]]'
source_type: github_releases
theme: uncategorized
title: 48 other changes in rust-v0.92.0
type: change
---

<!-- chronolog:begin region="header" -->
# 48 other changes in rust-v0.92.0

**Codex CLI** · 2026-01-27 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.92.0) · from [[Releases/Codex CLI/codex-cli-2026-01-27-rust-v0-92-0-github-280265755-5634ff7c|0.92.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> API v2 threads can now inject dynamic tools at startup and route their calls/responses end-to-end through the server and core tool pipeline. (#9539)

> Introduced a `thread/unarchive` RPC to restore archived rollouts back into active sessions. (#9843)

> `request_user_input` is now rejected outside Plan/Pair modes to prevent invalid tool calls. (#9955)

> Release packaging now consistently writes the bundle zip to `dist/`. (#9934)

> Updated key dependencies in the Rust workspace (including `axum`, `tracing`, `globset`, and `tokio-test`). (#9880, #9882, #9883, #9884)

> Aligned feature stage naming with public maturity stages and added clearer warnings for underdevelopment features. (#9929, #9954)

> #9850 chore: remove extra newline in println @SohailRaoufi

> #9868 Adjust modes masks @aibrahim-oai

> #9874 Prompt @aibrahim-oai

> #9877 Plan prompt @aibrahim-oai

> #9539 feat: dynamic tools injection @jif-oai

> #9789 Fix flakey resume test @gt-oai

> #9784 Fix flakey conversation flow test @gt-oai

> #9918 feat: explorer collab @jif-oai

> #9899 feat: disable collab at max depth @jif-oai

> #9916 Fix up config disabled err msg @gt-oai

> #9890 Feat: add isOther to question returned by request user input tool @shijie-oai

> #9817 feat: codex exec mapping of collab tools @jif-oai

> #9776 fix: attempt to reduce high cpu usage when using collab @eugeneoden

> #9928 prompt @aibrahim-oai

> #9925 chore: update interrupt message @jif-oai

> #9843 Add thread/unarchive to restore archived rollouts @charley-oai

> #9929 Aligned feature stage names with public feature maturity stages @etraut-openai

> #9934 ensure codex bundle zip is created in dist/ @iceweasel-oai

> #9897 [app-server] feat: add filtering on thread list @jif-oai

> #9943 plan prompt @aibrahim-oai

> #9880 chore(deps): bump tracing from 0.1.43 to 0.1.44 in /codex-rs @dependabot

> #9882 chore(deps): bump tokio-test from 0.4.4 to 0.4.5 in /codex-rs @dependabot

> #9883 chore(deps): bump axum from 0.8.4 to 0.8.8 in /codex-rs @dependabot

> #9884 chore(deps): bump globset from 0.4.16 to 0.4.18 in /codex-rs @dependabot

> #9823 fix: use `brew upgrade --cask codex` to avoid warnings and ambiguity @JBallin

> #9951 fix: try to fix freezes 2 @jif-oai

> #9955 Reject request_user_input outside Plan/Pair @charley-oai

> #9933 Updated contribution guidelines @etraut-openai

> #9892 Reuse ChatComposer in request_user_input overlay @aibrahim-oai

> #9957 NIT larger buffer @jif-oai

> #9953 feat: load interface metadata from SKILL.json @alexsong-oai

> #9954 Warn users on enabling underdevelopment features @aibrahim-oai

> #9961 Use test_codex more @pakrym-oai

> #9966 plan prompt v7 @aibrahim-oai

> #9968 Improve plan mode prompt @aibrahim-oai

> #9969 prompt final @aibrahim-oai

> #9475 Fix `resume --last` with `--json` option @etraut-openai

> #9970 prompt @aibrahim-oai

> #9975 plan prompt @aibrahim-oai

> #9971 tui: wrapping user input questions @aibrahim-oai

> #9977 make plan prompt less detailed @aibrahim-oai

> #9759 Fix: cap aggregated exec output consistently @Kbediako

Source: https://github.com/openai/codex/releases/tag/rust-v0.92.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-27-5-search-and-browsing-changes-in-rust-v0-92-0|5 Search and Browsing changes in rust-v0.92.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-01-27-9818-feat-rebase-multi-agent-tui-on-config-snapshot-jif-oai|♯9818 feat: rebase multi-agent tui on config_snapshot @jif-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-01-27-refreshed-protocol-mcp-docs-to-reflect-thread-unarchive-and-the-updated-request|Refreshed protocol/MCP docs to reflect thread/unarchive and the updated…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-27-3-interface-experience-changes-in-rust-v0-92-0|3 Interface Experience changes in rust-v0.92.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-27-2-developer-workflow-changes-in-rust-v0-92-0|2 Developer Workflow changes in rust-v0.92.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-27-2-safety-and-privacy-changes-in-rust-v0-92-0|2 Safety and Privacy changes in rust-v0.92.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-27-2-account-and-access-changes-in-rust-v0-92-0|2 Account and Access changes in rust-v0.92.0]] · Account and Access
- [[Changes/Codex CLI/2026-01-27-2-collaboration-changes-in-rust-v0-92-0|2 Collaboration changes in rust-v0.92.0]] · Collaboration
- [[Changes/Codex CLI/2026-01-27-9718-feat-tui-personality-dylan-hurd-oai|♯9718 feat(tui) /personality @dylan-hurd-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-01-27-2-model-support-changes-in-rust-v0-92-0|2 Model Support changes in rust-v0.92.0]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-27-3f84b6&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-27-48-other-changes-in-rust-v0-92-0.md%0ACard%20ID%3A%20codex-cli-2026-01-27-3f84b6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.92.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->