---
card_id: github-copilot-cli-2026-03-31-6459da
date: '2026-03-31'
description: 'GitHub Copilot CLI · 2026-03-31 · Apps and Integrations: 5 changes in
  1.0.14 — Allow SDK session participants to respond to elicitation requests via…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1104
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3a3bf0a2d2c106e422a2f5fe2f6f50ed3997d9aafd7ade7722b230718943f8c9
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-03-31-6459da
  comparison: ''
  date: '2026-03-31'
  description: 'GitHub Copilot CLI — 1.0.14: 5 Apps and Integrations changes'
  evidence:
  - quote: Allow SDK session participants to respond to elicitation requests via handlePendingElicitation
      API
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.14
  - quote: SDK exit_plan_mode.requested event is now always emitted, regardless of
      whether a direct callback is configured
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.14
  - quote: MCP servers blocked by allowlist policy are now hidden from /mcp show
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.14
  - quote: Uninstalling a marketplace plugin removes its cached data from disk
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.14
  - quote: MCP registry lookups are more reliable with automatic retries and request
      timeouts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.14
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 5-apps-and-integrations-changes-in-v1-0-14
  source_release: github-copilot-cli-2026-03-31-v1-0-14-github-303495089-79909e3a
  source_type: github_releases
  theme: apps-integrations
  title: 5 Apps and Integrations changes in v1.0.14
  type: change
related_changes:
- '[[Changes/OpenCode/2026-03-30-2-apps-and-integrations-changes-in-v1-3-9-1|2 Apps
  and Integrations changes in v1.3.9 + 1]]'
- '[[Changes/OpenHands/2026-03-30-added-support-for-hooks-by-xingyaoww-in-https-github-com-openhands-openhands-pul|Added
  support for hooks]]'
- '[[Changes/Codex CLI/2026-03-31-12-apps-and-integrations-changes-in-rust-v0-118-0|12
  Apps and Integrations changes in rust-v0.118.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-31-v1-0-14-github-303495089-79909e3a|github-copilot-cli-2026-03-31-v1-0-14-github-303495089-79909e3a]]'
source_type: github_releases
theme: apps-integrations
title: 5 Apps and Integrations changes in v1.0.14
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Apps and Integrations changes in v1.0.14

**GitHub Copilot CLI** · 2026-03-31 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.14) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-31-v1-0-14-github-303495089-79909e3a|1.0.14]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Allow SDK session participants to respond to elicitation requests via handlePendingElicitation API

> SDK exit_plan_mode.requested event is now always emitted, regardless of whether a direct callback is configured

> MCP servers blocked by allowlist policy are now hidden from /mcp show

> Uninstalling a marketplace plugin removes its cached data from disk

> MCP registry lookups are more reliable with automatic retries and request timeouts

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.14
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-03-31-3-model-support-changes-in-v1-0-14|3 Model Support changes in v1.0.14]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-03-31-2-interface-experience-changes-in-v1-0-14|2 Interface Experience changes in v1.0.14]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-03-31-grep-and-glob-search-results-return-promptly-when-a-timeout-is-reached|Grep and glob search results return promptly when a timeout is reached]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-03-31-2-safety-and-privacy-changes-in-v1-0-14|2 Safety and Privacy changes in v1.0.14]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-03-31-mcp-server-oauth-authentication-works-when-the-cli-runs-in-acp-mode|MCP server OAuth authentication works when the CLI runs in ACP mode]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-03-31-4-developer-workflow-changes-in-v1-0-14|4 Developer Workflow changes in v1.0.14]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-03-31-2-reliability-and-performance-changes-in-v1-0-14|2 Reliability and Performance changes in v1.0.14]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-03-31-6-other-changes-in-v1-0-14|6 other changes in v1.0.14]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-31 · Codex CLI · [[Changes/Codex CLI/2026-03-31-12-apps-and-integrations-changes-in-rust-v0-118-0|12 Apps and Integrations changes in rust-v0.118.0]]
- Later: 2026-03-31 · OpenCode · [[Changes/OpenCode/2026-03-31-4-apps-and-integrations-changes-in-v1-3-12-2|4 Apps and Integrations changes in v1.3.12 + 2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-03-31-6459da&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-03-31-5-apps-and-integrations-changes-in-v1-0-14.md%0ACard%20ID%3A%20github-copilot-cli-2026-03-31-6459da%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.14%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->