---
card_id: gemini-cli-2026-04-01-af43a3
date: '2026-04-01'
description: 'Gemini CLI · 2026-04-01 · Agent Mode: 10 changes in Release v0.36.0
  — feat(core): multi-registry architecture and tool filtering for subagents by @akh64bit
  in…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1000
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f598e965cf772865fccf854fd960a97e49d078c73f92369c7b6eb24dea666c76
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-04-01-af43a3
  comparison: ''
  date: '2026-04-01'
  description: 'Gemini CLI — Release v0.36.0: 10 Agent Mode changes'
  evidence:
  - quote: 'feat(core): multi-registry architecture and tool filtering for subagents
      by @akh64bit in https://github.com/google-gemini/gemini-cli/pull/22712'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0
  - quote: 'feat(a2a): add agent acknowledgment command and enhance registry discovery
      by @alisa-alisa in https://github.com/google-gemini/gemini-cli/pull/22389'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0
  - quote: 'feat(core): subagent local execution and tool isolation by @akh64bit in
      https://github.com/google-gemini/gemini-cli/pull/22718'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0
  - quote: 'refactor(cli): group subagent trajectory deletion and use native filesystem
      testing by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/22890'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0
  - quote: 'feat(core): resilient subagent tool rejection with contextual feedback
      by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/22951'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0
  - quote: 'feat(core): introduce AgentSession and rename stream events to agent events
      by @mbleigh in https://github.com/google-gemini/gemini-cli/pull/23159'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0
  - quote: 'feat(core): refine User-Agent for VS Code traffic (unified format) by
      @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/23256'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0
  - quote: 'feat(core): add event-translator and update agent types by @adamfweidman
      in https://github.com/google-gemini/gemini-cli/pull/22985'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0
  - quote: 'chore(config): disable agents by default by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/23546'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0
  - quote: 'feat(evals): add behavioral evaluations for subagent routing by @Samee24
      in https://github.com/google-gemini/gemini-cli/pull/23272'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 10-agent-mode-changes-in-v0-36-0
  source_release: gemini-cli-2026-04-01-v0-36-0-github-304395807-bc719eb1
  source_type: github_releases
  theme: agent-mode
  title: 10 Agent Mode changes in v0.36.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-03-31-4-agent-mode-changes-in-rust-v0-118-0|4 Agent Mode
  changes in rust-v0.118.0]]'
- '[[Changes/Claude Code/2026-04-01-3-agent-mode-changes-in-v2-1-89|3 Agent Mode changes
  in v2.1.89]]'
- '[[Changes/Cline/2026-04-01-exclude-new-task-tool-from-system-prompt-in-yolo-headless-mode|Exclude
  new_task tool from system prompt in yolo/headless mode]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-04-01-v0-36-0-github-304395807-bc719eb1|gemini-cli-2026-04-01-v0-36-0-github-304395807-bc719eb1]]'
source_type: github_releases
theme: agent-mode
title: 10 Agent Mode changes in v0.36.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Agent Mode changes in v0.36.0

**Gemini CLI** · 2026-04-01 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0) · from [[Releases/Gemini CLI/gemini-cli-2026-04-01-v0-36-0-github-304395807-bc719eb1|Release v0.36.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat(core): multi-registry architecture and tool filtering for subagents by @akh64bit in https://github.com/google-gemini/gemini-cli/pull/22712

> feat(a2a): add agent acknowledgment command and enhance registry discovery by @alisa-alisa in https://github.com/google-gemini/gemini-cli/pull/22389

> feat(core): subagent local execution and tool isolation by @akh64bit in https://github.com/google-gemini/gemini-cli/pull/22718

> refactor(cli): group subagent trajectory deletion and use native filesystem testing by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/22890

> feat(core): resilient subagent tool rejection with contextual feedback by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/22951

> feat(core): introduce AgentSession and rename stream events to agent events by @mbleigh in https://github.com/google-gemini/gemini-cli/pull/23159

> feat(core): refine User-Agent for VS Code traffic (unified format) by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/23256

> feat(core): add event-translator and update agent types by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/22985

> chore(config): disable agents by default by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/23546

> feat(evals): add behavioral evaluations for subagent routing by @Samee24 in https://github.com/google-gemini/gemini-cli/pull/23272

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-04-01-3-memory-and-personalization-changes-in-v0-36-0|3 Memory and Personalization changes in v0.36.0]] · Memory and Personalization
- [[Changes/Gemini CLI/2026-04-01-7-safety-and-privacy-changes-in-v0-36-0|7 Safety and Privacy changes in v0.36.0]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-04-01-feat-core-implement-strict-macos-sandboxing-using-seatbelt-allowlist-by-ehedlund|feat(core): implement strict macOS sandboxing using Seatbelt allowlist]] · Mobile and Desktop
- [[Changes/Gemini CLI/2026-04-01-7-model-support-changes-in-v0-36-0|7 Model Support changes in v0.36.0]] · Model Support
- [[Changes/Gemini CLI/2026-04-01-test-core-migrate-hook-tests-to-scheduler-by-abhipatel12-in-https-github-com-goo|test(core): migrate hook tests to scheduler]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-04-01-feat-core-cap-jit-context-upward-traversal-at-git-root-by-sandytao520-in-https-g|feat(core): cap JIT context upward traversal at git root]] · Context Window
- [[Changes/Gemini CLI/2026-04-01-5-apps-and-integrations-changes-in-v0-36-0|5 Apps and Integrations changes in v0.36.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-04-01-refactor-ide-replace-dynamic-undici-import-with-static-fetch-import-by-cocosheng|refactor(ide): replace dynamic undici import with static fetch import]] · Editor Experience
- [[Changes/Gemini CLI/2026-04-01-2-interface-experience-changes-in-v0-36-0|2 Interface Experience changes in v0.36.0]] · Interface Experience
- [[Changes/Gemini CLI/2026-04-01-feat-core-change-user-facing-auth-type-from-oauth2-to-oauth-by-adamfweidman-in-h|feat(core): change user-facing auth type from oauth2 to oauth]] · Account and Access
- [[Changes/Gemini CLI/2026-04-01-3-developer-workflow-changes-in-v0-36-0|3 Developer Workflow changes in v0.36.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-04-01-perf-cli-background-ide-client-to-speed-up-initialization-by-sehoon38-in-https-g|perf(cli): background IDE client to speed up initialization]] · Reliability and Performance
- [[Changes/Gemini CLI/2026-04-01-53-other-changes-in-v0-36-0|53 other changes in v0.36.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-01 · Cline · [[Changes/Cline/2026-04-01-exclude-new-task-tool-from-system-prompt-in-yolo-headless-mode|Exclude new_task tool from system prompt in yolo/headless mode]]
- Later: 2026-04-02 · Cursor · [[Changes/Cursor/2026-04-02-4-agent-mode-changes-in-3-0|4 Agent Mode changes in 3.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-04-01-af43a3&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-04-01-10-agent-mode-changes-in-v0-36-0.md%0ACard%20ID%3A%20gemini-cli-2026-04-01-af43a3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.36.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->