---
card_id: claude-code-2026-08-28-fc9086
date: '2026-08-28'
description: 'Claude Code · 2026-08-28 · Other changes: 8 changes in v2.1.251 — Added
  a Spend limit bar to `/usage` and a `rate_limits.spend_limit` status line field
  for…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 255a693a5463a31ca1d8fcd561c2e8beb7d6246f3292686bd522c2278a36ae40
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-28-fc9086
  comparison: ''
  date: '2026-08-28'
  description: 'Claude Code — v2.1.251: 8 other changes'
  evidence:
  - quote: Added a Spend limit bar to `/usage` and a `rate_limits.spend_limit` status
      line field for developers behind a Claude apps gateway with spend limits
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: Improved CPU usage during turns in interactive sessions by cutting redundant
      UI re-renders
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: 'Improved install size: the native binary is about 5 MB smaller'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: Improved the managed settings approval dialog to list only the settings
      that changed since you last approved them
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: Changed `/radio` to be available on Bedrock, Vertex AI, Foundry, and Claude
      Platform on AWS, and when telemetry is disabled
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: Changed the footer PR badge on Bedrock, Vertex, and Foundry, and when telemetry
      is off, to call the GitHub API directly (via `gh auth token`, `GH_TOKEN`, or
      `GITHUB_TOKEN`) instead of `gh pr view`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: Changed `ANTHROPIC_CUSTOM_HEADERS` from managed or project settings to
      require approval when it sets a credential, org/tenant, routing, or API-behavior
      header (e.g. `Authorization`, `Host`)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: Removed syntax highlighting for six rarely used languages (1c, gml, isbl,
      mathematica, maxima, sqf); the binary is 2.5 MB smaller
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 8-other-changes-in-v2-1-251
  source_release: claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96
  source_type: github_releases
  theme: uncategorized
  title: 8 other changes in v2.1.251
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96|claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96]]'
source_type: github_releases
superseded: true
theme: uncategorized
title: 8 other changes in v2.1.251
type: change
---

<!-- chronolog:begin region="header" -->
# 8 other changes in v2.1.251

**Claude Code** · 2026-08-28 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.251) · from [[Releases/Claude Code/claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96|v2.1.251]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a Spend limit bar to `/usage` and a `rate_limits.spend_limit` status line field for developers behind a Claude apps gateway with spend limits

> Improved CPU usage during turns in interactive sessions by cutting redundant UI re-renders

> Improved install size: the native binary is about 5 MB smaller

> Improved the managed settings approval dialog to list only the settings that changed since you last approved them

> Changed `/radio` to be available on Bedrock, Vertex AI, Foundry, and Claude Platform on AWS, and when telemetry is disabled

> Changed the footer PR badge on Bedrock, Vertex, and Foundry, and when telemetry is off, to call the GitHub API directly (via `gh auth token`, `GH_TOKEN`, or `GITHUB_TOKEN`) instead of `gh pr view`

> Changed `ANTHROPIC_CUSTOM_HEADERS` from managed or project settings to require approval when it sets a credential, org/tenant, routing, or API-behavior header (e.g. `Authorization`, `Host`)

> Removed syntax highlighting for six rarely used languages (1c, gml, isbl, mathematica, maxima, sqf); the binary is 2.5 MB smaller

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-28-changed-analytics-to-no-longer-turn-off-before-sign-in-solely-because-managed-se|Changed analytics to no longer turn off before sign-in solely because managed…]] · Account and Access
- [[Changes/Claude Code/2026-08-28-4-model-support-changes-in-v2-1-251|4 Model Support changes in v2.1.251]] · Model Support
- [[Changes/Claude Code/2026-08-28-added-a-per-session-prompt-cache-line-to-cost-hit-ratio-misses-tokens-re-cached|Added a per-session prompt-cache line to /cost…]] · Pricing Model
- [[Changes/Claude Code/2026-08-28-4-apps-and-integrations-changes-in-v2-1-251|4 Apps and Integrations changes in v2.1.251]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-28-3-developer-workflow-changes-in-v2-1-251|3 Developer Workflow changes in v2.1.251]] · Developer Workflow
- [[Changes/Claude Code/2026-08-28-improved-retry-when-the-model-s-tool-call-is-malformed-the-broken-output-is-now|Improved retry when the model's tool call is malformed]] · Context Window
- [[Changes/Claude Code/2026-08-28-4-agent-mode-changes-in-v2-1-251|4 Agent Mode changes in v2.1.251]] · Agent Mode
- [[Changes/Claude Code/2026-08-28-improved-amazon-bedrock-session-start-under-claude-code-provider-managed-by-host|Improved Amazon Bedrock session start under CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-28-6-safety-and-privacy-changes-in-v2-1-251|6 Safety and Privacy changes in v2.1.251]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-28-fc9086&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-28-8-other-changes-in-v2-1-251.md%0ACard%20ID%3A%20claude-code-2026-08-28-fc9086%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.251%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->