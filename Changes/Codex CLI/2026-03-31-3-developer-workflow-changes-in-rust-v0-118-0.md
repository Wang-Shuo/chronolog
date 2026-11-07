---
card_id: codex-cli-2026-03-31-81006a
date: '2026-03-31'
description: 'Codex CLI · 2026-03-31 · Developer Workflow: 3 changes in 0.118.0 —
  `codex exec` now supports the prompt-plus-stdin workflow, so you can pipe input
  and still…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2758
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 46ccdea84b77b22b197786fa59ef52bfaba6ebde3bfc878d3578dfc290ef2ec7
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-31-81006a
  comparison: ''
  date: '2026-03-31'
  description: 'Codex CLI — 0.118.0: 3 Developer Workflow changes'
  evidence:
  - quote: '`codex exec` now supports the prompt-plus-stdin workflow, so you can pipe
      input and still pass a separate prompt on the command line. (#15917)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#15906 chore: remove skill metadata from command approval payloads @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  - quote: '#16118 fix: fix comment linter lint violations in Linux-only code @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.118.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-developer-workflow-changes-in-rust-v0-118-0
  source_release: codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6
  source_type: github_releases
  theme: developer-workflow
  title: 3 Developer Workflow changes in rust-v0.118.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-03-29-10-developer-workflow-changes-in-v1-3-6-2|10 Developer
  Workflow changes in v1.3.6 + 2]]'
- '[[Changes/GitHub Copilot CLI/2026-03-30-2-developer-workflow-changes-in-v1-0-13|2
  Developer Workflow changes in v1.0.13]]'
- '[[Changes/OpenCode/2026-03-30-2-developer-workflow-changes-in-v1-3-9-1|2 Developer
  Workflow changes in v1.3.9 + 1]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6|codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6]]'
source_type: github_releases
theme: developer-workflow
title: 3 Developer Workflow changes in rust-v0.118.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Developer Workflow changes in rust-v0.118.0

**Codex CLI** · 2026-03-31 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.118.0) · from [[Releases/Codex CLI/codex-cli-2026-03-31-rust-v0-118-0-github-303805427-02df59b6|0.118.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `codex exec` now supports the prompt-plus-stdin workflow, so you can pipe input and still pass a separate prompt on the command line. (#15917)

> #15906 chore: remove skill metadata from command approval payloads @bolinfest

> #16118 fix: fix comment linter lint violations in Linux-only code @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.118.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-31-16286-auth-generalize-external-auth-tokens-for-bearer-only-sources-bolinfest|♯16286 auth: generalize external auth tokens for bearer-only sources @bolinfest]] · Context Window
- [[Changes/Codex CLI/2026-03-31-16021-fix-copy-regression-in-tui-app-server-turn-completion-etraut-openai|♯16021 Fix /copy regression in tui_app_server turn completion @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-03-31-12-apps-and-integrations-changes-in-rust-v0-118-0|12 Apps and Integrations changes in rust-v0.118.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-31-16114-remove-tui-voice-transcription-feature-etraut-openai|♯16114 Remove TUI voice transcription feature @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-31-3-interface-experience-changes-in-rust-v0-118-0|3 Interface Experience changes in rust-v0.118.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-31-4-account-and-access-changes-in-rust-v0-118-0|4 Account and Access changes in rust-v0.118.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-31-15934-add-usage-based-business-plan-types-bwanner-oai|♯15934 Add usage-based business plan types @bwanner-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-03-31-7-safety-and-privacy-changes-in-rust-v0-118-0|7 Safety and Privacy changes in rust-v0.118.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-31-4-agent-mode-changes-in-rust-v0-118-0|4 Agent Mode changes in rust-v0.118.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-31-7-mobile-and-desktop-changes-in-rust-v0-118-0|7 Mobile and Desktop changes in rust-v0.118.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-31-4-collaboration-changes-in-rust-v0-118-0|4 Collaboration changes in rust-v0.118.0]] · Collaboration
- [[Changes/Codex CLI/2026-03-31-5-model-support-changes-in-rust-v0-118-0|5 Model Support changes in rust-v0.118.0]] · Model Support
- [[Changes/Codex CLI/2026-03-31-51-other-changes-in-rust-v0-118-0|51 other changes in rust-v0.118.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-30 · OpenCode · [[Changes/OpenCode/2026-03-30-2-developer-workflow-changes-in-v1-3-9-1|2 Developer Workflow changes in v1.3.9 + 1]]
- Later: 2026-03-31 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-31-4-developer-workflow-changes-in-v1-0-14|4 Developer Workflow changes in v1.0.14]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-31-81006a&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-31-3-developer-workflow-changes-in-rust-v0-118-0.md%0ACard%20ID%3A%20codex-cli-2026-03-31-81006a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.118.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->