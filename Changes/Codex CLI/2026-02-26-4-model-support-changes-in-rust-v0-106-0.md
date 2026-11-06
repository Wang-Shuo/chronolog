---
card_id: codex-cli-2026-02-26-911eab
date: '2026-02-26'
description: 'Codex CLI · 2026-02-26 · Model Support: 4 changes in 0.106.0 — Made
  `5.3-codex` visible in the CLI model list for API users (#12808)'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1144
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b3c3cfc99f1710652d9e819df2a110f0dbe09a3abf86af82a9c3040d5508e359
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-26-911eab
  comparison: ''
  date: '2026-02-26'
  description: 'Codex CLI — 0.106.0: 4 Model Support changes'
  evidence:
  - quote: Made `5.3-codex` visible in the CLI model list for API users (#12808)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: 'Improved realtime websocket reliability by retrying timeout-related HTTP
      400 handshake failures and preferring WebSocket v2 when supported by the selected
      model (#12791, #12838)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12838 Use websocket v2 as model-preferred websocket protocol @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12873 Use model catalog default for reasoning summary fallback @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-model-support-changes-in-rust-v0-106-0
  source_release: codex-cli-2026-02-26-rust-v0-106-0-github-291146451-379358db
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in rust-v0.106.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-02-25-6-model-support-changes-in-rust-v0-105-0|6 Model
  Support changes in rust-v0.105.0]]'
- '[[Changes/Gemini CLI/2026-02-25-8-model-support-changes-in-v0-30-0|8 Model Support
  changes in v0.30.0]]'
- '[[Changes/Windsurf/2026-02-25-new-model-picker|New Model Picker]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-26-rust-v0-106-0-github-291146451-379358db|codex-cli-2026-02-26-rust-v0-106-0-github-291146451-379358db]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in rust-v0.106.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in rust-v0.106.0

**Codex CLI** · 2026-02-26 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.106.0) · from [[Releases/Codex CLI/codex-cli-2026-02-26-rust-v0-106-0-github-291146451-379358db|0.106.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Made `5.3-codex` visible in the CLI model list for API users (#12808)

> Improved realtime websocket reliability by retrying timeout-related HTTP 400 handshake failures and preferring WebSocket v2 when supported by the selected model (#12791, #12838)

> #12838 Use websocket v2 as model-preferred websocket protocol @pakrym-oai

> #12873 Use model catalog default for reasoning summary fallback @pakrym-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.106.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-26-2-account-and-access-changes-in-rust-v0-106-0|2 Account and Access changes in rust-v0.106.0]] · Account and Access
- [[Changes/Codex CLI/2026-02-26-5-agent-mode-changes-in-rust-v0-106-0|5 Agent Mode changes in rust-v0.106.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-26-2-collaboration-changes-in-rust-v0-106-0|2 Collaboration changes in rust-v0.106.0]] · Collaboration
- [[Changes/Codex CLI/2026-02-26-improved-tui-local-file-link-rendering-to-hide-absolute-paths-while-preserving-v|Improved TUI local file-link rendering to hide absolute paths while preserving…]] · Interface Experience
- [[Changes/Codex CLI/2026-02-26-12417-core-bundle-settings-diff-updates-into-one-dev-user-envelope-charley-oai|♯12417 core: bundle settings diff updates into one dev/user envelope @charley-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-02-26-3-memory-and-personalization-changes-in-rust-v0-106-0|3 Memory and Personalization changes in rust-v0.106.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-26-2-mobile-and-desktop-changes-in-rust-v0-106-0|2 Mobile and Desktop changes in rust-v0.106.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-26-12800-fix-enforce-sandbox-envelope-for-zsh-fork-execution-bolinfest|♯12800 fix: enforce sandbox envelope for zsh fork execution @bolinfest]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-26-12758-feat-include-available-decisions-in-command-approval-requests-bolinfest|♯12758 feat: include available decisions in command approval requests @bolinfest]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-26-2-reliability-and-performance-changes-in-rust-v0-106-0|2 Reliability and Performance changes in rust-v0.106.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-02-26-36-other-changes-in-rust-v0-106-0|36 other changes in rust-v0.106.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-02-25 · Windsurf · [[Changes/Windsurf/2026-02-25-new-model-picker|New Model Picker]]
- Later: 2026-02-27 · Cline · [[Changes/Cline/2026-02-27-4-model-support-changes-in-v3-68-0|4 Model Support changes in v3.68.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-26-911eab&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-26-4-model-support-changes-in-rust-v0-106-0.md%0ACard%20ID%3A%20codex-cli-2026-02-26-911eab%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.106.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->