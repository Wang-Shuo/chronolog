---
card_id: claude-code-2026-08-14-22f6f8
date: '2026-08-14'
description: 'Claude Code · 2026-08-14 · Safety and Privacy: 3 changes in v2.1.233
  — Fixed cloud sessions occasionally being marked as lost when the environment shut
  down…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1216
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 61729ddd9f9b36d3c1bae688f758477629e59fbb1798805209f5b78bace0d75f
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-14-22f6f8
  comparison: ''
  date: '2026-08-14'
  description: 'Claude Code — v2.1.233: 3 Safety and Privacy changes'
  evidence:
  - quote: Fixed cloud sessions occasionally being marked as lost when the environment
      shut down while Claude was waiting on a permission prompt
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.233
  - quote: Fixed Notification hooks not firing for permission prompts when running
      under Claude Desktop or VS Code
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.233
  - quote: Reverted the 2.1.232 Bash permission changes for Cygwin-style symlinks
      on Windows and for input redirections (`< file`); a narrower version will return
      in a later release
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.233
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-safety-and-privacy-changes-in-v2-1-233
  source_release: claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v2.1.233
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-08-2-safety-and-privacy-changes-in-v2-1-225|2 Safety
  and Privacy changes in v2.1.225]]'
- '[[Changes/Claude Code/2026-08-12-improved-sandbox-ipv6-literals-in-network-domain-lists-are-now-bracketed-1-443-a|Improved
  sandbox: IPv6 literals in network domain lists are now bracketed…]]'
- '[[Changes/Claude Code/2026-08-13-9-safety-and-privacy-changes-in-v2-1-232|9 Safety
  and Privacy changes in v2.1.232]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9|claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v2.1.233
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v2.1.233

**Claude Code** · 2026-08-14 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.233) · from [[Releases/Claude Code/claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9|v2.1.233]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed cloud sessions occasionally being marked as lost when the environment shut down while Claude was waiting on a permission prompt

> Fixed Notification hooks not firing for permission prompts when running under Claude Desktop or VS Code

> Reverted the 2.1.232 Bash permission changes for Cygwin-style symlinks on Windows and for input redirections (`< file`); a narrower version will return in a later release

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.233
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-14-improved-screen-reader-mode-the-effort-selector-renders-as-a-numbered-list-with|Improved screen reader mode]] · Accessibility and Localization
- [[Changes/Claude Code/2026-08-14-changed-the-github-app-setup-tip-to-no-longer-appear-in-repositories-whose-origi|Changed the GitHub app setup tip to no longer appear in repositories whose origin…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-08-14-improved-apps-gateway-error-forwarding-400-413-errors-from-vertex-foundry-and-cl|Improved apps gateway error forwarding]] · Context Window
- [[Changes/Claude Code/2026-08-14-improved-claude-self-hosted-runner-session-start-time-the-session-branch-is-now|Improved claude self-hosted-runner session start time]] · Agent Mode
- [[Changes/Claude Code/2026-08-14-2-model-support-changes-in-v2-1-233|2 Model Support changes in v2.1.233]] · Model Support
- [[Changes/Claude Code/2026-08-14-added-opt-in-memory-cgroup-support-for-bash-tool-commands-on-linux-claude-code-t|Added opt-in memory cgroup support for Bash tool commands on Linux…]] · Memory and Personalization
- [[Changes/Claude Code/2026-08-14-added-gitlab-merge-request-url-support-to-the-worktree-flag-and-the-claude-agent|Added GitLab merge request URL support to the --worktree flag…]] · Developer Workflow
- [[Changes/Claude Code/2026-08-14-2-apps-and-integrations-changes-in-v2-1-233|2 Apps and Integrations changes in v2.1.233]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-13 · Claude Code · [[Changes/Claude Code/2026-08-13-9-safety-and-privacy-changes-in-v2-1-232|9 Safety and Privacy changes in v2.1.232]]
- Later: 2026-08-17 · Claude Code · [[Changes/Claude Code/2026-08-17-8-safety-and-privacy-changes-in-v2-1-234|8 Safety and Privacy changes in v2.1.234]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-14-22f6f8&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-14-3-safety-and-privacy-changes-in-v2-1-233.md%0ACard%20ID%3A%20claude-code-2026-08-14-22f6f8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.233%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->