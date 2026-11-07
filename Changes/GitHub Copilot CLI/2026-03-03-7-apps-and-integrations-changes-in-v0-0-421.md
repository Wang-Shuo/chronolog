---
card_id: github-copilot-cli-2026-03-03-699cb8
date: '2026-03-03'
description: 'GitHub Copilot CLI · 2026-03-03 · Apps and Integrations: 7 changes in
  0.0.421 — Add structured form input for the ask_user tool using MCP Elicitations…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1076
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 84578e99544cbdc69da7ada72b60fb7f14bf55d98a509e58dedba8d7dbf873f1
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-03-03-699cb8
  comparison: ''
  date: '2026-03-03'
  description: 'GitHub Copilot CLI — 0.0.421: 7 Apps and Integrations changes'
  evidence:
  - quote: Add structured form input for the ask_user tool using MCP Elicitations
      (experimental)
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.421
  - quote: Plugin commands read extraKnownMarketplaces from project-level .claude/settings.json
      for Claude compatibility
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.421
  - quote: Git hooks can detect Copilot CLI subprocesses via the COPILOT_CLI=1 environment
      variable to skip interactive prompts
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.421
  - quote: Python-based MCP servers no longer time out due to buffered stdout
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.421
  - quote: MCP server availability correctly updates after signing in, switching accounts,
      or signing out
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.421
  - quote: Add --plugin-dir flag to load a plugin from a local directory
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.421
  - quote: MCP elicitation form displays taller multi-line text input, hides tab bar
      for single-field forms, and fixes error flashing on field navigation
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.421
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 7-apps-and-integrations-changes-in-v0-0-421
  source_release: github-copilot-cli-2026-03-03-v0-0-421-github-292666876-368c942d
  source_type: github_releases
  theme: apps-integrations
  title: 7 Apps and Integrations changes in v0.0.421
  type: change
related_changes:
- '[[Changes/Cursor/2026-03-03-mcp-apps-support-interactive-user-interfaces-like-charts-from-amplitude-diagrams|MCP
  Apps]]'
- '[[Changes/Cursor/2026-03-03-on-teams-and-enterprise-plans-admins-can-now-create-team-marketplaces-to-share-p|Team
  marketplaces for plugins]]'
- '[[Changes/Gemini CLI/2026-03-03-3-apps-and-integrations-changes-in-v0-32-0|3 Apps
  and Integrations changes in v0.32.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-03-v0-0-421-github-292666876-368c942d|github-copilot-cli-2026-03-03-v0-0-421-github-292666876-368c942d]]'
source_type: github_releases
theme: apps-integrations
title: 7 Apps and Integrations changes in v0.0.421
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Apps and Integrations changes in v0.0.421

**GitHub Copilot CLI** · 2026-03-03 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v0.0.421) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-03-v0-0-421-github-292666876-368c942d|0.0.421]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add structured form input for the ask_user tool using MCP Elicitations (experimental)

> Plugin commands read extraKnownMarketplaces from project-level .claude/settings.json for Claude compatibility

> Git hooks can detect Copilot CLI subprocesses via the COPILOT_CLI=1 environment variable to skip interactive prompts

> Python-based MCP servers no longer time out due to buffered stdout

> MCP server availability correctly updates after signing in, switching accounts, or signing out

> Add --plugin-dir flag to load a plugin from a local directory

> MCP elicitation form displays taller multi-line text input, hides tab bar for single-field forms, and fixes error flashing on field navigation

Source: https://github.com/github/copilot-cli/releases/tag/v0.0.421
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-03-03-right-click-paste-no-longer-produces-garbled-text-on-windows|Right-click paste no longer produces garbled text on Windows]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-03-03-shell-command-output-on-windows-no-longer-renders-as-no-changes-detected-in-the|Shell command output on Windows no longer renders as "No changes detected" in the timeline]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-03-03-2-editor-experience-changes-in-v0-0-421|2 Editor Experience changes in v0.0.421]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-03-03-2-model-support-changes-in-v0-0-421|2 Model Support changes in v0.0.421]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-03-03-autopilot-permission-dialog-appears-on-first-prompt-submission-instead-of-on-mod|Autopilot permission dialog appears on first prompt submission instead of on mode switch]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-03-03-2-interface-experience-changes-in-v0-0-421|2 Interface Experience changes in v0.0.421]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-03-03-4-developer-workflow-changes-in-v0-0-421|4 Developer Workflow changes in v0.0.421]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-03-03-2-other-changes-in-v0-0-421|2 other changes in v0.0.421]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-03 · Gemini CLI · [[Changes/Gemini CLI/2026-03-03-3-apps-and-integrations-changes-in-v0-32-0|3 Apps and Integrations changes in v0.32.0]]
- Later: 2026-03-03 · OpenCode · [[Changes/OpenCode/2026-03-03-2-apps-and-integrations-changes-in-v1-2-16|2 Apps and Integrations changes in v1.2.16]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-03-03-699cb8&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-03-03-7-apps-and-integrations-changes-in-v0-0-421.md%0ACard%20ID%3A%20github-copilot-cli-2026-03-03-699cb8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv0.0.421%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->