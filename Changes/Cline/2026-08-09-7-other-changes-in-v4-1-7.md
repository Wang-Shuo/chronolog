---
card_id: cline-2026-08-09-3ab42a
date: '2026-08-09'
description: 'Cline · 2026-08-09 · Other changes: 7 changes in v4.1.7 — Bring back
  a copy button on turn-final response rows.'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dd6ff058eb2d89bb377b8c3016a8662e3bc311902e85aa1cd00f79bcd1dbf3f7
product: cline
product_name: Cline
record:
  card_id: cline-2026-08-09-3ab42a
  comparison: ''
  date: '2026-08-09'
  description: 'Cline — v4.1.7: 7 other changes'
  evidence:
  - quote: Bring back a copy button on turn-final response rows.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.7
  - quote: Fade the "View Changes" button until changes since the last message are
      confirmed, and hide it entirely when there is nothing to show.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.7
  - quote: 'Preserve prompts queued during a turn when that turn is interrupted: they
      survive aborts, are drained after a turn aborts itself, and the stop is surfaced
      instead of the queue being silently dropped.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.7
  - quote: Settle the turn phase when a mode switch aborts a running turn.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.7
  - quote: Report queued-turn failures as `run.failed` instead of letting them complete
      silently.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.7
  - quote: Route LiteLLM through Chat Completions instead of the Responses API, fixing
      requests against LiteLLM proxies.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.7
  - quote: Use the configured fetch for Vertex ADC token refreshes, so they work behind
      proxies and custom transports.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 7-other-changes-in-v4-1-7
  source_release: cline-2026-08-09-v4-1-7-github-367373350-886ff444
  source_type: github_releases
  theme: uncategorized
  title: 7 other changes in v4.1.7
  type: change
source_release: '[[Releases/Cline/cline-2026-08-09-v4-1-7-github-367373350-886ff444|cline-2026-08-09-v4-1-7-github-367373350-886ff444]]'
source_type: github_releases
theme: uncategorized
title: 7 other changes in v4.1.7
type: change
---

<!-- chronolog:begin region="header" -->
# 7 other changes in v4.1.7

**Cline** · 2026-08-09 · Other changes · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.7) · from [[Releases/Cline/cline-2026-08-09-v4-1-7-github-367373350-886ff444|v4.1.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Bring back a copy button on turn-final response rows.

> Fade the "View Changes" button until changes since the last message are confirmed, and hide it entirely when there is nothing to show.

> Preserve prompts queued during a turn when that turn is interrupted: they survive aborts, are drained after a turn aborts itself, and the stop is surfaced instead of the queue being silently dropped.

> Settle the turn phase when a mode switch aborts a running turn.

> Report queued-turn failures as `run.failed` instead of letting them complete silently.

> Route LiteLLM through Chat Completions instead of the Responses API, fixing requests against LiteLLM proxies.

> Use the configured fetch for Vertex ADC token refreshes, so they work behind proxies and custom transports.

Source: https://github.com/cline/cline/releases/tag/v4.1.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-08-09-fall-back-to-the-session-cwd-or-desktop-for-mention-file-search-in-empty-windows|Fall back to the session cwd or Desktop for @-mention file search in empty windows]] · Mobile and Desktop
- [[Changes/Cline/2026-08-09-2-account-and-access-changes-in-v4-1-7|2 Account and Access changes in v4.1.7]] · Account and Access
- [[Changes/Cline/2026-08-09-include-files-that-were-untracked-when-a-snapshot-was-taken-in-checkpoint-diffs|Include files that were untracked when a snapshot was taken in checkpoint diffs…]] · Developer Workflow
- [[Changes/Cline/2026-08-09-retry-network-interruptions-that-happen-mid-stream-but-before-any-model-output-i|Retry network interruptions that happen mid-stream but before any model output…]] · Model Support
- [[Changes/Cline/2026-08-09-2-context-window-changes-in-v4-1-7|2 Context Window changes in v4.1.7]] · Context Window
- [[Changes/Cline/2026-08-09-restore-the-view-changes-button-on-completion-rows-backed-by-sdk-checkpoints-so|Restore the "View Changes" button on completion rows, backed by SDK checkpoints…]] · Editor Experience
- [[Changes/Cline/2026-08-09-2-apps-and-integrations-changes-in-v4-1-7|2 Apps and Integrations changes in v4.1.7]] · Apps and Integrations
- [[Changes/Cline/2026-08-09-never-run-a-foreign-compiled-plugin-sandbox-bootstrap-for-a-source-host|Never run a foreign compiled plugin-sandbox bootstrap for a source host]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-08-09-3ab42a&body=Card%3A%20Changes%2FCline%2F2026-08-09-7-other-changes-in-v4-1-7.md%0ACard%20ID%3A%20cline-2026-08-09-3ab42a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->