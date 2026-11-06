---
card_id: codex-cli-2026-07-29-5693fa
date: '2026-07-29'
description: 'Codex CLI · 2026-07-29 · Apps and Integrations: 47 changes in 0.146.0
  — Support Agent Plugins manifests, workspace plugin publishing, and additional plugin…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1224
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bfbfc46894ec2e41be148d380d1fde4f74cd46bee03428653250a2295c5dca43
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-29-5693fa
  comparison: ''
  date: '2026-07-29'
  description: 'Codex CLI — 0.146.0: 47 Apps and Integrations changes'
  evidence:
  - quote: 'Support Agent Plugins manifests, workspace plugin publishing, and additional
      plugin marketplaces for Amazon Bedrock and Claude Code. (#35105, #35254, #34931,
      #34979)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: 'Honor configured proxies across authentication, plugin downloads, MCP
      authorization, remote execution, WebSockets, redirects, and LM Studio connections.
      (#34479, #34509, #34655, #34678, #35023, #35056, #35239)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: 'Keep MCP connections and Apps tools current when authentication or configuration
      changes, reconnecting closed servers without restarting healthy connections.
      (#34952, #34957, #35028, #35144, #35146, #35151)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34506 Respect system proxies during plugin startup sync @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34509 Honor system proxy settings for remote plugins @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34522 Split MCP connection manager into focused modules @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34550 Test thread-scoped MCP refresh behavior @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34561 Extract MCP binding clients from the connection manager @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34573 Accept `forceRefetch` in plugin list requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34588 Bind MCP calls to captured catalog revisions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34644 Verify Git plugin SHA checkouts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34708 Rename the MCP connection manager to `McpConnectionSet` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34733 Make MCP resource clients follow the latest runtime @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34747 Register the MCP 2026-07-28 feature flag @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34786 Simplify app-server integration test setup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34839 Preserve user input when MCP startup is interrupted @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34849 Cache remote plugin catalogs by scope @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34851 Use batch metadata for plugin app summaries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34877 Wait for local plugin cache refreshes in `plugin/list` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34883 Set a default user agent for MCP HTTP requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34930 Centralize thread MCP state in `McpRuntime` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34931 Use the API plugin marketplace for Amazon Bedrock @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34952 Reuse MCP connections across runtime refreshes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34957 Replace closed MCP connections during reconciliation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34962 Move MCP connection helpers into the test module @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34979 Infer the bundled Claude Code plugin marketplace @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34991 Allow omitting MCP tool prefixes per server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35016 Add trusted plugin script attribution @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35020 Attribute command executions to trusted plugin scripts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35028 Preserve refreshed Apps tools across MCP runtime updates @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35029 Preserve plugin attribution across command approvals @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35144 Prewarm MCP runtime updates in the background @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35146 Refresh MCP runtimes when session auth changes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35151 Reconnect MCP servers on explicit refresh @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35164 Encapsulate MCP refresh coordination @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35194 Preserve output from hooks that exit before reading stdin @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35196 Make the Apps recovery exposure test deterministic @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35204 Refresh MCP runtimes across thread startup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35205 Use current MCP authority for elicitation reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35213 Refresh managed MCP requirements for active threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35216 Refresh MCP config independently across threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35239 Route MCP auth discovery through runtime HTTP clients @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35254 Expose workspace plugin publish capability @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35261 Propagate remote plugin IDs to skill metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35262 Track remote plugin IDs in skill invocation analytics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35280 Skip plugin MCP filtering when no allowlists are configured @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35414 Raise the MCP server recursion limit @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 47-apps-and-integrations-changes-in-rust-v0-146-0
  source_release: codex-cli-2026-07-29-rust-v0-146-0-github-361463950-6d491983
  source_type: github_releases
  theme: apps-integrations
  title: 47 Apps and Integrations changes in rust-v0.146.0
  type: change
related_changes:
- '[[Changes/Cline/2026-07-24-include-the-host-plugin-version-in-telemetry-events|Include
  the host plugin version in telemetry events]]'
- '[[Changes/Cursor/2026-07-28-plugins-mcp-servers-hooks-and-skills-to-extend-cursor-across-your-workflows|Plugins,
  MCP servers, hooks, and skills to extend Cursor across your workflows]]'
- '[[Changes/ChatGPT/2026-07-29-we-re-beginning-to-roll-out-sign-in-with-chatgpt-across-select-plugins-and-partn|Sign
  in with ChatGPT]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-29-rust-v0-146-0-github-361463950-6d491983|codex-cli-2026-07-29-rust-v0-146-0-github-361463950-6d491983]]'
source_type: github_releases
theme: apps-integrations
title: 47 Apps and Integrations changes in rust-v0.146.0
type: change
---

<!-- chronolog:begin region="header" -->
# 47 Apps and Integrations changes in rust-v0.146.0

**Codex CLI** · 2026-07-29 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.146.0) · from [[Releases/Codex CLI/codex-cli-2026-07-29-rust-v0-146-0-github-361463950-6d491983|0.146.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Support Agent Plugins manifests, workspace plugin publishing, and additional plugin marketplaces for Amazon Bedrock and Claude Code. (#35105, #35254, #34931, #34979)

> Honor configured proxies across authentication, plugin downloads, MCP authorization, remote execution, WebSockets, redirects, and LM Studio connections. (#34479, #34509, #34655, #34678, #35023, #35056, #35239)

> Keep MCP connections and Apps tools current when authentication or configuration changes, reconnecting closed servers without restarting healthy connections. (#34952, #34957, #35028, #35144, #35146, #35151)

> #34506 Respect system proxies during plugin startup sync @copyberry

> #34509 Honor system proxy settings for remote plugins @copyberry

> #34522 Split MCP connection manager into focused modules @copyberry

> #34550 Test thread-scoped MCP refresh behavior @copyberry

> #34561 Extract MCP binding clients from the connection manager @copyberry

> #34573 Accept `forceRefetch` in plugin list requests @copyberry

> #34588 Bind MCP calls to captured catalog revisions @copyberry

> #34644 Verify Git plugin SHA checkouts @copyberry

> #34708 Rename the MCP connection manager to `McpConnectionSet` @copyberry

> #34733 Make MCP resource clients follow the latest runtime @copyberry

> #34747 Register the MCP 2026-07-28 feature flag @copyberry

> #34786 Simplify app-server integration test setup @copyberry

> #34839 Preserve user input when MCP startup is interrupted @copyberry

> #34849 Cache remote plugin catalogs by scope @copyberry

> #34851 Use batch metadata for plugin app summaries @copyberry

> #34877 Wait for local plugin cache refreshes in `plugin/list` @copyberry

> #34883 Set a default user agent for MCP HTTP requests @copyberry

> #34930 Centralize thread MCP state in `McpRuntime` @copyberry

> #34931 Use the API plugin marketplace for Amazon Bedrock @copyberry

> #34952 Reuse MCP connections across runtime refreshes @copyberry

> #34957 Replace closed MCP connections during reconciliation @copyberry

> #34962 Move MCP connection helpers into the test module @copyberry

> #34979 Infer the bundled Claude Code plugin marketplace @copyberry

> #34991 Allow omitting MCP tool prefixes per server @copyberry

> #35016 Add trusted plugin script attribution @copyberry

> #35020 Attribute command executions to trusted plugin scripts @copyberry

> #35028 Preserve refreshed Apps tools across MCP runtime updates @copyberry

> #35029 Preserve plugin attribution across command approvals @copyberry

> #35144 Prewarm MCP runtime updates in the background @copyberry

> #35146 Refresh MCP runtimes when session auth changes @copyberry

> #35151 Reconnect MCP servers on explicit refresh @copyberry

> #35164 Encapsulate MCP refresh coordination @copyberry

> #35194 Preserve output from hooks that exit before reading stdin @copyberry

> #35196 Make the Apps recovery exposure test deterministic @copyberry

> #35204 Refresh MCP runtimes across thread startup @copyberry

> #35205 Use current MCP authority for elicitation reviews @copyberry

> #35213 Refresh managed MCP requirements for active threads @copyberry

> #35216 Refresh MCP config independently across threads @copyberry

> #35239 Route MCP auth discovery through runtime HTTP clients @copyberry

> #35254 Expose workspace plugin publish capability @copyberry

> #35261 Propagate remote plugin IDs to skill metadata @copyberry

> #35262 Track remote plugin IDs in skill invocation analytics @copyberry

> #35280 Skip plugin MCP filtering when no allowlists are configured @copyberry

> #35414 Raise the MCP server recursion limit @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.146.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-29-2-search-and-browsing-changes-in-rust-v0-146-0|2 Search and Browsing changes in rust-v0.146.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-29-2-mobile-and-desktop-changes-in-rust-v0-146-0|2 Mobile and Desktop changes in rust-v0.146.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-29-34850-disable-image-generation-for-free-plan-accounts-copyberry|♯34850 Disable image generation for Free-plan accounts @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-07-29-3-collaboration-changes-in-rust-v0-146-0|3 Collaboration changes in rust-v0.146.0]] · Collaboration
- [[Changes/Codex CLI/2026-07-29-3-model-support-changes-in-rust-v0-146-0|3 Model Support changes in rust-v0.146.0]] · Model Support
- [[Changes/Codex CLI/2026-07-29-5-context-window-changes-in-rust-v0-146-0|5 Context Window changes in rust-v0.146.0]] · Context Window
- [[Changes/Codex CLI/2026-07-29-35530-track-model-and-personality-in-world-state-copyberry|♯35530 Track model and personality in world state @copyberry]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-29-34643-migrate-login-http-construction-to-httpclient-copyberry|♯34643 Migrate login HTTP construction to HttpClient @copyberry]] · Account and Access
- [[Changes/Codex CLI/2026-07-29-8-interface-experience-changes-in-rust-v0-146-0|8 Interface Experience changes in rust-v0.146.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-29-12-developer-workflow-changes-in-rust-v0-146-0|12 Developer Workflow changes in rust-v0.146.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-29-11-agent-mode-changes-in-rust-v0-146-0|11 Agent Mode changes in rust-v0.146.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-29-3-editor-experience-changes-in-rust-v0-146-0|3 Editor Experience changes in rust-v0.146.0]] · Editor Experience
- [[Changes/Codex CLI/2026-07-29-6-safety-and-privacy-changes-in-rust-v0-146-0|6 Safety and Privacy changes in rust-v0.146.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-29-2-enterprise-and-administration-changes-in-rust-v0-146-0|2 Enterprise and Administration changes in rust-v0.146.0]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-07-29-2-files-and-data-changes-in-rust-v0-146-0|2 Files and Data changes in rust-v0.146.0]] · Files and Data
- [[Changes/Codex CLI/2026-07-29-129-other-changes-in-rust-v0-146-0|129 other changes in rust-v0.146.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-07-29 · ChatGPT · [[Changes/ChatGPT/2026-07-29-we-re-beginning-to-roll-out-sign-in-with-chatgpt-across-select-plugins-and-partn|Sign in with ChatGPT]]
- Later: 2026-07-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-30-2-apps-and-integrations-changes-in-v1-0-76|2 Apps and Integrations changes in v1.0.76]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-29-5693fa&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-29-47-apps-and-integrations-changes-in-rust-v0-146-0.md%0ACard%20ID%3A%20codex-cli-2026-07-29-5693fa%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.146.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->