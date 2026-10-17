---
card_id: claude-code-2026-10-08-0a83bd
date: '2026-10-08'
description: 'Claude Code · 2026-10-08 · Agent Mode: 3 changes in v2.1.295 — Changed
  subagents to preload at most 32 skills from the `skills` field, each once; a subagent…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1190
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8858b1fd49be4ed68a206b71a3224deb0dcd762eaeefc8378c38c565e30f08f6
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-08-0a83bd
  comparison: ''
  date: '2026-10-08'
  description: 'Claude Code — v2.1.295: 3 Agent Mode changes'
  evidence:
  - quote: Changed subagents to preload at most 32 skills from the `skills` field,
      each once; a subagent with the Skill tool can still invoke the rest
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: 'Self-hosted runner: Changed the runner to stop passing `CCR_AUTO_MODE_ALLOW`,
      `CCR_AUTO_MODE_ENVIRONMENT` and `CCR_AUTO_MODE_SOFT_DENY` into a session''s
      environment'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  - quote: '[Cloud sessions] Improved the setup script box in the cloud environment
      form: it starts taller, grows with your script, and can be resized by dragging'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-agent-mode-changes-in-v2-1-295
  source_release: claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510
  source_type: github_releases
  theme: agent-mode
  title: 3 Agent Mode changes in v2.1.295
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-06-3-agent-mode-changes-in-v2-1-292|3 Agent Mode
  changes in v2.1.292]]'
- '[[Changes/Cursor/2026-10-06-remote-control-doesn-t-move-your-agents-anywhere-it-keeps-running-on-your-comput|Agents
  keep running on your computer]]'
- '[[Changes/Claude Code/2026-10-07-2-agent-mode-changes-in-v2-1-293|2 Agent Mode
  changes in v2.1.293]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510|claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510]]'
source_type: github_releases
theme: agent-mode
title: 3 Agent Mode changes in v2.1.295
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Agent Mode changes in v2.1.295

**Claude Code** · 2026-10-08 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.295) · from [[Releases/Claude Code/claude-code-2026-10-08-v2-1-295-github-407134589-d5c87510|v2.1.295]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changed subagents to preload at most 32 skills from the `skills` field, each once; a subagent with the Skill tool can still invoke the rest

> Self-hosted runner: Changed the runner to stop passing `CCR_AUTO_MODE_ALLOW`, `CCR_AUTO_MODE_ENVIRONMENT` and `CCR_AUTO_MODE_SOFT_DENY` into a session's environment

> [Cloud sessions] Improved the setup script box in the cloud environment form: it starts taller, grows with your script, and can be resized by dragging

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.295
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-08-added-a-line-on-stderr-when-it-is-a-terminal-that-says-what-a-claude-p-run-is-wa|Added a line on stderr, when it is a terminal, that says what a claude -p run…]] · Developer Workflow
- [[Changes/Claude Code/2026-10-08-improved-token-counts-behind-a-claude-apps-gateway-on-amazon-bedrock-which-conte|Improved token counts behind a Claude apps gateway on Amazon Bedrock…]] · Context Window
- [[Changes/Claude Code/2026-10-08-changed-ctrl-c-at-the-idle-prompt-of-an-attached-background-session-to-leave-a-p|Changed Ctrl+C at the idle prompt of an attached background session to leave…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-10-08-14-apps-and-integrations-changes-in-v2-1-295|14 Apps and Integrations changes in v2.1.295]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-08-added-support-for-forceloginmethod-gateway-and-forcelogingatewayurl-in-your-own|Added support for forceLoginMethod: "gateway" and forceLoginGatewayUrl…]] · Account and Access
- [[Changes/Claude Code/2026-10-08-changed-tab-stops-to-count-from-where-a-text-starts-instead-of-from-the-screen-s|Changed tab stops to count from where a text starts instead of from the screen's left edge]] · Editor Experience
- [[Changes/Claude Code/2026-10-08-2-model-support-changes-in-v2-1-295|2 Model Support changes in v2.1.295]] · Model Support
- [[Changes/Claude Code/2026-10-08-2-interface-experience-changes-in-v2-1-295|2 Interface Experience changes in v2.1.295]] · Interface Experience
- [[Changes/Claude Code/2026-10-08-2-mobile-and-desktop-changes-in-v2-1-295|2 Mobile and Desktop changes in v2.1.295]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-08-5-safety-and-privacy-changes-in-v2-1-295|5 Safety and Privacy changes in v2.1.295]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-08-claude-tag-changed-claude-s-notice-that-a-channel-shared-across-enterprise-grid|Claude Tag Changed Claude's notice that a channel shared across Enterprise Grid…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-08-15-other-changes-in-v2-1-295|15 other changes in v2.1.295]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-07 · Claude Code · [[Changes/Claude Code/2026-10-07-2-agent-mode-changes-in-v2-1-293|2 Agent Mode changes in v2.1.293]]
- Later: 2026-10-09 · Claude Code · [[Changes/Claude Code/2026-10-09-3-agent-mode-changes-in-v2-1-296|3 Agent Mode changes in v2.1.296]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-08-0a83bd&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-08-3-agent-mode-changes-in-v2-1-295.md%0ACard%20ID%3A%20claude-code-2026-10-08-0a83bd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.295%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->