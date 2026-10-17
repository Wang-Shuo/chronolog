---
card_id: claude-code-2026-07-22-3c6fbf
date: '2026-07-22'
description: 'Claude Code · 2026-07-22 · Safety and Privacy: 3 changes in v2.1.218
  — Fixed agent frontmatter hooks running from untrusted folders: hooks now require
  the…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1193
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 327ab2cc6967654437ec06a6e0e0c3e06cacf58eb92534ffb21f1a5eb229b2dd
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-22-3c6fbf
  comparison: ''
  date: '2026-07-22'
  description: 'Claude Code — v2.1.218: 3 Safety and Privacy changes'
  evidence:
  - quote: 'Fixed agent frontmatter hooks running from untrusted folders: hooks now
      require the agent file''s own folder to have accepted workspace trust'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.218
  - quote: 'Improved auto mode: the dangerous-rm, background-`&`, and suspicious-Windows-path
      checks no longer open permission dialogs; the auto-mode classifier adjudicates
      them instead'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.218
  - quote: Improved sandbox command restrictions for IDE interactions
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.218
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-safety-and-privacy-changes-in-v2-1-218
  source_release: claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v2.1.218
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-18-9-safety-and-privacy-changes-in-v2-1-214|9 Safety
  and Privacy changes in v2.1.214]]'
- '[[Changes/Claude Code/2026-07-20-5-safety-and-privacy-changes-in-v2-1-216|5 Safety
  and Privacy changes in v2.1.216]]'
- '[[Changes/Claude Code/2026-07-21-fixed-remote-control-sessions-not-showing-a-pending-permission-prompt-or-dialog|Fixed
  Remote Control sessions not showing a pending permission prompt or dialog…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4|claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v2.1.218
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v2.1.218

**Claude Code** · 2026-07-22 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.218) · from [[Releases/Claude Code/claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4|v2.1.218]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed agent frontmatter hooks running from untrusted folders: hooks now require the agent file's own folder to have accepted workspace trust

> Improved auto mode: the dangerous-rm, background-`&`, and suspicious-Windows-path checks no longer open permission dialogs; the auto-mode classifier adjudicates them instead

> Improved sandbox command restrictions for IDE interactions

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.218
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-22-changed-plan-mode-with-auto-to-no-longer-prompt-for-bash-commands-the-static-ana|Changed plan mode with auto to no longer prompt for Bash commands the static…]] · Agent Mode
- [[Changes/Claude Code/2026-07-22-changed-server-managed-settings-so-benign-feature-and-cost-toggles-no-longer-tri|Changed server-managed settings so benign feature and cost toggles no longer trigger…]] · Pricing Model
- [[Changes/Claude Code/2026-07-22-added-an-announcement-when-fast-mode-changes-as-a-result-of-switching-models-via|Added an announcement when fast mode changes as a result of switching models…]] · Model Support
- [[Changes/Claude Code/2026-07-22-changed-deep-research-to-start-only-when-invoked-manually-claude-no-longer-launc|Changed /deep-research to start only when invoked manually]] · Search and Browsing
- [[Changes/Claude Code/2026-07-22-3-apps-and-integrations-changes-in-v2-1-218|3 Apps and Integrations changes in v2.1.218]] · Apps and Integrations
- [[Changes/Claude Code/2026-07-22-added-screen-reader-announcements-of-deleted-text-for-word-and-line-deletions-op|Added screen-reader announcements of deleted text for word and line deletions…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-07-22-changed-code-review-to-run-as-a-background-subagent-so-review-work-no-longer-fil|Changed /code-review to run as a background subagent, so review work no longer…]] · Developer Workflow
- [[Changes/Claude Code/2026-07-22-changed-skills-with-context-fork-to-run-in-the-background-by-default-opt-out-per|Changed skills with context: fork to run in the background by default]] · Context Window
- [[Changes/Claude Code/2026-07-22-improved-trust-dialogs-to-name-the-repository-root-the-grant-covers|Improved trust dialogs to name the repository root the grant covers]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-21 · Claude Code · [[Changes/Claude Code/2026-07-21-fixed-remote-control-sessions-not-showing-a-pending-permission-prompt-or-dialog|Fixed Remote Control sessions not showing a pending permission prompt or dialog…]]
- Later: 2026-07-23 · ChatGPT · [[Changes/ChatGPT/2026-07-23-health-is-built-with-layered-privacy-and-security-safeguards-connected-medical-r|Health is built with layered privacy and security safeguards]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-22-3c6fbf&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-22-3-safety-and-privacy-changes-in-v2-1-218.md%0ACard%20ID%3A%20claude-code-2026-07-22-3c6fbf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.218%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->