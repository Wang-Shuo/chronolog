---
card_id: claude-code-2026-10-14-2e5cb3
date: '2026-10-14'
description: 'Claude Code · 2026-10-14 · Developer Workflow: 10 changes in v2.1.299
  — Added idle compaction in the terminal: a 200K+ token conversation left idle for
  about…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1306
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b72f19fcef85191a3c8dff1785ba4881c2e8beeae3447ff101e771213b794a8c
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-14-2e5cb3
  comparison: ''
  date: '2026-10-14'
  description: 'Claude Code — v2.1.299: 10 Developer Workflow changes'
  evidence:
  - quote: 'Added idle compaction in the terminal: a 200K+ token conversation left
      idle for about 54 minutes is compacted before its one-hour prompt cache expires,
      so your next message doesn''t reprocess it all'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: 'Self-hosted runner: Improved what `setup` and `doctor` say when the runner''s
      machine has no git credentials'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: 'Improved sandboxed Bash on Linux: Esc and Ctrl-C now work while wildcard
      read rules are being expanded for a command'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: 'Improved the error shown when a worktree cannot be created because its
      base commit does not resolve: it now says how the lookup ended and the likely
      reasons, such as a repository without a commit'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: 'Improved the error for creating a worktree at a bare-repository layout''s
      root: it now explains the layout instead of an unrelated git error'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: 'Changed skill and command loading: one whose file or folder name has hidden,
      direction-changing or blank-like characters, `<` or `>` is no longer offered
      until renamed; such a `name:` is ignored'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: 'Changed the resume command printed at exit: it names the session by its
      ID and no longer by its name, so that nothing in a session name can run when
      the line is pasted'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: 'Changed the resume command printed at exit of a worktree session: it uses
      `-w` and `-r` if the long flags do not fit the terminal. If neither fits a kept
      worktree, rows above it say where to run it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Changed the errors shown when `/ultrareview` can't upload a repository
      to stop suggesting `git add .`, which could stage or commit untracked files
      such as `.env`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: '[Cloud sessions] Improved the deploy command shown when you create a self-hosted
      environment or environment key: it shows in full, wraps between arguments, and
      has a visible copy button'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 10-developer-workflow-changes-in-v2-1-299
  source_release: claude-code-2026-10-14-v2-1-299-github-412217284-623d9162
  source_type: github_releases
  theme: developer-workflow
  title: 10 Developer Workflow changes in v2.1.299
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-08-added-a-line-on-stderr-when-it-is-a-terminal-that-says-what-a-claude-p-run-is-wa|Added
  a line on stderr, when it is a terminal, that says what a claude -p run…]]'
- '[[Changes/Claude Code/2026-10-09-3-developer-workflow-changes-in-v2-1-296|3 Developer
  Workflow changes in v2.1.296]]'
- '[[Changes/Claude Code/2026-10-14-added-a-dir-prop-on-a-mod-s-text-for-right-to-left-text-on-windows-and-in-vs-cod|Added
  a dir prop on a mod''s Text for right-to-left text]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-14-v2-1-299-github-412217284-623d9162|claude-code-2026-10-14-v2-1-299-github-412217284-623d9162]]'
source_type: github_releases
theme: developer-workflow
title: 10 Developer Workflow changes in v2.1.299
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Developer Workflow changes in v2.1.299

**Claude Code** · 2026-10-14 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.299) · from [[Releases/Claude Code/claude-code-2026-10-14-v2-1-299-github-412217284-623d9162|v2.1.299]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added idle compaction in the terminal: a 200K+ token conversation left idle for about 54 minutes is compacted before its one-hour prompt cache expires, so your next message doesn't reprocess it all

> Self-hosted runner: Improved what `setup` and `doctor` say when the runner's machine has no git credentials

> Improved sandboxed Bash on Linux: Esc and Ctrl-C now work while wildcard read rules are being expanded for a command

> Improved the error shown when a worktree cannot be created because its base commit does not resolve: it now says how the lookup ended and the likely reasons, such as a repository without a commit

> Improved the error for creating a worktree at a bare-repository layout's root: it now explains the layout instead of an unrelated git error

> Changed skill and command loading: one whose file or folder name has hidden, direction-changing or blank-like characters, `<` or `>` is no longer offered until renamed; such a `name:` is ignored

> Changed the resume command printed at exit: it names the session by its ID and no longer by its name, so that nothing in a session name can run when the line is pasted

> Changed the resume command printed at exit of a worktree session: it uses `-w` and `-r` if the long flags do not fit the terminal. If neither fits a kept worktree, rows above it say where to run it

> Changed the errors shown when `/ultrareview` can't upload a repository to stop suggesting `git add .`, which could stage or commit untracked files such as `.env`

> [Cloud sessions] Improved the deploy command shown when you create a self-hosted environment or environment key: it shows in full, wraps between arguments, and has a visible copy button

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-14-added-a-one-time-note-when-plan-mode-won-t-ask-before-most-edits-or-commands-bec|Added a one-time note when plan mode won't ask before most edits or commands because…]] · Editor Experience
- [[Changes/Claude Code/2026-10-14-19-apps-and-integrations-changes-in-v2-1-299|19 Apps and Integrations changes in v2.1.299]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-14-2-context-window-changes-in-v2-1-299|2 Context Window changes in v2.1.299]] · Context Window
- [[Changes/Claude Code/2026-10-14-2-model-support-changes-in-v2-1-299|2 Model Support changes in v2.1.299]] · Model Support
- [[Changes/Claude Code/2026-10-14-2-files-and-data-changes-in-v2-1-299|2 Files and Data changes in v2.1.299]] · Files and Data
- [[Changes/Claude Code/2026-10-14-added-support-for-turning-off-the-attribution-block-in-claude-desktop-s-code-tab|Added support for turning off the attribution block in Claude Desktop's Code tab]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-14-5-agent-mode-changes-in-v2-1-299|5 Agent Mode changes in v2.1.299]] · Agent Mode
- [[Changes/Claude Code/2026-10-14-added-effort-and-fast-in-agent-view-to-set-what-new-sessions-start-with-a-bare-m|Added /effort and /fast in agent view to set what new sessions start with]] · Interface Experience
- [[Changes/Claude Code/2026-10-14-improved-memory-and-disk-use-when-pdfs-are-mentioned-their-bytes-are-no-longer-k|Improved memory and disk use when PDFs are @-mentioned]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-14-added-usage-warnings-for-max-effort-workflows-always-on-context-and-large-tool-r|Added /usage warnings for max effort, workflows, always-on context and large tool…]] · Context Window
- [[Changes/Claude Code/2026-10-14-improved-the-error-shown-when-a-cloud-session-is-refused-because-your-claude-ai|Improved the error shown when a cloud session is refused because your claude.ai…]] · Account and Access
- [[Changes/Claude Code/2026-10-14-vscode-improved-startup-the-model-picker-and-slash-command-menu-now-fill-in-righ|VSCode Improved startup]] · Interface Experience
- [[Changes/Claude Code/2026-10-14-6-safety-and-privacy-changes-in-v2-1-299|6 Safety and Privacy changes in v2.1.299]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-14-11-other-changes-in-v2-1-299|11 other changes in v2.1.299]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-added-a-dir-prop-on-a-mod-s-text-for-right-to-left-text-on-windows-and-in-vs-cod|Added a dir prop on a mod's Text for right-to-left text]]
- Later: 2026-10-15 · Claude Code · [[Changes/Claude Code/2026-10-15-added-rows-to-a-mod-s-input-a-text-field-of-several-lines-in-the-terminal-where|Added rows to a mod's Input]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-14-2e5cb3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-14-10-developer-workflow-changes-in-v2-1-299.md%0ACard%20ID%3A%20claude-code-2026-10-14-2e5cb3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.299%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->