---
card_id: codex-cli-2026-07-08-5119e0
date: '2026-07-08'
description: 'Codex CLI · 2026-07-08 · Apps and Integrations: 66 changes in 0.143.0
  — Added `codex remote-control pair` for generating manual pairing codes from a running…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2763
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 06fdd6602aa0329acdfeb5fbcbbdc56da2311a9ab1db9b2df8e061bda411c33f
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-08-5119e0
  comparison: ''
  date: '2026-07-08'
  description: 'Codex CLI — 0.143.0: 66 Apps and Integrations changes'
  evidence:
  - quote: Added `codex remote-control pair` for generating manual pairing codes from
      a running daemon. (#29913)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: 'Improved recovery when exec servers are temporarily offline and prevented
      remote-control token refresh retry storms. (#30098, #30201)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: 'Documented UUID7 thread and turn IDs, plus recommended remote-executor
      integration-test workflows. (#27714, #29790)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29485 [codex] fetch featured IDs for remote plugins @ericning-o'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29488 [plugins] Add dark-mode logo metadata @drewschuster-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29486 [codex] Use tool search for MCP tools by default @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#26704 TUI Plugin Sharing 4 - cover remote plugin catalog flows @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29493 mcp: accept foreign absolute cwd for remote stdio @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29518 Remove redundant Codex Apps manager flag @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29528 Centralize Codex Apps client handling @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29575 Remove redundant Codex Apps cache guard @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29583 Group Codex Apps client setup @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29615 Fix Codex Apps auth elicitation hang @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29608 Shut down superseded MCP managers on refresh @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29495 Separate local and remote plugin analytics IDs @jameswt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29696 [codex] Fix stale approval policy in MCP test @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29704 [codex] Fix stale approval policy in MCP test @kumquatexpress'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#28976 Add MCP tool call error metrics @stevenlee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29620 Decouple plugin manifest path resolution @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#28918 Make selected plugin roots URI-native @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#28630 [codex] trace MCP startup latency @rphilizaire-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29690 [plugins] Add marketplace source requirements @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29765 [codex] Ignore local curated plugins when remote catalog is active
      @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29753 [plugins] Enforce marketplace source admission requirements @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29723 connectors: own app metadata types @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29788 test: run app-server integration tests under Wine @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29789 test: use automatic environments in app-server integration tests
      @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29790 docs: document remote executor integration testing @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29628 Keep executor plugin MCP paths URI-native @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29831 Cache plugin namespace during executor skill discovery @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29889 [apps] Thread structured icon assets through app list @drewschuster-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29724 mcp: keep elicitation requests below app wire types @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29684 [plugins] Track plugin install requests by ID @adaley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29893 [codex] dedupe remote control account header @shuo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29851 Add a connector declaration snapshot @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29852 Read connector declarations from executor plugins @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29785 Isolate curated plugin sync Git environment @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29913 feat(remote-control): add daemon pairing command @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#26705 TUI Plugin Sharing 5 - polish remote plugin catalog rows @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29733 Allow ChatGPT-hosted MCP servers to use session auth @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29956 [codex] Populate remote plugin local versions @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29969 Report MCP error codes with server attribution @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#28522 Support HTTP MCP servers from selected executor plugins @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#28529 Support OAuth for HTTP MCP servers from selected executor plugins
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29648 [codex] Add managed MCP server matchers @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30100 Let extensions contribute World State sections @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29877 [codex] Surface MCP reauthentication-required startup failures
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30110 [codex] add code-mode host failure supervision hooks @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30101 Pin MCP runtimes to model steps @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30093 Project selected plugin runtime by environment availability @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30127 Keep MCP elicitation routable across runtime refreshes @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29934 Expose MCP app identity in app context @martinauyeung-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29920 Retry failed Codex Apps MCP startup @kbazzi'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29516 Persist Cloudflare affinity cookies for MCP HTTP @stevenlee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30148 Reuse MCP runtimes when selected availability changes nothing @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30229 Relax hooks.json top-level metadata validation @charlesgong-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29375 [codex] Support npm marketplace plugin sources @charlesgong-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30201 fix(remote-control): avoid server token refresh retry storms @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29691 [plugins] Enforce marketplace source policy at runtime @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30297 [codex] Enable remote plugins by default @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30981 [codex] expose remote plugin versions @ericning-o'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30223 Make plugin guidance react to environment readiness @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31189 Fix cancelled review leaving MCP startup busy @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#30226 Make Apps guidance react to MCP availability @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#31293 [codex] app-server: expose plugin install policy source @ericning-o'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  - quote: '#29992 app-server: cover selected environments in integration tests @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.143.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 66-apps-and-integrations-changes-in-rust-v0-143-0
  source_release: codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c
  source_type: github_releases
  theme: apps-integrations
  title: 66 Apps and Integrations changes in rust-v0.143.0
  type: change
related_changes:
- '[[Changes/OpenHands/2026-07-07-2-apps-and-integrations-changes-in-1-9-1|2 Apps
  and Integrations changes in 1.9.1]]'
- '[[Changes/v0/2026-07-07-3-apps-and-integrations-changes-in-grouped-tool-approvals-richer-mcp|3
  Apps and Integrations changes in Grouped tool approvals, richer MCP…]]'
- '[[Changes/Claude Code/2026-07-08-reserved-the-claude-browser-mcp-server-name-alongside-claude-preview-ahead-of-th|Reserved
  the "Claude Browser" MCP server name (alongside "Claude Preview") ahead…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c|codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c]]'
source_type: github_releases
theme: apps-integrations
title: 66 Apps and Integrations changes in rust-v0.143.0
type: change
---

<!-- chronolog:begin region="header" -->
# 66 Apps and Integrations changes in rust-v0.143.0

**Codex CLI** · 2026-07-08 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.143.0) · from [[Releases/Codex CLI/codex-cli-2026-07-08-rust-v0-143-0-github-350650561-9eba805c|0.143.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `codex remote-control pair` for generating manual pairing codes from a running daemon. (#29913)

> Improved recovery when exec servers are temporarily offline and prevented remote-control token refresh retry storms. (#30098, #30201)

> Documented UUID7 thread and turn IDs, plus recommended remote-executor integration-test workflows. (#27714, #29790)

> #29485 [codex] fetch featured IDs for remote plugins @ericning-o

> #29488 [plugins] Add dark-mode logo metadata @drewschuster-openai

> #29486 [codex] Use tool search for MCP tools by default @sayan-oai

> #26704 TUI Plugin Sharing 4 - cover remote plugin catalog flows @canvrno-oai

> #29493 mcp: accept foreign absolute cwd for remote stdio @anp-oai

> #29518 Remove redundant Codex Apps manager flag @aibrahim-oai

> #29528 Centralize Codex Apps client handling @aibrahim-oai

> #29575 Remove redundant Codex Apps cache guard @aibrahim-oai

> #29583 Group Codex Apps client setup @aibrahim-oai

> #29615 Fix Codex Apps auth elicitation hang @jif-oai

> #29608 Shut down superseded MCP managers on refresh @jif-oai

> #29495 Separate local and remote plugin analytics IDs @jameswt-oai

> #29696 [codex] Fix stale approval policy in MCP test @sayan-oai

> #29704 [codex] Fix stale approval policy in MCP test @kumquatexpress

> #28976 Add MCP tool call error metrics @stevenlee-oai

> #29620 Decouple plugin manifest path resolution @jif-oai

> #28918 Make selected plugin roots URI-native @jif-oai

> #28630 [codex] trace MCP startup latency @rphilizaire-openai

> #29690 [plugins] Add marketplace source requirements @xl-openai

> #29765 [codex] Ignore local curated plugins when remote catalog is active @xl-openai

> #29753 [plugins] Enforce marketplace source admission requirements @xl-openai

> #29723 connectors: own app metadata types @anp-oai

> #29788 test: run app-server integration tests under Wine @anp-oai

> #29789 test: use automatic environments in app-server integration tests @anp-oai

> #29790 docs: document remote executor integration testing @anp-oai

> #29628 Keep executor plugin MCP paths URI-native @jif-oai

> #29831 Cache plugin namespace during executor skill discovery @jif-oai

> #29889 [apps] Thread structured icon assets through app list @drewschuster-openai

> #29724 mcp: keep elicitation requests below app wire types @anp-oai

> #29684 [plugins] Track plugin install requests by ID @adaley-openai

> #29893 [codex] dedupe remote control account header @shuo-openai

> #29851 Add a connector declaration snapshot @jif-oai

> #29852 Read connector declarations from executor plugins @jif-oai

> #29785 Isolate curated plugin sync Git environment @etraut-openai

> #29913 feat(remote-control): add daemon pairing command @apanasenko-oai

> #26705 TUI Plugin Sharing 5 - polish remote plugin catalog rows @canvrno-oai

> #29733 Allow ChatGPT-hosted MCP servers to use session auth @aibrahim-oai

> #29956 [codex] Populate remote plugin local versions @abhinav-oai

> #29969 Report MCP error codes with server attribution @aibrahim-oai

> #28522 Support HTTP MCP servers from selected executor plugins @jif-oai

> #28529 Support OAuth for HTTP MCP servers from selected executor plugins @jif-oai

> #29648 [codex] Add managed MCP server matchers @felixxia-oai

> #30100 Let extensions contribute World State sections @jif-oai

> #29877 [codex] Surface MCP reauthentication-required startup failures @felixxia-oai

> #30110 [codex] add code-mode host failure supervision hooks @cconger

> #30101 Pin MCP runtimes to model steps @jif-oai

> #30093 Project selected plugin runtime by environment availability @jif-oai

> #30127 Keep MCP elicitation routable across runtime refreshes @jif-oai

> #29934 Expose MCP app identity in app context @martinauyeung-oai

> #29920 Retry failed Codex Apps MCP startup @kbazzi

> #29516 Persist Cloudflare affinity cookies for MCP HTTP @stevenlee-oai

> #30148 Reuse MCP runtimes when selected availability changes nothing @jif-oai

> #30229 Relax hooks.json top-level metadata validation @charlesgong-openai

> #29375 [codex] Support npm marketplace plugin sources @charlesgong-openai

> #30201 fix(remote-control): avoid server token refresh retry storms @apanasenko-oai

> #29691 [plugins] Enforce marketplace source policy at runtime @xl-openai

> #30297 [codex] Enable remote plugins by default @xl-openai

> #30981 [codex] expose remote plugin versions @ericning-o

> #30223 Make plugin guidance react to environment readiness @sayan-oai

> #31189 Fix cancelled review leaving MCP startup busy @charliemarsh-oai

> #30226 Make Apps guidance react to MCP availability @sayan-oai

> #31293 [codex] app-server: expose plugin install policy source @ericning-o

> #29992 app-server: cover selected environments in integration tests @anp-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.143.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-08-5-collaboration-changes-in-rust-v0-143-0|5 Collaboration changes in rust-v0.143.0]] · Collaboration
- [[Changes/Codex CLI/2026-07-08-5-account-and-access-changes-in-rust-v0-143-0|5 Account and Access changes in rust-v0.143.0]] · Account and Access
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
- [[Changes/Codex CLI/2026-07-08-145-other-changes-in-rust-v0-143-0|145 other changes in rust-v0.143.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-07-08 · Claude Code · [[Changes/Claude Code/2026-07-08-reserved-the-claude-browser-mcp-server-name-alongside-claude-preview-ahead-of-th|Reserved the "Claude Browser" MCP server name (alongside "Claude Preview") ahead…]]
- Later: 2026-07-08 · Devin · [[Changes/Devin/2026-07-08-mobbin-mcp-server|Mobbin MCP Server]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-08-5119e0&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-08-66-apps-and-integrations-changes-in-rust-v0-143-0.md%0ACard%20ID%3A%20codex-cli-2026-07-08-5119e0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.143.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->