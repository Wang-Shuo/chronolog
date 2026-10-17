---
card_id: claude-code-2026-03-26-b1182f
date: '2026-03-26'
description: 'Claude Code · 2026-03-26 · Developer Workflow: Added `WorktreeCreate`
  hook support for `type: "http"` — return the created worktree path via…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1104
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: significant
machine_hash: 59c970582dd9ae797ed554b2350eb69a01e34a326edfb1f5ba0471f09c436575
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-03-26-b1182f
  comparison: ''
  confidence: low
  date: '2026-03-26'
  description: 'Claude Code — v2.1.84: Added `WorktreeCreate` hook support for `type:
    "http"` — return the created worktree path via `hookSpecificOutput.worktreePath`
    in the response JSON'
  evidence:
  - quote: 'Added `WorktreeCreate` hook support for `type: "http"` — return the created
      worktree path via `hookSpecificOutput.worktreePath` in the response JSON'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  extractor_version: fallback-v4
  impact: significant
  product: claude-code
  product_name: Claude Code
  slug: added-worktreecreate-hook-support-for-type-http-return-the-created-worktree-path
  source_release: claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa
  source_type: github_releases
  theme: developer-workflow
  title: 'Added `WorktreeCreate` hook support for `type: "http"`'
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-17-terminal-notifications-iterm2-kitty-ghostty-popups-progress-bar-now-reach-the-ou|Terminal
  notifications (iTerm2/Kitty/Ghostty popups, progress bar) now reach…]]'
- '[[Changes/Claude Code/2026-03-20-resuming-a-session-that-was-in-a-worktree-now-switches-back-to-that-worktree|Resuming
  a session that was in a worktree now switches back to that worktree]]'
- '[[Changes/Claude Code/2026-03-20-added-bare-flag-for-scripted-p-calls-skips-hooks-lsp-plugin-sync-and-skill-direc|Added
  --bare flag for scripted -p calls]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa]]'
source_type: github_releases
superseded: true
theme: developer-workflow
title: 'Added WorktreeCreate hook support for type: "http"'
type: change
---

<!-- chronolog:begin region="header" -->
# Added `WorktreeCreate` hook support for `type: "http"`

**Claude Code** · 2026-03-26 · [[Themes/developer-workflow|Developer Workflow]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.84) · from [[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|v2.1.84]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `WorktreeCreate` hook support for `type: "http"` — return the created worktree path via `hookSpecificOutput.worktreePath` in the response JSON
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-26-added-claude-stream-idle-timeout-ms-env-var-to-configure-the-streaming-idle-watc|Added CLAUDE_STREAM_IDLE_TIMEOUT_MS env var to configure the streaming idle…]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-26-added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef|Added ANTHROPIC_DEFAULT{OPUS,SONNET,HAIKU}MODEL_SUPPORTS env vars to override…]] · Model Support
- [[Changes/Claude Code/2026-03-26-added-taskcreated-hook-that-fires-when-a-task-is-created-via-taskcreate|Added TaskCreated hook that fires when a task is created via TaskCreate]] · Agent Mode
- [[Changes/Claude Code/2026-03-26-added-powershell-tool-for-windows-as-an-opt-in-preview-learn-more-at-https-code|Added PowerShell tool for Windows as an opt-in preview]] · Mobile and Desktop
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-20 · Claude Code · [[Changes/Claude Code/2026-03-20-added-bare-flag-for-scripted-p-calls-skips-hooks-lsp-plugin-sync-and-skill-direc|Added --bare flag for scripted -p calls]]
- Later: 2026-03-27 · Claude Code · [[Changes/Claude Code/2026-03-27-added-x-claude-code-session-id-header-to-api-requests-so-proxies-can-aggregate-r|Added X-Claude-Code-Session-Id header to API requests so proxies can aggregate…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-26-b1182f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-26-added-worktreecreate-hook-support-for-type-http-return-the-created-worktree-path.md%0ACard%20ID%3A%20claude-code-2026-03-26-b1182f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.84%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->