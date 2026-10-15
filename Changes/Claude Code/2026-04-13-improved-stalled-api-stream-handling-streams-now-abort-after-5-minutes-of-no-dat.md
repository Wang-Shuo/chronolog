---
card_id: claude-code-2026-04-13-c9394b
date: '2026-04-13'
description: 'Claude Code · 2026-04-13 · Reliability and Performance: Improved stalled
  API stream handling: streams now abort after 5 minutes of no data and retry…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1215
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: b91711e7053473f612314bb6d29131833c2bc81b208069c2b56e517b56d474ad
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-13-c9394b
  comparison: ''
  date: '2026-04-13'
  description: 'Claude Code — v2.1.105: Improved stalled API stream handling: streams
    now abort after 5 minutes of no data and retry non-streaming instead of hanging
    indefinitely'
  evidence:
  - quote: 'Improved stalled API stream handling: streams now abort after 5 minutes
      of no data and retry non-streaming instead of hanging indefinitely'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.105
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: improved-stalled-api-stream-handling-streams-now-abort-after-5-minutes-of-no-dat
  source_release: claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3
  source_type: github_releases
  theme: reliability-performance
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Improved stalled API stream handling
  type: change
related_changes:
- '[[Changes/Cursor/2026-03-19-composer-2-is-now-available-in-cursor-frontier-level-coding-performance-with-str|Composer
  2 is now available in Cursor]]'
- '[[Changes/Claude Code/2026-03-26-added-claude-stream-idle-timeout-ms-env-var-to-configure-the-streaming-idle-watc|Added
  CLAUDE_STREAM_IDLE_TIMEOUT_MS env var to configure the streaming idle…]]'
- '[[Changes/Claude Code/2026-04-10-improved-brief-mode-to-retry-once-when-claude-responds-with-plain-text-instead-o|Improved
  brief mode to retry once when Claude responds with plain text instead…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3|claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3]]'
source_type: github_releases
theme: reliability-performance
title: Improved stalled API stream handling
type: change
---

<!-- chronolog:begin region="header" -->
# Improved stalled API stream handling

**Claude Code** · 2026-04-13 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.105) · from [[Releases/Claude Code/claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3|v2.1.105]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved stalled API stream handling: streams now abort after 5 minutes of no data and retry non-streaming instead of hanging indefinitely
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.105
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-13-added-path-parameter-to-the-enterworktree-tool-to-switch-into-an-existing-worktr|Added path parameter to the EnterWorktree tool to switch into an existing…]] · Developer Workflow
- [[Changes/Claude Code/2026-04-13-added-background-monitor-support-for-plugins-via-a-top-level-monitors-manifest-k|Added background monitor support for plugins via a top-level monitors manifest key…]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-13-added-precompact-hook-support-hooks-can-now-block-compaction-by-exiting-with-cod|Added PreCompact hook support]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-13-proactive-is-now-an-alias-for-loop|/proactive is now an alias for /loop]] · Automation and Scheduling
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-04-10 · Claude Code · [[Changes/Claude Code/2026-04-10-improved-brief-mode-to-retry-once-when-claude-responds-with-plain-text-instead-o|Improved brief mode to retry once when Claude responds with plain text instead…]]
- Later: 2026-04-20 · Claude Code · [[Changes/Claude Code/2026-04-20-resume-on-large-sessions-is-significantly-faster-up-to-67-on-40mb-sessions-and-h|/resume on large sessions is significantly faster (up to 67% on 40MB+ sessions)…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-13-c9394b&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-13-improved-stalled-api-stream-handling-streams-now-abort-after-5-minutes-of-no-dat.md%0ACard%20ID%3A%20claude-code-2026-04-13-c9394b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.105%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->