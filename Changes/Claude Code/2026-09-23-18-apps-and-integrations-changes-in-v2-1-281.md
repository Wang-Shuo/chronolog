---
card_id: claude-code-2026-09-23-b6b1f4
date: '2026-09-23'
description: 'Claude Code · 2026-09-23 · Apps and Integrations: 18 changes in v2.1.281
  — Added `assume_role` on Claude apps gateway Bedrock upstreams: the gateway calls…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1280
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 159c05152a0ffd710abd88a9fa2ec229341b239d4c4f8a07fa461d081884ef88
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-23-b6b1f4
  comparison: ''
  date: '2026-09-23'
  description: 'Claude Code — v2.1.281: 18 Apps and Integrations changes'
  evidence:
  - quote: 'Added `assume_role` on Claude apps gateway Bedrock upstreams: the gateway
      calls Bedrock as an IAM role it assumes through STS, in another AWS account
      if needed, optionally one session per developer'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Added `guardrail: {id, version}` on Claude apps gateway Bedrock upstreams
      to apply an Amazon Bedrock guardrail to every request sent through them (set
      it on all Bedrock upstreams or none)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Added MCP URL-mode elicitation on 2026-07-28 protocol connections, so servers
      can ask Claude Code to open a browser-based flow; no waiting dialog is left
      on screen when the server has no way to confirm completion
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Added MCP server checks to `claude plugin validate`: it reports `.mcp.json`
      entries that would be silently dropped at load, undeclared `${user_config.*}`
      references, and insecure URLs'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Added a scrollbar to the `/skills`, `/mcp` and `/plugin` Installed lists
      in fullscreen mode, like the one `/workflows` now has: it appears while the
      mouse is over the list and can be clicked or dragged'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Improved the time to resume very long sessions that have been compacted,
      most noticeably through the Agent SDK and Claude Desktop
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Improved plugin hook-failure errors to name the offending plugin, and added
      a `claude plugin validate` warning when a shell-form hook leaves `${CLAUDE_PLUGIN_ROOT}`
      unquoted (it breaks on plugin paths with spaces)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Improved the `/` menu, `/skills`, `/context` and the `/plugin` Installed
      list to show skills synced from claude.ai by their short name when no other
      command uses it, not `anthropic-skills:<name>`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Improved `/install-github-app`, `/desktop`, the `/permissions` auto mode
      environment prompts, and the `/plugin` "Add marketplace?" and "Run this command?"
      prompts: they now use the standard dialog frame with key hints, and Ctrl+C or
      Ctrl+D cancels them on the second press like other dialogs'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Improved the `/workflows` and `/mcp` lists: they page (PgUp/PgDn, Home/End)
      and take j/k and the mouse like other lists, their arrows follow `select:previous`/`select:next`
      rebinds, and `x` in `/workflows` stops the run the pointer is on'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Improved the `/plugin` plugin and marketplace details menus and the `/remote-control`
      already-connected menu: they now support Home/End and clicking a row'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Improved the /plugin Installed list: rows now line up in columns (status,
      name, type, details) across every section'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Improved `/hooks`: a hook''s detail screen now says what kind of hook
      it is and where to change it, instead of always pointing at settings.json, and
      the hooks-disabled, safe mode and managed-hooks-only notices each say what is
      happening in one plain sentence'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Changed /mcp: each server''s row now starts with its status icon and name,
      says its state once, and in a narrow terminal drops trailing facts like "managed"
      before shortening the name'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Changed Remote Control attachment downloads to reuse connections and to
      skip files already downloaded in the session
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Changed MCP resource lists (the resource list tool and @-mention suggestions)
      to skip MCP Apps UI resources; reading one by URI still works
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Changed `claude plugin uninstall --json` and the /plugin dialog to say
      a plugin's data was kept when its folder stays because another installed plugin
      uses it or install records cannot be read
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: '[Claude Tag] Added a short line in the Slack thread after someone presses
      Stop, naming who stopped Claude''s response and saying to mention @Claude to
      continue'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 18-apps-and-integrations-changes-in-v2-1-281
  source_release: claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95
  source_type: github_releases
  theme: apps-integrations
  title: 18 Apps and Integrations changes in v2.1.281
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-17-added-plugin-install-plugin-marketplace-source-which-offers-to-add-the-marketpla|Added
  /plugin install plugin --marketplace source, which offers to add…]]'
- '[[Changes/Claude Code/2026-09-18-6-apps-and-integrations-changes-in-v2-1-277|6
  Apps and Integrations changes in v2.1.277]]'
- '[[Changes/Claude Code/2026-09-22-8-apps-and-integrations-changes-in-v2-1-280|8
  Apps and Integrations changes in v2.1.280]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95|claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95]]'
source_type: github_releases
theme: apps-integrations
title: 18 Apps and Integrations changes in v2.1.281
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Apps and Integrations changes in v2.1.281

**Claude Code** · 2026-09-23 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.281) · from [[Releases/Claude Code/claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95|v2.1.281]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `assume_role` on Claude apps gateway Bedrock upstreams: the gateway calls Bedrock as an IAM role it assumes through STS, in another AWS account if needed, optionally one session per developer

> Added `guardrail: {id, version}` on Claude apps gateway Bedrock upstreams to apply an Amazon Bedrock guardrail to every request sent through them (set it on all Bedrock upstreams or none)

> Added MCP URL-mode elicitation on 2026-07-28 protocol connections, so servers can ask Claude Code to open a browser-based flow; no waiting dialog is left on screen when the server has no way to confirm completion

> Added MCP server checks to `claude plugin validate`: it reports `.mcp.json` entries that would be silently dropped at load, undeclared `${user_config.*}` references, and insecure URLs

> Added a scrollbar to the `/skills`, `/mcp` and `/plugin` Installed lists in fullscreen mode, like the one `/workflows` now has: it appears while the mouse is over the list and can be clicked or dragged

> Improved the time to resume very long sessions that have been compacted, most noticeably through the Agent SDK and Claude Desktop

> Improved plugin hook-failure errors to name the offending plugin, and added a `claude plugin validate` warning when a shell-form hook leaves `${CLAUDE_PLUGIN_ROOT}` unquoted (it breaks on plugin paths with spaces)

> Improved the `/` menu, `/skills`, `/context` and the `/plugin` Installed list to show skills synced from claude.ai by their short name when no other command uses it, not `anthropic-skills:<name>`

> Improved `/install-github-app`, `/desktop`, the `/permissions` auto mode environment prompts, and the `/plugin` "Add marketplace?" and "Run this command?" prompts: they now use the standard dialog frame with key hints, and Ctrl+C or Ctrl+D cancels them on the second press like other dialogs

> Improved the `/workflows` and `/mcp` lists: they page (PgUp/PgDn, Home/End) and take j/k and the mouse like other lists, their arrows follow `select:previous`/`select:next` rebinds, and `x` in `/workflows` stops the run the pointer is on

> Improved the `/plugin` plugin and marketplace details menus and the `/remote-control` already-connected menu: they now support Home/End and clicking a row

> Improved the /plugin Installed list: rows now line up in columns (status, name, type, details) across every section

> Improved `/hooks`: a hook's detail screen now says what kind of hook it is and where to change it, instead of always pointing at settings.json, and the hooks-disabled, safe mode and managed-hooks-only notices each say what is happening in one plain sentence

> Changed /mcp: each server's row now starts with its status icon and name, says its state once, and in a narrow terminal drops trailing facts like "managed" before shortening the name

> Changed Remote Control attachment downloads to reuse connections and to skip files already downloaded in the session

> Changed MCP resource lists (the resource list tool and @-mention suggestions) to skip MCP Apps UI resources; reading one by URI still works

> Changed `claude plugin uninstall --json` and the /plugin dialog to say a plugin's data was kept when its folder stays because another installed plugin uses it or install records cannot be read

> [Claude Tag] Added a short line in the Slack thread after someone presses Stop, naming who stopped Claude's response and saying to mention @Claude to continue

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-23-improved-interactive-startup-time-git-reads-startup-telemetry-and-the-bedrock-ve|Improved interactive startup time]] · Model Support
- [[Changes/Claude Code/2026-09-23-2-account-and-access-changes-in-v2-1-281|2 Account and Access changes in v2.1.281]] · Account and Access
- [[Changes/Claude Code/2026-09-23-claude-tag-changed-the-routine-list-claude-gives-when-asked-in-a-slack-thread-to|Claude Tag Changed the routine list Claude gives when asked in a Slack thread…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-09-23-7-developer-workflow-changes-in-v2-1-281|7 Developer Workflow changes in v2.1.281]] · Developer Workflow
- [[Changes/Claude Code/2026-09-23-2-mobile-and-desktop-changes-in-v2-1-281|2 Mobile and Desktop changes in v2.1.281]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-23-4-interface-experience-changes-in-v2-1-281|4 Interface Experience changes in v2.1.281]] · Interface Experience
- [[Changes/Claude Code/2026-09-23-9-agent-mode-changes-in-v2-1-281|9 Agent Mode changes in v2.1.281]] · Agent Mode
- [[Changes/Claude Code/2026-09-23-improved-deep-research-reliability-on-long-research-briefs-by-removing-unused-re|Improved /deep-research reliability on long research briefs by removing unused…]] · Search and Browsing
- [[Changes/Claude Code/2026-09-23-12-safety-and-privacy-changes-in-v2-1-281|12 Safety and Privacy changes in v2.1.281]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-23-improved-screen-reader-output-in-mcp-a-disabled-server-is-read-as-off-instead-of|Improved screen-reader output in /mcp]] · Accessibility and Localization
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-8-apps-and-integrations-changes-in-v2-1-280|8 Apps and Integrations changes in v2.1.280]]
- Later: 2026-09-23 · Cursor · [[Changes/Cursor/2026-09-23-integrations|Integrations]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-23-b6b1f4&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-23-18-apps-and-integrations-changes-in-v2-1-281.md%0ACard%20ID%3A%20claude-code-2026-09-23-b6b1f4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.281%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->