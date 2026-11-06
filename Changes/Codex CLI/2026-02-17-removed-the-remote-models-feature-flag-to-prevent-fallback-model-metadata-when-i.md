---
card_id: codex-cli-2026-02-17-16059a
date: '2026-02-17'
description: 'Codex CLI · 2026-02-17 · Reliability and Performance: Removed the `remote_models`
  feature flag to prevent fallback model metadata when it was disabled…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1160
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: ed461e78d134193bcf7bb00e6d60492b6828d9d6d54e13125383d4d7e2fd417c
product: codex-cli
product_name: Codex CLI
record:
  ai_generated: true
  card_id: codex-cli-2026-02-17-16059a
  comparison: ''
  confidence: low
  date: '2026-02-17'
  description: 'Codex CLI — 0.103.0: Removed the `remote_models` feature flag to prevent
    fallback model metadata when it was disabled, improving model selection reliability
    and performance. (#11699)'
  evidence:
  - quote: Removed the `remote_models` feature flag to prevent fallback model metadata
      when it was disabled, improving model selection reliability and performance.
      (#11699)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.103.0
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: removed-the-remote-models-feature-flag-to-prevent-fallback-model-metadata-when-i
  source_release: codex-cli-2026-02-17-rust-v0-103-0-github-287457049-69ff7e22
  source_type: github_releases
  theme: reliability-performance
  theme_matches:
  - matched_terms:
    - reliability and performance
    - performance
    score: 180
    theme: reliability-performance
  - matched_terms:
    - model
    - models
    score: 100
    theme: model-support
  title: Removed the `remote_models` feature flag to prevent fallback model metadata…
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-02-13-performance-improvements-we-ve-made-multiple-performance-enhancements-to-improve|Performance
  improvements]]'
- '[[Changes/GitHub Copilot CLI/2026-02-14-reduce-memory-usage-from-encoding-streaming-chunks|Reduce
  memory usage from encoding streaming chunks]]'
- '[[Changes/Claude Code/2026-02-17-improved-memory-usage-for-shell-commands-that-produce-large-output-rss-no-longer|Improved
  memory usage for shell commands that produce large output]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-17-rust-v0-103-0-github-287457049-69ff7e22|codex-cli-2026-02-17-rust-v0-103-0-github-287457049-69ff7e22]]'
source_type: github_releases
theme: reliability-performance
title: Removed the remote_models feature flag to prevent fallback model metadata…
type: change
---

<!-- chronolog:begin region="header" -->
# Removed the `remote_models` feature flag to prevent fallback model metadata…

**Codex CLI** · 2026-02-17 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.103.0) · from [[Releases/Codex CLI/codex-cli-2026-02-17-rust-v0-103-0-github-287457049-69ff7e22|0.103.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Removed the `remote_models` feature flag to prevent fallback model metadata when it was disabled, improving model selection reliability and performance. (#11699)
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.103.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-17-11699-chore-rm-remote-models-fflag-sayan-oai|♯11699 chore: rm remote models fflag @sayan-oai]] · Model Support
- [[Changes/Codex CLI/2026-02-17-commit-co-author-attribution-now-uses-a-codex-managed-prepare-commit-msg-hook-wi|Commit co-author attribution now uses a Codex-managed prepare-commit-msg hook…]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-17-11706-apps-expose-more-fields-from-apps-listing-endpoints-mzeng-openai|♯11706 apps Expose more fields from apps listing endpoints]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-17-9-other-changes-in-rust-v0-103-0|9 other changes in rust-v0.103.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-02-17 · Claude Code · [[Changes/Claude Code/2026-02-17-improved-memory-usage-for-shell-commands-that-produce-large-output-rss-no-longer|Improved memory usage for shell commands that produce large output]]
- Later: 2026-02-17 · Cursor · [[Changes/Cursor/2026-02-17-2-reliability-and-performance-changes-in-2-5|2 Reliability and Performance changes in 2.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-17-16059a&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-17-removed-the-remote-models-feature-flag-to-prevent-fallback-model-metadata-when-i.md%0ACard%20ID%3A%20codex-cli-2026-02-17-16059a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.103.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->