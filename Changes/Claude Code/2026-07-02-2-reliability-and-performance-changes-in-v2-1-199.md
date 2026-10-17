---
card_id: claude-code-2026-07-02-a630bb
date: '2026-07-02'
description: 'Claude Code · 2026-07-02 · Reliability and Performance: 2 changes in
  v2.1.199 — Transient server rate-limit errors (429s unrelated to your usage limit)
  are now…'
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
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ae399b5c6c4c180b706e48f45f48c370ef696750723e8c679e658a76501b3770
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-02-a630bb
  comparison: ''
  date: '2026-07-02'
  description: 'Claude Code — v2.1.199: 2 Reliability and Performance changes'
  evidence:
  - quote: Transient server rate-limit errors (429s unrelated to your usage limit)
      are now retried automatically with backoff for subscribers instead of failing
      the turn
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.199
  - quote: '`CLAUDE_CODE_RETRY_WATCHDOG` now raises the default retry count for non-capacity
      transient errors to 300 and lifts the cap of 15 on `CLAUDE_CODE_MAX_RETRIES`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.199
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-reliability-and-performance-changes-in-v2-1-199
  source_release: claude-code-2026-07-02-v2-1-199-github-348195313-a8a76d9f
  source_type: github_releases
  theme: reliability-performance
  title: 2 Reliability and Performance changes in v2.1.199
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-06-18-easier-conversation-sharing-sharing-a-conversation-is-now-faster-with-a-one-clic|Easier
  conversation sharing]]'
- '[[Changes/Claude Code/2026-06-20-the-stream-stall-hint-now-reads-waiting-for-api-response-will-retry-in-instead-o|The
  stream-stall hint now reads "Waiting for API response · will retry in …" instead…]]'
- '[[Changes/Claude Code/2026-06-25-added-automatic-memory-pressure-reaping-for-idle-background-shell-commands-disab|Added
  automatic memory-pressure reaping for idle background shell commands…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-02-v2-1-199-github-348195313-a8a76d9f|claude-code-2026-07-02-v2-1-199-github-348195313-a8a76d9f]]'
source_type: github_releases
theme: reliability-performance
title: 2 Reliability and Performance changes in v2.1.199
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Reliability and Performance changes in v2.1.199

**Claude Code** · 2026-07-02 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.199) · from [[Releases/Claude Code/claude-code-2026-07-02-v2-1-199-github-348195313-a8a76d9f|v2.1.199]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Transient server rate-limit errors (429s unrelated to your usage limit) are now retried automatically with backoff for subscribers instead of failing the turn

> `CLAUDE_CODE_RETRY_WATCHDOG` now raises the default retry count for non-capacity transient errors to 300 and lifts the cap of 15 on `CLAUDE_CODE_MAX_RETRIES`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.199
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-02-claude-agents-session-rows-now-show-pull-request-links-as-bare-n-without-the-red|claude agents session rows now show pull-request links as bare ♯N without…]] · Developer Workflow
- [[Changes/Claude Code/2026-07-02-stacked-slash-skill-invocations-like-skill-a-skill-b-do-xyz-now-load-all-leading|Stacked slash-skill invocations like /skill-a /skill-b do XYZ now load all leading…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-06-25 · Claude Code · [[Changes/Claude Code/2026-06-25-added-automatic-memory-pressure-reaping-for-idle-background-shell-commands-disab|Added automatic memory-pressure reaping for idle background shell commands…]]
- Later: 2026-07-03 · Claude Code · [[Changes/Claude Code/2026-07-03-improved-the-install-script-to-explain-when-installation-is-killed-by-the-system|Improved the install script to explain when installation is killed by the system…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-02-a630bb&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-02-2-reliability-and-performance-changes-in-v2-1-199.md%0ACard%20ID%3A%20claude-code-2026-07-02-a630bb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.199%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->