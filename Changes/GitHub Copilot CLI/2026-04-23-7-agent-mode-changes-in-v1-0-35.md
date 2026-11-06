---
card_id: github-copilot-cli-2026-04-23-9cfbc6
date: '2026-04-23'
description: 'GitHub Copilot CLI · 2026-04-23 · Agent Mode: 7 changes in 1.0.35 —
  Configure Copilot agent now has shell access on Windows'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1022
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6458a2ee45c4263fd3c1eeca9be57ed63e5fbc807c1acd21a46fb911f7e6e30e
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-04-23-9cfbc6
  comparison: ''
  date: '2026-04-23'
  description: 'GitHub Copilot CLI — 1.0.35: 7 Agent Mode changes'
  evidence:
  - quote: Configure Copilot agent now has shell access on Windows
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Self-correcting custom tool calls in agentic loop
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Custom agents and skills in ~/.claude/ are no longer incorrectly loaded
      as Copilot project config
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: 'Sync task calls block until completion under MULTI_TURN_AGENTS instead
      of auto-promoting to background after 60s; sync no longer returns a reusable
      agent_id, use mode: "background" for follow-ups'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Auto mode no longer fails with an error when switching to a model that
      doesn't support the configured reasoning effort
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Hide subagent thinking from the timeline
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  - quote: Custom agent name is now visible in the statusline footer and can be toggled
      via /statusline
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.35
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 7-agent-mode-changes-in-v1-0-35
  source_release: github-copilot-cli-2026-04-23-v1-0-35-github-312982689-0111445c
  source_type: github_releases
  theme: agent-mode
  title: 7 Agent Mode changes in v1.0.35
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-04-23-8-agent-mode-changes-in-rust-v0-123-0|8 Agent Mode
  changes in rust-v0.123.0]]'
- '[[Changes/Codex CLI/2026-04-23-11-agent-mode-changes-in-rust-v0-124-0|11 Agent
  Mode changes in rust-v0.124.0]]'
- '[[Changes/Gemini CLI/2026-04-23-6-agent-mode-changes-in-v0-39-0|6 Agent Mode changes
  in v0.39.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-23-v1-0-35-github-312982689-0111445c|github-copilot-cli-2026-04-23-v1-0-35-github-312982689-0111445c]]'
source_type: github_releases
theme: agent-mode
title: 7 Agent Mode changes in v1.0.35
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Agent Mode changes in v1.0.35

**GitHub Copilot CLI** · 2026-04-23 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.35) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-04-23-v1-0-35-github-312982689-0111445c|1.0.35]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Configure Copilot agent now has shell access on Windows

> Self-correcting custom tool calls in agentic loop

> Custom agents and skills in ~/.claude/ are no longer incorrectly loaded as Copilot project config

> Sync task calls block until completion under MULTI_TURN_AGENTS instead of auto-promoting to background after 60s; sync no longer returns a reusable agent_id, use mode: "background" for follow-ups

> Auto mode no longer fails with an error when switching to a model that doesn't support the configured reasoning effort

> Hide subagent thinking from the timeline

> Custom agent name is now visible in the statusline footer and can be toggled via /statusline

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.35
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-04-23-6-editor-experience-changes-in-v1-0-35|6 Editor Experience changes in v1.0.35]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-04-23-tool-availability-detection-works-correctly-on-windows|Tool availability detection works correctly on Windows]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-04-23-2-account-and-access-changes-in-v1-0-35|2 Account and Access changes in v1.0.35]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-04-23-3-apps-and-integrations-changes-in-v1-0-35|3 Apps and Integrations changes in v1.0.35]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-04-23-4-interface-experience-changes-in-v1-0-35|4 Interface Experience changes in v1.0.35]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-04-23-2-context-window-changes-in-v1-0-35|2 Context Window changes in v1.0.35]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-04-23-2-model-support-changes-in-v1-0-35|2 Model Support changes in v1.0.35]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-04-23-improve-rendering-performance-when-displaying-large-amounts-of-text-in-the-timel|Improve rendering performance when displaying large amounts of text in the timeline]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-04-23-4-developer-workflow-changes-in-v1-0-35|4 Developer Workflow changes in v1.0.35]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-04-23-permission-prompts-appear-correctly-in-remote-sessions-for-the-cli-tui|Permission prompts appear correctly in remote sessions for the CLI TUI]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-04-23-12-other-changes-in-v1-0-35|12 other changes in v1.0.35]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-23 · Gemini CLI · [[Changes/Gemini CLI/2026-04-23-6-agent-mode-changes-in-v0-39-0|6 Agent Mode changes in v0.39.0]]
- Later: 2026-04-24 · Codex CLI · [[Changes/Codex CLI/2026-04-24-5-agent-mode-changes-in-rust-v0-125-0|5 Agent Mode changes in rust-v0.125.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-04-23-9cfbc6&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-04-23-7-agent-mode-changes-in-v1-0-35.md%0ACard%20ID%3A%20github-copilot-cli-2026-04-23-9cfbc6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.35%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->