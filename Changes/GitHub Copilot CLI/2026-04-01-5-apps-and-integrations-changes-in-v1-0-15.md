---
card_id: github-copilot-cli-2026-04-01-c15746
date: '2026-04-01'
description: 'GitHub Copilot CLI · 2026-04-01 · Apps and Integrations: 5 changes in
  1.0.15 — Add mcp.config.list, mcp.config.add, mcp.config.update, and mcp.config.remove…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1105
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7a3be8e5c25a0f08683095436dd5331c2e85ce72373bed57b793e6396e14c07d
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-04-01-c15746
  comparison: ''
  date: '2026-04-01'
  description: 'GitHub Copilot CLI — 1.0.15: 5 Apps and Integrations changes'
  evidence:
  - quote: Add mcp.config.list, mcp.config.add, mcp.config.update, and mcp.config.remove
      server RPCs for managing persistent MCP server configuration
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.15
  - quote: Add postToolUseFailure hooks for tool errors and make postToolUse run only
      after successful tool calls
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.15
  - quote: MCP servers that are slow to connect no longer block the agent from starting
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.15
  - quote: MCP tools with long names no longer cause model API errors due to exceeding
      the 64-character limit
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.15
  - quote: Suppress spurious MCP server failure warnings from concurrent startup attempts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.15
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 5-apps-and-integrations-changes-in-v1-0-15
  source_release: github-copilot-cli-2026-04-01-v1-0-15-github-304307238-4db7dc28
  source_type: github_releases
  theme: apps-integrations
  title: 5 Apps and Integrations changes in v1.0.15
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-04-01-elevenagents-2b20f8|ElevenAgents]]'
- '[[Changes/ElevenLabs/2026-04-01-sdk-releases|SDK Releases]]'
- '[[Changes/Gemini CLI/2026-04-01-5-apps-and-integrations-changes-in-v0-36-0|5 Apps
  and Integrations changes in v0.36.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-01-v1-0-15-github-304307238-4db7dc28|github-copilot-cli-2026-04-01-v1-0-15-github-304307238-4db7dc28]]'
source_type: github_releases
theme: apps-integrations
title: 5 Apps and Integrations changes in v1.0.15
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Apps and Integrations changes in v1.0.15

**GitHub Copilot CLI** · 2026-04-01 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.15) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-01-v1-0-15-github-304307238-4db7dc28|1.0.15]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add mcp.config.list, mcp.config.add, mcp.config.update, and mcp.config.remove server RPCs for managing persistent MCP server configuration

> Add postToolUseFailure hooks for tool errors and make postToolUse run only after successful tool calls

> MCP servers that are slow to connect no longer block the agent from starting

> MCP tools with long names no longer cause model API errors due to exceeding the 64-character limit

> Suppress spurious MCP server failure warnings from concurrent startup attempts

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.15
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-04-01-remove-support-for-gpt-5-1-codex-gpt-5-1-codex-mini-and-gpt-5-1-codex-max-models|Remove support for gpt-5.1-codex, gpt-5.1-codex-mini, and gpt-5.1-codex-max models]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-04-01-3-editor-experience-changes-in-v1-0-15|3 Editor Experience changes in v1.0.15]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-04-01-2-account-and-access-changes-in-v1-0-15|2 Account and Access changes in v1.0.15]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-04-01-improved-performance-of-expand-collapse-ctrl-e-ctrl-o-in-alt-screen-mode-for-lon|Improved performance of expand/collapse (ctrl+e, ctrl+o) in alt-screen mode for long…]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-04-01-2-developer-workflow-changes-in-v1-0-15|2 Developer Workflow changes in v1.0.15]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-04-01-4-interface-experience-changes-in-v1-0-15|4 Interface Experience changes in v1.0.15]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-04-01-10-other-changes-in-v1-0-15|10 other changes in v1.0.15]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-01 · Gemini CLI · [[Changes/Gemini CLI/2026-04-01-5-apps-and-integrations-changes-in-v0-36-0|5 Apps and Integrations changes in v0.36.0]]
- Later: 2026-04-02 · Claude Code · [[Changes/Claude Code/2026-04-02-4-apps-and-integrations-changes-in-v2-1-91|4 Apps and Integrations changes in v2.1.91]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-04-01-c15746&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-04-01-5-apps-and-integrations-changes-in-v1-0-15.md%0ACard%20ID%3A%20github-copilot-cli-2026-04-01-c15746%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.15%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->