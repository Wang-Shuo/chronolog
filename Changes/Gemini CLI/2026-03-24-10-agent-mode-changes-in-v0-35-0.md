---
card_id: gemini-cli-2026-03-24-540251
date: '2026-03-24'
description: 'Gemini CLI · 2026-03-24 · Agent Mode: 10 changes in Release v0.35.0
  — feat(core): simplify subagent success UI and improve early termination display
  by…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 992
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 10ba198a89499a55c274ab4c74b3cb3745505adfdc31feee2e58de760fef9283
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-03-24-540251
  comparison: ''
  date: '2026-03-24'
  description: 'Gemini CLI — Release v0.35.0: 10 Agent Mode changes'
  evidence:
  - quote: 'feat(core): simplify subagent success UI and improve early termination
      display by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/21917'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  - quote: 'feat(core): differentiate User-Agent for a2a-server and ACP clients by
      @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/22059'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  - quote: 'feat(core): add google credentials provider for remote agents by @adamfweidman
      in https://github.com/google-gemini/gemini-cli/pull/21024'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  - quote: 'feat(cli): allow safe tools to execute concurrently while agent is busy
      by @spencer426 in https://github.com/google-gemini/gemini-cli/pull/21988'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  - quote: 'feat(core): increase sub-agent turn and time limits by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/22196'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  - quote: 'docs: overhaul subagents documentation and add /agents command by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/22345'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  - quote: 'feat(agent): add allowed domain restrictions for browser agent by @cynthialong0-0
      in https://github.com/google-gemini/gemini-cli/pull/21775'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  - quote: 'refactor(core): Creates AgentSession abstraction for consolidated agent
      interface. by @mbleigh in https://github.com/google-gemini/gemini-cli/pull/22270'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  - quote: 'feat: enable subagents by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/22386'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  - quote: 'feat(core): add foundation for subagent tool isolation by @akh64bit in
      https://github.com/google-gemini/gemini-cli/pull/22708'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 10-agent-mode-changes-in-v0-35-0
  source_release: gemini-cli-2026-03-24-v0-35-0-github-300868580-f6f9b621
  source_type: github_releases
  theme: agent-mode
  title: 10 Agent Mode changes in v0.35.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-03-23-elevenagents|ElevenAgents]]'
- '[[Changes/ElevenLabs/2026-03-23-python-sdk|Python SDK]]'
- '[[Changes/GitHub Copilot CLI/2026-03-23-2-agent-mode-changes-in-v1-0-11|2 Agent
  Mode changes in v1.0.11]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-03-24-v0-35-0-github-300868580-f6f9b621|gemini-cli-2026-03-24-v0-35-0-github-300868580-f6f9b621]]'
source_type: github_releases
theme: agent-mode
title: 10 Agent Mode changes in v0.35.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Agent Mode changes in v0.35.0

**Gemini CLI** · 2026-03-24 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0) · from [[Releases/Gemini CLI/gemini-cli-2026-03-24-v0-35-0-github-300868580-f6f9b621|Release v0.35.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat(core): simplify subagent success UI and improve early termination display by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/21917

> feat(core): differentiate User-Agent for a2a-server and ACP clients by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/22059

> feat(core): add google credentials provider for remote agents by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/21024

> feat(cli): allow safe tools to execute concurrently while agent is busy by @spencer426 in https://github.com/google-gemini/gemini-cli/pull/21988

> feat(core): increase sub-agent turn and time limits by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/22196

> docs: overhaul subagents documentation and add /agents command by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/22345

> feat(agent): add allowed domain restrictions for browser agent by @cynthialong0-0 in https://github.com/google-gemini/gemini-cli/pull/21775

> refactor(core): Creates AgentSession abstraction for consolidated agent interface. by @mbleigh in https://github.com/google-gemini/gemini-cli/pull/22270

> feat: enable subagents by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/22386

> feat(core): add foundation for subagent tool isolation by @akh64bit in https://github.com/google-gemini/gemini-cli/pull/22708

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.35.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-03-24-refactor-core-align-jit-memory-placement-with-tiered-context-model-by-sandytao52|refactor(core): align JIT memory placement with tiered context model]] · Memory and Personalization
- [[Changes/Gemini CLI/2026-03-24-docs-cli-add-custom-keybinding-documentation-by-scidomino-in-https-github-com-go|docs(cli): add custom keybinding documentation]] · Interface Experience
- [[Changes/Gemini CLI/2026-03-24-docs-document-npm-deprecation-warnings-as-safe-to-ignore-by-h30s-in-https-github|docs: document npm deprecation warnings as safe to ignore]] · Files and Data
- [[Changes/Gemini CLI/2026-03-24-2-context-window-changes-in-v0-35-0|2 Context Window changes in v0.35.0]] · Context Window
- [[Changes/Gemini CLI/2026-03-24-feat-skills-improve-async-pr-review-workflow-and-logging-by-mattkorwel-in-https|feat(skills): improve async-pr-review workflow and logging]] · Developer Workflow
- [[Changes/Gemini CLI/2026-03-24-5-apps-and-integrations-changes-in-v0-35-0|5 Apps and Integrations changes in v0.35.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-03-24-docs-core-add-authentication-guide-for-remote-subagents-by-adamfweidman-in-https|docs(core): add authentication guide for remote subagents]] · Account and Access
- [[Changes/Gemini CLI/2026-03-24-7-model-support-changes-in-v0-35-0|7 Model Support changes in v0.35.0]] · Model Support
- [[Changes/Gemini CLI/2026-03-24-feat-telemetry-add-clearcut-instrumentation-for-ai-credits-billing-events-by-gsq|feat(telemetry): add Clearcut instrumentation for AI credits billing events]] · Pricing Model
- [[Changes/Gemini CLI/2026-03-24-2-automation-and-scheduling-changes-in-v0-35-0|2 Automation and Scheduling changes in v0.35.0]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-03-24-5-safety-and-privacy-changes-in-v0-35-0|5 Safety and Privacy changes in v0.35.0]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-03-24-58-other-changes-in-v0-35-0|58 other changes in v0.35.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-03-23 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-23-2-agent-mode-changes-in-v1-0-11|2 Agent Mode changes in v1.0.11]]
- Later: 2026-03-25 · Claude Code · [[Changes/Claude Code/2026-03-25-agents-can-now-declare-initialprompt-in-frontmatter-to-auto-submit-a-first-turn|Agents can now declare initialPrompt in frontmatter to auto-submit a first turn]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-03-24-540251&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-03-24-10-agent-mode-changes-in-v0-35-0.md%0ACard%20ID%3A%20gemini-cli-2026-03-24-540251%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.35.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->