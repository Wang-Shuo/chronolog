---
card_id: github-copilot-cli-2026-08-03-305d7a
date: '2026-08-03'
description: 'GitHub Copilot CLI · 2026-08-03 · Agent Mode: A run whose prompt is
  piped over stdin now treats its `sessionEnd` hook the same way `-p` does: the hook
  fires…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1124
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: change
machine_hash: 49b91aa76beed562bee5ed4a79b86b762553d7d158bec3dbe1cefe007d7e8813
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  ai_generated: true
  card_id: github-copilot-cli-2026-08-03-305d7a
  comparison: ''
  confidence: low
  date: '2026-08-03'
  description: 'GitHub Copilot CLI — 1.0.78: A run whose prompt is piped over stdin
    now treats its `sessionEnd` hook the same way `-p` does: the hook fires once per
    completed agent turn with `reason` `complete` (or `error` if the turn failed),
    instead of once at shutdown with `user_exit`. As with `-p`, a piped run that exits
    before completing a turn fires no `sessionEnd` hook'
  evidence:
  - quote: 'A run whose prompt is piped over stdin now treats its `sessionEnd` hook
      the same way `-p` does: the hook fires once per completed agent turn with `reason`
      `complete` (or `error` if the turn failed), instead of once at shutdown with
      `user_exit`. As with `-p`, a piped run that exits before completing a turn fires
      no `sessionEnd` hook'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: change
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: a-run-whose-prompt-is-piped-over-stdin-now-treats-its-sessionend-hook-the-same-w
  source_release: github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc
  source_type: github_releases
  theme: agent-mode
  title: A run whose prompt is piped over stdin now treats its `sessionEnd` hook the
    same way…
  type: change
related_changes:
- '[[Changes/Replit/2026-07-31-agent|Agent]]'
- '[[Changes/ElevenLabs/2026-08-03-elevenagents|ElevenAgents]]'
- '[[Changes/ElevenLabs/2026-08-03-packages|Packages]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc|github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc]]'
source_type: github_releases
theme: agent-mode
title: A run whose prompt is piped over stdin now treats its sessionEnd hook the same
  way…
type: change
---

<!-- chronolog:begin region="header" -->
# A run whose prompt is piped over stdin now treats its `sessionEnd` hook the same way…

**GitHub Copilot CLI** · 2026-08-03 · [[Themes/agent-mode|Agent Mode]] · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.78) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc|1.0.78]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> A run whose prompt is piped over stdin now treats its `sessionEnd` hook the same way `-p` does: the hook fires once per completed agent turn with `reason` `complete` (or `error` if the turn failed), instead of once at shutdown with `user_exit`. As with `-p`, a piped run that exits before completing a turn fires no `sessionEnd` hook
>
> Source: https://github.com/github/copilot-cli/releases/tag/v1.0.78
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-08-03-4-apps-and-integrations-changes-in-v1-0-78|4 Apps and Integrations changes in v1.0.78]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-08-03-2-editor-experience-changes-in-v1-0-78|2 Editor Experience changes in v1.0.78]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-08-03-resuming-a-long-session-is-dramatically-faster-and-far-lighter-on-memory-because|Resuming a long session is dramatically faster and far lighter on memory, because…]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-08-03-2-account-and-access-changes-in-v1-0-78|2 Account and Access changes in v1.0.78]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-08-03-the-allow-all-auto-safety-judge-model-is-no-longer-user-configurable-the-judge-m|The /allow-all auto safety-judge model is no longer user-configurable]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-08-03-2-interface-experience-changes-in-v1-0-78|2 Interface Experience changes in v1.0.78]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-08-03-3-safety-and-privacy-changes-in-v1-0-78|3 Safety and Privacy changes in v1.0.78]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-08-03-2-developer-workflow-changes-in-v1-0-78|2 Developer Workflow changes in v1.0.78]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-08-03-9-other-changes-in-v1-0-78|9 other changes in v1.0.78]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-03 · ElevenLabs · [[Changes/ElevenLabs/2026-08-03-packages|Packages]]
- Later: 2026-08-03 · OpenHands · [[Changes/OpenHands/2026-08-03-3-agent-mode-changes-in-v1-9-0|3 Agent Mode changes in v1.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-08-03-305d7a&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-08-03-a-run-whose-prompt-is-piped-over-stdin-now-treats-its-sessionend-hook-the-same-w.md%0ACard%20ID%3A%20github-copilot-cli-2026-08-03-305d7a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.78%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->