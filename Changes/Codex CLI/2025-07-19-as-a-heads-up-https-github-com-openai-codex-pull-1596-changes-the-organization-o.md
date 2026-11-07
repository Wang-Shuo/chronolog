---
card_id: codex-cli-2025-07-19-1db886
date: '2025-07-19'
description: 'Codex CLI · 2025-07-19 · Reliability and Performance: As a heads up,
  https://github.com/openai/codex/pull/1596 changes the organization of the…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2434
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 4439fe1fd875c75796ddaabe73bcfa1aa8e7b37f8a411329928c06315fc4de5e
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
- '[[Changes/Dify/2025-07-10-optimize-the-memory-usage-of-tencent-vector-database-by-wlleiiwang-in-https-gith|Optimize
  the memory usage of Tencent Vector Database]]'
- '[[Changes/Open WebUI/2025-07-14-4-reliability-and-performance-changes-in-v0-6-16|4
  Reliability and Performance changes in v0.6.16]]'
- '[[Changes/Ollama/2025-07-18-2-reliability-and-performance-changes-in-v0-10-0|2
  Reliability and Performance changes in v0.10.0]]'
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

- Earlier: 2025-07-18 · Ollama · [[Changes/Ollama/2025-07-18-2-reliability-and-performance-changes-in-v0-10-0|2 Reliability and Performance changes in v0.10.0]]
- Later: 2025-07-19 · Gemini CLI · [[Changes/Gemini CLI/2025-07-19-run-model-availability-check-in-the-background-to-speed-up-startup-by-sandytao52|Run model availability check in the background to speed up startup]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-07-19-1db886&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-07-19-as-a-heads-up-https-github-com-openai-codex-pull-1596-changes-the-organization-o.md%0ACard%20ID%3A%20codex-cli-2025-07-19-1db886%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->