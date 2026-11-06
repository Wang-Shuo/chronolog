---
card_id: codex-cli-2026-06-09-ff8908
date: '2026-06-09'
description: 'Codex CLI · 2026-06-09 · Other changes: 24 changes in 0.139.0 — `codex
  resume --last "..."` and `codex fork --last "..."` now treat the trailing argument
  as…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 967ccb808cc241ea2fd35e1f7dc18c6179f2a59d311c7d130b71cb880acf3140
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-09-ff8908
  comparison: ''
  date: '2026-06-09'
  description: 'Codex CLI — 0.139.0: 24 other changes'
  evidence:
  - quote: '`codex resume --last "..."` and `codex fork --last "..."` now treat the
      trailing argument as the initial prompt instead of misreading it as a session
      ID. (#26818)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: Bare URLs with `~` in the path are now linkified end to end in the TUI
      instead of being truncated before the tilde. (#27088)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: Thread resets such as `/new`, `/clear`, and `/fork` no longer drop cloud-managed
      requirements or feature flags during TUI config reloads. (#25177)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: The embedded V8 toolchain was updated to `rusty_v8` 149.2.0. (#26464)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26464 build(v8): update rusty_v8 to 149.2.0 @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26895 ci: use bazel environment for BuildBuddy secret @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26818 fix(tui): accept prompts with resume and fork @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#24820 deps: update starlark to 0.14.2 @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26974 Ignore proc-macro-error2 advisory @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26969 feat: count V2 concurrency by active execution @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26997 Avoid reopening v2 descendants on resume @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26202 [codex] Restore release symbol artifacts with line tables @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26852 fix(app-server): avoid blocking connection cleanup @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26923 Add HTTP window ID to Responses client metadata @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#27024 ci: template custom runner names by repo @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#27038 [codex] Clarify PR babysitter state mutations @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26687 Pair thread environment settings @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#27060 [codex-analytics] stop sending codex error subreason @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#24118 feat: support oneOf and allOf in tool input schemas @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26091 [codex] Add OTEL counter descriptions @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#26840 Add typed file URIs @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#27088 fix(tui): linkify complete bare URLs with tildes @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#27092 Add extra config to StoredThread, leave empty for now @kumquatexpress'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  - quote: '#25177 Preserve cloud requirements across TUI thread resets @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.139.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 24-other-changes-in-rust-v0-139-0
  source_release: codex-cli-2026-06-09-rust-v0-139-0-github-336847772-eda0ee6f
  source_type: github_releases
  theme: uncategorized
  title: 24 other changes in rust-v0.139.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-09-rust-v0-139-0-github-336847772-eda0ee6f|codex-cli-2026-06-09-rust-v0-139-0-github-336847772-eda0ee6f]]'
source_type: github_releases
theme: uncategorized
title: 24 other changes in rust-v0.139.0
type: change
---

<!-- chronolog:begin region="header" -->
# 24 other changes in rust-v0.139.0

**Codex CLI** · 2026-06-09 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.139.0) · from [[Releases/Codex CLI/codex-cli-2026-06-09-rust-v0-139-0-github-336847772-eda0ee6f|0.139.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `codex resume --last "..."` and `codex fork --last "..."` now treat the trailing argument as the initial prompt instead of misreading it as a session ID. (#26818)

> Bare URLs with `~` in the path are now linkified end to end in the TUI instead of being truncated before the tilde. (#27088)

> Thread resets such as `/new`, `/clear`, and `/fork` no longer drop cloud-managed requirements or feature flags during TUI config reloads. (#25177)

> The embedded V8 toolchain was updated to `rusty_v8` 149.2.0. (#26464)

> #26464 build(v8): update rusty_v8 to 149.2.0 @cconger

> #26895 ci: use bazel environment for BuildBuddy secret @bolinfest

> #26818 fix(tui): accept prompts with resume and fork @fcoury-oai

> #24820 deps: update starlark to 0.14.2 @bolinfest

> #26974 Ignore proc-macro-error2 advisory @jif-oai

> #26969 feat: count V2 concurrency by active execution @jif-oai

> #26997 Avoid reopening v2 descendants on resume @jif-oai

> #26202 [codex] Restore release symbol artifacts with line tables @nornagon-openai

> #26852 fix(app-server): avoid blocking connection cleanup @apanasenko-oai

> #26923 Add HTTP window ID to Responses client metadata @ningyi-oai

> #27024 ci: template custom runner names by repo @bolinfest

> #27038 [codex] Clarify PR babysitter state mutations @anp-oai

> #26687 Pair thread environment settings @pakrym-oai

> #27060 [codex-analytics] stop sending codex error subreason @rhan-oai

> #24118 feat: support oneOf and allOf in tool input schemas @celia-oai

> #26091 [codex] Add OTEL counter descriptions @richardopenai

> #26840 Add typed file URIs @anp-oai

> #27088 fix(tui): linkify complete bare URLs with tildes @fcoury-oai

> #27092 Add extra config to StoredThread, leave empty for now @kumquatexpress

> #25177 Preserve cloud requirements across TUI thread resets @canvrno-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.139.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-09-3-context-window-changes-in-rust-v0-139-0|3 Context Window changes in rust-v0.139.0]] · Context Window
- [[Changes/Codex CLI/2026-06-09-3-search-and-browsing-changes-in-rust-v0-139-0|3 Search and Browsing changes in rust-v0.139.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-09-plugin-marketplace-automation-is-more-informative-and-responsive-codex-plugin-ma|Plugin marketplace automation is more informative and responsive]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-06-09-26637-codex-speed-up-external-agent-session-imports-stefanstokic-oai|♯26637 codex Speed up external agent session imports @stefanstokic-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-06-09-8-apps-and-integrations-changes-in-rust-v0-139-0|8 Apps and Integrations changes in rust-v0.139.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-09-26821-codex-exclude-external-tool-output-from-memories-rka-oai|♯26821 codex Exclude external tool output from memories @rka-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-06-09-5-agent-mode-changes-in-rust-v0-139-0|5 Agent Mode changes in rust-v0.139.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-09-release-builds-once-again-publish-separate-symbol-archives-with-line-tables-impr|Release builds once again publish separate symbol archives with line tables…]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-09-4-editor-experience-changes-in-rust-v0-139-0|4 Editor Experience changes in rust-v0.139.0]] · Editor Experience
- [[Changes/Codex CLI/2026-06-09-5-safety-and-privacy-changes-in-rust-v0-139-0|5 Safety and Privacy changes in rust-v0.139.0]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-09-ff8908&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-09-24-other-changes-in-rust-v0-139-0.md%0ACard%20ID%3A%20codex-cli-2026-06-09-ff8908%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.139.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->