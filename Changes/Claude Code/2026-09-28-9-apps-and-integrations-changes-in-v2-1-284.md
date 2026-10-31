---
card_id: claude-code-2026-09-28-7c2d11
date: '2026-09-28'
description: 'Claude Code · 2026-09-28 · Apps and Integrations: 9 changes in v2.1.284
  — Added `auth: { google: {} }` for Claude apps gateway `telemetry.forward_to`…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1285
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 229080f873f140359285b04dbbcb397f2ffe59afbfaf16a43274dbf0100a4eb4
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-28-7c2d11
  comparison: ''
  date: '2026-09-28'
  description: 'Claude Code — v2.1.284: 9 Apps and Integrations changes'
  evidence:
  - quote: 'Added `auth: { google: {} }` for Claude apps gateway `telemetry.forward_to`
      destinations, so telemetry can be exported straight to Google Cloud''s OTLP
      endpoint using the gateway''s Google Cloud credentials'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: 'Improved lists such as `/tasks`, `/copy` and `/hooks`: the details after
      each name now line up in one column when they fit, and otherwise sit at the
      right edge'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: Improved `claude plugin marketplace add` to say when it replaces a marketplace
      already added under the same name from a different source, and how to undo it
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: Changed the non-interactive first turn to still wait up to 2s for connecting
      MCP servers named by `--allowedTools` or an `mcp_tool` hook, even when `CLAUDE_CODE_MCP_STARTUP_WAIT_MS`
      is `0`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: Changed `/recap` to decline with a short notice when it arrives relayed
      from a chat thread (your own included) or from a routine or webhook; typed in
      the terminal, the Claude apps, Remote Control, `-p` or an SDK host, it runs
      as before
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: Changed `/artifacts` to show its filter tabs beside the title with one-word
      labels (All, Mine, Shared), using the same tab bar as `/config` and `/plugin`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: '[VSCode] Added plugin load errors and notes to the Manage plugins rows,
      with a popup to disable, uninstall or copy the error'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: '[Claude Tag] Improved the error shown when adding a channel manager fails
      because the channel''s Slack workspace can''t be confirmed as connected to your
      organization'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  - quote: '[Claude Tag] Improved a channel''s access lists in admin settings to show
      the connectors, repositories and plugins an auto-join pattern attaches, and
      where each comes from'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 9-apps-and-integrations-changes-in-v2-1-284
  source_release: claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49
  source_type: github_releases
  theme: apps-integrations
  title: 9 Apps and Integrations changes in v2.1.284
  type: change
related_changes:
- '[[Changes/Cursor/2026-09-23-integrations|Integrations]]'
- '[[Changes/Claude Code/2026-09-24-8-apps-and-integrations-changes-in-v2-1-282|8
  Apps and Integrations changes in v2.1.282]]'
- '[[Changes/Claude Code/2026-09-25-14-apps-and-integrations-changes-in-v2-1-283|14
  Apps and Integrations changes in v2.1.283]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49]]'
source_type: github_releases
superseded: true
theme: apps-integrations
title: 9 Apps and Integrations changes in v2.1.284
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Apps and Integrations changes in v2.1.284

**Claude Code** · 2026-09-28 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.284) · from [[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|v2.1.284]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `auth: { google: {} }` for Claude apps gateway `telemetry.forward_to` destinations, so telemetry can be exported straight to Google Cloud's OTLP endpoint using the gateway's Google Cloud credentials

> Improved lists such as `/tasks`, `/copy` and `/hooks`: the details after each name now line up in one column when they fit, and otherwise sit at the right edge

> Improved `claude plugin marketplace add` to say when it replaces a marketplace already added under the same name from a different source, and how to undo it

> Changed the non-interactive first turn to still wait up to 2s for connecting MCP servers named by `--allowedTools` or an `mcp_tool` hook, even when `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` is `0`

> Changed `/recap` to decline with a short notice when it arrives relayed from a chat thread (your own included) or from a routine or webhook; typed in the terminal, the Claude apps, Remote Control, `-p` or an SDK host, it runs as before

> Changed `/artifacts` to show its filter tabs beside the title with one-word labels (All, Mine, Shared), using the same tab bar as `/config` and `/plugin`

> [VSCode] Added plugin load errors and notes to the Manage plugins rows, with a popup to disable, uninstall or copy the error

> [Claude Tag] Improved the error shown when adding a channel manager fails because the channel's Slack workspace can't be confirmed as connected to your organization

> [Claude Tag] Improved a channel's access lists in admin settings to show the connectors, repositories and plugins an auto-join pattern attaches, and where each comes from

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.284
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-28-added-a-yes-but-ask-again-next-time-answer-to-auto-mode-s-prompt-before-a-read-o|Added a "Yes, but ask again next time" answer to auto mode's prompt before a read…]] · Agent Mode
- [[Changes/Claude Code/2026-09-28-claude-tag-improved-notify-members-now-in-admin-settings-one-press-reaches-every|Claude Tag Improved "Notify members now" in admin settings]] · Enterprise and Administration
- [[Changes/Claude Code/2026-09-28-2-memory-and-personalization-changes-in-v2-1-284|2 Memory and Personalization changes in v2.1.284]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-28-added-effortslider-decreaseeffort-increaseeffort-and-toggleultracode-keybinding|Added effortSlider:decreaseEffort, increaseEffort and toggleUltracode…]] · Interface Experience
- [[Changes/Claude Code/2026-09-28-2-pricing-model-changes-in-v2-1-284|2 Pricing Model changes in v2.1.284]] · Pricing Model
- [[Changes/Claude Code/2026-09-28-added-mcp-reconnect-all-in-the-interactive-terminal-to-retry-every-mcp-server-th|Added /mcp reconnect all in the interactive terminal to retry every MCP server…]] · Account and Access
- [[Changes/Claude Code/2026-09-28-2-collaboration-changes-in-v2-1-284|2 Collaboration changes in v2.1.284]] · Collaboration
- [[Changes/Claude Code/2026-09-28-4-safety-and-privacy-changes-in-v2-1-284|4 Safety and Privacy changes in v2.1.284]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-28-4-account-and-access-changes-in-v2-1-284|4 Account and Access changes in v2.1.284]] · Account and Access
- [[Changes/Claude Code/2026-09-28-changed-ultracode-into-its-own-toggle-in-effort-tab-or-effort-ultracode-on-off-i|Changed Ultracode into its own toggle in /effort (Tab, or /effort ultracode on / off)]] · Editor Experience
- [[Changes/Claude Code/2026-09-28-added-rate-limit-options-to-help-and-the-command-menu-for-claude-ai-subscribers|Added /rate-limit-options to /help and the command menu for claude.ai…]] · Interface Experience
- [[Changes/Claude Code/2026-09-28-6-model-support-changes-in-v2-1-284|6 Model Support changes in v2.1.284]] · Model Support
- [[Changes/Claude Code/2026-09-28-9-other-changes-in-v2-1-284|9 other changes in v2.1.284]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-25 · Claude Code · [[Changes/Claude Code/2026-09-25-14-apps-and-integrations-changes-in-v2-1-283|14 Apps and Integrations changes in v2.1.283]]
- Later: 2026-09-29 · ChatGPT · [[Changes/ChatGPT/2026-09-29-plugins-can-now-include-interactive-panels-sidebar-views-and-viewers-or-editors-d0bd7e|Work with interactive plugin extensions]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-28-7c2d11&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-28-9-apps-and-integrations-changes-in-v2-1-284.md%0ACard%20ID%3A%20claude-code-2026-09-28-7c2d11%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.284%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->