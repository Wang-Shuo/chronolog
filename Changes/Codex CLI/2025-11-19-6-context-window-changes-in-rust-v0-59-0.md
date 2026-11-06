---
card_id: codex-cli-2025-11-19-ab8bbc
date: '2025-11-19'
description: 'Codex CLI · 2025-11-19 · Context Window: 6 changes in 0.59.0 — Expanded
  Tool Token Limits: codex models now support up to 10,000 tool output tokens. Configure…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 930
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fb6d455ff491575e768279b733508aff7dfcb73a07c51dc3a68bdce40eccd000
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-11-19-ab8bbc
  comparison: ''
  date: '2025-11-19'
  description: 'Codex CLI — 0.59.0: 6 Context Window changes'
  evidence:
  - quote: 'Expanded Tool Token Limits: codex models now support up to 10,000 tool
      output tokens. Configure this via `tool_output_token_limit` in `config.toml`.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: 'chore: consolidate compaction token usage (#6894) — @jif'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: Run remote auto compaction (#6879) — @pakrym
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: Remote compaction on by-default (#6866) — @pakrym
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: Add the utility to truncate by tokens (#6746) — @aibrahim
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: 'feat: remote compaction (#6795) — @jif'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-context-window-changes-in-rust-v0-59-0
  source_release: codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7
  source_type: github_releases
  theme: context-window
  title: 6 Context Window changes in rust-v0.59.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-11-13-6597-feat-proxy-context-left-after-compaction-2a417c47a|♯6597
  — feat: proxy context left after compaction (2a417c47a)]]'
- '[[Changes/GitHub Copilot CLI/2025-11-17-support-adding-images-to-context-via-drag-dropping-and-pasting-paths-to-image-fi|Support
  adding images to context via drag & dropping and pasting paths to image files]]'
- '[[Changes/Cline/2025-11-18-feat-bedrock-add-context-window-error-detection-and-retry-handling-by-arafatkatz|feat(bedrock):
  add context window error detection and retry handling]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7|codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7]]'
source_type: github_releases
theme: context-window
title: 6 Context Window changes in rust-v0.59.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Context Window changes in rust-v0.59.0

**Codex CLI** · 2025-11-19 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.59.0) · from [[Releases/Codex CLI/codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7|0.59.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Expanded Tool Token Limits: codex models now support up to 10,000 tool output tokens. Configure this via `tool_output_token_limit` in `config.toml`.

> chore: consolidate compaction token usage (#6894) — @jif

> Run remote auto compaction (#6879) — @pakrym

> Remote compaction on by-default (#6866) — @pakrym

> Add the utility to truncate by tokens (#6746) — @aibrahim

> feat: remote compaction (#6795) — @jif

Source: https://github.com/openai/codex/releases/tag/rust-v0.59.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-11-19-handle-don-t-trust-directory-selection-in-onboarding-4941-viniciusmotta8|Handle "Don't Trust" directory selection in onboarding (♯4941) — @viniciusmotta8]] · Interface Experience
- [[Changes/Codex CLI/2025-11-19-2-agent-mode-changes-in-rust-v0-59-0|2 Agent Mode changes in rust-v0.59.0]] · Agent Mode
- [[Changes/Codex CLI/2025-11-19-native-compaction-support-added-first-class-support-for-compaction-improving-per|Native Compaction Support]] · Reliability and Performance
- [[Changes/Codex CLI/2025-11-19-bug-fix-rmcp-client-refresh-oauth-tokens-using-expires-at-6574-laelluo|:bug: fix(rmcp-client): refresh OAuth tokens using expires_at (♯6574) — @LaelLuo]] · Account and Access
- [[Changes/Codex CLI/2025-11-19-promote-shared-helpers-for-suite-tests-6460-aibrahim|Promote shared helpers for suite tests (♯6460) — @aibrahim]] · Collaboration
- [[Changes/Codex CLI/2025-11-19-15-developer-workflow-changes-in-rust-v0-59-0|15 Developer Workflow changes in rust-v0.59.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-11-19-3-mobile-and-desktop-changes-in-rust-v0-59-0|3 Mobile and Desktop changes in rust-v0.59.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-11-19-use-shared-network-gating-helper-in-chat-completion-tests-6461-aibrahim|Use shared network gating helper in chat completion tests (♯6461) — @aibrahim]] · Editor Experience
- [[Changes/Codex CLI/2025-11-19-5-model-support-changes-in-rust-v0-59-0|5 Model Support changes in rust-v0.59.0]] · Model Support
- [[Changes/Codex CLI/2025-11-19-5-apps-and-integrations-changes-in-rust-v0-59-0|5 Apps and Integrations changes in rust-v0.59.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-11-19-7-safety-and-privacy-changes-in-rust-v0-59-0|7 Safety and Privacy changes in rust-v0.59.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-11-19-credits-are-now-visible-in-status|Credits are now visible in /status]] · Pricing Model
- [[Changes/Codex CLI/2025-11-19-53-other-changes-in-rust-v0-59-0|53 other changes in rust-v0.59.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2025-11-18 · Cline · [[Changes/Cline/2025-11-18-feat-bedrock-add-context-window-error-detection-and-retry-handling-by-arafatkatz|feat(bedrock): add context window error detection and retry handling]]
- Later: 2025-11-20 · Codex CLI · [[Changes/Codex CLI/2025-11-20-ux-fixes-corrected-reasoning-display-preserved-review-footer-context-after-revie|UX fixes: corrected reasoning display, preserved review footer context after…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-11-19-ab8bbc&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-11-19-6-context-window-changes-in-rust-v0-59-0.md%0ACard%20ID%3A%20codex-cli-2025-11-19-ab8bbc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.59.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->