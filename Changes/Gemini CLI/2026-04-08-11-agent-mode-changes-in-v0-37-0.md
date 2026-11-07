---
card_id: gemini-cli-2026-04-08-abf4e3
date: '2026-04-08'
description: 'Gemini CLI · 2026-04-08 · Agent Mode: 11 changes in Release v0.37.0
  — feat(evals): centralize test agents into test-utils for reuse by @Samee24 in…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1007
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ad50de0486c47f34802ff5c03c935e300d08c2432da63c5ed5392211ca46591b
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-04-08-abf4e3
  comparison: ''
  date: '2026-04-08'
  description: 'Gemini CLI — Release v0.37.0: 11 Agent Mode changes'
  evidence:
  - quote: 'feat(evals): centralize test agents into test-utils for reuse by @Samee24
      in https://github.com/google-gemini/gemini-cli/pull/23616'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.37.0
  - quote: 'revert: chore(config): disable agents by default by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/23672'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.37.0
  - quote: 'feat(browser): add maxActionsPerTask for browser agent setting by @cynthialong0-0
      in https://github.com/google-gemini/gemini-cli/pull/23216'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.37.0
  - quote: 'feat(core): support inline agentCardJson for remote agents by @adamfweidman
      in https://github.com/google-gemini/gemini-cli/pull/23743'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.37.0
  - quote: 'docs(core): document agent_card_json string literal options for remote
      agents by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/23797'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.37.0
  - quote: 'feat(core): subagent isolation and cleanup hardening by @abhipatel12 in
      https://github.com/google-gemini/gemini-cli/pull/23903'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.37.0
  - quote: 'test(evals): add comprehensive subagent delegation evaluations by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/24132'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.37.0
  - quote: 'docs: update subagents docs to not be experimental by @abhipatel12 in
      https://github.com/google-gemini/gemini-cli/pull/24343'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.37.0
  - quote: 'feat(core): infrastructure for event-driven subagent history by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/23914'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.37.0
  - quote: 'feat(core): update browser agent prompt to check open pages first when
      bringing up by @cynthialong0-0 in https://github.com/google-gemini/gemini-cli/pull/24431'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.37.0
  - quote: 'docs(core): add subagent tool isolation draft doc by @akh64bit in https://github.com/google-gemini/gemini-cli/pull/23275'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.37.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 11-agent-mode-changes-in-v0-37-0
  source_release: gemini-cli-2026-04-08-v0-37-0-github-306699346-f88de07d
  source_type: github_releases
  theme: agent-mode
  title: 11 Agent Mode changes in v0.37.0
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-04-07-new-agent-permissions-system-accessible-in-settings|New
  agent permissions system accessible in settings]]'
- '[[Changes/Google Antigravity/2026-04-07-agent-permissions|Agent Permissions]]'
- '[[Changes/Claude Code/2026-04-08-2-agent-mode-changes-in-v2-1-97|2 Agent Mode changes
  in v2.1.97]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-04-08-v0-37-0-github-306699346-f88de07d|gemini-cli-2026-04-08-v0-37-0-github-306699346-f88de07d]]'
source_type: github_releases
theme: agent-mode
title: 11 Agent Mode changes in v0.37.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Agent Mode changes in v0.37.0

**Gemini CLI** · 2026-04-08 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.37.0) · from [[Releases/Gemini CLI/gemini-cli-2026-04-08-v0-37-0-github-306699346-f88de07d|Release v0.37.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat(evals): centralize test agents into test-utils for reuse by @Samee24 in https://github.com/google-gemini/gemini-cli/pull/23616

> revert: chore(config): disable agents by default by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/23672

> feat(browser): add maxActionsPerTask for browser agent setting by @cynthialong0-0 in https://github.com/google-gemini/gemini-cli/pull/23216

> feat(core): support inline agentCardJson for remote agents by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/23743

> docs(core): document agent_card_json string literal options for remote agents by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/23797

> feat(core): subagent isolation and cleanup hardening by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/23903

> test(evals): add comprehensive subagent delegation evaluations by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/24132

> docs: update subagents docs to not be experimental by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/24343

> feat(core): infrastructure for event-driven subagent history by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/23914

> feat(core): update browser agent prompt to check open pages first when bringing up by @cynthialong0-0 in https://github.com/google-gemini/gemini-cli/pull/24431

> docs(core): add subagent tool isolation draft doc by @akh64bit in https://github.com/google-gemini/gemini-cli/pull/23275

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.37.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-04-08-feat-cli-support-tab-to-queue-for-messages-while-generating-by-gundermanc-in-htt|feat(cli): support 'tab to queue' for messages while generating]] · Editor Experience
- [[Changes/Gemini CLI/2026-04-08-3-developer-workflow-changes-in-v0-37-0|3 Developer Workflow changes in v0.37.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-04-08-refine-onboarding-metrics-to-log-the-duration-explicitly-and-use-the-tier-name-b|Refine onboarding metrics to log the duration explicitly and use the tier name]] · Interface Experience
- [[Changes/Gemini CLI/2026-04-08-default-enable-narration-for-the-team-by-gundermanc-in-https-github-com-google-g|Default enable narration for the team]] · Collaboration
- [[Changes/Gemini CLI/2026-04-08-2-memory-and-personalization-changes-in-v0-37-0|2 Memory and Personalization changes in v0.37.0]] · Memory and Personalization
- [[Changes/Gemini CLI/2026-04-08-5-context-window-changes-in-v0-37-0|5 Context Window changes in v0.37.0]] · Context Window
- [[Changes/Gemini CLI/2026-04-08-5-model-support-changes-in-v0-37-0|5 Model Support changes in v0.37.0]] · Model Support
- [[Changes/Gemini CLI/2026-04-08-docs-update-quotas-and-pricing-by-jkcinouye-in-https-github-com-google-gemini-ge|Docs: Update quotas and pricing]] · Pricing Model
- [[Changes/Gemini CLI/2026-04-08-3-apps-and-integrations-changes-in-v0-37-0|3 Apps and Integrations changes in v0.37.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-04-08-16-safety-and-privacy-changes-in-v0-37-0|16 Safety and Privacy changes in v0.37.0]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-04-08-52-other-changes-in-v0-37-0|52 other changes in v0.37.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-08 · Claude Code · [[Changes/Claude Code/2026-04-08-2-agent-mode-changes-in-v2-1-97|2 Agent Mode changes in v2.1.97]]
- Later: 2026-04-09 · Claude Code · [[Changes/Claude Code/2026-04-09-3-agent-mode-changes-in-v2-1-98|3 Agent Mode changes in v2.1.98]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-04-08-abf4e3&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-04-08-11-agent-mode-changes-in-v0-37-0.md%0ACard%20ID%3A%20gemini-cli-2026-04-08-abf4e3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.37.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->