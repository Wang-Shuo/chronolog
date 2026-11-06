---
card_id: codex-cli-2025-08-20-8360b0
date: '2025-08-20'
description: 'Codex CLI · 2025-08-20 · Account and Access: 9 changes in 0.23.0 — Auth
  improvements: show login options when not signed in with ChatGPT (#2440) and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 874
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5955178eda5072865592752ba5bfcdc786628501901784998826c4160fdb2270
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-08-20-8360b0
  comparison: ''
  date: '2025-08-20'
  description: 'Codex CLI — 0.23.0: 9 Account and Access changes'
  evidence:
  - quote: 'Auth improvements: show login options when not signed in with ChatGPT
      (#2440) and auto‑refresh ChatGPT auth token (#2484).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.23.0
  - quote: '[#2373](https://github.com/openai/codex/pull/2373) Added MCP server command
      to enable authentication using ChatGPT'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.23.0
  - quote: '[#2388](https://github.com/openai/codex/pull/2388) fix: refactor login/src/server.rs
      so process_request() is a separate function'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.23.0
  - quote: '[#2393](https://github.com/openai/codex/pull/2393) fix: async-ify login
      flow'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.23.0
  - quote: '[#2395](https://github.com/openai/codex/pull/2395) fix: eliminate ServerOptions.login_timeout
      and use tokio::time::timeout()'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.23.0
  - quote: '[#2398](https://github.com/openai/codex/pull/2398) fix: reduce references
      to Server in codex-login crate'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.23.0
  - quote: '[#2399](https://github.com/openai/codex/pull/2399) fix: remove shutdown_flag
      param to run_login_server()'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.23.0
  - quote: '[#2440](https://github.com/openai/codex/pull/2440) Show login options
      when not signed in with ChatGPT'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.23.0
  - quote: '[#2475](https://github.com/openai/codex/pull/2475) Fix: Sign in appear
      even if using other providers.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.23.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-account-and-access-changes-in-rust-v0-23-0
  source_release: codex-cli-2025-08-20-rust-v0-23-0-github-241091696-29f8dece
  source_type: github_releases
  theme: account-access
  title: 9 Account and Access changes in rust-v0.23.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-08-14-7-account-and-access-changes-in-v0-1-21|7 Account
  and Access changes in v0.1.21]]'
- '[[Changes/Codex CLI/2025-08-15-https-github-com-openai-codex-pull-2294-moves-the-login-server-from-python-to-ru|(source
  link) moves the login server from Python…]]'
- '[[Changes/Gemini CLI/2025-08-18-feat-oauth-make-oauth-client-a-singleton-to-survive-cache-failures-by-mboshernit|feat(oauth):
  Make oauth client a singleton to survive cache failures]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-08-20-rust-v0-23-0-github-241091696-29f8dece|codex-cli-2025-08-20-rust-v0-23-0-github-241091696-29f8dece]]'
source_type: github_releases
theme: account-access
title: 9 Account and Access changes in rust-v0.23.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Account and Access changes in rust-v0.23.0

**Codex CLI** · 2025-08-20 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.23.0) · from [[Releases/Codex CLI/codex-cli-2025-08-20-rust-v0-23-0-github-241091696-29f8dece|0.23.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Auth improvements: show login options when not signed in with ChatGPT (#2440) and auto‑refresh ChatGPT auth token (#2484).

> [#2373](https://github.com/openai/codex/pull/2373) Added MCP server command to enable authentication using ChatGPT

> [#2388](https://github.com/openai/codex/pull/2388) fix: refactor login/src/server.rs so process_request() is a separate function

> [#2393](https://github.com/openai/codex/pull/2393) fix: async-ify login flow

> [#2395](https://github.com/openai/codex/pull/2395) fix: eliminate ServerOptions.login_timeout and use tokio::time::timeout()

> [#2398](https://github.com/openai/codex/pull/2398) fix: reduce references to Server in codex-login crate

> [#2399](https://github.com/openai/codex/pull/2399) fix: remove shutdown_flag param to run_login_server()

> [#2440](https://github.com/openai/codex/pull/2440) Show login options when not signed in with ChatGPT

> [#2475](https://github.com/openai/codex/pull/2475) Fix: Sign in appear even if using other providers.

Source: https://github.com/openai/codex/releases/tag/rust-v0.23.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-08-20-3-editor-experience-changes-in-rust-v0-23-0|3 Editor Experience changes in rust-v0.23.0]] · Editor Experience
- [[Changes/Codex CLI/2025-08-20-2464-https-github-com-openai-codex-pull-2464-docs-document-writable-roots-for-sa|♯2464((source link) docs: document writable_roots…]] · Safety and Privacy
- [[Changes/Codex CLI/2025-08-20-2474-https-github-com-openai-codex-pull-2474-add-a-slash-command-to-control-perm|♯2474((source link) Add a slash command to control…]] · Developer Workflow
- [[Changes/Codex CLI/2025-08-20-4-model-support-changes-in-rust-v0-23-0|4 Model Support changes in rust-v0.23.0]] · Model Support
- [[Changes/Codex CLI/2025-08-20-2-mobile-and-desktop-changes-in-rust-v0-23-0|2 Mobile and Desktop changes in rust-v0.23.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-08-20-2-interface-experience-changes-in-rust-v0-23-0|2 Interface Experience changes in rust-v0.23.0]] · Interface Experience
- [[Changes/Codex CLI/2025-08-20-2352-https-github-com-openai-codex-pull-2352-tui-skip-identical-consecutive-entr|♯2352((source link) tui: skip identical consecutive…]] · Projects and Workspaces
- [[Changes/Codex CLI/2025-08-20-2-context-window-changes-in-rust-v0-23-0|2 Context Window changes in rust-v0.23.0]] · Context Window
- [[Changes/Codex CLI/2025-08-20-5-apps-and-integrations-changes-in-rust-v0-23-0|5 Apps and Integrations changes in rust-v0.23.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-08-20-33-other-changes-in-rust-v0-23-0|33 other changes in rust-v0.23.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2025-08-18 · Gemini CLI · [[Changes/Gemini CLI/2025-08-18-feat-oauth-make-oauth-client-a-singleton-to-survive-cache-failures-by-mboshernit|feat(oauth): Make oauth client a singleton to survive cache failures]]
- Later: 2025-08-26 · Codex CLI · [[Changes/Codex CLI/2025-08-26-2528-fix-login-for-internal-employees|♯2528 Fix login for internal employees]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-08-20-8360b0&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-08-20-9-account-and-access-changes-in-rust-v0-23-0.md%0ACard%20ID%3A%20codex-cli-2025-08-20-8360b0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.23.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->