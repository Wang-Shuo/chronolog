---
card_id: gemini-cli-2026-01-14-2166d3
date: '2026-01-14'
description: 'Gemini CLI · 2026-01-14 · Agent Mode: 10 changes in Release v0.24.0
  — feat(agents): add support for remote agents and multi-agent TOML files by @adamfweidman…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 923
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a7d94825f4a8f1a604daa4c4a69c8a53aa7e5edb1bed83cdbb6c46a57aa3ffe7
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-01-14-2166d3
  comparison: ''
  date: '2026-01-14'
  description: 'Gemini CLI — Release v0.24.0: 10 Agent Mode changes'
  evidence:
  - quote: 'feat(agents): add support for remote agents and multi-agent TOML files
      by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/15437'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: 'Agent Skills: Implement Core Skill Infrastructure & Tiered Discovery by
      @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15698'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: 'feat(agents): Add remote agents to agent registry by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/15711'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: 'Agent Skills: Unify Representation & Centralize Loading by @NTaylorMullen
      in https://github.com/google-gemini/gemini-cli/pull/15833'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: 'feat(core): Standardize Tool and Agent Invocation constructors (Phase
      2) by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15775'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: 'feat(hooks): implement granular stop and block behavior for agent hooks
      by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/15824'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: 'Agent Skills: Implement /skills reload by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15865'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: 'Agent Skills: Add skill directory to WorkspaceContext upon activation
      by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15870'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: 'feat(agents): add support for remote agents by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/16013'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: 'Agent Skills: Initial Documentation & Tutorial by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15869'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 10-agent-mode-changes-in-v0-24-0
  source_release: gemini-cli-2026-01-14-v0-24-0-github-276723271-62398547
  source_type: github_releases
  theme: agent-mode
  title: 10 Agent Mode changes in v0.24.0
  type: change
related_changes:
- '[[Changes/Windsurf/2026-01-13-new-features-and-improvements|New Features and Improvements]]'
- '[[Changes/Claude Code/2026-01-14-added-inline-display-of-agent-s-final-response-in-task-notifications-making-it-e|Added
  inline display of agent''s final response in task notifications, making…]]'
- '[[Changes/Codex CLI/2026-01-14-2-agent-mode-changes-in-rust-v0-81-0|2 Agent Mode
  changes in rust-v0.81.0]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-01-14-v0-24-0-github-276723271-62398547|gemini-cli-2026-01-14-v0-24-0-github-276723271-62398547]]'
source_type: github_releases
theme: agent-mode
title: 10 Agent Mode changes in v0.24.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Agent Mode changes in v0.24.0

**Gemini CLI** · 2026-01-14 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0) · from [[Releases/Gemini CLI/gemini-cli-2026-01-14-v0-24-0-github-276723271-62398547|Release v0.24.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat(agents): add support for remote agents and multi-agent TOML files by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/15437

> Agent Skills: Implement Core Skill Infrastructure & Tiered Discovery by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15698

> feat(agents): Add remote agents to agent registry by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/15711

> Agent Skills: Unify Representation & Centralize Loading by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15833

> feat(core): Standardize Tool and Agent Invocation constructors (Phase 2) by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/15775

> feat(hooks): implement granular stop and block behavior for agent hooks by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/15824

> Agent Skills: Implement /skills reload by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15865

> Agent Skills: Add skill directory to WorkspaceContext upon activation by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15870

> feat(agents): add support for remote agents by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/16013

> Agent Skills: Initial Documentation & Tutorial by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15869

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-01-14-7-safety-and-privacy-changes-in-v0-24-0|7 Safety and Privacy changes in v0.24.0]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-01-14-feat-add-folder-suggestions-to-dir-add-command-by-jackwotherspoon-in-https-githu|feat: add folder suggestions to /dir add command]] · Developer Workflow
- [[Changes/Gemini CLI/2026-01-14-9-apps-and-integrations-changes-in-v0-24-0|9 Apps and Integrations changes in v0.24.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-01-14-4-editor-experience-changes-in-v0-24-0|4 Editor Experience changes in v0.24.0]] · Editor Experience
- [[Changes/Gemini CLI/2026-01-14-6-model-support-changes-in-v0-24-0|6 Model Support changes in v0.24.0]] · Model Support
- [[Changes/Gemini CLI/2026-01-14-2-context-window-changes-in-v0-24-0|2 Context Window changes in v0.24.0]] · Context Window
- [[Changes/Gemini CLI/2026-01-14-38-other-changes-in-v0-24-0|38 other changes in v0.24.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-01-14 · Codex CLI · [[Changes/Codex CLI/2026-01-14-2-agent-mode-changes-in-rust-v0-81-0|2 Agent Mode changes in rust-v0.81.0]]
- Later: 2026-01-14 · OpenCode · [[Changes/OpenCode/2026-01-14-do-not-allow-agent-to-ask-custom-less-questions|Do not allow agent to ask custom-less questions]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-01-14-2166d3&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-01-14-10-agent-mode-changes-in-v0-24-0.md%0ACard%20ID%3A%20gemini-cli-2026-01-14-2166d3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.24.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->