---
card_id: codex-cli-2026-02-05-f0c7c8
date: '2026-02-05'
description: 'Codex CLI · 2026-02-05 · Other changes: 18 changes in 0.97.0 — Added
  live skill update detection, so skill file changes are picked up without restarting…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: da0616e2729a6cf4d93819d6ad90710180e3642449c4c57504f9e188ceaa9008
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-05-f0c7c8
  comparison: ''
  date: '2026-02-05'
  description: 'Codex CLI — 0.97.0: 18 other changes'
  evidence:
  - quote: Added live skill update detection, so skill file changes are picked up
      without restarting. (#10478)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: Added configurable `log_dir` so logs can be redirected (including via `-c`
      overrides) more easily. (#10678)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: 'Improved cloud requirements reliability with higher timeouts, retries,
      and corrected precedence over MDM settings. (#10631, #10633, #10659)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: Persisted pending-input user events more consistently for mid-turn injected
      input handling. (#10656)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: Documented how to opt in to the experimental app-server API. (#10667)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: Updated docs/schema coverage for new `log_dir` configuration behavior.
      (#10678)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10595 Stop client from being state carrier @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10644 fix: flaky test @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10629 feat: add phase 1 mem client @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10633 Cloud Requirements: take precedence over MDM @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10659 Increase cloud req timeout @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10656 Persist pending input user events @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10634 feat: add phase 1 mem db @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10478 Added support for live updates to skills @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10567 feat(app-server, core): allow text + image content items for dynamic
      tool outputs @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10678 feat(core): add configurable log_dir @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10631 Cloud Requirements: increase timeout and retries @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  - quote: '#10701 fix(tui): restore working shimmer after preamble output @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.97.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 18-other-changes-in-rust-v0-97-0
  source_release: codex-cli-2026-02-05-rust-v0-97-0-github-283219180-522ab2d0
  source_type: github_releases
  theme: uncategorized
  title: 18 other changes in rust-v0.97.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-05-rust-v0-97-0-github-283219180-522ab2d0|codex-cli-2026-02-05-rust-v0-97-0-github-283219180-522ab2d0]]'
source_type: github_releases
theme: uncategorized
title: 18 other changes in rust-v0.97.0
type: change
---

<!-- chronolog:begin region="header" -->
# 18 other changes in rust-v0.97.0

**Codex CLI** · 2026-02-05 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.97.0) · from [[Releases/Codex CLI/codex-cli-2026-02-05-rust-v0-97-0-github-283219180-522ab2d0|0.97.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added live skill update detection, so skill file changes are picked up without restarting. (#10478)

> Added configurable `log_dir` so logs can be redirected (including via `-c` overrides) more easily. (#10678)

> Improved cloud requirements reliability with higher timeouts, retries, and corrected precedence over MDM settings. (#10631, #10633, #10659)

> Persisted pending-input user events more consistently for mid-turn injected input handling. (#10656)

> Documented how to opt in to the experimental app-server API. (#10667)

> Updated docs/schema coverage for new `log_dir` configuration behavior. (#10678)

> #10595 Stop client from being state carrier @pakrym-oai

> #10644 fix: flaky test @jif-oai

> #10629 feat: add phase 1 mem client @jif-oai

> #10633 Cloud Requirements: take precedence over MDM @gt-oai

> #10659 Increase cloud req timeout @gt-oai

> #10656 Persist pending input user events @aibrahim-oai

> #10634 feat: add phase 1 mem db @jif-oai

> #10478 Added support for live updates to skills @etraut-openai

> #10567 feat(app-server, core): allow text + image content items for dynamic tool outputs @owenlin0

> #10678 feat(core): add configurable log_dir @joshka-oai

> #10631 Cloud Requirements: increase timeout and retries @gt-oai

> #10701 fix(tui): restore working shimmer after preamble output @joshka-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.97.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-05-4-memory-and-personalization-changes-in-rust-v0-97-0|4 Memory and Personalization changes in rust-v0.97.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-05-2-model-support-changes-in-rust-v0-97-0|2 Model Support changes in rust-v0.97.0]] · Model Support
- [[Changes/Codex CLI/2026-02-05-2-developer-workflow-changes-in-rust-v0-97-0|2 Developer Workflow changes in rust-v0.97.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-05-10649-fix-test-shell-command-interruption-flake-gt-oai|♯10649 Fix test_shell_command_interruption flake @gt-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-02-05-6-apps-and-integrations-changes-in-rust-v0-97-0|6 Apps and Integrations changes in rust-v0.97.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-05-2-safety-and-privacy-changes-in-rust-v0-97-0|2 Safety and Privacy changes in rust-v0.97.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-05-10667-chore-app-server-document-experimental-api-opt-in-owenlin0|♯10667 chore(app-server): document experimental API opt-in @owenlin0]] · Files and Data
- [[Changes/Codex CLI/2026-02-05-2-interface-experience-changes-in-rust-v0-97-0|2 Interface Experience changes in rust-v0.97.0]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-05-f0c7c8&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-05-18-other-changes-in-rust-v0-97-0.md%0ACard%20ID%3A%20codex-cli-2026-02-05-f0c7c8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.97.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->