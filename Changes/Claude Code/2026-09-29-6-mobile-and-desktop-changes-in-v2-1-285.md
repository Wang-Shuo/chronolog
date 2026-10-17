---
card_id: claude-code-2026-09-29-1ea1d6
date: '2026-09-29'
description: 'Claude Code · 2026-09-29 · Mobile and Desktop: 6 changes in v2.1.285
  — Added `claude --desktop` to open the Claude desktop app on the current directory,
  or on…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support 🥳]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1295
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: eaa16784c5f133cf54fc42d318dc97051c516633bf87c074e431f28a794ad1c7
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-29-1ea1d6
  comparison: ''
  date: '2026-09-29'
  description: 'Claude Code — v2.1.285: 6 Mobile and Desktop changes'
  evidence:
  - quote: Added `claude --desktop` to open the Claude desktop app on the current
      directory, or on a session with `--continue` / `--resume <id>`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: 'Improved Remote Control: a `/btw` side question asked of a session hosted
      by an app such as Claude Desktop now sees the turn in progress, not only the
      last finished one'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Changed `/ultrareview` on macOS and Linux to leave symbolic refs out when
      uploading a local checkout; a checkout whose current branch is a symbolic ref
      is now refused with an explanation
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Changed `/ultrareview` on macOS and Linux to require git 2.31 or newer
      to upload a local repository; checkouts made with `--separate-git-dir` are now
      refused instead of being uploaded with an older method
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Changed `/ultrareview` uploads on macOS and Linux to send a partial clone
      as a working-tree snapshot on git 2.31 or newer, instead of falling back or
      refusing when git's version looked too old
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Changed `/ultrareview` uploads on macOS and Linux to refuse, instead of
      fetching, a partial clone missing some of its working tree's files on older
      git versions; a clone made without `--filter` uploads
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-mobile-and-desktop-changes-in-v2-1-285
  source_release: claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc
  source_type: github_releases
  theme: mobile-desktop
  title: 6 Mobile and Desktop changes in v2.1.285
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-24-2-mobile-and-desktop-changes-in-v2-1-282|2 Mobile
  and Desktop changes in v2.1.282]]'
- '[[Changes/ChatGPT/2026-09-29-site-owners-and-editors-on-plus-and-pro-can-select-edit-site-from-a-published-si|Site
  owners and editors on Plus and Pro can select Edit site from a published Site…]]'
- '[[Changes/ChatGPT/2026-09-29-audio-is-deleted-once-your-notes-are-ready-and-can-t-be-accessed-or-replayed-ava|Audio
  is deleted once your notes are ready and can’t be accessed or replayed]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc|claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc]]'
source_type: github_releases
theme: mobile-desktop
title: 6 Mobile and Desktop changes in v2.1.285
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Mobile and Desktop changes in v2.1.285

**Claude Code** · 2026-09-29 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.285) · from [[Releases/Claude Code/claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc|v2.1.285]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `claude --desktop` to open the Claude desktop app on the current directory, or on a session with `--continue` / `--resume <id>`

> Improved Remote Control: a `/btw` side question asked of a session hosted by an app such as Claude Desktop now sees the turn in progress, not only the last finished one

> Changed `/ultrareview` on macOS and Linux to leave symbolic refs out when uploading a local checkout; a checkout whose current branch is a symbolic ref is now refused with an explanation

> Changed `/ultrareview` on macOS and Linux to require git 2.31 or newer to upload a local repository; checkouts made with `--separate-git-dir` are now refused instead of being uploaded with an older method

> Changed `/ultrareview` uploads on macOS and Linux to send a partial clone as a working-tree snapshot on git 2.31 or newer, instead of falling back or refusing when git's version looked too old

> Changed `/ultrareview` uploads on macOS and Linux to refuse, instead of fetching, a partial clone missing some of its working tree's files on older git versions; a clone made without `--filter` uploads

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-29-2-context-window-changes-in-v2-1-285|2 Context Window changes in v2.1.285]] · Context Window
- [[Changes/Claude Code/2026-09-29-claude-tag-added-direct-messages-with-claude-for-members-on-an-enterprise-plan-s|Claude Tag Added direct messages with Claude for members on an Enterprise plan…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-09-29-improved-responsiveness-when-leaving-the-ctrl-o-transcript-view-in-long-sessions|Improved responsiveness when leaving the ctrl+o transcript view in long sessions…]] · Interface Experience
- [[Changes/Claude Code/2026-09-29-3-model-support-changes-in-v2-1-285|3 Model Support changes in v2.1.285]] · Model Support
- [[Changes/Claude Code/2026-09-29-14-apps-and-integrations-changes-in-v2-1-285|14 Apps and Integrations changes in v2.1.285]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-29-fixed-the-powershell-tool-s-permission-check-skipping-deny-and-ask-rules-and-cac|Fixed the PowerShell tool's permission check skipping deny and ask rules…]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-29-changed-team-and-enterprise-sessions-and-sessions-whose-sign-in-plan-claude-code|Changed Team and Enterprise sessions, and sessions whose sign-in plan Claude Code…]] · Account and Access
- [[Changes/Claude Code/2026-09-29-2-editor-experience-changes-in-v2-1-285|2 Editor Experience changes in v2.1.285]] · Editor Experience
- [[Changes/Claude Code/2026-09-29-2-agent-mode-changes-in-v2-1-285|2 Agent Mode changes in v2.1.285]] · Agent Mode
- [[Changes/Claude Code/2026-09-29-9-safety-and-privacy-changes-in-v2-1-285|9 Safety and Privacy changes in v2.1.285]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-29-changed-memory-so-that-auto-memory-can-no-longer-be-turned-on-from-a-background|Changed /memory so that Auto-memory can no longer be turned on from a background…]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-29-3-developer-workflow-changes-in-v2-1-285|3 Developer Workflow changes in v2.1.285]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-09-29 · ChatGPT · [[Changes/ChatGPT/2026-09-29-audio-is-deleted-once-your-notes-are-ready-and-can-t-be-accessed-or-replayed-ava|Audio is deleted once your notes are ready and can’t be accessed or replayed]]
- Later: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-2-mobile-and-desktop-changes-in-v2-1-287|2 Mobile and Desktop changes in v2.1.287]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-29-1ea1d6&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-29-6-mobile-and-desktop-changes-in-v2-1-285.md%0ACard%20ID%3A%20claude-code-2026-09-29-1ea1d6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.285%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->