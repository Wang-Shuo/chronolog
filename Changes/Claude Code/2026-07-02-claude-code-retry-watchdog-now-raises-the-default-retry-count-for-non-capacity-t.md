---
card_id: claude-code-2026-07-02-ebe592
date: '2026-07-02'
description: 'Claude Code · 2026-07-02 · Reliability and Performance: `CLAUDE_CODE_RETRY_WATCHDOG`
  now raises the default retry count for non-capacity transient errors to…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1295
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: bc5bd46e37d67ae33b85f0aae1d5af7cc3129d2704ad7ead0af299e9efa1d014
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-02-ebe592
  comparison: ''
  date: '2026-07-02'
  description: 'Claude Code — v2.1.199: `CLAUDE_CODE_RETRY_WATCHDOG` now raises the
    default retry count for non-capacity transient errors to 300 and lifts the cap
    of 15 on `CLAUDE_CODE_MAX_RETRIES`'
  evidence:
  - quote: '`CLAUDE_CODE_RETRY_WATCHDOG` now raises the default retry count for non-capacity
      transient errors to 300 and lifts the cap of 15 on `CLAUDE_CODE_MAX_RETRIES`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.199
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: claude-code-retry-watchdog-now-raises-the-default-retry-count-for-non-capacity-t
  source_release: claude-code-2026-07-02-v2-1-199-github-348195313-a8a76d9f
  source_type: github_releases
  theme: reliability-performance
  theme_matches: []
  theme_resolution: manual-backfill-review-v1
  title: '`CLAUDE_CODE_RETRY_WATCHDOG` now raises the default retry count for non-capacity…'
  type: change
related_changes:
- '[[Changes/Cursor/2026-06-17-your-environment-is-captured-in-a-reusable-snapshot-so-future-cloud-agents-start|Your
  environment is captured in a reusable snapshot, so future cloud agents start up…]]'
- '[[Changes/Claude Code/2026-06-20-the-stream-stall-hint-now-reads-waiting-for-api-response-will-retry-in-instead-o|The
  stream-stall hint now reads "Waiting for API response · will retry in …" instead…]]'
- '[[Changes/Claude Code/2026-07-02-transient-server-rate-limit-errors-429s-unrelated-to-your-usage-limit-are-now-re|Transient
  server rate-limit errors (429s unrelated to your usage limit) are now…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-02-v2-1-199-github-348195313-a8a76d9f|claude-code-2026-07-02-v2-1-199-github-348195313-a8a76d9f]]'
source_type: github_releases
theme: reliability-performance
title: CLAUDE_CODE_RETRY_WATCHDOG now raises the default retry count for non-capacity…
type: change
---

<!-- chronolog:begin region="header" -->
# `CLAUDE_CODE_RETRY_WATCHDOG` now raises the default retry count for non-capacity…

**Claude Code** · 2026-07-02 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.199) · from [[Releases/Claude Code/claude-code-2026-07-02-v2-1-199-github-348195313-a8a76d9f|v2.1.199]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `CLAUDE_CODE_RETRY_WATCHDOG` now raises the default retry count for non-capacity transient errors to 300 and lifts the cap of 15 on `CLAUDE_CODE_MAX_RETRIES`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.199
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-02-claude-agents-session-rows-now-show-pull-request-links-as-bare-n-without-the-red|claude agents session rows now show pull-request links as bare ♯N without…]] · Developer Workflow
- [[Changes/Claude Code/2026-07-02-transient-server-rate-limit-errors-429s-unrelated-to-your-usage-limit-are-now-re|Transient server rate-limit errors (429s unrelated to your usage limit) are now…]] · Reliability and Performance
- [[Changes/Claude Code/2026-07-02-stacked-slash-skill-invocations-like-skill-a-skill-b-do-xyz-now-load-all-leading|Stacked slash-skill invocations like /skill-a /skill-b do XYZ now load all leading…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-06-20 · Claude Code · [[Changes/Claude Code/2026-06-20-the-stream-stall-hint-now-reads-waiting-for-api-response-will-retry-in-instead-o|The stream-stall hint now reads "Waiting for API response · will retry in …" instead…]]
- Later: 2026-07-03 · Claude Code · [[Changes/Claude Code/2026-07-03-improved-the-install-script-to-explain-when-installation-is-killed-by-the-system|Improved the install script to explain when installation is killed by the system…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-02-ebe592&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-02-claude-code-retry-watchdog-now-raises-the-default-retry-count-for-non-capacity-t.md%0ACard%20ID%3A%20claude-code-2026-07-02-ebe592%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.199%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->