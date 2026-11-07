---
card_id: github-copilot-cli-2026-08-03-661438
date: '2026-08-03'
description: 'GitHub Copilot CLI · 2026-08-03 · Reliability and Performance: Resuming
  a long session is dramatically faster and far lighter on memory, because its history
  is…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1327
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 3cb6820d4627edcb14367547a02017c48527eee07295d316578bbff01266d73b
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-08-03-661438
  comparison: ''
  date: '2026-08-03'
  description: 'GitHub Copilot CLI — 1.0.78: Resuming a long session is dramatically
    faster and far lighter on memory, because its history is now read once at startup
    (in parallel, across CPU cores) instead of being re-read in full for every check
    the CLI runs before it can paint. In our benchmark a 230MB, 74k-event transcript
    came back in well under a second instead of about ten, at roughly a quarter of
    the peak memory; the exact gain depends on your machine''s core count and disk'
  evidence:
  - quote: Resuming a long session is dramatically faster and far lighter on memory,
      because its history is now read once at startup (in parallel, across CPU cores)
      instead of being re-read in full for every check the CLI runs before it can
      paint. In our benchmark a 230MB, 74k-event transcript came back in well under
      a second instead of about ten, at roughly a quarter of the peak memory; the
      exact gain depends on your machine's core count and disk
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: resuming-a-long-session-is-dramatically-faster-and-far-lighter-on-memory-because
  source_release: github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc
  source_type: github_releases
  theme: reliability-performance
  theme_matches:
  - matched_terms:
    - memory
    score: 110
    theme: memory
  - matched_terms:
    - faster
    score: 50
    theme: reliability-performance
  theme_resolution: manual-semantic-rule-v2
  title: Resuming a long session is dramatically faster and far lighter on memory,
    because…
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-30-diff-scrolls-and-syntax-highlights-large-multi-file-diffs-faster|/diff
  scrolls and syntax-highlights large multi-file diffs faster]]'
- '[[Changes/Runway/2026-07-30-when-you-hit-your-concurrency-limit-on-a-model-model-router-can-now-automaticall|Capacity
  Fallbacks in Model Router]]'
- '[[Changes/Google Antigravity/2026-07-31-2-reliability-and-performance-changes-in-hub-v2-5-0-enterprise-sign-in-gemini|2
  Reliability and Performance changes in HUB v2.5.0 — Enterprise sign-in: Gemini…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc|github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc]]'
source_type: github_releases
theme: reliability-performance
title: Resuming a long session is dramatically faster and far lighter on memory, because…
type: change
---

<!-- chronolog:begin region="header" -->
# Resuming a long session is dramatically faster and far lighter on memory, because…

**GitHub Copilot CLI** · 2026-08-03 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.78) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc|1.0.78]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Resuming a long session is dramatically faster and far lighter on memory, because its history is now read once at startup (in parallel, across CPU cores) instead of being re-read in full for every check the CLI runs before it can paint. In our benchmark a 230MB, 74k-event transcript came back in well under a second instead of about ten, at roughly a quarter of the peak memory; the exact gain depends on your machine's core count and disk
>
> Source: https://github.com/github/copilot-cli/releases/tag/v1.0.78
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-08-03-4-apps-and-integrations-changes-in-v1-0-78|4 Apps and Integrations changes in v1.0.78]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-08-03-a-run-whose-prompt-is-piped-over-stdin-now-treats-its-sessionend-hook-the-same-w|A run whose prompt is piped over stdin now treats its sessionEnd hook the same way…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-08-03-2-editor-experience-changes-in-v1-0-78|2 Editor Experience changes in v1.0.78]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-08-03-2-account-and-access-changes-in-v1-0-78|2 Account and Access changes in v1.0.78]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-08-03-the-allow-all-auto-safety-judge-model-is-no-longer-user-configurable-the-judge-m|The /allow-all auto safety-judge model is no longer user-configurable]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-08-03-2-interface-experience-changes-in-v1-0-78|2 Interface Experience changes in v1.0.78]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-08-03-3-safety-and-privacy-changes-in-v1-0-78|3 Safety and Privacy changes in v1.0.78]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-08-03-2-developer-workflow-changes-in-v1-0-78|2 Developer Workflow changes in v1.0.78]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-08-03-9-other-changes-in-v1-0-78|9 other changes in v1.0.78]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-07-31 · Google Antigravity · [[Changes/Google Antigravity/2026-07-31-2-reliability-and-performance-changes-in-hub-v2-5-0-enterprise-sign-in-gemini|2 Reliability and Performance changes in HUB v2.5.0 — Enterprise sign-in: Gemini…]]
- Later: 2026-08-04 · Ollama · [[Changes/Ollama/2026-08-04-qwen3-5-is-faster-on-apple-gpus-the-mlx-engine-now-uses-the-model-s-mtp-head-for|Qwen3.5 is faster on Apple GPUs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-08-03-661438&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-08-03-resuming-a-long-session-is-dramatically-faster-and-far-lighter-on-memory-because.md%0ACard%20ID%3A%20github-copilot-cli-2026-08-03-661438%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.78%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->