---
card_id: claude-code-2026-02-28-083bf6
date: '2026-02-28'
description: 'Claude Code · 2026-02-28 · Safety and Privacy: Fixed listener leak in
  interactive permission handler during auto-approvals'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1049
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: fix
machine_hash: c3a914a7567b660add71b4c6bbe371b1e7327f9fe341c178b697b19ad0f90731
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-02-28-083bf6
  comparison: ''
  date: '2026-02-28'
  description: 'Claude Code — v2.1.63: Fixed listener leak in interactive permission
    handler during auto-approvals'
  evidence:
  - quote: Fixed listener leak in interactive permission handler during auto-approvals
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.63
  extractor_version: fallback-v5
  impact: incremental
  kind: fix
  product: claude-code
  product_name: Claude Code
  slug: fixed-listener-leak-in-interactive-permission-handler-during-auto-approvals
  source_release: claude-code-2026-02-28-v2-1-63-github-291579549-8767ab9c
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Fixed listener leak in interactive permission handler during auto-approvals
  type: change
related_changes:
- '[[Changes/Cursor/2026-02-18-7-safety-and-privacy-changes-in-cli-improvements-and-mermaid-ascii|7
  Safety and Privacy changes in CLI Improvements and Mermaid ASCII…]]'
- '[[Changes/Claude Code/2026-02-19-3-safety-and-privacy-changes-in-v2-1-49|3 Safety
  and Privacy changes in v2.1.49]]'
- '[[Changes/Claude Code/2026-02-24-3-safety-and-privacy-changes-in-v2-1-51|3 Safety
  and Privacy changes in v2.1.51]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-28-v2-1-63-github-291579549-8767ab9c|claude-code-2026-02-28-v2-1-63-github-291579549-8767ab9c]]'
source_type: github_releases
theme: safety-privacy
title: Fixed listener leak in interactive permission handler during auto-approvals
type: change
---

<!-- chronolog:begin region="header" -->
# Fixed listener leak in interactive permission handler during auto-approvals

**Claude Code** · 2026-02-28 · [[Themes/safety-privacy|Safety and Privacy]] · Fix · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.63) · from [[Releases/Claude Code/claude-code-2026-02-28-v2-1-63-github-291579549-8767ab9c|v2.1.63]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed listener leak in interactive permission handler during auto-approvals
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.63
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-02-28-added-manual-url-paste-fallback-during-mcp-oauth-authentication-if-the-automatic|Added manual URL paste fallback during MCP OAuth authentication]] · Account and Access
- [[Changes/Claude Code/2026-02-28-project-configs-auto-memory-now-shared-across-git-worktrees-of-the-same-reposito|Project configs & auto memory now shared across git worktrees of the same repository]] · Memory and Personalization
- [[Changes/Claude Code/2026-02-28-improved-model-command-to-show-the-currently-active-model-in-the-slash-command-m|Improved /model command to show the currently active model in the slash command menu]] · Developer Workflow
- [[Changes/Claude Code/2026-02-28-added-always-copy-full-response-option-to-the-copy-picker-when-selected-future-c|Added "Always copy full response" option to the /copy picker]] · Interface Experience
- [[Changes/Claude Code/2026-02-28-added-http-hooks-which-can-post-json-to-a-url-and-receive-json-instead-of-runnin|Added HTTP hooks, which can POST JSON to a URL and receive JSON instead of running…]] · Agent Mode
- [[Changes/Claude Code/2026-02-28-added-enable-claudeai-mcp-servers-false-env-var-to-opt-out-from-making-claude-ai|Added ENABLE_CLAUDEAI_MCP_SERVERS=false env var to opt out from making claude.ai…]] · Apps and Integrations
- [[Changes/Claude Code/2026-02-28-improved-memory-usage-in-long-sessions-with-subagents-by-stripping-heavy-progres|Improved memory usage in long sessions with subagents by stripping heavy progress…]] · Reliability and Performance
- [[Changes/Claude Code/2026-02-28-added-simplify-and-batch-bundled-slash-commands|Added /simplify and /batch bundled slash commands]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-02-24 · Claude Code · [[Changes/Claude Code/2026-02-24-3-safety-and-privacy-changes-in-v2-1-51|3 Safety and Privacy changes in v2.1.51]]
- Later: 2026-03-03 · Cursor · [[Changes/Cursor/2026-03-03-fixed-team-permission-and-access-control-inconsistencies-across-organization-set|Fixed team permission and access control inconsistencies across organization setups]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-02-28-083bf6&body=Card%3A%20Changes%2FClaude%20Code%2F2026-02-28-fixed-listener-leak-in-interactive-permission-handler-during-auto-approvals.md%0ACard%20ID%3A%20claude-code-2026-02-28-083bf6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.63%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->