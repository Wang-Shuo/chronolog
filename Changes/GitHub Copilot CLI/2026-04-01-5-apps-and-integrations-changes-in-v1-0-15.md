---
card_id: github-copilot-cli-2026-04-01-c15746
date: '2026-04-01'
description: 'GitHub Copilot CLI · 2026-04-01 · Apps and Integrations: 5 changes in
  1.0.15 — Add mcp.config.list, mcp.config.add, mcp.config.update, and mcp.config.remove…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2665
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 28ebd493302a249a40433d28a7f31b269339d33514fd2ffd8879ec3fd64b96bd
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
- Later: 2026-04-02 · AnythingLLM · [[Changes/AnythingLLM/2026-04-02-2-apps-and-integrations-changes-in-v1-12-0|2 Apps and Integrations changes in v1.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-04-01-c15746&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-04-01-5-apps-and-integrations-changes-in-v1-0-15.md%0ACard%20ID%3A%20github-copilot-cli-2026-04-01-c15746%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.15%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->