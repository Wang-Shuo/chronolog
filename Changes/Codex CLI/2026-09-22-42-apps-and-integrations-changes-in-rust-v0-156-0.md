---
card_id: codex-cli-2026-09-22-3a6770
date: '2026-09-22'
description: 'Codex CLI · 2026-09-22 · Apps and Integrations: 42 changes in 0.156.0
  — Explore account usage, token totals, and plugin and skill activity through the
  `/usage`…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2839
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f7f76558f6c2098e32db640ceaacdb561d0d22a62542c5e9273a281638e1c37a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-22-3a6770
  comparison: ''
  date: '2026-09-22'
  description: 'Codex CLI — 0.156.0: 42 Apps and Integrations changes'
  evidence:
  - quote: 'Explore account usage, token totals, and plugin and skill activity through
      the `/usage` analytics dashboard. (#45764, #45769)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44655 Honor thread-level plugin exclusions across runtime capabilities
      @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44826 Expose advertised MCP server capabilities in status responses @gpeal'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44832 Add trusted enterprise MCP auth configuration @nicksteele-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44905 Expose disabled plugin settings in the app-server API @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44938 Add connector auth failure detection without an install URL @priyanshusingh-de'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44948 Add context snapshots for async questions and plugin refresh @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45248 Use captured step settings for request metadata and tool hooks
      @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45409 Add session and originating window IDs to MCP request metadata
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45428 Avoid cloning MCP server status snapshot data @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45439 Share tool output schemas and defer MCP envelope construction @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45440 Share Apps tool catalogs without retaining unused snapshots @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45445 Attribute command and plugin analytics to the invoking model @jwang-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45459 Resolve enterprise-managed MCP registrations in the catalog @nicksteele-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45509 Share MCP tool specs until search results are selected @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45515 Filter plugin-install test analytics by event type @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45554 Use shared Bazel cache preparation in SDK CI @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45649 Add elicitation classification support to app and MCP analytics
      @priyanshusingh-de'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45716 Classify MCP auth and approval outcomes in analytics @priyanshusingh-de'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45755 Honor canonical plugin disables for shared connectors @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45796 Preserve `ImageUserInput` in the Python SDK @kchainani-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45805 Preserve MCP App UI metadata in tool-call events and history @victor-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45806 Restrict plugin install requests to the root thread @rennie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46019 Allow hosted Apps MCP contributions to override the protocol mode
      @teddywyly-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46029 Allow browser app cleanup hooks on interrupt @syuan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46033 Preserve orchestrator skill caches across MCP runtime updates @hlevy-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46042 Add read-only policy support to MCP tool requests @rennie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46066 Keep MCP user interaction on the root thread @rennie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46309 Preserve plugin caches across display metadata refreshes @vkg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46323 Record active plugin inventory in turn analytics @marksteinbrick-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46335 Keep MCP policy evaluation consistent with turn environments @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46493 Allow `/review` during MCP startup @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46528 Bind executor plugin measurements to the trusted plugin version
      @papayo-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46539 Add a command-start callback for tool lifecycle extensions @papayo-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46542 Add authenticated remote plugin measurement references @papayo-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46544 Expose declared onboarding skills in plugin details @victor-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46558 Add shared plugin catalog discovery APIs @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46564 Rename plugin MCP and app extension APIs @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46567 Separate plugin catalog listing from package resolution @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46572 Add turn-start cloud plugin discovery to the MCP extension @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46877 Allow subagents to request MCP elicitation input @rennie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46989 Expand agent message board tool integration coverage @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 42-apps-and-integrations-changes-in-rust-v0-156-0
  source_release: codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4
  source_type: github_releases
  theme: apps-integrations
  title: 42 Apps and Integrations changes in rust-v0.156.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-09-21-8-apps-and-integrations-changes-in-v1-0-87|8
  Apps and Integrations changes in v1.0.87]]'
- '[[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps
  and Integrations changes in v0.11.4]]'
- '[[Changes/Claude Code/2026-09-22-8-apps-and-integrations-changes-in-v2-1-280|8
  Apps and Integrations changes in v2.1.280]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4]]'
source_type: github_releases
theme: apps-integrations
title: 42 Apps and Integrations changes in rust-v0.156.0
type: change
---

<!-- chronolog:begin region="header" -->
# 42 Apps and Integrations changes in rust-v0.156.0

**Codex CLI** · 2026-09-22 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.156.0) · from [[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Explore account usage, token totals, and plugin and skill activity through the `/usage` analytics dashboard. (#45764, #45769)

> #44655 Honor thread-level plugin exclusions across runtime capabilities @mzeng-openai

> #44826 Expose advertised MCP server capabilities in status responses @gpeal

> #44832 Add trusted enterprise MCP auth configuration @nicksteele-oai

> #44905 Expose disabled plugin settings in the app-server API @mzeng-openai

> #44938 Add connector auth failure detection without an install URL @priyanshusingh-de

> #44948 Add context snapshots for async questions and plugin refresh @pakrym-oai

> #45248 Use captured step settings for request metadata and tool hooks @abhinav-oai

> #45409 Add session and originating window IDs to MCP request metadata @jif-oai

> #45428 Avoid cloning MCP server status snapshot data @charliemarsh-oai

> #45439 Share tool output schemas and defer MCP envelope construction @charliemarsh-oai

> #45440 Share Apps tool catalogs without retaining unused snapshots @charliemarsh-oai

> #45445 Attribute command and plugin analytics to the invoking model @jwang-openai

> #45459 Resolve enterprise-managed MCP registrations in the catalog @nicksteele-oai

> #45509 Share MCP tool specs until search results are selected @owenlin0

> #45515 Filter plugin-install test analytics by event type @zm-oai

> #45554 Use shared Bazel cache preparation in SDK CI @charliemarsh-oai

> #45649 Add elicitation classification support to app and MCP analytics @priyanshusingh-de

> #45716 Classify MCP auth and approval outcomes in analytics @priyanshusingh-de

> #45755 Honor canonical plugin disables for shared connectors @mzeng-openai

> #45796 Preserve `ImageUserInput` in the Python SDK @kchainani-oai

> #45805 Preserve MCP App UI metadata in tool-call events and history @victor-openai

> #45806 Restrict plugin install requests to the root thread @rennie-openai

> #46019 Allow hosted Apps MCP contributions to override the protocol mode @teddywyly-oai

> #46029 Allow browser app cleanup hooks on interrupt @syuan-oai

> #46033 Preserve orchestrator skill caches across MCP runtime updates @hlevy-openai

> #46042 Add read-only policy support to MCP tool requests @rennie-openai

> #46066 Keep MCP user interaction on the root thread @rennie-openai

> #46309 Preserve plugin caches across display metadata refreshes @vkg-oai

> #46323 Record active plugin inventory in turn analytics @marksteinbrick-oai

> #46335 Keep MCP policy evaluation consistent with turn environments @sayan-oai

> #46493 Allow `/review` during MCP startup @etraut-openai

> #46528 Bind executor plugin measurements to the trusted plugin version @papayo-oai

> #46539 Add a command-start callback for tool lifecycle extensions @papayo-oai

> #46542 Add authenticated remote plugin measurement references @papayo-oai

> #46544 Expose declared onboarding skills in plugin details @victor-openai

> #46558 Add shared plugin catalog discovery APIs @TAFOYA-OAI

> #46564 Rename plugin MCP and app extension APIs @TAFOYA-OAI

> #46567 Separate plugin catalog listing from package resolution @TAFOYA-OAI

> #46572 Add turn-start cloud plugin discovery to the MCP extension @TAFOYA-OAI

> #46877 Allow subagents to request MCP elicitation input @rennie-openai

> #46989 Expand agent message board tool integration coverage @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.156.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-22-13-account-and-access-changes-in-rust-v0-156-0|13 Account and Access changes in rust-v0.156.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-22-32-interface-experience-changes-in-rust-v0-156-0|32 Interface Experience changes in rust-v0.156.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-22-2-search-and-browsing-changes-in-rust-v0-156-0|2 Search and Browsing changes in rust-v0.156.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-09-22-46027-document-and-test-wildcards-in-network-proxy-domain-patterns-viyatb-oai|♯46027 Document and test ? wildcards in network proxy domain patterns @viyatb-oai]] · Files and Data
- [[Changes/Codex CLI/2026-09-22-45544-discourage-logging-full-image-generation-results-gan-tu|♯45544 Discourage logging full image generation results @Gan-Tu]] · Image Generation
- [[Changes/Codex CLI/2026-09-22-17-context-window-changes-in-rust-v0-156-0|17 Context Window changes in rust-v0.156.0]] · Context Window
- [[Changes/Codex CLI/2026-09-22-45849-preserve-the-app-server-shutdown-signal-future-across-loop-iterations-jger|♯45849 Preserve the app-server shutdown signal future across loop iterations @jgershen-oai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-09-22-11-mobile-and-desktop-changes-in-rust-v0-156-0|11 Mobile and Desktop changes in rust-v0.156.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-22-34-agent-mode-changes-in-rust-v0-156-0|34 Agent Mode changes in rust-v0.156.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-22-46040-default-tui-animations-off-when-a-screen-reader-is-detected-etraut-openai|♯46040 Default TUI animations off when a screen reader is detected @etraut-openai]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-09-22-9-collaboration-changes-in-rust-v0-156-0|9 Collaboration changes in rust-v0.156.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-22-6-memory-and-personalization-changes-in-rust-v0-156-0|6 Memory and Personalization changes in rust-v0.156.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-22-6-editor-experience-changes-in-rust-v0-156-0|6 Editor Experience changes in rust-v0.156.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-22-17-voice-and-audio-changes-in-rust-v0-156-0|17 Voice and Audio changes in rust-v0.156.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-22-25-model-support-changes-in-rust-v0-156-0|25 Model Support changes in rust-v0.156.0]] · Model Support
- [[Changes/Codex CLI/2026-09-22-50-safety-and-privacy-changes-in-rust-v0-156-0|50 Safety and Privacy changes in rust-v0.156.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-22-45960-tag-memory-usage-telemetry-with-the-memory-version-jif-oai|♯45960 Tag memory usage telemetry with the memory version @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-22-22-developer-workflow-changes-in-rust-v0-156-0|22 Developer Workflow changes in rust-v0.156.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-22-248-other-changes-in-rust-v0-156-0|248 other changes in rust-v0.156.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-8-apps-and-integrations-changes-in-v2-1-280|8 Apps and Integrations changes in v2.1.280]]
- Later: 2026-09-22 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-22-6-apps-and-integrations-changes-in-v1-0-88|6 Apps and Integrations changes in v1.0.88]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-22-3a6770&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-22-42-apps-and-integrations-changes-in-rust-v0-156-0.md%0ACard%20ID%3A%20codex-cli-2026-09-22-3a6770%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.156.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->