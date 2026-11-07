---
card_id: github-copilot-cli-2026-03-26-2f4eed
date: '2026-03-26'
description: 'GitHub Copilot CLI · 2026-03-26 · Apps and Integrations: 4 changes in
  1.0.12 — MCP servers defined in .mcp.json start correctly when the working directory
  is…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1099
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9b0b77ec23c21b6bde1d75ab7c5482b4817e5f18d0d6f95220d756c866091010
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-03-26-2f4eed
  comparison: ''
  date: '2026-03-26'
  description: 'GitHub Copilot CLI — 1.0.12: 4 Apps and Integrations changes'
  evidence:
  - quote: MCP servers defined in .mcp.json start correctly when the working directory
      is the git root
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  - quote: Plugin hooks now receive CLAUDE_PROJECT_DIR and CLAUDE_PLUGIN_DATA environment
      variables, and support {{project_dir}} and {{plugin_data_dir}} template variables
      in hook configurations
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  - quote: Workspace MCP servers are now correctly loaded and visible to the agent
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  - quote: /clear preserves MCP servers in the new session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.12
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-apps-and-integrations-changes-in-v1-0-12
  source_release: github-copilot-cli-2026-03-26-v1-0-12-github-302121824-04d76a7e
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v1.0.12
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-26-4-apps-and-integrations-changes-in-v2-1-85|4 Apps
  and Integrations changes in v2.1.85]]'
- '[[Changes/Codex CLI/2026-03-26-the-app-server-backed-tui-is-now-enabled-by-default-and-the-plugin-app-rollout-f|The
  app-server-backed TUI is now enabled by default, and the plugin/app rollout…]]'
- '[[Changes/Codex CLI/2026-03-26-57-apps-and-integrations-changes-in-rust-v0-117-0|57
  Apps and Integrations changes in rust-v0.117.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-26-v1-0-12-github-302121824-04d76a7e|github-copilot-cli-2026-03-26-v1-0-12-github-302121824-04d76a7e]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v1.0.12
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v1.0.12

**GitHub Copilot CLI** · 2026-03-26 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.12) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-26-v1-0-12-github-302121824-04d76a7e|1.0.12]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MCP servers defined in .mcp.json start correctly when the working directory is the git root

> Plugin hooks now receive CLAUDE_PROJECT_DIR and CLAUDE_PLUGIN_DATA environment variables, and support {{project_dir}} and {{plugin_data_dir}} template variables in hook configurations

> Workspace MCP servers are now correctly loaded and visible to the agent

> /clear preserves MCP servers in the new session

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.12
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-03-26-3-interface-experience-changes-in-v1-0-12|3 Interface Experience changes in v1.0.12]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-03-26-diff-view-correctly-renders-all-lines-when-intra-line-highlighting-is-present|/diff view correctly renders all lines when intra-line highlighting is present]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-03-26-cli-no-longer-crashes-with-out-of-memory-errors-when-running-shell-commands-that|CLI no longer crashes with out-of-memory errors when running shell commands…]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-03-26-resume-session-restores-the-previously-selected-custom-agent|Resume session restores the previously selected custom agent]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-03-26-model-display-header-shows-the-active-reasoning-effort-level-e-g-high-next-to-th|Model display header shows the active reasoning effort level (e.g. "(high)") next…]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-03-26-2-mobile-and-desktop-changes-in-v1-0-12|2 Mobile and Desktop changes in v1.0.12]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-03-26-2-developer-workflow-changes-in-v1-0-12|2 Developer Workflow changes in v1.0.12]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-03-26-12-other-changes-in-v1-0-12|12 other changes in v1.0.12]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-26 · Codex CLI · [[Changes/Codex CLI/2026-03-26-57-apps-and-integrations-changes-in-rust-v0-117-0|57 Apps and Integrations changes in rust-v0.117.0]]
- Later: 2026-03-27 · ChatGPT · [[Changes/ChatGPT/2026-03-27-we-re-rolling-out-updated-box-notion-linear-and-dropbox-apps-in-chatgpt-these-up-9f6ee9|Updated Box, Notion, Linear, and Dropbox apps]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-03-26-2f4eed&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-03-26-4-apps-and-integrations-changes-in-v1-0-12.md%0ACard%20ID%3A%20github-copilot-cli-2026-03-26-2f4eed%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.12%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->