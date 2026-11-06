---
card_id: codex-cli-2026-01-14-39d356
date: '2026-01-14'
description: 'Codex CLI · 2026-01-14 · Apps and Integrations: 10 changes in 0.81.0
  — The `codex` tool in `codex mcp-server` now includes the `threadId` in the response
  so it…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1028
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 28de40f8180e47e18bc81c0097d1e50c815340f13a1d76fa1b44243e214d4579
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-14-39d356
  comparison: ''
  date: '2026-01-14'
  description: 'Codex CLI — 0.81.0: 10 Apps and Integrations changes'
  evidence:
  - quote: 'The `codex` tool in `codex mcp-server` now includes the `threadId` in
      the response so it can be used with the `codex-reply` tool, fixing #3712. The
      documentation has been updated at https://developers.openai.com/codex/guides/agents-sdk/.
      (#9192)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8973 chore: add mcp call metric @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9010 fix: include AGENTS.md as repo root marker for integration tests
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8971 add static mcp callback uri support @WhammyLeaf'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8957 feat: hot reload mcp servers @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9129 Support response.done and add integration tests @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9101 Restrict MCP servers from `requirements.toml` @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#8661 Fix spinner/Esc interrupt when MCP startup completes mid-turn @2mawi2'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9166 fix: integration test for #9011 @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  - quote: '#9192 feat: add threadId to MCP server messages @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.81.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 10-apps-and-integrations-changes-in-rust-v0-81-0
  source_release: codex-cli-2026-01-14-rust-v0-81-0-github-276819252-cf63dc40
  source_type: github_releases
  theme: apps-integrations
  title: 10 Apps and Integrations changes in rust-v0.81.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-01-09-2-apps-and-integrations-changes-in-rust-v0-80-0|2
  Apps and Integrations changes in rust-v0.80.0]]'
- '[[Changes/Cline/2026-01-10-2-apps-and-integrations-changes-in-v3-49-0|2 Apps and
  Integrations changes in v3.49.0]]'
- '[[Changes/Claude Code/2026-01-13-2-apps-and-integrations-changes-in-v2-1-6|2 Apps
  and Integrations changes in v2.1.6]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-14-rust-v0-81-0-github-276819252-cf63dc40|codex-cli-2026-01-14-rust-v0-81-0-github-276819252-cf63dc40]]'
source_type: github_releases
theme: apps-integrations
title: 10 Apps and Integrations changes in rust-v0.81.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Apps and Integrations changes in rust-v0.81.0

**Codex CLI** · 2026-01-14 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.81.0) · from [[Releases/Codex CLI/codex-cli-2026-01-14-rust-v0-81-0-github-276819252-cf63dc40|0.81.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The `codex` tool in `codex mcp-server` now includes the `threadId` in the response so it can be used with the `codex-reply` tool, fixing #3712. The documentation has been updated at https://developers.openai.com/codex/guides/agents-sdk/. (#9192)

> #8973 chore: add mcp call metric @jif-oai

> #9010 fix: include AGENTS.md as repo root marker for integration tests @bolinfest

> #8971 add static mcp callback uri support @WhammyLeaf

> #8957 feat: hot reload mcp servers @shijie-oai

> #9129 Support response.done and add integration tests @pakrym-oai

> #9101 Restrict MCP servers from `requirements.toml` @gt-oai

> #8661 Fix spinner/Esc interrupt when MCP startup completes mid-turn @2mawi2

> #9166 fix: integration test for #9011 @bolinfest

> #9192 feat: add threadId to MCP server messages @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.81.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-14-2-agent-mode-changes-in-rust-v0-81-0|2 Agent Mode changes in rust-v0.81.0]] · Agent Mode
- [[Changes/Codex CLI/2026-01-14-2-interface-experience-changes-in-rust-v0-81-0|2 Interface Experience changes in rust-v0.81.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-14-5-developer-workflow-changes-in-rust-v0-81-0|5 Developer Workflow changes in rust-v0.81.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-14-2-account-and-access-changes-in-rust-v0-81-0|2 Account and Access changes in rust-v0.81.0]] · Account and Access
- [[Changes/Codex CLI/2026-01-14-5-safety-and-privacy-changes-in-rust-v0-81-0|5 Safety and Privacy changes in rust-v0.81.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-14-2-mobile-and-desktop-changes-in-rust-v0-81-0|2 Mobile and Desktop changes in rust-v0.81.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-14-9020-fix-tui-document-paste-burst-state-machine-joshka-oai|♯9020 fix(tui): document paste-burst state machine @joshka-oai]] · Files and Data
- [[Changes/Codex CLI/2026-01-14-8-model-support-changes-in-rust-v0-81-0|8 Model Support changes in rust-v0.81.0]] · Model Support
- [[Changes/Codex CLI/2026-01-14-2-editor-experience-changes-in-rust-v0-81-0|2 Editor Experience changes in rust-v0.81.0]] · Editor Experience
- [[Changes/Codex CLI/2026-01-14-72-other-changes-in-rust-v0-81-0|72 other changes in rust-v0.81.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-01-13 · Claude Code · [[Changes/Claude Code/2026-01-13-2-apps-and-integrations-changes-in-v2-1-6|2 Apps and Integrations changes in v2.1.6]]
- Later: 2026-01-14 · Gemini CLI · [[Changes/Gemini CLI/2026-01-14-9-apps-and-integrations-changes-in-v0-24-0|9 Apps and Integrations changes in v0.24.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-14-39d356&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-14-10-apps-and-integrations-changes-in-rust-v0-81-0.md%0ACard%20ID%3A%20codex-cli-2026-01-14-39d356%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.81.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->