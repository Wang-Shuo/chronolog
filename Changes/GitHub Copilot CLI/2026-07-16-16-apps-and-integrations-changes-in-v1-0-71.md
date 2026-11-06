---
card_id: github-copilot-cli-2026-07-16-c9a5d5
date: '2026-07-16'
description: 'GitHub Copilot CLI · 2026-07-16 · Apps and Integrations: 16 changes
  in 1.0.71 — Keep MCP tool lists up to date when servers change'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1211
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1f3a577b92adeb511f717f3276dcfe79b4f290157b974ab822b3e4e1e9562094
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-07-16-c9a5d5
  comparison: ''
  date: '2026-07-16'
  description: 'GitHub Copilot CLI — 1.0.71: 16 Apps and Integrations changes'
  evidence:
  - quote: Keep MCP tool lists up to date when servers change
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Keep all MCP Server Type options visible on short terminals
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Plan mode now hard-blocks built-in tool calls that would modify the workspace,
      so the agent can no longer edit files or run mutating shell commands while planning
      (built-in mutators like opening a pull request are blocked; MCP and external
      tools are still allowed)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Persist GitHub MCP toolset/tool config via settings.json (githubMcpToolsets,
      githubMcpTools, etc.)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Add `plugins marketplace` subcommands to list, add, and remove plugin marketplaces
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Show repo-enabled plugins in /plugin list and skill pickers
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Display plugin root skills as /plugin instead of /plugin:plugin
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Keep valid hooks in a config file when one hook entry is malformed
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Using --add-github-mcp-tool "\*" now enables all GitHub MCP tools
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Show a warning when a workspace MCP config is malformed or cannot be loaded
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Make bare `copilot mcp` and `copilot skill` print help and exit 0, matching
      `copilot plugin`. Consistent with `plugin`, the implicit `help <subcommand>`
      form is not supported for these groups; use `copilot mcp <subcommand> --help`
      (or `copilot skill <subcommand> --help`) instead.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Show --plugin-dir plugins in copilot plugin list
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Surface --plugin-dir warnings in the terminal
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Keep stored Git credential helpers available for marketplace plugin installs
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: 'Remove duplicate Error: prefixes from plugin command failures'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  - quote: Show the full command with its arguments (not just the wrapper) in the
      /mcp server detail view
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.71
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 16-apps-and-integrations-changes-in-v1-0-71
  source_release: github-copilot-cli-2026-07-16-v1-0-71-github-354824472-a089f622
  source_type: github_releases
  theme: apps-integrations
  title: 16 Apps and Integrations changes in v1.0.71
  type: change
related_changes:
- '[[Changes/Lovable/2026-07-13-let-your-app-s-users-connect-their-own-accounts|Let
  your app''s users connect their own accounts]]'
- '[[Changes/Claude Code/2026-07-14-3-apps-and-integrations-changes-in-v2-1-208|3
  Apps and Integrations changes in v2.1.208]]'
- '[[Changes/Claude Code/2026-07-15-2-apps-and-integrations-changes-in-v2-1-211|2
  Apps and Integrations changes in v2.1.211]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-16-v1-0-71-github-354824472-a089f622|github-copilot-cli-2026-07-16-v1-0-71-github-354824472-a089f622]]'
source_type: github_releases
theme: apps-integrations
title: 16 Apps and Integrations changes in v1.0.71
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Apps and Integrations changes in v1.0.71

**GitHub Copilot CLI** · 2026-07-16 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.71) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-16-v1-0-71-github-354824472-a089f622|1.0.71]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Keep MCP tool lists up to date when servers change

> Keep all MCP Server Type options visible on short terminals

> Plan mode now hard-blocks built-in tool calls that would modify the workspace, so the agent can no longer edit files or run mutating shell commands while planning (built-in mutators like opening a pull request are blocked; MCP and external tools are still allowed)

> Persist GitHub MCP toolset/tool config via settings.json (githubMcpToolsets, githubMcpTools, etc.)

> Add `plugins marketplace` subcommands to list, add, and remove plugin marketplaces

> Show repo-enabled plugins in /plugin list and skill pickers

> Display plugin root skills as /plugin instead of /plugin:plugin

> Keep valid hooks in a config file when one hook entry is malformed

> Using --add-github-mcp-tool "\*" now enables all GitHub MCP tools

> Show a warning when a workspace MCP config is malformed or cannot be loaded

> Make bare `copilot mcp` and `copilot skill` print help and exit 0, matching `copilot plugin`. Consistent with `plugin`, the implicit `help <subcommand>` form is not supported for these groups; use `copilot mcp <subcommand> --help` (or `copilot skill <subcommand> --help`) instead.

> Show --plugin-dir plugins in copilot plugin list

> Surface --plugin-dir warnings in the terminal

> Keep stored Git credential helpers available for marketplace plugin installs

> Remove duplicate Error: prefixes from plugin command failures

> Show the full command with its arguments (not just the wrapper) in the /mcp server detail view

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.71
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-07-16-3-model-support-changes-in-v1-0-71|3 Model Support changes in v1.0.71]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-07-16-server-mode-reconnects-oauth-mcp-servers-from-cached-tokens|Server mode reconnects OAuth MCP servers from cached tokens]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-07-16-5-editor-experience-changes-in-v1-0-71|5 Editor Experience changes in v1.0.71]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-07-16-add-canvas-support-in-the-cli-for-extension-driven-interactions|Add canvas support in the CLI for extension-driven interactions]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-07-16-refresh-memory-context-after-30-minutes-in-long-lived-sessions|Refresh memory context after 30 minutes in long-lived sessions]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-07-16-2-safety-and-privacy-changes-in-v1-0-71|2 Safety and Privacy changes in v1.0.71]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-07-16-8-developer-workflow-changes-in-v1-0-71|8 Developer Workflow changes in v1.0.71]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-07-16-3-pricing-model-changes-in-v1-0-71|3 Pricing Model changes in v1.0.71]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-07-16-2-collaboration-changes-in-v1-0-71|2 Collaboration changes in v1.0.71]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-07-16-2-context-window-changes-in-v1-0-71|2 Context Window changes in v1.0.71]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-07-16-add-plugins-marketplace-browse-and-update-commands|Add plugins marketplace browse and update commands]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-07-16-add-voice-devices-to-choose-and-persist-the-microphone-for-voice-mode|Add /voice devices to choose and persist the microphone for voice mode]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-07-16-5-interface-experience-changes-in-v1-0-71|5 Interface Experience changes in v1.0.71]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-07-16-8-agent-mode-changes-in-v1-0-71|8 Agent Mode changes in v1.0.71]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-07-16-30-other-changes-in-v1-0-71|30 other changes in v1.0.71]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-07-15 · Claude Code · [[Changes/Claude Code/2026-07-15-2-apps-and-integrations-changes-in-v2-1-211|2 Apps and Integrations changes in v2.1.211]]
- Later: 2026-07-16 · Lovable · [[Changes/Lovable/2026-07-16-reuse-your-workspace-identity-in-the-apps-you-build|Reuse your workspace identity in the apps you build]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-07-16-c9a5d5&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-07-16-16-apps-and-integrations-changes-in-v1-0-71.md%0ACard%20ID%3A%20github-copilot-cli-2026-07-16-c9a5d5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.71%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->