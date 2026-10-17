---
card_id: cursor-2026-01-22-8c7a09
date: '2026-01-22'
description: 'Cursor · 2026-01-22 · Apps and Integrations: 4 changes in Subagents,
  Skills, and Image Generation — MCP server definitions and tools now live as JSON
  files in…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1036
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 88ba02e726b7dc10c3e6305ad2216c3be4d2afbb25edcdffd6620e7e388ed4bd
product: cursor
product_name: Cursor
record:
  card_id: cursor-2026-01-22-8c7a09
  comparison: ''
  date: '2026-01-22'
  description: 'Cursor — Subagents, Skills, and Image Generation: 4 Apps and Integrations
    changes'
  evidence:
  - quote: MCP server definitions and tools now live as JSON files in .cursor. Agents
      discover and load MCPs only when needed, reducing token usage and keeping the
      context focused.
    source_release: https://cursor.com/changelog/2-4
  - quote: 'Improved capabilities & coverage for hooks: stop hook; modify prompts
      beforeSubmitPrompt ; PreToolUse and PostToolUse hooks.'
    source_release: https://cursor.com/changelog/2-4
  - quote: Added compatibility with Claude Code hooks in CLI.
    source_release: https://cursor.com/changelog/2-4
  - quote: /mcp enable and /mcp disable now only show relevant MCP servers in autocomplete
      in CLI.
    source_release: https://cursor.com/changelog/2-4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cursor
  product_name: Cursor
  slug: 4-apps-and-integrations-changes-in-2-4
  source_release: cursor-2026-01-22-2-4-https-cursor-com-changelog-2-4-a10c8f03
  source_type: cursor_changelog
  theme: apps-integrations
  title: 4 Apps and Integrations changes in 2.4
  type: change
related_changes:
- '[[Changes/Claude Code/2026-01-13-2-apps-and-integrations-changes-in-v2-1-6|2 Apps
  and Integrations changes in v2.1.6]]'
- '[[Changes/Claude Code/2026-01-20-2-apps-and-integrations-changes-in-v2-1-14|2 Apps
  and Integrations changes in v2.1.14]]'
- '[[Changes/Claude Code/2026-01-22-vscode-added-native-plugin-management-support|VSCode
  Added native plugin management support]]'
source_release: '[[Releases/Cursor/cursor-2026-01-22-2-4-https-cursor-com-changelog-2-4-a10c8f03|cursor-2026-01-22-2-4-https-cursor-com-changelog-2-4-a10c8f03]]'
source_type: cursor_changelog
theme: apps-integrations
title: 4 Apps and Integrations changes in 2.4
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in 2.4

**Cursor** · 2026-01-22 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://cursor.com/changelog/2-4) · from [[Releases/Cursor/cursor-2026-01-22-2-4-https-cursor-com-changelog-2-4-a10c8f03|Subagents, Skills, and Image Generation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MCP server definitions and tools now live as JSON files in .cursor. Agents discover and load MCPs only when needed, reducing token usage and keeping the context focused.

> Improved capabilities & coverage for hooks: stop hook; modify prompts beforeSubmitPrompt ; PreToolUse and PostToolUse hooks.

> Added compatibility with Claude Code hooks in CLI.

> /mcp enable and /mcp disable now only show relevant MCP servers in autocomplete in CLI.

Source: https://cursor.com/changelog/2-4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cursor/2026-01-22-2-editor-experience-changes-in-2-4|2 Editor Experience changes in 2.4]] · Editor Experience
- [[Changes/Cursor/2026-01-22-added-team-and-mdm-hooks-support-to-cli-with-more-efficient-execution|Added team and MDM hooks support to CLI with more efficient execution]] · Collaboration
- [[Changes/Cursor/2026-01-22-agents-can-now-read-pdfs-which-you-can-attach-in-chats-as-context|Agents can now read PDFs, which you can attach in chats as context]] · Context Window
- [[Changes/Cursor/2026-01-22-image-generation|Image generation]] · Image Generation
- [[Changes/Cursor/2026-01-22-unified-cli-permissions-with-the-editor-including-run-everything-auto-run-in-san|Unified CLI permissions with the editor, including Run Everything, Auto-Run…]] · Safety and Privacy
- [[Changes/Cursor/2026-01-22-skills|Skills]] · Agent Mode
- [[Changes/Cursor/2026-01-22-browser-can-now-request-local-network-permissions-fixing-authentication-flows-wi|Browser can now request local network permissions, fixing authentication flows…]] · Account and Access
- [[Changes/Cursor/2026-01-22-4-agent-mode-changes-in-2-4|4 Agent Mode changes in 2.4]] · Agent Mode
- [[Changes/Cursor/2026-01-22-windows-notifications-now-have-accept-reject-buttons-like-macos|Windows notifications now have accept/reject buttons like MacOS]] · Mobile and Desktop
- [[Changes/Cursor/2026-01-22-agents-are-solving-increasingly-complex-long-running-tasks-across-your-codebase|Agents are solving increasingly complex, long-running tasks across your codebase]] · Agent Mode
- [[Changes/Cursor/2026-01-22-subagents|Subagents]] · Agent Mode
- [[Changes/Cursor/2026-01-22-2-interface-experience-changes-in-2-4|2 Interface Experience changes in 2.4]] · Interface Experience
- [[Changes/Cursor/2026-01-22-added-max-mode-on-off-to-toggle-max-mode-on-models-that-support-it-in-cli|Added /max-mode on / off to toggle max mode on models that support it in CLI]] · Model Support
- [[Changes/Cursor/2026-01-22-3-developer-workflow-changes-in-2-4|3 Developer Workflow changes in 2.4]] · Developer Workflow
- [[Changes/Cursor/2026-01-22-cursor-blame|Cursor Blame]] · Enterprise and Administration
- [[Changes/Cursor/2026-01-22-clarification-questions-from-the-agent|Clarification questions from the agent]] · Agent Mode
- [[Changes/Cursor/2026-01-22-4-reliability-and-performance-changes-in-2-4|4 Reliability and Performance changes in 2.4]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-01-22 · Claude Code · [[Changes/Claude Code/2026-01-22-vscode-added-native-plugin-management-support|VSCode Added native plugin management support]]
- Later: 2026-01-23 · Claude Code · [[Changes/Claude Code/2026-01-23-2-apps-and-integrations-changes-in-v2-1-19|2 Apps and Integrations changes in v2.1.19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cursor-2026-01-22-8c7a09&body=Card%3A%20Changes%2FCursor%2F2026-01-22-4-apps-and-integrations-changes-in-2-4.md%0ACard%20ID%3A%20cursor-2026-01-22-8c7a09%0ASource%3A%20https%3A%2F%2Fcursor.com%2Fchangelog%2F2-4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->