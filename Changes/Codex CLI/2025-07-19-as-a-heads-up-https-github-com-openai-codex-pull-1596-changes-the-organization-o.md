---
card_id: codex-cli-2025-07-19-1db886
date: '2025-07-19'
description: 'Codex CLI · 2025-07-19 · Reliability and Performance: As a heads up,
  https://github.com/openai/codex/pull/1596 changes the organization of the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 947
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 77c3a7d729aa76fc782511efded485841c7ef4c727d96acd32222fc61ae7151a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-07-19-1db886
  comparison: ''
  date: '2025-07-19'
  description: 'Codex CLI — 0.8.0: As a heads up, https://github.com/openai/codex/pull/1596
    changes the organization of the `~/.codex/sessions` folder so it has `YYYY/MM/DD`
    subfolders. This should make it easier to find recent sessions and avoid degrading
    filesystem performance because previously `~/.codex/sessions` could end up with
    an unbounded number of entries'
  evidence:
  - quote: As a heads up, https://github.com/openai/codex/pull/1596 changes the organization
      of the `~/.codex/sessions` folder so it has `YYYY/MM/DD` subfolders. This should
      make it easier to find recent sessions and avoid degrading filesystem performance
      because previously `~/.codex/sessions` could end up with an unbounded number
      of entries
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.8.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: as-a-heads-up-https-github-com-openai-codex-pull-1596-changes-the-organization-o
  source_release: codex-cli-2025-07-19-rust-v0-8-0-github-233643033-2038cb65
  source_type: github_releases
  theme: reliability-performance
  title: As a heads up, https://github.com/openai/codex/pull/1596 changes the organization…
  type: change
related_changes:
- '[[Changes/Cursor/2025-07-03-faster-tab|Faster Tab]]'
- '[[Changes/Cursor/2025-07-03-4-reliability-and-performance-changes-in-1-2|4 Reliability
  and Performance changes in 1.2]]'
- '[[Changes/Cline/2025-07-08-optimize-provider-switching-performance-with-batched-storage-operations-by-arafa|Optimize
  provider switching performance with batched storage operations]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-07-19-rust-v0-8-0-github-233643033-2038cb65|codex-cli-2025-07-19-rust-v0-8-0-github-233643033-2038cb65]]'
source_type: github_releases
theme: reliability-performance
title: As a heads up, (source link) changes the organization…
type: change
---

<!-- chronolog:begin region="header" -->
# As a heads up, https://github.com/openai/codex/pull/1596 changes the organization…

**Codex CLI** · 2025-07-19 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.8.0) · from [[Releases/Codex CLI/codex-cli-2025-07-19-rust-v0-8-0-github-233643033-2038cb65|0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> As a heads up, https://github.com/openai/codex/pull/1596 changes the organization of the `~/.codex/sessions` folder so it has `YYYY/MM/DD` subfolders. This should make it easier to find recent sessions and avoid degrading filesystem performance because previously `~/.codex/sessions` could end up with an unbounded number of entries
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.8.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-07-19-though-https-github-com-openai-codex-pull-1590-should-make-it-so-that-on-windows|Though (source link) should make it so that, on Windows…]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-07-19-https-github-com-openai-codex-pull-1589-changes-ctrl-d-so-it-only-exits-the-tui|(source link) changes ctrl-d so it only exits the TUI…]] · Agent Mode
- [[Changes/Codex CLI/2025-07-19-as-of-https-github-com-openai-codex-pull-1594-we-now-stream-the-response-from-th|As of (source link) we now stream the response…]] · Model Support
- [[Changes/Codex CLI/2025-07-19-https-github-com-openai-codex-pull-1571-fixes-a-longstanding-issue-where-we-fail|(source link) fixes a longstanding issue where we failed…]] · Apps and Integrations
- [[Changes/Codex CLI/2025-07-19-2-other-changes-in-rust-v0-8-0|2 other changes in rust-v0.8.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2025-07-08 · Cline · [[Changes/Cline/2025-07-08-optimize-provider-switching-performance-with-batched-storage-operations-by-arafa|Optimize provider switching performance with batched storage operations]]
- Later: 2025-07-19 · Gemini CLI · [[Changes/Gemini CLI/2025-07-19-run-model-availability-check-in-the-background-to-speed-up-startup-by-sandytao52|Run model availability check in the background to speed up startup]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-07-19-1db886&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-07-19-as-a-heads-up-https-github-com-openai-codex-pull-1596-changes-the-organization-o.md%0ACard%20ID%3A%20codex-cli-2025-07-19-1db886%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->