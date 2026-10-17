---
card_id: claude-code-2026-09-17-03c9eb
date: '2026-09-17'
description: 'Claude Code · 2026-09-17 · Apps and Integrations: 10 changes in v2.1.274
  — Added `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` to bound how long the first non-interactive…'
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
machine_hash: d382cfd0774bba8d990b1628cdcd98fa810ad2e2a6f5efbd22041ed933ad1f33
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-17-03c9eb
  comparison: ''
  date: '2026-09-17'
  description: 'Claude Code — v2.1.274: 10 Apps and Integrations changes'
  evidence:
  - quote: Added `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` to bound how long the first non-interactive
      turn waits for connecting MCP servers (`0` = don't wait)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: Added `store.connect_timeout_seconds` to the Claude apps gateway config
      to lengthen the Postgres connect timeout (default 5 seconds), and improved the
      boot error when the database is unreachable to point to `store.postgres_url`
      and the configured timeout
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: Added a Claude apps gateway warning when a replica has more requests open
      than the 256 it sends upstream at once, and a startup log line showing that
      limit
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: 'Improved startup in `--input-format stream-json` sessions: the first turn
      no longer waits up to 2s for still-connecting MCP servers whose tools tool search
      defers; they arrive on a later turn'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: 'Improved Claude apps gateway boot: it now tries the first Postgres connection
      up to three times before exiting, so a database that is reachable a few seconds
      late no longer fails the boot'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: 'Improved the Claude apps gateway''s spend-limit check under load: it now
      takes one database round trip instead of four, so fewer checks time out on a
      busy gateway'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: 'Changed Bedrock, Vertex, Foundry and telemetry-disabled installs to use
      the v2 MCP client and MCP 2026-07-28 negotiation with direct HTTP servers by
      default, as other installs already do (opt out: `MCP_SDK_GENERATION=v1` or `MCP_PROTOCOL_NEGOTIATION=legacy`)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: 'Changed `"type": "sdk"` MCP entries in `.mcp.json`, settings, plugins
      and agent files to be skipped with a warning: only an SDK host application can
      register in-process servers'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: Changed plugin and marketplace clones to leave Git LFS files as pointers
      instead of downloading them; `git lfs pull` in the checkout fetches them
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  - quote: '[Claude Tag] Improved Claude''s live progress checklist in Slack: capped
      at 2,000 characters, reposted at most every 15 minutes in busy threads, with
      older "Latest task list" links updated'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 10-apps-and-integrations-changes-in-v2-1-274
  source_release: claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d
  source_type: github_releases
  theme: apps-integrations
  title: 10 Apps and Integrations changes in v2.1.274
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-14-you-can-change-your-health-permissions-anytime-in-settings-plugins-health-learn|You
  can change your Health permissions anytime in Settings → Plugins → Health]]'
- '[[Changes/Claude Code/2026-09-14-5-apps-and-integrations-changes-in-v2-1-271|5
  Apps and Integrations changes in v2.1.271]]'
- '[[Changes/Claude Code/2026-09-15-3-apps-and-integrations-changes-in-v2-1-273|3
  Apps and Integrations changes in v2.1.273]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d|claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d]]'
source_type: github_releases
theme: apps-integrations
title: 10 Apps and Integrations changes in v2.1.274
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Apps and Integrations changes in v2.1.274

**Claude Code** · 2026-09-17 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.274) · from [[Releases/Claude Code/claude-code-2026-09-17-v2-1-274-github-390317660-0d9c7c5d|v2.1.274]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` to bound how long the first non-interactive turn waits for connecting MCP servers (`0` = don't wait)

> Added `store.connect_timeout_seconds` to the Claude apps gateway config to lengthen the Postgres connect timeout (default 5 seconds), and improved the boot error when the database is unreachable to point to `store.postgres_url` and the configured timeout

> Added a Claude apps gateway warning when a replica has more requests open than the 256 it sends upstream at once, and a startup log line showing that limit

> Improved startup in `--input-format stream-json` sessions: the first turn no longer waits up to 2s for still-connecting MCP servers whose tools tool search defers; they arrive on a later turn

> Improved Claude apps gateway boot: it now tries the first Postgres connection up to three times before exiting, so a database that is reachable a few seconds late no longer fails the boot

> Improved the Claude apps gateway's spend-limit check under load: it now takes one database round trip instead of four, so fewer checks time out on a busy gateway

> Changed Bedrock, Vertex, Foundry and telemetry-disabled installs to use the v2 MCP client and MCP 2026-07-28 negotiation with direct HTTP servers by default, as other installs already do (opt out: `MCP_SDK_GENERATION=v1` or `MCP_PROTOCOL_NEGOTIATION=legacy`)

> Changed `"type": "sdk"` MCP entries in `.mcp.json`, settings, plugins and agent files to be skipped with a warning: only an SDK host application can register in-process servers

> Changed plugin and marketplace clones to leave Git LFS files as pointers instead of downloading them; `git lfs pull` in the checkout fetches them

> [Claude Tag] Improved Claude's live progress checklist in Slack: capped at 2,000 characters, reposted at most every 15 minutes in busy threads, with older "Latest task list" links updated

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.274
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-17-improved-claude-apps-gateway-sign-in-rate-limit-errors-login-now-explains-the-re|Improved Claude apps gateway sign-in rate limit errors]] · Account and Access
- [[Changes/Claude Code/2026-09-17-2-model-support-changes-in-v2-1-274|2 Model Support changes in v2.1.274]] · Model Support
- [[Changes/Claude Code/2026-09-17-claude-code-on-the-web-changed-a-routine-s-on-hold-notice-when-your-subscription|Claude Code on the web Changed a routine's on-hold notice]] · Pricing Model
- [[Changes/Claude Code/2026-09-17-added-enduser-sub-the-idp-subject-to-the-telemetry-claude-desktop-and-cowork-sen|Added enduser.sub, the IdP subject, to the telemetry Claude Desktop and Cowork…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-17-vscode-improved-screen-reader-navigation-of-the-conversation-each-message-is-ann|VSCode Improved screen reader navigation of the conversation]] · Accessibility and Localization
- [[Changes/Claude Code/2026-09-17-7-developer-workflow-changes-in-v2-1-274|7 Developer Workflow changes in v2.1.274]] · Developer Workflow
- [[Changes/Claude Code/2026-09-17-vscode-added-a-claudecode-lockeditorgroups-setting-to-stop-claude-from-locking-t|VSCode Added a claudeCode.lockEditorGroups setting to stop Claude from locking…]] · Editor Experience
- [[Changes/Claude Code/2026-09-17-vscode-added-memory-and-instructions-entries-to-the-customize-menu-memory-shows|VSCode Added Memory and Instructions entries to the Customize menu]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-17-claude-tag-removed-the-repeated-guest-attribution-note-claude-appended-to-a-slac|Claude Tag Removed the repeated guest-attribution note Claude appended to a Slack…]] · Files and Data
- [[Changes/Claude Code/2026-09-17-2-interface-experience-changes-in-v2-1-274|2 Interface Experience changes in v2.1.274]] · Interface Experience
- [[Changes/Claude Code/2026-09-17-3-safety-and-privacy-changes-in-v2-1-274|3 Safety and Privacy changes in v2.1.274]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-17-added-a-visible-warning-when-memory-usage-is-critical-with-steps-to-free-memory|Added a visible warning when memory usage is critical, with steps to free memory…]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-17-8-other-changes-in-v2-1-274|8 other changes in v2.1.274]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-15 · Claude Code · [[Changes/Claude Code/2026-09-15-3-apps-and-integrations-changes-in-v2-1-273|3 Apps and Integrations changes in v2.1.273]]
- Later: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-6-apps-and-integrations-changes-in-v2-1-275|6 Apps and Integrations changes in v2.1.275]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-17-03c9eb&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-17-10-apps-and-integrations-changes-in-v2-1-274.md%0ACard%20ID%3A%20claude-code-2026-09-17-03c9eb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.274%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->