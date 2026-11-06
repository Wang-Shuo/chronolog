---
card_id: codex-cli-2026-08-07-37703f
date: '2026-08-07'
description: 'Codex CLI · 2026-08-07 · Apps and Integrations: 65 changes in 0.147.0
  — Install portable Agent Plugins and search across local, personal, workspace, and
  remote…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1233
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 014f255f685ffcfaf3d623fd3fe28e08a2eb952d0b4fa74c2a7fa9c263f2200d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-07-37703f
  comparison: ''
  date: '2026-08-07'
  description: 'Codex CLI — 0.147.0: 65 Apps and Integrations changes'
  evidence:
  - quote: 'Install portable Agent Plugins and search across local, personal, workspace,
      and remote plugin catalogs. (#36544, #36409, #36919, #36796)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: 'Support the opt-in MCP 2026-07-28 protocol, including paginated discovery,
      multi-round requests, and non-blocking server startup. (#35724, #35725, #35590,
      #35742)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: 'Prevent lost or stalled terminal input when focus returns, MCP servers
      initialize, or Ghostty handles keyboard shortcuts. (#35649, #35957, #36834)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: 'Harden plugin isolation and deny network access when policy updates fail.
      (#37027, #36967, #36037)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: 'Upgrade the MCP SDK to 3.0.0, Ratatui to 0.30.2, and V8 to 150.4.0. (#36001,
      #35959, #35831)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35590 Expose cached MCP tools before server startup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35675 Prepare MCP and plugin recommendations concurrently @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35724 Add MCP 2026-07-28 discovery support @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35725 Complete MCP 2026 client support @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35742 Avoid blocking turns on optional MCP startup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35777 Resolve MCP tool catalogs concurrently @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35794 Wait for MCP readiness in the curated sync test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35836 Clean up cancelled MCP elicitation requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35837 Expose plugin eligibility metadata in app-server summaries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35839 Decouple recommended plugins from tool suggestions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35840 Handle legacy MCP discovery prevalidation errors @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35856 Resolve imported connectors by MCP server name @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35859 Expose plugin installation timestamps in app-server summaries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35878 Use step environments for MCP file uploads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35937 Let unrelated tools run while MCP servers start @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35941 Bound MCP namespace descriptions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35957 Fix TUI input queue handling during MCP startup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36002 Resolve MCP file uploads with environment-native paths @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36011 Share optional MCP startup grace across connection sets @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36031 Load cloud-managed servers in MCP CLI commands @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36039 Limit MCP catalog pagination @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36047 Extract MCP environment headers into a local variable @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36055 Expose MCP read-only hints in tool call items @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36148 Harden the file change approval integration test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36218 Expose connector candidates in external agent detection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36306 Restrict hosted MCP credentials to local environments @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36339 Enable skills in the MCP server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36355 Keep MCP tool calls bound to their thread @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36359 Consolidate MCP config editing in codex-core @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36360 Use MCP bindings as the step tool catalog @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36365 Add strict automatic review for MCP elicitations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36402 Declare the experimental plugin search API @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36409 Implement remote plugin search @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36485 Increase remote plugin bundle size limits @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36534 Raise the MCP catalog item limit to 2,048 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36716 Deduplicate MCP resource operation handling @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36734 Deduplicate MCP resource list handling @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36769 Stabilize the startup Git enrichment integration test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36772 Raise the host-owned Codex Apps catalog limit @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36781 Add per-surface MCP tool exposure controls @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36792 Gate plugin usage instructions by model capability @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36796 Add Agent Plugins MCP config parsing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36810 Add MCP client conformance regression gates @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36882 Preserve complete MCP namespace descriptions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36895 Handle late MCP startup results after lag timeout @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36900 Register app tools independently of the connector list @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36910 Negotiate MCP extensions per app-server session @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36917 Test explicit plugin mentions with disabled apps @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36919 Merge local plugins into plugin search results @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36967 Skip symlinks when installing plugins @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36977 Improve connector detection for migrated sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36983 Preserve ChatGPT auth for trusted staging MCP servers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37000 Keep shared skill caches fresh across plugin loads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37027 Enforce Agent Plugin runtime boundaries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37066 Preserve longer MCP source descriptions in tool search @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37068 Fall back to per-process MCP cleanup on macOS @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37101 Reuse stable MCP bindings across sampling steps @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37167 Expose session sources to MCP contributors @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37168 Bound remote MCP handshake HTTP requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37169 Move plugin skill snapshot integration tests into core @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 65-apps-and-integrations-changes-in-rust-v0-147-0
  source_release: codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2
  source_type: github_releases
  theme: apps-integrations
  title: 65 Apps and Integrations changes in rust-v0.147.0
  type: change
related_changes:
- '[[Changes/Cline/2026-08-05-2-apps-and-integrations-changes-in-v4-1-4|2 Apps and
  Integrations changes in v4.1.4]]'
- '[[Changes/OpenHands/2026-08-05-chore-bump-openhands-extensions-to-0-16-0-by-hieptl-in-https-github-com-openhand|chore:
  bump @openhands/extensions to 0.16.0]]'
- '[[Changes/Claude Code/2026-08-07-3-apps-and-integrations-changes-in-v2-1-224|3
  Apps and Integrations changes in v2.1.224]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2|codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2]]'
source_type: github_releases
theme: apps-integrations
title: 65 Apps and Integrations changes in rust-v0.147.0
type: change
---

<!-- chronolog:begin region="header" -->
# 65 Apps and Integrations changes in rust-v0.147.0

**Codex CLI** · 2026-08-07 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.147.0) · from [[Releases/Codex CLI/codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2|0.147.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Install portable Agent Plugins and search across local, personal, workspace, and remote plugin catalogs. (#36544, #36409, #36919, #36796)

> Support the opt-in MCP 2026-07-28 protocol, including paginated discovery, multi-round requests, and non-blocking server startup. (#35724, #35725, #35590, #35742)

> Prevent lost or stalled terminal input when focus returns, MCP servers initialize, or Ghostty handles keyboard shortcuts. (#35649, #35957, #36834)

> Harden plugin isolation and deny network access when policy updates fail. (#37027, #36967, #36037)

> Upgrade the MCP SDK to 3.0.0, Ratatui to 0.30.2, and V8 to 150.4.0. (#36001, #35959, #35831)

> #35590 Expose cached MCP tools before server startup @copyberry

> #35675 Prepare MCP and plugin recommendations concurrently @copyberry

> #35724 Add MCP 2026-07-28 discovery support @copyberry

> #35725 Complete MCP 2026 client support @copyberry

> #35742 Avoid blocking turns on optional MCP startup @copyberry

> #35777 Resolve MCP tool catalogs concurrently @copyberry

> #35794 Wait for MCP readiness in the curated sync test @copyberry

> #35836 Clean up cancelled MCP elicitation requests @copyberry

> #35837 Expose plugin eligibility metadata in app-server summaries @copyberry

> #35839 Decouple recommended plugins from tool suggestions @copyberry

> #35840 Handle legacy MCP discovery prevalidation errors @copyberry

> #35856 Resolve imported connectors by MCP server name @copyberry

> #35859 Expose plugin installation timestamps in app-server summaries @copyberry

> #35878 Use step environments for MCP file uploads @copyberry

> #35937 Let unrelated tools run while MCP servers start @copyberry

> #35941 Bound MCP namespace descriptions @copyberry

> #35957 Fix TUI input queue handling during MCP startup @copyberry

> #36002 Resolve MCP file uploads with environment-native paths @copyberry

> #36011 Share optional MCP startup grace across connection sets @copyberry

> #36031 Load cloud-managed servers in MCP CLI commands @copyberry

> #36039 Limit MCP catalog pagination @copyberry

> #36047 Extract MCP environment headers into a local variable @copyberry

> #36055 Expose MCP read-only hints in tool call items @copyberry

> #36148 Harden the file change approval integration test @copyberry

> #36218 Expose connector candidates in external agent detection @copyberry

> #36306 Restrict hosted MCP credentials to local environments @copyberry

> #36339 Enable skills in the MCP server @copyberry

> #36355 Keep MCP tool calls bound to their thread @copyberry

> #36359 Consolidate MCP config editing in codex-core @copyberry

> #36360 Use MCP bindings as the step tool catalog @copyberry

> #36365 Add strict automatic review for MCP elicitations @copyberry

> #36402 Declare the experimental plugin search API @copyberry

> #36409 Implement remote plugin search @copyberry

> #36485 Increase remote plugin bundle size limits @copyberry

> #36534 Raise the MCP catalog item limit to 2,048 @copyberry

> #36716 Deduplicate MCP resource operation handling @copyberry

> #36734 Deduplicate MCP resource list handling @copyberry

> #36769 Stabilize the startup Git enrichment integration test @copyberry

> #36772 Raise the host-owned Codex Apps catalog limit @copyberry

> #36781 Add per-surface MCP tool exposure controls @copyberry

> #36792 Gate plugin usage instructions by model capability @copyberry

> #36796 Add Agent Plugins MCP config parsing @copyberry

> #36810 Add MCP client conformance regression gates @copyberry

> #36882 Preserve complete MCP namespace descriptions @copyberry

> #36895 Handle late MCP startup results after lag timeout @copyberry

> #36900 Register app tools independently of the connector list @copyberry

> #36910 Negotiate MCP extensions per app-server session @copyberry

> #36917 Test explicit plugin mentions with disabled apps @copyberry

> #36919 Merge local plugins into plugin search results @copyberry

> #36967 Skip symlinks when installing plugins @copyberry

> #36977 Improve connector detection for migrated sessions @copyberry

> #36983 Preserve ChatGPT auth for trusted staging MCP servers @copyberry

> #37000 Keep shared skill caches fresh across plugin loads @copyberry

> #37027 Enforce Agent Plugin runtime boundaries @copyberry

> #37066 Preserve longer MCP source descriptions in tool search @copyberry

> #37068 Fall back to per-process MCP cleanup on macOS @copyberry

> #37101 Reuse stable MCP bindings across sampling steps @copyberry

> #37167 Expose session sources to MCP contributors @copyberry

> #37168 Bound remote MCP handshake HTTP requests @copyberry

> #37169 Move plugin skill snapshot integration tests into core @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.147.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-07-10-collaboration-changes-in-rust-v0-147-0|10 Collaboration changes in rust-v0.147.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-07-8-account-and-access-changes-in-rust-v0-147-0|8 Account and Access changes in rust-v0.147.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-07-36140-wait-for-memory-consolidation-shutdown-before-finishing-jobs-copyberry|♯36140 Wait for memory consolidation shutdown before finishing jobs @copyberry]] · Memory and Personalization
- [[Changes/Codex CLI/2026-08-07-15-developer-workflow-changes-in-rust-v0-147-0|15 Developer Workflow changes in rust-v0.147.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-07-36043-document-the-responses-api-proxy-reqwest-exception-copyberry|♯36043 Document the Responses API proxy reqwest exception @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-08-07-36228-support-enterprise-automation-account-plans-copyberry|♯36228 Support Enterprise automation account plans @copyberry]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-08-07-3-search-and-browsing-changes-in-rust-v0-147-0|3 Search and Browsing changes in rust-v0.147.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-08-07-17-agent-mode-changes-in-rust-v0-147-0|17 Agent Mode changes in rust-v0.147.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-07-13-model-support-changes-in-rust-v0-147-0|13 Model Support changes in rust-v0.147.0]] · Model Support
- [[Changes/Codex CLI/2026-08-07-36807-extract-audio-preparation-into-a-utility-crate-copyberry|♯36807 Extract audio preparation into a utility crate @copyberry]] · Voice and Audio
- [[Changes/Codex CLI/2026-08-07-4-mobile-and-desktop-changes-in-rust-v0-147-0|4 Mobile and Desktop changes in rust-v0.147.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-07-9-safety-and-privacy-changes-in-rust-v0-147-0|9 Safety and Privacy changes in rust-v0.147.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-07-10-context-window-changes-in-rust-v0-147-0|10 Context Window changes in rust-v0.147.0]] · Context Window
- [[Changes/Codex CLI/2026-08-07-6-interface-experience-changes-in-rust-v0-147-0|6 Interface Experience changes in rust-v0.147.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-07-196-other-changes-in-rust-v0-147-0|196 other changes in rust-v0.147.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-08-07 · Claude Code · [[Changes/Claude Code/2026-08-07-3-apps-and-integrations-changes-in-v2-1-224|3 Apps and Integrations changes in v2.1.224]]
- Later: 2026-08-08 · Claude Code · [[Changes/Claude Code/2026-08-08-3-apps-and-integrations-changes-in-v2-1-225|3 Apps and Integrations changes in v2.1.225]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-07-37703f&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-07-65-apps-and-integrations-changes-in-rust-v0-147-0.md%0ACard%20ID%3A%20codex-cli-2026-08-07-37703f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.147.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->