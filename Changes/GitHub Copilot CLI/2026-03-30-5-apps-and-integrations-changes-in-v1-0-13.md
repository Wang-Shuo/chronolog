---
card_id: github-copilot-cli-2026-03-30-3c7483
date: '2026-03-30'
description: 'GitHub Copilot CLI · 2026-03-30 · Apps and Integrations: 5 changes in
  1.0.13 — SDK exit_plan_mode.requested event is now always emitted, regardless of
  whether…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1103
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fa840041b5b191fdf95f5f161978a6452a6fb885bc0f5923b3ba26a9886e7dbe
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-03-30-3c7483
  comparison: ''
  date: '2026-03-30'
  description: 'GitHub Copilot CLI — 1.0.13: 5 Apps and Integrations changes'
  evidence:
  - quote: SDK exit_plan_mode.requested event is now always emitted, regardless of
      whether a direct callback is configured
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.13
  - quote: MCP registry lookups are more reliable with automatic retries and request
      timeouts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.13
  - quote: MCP servers can request LLM inference (sampling) with user approval via
      a new review prompt
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.13
  - quote: MCP servers blocked by allowlist policy are now hidden from /mcp show
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.13
  - quote: Uninstalling a marketplace plugin removes its cached data from disk
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.13
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 5-apps-and-integrations-changes-in-v1-0-13
  source_release: github-copilot-cli-2026-03-30-v1-0-13-github-303313822-db3397e2
  source_type: github_releases
  theme: apps-integrations
  title: 5 Apps and Integrations changes in v1.0.13
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-03-26-4-apps-and-integrations-changes-in-v1-0-12|4
  Apps and Integrations changes in v1.0.12]]'
- '[[Changes/ChatGPT/2026-03-27-we-re-rolling-out-updated-box-notion-linear-and-dropbox-apps-in-chatgpt-these-up-9f6ee9|Updated
  Box, Notion, Linear, and Dropbox apps]]'
- '[[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|Reduced
  startup event-loop stalls when many claude.ai MCP connectors are configured…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-30-v1-0-13-github-303313822-db3397e2|github-copilot-cli-2026-03-30-v1-0-13-github-303313822-db3397e2]]'
source_type: github_releases
theme: apps-integrations
title: 5 Apps and Integrations changes in v1.0.13
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Apps and Integrations changes in v1.0.13

**GitHub Copilot CLI** · 2026-03-30 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.13) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-30-v1-0-13-github-303313822-db3397e2|1.0.13]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> SDK exit_plan_mode.requested event is now always emitted, regardless of whether a direct callback is configured

> MCP registry lookups are more reliable with automatic retries and request timeouts

> MCP servers can request LLM inference (sampling) with user approval via a new review prompt

> MCP servers blocked by allowlist policy are now hidden from /mcp show

> Uninstalling a marketplace plugin removes its cached data from disk

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.13
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-03-30-grep-and-glob-search-results-return-promptly-when-a-timeout-is-reached|Grep and glob search results return promptly when a timeout is reached]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-03-30-mcp-server-oauth-authentication-works-when-the-cli-runs-in-acp-mode|MCP server OAuth authentication works when the CLI runs in ACP mode]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-03-30-2-interface-experience-changes-in-v1-0-13|2 Interface Experience changes in v1.0.13]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-03-30-2-developer-workflow-changes-in-v1-0-13|2 Developer Workflow changes in v1.0.13]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-03-30-2-model-support-changes-in-v1-0-13|2 Model Support changes in v1.0.13]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-03-30-mcp-servers-using-microsoft-entra-id-authentication-no-longer-show-the-consent-s|MCP servers using Microsoft Entra ID authentication no longer show the consent…]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-03-30-2-reliability-and-performance-changes-in-v1-0-13|2 Reliability and Performance changes in v1.0.13]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-03-30-5-other-changes-in-v1-0-13|5 other changes in v1.0.13]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-27 · Claude Code · [[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|Reduced startup event-loop stalls when many claude.ai MCP connectors are configured…]]
- Later: 2026-03-30 · OpenHands · [[Changes/OpenHands/2026-03-30-added-support-for-hooks-by-xingyaoww-in-https-github-com-openhands-openhands-pul|Added support for hooks]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-03-30-3c7483&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-03-30-5-apps-and-integrations-changes-in-v1-0-13.md%0ACard%20ID%3A%20github-copilot-cli-2026-03-30-3c7483%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.13%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->