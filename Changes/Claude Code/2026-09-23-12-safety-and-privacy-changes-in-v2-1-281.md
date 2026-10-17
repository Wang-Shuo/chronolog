---
card_id: claude-code-2026-09-23-e456b4
date: '2026-09-23'
description: 'Claude Code · 2026-09-23 · Safety and Privacy: 12 changes in v2.1.281
  — Added an auto mode recommendation to `/insights` that estimates how many permission…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1256
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5fa12ed2386faa75803484ecc7b951fdfd3e7a76d18eb11522a5f6efca03d718
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-23-e456b4
  comparison: ''
  date: '2026-09-23'
  description: 'Claude Code — v2.1.281: 12 Safety and Privacy changes'
  evidence:
  - quote: Added an auto mode recommendation to `/insights` that estimates how many
      permission prompts auto mode could have handled in your recent sessions
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Fixed a session resumed after a restart during a pending permission prompt
      sending a different history than before, which broke the prompt cache from that
      point
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Fixed permission dialogs and attachment checks reading a path under macOS's
      `/.vol`, `/.nofollow` or `/.resolve` (which can reach a network mount) before
      approval
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Fixed a permission rule containing a NUL byte being expanded into a wildcard
      match; such a rule now matches nothing
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Fixed `claude --bg` starting a background session, and running its project
      hooks, in a directory that had not passed the workspace trust prompt; it now
      asks for trust first, or exits when not run interactively
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Fixed remote sessions staying on "needs approval" with a stale prompt after
      a permission prompt and a sandbox network-access prompt overlapped and both
      were answered
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: Fixed pressing Shift+Tab twice quickly landing on the wrong permission
      mode
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Windows: Fixed Bash commands that write to `$TMPDIR/…` failing with "Permission
      denied"'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Improved auto mode after resuming a session in a new process: the permission
      classifier can now reuse its earlier prompt cache instead of rewriting it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Improved sandbox guidance on macOS: when a local dev server can''t bind
      a port, Claude now points to `sandbox.network.allowLocalBinding`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: 'Improved `/help` and `/sandbox`: ←/→ and Tab switch tabs from inside a
      tab''s list, and ↓ on an empty Custom commands tab in `/help` no longer leaves
      the keys stuck until Esc'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  - quote: '[Claude Code on the web] Improved the file card shown when a cloud session
      can''t open a file: it now says whether the file no longer exists or the session''s
      permission settings block reading it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 12-safety-and-privacy-changes-in-v2-1-281
  source_release: claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95
  source_type: github_releases
  theme: safety-privacy
  title: 12 Safety and Privacy changes in v2.1.281
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-18-4-safety-and-privacy-changes-in-v2-1-277|4 Safety
  and Privacy changes in v2.1.277]]'
- '[[Changes/ChatGPT/2026-09-21-privacy-center-is-rolling-out-to-signed-in-chatgpt-free-go-plus-and-pro-users-it-0d2f36|Privacy
  Center in ChatGPT]]'
- '[[Changes/Claude Code/2026-09-22-2-safety-and-privacy-changes-in-v2-1-280|2 Safety
  and Privacy changes in v2.1.280]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95|claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95]]'
source_type: github_releases
theme: safety-privacy
title: 12 Safety and Privacy changes in v2.1.281
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Safety and Privacy changes in v2.1.281

**Claude Code** · 2026-09-23 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.281) · from [[Releases/Claude Code/claude-code-2026-09-23-v2-1-281-github-394877414-9173ae95|v2.1.281]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added an auto mode recommendation to `/insights` that estimates how many permission prompts auto mode could have handled in your recent sessions

> Fixed a session resumed after a restart during a pending permission prompt sending a different history than before, which broke the prompt cache from that point

> Fixed permission dialogs and attachment checks reading a path under macOS's `/.vol`, `/.nofollow` or `/.resolve` (which can reach a network mount) before approval

> Fixed a permission rule containing a NUL byte being expanded into a wildcard match; such a rule now matches nothing

> Fixed `claude --bg` starting a background session, and running its project hooks, in a directory that had not passed the workspace trust prompt; it now asks for trust first, or exits when not run interactively

> Fixed remote sessions staying on "needs approval" with a stale prompt after a permission prompt and a sandbox network-access prompt overlapped and both were answered

> Fixed pressing Shift+Tab twice quickly landing on the wrong permission mode

> Windows: Fixed Bash commands that write to `$TMPDIR/…` failing with "Permission denied"

> Improved auto mode after resuming a session in a new process: the permission classifier can now reuse its earlier prompt cache instead of rewriting it

> Improved sandbox guidance on macOS: when a local dev server can't bind a port, Claude now points to `sandbox.network.allowLocalBinding`

> Improved `/help` and `/sandbox`: ←/→ and Tab switch tabs from inside a tab's list, and ↓ on an empty Custom commands tab in `/help` no longer leaves the keys stuck until Esc

> [Claude Code on the web] Improved the file card shown when a cloud session can't open a file: it now says whether the file no longer exists or the session's permission settings block reading it

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.281
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-23-improved-interactive-startup-time-git-reads-startup-telemetry-and-the-bedrock-ve|Improved interactive startup time]] · Model Support
- [[Changes/Claude Code/2026-09-23-2-account-and-access-changes-in-v2-1-281|2 Account and Access changes in v2.1.281]] · Account and Access
- [[Changes/Claude Code/2026-09-23-claude-tag-changed-the-routine-list-claude-gives-when-asked-in-a-slack-thread-to|Claude Tag Changed the routine list Claude gives when asked in a Slack thread…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-09-23-7-developer-workflow-changes-in-v2-1-281|7 Developer Workflow changes in v2.1.281]] · Developer Workflow
- [[Changes/Claude Code/2026-09-23-2-mobile-and-desktop-changes-in-v2-1-281|2 Mobile and Desktop changes in v2.1.281]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-23-4-interface-experience-changes-in-v2-1-281|4 Interface Experience changes in v2.1.281]] · Interface Experience
- [[Changes/Claude Code/2026-09-23-9-agent-mode-changes-in-v2-1-281|9 Agent Mode changes in v2.1.281]] · Agent Mode
- [[Changes/Claude Code/2026-09-23-improved-deep-research-reliability-on-long-research-briefs-by-removing-unused-re|Improved /deep-research reliability on long research briefs by removing unused…]] · Search and Browsing
- [[Changes/Claude Code/2026-09-23-18-apps-and-integrations-changes-in-v2-1-281|18 Apps and Integrations changes in v2.1.281]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-23-improved-screen-reader-output-in-mcp-a-disabled-server-is-read-as-off-instead-of|Improved screen-reader output in /mcp]] · Accessibility and Localization
- [[Changes/Claude Code/2026-09-23-13-other-changes-in-v2-1-281|13 other changes in v2.1.281]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-2-safety-and-privacy-changes-in-v2-1-280|2 Safety and Privacy changes in v2.1.280]]
- Later: 2026-09-23 · Cursor · [[Changes/Cursor/2026-09-23-2-safety-and-privacy-changes-in-rollouts-and-security-review|2 Safety and Privacy changes in Rollouts and Security Review]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-23-e456b4&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-23-12-safety-and-privacy-changes-in-v2-1-281.md%0ACard%20ID%3A%20claude-code-2026-09-23-e456b4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.281%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->