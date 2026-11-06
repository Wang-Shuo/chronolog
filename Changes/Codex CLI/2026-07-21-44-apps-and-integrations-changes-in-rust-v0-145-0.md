---
card_id: codex-cli-2026-07-21-e8c4a9
date: '2026-07-21'
description: 'Codex CLI · 2026-07-21 · Apps and Integrations: 44 changes in 0.145.0
  — Expanded `/import` to migrate Cursor and Claude Code settings, MCP servers, plugins…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1216
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cd892272ee45b74bbc65375c7547a4a688376572f5a3ebf8c1a9bd91f5bc89d9
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-21-e8c4a9
  comparison: ''
  date: '2026-07-21'
  description: 'Codex CLI — 0.145.0: 44 Apps and Integrations changes'
  evidence:
  - quote: 'Expanded `/import` to migrate Cursor and Claude Code settings, MCP servers,
      plugins, sessions, commands, and project-scoped memories. (#31672, #33411, #33426,
      #33444)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: 'Reduced startup and large-context overhead with concurrent skill/plugin
      discovery and more efficient remote compaction. (#31566, #33369, #33423, #34431)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31790 Reduce MCP tool-list trace volume @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31803 fix(mcp): default Apps product SKU to codex @alecbarber-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31745 code-mode: retain shared MCP types for deferred tools @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31672 Import enabled plugins from known marketplaces @charlesgong-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31481 fix: forward originator to Codex Apps MCP @raquel-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31686 [codex-apps] Filter optional file fields by tool schema @tsarlandie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31805 Bound remote MCP stdio lines @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32272 Expose scheduled tasks in plugin details @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32301 Trust hooks from materialized workspace plugins @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32698 Extract connector runtime snapshot management @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32781 Apply MCP startup timeouts during client creation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32867 Include connector IDs in MCP tool call analytics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32891 Attach connector caches to diagnostic uploads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32894 Serialize plugin install requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32949 Tighten recommended plugin install suggestions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33113 Allow injecting the Codex Apps tools cache @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33149 Build MCP tool runtimes before router planning @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33180 Serialize concurrent MCP stdin writes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33182 Preserve plugin install failure subtypes during imports @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33184 Reuse MCP tool catalogs across sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33213 Prepare Python SDK 0.144.4 stable release @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33223 Instrument environment and plugin resolution paths @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33297 Allow MCP servers to opt out of tool catalog caching @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33308 Expand MCP tool catalog cache regression coverage @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33411 Migrate plugin commands into skills on install @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33414 Expose connector candidates from imported sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33421 Fetch workspace connectors concurrently @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33423 Load executor plugin declarations concurrently @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33424 Attribute OpenAI docs MCP requests to Codex @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33427 Propagate deferred environment capability roots to MCP @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33467 Remove template IDs from MCP tool call metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33509 Preserve encrypted content in MCP tool outputs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33677 Forward thread originators from standalone extensions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33889 Centralize thread MCP connections in `McpRuntime` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33895 Add SessionEnd hooks for thread teardown @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33896 Expose plugin installation interstitial requirements @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33908 Allow publishing plugins through share updates @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34206 Avoid retaining decoded MCP images in history cells @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34389 Route Codex Apps MCP through plugin service @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34396 Run compact session-start hooks before turn continuation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34408 Support threadless MCP connections without event channels @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34417 Enrich app/read connector metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 44-apps-and-integrations-changes-in-rust-v0-145-0
  source_release: codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f
  source_type: github_releases
  theme: apps-integrations
  title: 44 Apps and Integrations changes in rust-v0.145.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-20-background-sessions-mcp-and-install-github-app-now-park-a-needs-input-request-in|Background
  sessions: /mcp and /install-github-app now park…]]'
- '[[Changes/GitHub Copilot CLI/2026-07-20-10-apps-and-integrations-changes-in-v1-0-72|10
  Apps and Integrations changes in v1.0.72]]'
- '[[Changes/Claude Code/2026-07-21-capped-the-frontend-design-plugin-suggestion-tip-at-3-lifetime-impressions-inste|Capped
  the frontend-design plugin suggestion tip at 3 lifetime impressions instead…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f]]'
source_type: github_releases
theme: apps-integrations
title: 44 Apps and Integrations changes in rust-v0.145.0
type: change
---

<!-- chronolog:begin region="header" -->
# 44 Apps and Integrations changes in rust-v0.145.0

**Codex CLI** · 2026-07-21 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.145.0) · from [[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|0.145.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Expanded `/import` to migrate Cursor and Claude Code settings, MCP servers, plugins, sessions, commands, and project-scoped memories. (#31672, #33411, #33426, #33444)

> Reduced startup and large-context overhead with concurrent skill/plugin discovery and more efficient remote compaction. (#31566, #33369, #33423, #34431)

> #31790 Reduce MCP tool-list trace volume @jif-oai

> #31803 fix(mcp): default Apps product SKU to codex @alecbarber-oai

> #31745 code-mode: retain shared MCP types for deferred tools @sayan-oai

> #31672 Import enabled plugins from known marketplaces @charlesgong-openai

> #31481 fix: forward originator to Codex Apps MCP @raquel-openai

> #31686 [codex-apps] Filter optional file fields by tool schema @tsarlandie-oai

> #31805 Bound remote MCP stdio lines @jif-oai

> #32272 Expose scheduled tasks in plugin details @copyberry

> #32301 Trust hooks from materialized workspace plugins @copyberry

> #32698 Extract connector runtime snapshot management @copyberry

> #32781 Apply MCP startup timeouts during client creation @copyberry

> #32867 Include connector IDs in MCP tool call analytics @copyberry

> #32891 Attach connector caches to diagnostic uploads @copyberry

> #32894 Serialize plugin install requests @copyberry

> #32949 Tighten recommended plugin install suggestions @copyberry

> #33113 Allow injecting the Codex Apps tools cache @copyberry

> #33149 Build MCP tool runtimes before router planning @copyberry

> #33180 Serialize concurrent MCP stdin writes @copyberry

> #33182 Preserve plugin install failure subtypes during imports @copyberry

> #33184 Reuse MCP tool catalogs across sessions @copyberry

> #33213 Prepare Python SDK 0.144.4 stable release @copyberry

> #33223 Instrument environment and plugin resolution paths @copyberry

> #33297 Allow MCP servers to opt out of tool catalog caching @copyberry

> #33308 Expand MCP tool catalog cache regression coverage @copyberry

> #33411 Migrate plugin commands into skills on install @copyberry

> #33414 Expose connector candidates from imported sessions @copyberry

> #33421 Fetch workspace connectors concurrently @copyberry

> #33423 Load executor plugin declarations concurrently @copyberry

> #33424 Attribute OpenAI docs MCP requests to Codex @copyberry

> #33427 Propagate deferred environment capability roots to MCP @copyberry

> #33467 Remove template IDs from MCP tool call metadata @copyberry

> #33509 Preserve encrypted content in MCP tool outputs @copyberry

> #33677 Forward thread originators from standalone extensions @copyberry

> #33889 Centralize thread MCP connections in `McpRuntime` @copyberry

> #33895 Add SessionEnd hooks for thread teardown @copyberry

> #33896 Expose plugin installation interstitial requirements @copyberry

> #33908 Allow publishing plugins through share updates @copyberry

> #34206 Avoid retaining decoded MCP images in history cells @copyberry

> #34389 Route Codex Apps MCP through plugin service @copyberry

> #34396 Run compact session-start hooks before turn continuation @copyberry

> #34408 Support threadless MCP connections without event channels @copyberry

> #34417 Enrich app/read connector metadata @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.145.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-21-4-collaboration-changes-in-rust-v0-145-0|4 Collaboration changes in rust-v0.145.0]] · Collaboration
- [[Changes/Codex CLI/2026-07-21-20-agent-mode-changes-in-rust-v0-145-0|20 Agent Mode changes in rust-v0.145.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-21-12-developer-workflow-changes-in-rust-v0-145-0|12 Developer Workflow changes in rust-v0.145.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-21-7-voice-and-audio-changes-in-rust-v0-145-0|7 Voice and Audio changes in rust-v0.145.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-07-21-12-context-window-changes-in-rust-v0-145-0|12 Context Window changes in rust-v0.145.0]] · Context Window
- [[Changes/Codex CLI/2026-07-21-4-editor-experience-changes-in-rust-v0-145-0|4 Editor Experience changes in rust-v0.145.0]] · Editor Experience
- [[Changes/Codex CLI/2026-07-21-17-safety-and-privacy-changes-in-rust-v0-145-0|17 Safety and Privacy changes in rust-v0.145.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-21-3-mobile-and-desktop-changes-in-rust-v0-145-0|3 Mobile and Desktop changes in rust-v0.145.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-21-3-image-generation-changes-in-rust-v0-145-0|3 Image Generation changes in rust-v0.145.0]] · Image Generation
- [[Changes/Codex CLI/2026-07-21-22-model-support-changes-in-rust-v0-145-0|22 Model Support changes in rust-v0.145.0]] · Model Support
- [[Changes/Codex CLI/2026-07-21-33201-branch-conversations-when-editing-earlier-tui-prompts-copyberry|♯33201 Branch conversations when editing earlier TUI prompts @copyberry]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-07-21-3-reliability-and-performance-changes-in-rust-v0-145-0|3 Reliability and Performance changes in rust-v0.145.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-07-21-33167-document-the-windows-exec-yield-time-range-copyberry|♯33167 Document the Windows exec yield time range @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-07-21-11-memory-and-personalization-changes-in-rust-v0-145-0|11 Memory and Personalization changes in rust-v0.145.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-21-3-search-and-browsing-changes-in-rust-v0-145-0|3 Search and Browsing changes in rust-v0.145.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-21-9-account-and-access-changes-in-rust-v0-145-0|9 Account and Access changes in rust-v0.145.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-21-18-interface-experience-changes-in-rust-v0-145-0|18 Interface Experience changes in rust-v0.145.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-21-161-other-changes-in-rust-v0-145-0|161 other changes in rust-v0.145.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-07-21 · Claude Code · [[Changes/Claude Code/2026-07-21-capped-the-frontend-design-plugin-suggestion-tip-at-3-lifetime-impressions-inste|Capped the frontend-design plugin suggestion tip at 3 lifetime impressions instead…]]
- Later: 2026-07-22 · Claude Code · [[Changes/Claude Code/2026-07-22-3-apps-and-integrations-changes-in-v2-1-218|3 Apps and Integrations changes in v2.1.218]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-21-e8c4a9&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-21-44-apps-and-integrations-changes-in-rust-v0-145-0.md%0ACard%20ID%3A%20codex-cli-2026-07-21-e8c4a9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.145.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->