---
card_id: claude-code-2026-09-18-d01496
date: '2026-09-18'
description: 'Claude Code · 2026-09-18 · Agent Mode: 4 changes in v2.1.277 — Added
  AGENTS.md support: in a project with no CLAUDE.md, Claude Code reads AGENTS.md instead…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1170
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e2e20ed44f8c005d67fc43e258dada80129817157623146e9e887540694b5bbb
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-18-d01496
  comparison: ''
  date: '2026-09-18'
  description: 'Claude Code — v2.1.277: 4 Agent Mode changes'
  evidence:
  - quote: 'Added AGENTS.md support: in a project with no CLAUDE.md, Claude Code reads
      AGENTS.md instead; change it under "Project instructions" in `/config` (not
      yet on Bedrock, Vertex or Foundry)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
  - quote: Changed subagent results to reach the main agent under a header marking
      them as subagent output, with the result indented, so text in a subagent's result
      cannot pass as the session's own instructions
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
  - quote: Changed workflow scripts' computed `agent()` prompts on Bedrock, Vertex
      and Foundry to reach the subagent framed as script-authored text, so the safety
      classifier does not read them as the user
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
  - quote: '[VSCode] Added background shells and other running tasks to the agent
      map, each with a Stop, and a typed `/tasks` that opens it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-agent-mode-changes-in-v2-1-277
  source_release: claude-code-2026-09-18-v2-1-277-github-391616593-06a20f36
  source_type: github_releases
  theme: agent-mode
  title: 4 Agent Mode changes in v2.1.277
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-14-7-agent-mode-changes-in-v2-1-271|7 Agent Mode
  changes in v2.1.271]]'
- '[[Changes/Claude Code/2026-09-15-changed-auto-mode-on-bedrock-vertex-and-foundry-to-use-the-local-classifier-by-d|Changed
  auto mode on Bedrock, Vertex and Foundry to use the local classifier…]]'
- '[[Changes/Claude Code/2026-09-17-vscode-improved-the-agent-map-the-pill-counts-running-agents-and-turns-red-after|VSCode
  Improved the agent map]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-18-v2-1-277-github-391616593-06a20f36|claude-code-2026-09-18-v2-1-277-github-391616593-06a20f36]]'
source_type: github_releases
theme: agent-mode
title: 4 Agent Mode changes in v2.1.277
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in v2.1.277

**Claude Code** · 2026-09-18 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.277) · from [[Releases/Claude Code/claude-code-2026-09-18-v2-1-277-github-391616593-06a20f36|v2.1.277]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added AGENTS.md support: in a project with no CLAUDE.md, Claude Code reads AGENTS.md instead; change it under "Project instructions" in `/config` (not yet on Bedrock, Vertex or Foundry)

> Changed subagent results to reach the main agent under a header marking them as subagent output, with the result indented, so text in a subagent's result cannot pass as the session's own instructions

> Changed workflow scripts' computed `agent()` prompts on Bedrock, Vertex and Foundry to reach the subagent framed as script-authored text, so the safety classifier does not read them as the user

> [VSCode] Added background shells and other running tasks to the agent map, each with a Stop, and a typed `/tasks` that opens it

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
- [[Changes/Claude Code/2026-09-18-6-apps-and-integrations-changes-in-v2-1-277|6 Apps and Integrations changes in v2.1.277]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-18-claude-code-on-the-web-changed-the-admin-claude-code-setting-labeled-web-to-clou|Claude Code on the web Changed the admin Claude Code setting labeled…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-18-changed-fable-to-always-appear-in-model-on-the-anthropic-api-it-is-greyed-out-on|Changed Fable to always appear in /model on the Anthropic API]] · Model Support
- [[Changes/Claude Code/2026-09-18-7-other-changes-in-v2-1-277|7 other changes in v2.1.277]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-vscode-improved-the-agent-map-the-pill-counts-running-agents-and-turns-red-after|VSCode Improved the agent map]]
- Later: 2026-09-19 · Claude Code · [[Changes/Claude Code/2026-09-19-added-an-auto-mode-server-row-to-status-showing-whether-this-session-s-auto-mode|Added an Auto mode server row to /status showing whether this session's auto…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-18-d01496&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-18-4-agent-mode-changes-in-v2-1-277.md%0ACard%20ID%3A%20claude-code-2026-09-18-d01496%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.277%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->