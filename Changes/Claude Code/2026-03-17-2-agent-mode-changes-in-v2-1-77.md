---
card_id: claude-code-2026-03-17-e856f6
date: '2026-03-17'
description: 'Claude Code · 2026-03-17 · Agent Mode: 2 changes in v2.1.77 — The Agent
  tool no longer accepts a `resume` parameter — use `SendMessage({to: agentId})` to…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 985
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 39e8112970698713c4a601d7d54de22944dc9d6a6992fe0eb11b03ccd204d0b3
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-17-e856f6
  comparison: ''
  date: '2026-03-17'
  description: 'Claude Code — v2.1.77: 2 Agent Mode changes'
  evidence:
  - quote: 'The Agent tool no longer accepts a `resume` parameter — use `SendMessage({to:
      agentId})` to continue a previously spawned agent'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
  - quote: '`SendMessage` now auto-resumes stopped agents in the background instead
      of returning an error'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-agent-mode-changes-in-v2-1-77
  source_release: claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c
  source_type: github_releases
  theme: agent-mode
  title: 2 Agent Mode changes in v2.1.77
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-05-2-agent-mode-changes-in-v2-1-69|2 Agent Mode changes
  in v2.1.69]]'
- '[[Changes/Claude Code/2026-03-10-2-agent-mode-changes-in-v2-1-72|2 Agent Mode changes
  in v2.1.72]]'
- '[[Changes/Claude Code/2026-03-14-improved-background-agent-behavior-killing-a-background-agent-now-preserves-its|Improved
  background agent behavior]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c|claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c]]'
source_type: github_releases
theme: agent-mode
title: 2 Agent Mode changes in v2.1.77
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Agent Mode changes in v2.1.77

**Claude Code** · 2026-03-17 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.77) · from [[Releases/Claude Code/claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c|v2.1.77]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The Agent tool no longer accepts a `resume` parameter — use `SendMessage({to: agentId})` to continue a previously spawned agent

> `SendMessage` now auto-resumes stopped agents in the background instead of returning an error

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-17-show-a-notice-when-apikeyhelper-takes-longer-than-10s-preventing-it-from-blockin|Show a notice when apiKeyHelper takes longer than 10s, preventing it from blocking…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-03-17-vscode-improved-plan-preview-tab-titles-to-use-the-plan-s-heading-instead-of-cla|VSCode Improved plan preview tab titles to use the plan's heading instead…]] · Editor Experience
- [[Changes/Claude Code/2026-03-17-copy-now-accepts-an-optional-index-copy-n-copies-the-nth-latest-assistant-respon|/copy now accepts an optional index: /copy N copies the Nth-latest assistant response]] · Interface Experience
- [[Changes/Claude Code/2026-03-17-2-apps-and-integrations-changes-in-v2-1-77|2 Apps and Integrations changes in v2.1.77]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-17-background-bash-tasks-are-now-killed-if-output-exceeds-5gb-preventing-runaway-pr|Background bash tasks are now killed if output exceeds 5GB, preventing runaway…]] · Developer Workflow
- [[Changes/Claude Code/2026-03-17-faster-resume-on-fork-heavy-and-very-large-sessions-up-to-45-faster-loading-and|Faster --resume on fork-heavy and very large sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-17-3-safety-and-privacy-changes-in-v2-1-77|3 Safety and Privacy changes in v2.1.77]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-17-2-mobile-and-desktop-changes-in-v2-1-77|2 Mobile and Desktop changes in v2.1.77]] · Mobile and Desktop
- [[Changes/Claude Code/2026-03-17-increased-default-maximum-output-token-limits-for-claude-opus-4-6-to-64k-tokens|Increased default maximum output token limits for Claude Opus 4.6 to 64k tokens…]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-03-14 · Claude Code · [[Changes/Claude Code/2026-03-14-improved-background-agent-behavior-killing-a-background-agent-now-preserves-its|Improved background agent behavior]]
- Later: 2026-03-25 · Claude Code · [[Changes/Claude Code/2026-03-25-agents-can-now-declare-initialprompt-in-frontmatter-to-auto-submit-a-first-turn|Agents can now declare initialPrompt in frontmatter to auto-submit a first turn]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-17-e856f6&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-17-2-agent-mode-changes-in-v2-1-77.md%0ACard%20ID%3A%20claude-code-2026-03-17-e856f6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.77%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->