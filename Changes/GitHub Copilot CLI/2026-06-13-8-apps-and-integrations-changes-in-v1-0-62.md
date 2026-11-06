---
card_id: github-copilot-cli-2026-06-13-0b8007
date: '2026-06-13'
description: 'GitHub Copilot CLI · 2026-06-13 · Apps and Integrations: 8 changes in
  1.0.62 — Plugins can now ship extensions, making them installable via the plugin…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1178
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2f4b71ef2556b4222cf5007493fb6c4a560b8e93a0a30d5ebc1abe9d68b0880e
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-13-0b8007
  comparison: ''
  date: '2026-06-13'
  description: 'GitHub Copilot CLI — 1.0.62: 8 Apps and Integrations changes'
  evidence:
  - quote: Plugins can now ship extensions, making them installable via the plugin
      marketplace
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  - quote: Add /app slash command to open the GitHub app or a browser fallback
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  - quote: Make the MCP server config form easier to use with a picker-based flow
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  - quote: Add session-scoped extensions and canvases
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  - quote: MCP server names with dots and slashes map to valid Responses API namespaces
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  - quote: Keep workspace MCP servers from restarting in a loop
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  - quote: Claude-format plugin `preToolUse` and `permissionRequest` hooks now fire
      correctly for tool matchers like `Bash`, `Read`, and `*`, and Claude-format
      hook payloads carry the Claude tool name (`Bash` rather than `bash`)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  - quote: Plugin install works when the marketplace ref is a fully-qualified tag
      (e.g. refs/tags/v2.1.0)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.62
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 8-apps-and-integrations-changes-in-v1-0-62
  source_release: github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e
  source_type: github_releases
  theme: apps-integrations
  title: 8 Apps and Integrations changes in v1.0.62
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-10-3-apps-and-integrations-changes-in-v2-1-172|3
  Apps and Integrations changes in v2.1.172]]'
- '[[Changes/Cline/2026-06-11-2-apps-and-integrations-changes-in-v3-89-2|2 Apps and
  Integrations changes in v3.89.2]]'
- '[[Changes/Cline/2026-06-11-restore-the-anthropic-provider-on-vs-code-1-123-and-later-where-the-updated-node|Restore
  the Anthropic provider on VS Code 1.123 and later, where the updated Node 24…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e|github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e]]'
source_type: github_releases
theme: apps-integrations
title: 8 Apps and Integrations changes in v1.0.62
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Apps and Integrations changes in v1.0.62

**GitHub Copilot CLI** · 2026-06-13 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.62) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-13-v1-0-62-github-339039020-f6ff7e5e|1.0.62]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Plugins can now ship extensions, making them installable via the plugin marketplace

> Add /app slash command to open the GitHub app or a browser fallback

> Make the MCP server config form easier to use with a picker-based flow

> Add session-scoped extensions and canvases

> MCP server names with dots and slashes map to valid Responses API namespaces

> Keep workspace MCP servers from restarting in a loop

> Claude-format plugin `preToolUse` and `permissionRequest` hooks now fire correctly for tool matchers like `Bash`, `Read`, and `*`, and Claude-format hook payloads carry the Claude tool name (`Bash` rather than `bash`)

> Plugin install works when the marketplace ref is a fully-qualified tag (e.g. refs/tags/v2.1.0)

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.62
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-13-speed-up-branch-and-head-detection-in-warm-sessions|Speed up branch and HEAD detection in warm sessions]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-13-4-agent-mode-changes-in-v1-0-62|4 Agent Mode changes in v1.0.62]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-13-every-and-after-can-now-schedule-slash-commands-e-g-every-1d-chronicle-standup|/every and /after can now schedule slash commands (e.g. /every 1d /chronicle standup)]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-13-voice-runtime-download-dialog-no-longer-reopens-in-a-loop-after-an-install-failu|Voice runtime download dialog no longer reopens in a loop after an install failure]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-06-13-2-safety-and-privacy-changes-in-v1-0-62|2 Safety and Privacy changes in v1.0.62]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-13-2-editor-experience-changes-in-v1-0-62|2 Editor Experience changes in v1.0.62]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-13-honor-max-output-tokens-for-byok-responses-providers|Honor max_output_tokens for BYOK Responses providers]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-13-remote-mcp-oauth-servers-start-only-once-per-matching-config-instead-of-restarti|Remote MCP OAuth servers start only once per matching config instead of restarting…]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-13-git-commands-no-longer-flash-a-console-window-on-windows|Git commands no longer flash a console window on Windows]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-06-13-allow-sdk-clients-to-configure-session-memory-through-session-create-and-session|Allow SDK clients to configure session memory through session.create and session.resume]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-06-13-3-interface-experience-changes-in-v1-0-62|3 Interface Experience changes in v1.0.62]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-13-3-model-support-changes-in-v1-0-62|3 Model Support changes in v1.0.62]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-13-improve-color-contrast-in-github-themes-to-meet-wcag-aa-accessibility-standards|Improve color contrast in GitHub themes to meet WCAG AA accessibility standards]] · Accessibility and Localization
- [[Changes/GitHub Copilot CLI/2026-06-13-6-developer-workflow-changes-in-v1-0-62|6 Developer Workflow changes in v1.0.62]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-13-14-other-changes-in-v1-0-62|14 other changes in v1.0.62]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-06-11 · Cline · [[Changes/Cline/2026-06-11-restore-the-anthropic-provider-on-vs-code-1-123-and-later-where-the-updated-node|Restore the Anthropic provider on VS Code 1.123 and later, where the updated Node 24…]]
- Later: 2026-06-15 · Claude Code · [[Changes/Claude Code/2026-06-15-2-apps-and-integrations-changes-in-v2-1-178|2 Apps and Integrations changes in v2.1.178]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-13-0b8007&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-13-8-apps-and-integrations-changes-in-v1-0-62.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-13-0b8007%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.62%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->