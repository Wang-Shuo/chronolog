---
card_id: codex-cli-2025-11-04-96b96e
date: '2025-11-04'
description: 'Codex CLI · 2025-11-04 · Other changes: 35 changes in 0.54.0 — **⚠️
  WARNING:** Attempting to pin musl 1.2.5 for DNS fixes in #6189 turned out to be
  the wrong…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cb1d7fe36ad9ed1464d6c29f846b802e87314bc8a28f6bc229f2539d85690af1
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-11-04-96b96e
  comparison: ''
  date: '2025-11-04'
  description: 'Codex CLI — 0.54.0: 35 other changes'
  evidence:
  - quote: '**⚠️ WARNING:** Attempting to pin musl 1.2.5 for DNS fixes in #6189 turned
      out to be the wrong fix. We reverted it in #6222 and published [0.55.0](https://github.com/openai/codex/releases/rust-v0.55.0).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: Otherwise, this release was mostly bugfixes and documentation tweaks.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#6189 fix: pin musl 1.2.5 for DNS fixes (#6189)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#6175 [App-server] v2 for account/updated and account/logout (#6175)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#4453 Follow symlinks during file search (#4453)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#5175 docs: add example config.toml (#5175)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#6180 fix: `--search` shouldn''t show deprecation message (#6180)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#6143 Fixed notify handler so it passes correct `input_messages` details
      (#6143)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#5996 feat: add the time after aborting (#5996)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#5541 tui: refine text area word separator handling (#5541)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#6129 feat: add options to responses-api-proxy to support Azure (#6129)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#6051 Fix rmcp client feature flag reference (#6051)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#5685 Add documentation for slash commands in `docs/slash_commands.md`.
      (#5685)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#6111 fix: improve usage URLs in status card and snapshots (#6111)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#6137 chore(deps): bump actions/upload-artifact from 4 to 5 (#6137)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#4903 fix: pasting api key stray character (#4903)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#6131 Fix incorrect "deprecated" message about experimental config key
      (#6131)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#5649 docs: Fix link anchor and markdown format in advanced guide (#5649)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#5659 Fixing small typo in docs (#5659)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#5935 tui: patch crossterm for better color queries (#5935)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#6050 [codex][app-server] improve error response for client requests (#6050)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#4973 docs: fix broken link in contributing guide (#4973)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#6027 feat: compactor 2 (#6027)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#6052 Add warning on compact (#6052)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#5979 Truncate total tool calls text (#5979)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#4797 docs: "Configuration" is not belongs "Getting started" (#4797)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#4804 chore(deps): bump indexmap from 2.10.0 to 2.11.4 in /codex-rs (#4804)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#4802 chore(deps): bump anyhow from 1.0.99 to 1.0.100 in /codex-rs (#4802)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#4800 chore(deps): bump actions/checkout from 4 to 5 (#4800)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#4801 chore(deps): bump actions/github-script from 7 to 8 (#4801)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#6045 fix: brew upgrade link (#6045)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#6034 test: undo (#6034)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#4426 chore(deps): bump thiserror from 2.0.16 to 2.0.17 in /codex-rs (#4426)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#6010 Update user instruction message format (#6010)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  - quote: '#4266 fix(tui): propagate errors in insert_history_lines_to_writer (#4266)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.54.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 35-other-changes-in-rust-v0-54-0
  source_release: codex-cli-2025-11-04-rust-v0-54-0-github-259667879-e60aafd4
  source_type: github_releases
  theme: uncategorized
  title: 35 other changes in rust-v0.54.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2025-11-04-rust-v0-54-0-github-259667879-e60aafd4|codex-cli-2025-11-04-rust-v0-54-0-github-259667879-e60aafd4]]'
source_type: github_releases
theme: uncategorized
title: 35 other changes in rust-v0.54.0
type: change
---

<!-- chronolog:begin region="header" -->
# 35 other changes in rust-v0.54.0

**Codex CLI** · 2025-11-04 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.54.0) · from [[Releases/Codex CLI/codex-cli-2025-11-04-rust-v0-54-0-github-259667879-e60aafd4|0.54.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **⚠️ WARNING:** Attempting to pin musl 1.2.5 for DNS fixes in #6189 turned out to be the wrong fix. We reverted it in #6222 and published [0.55.0](https://github.com/openai/codex/releases/rust-v0.55.0).

> Otherwise, this release was mostly bugfixes and documentation tweaks.

> #6189 fix: pin musl 1.2.5 for DNS fixes (#6189)

> #6175 [App-server] v2 for account/updated and account/logout (#6175)

> #4453 Follow symlinks during file search (#4453)

> #5175 docs: add example config.toml (#5175)

> #6180 fix: `--search` shouldn't show deprecation message (#6180)

> #6143 Fixed notify handler so it passes correct `input_messages` details (#6143)

> #5996 feat: add the time after aborting (#5996)

> #5541 tui: refine text area word separator handling (#5541)

> #6129 feat: add options to responses-api-proxy to support Azure (#6129)

> #6051 Fix rmcp client feature flag reference (#6051)

> #5685 Add documentation for slash commands in `docs/slash_commands.md`. (#5685)

> #6111 fix: improve usage URLs in status card and snapshots (#6111)

> #6137 chore(deps): bump actions/upload-artifact from 4 to 5 (#6137)

> #4903 fix: pasting api key stray character (#4903)

> #6131 Fix incorrect "deprecated" message about experimental config key (#6131)

> #5649 docs: Fix link anchor and markdown format in advanced guide (#5649)

> #5659 Fixing small typo in docs (#5659)

> #5935 tui: patch crossterm for better color queries (#5935)

> #6050 [codex][app-server] improve error response for client requests (#6050)

> #4973 docs: fix broken link in contributing guide (#4973)

> #6027 feat: compactor 2 (#6027)

> #6052 Add warning on compact (#6052)

> #5979 Truncate total tool calls text (#5979)

> #4797 docs: "Configuration" is not belongs "Getting started" (#4797)

> #4804 chore(deps): bump indexmap from 2.10.0 to 2.11.4 in /codex-rs (#4804)

> #4802 chore(deps): bump anyhow from 1.0.99 to 1.0.100 in /codex-rs (#4802)

> #4800 chore(deps): bump actions/checkout from 4 to 5 (#4800)

> #4801 chore(deps): bump actions/github-script from 7 to 8 (#4801)

> #6045 fix: brew upgrade link (#6045)

> #6034 test: undo (#6034)

> #4426 chore(deps): bump thiserror from 2.0.16 to 2.0.17 in /codex-rs (#4426)

> #6010 Update user instruction message format (#6010)

> #4266 fix(tui): propagate errors in insert_history_lines_to_writer (#4266)

Source: https://github.com/openai/codex/releases/tag/rust-v0.54.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-11-04-5956-parse-the-azure-openai-rate-limit-message-5956|♯5956 Parse the Azure OpenAI rate limit message (♯5956)]] · Apps and Integrations
- [[Changes/Codex CLI/2025-11-04-3-safety-and-privacy-changes-in-rust-v0-54-0|3 Safety and Privacy changes in rust-v0.54.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-11-04-6043-chore-add-shell-serialization-tests-for-json-6043|♯6043 chore: Add shell serialization tests for json (♯6043)]] · Developer Workflow
- [[Changes/Codex CLI/2025-11-04-6159-fix-typo-in-error-message-for-oauth-login-6159|♯6159 Fix typo in error message for OAuth login (♯6159)]] · Account and Access
- [[Changes/Codex CLI/2025-11-04-2-model-support-changes-in-rust-v0-54-0|2 Model Support changes in rust-v0.54.0]] · Model Support
- [[Changes/Codex CLI/2025-11-04-6124-fix-archive-conversation-on-windows-6124|♯6124 Fix "archive conversation" on Windows (♯6124)]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-11-04-6161-include-reasoning-tokens-in-the-context-window-calculation-6161|♯6161 Include reasoning tokens in the context window calculation (♯6161)]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-11-04-96b96e&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-11-04-35-other-changes-in-rust-v0-54-0.md%0ACard%20ID%3A%20codex-cli-2025-11-04-96b96e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.54.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->