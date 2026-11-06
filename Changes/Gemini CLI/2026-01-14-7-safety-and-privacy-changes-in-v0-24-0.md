---
card_id: gemini-cli-2026-01-14-0cb091
date: '2026-01-14'
description: 'Gemini CLI · 2026-01-14 · Safety and Privacy: 7 changes in Release v0.24.0
  — feat(ui): Add security warning and improve layout for Hooks list by @SandyTao520…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1004
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3c761d6b6775901221e53b522032d5adedf3a1c653c1badc5bced504bb5d62da
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-01-14-0cb091
  comparison: ''
  date: '2026-01-14'
  description: 'Gemini CLI — Release v0.24.0: 7 Safety and Privacy changes'
  evidence:
  - quote: 'feat(ui): Add security warning and improve layout for Hooks list by @SandyTao520
      in https://github.com/google-gemini/gemini-cli/pull/15440'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: 'refactor(core): remove deprecated permission aliases from BeforeToolHookOutput
      by @StoyanD in https://github.com/google-gemini/gemini-cli/pull/14855'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: 'Security: Project-level hook warnings by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/15470'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: Add security docs by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15739
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: Unify shell security policy and remove legacy logic by @abhipatel12 in
      https://github.com/google-gemini/gemini-cli/pull/15770
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: 'Agent Skills: Extension Support & Security Disclosure by @NTaylorMullen
      in https://github.com/google-gemini/gemini-cli/pull/15834'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: 'fix(cli): mock fs.readdir in consent tests for Windows compatibility by
      @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15904'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 7-safety-and-privacy-changes-in-v0-24-0
  source_release: gemini-cli-2026-01-14-v0-24-0-github-276723271-62398547
  source_type: github_releases
  theme: safety-privacy
  title: 7 Safety and Privacy changes in v0.24.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-01-13-provide-inline-feedback-when-rejecting-tool-permission-requests-so-agents-don-t|Provide
  inline feedback when rejecting tool permission requests so agents don''t have…]]'
- '[[Changes/Claude Code/2026-01-14-2-safety-and-privacy-changes-in-v2-1-7|2 Safety
  and Privacy changes in v2.1.7]]'
- '[[Changes/Codex CLI/2026-01-14-5-safety-and-privacy-changes-in-rust-v0-81-0|5 Safety
  and Privacy changes in rust-v0.81.0]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-01-14-v0-24-0-github-276723271-62398547|gemini-cli-2026-01-14-v0-24-0-github-276723271-62398547]]'
source_type: github_releases
theme: safety-privacy
title: 7 Safety and Privacy changes in v0.24.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in v0.24.0

**Gemini CLI** · 2026-01-14 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0) · from [[Releases/Gemini CLI/gemini-cli-2026-01-14-v0-24-0-github-276723271-62398547|Release v0.24.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat(ui): Add security warning and improve layout for Hooks list by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/15440

> refactor(core): remove deprecated permission aliases from BeforeToolHookOutput by @StoyanD in https://github.com/google-gemini/gemini-cli/pull/14855

> Security: Project-level hook warnings by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/15470

> Add security docs by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15739

> Unify shell security policy and remove legacy logic by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15770

> Agent Skills: Extension Support & Security Disclosure by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15834

> fix(cli): mock fs.readdir in consent tests for Windows compatibility by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15904

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-01-14-10-agent-mode-changes-in-v0-24-0|10 Agent Mode changes in v0.24.0]] · Agent Mode
- [[Changes/Gemini CLI/2026-01-14-feat-add-folder-suggestions-to-dir-add-command-by-jackwotherspoon-in-https-githu|feat: add folder suggestions to /dir add command]] · Developer Workflow
- [[Changes/Gemini CLI/2026-01-14-9-apps-and-integrations-changes-in-v0-24-0|9 Apps and Integrations changes in v0.24.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-01-14-4-editor-experience-changes-in-v0-24-0|4 Editor Experience changes in v0.24.0]] · Editor Experience
- [[Changes/Gemini CLI/2026-01-14-6-model-support-changes-in-v0-24-0|6 Model Support changes in v0.24.0]] · Model Support
- [[Changes/Gemini CLI/2026-01-14-2-context-window-changes-in-v0-24-0|2 Context Window changes in v0.24.0]] · Context Window
- [[Changes/Gemini CLI/2026-01-14-38-other-changes-in-v0-24-0|38 other changes in v0.24.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-01-14 · Codex CLI · [[Changes/Codex CLI/2026-01-14-5-safety-and-privacy-changes-in-rust-v0-81-0|5 Safety and Privacy changes in rust-v0.81.0]]
- Later: 2026-01-15 · Codex CLI · [[Changes/Codex CLI/2026-01-15-revert-linux-sandboxing-now-falls-back-to-landlock-only-restrictions-when-user-n|revert Linux sandboxing now falls back to Landlock-only restrictions when user…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-01-14-0cb091&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-01-14-7-safety-and-privacy-changes-in-v0-24-0.md%0ACard%20ID%3A%20gemini-cli-2026-01-14-0cb091%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.24.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->