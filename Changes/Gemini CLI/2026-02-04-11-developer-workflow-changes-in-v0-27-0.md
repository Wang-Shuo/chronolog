---
card_id: gemini-cli-2026-02-04-6e2a80
date: '2026-02-04'
description: 'Gemini CLI · 2026-02-04 · Developer Workflow: 11 changes in Release
  v0.27.0 — Support command/ctrl/alt backspace correctly by @scidomino in…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2703
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e9cfdb68785b1e6003cf9cca93fdcf8ac0a71e70c78e7143cda36fb30ce84c06
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-02-04-6e2a80
  comparison: ''
  date: '2026-02-04'
  description: 'Gemini CLI — Release v0.27.0: 11 Developer Workflow changes'
  evidence:
  - quote: Support command/ctrl/alt backspace correctly by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17175
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(cli): consolidate shell inactivity and redirection monitoring by
      @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/17086'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat: implement /rewind command by @Adib234 in https://github.com/google-gemini/gemini-cli/pull/15720'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Sanitize command names and descriptions by @ehedlund in https://github.com/google-gemini/gemini-cli/pull/17228
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(ui): display user tier in about command by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/17400'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(workflow): add stale pull request closer with linked-issue enforcement
      by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/17449'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(core): optimize shell tool llmContent output format by @SandyTao520
      in https://github.com/google-gemini/gemini-cli/pull/17538'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Slash command for helping in debugging by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/17609
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(cli): add oncall command for issue triage by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/17661'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(ui): add terminal cursor support by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/17711'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat: add review-frontend-and-fix command by @galz10 in https://github.com/google-gemini/gemini-cli/pull/17707'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 11-developer-workflow-changes-in-v0-27-0
  source_release: gemini-cli-2026-02-04-v0-27-0-github-282779403-9d866835
  source_type: github_releases
  theme: developer-workflow
  title: 11 Developer Workflow changes in v0.27.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-04-reduced-layout-jitter-in-the-terminal-when-the-spinner-appears-and-disappears-du|Reduced
  layout jitter in the terminal when the spinner appears and disappears during…]]'
- '[[Changes/Codex CLI/2026-02-04-10-developer-workflow-changes-in-rust-v0-95-0|10
  Developer Workflow changes in rust-v0.95.0]]'
- '[[Changes/Codex CLI/2026-02-04-constrained-requirement-values-now-include-source-provenance-enabling-source-awa|Constrained
  requirement values now include source provenance, enabling source-aware…]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-02-04-v0-27-0-github-282779403-9d866835|gemini-cli-2026-02-04-v0-27-0-github-282779403-9d866835]]'
source_type: github_releases
theme: developer-workflow
title: 11 Developer Workflow changes in v0.27.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Developer Workflow changes in v0.27.0

**Gemini CLI** · 2026-02-04 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0) · from [[Releases/Gemini CLI/gemini-cli-2026-02-04-v0-27-0-github-282779403-9d866835|Release v0.27.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Support command/ctrl/alt backspace correctly by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17175

> feat(cli): consolidate shell inactivity and redirection monitoring by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/17086

> feat: implement /rewind command by @Adib234 in https://github.com/google-gemini/gemini-cli/pull/15720

> Sanitize command names and descriptions by @ehedlund in https://github.com/google-gemini/gemini-cli/pull/17228

> feat(ui): display user tier in about command by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/17400

> feat(workflow): add stale pull request closer with linked-issue enforcement by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/17449

> feat(core): optimize shell tool llmContent output format by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/17538

> Slash command for helping in debugging by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/17609

> feat(cli): add oncall command for issue triage by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/17661

> feat(ui): add terminal cursor support by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/17711

> feat: add review-frontend-and-fix command by @galz10 in https://github.com/google-gemini/gemini-cli/pull/17707

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-02-04-14-apps-and-integrations-changes-in-v0-27-0|14 Apps and Integrations changes in v0.27.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-02-04-4-interface-experience-changes-in-v0-27-0|4 Interface Experience changes in v0.27.0]] · Interface Experience
- [[Changes/Gemini CLI/2026-02-04-security-hooks-wrap-hook-injected-context-in-distinct-xml-tags-by-yunaseoul-in-h|security(hooks): Wrap hook-injected context in distinct XML tags]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-02-04-4-editor-experience-changes-in-v0-27-0|4 Editor Experience changes in v0.27.0]] · Editor Experience
- [[Changes/Gemini CLI/2026-02-04-3-automation-and-scheduling-changes-in-v0-27-0|3 Automation and Scheduling changes in v0.27.0]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-02-04-6-model-support-changes-in-v0-27-0|6 Model Support changes in v0.27.0]] · Model Support
- [[Changes/Gemini CLI/2026-02-04-15-agent-mode-changes-in-v0-27-0|15 Agent Mode changes in v0.27.0]] · Agent Mode
- [[Changes/Gemini CLI/2026-02-04-72-other-changes-in-v0-27-0|72 other changes in v0.27.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-02-04 · Codex CLI · [[Changes/Codex CLI/2026-02-04-constrained-requirement-values-now-include-source-provenance-enabling-source-awa|Constrained requirement values now include source provenance, enabling source-aware…]]
- Later: 2026-02-04 · OpenCode · [[Changes/OpenCode/2026-02-04-6-developer-workflow-changes-in-v1-1-50|6 Developer Workflow changes in v1.1.50]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-02-04-6e2a80&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-02-04-11-developer-workflow-changes-in-v0-27-0.md%0ACard%20ID%3A%20gemini-cli-2026-02-04-6e2a80%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.27.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->