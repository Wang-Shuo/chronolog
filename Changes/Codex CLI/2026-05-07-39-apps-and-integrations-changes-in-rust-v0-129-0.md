---
card_id: codex-cli-2026-05-07-0fd8ed
date: '2026-05-07'
description: 'Codex CLI · 2026-05-07 · Apps and Integrations: 39 changes in 0.129.0
  — Plugin management now supports workspace sharing, share access controls, source…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2701
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1e889edbf1c70a571fcfb1110b098923f43cd833ee5fe580b6c769a94b6b6614
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-07-0fd8ed
  comparison: ''
  date: '2026-05-07'
  description: 'Codex CLI — 0.129.0: 39 Apps and Integrations changes'
  evidence:
  - quote: 'Plugin management now supports workspace sharing, share access controls,
      source filtering, local share path tracking, marketplace removal/upgrades, remote
      bundle sync, and admin-disabled status handling. (#20278, #21124, #21419, #20560,
      #19843, #20478, #20268, #20298)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: 'Hooks can be browsed and toggled from `/hooks`, can run before/after compaction,
      and can add `PreToolUse` context; Codex Apps auth and eligible MCP elicitations
      now surface through TUI/Guardian flows. (#19882, #19905, #20692, #19193, #19431)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: 'Windows Bazel CI now uses faster cross-compilation for tests, clippy,
      and release-build checks, and Bazel now runs sharded Rust integration tests.
      (#20585, #20701, #21057)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: 'Analytics and diagnostics coverage expanded for tool lifecycles, goals,
      plugin skills, thread sources, service tiers, and PR issue labeling. (#17089,
      #17090, #20799, #20923, #20949, #20969, #20893)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20278 feat: Add workspace plugin sharing APIs @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20260 fix(core): truncate large mcp tool outputs in rollouts @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#19843 /plugins: remove marketplace @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#19882 Add /hooks browser for lifecycle hooks @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20474 [plugin] Add Canva to suggesteable list. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20348 Move plugin out of core. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20268 Sync remote installed plugin bundles @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20069 Bypass review for always-allow MCP tools in auto-review @maja-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20267 Emit analytics for remote plugin installs @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20522 Alias codex_hooks feature as hooks @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20341 app-server: switch remote control to protocol v3 segmentation @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20298 Surface admin-disabled remote plugin status @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20265 Refresh remote plugin cache on auth changes @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20150 Add remote plugin skill read API @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20560 feat: Track local paths for shared plugins @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20478 /plugins: add marketplace upgrade flow @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20677 [codex] Emit MCP tool calls as turn items @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20853 [mcp-apps] Persist MCP Apps specific tool call end event. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21053 Use MCP server instructions in deferred namespace descriptions
      @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21057 bazel: run sharded rust integration tests @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20722 Remove remote plugin uninstall prefix gate @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20923 Add plugin ID to skill analytics @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21113 Auto-deny MCP elicitations for Xcode 26.4 clients @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21219 Add model and reasoning effort to MCP turn metadata @mchen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21271 Expose plugin manifest keywords in app server @alfozan'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21124 feat: Add plugin share access controls @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21055 Preserve session MCP config on refresh @aaronl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21277 [mcp] Return Accept early per feedback. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#19193 Support Codex Apps auth elicitations @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21329 feat: include thread ID in MCP turn metadata @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21350 [codex] fix builtin MCP Windows path test @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21281 Remove core MCP list tools op @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#19431 Route opted-in MCP elicitations through Guardian @cd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21419 feat: Add marketplace source filtering and plugin share context
      @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#19905 Add compact lifecycle hooks (started by vincentkoc - external contrib)
      @eternal-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 39-apps-and-integrations-changes-in-rust-v0-129-0
  source_release: codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e
  source_type: github_releases
  theme: apps-integrations
  title: 39 Apps and Integrations changes in rust-v0.129.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-06-mcp-server-child-processes-e-g-started-via-npx-or-uvx-are-now-fully-terminated-w|MCP
  server child processes (e.g. started via npx or uvx) are now fully terminated…]]'
- '[[Changes/GitHub Copilot CLI/2026-05-06-2-apps-and-integrations-changes-in-v1-0-42|2
  Apps and Integrations changes in v1.0.42]]'
- '[[Changes/Claude Code/2026-05-07-2-apps-and-integrations-changes-in-v2-1-133|2
  Apps and Integrations changes in v2.1.133]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e]]'
source_type: github_releases
theme: apps-integrations
title: 39 Apps and Integrations changes in rust-v0.129.0
type: change
---

<!-- chronolog:begin region="header" -->
# 39 Apps and Integrations changes in rust-v0.129.0

**Codex CLI** · 2026-05-07 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.129.0) · from [[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|0.129.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Plugin management now supports workspace sharing, share access controls, source filtering, local share path tracking, marketplace removal/upgrades, remote bundle sync, and admin-disabled status handling. (#20278, #21124, #21419, #20560, #19843, #20478, #20268, #20298)

> Hooks can be browsed and toggled from `/hooks`, can run before/after compaction, and can add `PreToolUse` context; Codex Apps auth and eligible MCP elicitations now surface through TUI/Guardian flows. (#19882, #19905, #20692, #19193, #19431)

> Windows Bazel CI now uses faster cross-compilation for tests, clippy, and release-build checks, and Bazel now runs sharded Rust integration tests. (#20585, #20701, #21057)

> Analytics and diagnostics coverage expanded for tool lifecycles, goals, plugin skills, thread sources, service tiers, and PR issue labeling. (#17089, #17090, #20799, #20923, #20949, #20969, #20893)

> #20278 feat: Add workspace plugin sharing APIs @xl-openai

> #20260 fix(core): truncate large mcp tool outputs in rollouts @owenlin0

> #19843 /plugins: remove marketplace @canvrno-oai

> #19882 Add /hooks browser for lifecycle hooks @abhinav-oai

> #20474 [plugin] Add Canva to suggesteable list. @mzeng-openai

> #20348 Move plugin out of core. @xl-openai

> #20268 Sync remote installed plugin bundles @xli-oai

> #20069 Bypass review for always-allow MCP tools in auto-review @maja-openai

> #20267 Emit analytics for remote plugin installs @xli-oai

> #20522 Alias codex_hooks feature as hooks @abhinav-oai

> #20341 app-server: switch remote control to protocol v3 segmentation @euroelessar

> #20298 Surface admin-disabled remote plugin status @xli-oai

> #20265 Refresh remote plugin cache on auth changes @xli-oai

> #20150 Add remote plugin skill read API @xli-oai

> #20560 feat: Track local paths for shared plugins @xl-openai

> #20478 /plugins: add marketplace upgrade flow @canvrno-oai

> #20677 [codex] Emit MCP tool calls as turn items @pakrym-oai

> #20853 [mcp-apps] Persist MCP Apps specific tool call end event. @mzeng-openai

> #21053 Use MCP server instructions in deferred namespace descriptions @sayan-oai

> #21057 bazel: run sharded rust integration tests @bolinfest

> #20722 Remove remote plugin uninstall prefix gate @xli-oai

> #20923 Add plugin ID to skill analytics @alexsong-oai

> #21113 Auto-deny MCP elicitations for Xcode 26.4 clients @etraut-openai

> #21219 Add model and reasoning effort to MCP turn metadata @mchen-oai

> #21271 Expose plugin manifest keywords in app server @alfozan

> #21124 feat: Add plugin share access controls @xl-openai

> #21055 Preserve session MCP config on refresh @aaronl-openai

> #21277 [mcp] Return Accept early per feedback. @mzeng-openai

> #19193 Support Codex Apps auth elicitations @mzeng-openai

> #21329 feat: include thread ID in MCP turn metadata @jif-oai

> #21350 [codex] fix builtin MCP Windows path test @jif-oai

> #21281 Remove core MCP list tools op @pakrym-oai

> #19431 Route opted-in MCP elicitations through Guardian @cd-oai

> #21419 feat: Add marketplace source filtering and plugin share context @xl-openai

> #19905 Add compact lifecycle hooks (started by vincentkoc - external contrib) @eternal-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.129.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-07-5-agent-mode-changes-in-rust-v0-129-0|5 Agent Mode changes in rust-v0.129.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-07-3-mobile-and-desktop-changes-in-rust-v0-129-0|3 Mobile and Desktop changes in rust-v0.129.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-07-3-collaboration-changes-in-rust-v0-129-0|3 Collaboration changes in rust-v0.129.0]] · Collaboration
- [[Changes/Codex CLI/2026-05-07-20065-feat-tui-redesign-session-picker-fcoury-oai|♯20065 feat(tui): redesign session picker @fcoury-oai]] · Interface Experience
- [[Changes/Codex CLI/2026-05-07-4-model-support-changes-in-rust-v0-129-0|4 Model Support changes in rust-v0.129.0]] · Model Support
- [[Changes/Codex CLI/2026-05-07-4-editor-experience-changes-in-rust-v0-129-0|4 Editor Experience changes in rust-v0.129.0]] · Editor Experience
- [[Changes/Codex CLI/2026-05-07-5-developer-workflow-changes-in-rust-v0-129-0|5 Developer Workflow changes in rust-v0.129.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-07-2-account-and-access-changes-in-rust-v0-129-0|2 Account and Access changes in rust-v0.129.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-07-7-context-window-changes-in-rust-v0-129-0|7 Context Window changes in rust-v0.129.0]] · Context Window
- [[Changes/Codex CLI/2026-05-07-tui-startup-and-accessibility-were-tightened-by-bounding-terminal-probes-clearin|TUI startup and accessibility were tightened by bounding terminal probes, clearing…]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-05-07-21379-document-codex-git-commit-attribution-config-henzelmann-oai|♯21379 Document Codex git commit attribution config @henzelmann-oai]] · Files and Data
- [[Changes/Codex CLI/2026-05-07-21054-rollout-store-web-search-and-mcp-tool-calls-owenlin0|♯21054 rollout: store web search and mcp tool calls @owenlin0]] · Search and Browsing
- [[Changes/Codex CLI/2026-05-07-16-memory-and-personalization-changes-in-rust-v0-129-0|16 Memory and Personalization changes in rust-v0.129.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-07-11-safety-and-privacy-changes-in-rust-v0-129-0|11 Safety and Privacy changes in rust-v0.129.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-07-2-reliability-and-performance-changes-in-rust-v0-129-0|2 Reliability and Performance changes in rust-v0.129.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-05-07-137-other-changes-in-rust-v0-129-0|137 other changes in rust-v0.129.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-07 · Claude Code · [[Changes/Claude Code/2026-05-07-2-apps-and-integrations-changes-in-v2-1-133|2 Apps and Integrations changes in v2.1.133]]
- Later: 2026-05-07 · Cursor · [[Changes/Cursor/2026-05-07-made-mcp-connection-behavior-more-predictable-and-added-explicit-stale-token-cle|Made MCP connection behavior more predictable, and added explicit stale token…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-07-0fd8ed&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-07-39-apps-and-integrations-changes-in-rust-v0-129-0.md%0ACard%20ID%3A%20codex-cli-2026-05-07-0fd8ed%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.129.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->