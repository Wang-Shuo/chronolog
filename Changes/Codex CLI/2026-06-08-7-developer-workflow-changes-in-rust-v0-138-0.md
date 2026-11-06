---
card_id: codex-cli-2026-06-08-82a298
date: '2026-06-08'
description: 'Codex CLI · 2026-06-08 · Developer Workflow: 7 changes in 0.138.0 —
  Goal workflows are more predictable: multiline paste in `/goal edit` no longer submits…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1178
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 900897cdef60a5f5420f2133114326891fb0d8d8b89cdeaaad6ab7d298716e5a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-08-82a298
  comparison: ''
  date: '2026-06-08'
  description: 'Codex CLI — 0.138.0: 7 Developer Workflow changes'
  evidence:
  - quote: 'Goal workflows are more predictable: multiline paste in `/goal edit` no
      longer submits early, idle auto-turns stay out of Plan mode, and goals stop
      auto-continuing after terminal turn failures. (#26047, #26147, #26690)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26175 feat: guard git enrichment @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26480 [codex] Add environment shell info @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26538 [codex] Add /usr/bin/bash shell fallback @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26669 [codex] Bound WSL local curated discovery @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26690 Block active goals after terminal turn errors @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26013 [codex] Gate terminal visualization instructions in TUI @vie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-developer-workflow-changes-in-rust-v0-138-0
  source_release: codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a
  source_type: github_releases
  theme: developer-workflow
  title: 7 Developer Workflow changes in rust-v0.138.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-06-05-11-developer-workflow-changes-in-v1-0-60|11
  Developer Workflow changes in v1.0.60]]'
- '[[Changes/Cline/2026-06-07-add-a-debug-section-in-settings-for-cline-testers|Add
  a debug section in settings for Cline testers]]'
- '[[Changes/Claude Code/2026-06-08-background-sessions-are-now-told-that-shared-checkout-edits-are-blocked-until-th|Background
  sessions are now told that shared-checkout edits are blocked until they…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a|codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a]]'
source_type: github_releases
theme: developer-workflow
title: 7 Developer Workflow changes in rust-v0.138.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Developer Workflow changes in rust-v0.138.0

**Codex CLI** · 2026-06-08 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.138.0) · from [[Releases/Codex CLI/codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a|0.138.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Goal workflows are more predictable: multiline paste in `/goal edit` no longer submits early, idle auto-turns stay out of Plan mode, and goals stop auto-continuing after terminal turn failures. (#26047, #26147, #26690)

> #26175 feat: guard git enrichment @jif-oai

> #26480 [codex] Add environment shell info @pakrym-oai

> #26538 [codex] Add /usr/bin/bash shell fallback @pakrym-oai

> #26669 [codex] Bound WSL local curated discovery @xl-openai

> #26690 Block active goals after terminal turn errors @etraut-openai

> #26013 [codex] Gate terminal visualization instructions in TUI @vie-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.138.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-08-6-safety-and-privacy-changes-in-rust-v0-138-0|6 Safety and Privacy changes in rust-v0.138.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-08-2-image-generation-changes-in-rust-v0-138-0|2 Image Generation changes in rust-v0.138.0]] · Image Generation
- [[Changes/Codex CLI/2026-06-08-4-mobile-and-desktop-changes-in-rust-v0-138-0|4 Mobile and Desktop changes in rust-v0.138.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-08-2-account-and-access-changes-in-rust-v0-138-0|2 Account and Access changes in rust-v0.138.0]] · Account and Access
- [[Changes/Codex CLI/2026-06-08-19-apps-and-integrations-changes-in-rust-v0-138-0|19 Apps and Integrations changes in rust-v0.138.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-08-6-model-support-changes-in-rust-v0-138-0|6 Model Support changes in rust-v0.138.0]] · Model Support
- [[Changes/Codex CLI/2026-06-08-4-context-window-changes-in-rust-v0-138-0|4 Context Window changes in rust-v0.138.0]] · Context Window
- [[Changes/Codex CLI/2026-06-08-8-agent-mode-changes-in-rust-v0-138-0|8 Agent Mode changes in rust-v0.138.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-08-3-editor-experience-changes-in-rust-v0-138-0|3 Editor Experience changes in rust-v0.138.0]] · Editor Experience
- [[Changes/Codex CLI/2026-06-08-54-other-changes-in-rust-v0-138-0|54 other changes in rust-v0.138.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-06-08 · Claude Code · [[Changes/Claude Code/2026-06-08-background-sessions-are-now-told-that-shared-checkout-edits-are-blocked-until-th|Background sessions are now told that shared-checkout edits are blocked until they…]]
- Later: 2026-06-09 · Codex CLI · [[Changes/Codex CLI/2026-06-09-release-builds-once-again-publish-separate-symbol-archives-with-line-tables-impr|Release builds once again publish separate symbol archives with line tables…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-08-82a298&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-08-7-developer-workflow-changes-in-rust-v0-138-0.md%0ACard%20ID%3A%20codex-cli-2026-06-08-82a298%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.138.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->