---
card_id: github-copilot-cli-2026-03-20-0a1690
date: '2026-03-20'
description: 'GitHub Copilot CLI · 2026-03-20 · Apps and Integrations: 6 changes in
  1.0.10 — Repo hooks (.github/hooks/) now fire correctly when using prompt mode (-p
  flag)'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1093
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3b846ac07d52ba6622cb90af747a8175fb6ca6b89bee2c03d28965ade476ad61
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-03-20-0a1690
  comparison: ''
  date: '2026-03-20'
  description: 'GitHub Copilot CLI — 1.0.10: 6 Apps and Integrations changes'
  evidence:
  - quote: Repo hooks (.github/hooks/) now fire correctly when using prompt mode (-p
      flag)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.10
  - quote: SDK clients can register custom slash commands when starting or joining
      a session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.10
  - quote: SDK clients can show elicitation dialogs to the user via session.ui.elicitation
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.10
  - quote: Plugins using .claude-plugin/ or .plugin/ manifest directories now load
      their MCP and LSP servers correctly
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.10
  - quote: Workspace MCP servers from .mcp.json, .vscode/mcp.json, and devcontainer.json
      are now loaded only after folder trust is confirmed
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.10
  - quote: Plugins loaded via --plugin-dir now appear in /plugin list under a separate
      'External Plugins' section
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.10
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 6-apps-and-integrations-changes-in-v1-0-10
  source_release: github-copilot-cli-2026-03-20-v1-0-10-github-299512094-807f990b
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in v1.0.10
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-03-19-marketplace-and-plugin-installs-from-shortened-urls-e-g-aka-ms-links-now-work-co|Marketplace
  and plugin installs from shortened URLs (e.g., aka.ms links) now work…]]'
- '[[Changes/Claude Code/2026-03-20-3-apps-and-integrations-changes-in-v2-1-81|3 Apps
  and Integrations changes in v2.1.81]]'
- '[[Changes/Cline/2026-03-20-2-apps-and-integrations-changes-in-v3-75-0|2 Apps and
  Integrations changes in v3.75.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-20-v1-0-10-github-299512094-807f990b|github-copilot-cli-2026-03-20-v1-0-10-github-299512094-807f990b]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in v1.0.10
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in v1.0.10

**GitHub Copilot CLI** · 2026-03-20 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.10) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-20-v1-0-10-github-299512094-807f990b|1.0.10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Repo hooks (.github/hooks/) now fire correctly when using prompt mode (-p flag)

> SDK clients can register custom slash commands when starting or joining a session

> SDK clients can show elicitation dialogs to the user via session.ui.elicitation

> Plugins using .claude-plugin/ or .plugin/ manifest directories now load their MCP and LSP servers correctly

> Workspace MCP servers from .mcp.json, .vscode/mcp.json, and devcontainer.json are now loaded only after folder trust is confirmed

> Plugins loaded via --plugin-dir now appear in /plugin list under a separate 'External Plugins' section

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.10
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-03-20-reduced-memory-usage-when-viewing-large-files-in-their-entirety|Reduced memory usage when viewing large files in their entirety]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-03-20-2-developer-workflow-changes-in-v1-0-10|2 Developer Workflow changes in v1.0.10]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-03-20-login-device-flow-works-correctly-in-codespaces-and-remote-terminal-environments|/login device flow works correctly in Codespaces and remote terminal environments]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-03-20-session-history-is-no-longer-lost-when-exiting-via-quit-ctrl-c-or-restart|Session history is no longer lost when exiting via /quit, Ctrl+C, or restart]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-03-20-2-model-support-changes-in-v1-0-10|2 Model Support changes in v1.0.10]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-03-20-elicitation-form-shows-shift-tab-hint-for-navigating-between-fields-in-reverse|Elicitation form shows Shift+Tab hint for navigating between fields in reverse]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-03-20-2-collaboration-changes-in-v1-0-10|2 Collaboration changes in v1.0.10]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-03-20-7-other-changes-in-v1-0-10|7 other changes in v1.0.10]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-20 · Cline · [[Changes/Cline/2026-03-20-2-apps-and-integrations-changes-in-v3-75-0|2 Apps and Integrations changes in v3.75.0]]
- Later: 2026-03-23 · ElevenLabs · [[Changes/ElevenLabs/2026-03-23-workspaces|Workspaces]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-03-20-0a1690&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-03-20-6-apps-and-integrations-changes-in-v1-0-10.md%0ACard%20ID%3A%20github-copilot-cli-2026-03-20-0a1690%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.10%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->