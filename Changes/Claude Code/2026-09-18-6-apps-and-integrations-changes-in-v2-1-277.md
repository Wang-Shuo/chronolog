---
card_id: claude-code-2026-09-18-a800e2
date: '2026-09-18'
description: 'Claude Code · 2026-09-18 · Apps and Integrations: 6 changes in v2.1.277
  — Added `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1` for Claude apps gateways whose
  only…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1275
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1dfbd20842ea59ffcfa74a2e373d903e3d0fcee0c5ed0e9d47a0a716dd7ee222
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-18-a800e2
  comparison: ''
  date: '2026-09-18'
  description: 'Claude Code — v2.1.277: 6 Apps and Integrations changes'
  evidence:
  - quote: 'Added `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1` for Claude apps gateways
      whose only egress is a forward proxy: every outbound request hands the proxy
      the hostname instead of resolving it locally'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
  - quote: Added an optional `headers:` map on Claude apps gateway upstreams, to send
      static headers to a proxy you run in front of a provider
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
  - quote: 'Improved session start-up for SDK and headless (`-p`) use: the first turn
      no longer waits on the per-directory CLAUDE.md lookup'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
  - quote: Improved the Claude apps gateway's loopback error messages to name `CLAUDE_GATEWAY_ALLOW_LOOPBACK`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
  - quote: 'Improved `/plugin` Installed: an MCP server listed apart from its plugin
      now shows which plugin it belongs to'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
  - quote: 'Improved `claude plugin install` on an already-installed plugin: it now
      says when the marketplace offers a newer version and names the `claude plugin
      update` command'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-apps-and-integrations-changes-in-v2-1-277
  source_release: claude-code-2026-09-18-v2-1-277-github-391616593-06a20f36
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in v2.1.277
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-17-10-apps-and-integrations-changes-in-v2-1-274|10
  Apps and Integrations changes in v2.1.274]]'
- '[[Changes/Claude Code/2026-09-17-6-apps-and-integrations-changes-in-v2-1-275|6
  Apps and Integrations changes in v2.1.275]]'
- '[[Changes/Claude Code/2026-09-17-added-plugin-install-plugin-marketplace-source-which-offers-to-add-the-marketpla|Added
  /plugin install plugin --marketplace source, which offers to add…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-18-v2-1-277-github-391616593-06a20f36|claude-code-2026-09-18-v2-1-277-github-391616593-06a20f36]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in v2.1.277
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in v2.1.277

**Claude Code** · 2026-09-18 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.277) · from [[Releases/Claude Code/claude-code-2026-09-18-v2-1-277-github-391616593-06a20f36|v2.1.277]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1` for Claude apps gateways whose only egress is a forward proxy: every outbound request hands the proxy the hostname instead of resolving it locally

> Added an optional `headers:` map on Claude apps gateway upstreams, to send static headers to a proxy you run in front of a provider

> Improved session start-up for SDK and headless (`-p`) use: the first turn no longer waits on the per-directory CLAUDE.md lookup

> Improved the Claude apps gateway's loopback error messages to name `CLAUDE_GATEWAY_ALLOW_LOOPBACK`

> Improved `/plugin` Installed: an MCP server listed apart from its plugin now shows which plugin it belongs to

> Improved `claude plugin install` on an already-installed plugin: it now says when the marketplace offers a newer version and names the `claude plugin update` command

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-18-3-enterprise-and-administration-changes-in-v2-1-277|3 Enterprise and Administration changes in v2.1.277]] · Enterprise and Administration
- [[Changes/Claude Code/2026-09-18-changed-ultrareview-in-non-interactive-sessions-to-refuse-when-the-repository-ha|Changed /ultrareview in non-interactive sessions to refuse when the repository has…]] · Collaboration
- [[Changes/Claude Code/2026-09-18-4-safety-and-privacy-changes-in-v2-1-277|4 Safety and Privacy changes in v2.1.277]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-18-vscode-added-the-session-s-cost-and-token-usage-to-the-account-usage-dialog-and|VSCode Added the session's cost and token usage to the Account & usage dialog…]] · Pricing Model
- [[Changes/Claude Code/2026-09-18-removed-the-background-haiku-auto-title-request-from-claude-p-runs-launched-outs|Removed the background Haiku auto-title request from claude -p runs launched…]] · Editor Experience
- [[Changes/Claude Code/2026-09-18-vscode-added-a-sign-out-row-to-the-panel-menu-with-logout-in-the-typed-command-m|VSCode Added a Sign out row to the panel menu, with /logout in the typed command menu]] · Interface Experience
- [[Changes/Claude Code/2026-09-18-improved-ultrareview-when-there-s-nothing-to-review-messages-say-which-case-you|Improved /ultrareview when there's nothing to review]] · Developer Workflow
- [[Changes/Claude Code/2026-09-18-claude-code-on-the-web-changed-the-admin-claude-code-setting-labeled-web-to-clou|Claude Code on the web Changed the admin Claude Code setting labeled…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-18-4-agent-mode-changes-in-v2-1-277|4 Agent Mode changes in v2.1.277]] · Agent Mode
- [[Changes/Claude Code/2026-09-18-changed-fable-to-always-appear-in-model-on-the-anthropic-api-it-is-greyed-out-on|Changed Fable to always appear in /model on the Anthropic API]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-added-plugin-install-plugin-marketplace-source-which-offers-to-add-the-marketpla|Added /plugin install plugin --marketplace source, which offers to add…]]
- Later: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-8-apps-and-integrations-changes-in-v2-1-280|8 Apps and Integrations changes in v2.1.280]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-18-a800e2&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-18-6-apps-and-integrations-changes-in-v2-1-277.md%0ACard%20ID%3A%20claude-code-2026-09-18-a800e2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.277%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->