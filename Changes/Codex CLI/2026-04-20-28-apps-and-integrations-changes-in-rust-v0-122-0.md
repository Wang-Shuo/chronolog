---
card_id: codex-cli-2026-04-20-9d9efc
date: '2026-04-20'
description: 'Codex CLI · 2026-04-20 · Apps and Integrations: 28 changes in 0.122.0
  — App-server approvals, user-input prompts, and MCP elicitations now disappear from
  the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1124
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 81c194aa6a92f2a591324785fd63c16a58d59f75ebdc61dd5403cf22f9f3649b
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-20-9d9efc
  comparison: ''
  date: '2026-04-20'
  description: 'Codex CLI — 0.122.0: 28 Apps and Integrations changes'
  evidence:
  - quote: App-server approvals, user-input prompts, and MCP elicitations now disappear
      from the TUI when another client resolves them, instead of leaving stale prompts
      behind (#15134).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: 'Documented custom MCP server approval defaults and exec-server stdin behavior
      (#17843, #18086).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: 'Updated app-server docs for plugin API changes, marketplace removal, resume/fork
      token-usage replay, and warning notifications (#17277, #17751, #18023, #18298).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: 'Split plugin and marketplace code into `codex-core-plugins`, moved more
      connector code into `connectors`, and continued breaking up the large core session/turn
      modules (#18070, #18158, #18200, #18206, #18244, #18249).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17714 Support original-detail metadata on MCP image outputs @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17853 [mcp] Add dummy tools for previously called but currently missing
      tools. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17831 [codex][mcp] Add resource uri meta to tool call item. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18070 Extract plugin loading and marketplace logic into codex-core-plugins
      @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18078 Fix MCP startup cancellation through app server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18085 [1/8] Add MCP server environment config @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17287 [code mode] defer mcp tools from exec description @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18055 Improve external agent plugin migration for configured marketplaces
      @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18158 Move more connector logic into connectors crate @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17843 Add server-level approval defaults for custom MCP servers @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18196 Use in-process app-server for unknown-thread MCP read test @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18116 Move marketplace add under plugin command @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18182 feat: Handle alternate plugin manifest paths @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18246 Sync local plugin imports, async remote imports, refresh caches
      after… @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17563 Add PermissionRequest hooks support @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18087 [4/6] Abstract MCP stdio server launching @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18381 Remove the tier constraint from connectors directory requests @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18017 [codex] Add cross-repo plugin sources to marketplace manifests
      @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17277 feat: Add remote plugin fields to plugin API @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18395 /plugins: Add inline enablement toggles @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#14718 fix: trust-gate project hooks and exec policies @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18449 [codex] Describe uninstalled cross-repo plugin reads @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18499 Fix plugin cache panic when cwd is unavailable @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18212 [5/6] Wire executor-backed MCP stdio @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 28-apps-and-integrations-changes-in-rust-v0-122-0
  source_release: codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e
  source_type: github_releases
  theme: apps-integrations
  title: 28 Apps and Integrations changes in rust-v0.122.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-04-16-mcp-migration-hint-now-links-to-documentation-with-platform-specific-instruction|MCP
  migration hint now links to documentation with platform-specific instructions…]]'
- '[[Changes/GitHub Copilot CLI/2026-04-16-3-apps-and-integrations-changes-in-v1-0-29|3
  Apps and Integrations changes in v1.0.29]]'
- '[[Changes/Claude Code/2026-04-20-2-apps-and-integrations-changes-in-v2-1-116|2
  Apps and Integrations changes in v2.1.116]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e]]'
source_type: github_releases
theme: apps-integrations
title: 28 Apps and Integrations changes in rust-v0.122.0
type: change
---

<!-- chronolog:begin region="header" -->
# 28 Apps and Integrations changes in rust-v0.122.0

**Codex CLI** · 2026-04-20 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.122.0) · from [[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|0.122.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server approvals, user-input prompts, and MCP elicitations now disappear from the TUI when another client resolves them, instead of leaving stale prompts behind (#15134).

> Documented custom MCP server approval defaults and exec-server stdin behavior (#17843, #18086).

> Updated app-server docs for plugin API changes, marketplace removal, resume/fork token-usage replay, and warning notifications (#17277, #17751, #18023, #18298).

> Split plugin and marketplace code into `codex-core-plugins`, moved more connector code into `connectors`, and continued breaking up the large core session/turn modules (#18070, #18158, #18200, #18206, #18244, #18249).

> #17714 Support original-detail metadata on MCP image outputs @fjord-oai

> #17853 [mcp] Add dummy tools for previously called but currently missing tools. @mzeng-openai

> #17831 [codex][mcp] Add resource uri meta to tool call item. @mzeng-openai

> #18070 Extract plugin loading and marketplace logic into codex-core-plugins @xl-openai

> #18078 Fix MCP startup cancellation through app server @etraut-openai

> #18085 [1/8] Add MCP server environment config @aibrahim-oai

> #17287 [code mode] defer mcp tools from exec description @sayan-oai

> #18055 Improve external agent plugin migration for configured marketplaces @alexsong-oai

> #18158 Move more connector logic into connectors crate @pakrym-oai

> #17843 Add server-level approval defaults for custom MCP servers @mzeng-openai

> #18196 Use in-process app-server for unknown-thread MCP read test @mzeng-openai

> #18116 Move marketplace add under plugin command @xli-oai

> #18182 feat: Handle alternate plugin manifest paths @xl-openai

> #18246 Sync local plugin imports, async remote imports, refresh caches after… @alexsong-oai

> #17563 Add PermissionRequest hooks support @abhinav-oai

> #18087 [4/6] Abstract MCP stdio server launching @aibrahim-oai

> #18381 Remove the tier constraint from connectors directory requests @xl-openai

> #18017 [codex] Add cross-repo plugin sources to marketplace manifests @xli-oai

> #17277 feat: Add remote plugin fields to plugin API @xl-openai

> #18395 /plugins: Add inline enablement toggles @canvrno-oai

> #14718 fix: trust-gate project hooks and exec policies @viyatb-oai

> #18449 [codex] Describe uninstalled cross-repo plugin reads @xli-oai

> #18499 Fix plugin cache panic when cwd is unavailable @etraut-openai

> #18212 [5/6] Wire executor-backed MCP stdio @aibrahim-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.122.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-20-6-developer-workflow-changes-in-rust-v0-122-0|6 Developer Workflow changes in rust-v0.122.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-20-tool-discovery-and-image-generation-are-now-enabled-by-default-with-higher-detai|Tool discovery and image generation are now enabled by default, with higher-detail…]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-17153-launch-image-generation-by-default-won-openai|♯17153 Launch image generation by default @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-10-agent-mode-changes-in-rust-v0-122-0|10 Agent Mode changes in rust-v0.122.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-20-6-model-support-changes-in-rust-v0-122-0|6 Model Support changes in rust-v0.122.0]] · Model Support
- [[Changes/Codex CLI/2026-04-20-10-context-window-changes-in-rust-v0-122-0|10 Context Window changes in rust-v0.122.0]] · Context Window
- [[Changes/Codex CLI/2026-04-20-4-memory-and-personalization-changes-in-rust-v0-122-0|4 Memory and Personalization changes in rust-v0.122.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-20-18398-refactor-use-cloneable-async-channels-for-shared-receivers-bolinfest|♯18398 refactor: use cloneable async channels for shared receivers @bolinfest]] · Collaboration
- [[Changes/Codex CLI/2026-04-20-plugin-workflows-now-include-tabbed-browsing-inline-enable-disable-toggles-marke|Plugin workflows now include tabbed browsing, inline enable/disable toggles…]] · Search and Browsing
- [[Changes/Codex CLI/2026-04-20-9-safety-and-privacy-changes-in-rust-v0-122-0|9 Safety and Privacy changes in rust-v0.122.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-20-2-interface-experience-changes-in-rust-v0-122-0|2 Interface Experience changes in rust-v0.122.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-20-2-mobile-and-desktop-changes-in-rust-v0-122-0|2 Mobile and Desktop changes in rust-v0.122.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-20-100-other-changes-in-rust-v0-122-0|100 other changes in rust-v0.122.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-20 · Claude Code · [[Changes/Claude Code/2026-04-20-2-apps-and-integrations-changes-in-v2-1-116|2 Apps and Integrations changes in v2.1.116]]
- Later: 2026-04-22 · Claude Code · [[Changes/Claude Code/2026-04-22-4-apps-and-integrations-changes-in-v2-1-117|4 Apps and Integrations changes in v2.1.117]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-20-9d9efc&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-20-28-apps-and-integrations-changes-in-rust-v0-122-0.md%0ACard%20ID%3A%20codex-cli-2026-04-20-9d9efc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.122.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->