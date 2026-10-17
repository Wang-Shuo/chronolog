---
card_id: claude-code-2026-05-11-45cd62
date: '2026-05-11'
description: 'Claude Code · 2026-05-11 · Apps and Integrations: 8 changes in v2.1.139
  — Added `claude plugin details <name>` to show a plugin''s component inventory and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1145
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ef7aacc36ee9918a55aeecc33dfb671cb0a1be9f2b063d5fb1de6761829e1d65
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-11-45cd62
  comparison: ''
  date: '2026-05-11'
  description: 'Claude Code — v2.1.139: 8 Apps and Integrations changes'
  evidence:
  - quote: Added `claude plugin details <name>` to show a plugin's component inventory
      and projected per-session token cost
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.139
  - quote: MCP stdio servers now receive `CLAUDE_PROJECT_DIR` in their environment,
      matching hooks. Plugin configs can reference `${CLAUDE_PROJECT_DIR}` in commands
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.139
  - quote: '`/mcp` Reconnect now picks up `.mcp.json` edits without a restart, and
      shows the HTTP status and URL when reconnecting fails'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.139
  - quote: '`claude plugin install <name>@<marketplace>` now auto-refreshes the marketplace
      and retries before reporting a plugin as not found'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.139
  - quote: '`/plugin` installed-plugin details now show hook event names and MCP server
      names cleanly'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.139
  - quote: '`/context` now shows the providing plugin''s name for plugin-sourced skills'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.139
  - quote: Remote MCP server reconnect retry on transient failures is now enabled
      for all users
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.139
  - quote: Remote Control, `/schedule`, claude.ai MCP connectors, and notification
      preferences are now disabled when `ANTHROPIC_API_KEY` / `apiKeyHelper` / `ANTHROPIC_AUTH_TOKEN`
      is set, even if a Claude.ai login also exists. Unset the API key to use these
      features
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.139
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 8-apps-and-integrations-changes-in-v2-1-139
  source_release: claude-code-2026-05-11-v2-1-139-github-320692766-5e65de7d
  source_type: github_releases
  theme: apps-integrations
  title: 8 Apps and Integrations changes in v2.1.139
  type: change
related_changes:
- '[[Changes/Cursor/2026-05-07-made-mcp-connection-behavior-more-predictable-and-added-explicit-stale-token-cle|Made
  MCP connection behavior more predictable, and added explicit stale token…]]'
- '[[Changes/Claude Code/2026-05-08-changed-plugin-marketplace-removal-key-to-d-matching-delete-elsewhere-instead-of|Changed
  plugin marketplace removal key to d (matching delete elsewhere) instead…]]'
- '[[Changes/Claude Code/2026-05-11-added-goal-command-set-a-completion-condition-and-claude-keeps-working-across-tu|Added
  /goal command]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-11-v2-1-139-github-320692766-5e65de7d|claude-code-2026-05-11-v2-1-139-github-320692766-5e65de7d]]'
source_type: github_releases
theme: apps-integrations
title: 8 Apps and Integrations changes in v2.1.139
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Apps and Integrations changes in v2.1.139

**Claude Code** · 2026-05-11 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.139) · from [[Releases/Claude Code/claude-code-2026-05-11-v2-1-139-github-320692766-5e65de7d|v2.1.139]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `claude plugin details <name>` to show a plugin's component inventory and projected per-session token cost

> MCP stdio servers now receive `CLAUDE_PROJECT_DIR` in their environment, matching hooks. Plugin configs can reference `${CLAUDE_PROJECT_DIR}` in commands

> `/mcp` Reconnect now picks up `.mcp.json` edits without a restart, and shows the HTTP status and URL when reconnecting fails

> `claude plugin install <name>@<marketplace>` now auto-refreshes the marketplace and retries before reporting a plugin as not found

> `/plugin` installed-plugin details now show hook event names and MCP server names cleanly

> `/context` now shows the providing plugin's name for plugin-sourced skills

> Remote MCP server reconnect retry on transient failures is now enabled for all users

> Remote Control, `/schedule`, claude.ai MCP connectors, and notification preferences are now disabled when `ANTHROPIC_API_KEY` / `apiKeyHelper` / `ANTHROPIC_AUTH_TOKEN` is set, even if a Claude.ai login also exists. Unset the API key to use these features

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.139
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-11-fixed-skill-name-permission-rules-the-wildcard-form-now-works-as-a-prefix-match|Fixed Skill(name ) permission rules]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-11-added-hook-args-string-field-exec-form-that-spawns-the-command-directly-without|Added hook args: string field (exec form) that spawns the command directly…]] · Developer Workflow
- [[Changes/Claude Code/2026-05-11-context-all-per-skill-token-estimates-now-account-for-the-model-s-tokenizer-and|/context all per-skill token estimates now account for the model's tokenizer…]] · Context Window
- [[Changes/Claude Code/2026-05-11-added-goal-command-set-a-completion-condition-and-claude-keeps-working-across-tu|Added /goal command]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-11-compaction-prompt-now-asks-the-model-to-preserve-sensitive-user-instructions|Compaction prompt now asks the model to preserve sensitive user instructions]] · Model Support
- [[Changes/Claude Code/2026-05-11-vscode-press-cmd-ctrl-shift-t-to-reopen-the-most-recently-closed-session-tab-con|VSCode Press Cmd/Ctrl+Shift+T to reopen the most recently closed session tab…]] · Editor Experience
- [[Changes/Claude Code/2026-05-11-added-scroll-speed-command-to-tune-mouse-wheel-scroll-speed-with-a-live-preview|Added /scroll-speed command to tune mouse wheel scroll speed with a live preview]] · Reliability and Performance
- [[Changes/Claude Code/2026-05-11-2-agent-mode-changes-in-v2-1-139|2 Agent Mode changes in v2.1.139]] · Agent Mode
- [[Changes/Claude Code/2026-05-11-added-transcript-view-navigation-for-keyboard-shortcuts-to-jump-between-user-pro|Added transcript view navigation]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-08 · Claude Code · [[Changes/Claude Code/2026-05-08-changed-plugin-marketplace-removal-key-to-d-matching-delete-elsewhere-instead-of|Changed plugin marketplace removal key to d (matching delete elsewhere) instead…]]
- Later: 2026-05-11 · Cursor · [[Changes/Cursor/2026-05-11-get-started-by-installing-the-integration-in-the-cursor-dashboard-learn-more-in|Get started by installing the integration in the Cursor dashboard]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-11-45cd62&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-11-8-apps-and-integrations-changes-in-v2-1-139.md%0ACard%20ID%3A%20claude-code-2026-05-11-45cd62%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.139%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->