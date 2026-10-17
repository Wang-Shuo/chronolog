---
card_id: claude-code-2026-06-04-336013
date: '2026-06-04'
description: 'Claude Code · 2026-06-04 · Apps and Integrations: 2 changes in v2.1.163
  — Hooks: Stop and SubagentStop hooks can now return…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1169
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d533eb0ef09d1bda9991bb8641fdacb710037feffe90783b2147da8fd8179502
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-04-336013
  comparison: ''
  date: '2026-06-04'
  description: 'Claude Code — v2.1.163: 2 Apps and Integrations changes'
  evidence:
  - quote: 'Hooks: Stop and SubagentStop hooks can now return `hookSpecificOutput.additionalContext`
      to give Claude feedback and keep the turn going without being labeled a hook
      error'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.163
  - quote: stdio MCP servers now receive the same `CLAUDE_CODE_SESSION_ID` as hooks/Bash
      on `--resume`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.163
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-apps-and-integrations-changes-in-v2-1-163
  source_release: claude-code-2026-06-04-v2-1-163-github-334509318-c6b9f988
  source_type: github_releases
  theme: apps-integrations
  title: 2 Apps and Integrations changes in v2.1.163
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-02-mcp-now-collapses-claude-ai-connectors-you-ve-never-signed-in-to-behind-a-show-u|/mcp
  now collapses claude.ai connectors you''ve never signed in to behind…]]'
- '[[Changes/Claude Code/2026-06-02-removed-the-jetbrains-plugin-install-suggestion-from-startup|Removed
  the JetBrains plugin install suggestion from startup]]'
- '[[Changes/Claude Code/2026-06-03-remote-control-now-shows-as-a-persistent-footer-pill-with-a-link-to-the-session|Remote
  Control now shows as a persistent footer pill (with a link to the session)…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-04-v2-1-163-github-334509318-c6b9f988|claude-code-2026-06-04-v2-1-163-github-334509318-c6b9f988]]'
source_type: github_releases
theme: apps-integrations
title: 2 Apps and Integrations changes in v2.1.163
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Apps and Integrations changes in v2.1.163

**Claude Code** · 2026-06-04 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.163) · from [[Releases/Claude Code/claude-code-2026-06-04-v2-1-163-github-334509318-c6b9f988|v2.1.163]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hooks: Stop and SubagentStop hooks can now return `hookSpecificOutput.additionalContext` to give Claude feedback and keep the turn going without being labeled a hook error

> stdio MCP servers now receive the same `CLAUDE_CODE_SESSION_ID` as hooks/Bash on `--resume`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.163
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-04-the-subscription-switch-suggestion-now-shows-in-the-startup-announcement-slot-in|The subscription-switch suggestion now shows in the startup announcement slot…]] · Pricing Model
- [[Changes/Claude Code/2026-06-04-fixed-org-managed-permission-rules-not-applying-for-the-entire-session-when-the|Fixed org-managed permission rules not applying for the entire session…]] · Safety and Privacy
- [[Changes/Claude Code/2026-06-04-2-agent-mode-changes-in-v2-1-163|2 Agent Mode changes in v2.1.163]] · Agent Mode
- [[Changes/Claude Code/2026-06-04-skills-added-escape-syntax-to-include-a-literal-before-a-digit-in-command-bodies|Skills: added \$ escape syntax to include a literal $ before a digit in command bodies]] · Developer Workflow
- [[Changes/Claude Code/2026-06-04-added-plugin-list-command-to-list-installed-plugins-with-enabled-disabled-filter|Added /plugin list command to list installed plugins…]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-04-2-interface-experience-changes-in-v2-1-163|2 Interface Experience changes in v2.1.163]] · Interface Experience
- [[Changes/Claude Code/2026-06-04-added-requiredminimumversion-and-requiredmaximumversion-managed-settings-claude|Added requiredMinimumVersion and requiredMaximumVersion managed settings]] · Enterprise and Administration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-06-03 · Claude Code · [[Changes/Claude Code/2026-06-03-remote-control-now-shows-as-a-persistent-footer-pill-with-a-link-to-the-session|Remote Control now shows as a persistent footer pill (with a link to the session)…]]
- Later: 2026-06-04 · Cursor · [[Changes/Cursor/2026-06-04-we-ve-shipped-a-batch-of-new-functionality-across-the-typescript-and-python-sdks|We've shipped a batch of new functionality across the TypeScript and Python SDKs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-04-336013&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-04-2-apps-and-integrations-changes-in-v2-1-163.md%0ACard%20ID%3A%20claude-code-2026-06-04-336013%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.163%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->