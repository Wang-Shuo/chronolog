---
card_id: codex-cli-2025-10-09-6aca5e
date: '2025-10-09'
description: 'Codex CLI · 2025-10-09 · Apps and Integrations: 6 changes in 0.46.0
  — Enable the `experimental_use_rmcp_client = true` flag in `config.toml` to use
  the new MCP…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2491
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 17e467ca8788c7c3631a8bb632208f00616ddee136abe045c2b94c3ff7f95a98
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-10-09-6aca5e
  comparison: ''
  date: '2025-10-09'
  description: 'Codex CLI — 0.46.0: 6 Apps and Integrations changes'
  evidence:
  - quote: Enable the `experimental_use_rmcp_client = true` flag in `config.toml`
      to use the new MCP stack. If you encounter issues, create a GitHub issue and
      add the `mcp` label. We would like to remove the experimental flag soon and
      will continue to expand MCP support over time.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: Set codex SDK TypeScript originator by @pakrym-oai in https://github.com/openai/codex/pull/4894
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: '[MCP] Add the ability to explicitly specify a credentials store by @gpeal
      in https://github.com/openai/codex/pull/4857'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: '[MCP] Add support for streamable http servers with `codex mcp add` and
      replace bearer token handling by @gpeal in https://github.com/openai/codex/pull/4904'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: '[MCP] Add an `enabled` config field by @gpeal in https://github.com/openai/codex/pull/4917'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: '[MCP] Add auth status to MCP servers by @gpeal in https://github.com/openai/codex/pull/4918'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-apps-and-integrations-changes-in-rust-v0-46-0
  source_release: codex-cli-2025-10-09-rust-v0-46-0-github-253202599-fb352044
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in rust-v0.46.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2025-10-08-added-validation-for-mcp-server-names-fixes-https-github-com-github-copilot-cli|Added
  validation for MCP server names…]]'
- '[[Changes/AnythingLLM/2025-10-09-2-apps-and-integrations-changes-in-v1-9-0|2 Apps
  and Integrations changes in v1.9.0]]'
- '[[Changes/ChatGPT/2025-10-09-we-re-adding-notion-and-linear-as-synced-connectors-for-pro-users-so-you-can-sec|Adding
  Notion & Linear synced connectors]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-10-09-rust-v0-46-0-github-253202599-fb352044|codex-cli-2025-10-09-rust-v0-46-0-github-253202599-fb352044]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in rust-v0.46.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in rust-v0.46.0

**Codex CLI** · 2025-10-09 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.46.0) · from [[Releases/Codex CLI/codex-cli-2025-10-09-rust-v0-46-0-github-253202599-fb352044|0.46.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Enable the `experimental_use_rmcp_client = true` flag in `config.toml` to use the new MCP stack. If you encounter issues, create a GitHub issue and add the `mcp` label. We would like to remove the experimental flag soon and will continue to expand MCP support over time.

> Set codex SDK TypeScript originator by @pakrym-oai in https://github.com/openai/codex/pull/4894

> [MCP] Add the ability to explicitly specify a credentials store by @gpeal in https://github.com/openai/codex/pull/4857

> [MCP] Add support for streamable http servers with `codex mcp add` and replace bearer token handling by @gpeal in https://github.com/openai/codex/pull/4904

> [MCP] Add an `enabled` config field by @gpeal in https://github.com/openai/codex/pull/4917

> [MCP] Add auth status to MCP servers by @gpeal in https://github.com/openai/codex/pull/4918

Source: https://github.com/openai/codex/releases/tag/rust-v0.46.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-10-09-tui-switch-to-tree-sitter-highlight-bash-highlighting-by-nornagon-openai-in-http|TUI Switch to tree-sitter-highlight bash highlighting]] · Developer Workflow
- [[Changes/Codex CLI/2025-10-09-tui-breathing-spinner-on-true-color-terms-by-nornagon-openai-in-https-github-com|TUI Breathing spinner on true-color terms]] · Interface Experience
- [[Changes/Codex CLI/2025-10-09-make-context-line-permanent-by-dedrisian-oai-in-https-github-com-openai-codex-pu|Make context line permanent]] · Context Window
- [[Changes/Codex CLI/2025-10-09-we-are-in-the-middle-of-significantly-improving-support-for-connecting-to-mcp-se|We are in the middle of significantly improving support for connecting to MCP…]] · Account and Access
- [[Changes/Codex CLI/2025-10-09-20-other-changes-in-rust-v0-46-0|20 other changes in rust-v0.46.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-10-09 · ChatGPT · [[Changes/ChatGPT/2025-10-09-we-re-adding-notion-and-linear-as-synced-connectors-for-pro-users-so-you-can-sec|Adding Notion & Linear synced connectors]]
- Later: 2025-10-10 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-10-10-improved-argument-input-to-mcp-servers-in-mcp-add-previously-users-had-to-use-co|Improved argument input to MCP servers in /mcp add -- previously, users had to use…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-10-09-6aca5e&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-10-09-6-apps-and-integrations-changes-in-rust-v0-46-0.md%0ACard%20ID%3A%20codex-cli-2025-10-09-6aca5e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.46.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->