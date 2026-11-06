---
card_id: github-copilot-cli-2026-04-09-2cfbe2
date: '2026-04-09'
description: 'GitHub Copilot CLI · 2026-04-09 · Apps and Integrations: 7 changes in
  1.0.22 — MCP tools with non-standard JSON schemas are now sanitized for compatibility…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1113
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b4a0bf48f9f99db81860fe181d76832762ccc03183a3093db3721e8b0bf97f21
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-04-09-2cfbe2
  comparison: ''
  date: '2026-04-09'
  description: 'GitHub Copilot CLI — 1.0.22: 7 Apps and Integrations changes'
  evidence:
  - quote: MCP tools with non-standard JSON schemas are now sanitized for compatibility
      with all model providers
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.22
  - quote: Better handling of large images from MCP and extension tools
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.22
  - quote: Plugins can now display a post-install message with setup instructions
      after installation
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.22
  - quote: Remove .vscode/mcp.json and .devcontainer/devcontainer.json as MCP server
      config sources; CLI now only reads .mcp.json. A migration hint appears when
      .vscode/mcp.json is detected without .mcp.json.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.22
  - quote: Plugins remain enabled across sessions and auto-install on startup based
      on user config
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.22
  - quote: sessionStart and sessionEnd hooks fire once per session in interactive
      mode instead of once per prompt
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.22
  - quote: Plugin agents respect the model specified in their frontmatter
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.22
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 7-apps-and-integrations-changes-in-v1-0-22
  source_release: github-copilot-cli-2026-04-09-v1-0-22-github-307239074-a988a80d
  source_type: github_releases
  theme: apps-integrations
  title: 7 Apps and Integrations changes in v1.0.22
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-08-this-release-introduces-updates-to-bugbot-including-the-ability-to-self-improve|Cursor
  introduces updates to Bugbot including the ability to self-improve in real…]]'
- '[[Changes/Gemini CLI/2026-04-08-3-apps-and-integrations-changes-in-v0-37-0|3 Apps
  and Integrations changes in v0.37.0]]'
- '[[Changes/Claude Code/2026-04-09-2-apps-and-integrations-changes-in-v2-1-98|2 Apps
  and Integrations changes in v2.1.98]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-09-v1-0-22-github-307239074-a988a80d|github-copilot-cli-2026-04-09-v1-0-22-github-307239074-a988a80d]]'
source_type: github_releases
theme: apps-integrations
title: 7 Apps and Integrations changes in v1.0.22
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Apps and Integrations changes in v1.0.22

**GitHub Copilot CLI** · 2026-04-09 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.22) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-09-v1-0-22-github-307239074-a988a80d|1.0.22]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MCP tools with non-standard JSON schemas are now sanitized for compatibility with all model providers

> Better handling of large images from MCP and extension tools

> Plugins can now display a post-install message with setup instructions after installation

> Remove .vscode/mcp.json and .devcontainer/devcontainer.json as MCP server config sources; CLI now only reads .mcp.json. A migration hint appears when .vscode/mcp.json is detected without .mcp.json.

> Plugins remain enabled across sessions and auto-install on startup based on user config

> sessionStart and sessionEnd hooks fire once per session in interactive mode instead of once per prompt

> Plugin agents respect the model specified in their frontmatter

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.22
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-04-09-permission-checks-and-other-hooks-now-work-correctly-when-using-anthropic-models|Permission checks and other hooks now work correctly when using Anthropic models…]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-04-09-support-bearer-token-authentication-for-byok-anthropic-models|Support bearer token authentication for BYOK Anthropic models]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-04-09-3-agent-mode-changes-in-v1-0-22|3 Agent Mode changes in v1.0.22]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-04-09-improved-rendering-performance-with-a-new-simplified-inline-renderer|Improved rendering performance with a new simplified inline renderer]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-04-09-slash-command-picker-appears-above-the-text-input-for-a-more-stable-layout|Slash command picker appears above the text input for a more stable layout]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-04-09-show-a-clear-message-to-contact-your-organization-administrator-when-remote-sess|Show a clear message to contact your organization administrator when remote sessions…]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-04-09-2-other-changes-in-v1-0-22|2 other changes in v1.0.22]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-09 · Claude Code · [[Changes/Claude Code/2026-04-09-2-apps-and-integrations-changes-in-v2-1-98|2 Apps and Integrations changes in v2.1.98]]
- Later: 2026-04-10 · Claude Code · [[Changes/Claude Code/2026-04-10-4-apps-and-integrations-changes-in-v2-1-101|4 Apps and Integrations changes in v2.1.101]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-04-09-2cfbe2&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-04-09-7-apps-and-integrations-changes-in-v1-0-22.md%0ACard%20ID%3A%20github-copilot-cli-2026-04-09-2cfbe2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.22%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->