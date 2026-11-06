---
card_id: codex-cli-2026-01-09-a2339d
date: '2026-01-09'
description: 'Codex CLI · 2026-01-09 · Developer Workflow: 4 changes in 0.80.0 — Git
  apply path parsing now handles quoted/escaped paths and `/dev/null` correctly to
  avoid…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1028
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b90f245c3e62b886c78a5c46c33ae4ff6796386dcf6c57f5eba4c538761fb9a0
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-09-a2339d
  comparison: ''
  date: '2026-01-09'
  description: 'Codex CLI — 0.80.0: 4 Developer Workflow changes'
  evidence:
  - quote: Git apply path parsing now handles quoted/escaped paths and `/dev/null`
      correctly to avoid misclassified changes. (#8824)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8824 fix: parse git apply paths correctly @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8894 chore: add small debug client @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8931 fix: correct login shell mismatch in the accept_elicitation_for_prompt_rule()
      test @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-developer-workflow-changes-in-rust-v0-80-0
  source_release: codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf
  source_type: github_releases
  theme: developer-workflow
  title: 4 Developer Workflow changes in rust-v0.80.0
  type: change
related_changes:
- '[[Changes/Cursor/2026-01-08-3-developer-workflow-changes-in-new-cli-features-and-improved-cli|3
  Developer Workflow changes in New CLI Features and Improved CLI…]]'
- '[[Changes/Claude Code/2026-01-09-improved-slash-command-suggestion-readability-by-truncating-long-descriptions-to|Improved
  slash command suggestion readability by truncating long descriptions to 2 lines]]'
- '[[Changes/Claude Code/2026-01-09-4-developer-workflow-changes-in-v2-1-2|4 Developer
  Workflow changes in v2.1.2]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf|codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf]]'
source_type: github_releases
theme: developer-workflow
title: 4 Developer Workflow changes in rust-v0.80.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Developer Workflow changes in rust-v0.80.0

**Codex CLI** · 2026-01-09 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.80.0) · from [[Releases/Codex CLI/codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf|0.80.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Git apply path parsing now handles quoted/escaped paths and `/dev/null` correctly to avoid misclassified changes. (#8824)

> #8824 fix: parse git apply paths correctly @tibo-openai

> #8894 chore: add small debug client @jif-oai

> #8931 fix: correct login shell mismatch in the accept_elicitation_for_prompt_rule() test @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.80.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-09-2-apps-and-integrations-changes-in-rust-v0-80-0|2 Apps and Integrations changes in rust-v0.80.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-09-2-agent-mode-changes-in-rust-v0-80-0|2 Agent Mode changes in rust-v0.80.0]] · Agent Mode
- [[Changes/Codex CLI/2026-01-09-codex-cli-subprocesses-again-inherit-env-vars-like-ld-library-path-dyld-library|Codex CLI subprocesses again inherit env vars like…]] · Reliability and Performance
- [[Changes/Codex CLI/2026-01-09-8939-chore-move-app-server-tests-from-chat-completion-to-responses-celia-oai|♯8939 chore move app server tests from chat completion to responses @celia-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-01-09-app-server-readme-now-documents-skills-support-and-usage-8853|App-server README now documents skills support and usage]] · Files and Data
- [[Changes/Codex CLI/2026-01-09-2-mobile-and-desktop-changes-in-rust-v0-80-0|2 Mobile and Desktop changes in rust-v0.80.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-09-4-model-support-changes-in-rust-v0-80-0|4 Model Support changes in rust-v0.80.0]] · Model Support
- [[Changes/Codex CLI/2026-01-09-3-interface-experience-changes-in-rust-v0-80-0|3 Interface Experience changes in rust-v0.80.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-09-2-safety-and-privacy-changes-in-rust-v0-80-0|2 Safety and Privacy changes in rust-v0.80.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-09-62-other-changes-in-rust-v0-80-0|62 other changes in rust-v0.80.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-01-09 · Claude Code · [[Changes/Claude Code/2026-01-09-4-developer-workflow-changes-in-v2-1-2|4 Developer Workflow changes in v2.1.2]]
- Later: 2026-01-09 · Open WebUI · [[Changes/Open WebUI/2026-01-09-24-developer-workflow-changes-in-v0-7-0|24 Developer Workflow changes in v0.7.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-09-a2339d&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-09-4-developer-workflow-changes-in-rust-v0-80-0.md%0ACard%20ID%3A%20codex-cli-2026-01-09-a2339d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.80.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->