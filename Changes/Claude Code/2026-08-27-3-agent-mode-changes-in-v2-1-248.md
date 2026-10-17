---
card_id: claude-code-2026-08-27-713131
date: '2026-08-27'
description: 'Claude Code · 2026-08-27 · Agent Mode: 3 changes in v2.1.248 — Added
  `experimental.cacheTtl` (`"5m"` or `"1h"`) to agent frontmatter: a per-agent prompt
  cache…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1148
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c4fb08a236cfc295515ff2ac0414808a359dacb67e0b993b4449048b54f95d05
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-27-713131
  comparison: ''
  date: '2026-08-27'
  description: 'Claude Code — v2.1.248: 3 Agent Mode changes'
  evidence:
  - quote: 'Added `experimental.cacheTtl` (`"5m"` or `"1h"`) to agent frontmatter:
      a per-agent prompt cache TTL used when no subagent TTL setting is configured'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.248
  - quote: Changed shift+enter in the agent view dispatch input to insert a newline
      (matching the prompt); ctrl+enter now dispatches and attaches
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.248
  - quote: 'Changed `SendMessage` from a subagent to another session: the result now
      notes that any reply is delivered to the parent session''s conversation, not
      to the subagent'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.248
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-agent-mode-changes-in-v2-1-248
  source_release: claude-code-2026-08-27-v2-1-248-github-378106990-677106e3
  source_type: github_releases
  theme: agent-mode
  title: 3 Agent Mode changes in v2.1.248
  type: change
related_changes:
- '[[Changes/Cursor/2026-08-19-goal|/goal]]'
- '[[Changes/Claude Code/2026-08-21-2-agent-mode-changes-in-v2-1-239|2 Agent Mode
  changes in v2.1.239]]'
- '[[Changes/Claude Code/2026-08-25-improved-subagent-results-a-subagent-that-stops-at-its-maxturns-limit-now-return|Improved
  subagent results]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-27-v2-1-248-github-378106990-677106e3|claude-code-2026-08-27-v2-1-248-github-378106990-677106e3]]'
source_type: github_releases
theme: agent-mode
title: 3 Agent Mode changes in v2.1.248
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Agent Mode changes in v2.1.248

**Claude Code** · 2026-08-27 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.248) · from [[Releases/Claude Code/claude-code-2026-08-27-v2-1-248-github-378106990-677106e3|v2.1.248]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `experimental.cacheTtl` (`"5m"` or `"1h"`) to agent frontmatter: a per-agent prompt cache TTL used when no subagent TTL setting is configured

> Changed shift+enter in the agent view dispatch input to insert a newline (matching the prompt); ctrl+enter now dispatches and attaches

> Changed `SendMessage` from a subagent to another session: the result now notes that any reply is delivered to the parent session's conversation, not to the subagent

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.248
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-27-changed-anthropic-telemetry-export-failures-to-log-at-debug-level-as-anthropic-t|Changed Anthropic telemetry export failures to log at debug level…]] · Developer Workflow
- [[Changes/Claude Code/2026-08-27-added-usage-credits-for-enterprise-organizations-billed-through-aws-marketplace|Added /usage-credits for Enterprise organizations billed through AWS Marketplace…]] · Pricing Model
- [[Changes/Claude Code/2026-08-27-2-interface-experience-changes-in-v2-1-248|2 Interface Experience changes in v2.1.248]] · Interface Experience
- [[Changes/Claude Code/2026-08-27-4-safety-and-privacy-changes-in-v2-1-248|4 Safety and Privacy changes in v2.1.248]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-27-improved-the-workflow-tool-s-prompt-footprint-its-description-is-now-about-1k-to|Improved the Workflow tool's prompt footprint]] · Context Window
- [[Changes/Claude Code/2026-08-27-improved-managed-settings-client-side-timeout-mcp-startup-mode-and-stream-watchd|Improved managed settings]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-27-changed-loop-self-paced-dynamic-mode-and-the-no-prompt-autonomous-default-are-no|Changed /loop: self-paced dynamic mode and the no-prompt autonomous default…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-08-27-7-other-changes-in-v2-1-248|7 other changes in v2.1.248]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-25 · Claude Code · [[Changes/Claude Code/2026-08-25-improved-subagent-results-a-subagent-that-stops-at-its-maxturns-limit-now-return|Improved subagent results]]
- Later: 2026-08-27 · Cursor · [[Changes/Cursor/2026-08-27-cloud-agents-no-longer-require-a-connected-github-or-other-third-party-scm-provi|Cloud Agents no longer require a connected GitHub or other third-party SCM provider…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-27-713131&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-27-3-agent-mode-changes-in-v2-1-248.md%0ACard%20ID%3A%20claude-code-2026-08-27-713131%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.248%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->