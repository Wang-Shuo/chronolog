---
card_id: github-copilot-cli-2026-03-16-a8f310
date: '2026-03-16'
description: 'GitHub Copilot CLI · 2026-03-16 · Apps and Integrations: 6 changes in
  1.0.6 — Hooks fire correctly when resuming a previous session'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1089
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fb02bb1ef7990ef2e777f84aa1d4ba313107c0e88533d98b4e6a9d37934d8794
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-03-16-a8f310
  comparison: ''
  date: '2026-03-16'
  description: 'GitHub Copilot CLI — 1.0.6: 6 Apps and Integrations changes'
  evidence:
  - quote: Hooks fire correctly when resuming a previous session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.6
  - quote: Flags --enable-all-github-mcp-tools, --add-github-mcp-toolset, and --add-github-mcp-tool
      now take effect when using the SDK (ACP mode)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.6
  - quote: Plugins using .claude-plugin/plugin.json are discovered when loaded via
      --plugin-dir
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.6
  - quote: Support Open Plugin spec file locations for loading plugin and marketplace
      manifests
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.6
  - quote: Hook config files now support Claude Code's nested matcher/hooks structure
      and optional type field
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.6
  - quote: 'Improve compatibility with the Open Plugins spec: support `.lsp.json`,
      PascalCase hook event names, `exclusive` path mode, and `:` namespace separator'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 6-apps-and-integrations-changes-in-v1-0-6
  source_release: github-copilot-cli-2026-03-16-v1-0-6-github-297705118-b80b4107
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in v1.0.6
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-03-16-17-apps-and-integrations-changes-in-rust-v0-115-0|17
  Apps and Integrations changes in rust-v0.115.0]]'
- '[[Changes/ElevenLabs/2026-03-16-javascript-sdk|JavaScript SDK]]'
- '[[Changes/ElevenLabs/2026-03-16-sdk-releases|SDK Releases]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-16-v1-0-6-github-297705118-b80b4107|github-copilot-cli-2026-03-16-v1-0-6-github-297705118-b80b4107]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in v1.0.6
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in v1.0.6

**GitHub Copilot CLI** · 2026-03-16 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.6) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-16-v1-0-6-github-297705118-b80b4107|1.0.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hooks fire correctly when resuming a previous session

> Flags --enable-all-github-mcp-tools, --add-github-mcp-toolset, and --add-github-mcp-tool now take effect when using the SDK (ACP mode)

> Plugins using .claude-plugin/plugin.json are discovered when loaded via --plugin-dir

> Support Open Plugin spec file locations for loading plugin and marketplace manifests

> Hook config files now support Claude Code's nested matcher/hooks structure and optional type field

> Improve compatibility with the Open Plugins spec: support `.lsp.json`, PascalCase hook event names, `exclusive` path mode, and `:` namespace separator

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-03-16-remaining-requests-widget-no-longer-shows-inaccurate-quota-data-for-copilot-free|Remaining requests widget no longer shows inaccurate quota data for Copilot Free users]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-03-16-model-can-discover-and-use-tools-dynamically-with-tool-search-for-claude-models|Model can discover and use tools dynamically with tool search for Claude models]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-03-16-extension-tools-now-work-with-the-permissions-system-use-skippermission-per-tool|Extension tools now work with the permissions system, use skipPermission per-tool…]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-03-16-custom-instruction-file-paths-load-correctly-when-using-copilot-custom-instructi|Custom instruction file paths load correctly when using COPILOT_CUSTOM_INSTRUCTIONS_DIRS]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-03-16-4-developer-workflow-changes-in-v1-0-6|4 Developer Workflow changes in v1.0.6]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-03-16-show-friendlier-error-messages-and-provide-keyboard-shortcut-to-open-event-links|Show friendlier error messages and provide keyboard shortcut to open event links…]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-03-16-5-agent-mode-changes-in-v1-0-6|5 Agent Mode changes in v1.0.6]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-03-16-3-mobile-and-desktop-changes-in-v1-0-6|3 Mobile and Desktop changes in v1.0.6]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-03-16-3-reliability-and-performance-changes-in-v1-0-6|3 Reliability and Performance changes in v1.0.6]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-03-16-8-other-changes-in-v1-0-6|8 other changes in v1.0.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-16 · ElevenLabs · [[Changes/ElevenLabs/2026-03-16-sdk-releases|SDK Releases]]
- Later: 2026-03-16 · Lovable · [[Changes/Lovable/2026-03-16-app-connectors-twitch-twilio-linear-telegram-and-contentful|App connectors: Twitch, Twilio, Linear, Telegram, and Contentful]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-03-16-a8f310&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-03-16-6-apps-and-integrations-changes-in-v1-0-6.md%0ACard%20ID%3A%20github-copilot-cli-2026-03-16-a8f310%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->