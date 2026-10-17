---
card_id: claude-code-2026-09-29-708866
date: '2026-09-29'
description: 'Claude Code · 2026-09-29 · Reliability and Performance: Fixed the PowerShell
  tool''s permission check skipping deny and ask rules, and caching that failure for…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1384
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: fix
machine_hash: dad1a1b95795ab95c68ad80e1cf1218d2646b884724cd7eaa0059a39bef35b14
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-29-708866
  comparison: ''
  date: '2026-09-29'
  description: 'Claude Code — v2.1.285: Fixed the PowerShell tool''s permission check
    skipping deny and ask rules, and caching that failure for later checks, when its
    command parser failed to start (for example when the machine was out of memory)'
  evidence:
  - quote: Fixed the PowerShell tool's permission check skipping deny and ask rules,
      and caching that failure for later checks, when its command parser failed to
      start (for example when the machine was out of memory)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  extractor_version: fallback-v5
  impact: incremental
  kind: fix
  product: claude-code
  product_name: Claude Code
  slug: fixed-the-powershell-tool-s-permission-check-skipping-deny-and-ask-rules-and-cac
  source_release: claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc
  source_type: github_releases
  theme: reliability-performance
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Fixed the PowerShell tool's permission check skipping deny and ask rules…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-17-added-a-visible-warning-when-memory-usage-is-critical-with-steps-to-free-memory|Added
  a visible warning when memory usage is critical, with steps to free memory…]]'
- '[[Changes/Cursor/2026-09-23-deploy-tracking|Deploy tracking]]'
- '[[Changes/Claude Code/2026-09-25-2-reliability-and-performance-changes-in-v2-1-283|2
  Reliability and Performance changes in v2.1.283]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc|claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc]]'
source_type: github_releases
theme: reliability-performance
title: Fixed the PowerShell tool's permission check skipping deny and ask rules…
type: change
---

<!-- chronolog:begin region="header" -->
# Fixed the PowerShell tool's permission check skipping deny and ask rules…

**Claude Code** · 2026-09-29 · [[Themes/reliability-performance|Reliability and Performance]] · Fix · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.285) · from [[Releases/Claude Code/claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc|v2.1.285]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed the PowerShell tool's permission check skipping deny and ask rules, and caching that failure for later checks, when its command parser failed to start (for example when the machine was out of memory)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-29-2-context-window-changes-in-v2-1-285|2 Context Window changes in v2.1.285]] · Context Window
- [[Changes/Claude Code/2026-09-29-claude-tag-added-direct-messages-with-claude-for-members-on-an-enterprise-plan-s|Claude Tag Added direct messages with Claude for members on an Enterprise plan…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-09-29-6-mobile-and-desktop-changes-in-v2-1-285|6 Mobile and Desktop changes in v2.1.285]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-29-improved-responsiveness-when-leaving-the-ctrl-o-transcript-view-in-long-sessions|Improved responsiveness when leaving the ctrl+o transcript view in long sessions…]] · Interface Experience
- [[Changes/Claude Code/2026-09-29-3-model-support-changes-in-v2-1-285|3 Model Support changes in v2.1.285]] · Model Support
- [[Changes/Claude Code/2026-09-29-14-apps-and-integrations-changes-in-v2-1-285|14 Apps and Integrations changes in v2.1.285]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-29-changed-team-and-enterprise-sessions-and-sessions-whose-sign-in-plan-claude-code|Changed Team and Enterprise sessions, and sessions whose sign-in plan Claude Code…]] · Account and Access
- [[Changes/Claude Code/2026-09-29-2-editor-experience-changes-in-v2-1-285|2 Editor Experience changes in v2.1.285]] · Editor Experience
- [[Changes/Claude Code/2026-09-29-2-agent-mode-changes-in-v2-1-285|2 Agent Mode changes in v2.1.285]] · Agent Mode
- [[Changes/Claude Code/2026-09-29-9-safety-and-privacy-changes-in-v2-1-285|9 Safety and Privacy changes in v2.1.285]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-29-changed-memory-so-that-auto-memory-can-no-longer-be-turned-on-from-a-background|Changed /memory so that Auto-memory can no longer be turned on from a background…]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-29-3-developer-workflow-changes-in-v2-1-285|3 Developer Workflow changes in v2.1.285]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-09-25 · Claude Code · [[Changes/Claude Code/2026-09-25-2-reliability-and-performance-changes-in-v2-1-283|2 Reliability and Performance changes in v2.1.283]]
- Later: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-2-reliability-and-performance-changes-in-v2-1-287|2 Reliability and Performance changes in v2.1.287]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-29-708866&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-29-fixed-the-powershell-tool-s-permission-check-skipping-deny-and-ask-rules-and-cac.md%0ACard%20ID%3A%20claude-code-2026-09-29-708866%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.285%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->