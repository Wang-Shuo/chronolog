---
card_id: claude-code-2026-03-26-33b65d
date: '2026-03-26'
description: 'Claude Code · 2026-03-26 · Reliability and Performance: Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS`
  env var to configure the streaming idle watchdog threshold…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1197
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 539d546f008cb7db26fd6e750d561401b33b879a904859af11aacdaa699c8d35
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-26-33b65d
  comparison: ''
  date: '2026-03-26'
  description: 'Claude Code — v2.1.84: Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var
    to configure the streaming idle watchdog threshold (default 90s)'
  evidence:
  - quote: Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming
      idle watchdog threshold (default 90s)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-claude-stream-idle-timeout-ms-env-var-to-configure-the-streaming-idle-watc
  source_release: claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa
  source_type: github_releases
  theme: reliability-performance
  theme_matches: []
  theme_resolution: manual-backfill-review-v1
  title: Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming
    idle…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-18-improved-startup-memory-usage-by-18mb-across-all-scenarios|Improved
  startup memory usage by ~18MB across all scenarios]]'
- '[[Changes/Claude Code/2026-03-18-improved-non-streaming-api-fallback-with-a-2-minute-per-attempt-timeout-preventi|Improved
  non-streaming API fallback with a 2-minute per-attempt timeout, preventing…]]'
- '[[Changes/Cursor/2026-03-19-composer-2-is-now-available-in-cursor-frontier-level-coding-performance-with-str|Composer
  2 is now available in Cursor]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa]]'
source_type: github_releases
superseded: true
theme: reliability-performance
title: Added CLAUDE_STREAM_IDLE_TIMEOUT_MS env var to configure the streaming idle…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming idle…

**Claude Code** · 2026-03-26 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.84) · from [[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|v2.1.84]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming idle watchdog threshold (default 90s)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-26-added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef|Added ANTHROPIC_DEFAULT{OPUS,SONNET,HAIKU}MODEL_SUPPORTS env vars to override…]] · Model Support
- [[Changes/Claude Code/2026-03-26-added-taskcreated-hook-that-fires-when-a-task-is-created-via-taskcreate|Added TaskCreated hook that fires when a task is created via TaskCreate]] · Agent Mode
- [[Changes/Claude Code/2026-03-26-added-powershell-tool-for-windows-as-an-opt-in-preview-learn-more-at-https-code|Added PowerShell tool for Windows as an opt-in preview]] · Mobile and Desktop
- [[Changes/Claude Code/2026-03-26-added-worktreecreate-hook-support-for-type-http-return-the-created-worktree-path|Added WorktreeCreate hook support for type: "http"]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-03-19 · Cursor · [[Changes/Cursor/2026-03-19-composer-2-is-now-available-in-cursor-frontier-level-coding-performance-with-str|Composer 2 is now available in Cursor]]
- Later: 2026-04-10 · Claude Code · [[Changes/Claude Code/2026-04-10-improved-brief-mode-to-retry-once-when-claude-responds-with-plain-text-instead-o|Improved brief mode to retry once when Claude responds with plain text instead…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-26-33b65d&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-26-added-claude-stream-idle-timeout-ms-env-var-to-configure-the-streaming-idle-watc.md%0ACard%20ID%3A%20claude-code-2026-03-26-33b65d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.84%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->