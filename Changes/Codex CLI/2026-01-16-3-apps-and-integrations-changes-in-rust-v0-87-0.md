---
card_id: codex-cli-2026-01-16-1071e7
date: '2026-01-16'
description: 'Codex CLI · 2026-01-16 · Apps and Integrations: 3 changes in 0.87.0
  — MCP CallToolResult now includes `threadId` in both `content` and `structuredContent`,
  and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1030
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d230d33e17de150f2c36ad707335718e480808f4ffb347d5b18920eb78948c69
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-16-1071e7
  comparison: ''
  date: '2026-01-16'
  description: 'Codex CLI — 0.87.0: 3 Apps and Integrations changes'
  evidence:
  - quote: MCP CallToolResult now includes `threadId` in both `content` and `structuredContent`,
      and returns a defined output schema for compatibility. (#9338)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  - quote: MCP interface docs updated to reflect structured output schema and `threadId`
      behavior. (#9338)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  - quote: '#9338 fix(mcp): include threadId in both content and structuredContent
      in CallToolResult @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.87.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-apps-and-integrations-changes-in-rust-v0-87-0
  source_release: codex-cli-2026-01-16-rust-v0-87-0-github-277440557-08f55bf8
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in rust-v0.87.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-01-14-9-apps-and-integrations-changes-in-v0-24-0|9 Apps
  and Integrations changes in v0.24.0]]'
- '[[Changes/Codex CLI/2026-01-15-9207-propagate-mcp-disabled-reason-gt-oai|♯9207
  Propagate MCP disabled reason @gt-oai]]'
- '[[Changes/Codex CLI/2026-01-16-accepting-an-mcp-elicitation-now-sends-an-empty-json-payload-instead-of-null-to|Accepting
  an MCP elicitation now sends an empty JSON payload instead of null…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-16-rust-v0-87-0-github-277440557-08f55bf8|codex-cli-2026-01-16-rust-v0-87-0-github-277440557-08f55bf8]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in rust-v0.87.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in rust-v0.87.0

**Codex CLI** · 2026-01-16 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.87.0) · from [[Releases/Codex CLI/codex-cli-2026-01-16-rust-v0-87-0-github-277440557-08f55bf8|0.87.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MCP CallToolResult now includes `threadId` in both `content` and `structuredContent`, and returns a defined output schema for compatibility. (#9338)

> MCP interface docs updated to reflect structured output schema and `threadId` behavior. (#9338)

> #9338 fix(mcp): include threadId in both content and structuredContent in CallToolResult @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.87.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-16-collaboration-wait-calls-can-block-on-multiple-ids-in-one-request-simplifying-mu|Collaboration wait calls can block on multiple IDs in one request, simplifying…]] · Collaboration
- [[Changes/Codex CLI/2026-01-16-9336-rename-model-turn-to-sampling-request-aibrahim-oai|♯9336 rename model turn to sampling request @aibrahim-oai]] · Model Support
- [[Changes/Codex CLI/2026-01-16-user-shell-commands-now-run-under-the-user-snapshot-so-aliases-and-shell-config|User shell commands now run under the user snapshot so aliases and shell config…]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-16-2-context-window-changes-in-rust-v0-87-0|2 Context Window changes in rust-v0.87.0]] · Context Window
- [[Changes/Codex CLI/2026-01-16-14-other-changes-in-rust-v0-87-0|14 other changes in rust-v0.87.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-01-16 · Codex CLI · [[Changes/Codex CLI/2026-01-16-accepting-an-mcp-elicitation-now-sends-an-empty-json-payload-instead-of-null-to|Accepting an MCP elicitation now sends an empty JSON payload instead of null…]]
- Later: 2026-01-16 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-01-16-mcp-servers-now-start-correctly-for-custom-agents|MCP servers now start correctly for custom agents]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-16-1071e7&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-16-3-apps-and-integrations-changes-in-rust-v0-87-0.md%0ACard%20ID%3A%20codex-cli-2026-01-16-1071e7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.87.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->