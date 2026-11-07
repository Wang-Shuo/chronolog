---
card_id: gemini-cli-2026-02-18-a38a03
date: '2026-02-18'
description: 'Gemini CLI · 2026-02-18 · Agent Mode: 8 changes in Release v0.29.0 —
  Encourage agent to utilize ecosystem tools to perform work by @gundermanc in…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 958
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 484ce2c08f0c649572e0327a1c1b0e650f38a720981d3f7f7aaf61302fd7f14a
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-02-18-a38a03
  comparison: ''
  date: '2026-02-18'
  description: 'Gemini CLI — Release v0.29.0: 8 Agent Mode changes'
  evidence:
  - quote: Encourage agent to utilize ecosystem tools to perform work by @gundermanc
      in https://github.com/google-gemini/gemini-cli/pull/17881
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.29.0
  - quote: 'feat(core): add default execution limits for subagents by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/18274'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.29.0
  - quote: 'feat(core): remove hardcoded policy bypass for local subagents by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/18153'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.29.0
  - quote: Add information about the agent skills lifecycle and clarify docs-writer
      skill metadata. by @g-samroberts in https://github.com/google-gemini/gemini-cli/pull/18234
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.29.0
  - quote: 'feat(skills): implement linking for agent skills by @MushuEE in https://github.com/google-gemini/gemini-cli/pull/18295'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.29.0
  - quote: 'feat(core): pause agent timeout budget while waiting for tool confirmation
      by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/18415'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.29.0
  - quote: 'feat(core): transition sub-agents to XML format and improve definitions
      by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/18555'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.29.0
  - quote: 'feat(core): optimize sub-agents system prompt intro by @NTaylorMullen
      in https://github.com/google-gemini/gemini-cli/pull/18608'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.29.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 8-agent-mode-changes-in-v0-29-0
  source_release: gemini-cli-2026-02-18-v0-29-0-github-287470100-0bac8990
  source_type: github_releases
  theme: agent-mode
  title: 8 Agent Mode changes in v0.29.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-18-2-agent-mode-changes-in-v2-1-47|2 Agent Mode changes
  in v2.1.47]]'
- '[[Changes/Codex CLI/2026-02-18-protocol-core-now-carry-distinct-approval-ids-for-command-approvals-to-support-m|Protocol/core
  now carry distinct approval IDs for command approvals to support…]]'
- '[[Changes/Cursor/2026-02-18-2-agent-mode-changes-in-cli-improvements-and-mermaid-ascii|2
  Agent Mode changes in CLI Improvements and Mermaid ASCII…]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-02-18-v0-29-0-github-287470100-0bac8990|gemini-cli-2026-02-18-v0-29-0-github-287470100-0bac8990]]'
source_type: github_releases
theme: agent-mode
title: 8 Agent Mode changes in v0.29.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Agent Mode changes in v0.29.0

**Gemini CLI** · 2026-02-18 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.29.0) · from [[Releases/Gemini CLI/gemini-cli-2026-02-18-v0-29-0-github-287470100-0bac8990|Release v0.29.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Encourage agent to utilize ecosystem tools to perform work by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/17881

> feat(core): add default execution limits for subagents by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/18274

> feat(core): remove hardcoded policy bypass for local subagents by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/18153

> Add information about the agent skills lifecycle and clarify docs-writer skill metadata. by @g-samroberts in https://github.com/google-gemini/gemini-cli/pull/18234

> feat(skills): implement linking for agent skills by @MushuEE in https://github.com/google-gemini/gemini-cli/pull/18295

> feat(core): pause agent timeout budget while waiting for tool confirmation by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/18415

> feat(core): transition sub-agents to XML format and improve definitions by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/18555

> feat(core): optimize sub-agents system prompt intro by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/18608

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.29.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-02-18-3-context-window-changes-in-v0-29-0|3 Context Window changes in v0.29.0]] · Context Window
- [[Changes/Gemini CLI/2026-02-18-feat-expand-verify-release-to-macos-and-windows-by-yunaseoul-in-https-github-com|feat: expand verify-release to macOS and Windows]] · Mobile and Desktop
- [[Changes/Gemini CLI/2026-02-18-7-developer-workflow-changes-in-v0-29-0|7 Developer Workflow changes in v0.29.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-02-18-2-editor-experience-changes-in-v0-29-0|2 Editor Experience changes in v0.29.0]] · Editor Experience
- [[Changes/Gemini CLI/2026-02-18-5-apps-and-integrations-changes-in-v0-29-0|5 Apps and Integrations changes in v0.29.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-02-18-ui-update-subdue-footer-colors-and-animate-progress-indicator-by-keithguerin-in|ui: update & subdue footer colors and animate progress indicator]] · Interface Experience
- [[Changes/Gemini CLI/2026-02-18-5-safety-and-privacy-changes-in-v0-29-0|5 Safety and Privacy changes in v0.29.0]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-02-18-2-memory-and-personalization-changes-in-v0-29-0|2 Memory and Personalization changes in v0.29.0]] · Memory and Personalization
- [[Changes/Gemini CLI/2026-02-18-feat-plan-add-positive-test-case-and-update-eval-stability-policy-by-jerop-in-ht|feat(plan): add positive test case and update eval stability policy]] · Reliability and Performance
- [[Changes/Gemini CLI/2026-02-18-11-model-support-changes-in-v0-29-0|11 Model Support changes in v0.29.0]] · Model Support
- [[Changes/Gemini CLI/2026-02-18-65-other-changes-in-v0-29-0|65 other changes in v0.29.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-02-18 · Cursor · [[Changes/Cursor/2026-02-18-2-agent-mode-changes-in-cli-improvements-and-mermaid-ascii|2 Agent Mode changes in CLI Improvements and Mermaid ASCII…]]
- Later: 2026-02-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-19-3-agent-mode-changes-in-v0-0-412|3 Agent Mode changes in v0.0.412]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-02-18-a38a03&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-02-18-8-agent-mode-changes-in-v0-29-0.md%0ACard%20ID%3A%20gemini-cli-2026-02-18-a38a03%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.29.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->