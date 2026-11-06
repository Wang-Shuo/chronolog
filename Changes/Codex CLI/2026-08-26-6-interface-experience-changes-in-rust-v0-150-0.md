---
card_id: codex-cli-2026-08-26-045b0f
date: '2026-08-26'
description: 'Codex CLI · 2026-08-26 · Interface Experience: 6 changes in 0.150.0
  — `/copy` now offers a picker for full responses, individual code blocks, and blockquotes…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1325
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d8f07ced1428b0b1a4d32f4ac93f31f3b60524071bc0a46f908379b98c1cffa4
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-26-045b0f
  comparison: ''
  date: '2026-08-26'
  description: 'Codex CLI — 0.150.0: 6 Interface Experience changes'
  evidence:
  - quote: '`/copy` now offers a picker for full responses, individual code blocks,
      and blockquotes. (#39997)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39702 Wait for turn completion events in multi-agent resume tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39795 Add hostname to the configurable TUI status line @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39985 Truncate Guardian instructions after rendering the policy @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39997 Add a response target picker to `/copy` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40449 Route peer agent completion activity to the initiating turn @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-interface-experience-changes-in-rust-v0-150-0
  source_release: codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c
  source_type: github_releases
  theme: interface-experience
  title: 6 Interface Experience changes in rust-v0.150.0
  type: change
related_changes:
- '[[Changes/Windsurf/2026-08-21-devin-cloud|Devin Cloud]]'
- '[[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-23954-add-trailing-space-to-autocomplete-suggestions-by-jone|SSR
  Agent Issue Fix (23954): Add trailing space to autocomplete suggestions]]'
- '[[Changes/Claude Code/2026-08-26-changed-the-prompt-footer-pr-badge-to-skip-its-github-re-check-on-terminal-refoc|Changed
  the prompt-footer PR badge to skip its GitHub re-check on terminal refocus…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c|codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c]]'
source_type: github_releases
theme: interface-experience
title: 6 Interface Experience changes in rust-v0.150.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Interface Experience changes in rust-v0.150.0

**Codex CLI** · 2026-08-26 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.150.0) · from [[Releases/Codex CLI/codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c|0.150.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `/copy` now offers a picker for full responses, individual code blocks, and blockquotes. (#39997)

> #39702 Wait for turn completion events in multi-agent resume tests @copyberry

> #39795 Add hostname to the configurable TUI status line @copyberry

> #39985 Truncate Guardian instructions after rendering the policy @copyberry

> #39997 Add a response target picker to `/copy` @copyberry

> #40449 Route peer agent completion activity to the initiating turn @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.150.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-26-39953-support-voice-aware-configuration-and-version-skew-builds-copyberry|♯39953 Support voice-aware configuration and version-skew builds @copyberry]] · Voice and Audio
- [[Changes/Codex CLI/2026-08-26-10-model-support-changes-in-rust-v0-150-0|10 Model Support changes in rust-v0.150.0]] · Model Support
- [[Changes/Codex CLI/2026-08-26-24-apps-and-integrations-changes-in-rust-v0-150-0|24 Apps and Integrations changes in rust-v0.150.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-26-15-developer-workflow-changes-in-rust-v0-150-0|15 Developer Workflow changes in rust-v0.150.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-26-40544-include-transparent-background-in-image-generation-analytics-copyberry|♯40544 Include transparent background in image generation analytics @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-26-14-agent-mode-changes-in-rust-v0-150-0|14 Agent Mode changes in rust-v0.150.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-26-12-safety-and-privacy-changes-in-rust-v0-150-0|12 Safety and Privacy changes in rust-v0.150.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-26-2-account-and-access-changes-in-rust-v0-150-0|2 Account and Access changes in rust-v0.150.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-26-39811-restrict-macos-preference-reads-to-full-disk-policies-copyberry|♯39811 Restrict macOS preference reads to full-disk policies @copyberry]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-26-40488-export-turn-cost-as-an-otel-metric-copyberry|♯40488 Export turn cost as an OTEL metric @copyberry]] · Pricing Model
- [[Changes/Codex CLI/2026-08-26-3-memory-and-personalization-changes-in-rust-v0-150-0|3 Memory and Personalization changes in rust-v0.150.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-08-26-40436-add-a-managed-gate-for-in-app-local-automation-copyberry|♯40436 Add a managed gate for in-app local automation @copyberry]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-08-26-14-context-window-changes-in-rust-v0-150-0|14 Context Window changes in rust-v0.150.0]] · Context Window
- [[Changes/Codex CLI/2026-08-26-110-other-changes-in-rust-v0-150-0|110 other changes in rust-v0.150.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-08-26 · Claude Code · [[Changes/Claude Code/2026-08-26-changed-the-prompt-footer-pr-badge-to-skip-its-github-re-check-on-terminal-refoc|Changed the prompt-footer PR badge to skip its GitHub re-check on terminal refocus…]]
- Later: 2026-08-27 · Claude Code · [[Changes/Claude Code/2026-08-27-2-interface-experience-changes-in-v2-1-248|2 Interface Experience changes in v2.1.248]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-26-045b0f&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-26-6-interface-experience-changes-in-rust-v0-150-0.md%0ACard%20ID%3A%20codex-cli-2026-08-26-045b0f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.150.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->