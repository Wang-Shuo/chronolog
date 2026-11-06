---
card_id: gemini-cli-2026-02-04-fbeeaa
date: '2026-02-04'
description: 'Gemini CLI · 2026-02-04 · Agent Mode: 15 changes in Release v0.27.0
  — feat(core): Enable AgentRegistry to track all discovered subagents by @SandyTao520
  in…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 944
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 87f2b97ec03473f9bade9c132ddb960c006f6ee47afb258030c40527e0ea313e
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-02-04-fbeeaa
  comparison: ''
  date: '2026-02-04'
  description: 'Gemini CLI — Release v0.27.0: 15 Agent Mode changes'
  evidence:
  - quote: 'feat(core): Enable AgentRegistry to track all discovered subagents by
      @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/17253'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(core): Have subagents use a JSON schema type for input. by @joshualitt
      in https://github.com/google-gemini/gemini-cli/pull/17152'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(cli): Add state management and plumbing for agent configuration dialog
      by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/17259'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(cli): add /agents config command and improve agent discovery by @SandyTao520
      in https://github.com/google-gemini/gemini-cli/pull/17342'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(core): Refresh agents after loading an extension. by @joshualitt
      in https://github.com/google-gemini/gemini-cli/pull/17355'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Refactor subagent delegation to be one tool per agent by @gundermanc in
      https://github.com/google-gemini/gemini-cli/pull/17346
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(plan): implement simple workflow for planning in main agent by @jerop
      in https://github.com/google-gemini/gemini-cli/pull/17326'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat: implement AgentConfigDialog for /agents config command by @SandyTao520
      in https://github.com/google-gemini/gemini-cli/pull/17370'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(agents): implement first-run experience for project-level sub-agents
      by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/17266'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(agents): migrate subagents to event-driven scheduler by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/17567'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Sub-agents documentation. by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/16639
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Load extension settings for hooks, agents, skills by @chrstnb in https://github.com/google-gemini/gemini-cli/pull/17245
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(skills): promote Agent Skills to stable by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17693'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'docs: Add Experimental Remote Agent Docs by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/17697'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'revert: promote Agent Skills to stable (#17693) by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17712'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 15-agent-mode-changes-in-v0-27-0
  source_release: gemini-cli-2026-02-04-v0-27-0-github-282779403-9d866835
  source_type: github_releases
  theme: agent-mode
  title: 15 Agent Mode changes in v0.27.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-02-03-4-agent-mode-changes-in-v0-0-402|4 Agent
  Mode changes in v0.0.402]]'
- '[[Changes/GitHub Copilot CLI/2026-02-03-support-agents-skills-directory-for-auto-loading-skills|Support
  .agents/skills directory for auto-loading skills]]'
- '[[Changes/Codex CLI/2026-02-04-4-agent-mode-changes-in-rust-v0-95-0|4 Agent Mode
  changes in rust-v0.95.0]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-02-04-v0-27-0-github-282779403-9d866835|gemini-cli-2026-02-04-v0-27-0-github-282779403-9d866835]]'
source_type: github_releases
theme: agent-mode
title: 15 Agent Mode changes in v0.27.0
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Agent Mode changes in v0.27.0

**Gemini CLI** · 2026-02-04 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0) · from [[Releases/Gemini CLI/gemini-cli-2026-02-04-v0-27-0-github-282779403-9d866835|Release v0.27.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat(core): Enable AgentRegistry to track all discovered subagents by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/17253

> feat(core): Have subagents use a JSON schema type for input. by @joshualitt in https://github.com/google-gemini/gemini-cli/pull/17152

> feat(cli): Add state management and plumbing for agent configuration dialog by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/17259

> feat(cli): add /agents config command and improve agent discovery by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/17342

> feat(core): Refresh agents after loading an extension. by @joshualitt in https://github.com/google-gemini/gemini-cli/pull/17355

> Refactor subagent delegation to be one tool per agent by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/17346

> feat(plan): implement simple workflow for planning in main agent by @jerop in https://github.com/google-gemini/gemini-cli/pull/17326

> feat: implement AgentConfigDialog for /agents config command by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/17370

> feat(agents): implement first-run experience for project-level sub-agents by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/17266

> feat(agents): migrate subagents to event-driven scheduler by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17567

> Sub-agents documentation. by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/16639

> Load extension settings for hooks, agents, skills by @chrstnb in https://github.com/google-gemini/gemini-cli/pull/17245

> feat(skills): promote Agent Skills to stable by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17693

> docs: Add Experimental Remote Agent Docs by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/17697

> revert: promote Agent Skills to stable (#17693) by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17712

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-02-04-11-developer-workflow-changes-in-v0-27-0|11 Developer Workflow changes in v0.27.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-02-04-14-apps-and-integrations-changes-in-v0-27-0|14 Apps and Integrations changes in v0.27.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-02-04-4-interface-experience-changes-in-v0-27-0|4 Interface Experience changes in v0.27.0]] · Interface Experience
- [[Changes/Gemini CLI/2026-02-04-security-hooks-wrap-hook-injected-context-in-distinct-xml-tags-by-yunaseoul-in-h|security(hooks): Wrap hook-injected context in distinct XML tags]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-02-04-4-editor-experience-changes-in-v0-27-0|4 Editor Experience changes in v0.27.0]] · Editor Experience
- [[Changes/Gemini CLI/2026-02-04-3-automation-and-scheduling-changes-in-v0-27-0|3 Automation and Scheduling changes in v0.27.0]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-02-04-6-model-support-changes-in-v0-27-0|6 Model Support changes in v0.27.0]] · Model Support
- [[Changes/Gemini CLI/2026-02-04-72-other-changes-in-v0-27-0|72 other changes in v0.27.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-02-04 · Codex CLI · [[Changes/Codex CLI/2026-02-04-4-agent-mode-changes-in-rust-v0-95-0|4 Agent Mode changes in rust-v0.95.0]]
- Later: 2026-02-05 · Claude Code · [[Changes/Claude Code/2026-02-05-updated-resume-to-re-use-agent-value-specified-in-previous-conversation-by-defau|Updated --resume to re-use --agent value specified in previous conversation by default]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-02-04-fbeeaa&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-02-04-15-agent-mode-changes-in-v0-27-0.md%0ACard%20ID%3A%20gemini-cli-2026-02-04-fbeeaa%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.27.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->