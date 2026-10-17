---
card_id: claude-code-2026-09-17-11e3ab
date: '2026-09-17'
description: 'Claude Code · 2026-09-17 · Apps and Integrations: 6 changes in v2.1.275
  — Improved prompt caching for a `--system-prompt` that contains a…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1274
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 56605128ab35648a046b831fd8ad685d86014a7d6e007207af51372634a00e21
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-17-11e3ab
  comparison: ''
  date: '2026-09-17'
  description: 'Claude Code — v2.1.275: 6 Apps and Integrations changes'
  evidence:
  - quote: 'Improved prompt caching for a `--system-prompt` that contains a `__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__`
      line: the text above it is now cached globally, as the SDK''s array form already
      is'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: Improved the `ListPlugins` tool description so Claude knows it lists plugins
      enabled on your claude.ai account, not plugins installed locally with `/plugin`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: Updated `/logout` for Claude apps gateway sign-ins to also end the session
      on gateways that advertise token revocation
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: Changed plugins installed from an npm source to be fetched with `npm pack
      --ignore-scripts` and integrity-verified, so a package's install scripts no
      longer run
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: '[VSCode] Added a Retry link to the MCP servers dialog when the server
      list fails to load'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: '[Claude Tag] Added attach conditions for access bundles in Claude Tag
      settings: an Owner can let a bundle also apply in channels with guests or Slack
      Connect channels, not just member-only'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-apps-and-integrations-changes-in-v2-1-275
  source_release: claude-code-2026-09-17-v2-1-275-github-391032307-12ccfafd
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in v2.1.275
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-14-5-apps-and-integrations-changes-in-v2-1-271|5
  Apps and Integrations changes in v2.1.271]]'
- '[[Changes/Claude Code/2026-09-15-3-apps-and-integrations-changes-in-v2-1-273|3
  Apps and Integrations changes in v2.1.273]]'
- '[[Changes/Claude Code/2026-09-17-10-apps-and-integrations-changes-in-v2-1-274|10
  Apps and Integrations changes in v2.1.274]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-17-v2-1-275-github-391032307-12ccfafd|claude-code-2026-09-17-v2-1-275-github-391032307-12ccfafd]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in v2.1.275
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in v2.1.275

**Claude Code** · 2026-09-17 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.275) · from [[Releases/Claude Code/claude-code-2026-09-17-v2-1-275-github-391032307-12ccfafd|v2.1.275]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved prompt caching for a `--system-prompt` that contains a `__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__` line: the text above it is now cached globally, as the SDK's array form already is

> Improved the `ListPlugins` tool description so Claude knows it lists plugins enabled on your claude.ai account, not plugins installed locally with `/plugin`

> Updated `/logout` for Claude apps gateway sign-ins to also end the session on gateways that advertise token revocation

> Changed plugins installed from an npm source to be fetched with `npm pack --ignore-scripts` and integrity-verified, so a package's install scripts no longer run

> [VSCode] Added a Retry link to the MCP servers dialog when the server list fails to load

> [Claude Tag] Added attach conditions for access bundles in Claude Tag settings: an Owner can let a bundle also apply in channels with guests or Slack Connect channels, not just member-only

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-17-vscode-improved-the-agent-map-the-pill-counts-running-agents-and-turns-red-after|VSCode Improved the agent map]] · Agent Mode
- [[Changes/Claude Code/2026-09-17-10-editor-experience-changes-in-v2-1-275|10 Editor Experience changes in v2.1.275]] · Editor Experience
- [[Changes/Claude Code/2026-09-17-vscode-added-viewing-editing-and-deleting-a-saved-memory-inside-the-memory-dialo|VSCode Added viewing, editing and deleting a saved memory inside the Memory dialog]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-17-7-safety-and-privacy-changes-in-v2-1-275|7 Safety and Privacy changes in v2.1.275]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-17-claude-tag-improved-claude-s-notices-in-enterprise-grid-channels-shared-across-w|Claude Tag Improved Claude's notices in Enterprise Grid channels shared across…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-09-17-added-a-send-now-key-ctrl-enter-or-ctrl-x-ctrl-s-that-interrupts-the-current-tur|Added a send-now key (ctrl+enter, or ctrl+x ctrl+s) that interrupts the current turn…]] · Model Support
- [[Changes/Claude Code/2026-09-17-2-developer-workflow-changes-in-v2-1-275|2 Developer Workflow changes in v2.1.275]] · Developer Workflow
- [[Changes/Claude Code/2026-09-17-added-the-signed-in-account-to-claude-apps-gateway-sign-in-when-the-gateway-name|Added the signed-in account to Claude apps gateway sign-in]] · Account and Access
- [[Changes/Claude Code/2026-09-17-improved-the-desktop-error-when-claude-desktop-does-not-open-it-now-says-why-and|Improved the /desktop error when Claude Desktop does not open]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-17-improved-the-artifact-tool-s-publish-and-read-results-they-now-say-who-can-open|Improved the Artifact tool's publish and read results]] · Interface Experience
- [[Changes/Claude Code/2026-09-17-added-plugin-install-plugin-marketplace-source-which-offers-to-add-the-marketpla|Added /plugin install plugin --marketplace source, which offers to add…]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-17-6-other-changes-in-v2-1-275|6 other changes in v2.1.275]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-10-apps-and-integrations-changes-in-v2-1-274|10 Apps and Integrations changes in v2.1.274]]
- Later: 2026-09-18 · Claude Code · [[Changes/Claude Code/2026-09-18-6-apps-and-integrations-changes-in-v2-1-277|6 Apps and Integrations changes in v2.1.277]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-17-11e3ab&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-17-6-apps-and-integrations-changes-in-v2-1-275.md%0ACard%20ID%3A%20claude-code-2026-09-17-11e3ab%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.275%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->