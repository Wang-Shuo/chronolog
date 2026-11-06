---
card_id: github-copilot-cli-2026-06-30-e8499c
date: '2026-06-30'
description: 'GitHub Copilot CLI · 2026-06-30 · Agent Mode: 8 changes in 1.0.66 —
  Hide excluded built-in agents from agent selection'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1090
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 43b3e62bb8e9c57ce33612abe10b327356929652c00cebf8198f44c4224bb586
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-30-e8499c
  comparison: ''
  date: '2026-06-30'
  description: 'GitHub Copilot CLI — 1.0.66: 8 Agent Mode changes'
  evidence:
  - quote: Hide excluded built-in agents from agent selection
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: 'read_agent since_turn: 0 now correctly returns all turns including turn
      0'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Expand @-style imports in AGENTS.md, CLAUDE.md, and Copilot instruction
      files
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Keep idle agents available after you cancel a turn
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Let custom agents set reasoning effort in their definitions
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: 'Guide the agent to format cross-repository issue/PR references as owner/repo#number
      (reserving bare #number for the current repo) so they don''t mislink to the
      current repository'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: COPILOT_HOME and --config-dir stop loading skills from ~/.agents/skills
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Show the active agent mode in the working footer text
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 8-agent-mode-changes-in-v1-0-66
  source_release: github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740
  source_type: github_releases
  theme: agent-mode
  title: 8 Agent Mode changes in v1.0.66
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-06-29-elevenagents-d1c29a|ElevenAgents]]'
- "[[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|\U0001FAAA
  Client User-Agent forwarded to model backends. The browser's User-Agent is now…]]"
- '[[Changes/GitHub Copilot CLI/2026-06-30-2-agent-mode-changes-in-v1-0-67|2 Agent
  Mode changes in v1.0.67]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740|github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740]]'
source_type: github_releases
theme: agent-mode
title: 8 Agent Mode changes in v1.0.66
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Agent Mode changes in v1.0.66

**GitHub Copilot CLI** · 2026-06-30 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.66) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740|1.0.66]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hide excluded built-in agents from agent selection

> read_agent since_turn: 0 now correctly returns all turns including turn 0

> Expand @-style imports in AGENTS.md, CLAUDE.md, and Copilot instruction files

> Keep idle agents available after you cancel a turn

> Let custom agents set reasoning effort in their definitions

> Guide the agent to format cross-repository issue/PR references as owner/repo#number (reserving bare #number for the current repo) so they don't mislink to the current repository

> COPILOT_HOME and --config-dir stop loading skills from ~/.agents/skills

> Show the active agent mode in the working footer text

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.66
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-30-2-editor-experience-changes-in-v1-0-66|2 Editor Experience changes in v1.0.66]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-30-voice-mode-turns-itself-off-when-the-engine-fails-to-start-at-boot|Voice mode turns itself off when the engine fails to start at boot]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-06-30-perform-tokenizer-warmup-in-parallel-on-a-background-thread-for-better-startup-p|Perform tokenizer warmup in parallel on a background thread for better startup performance]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-30-2-collaboration-changes-in-v1-0-66|2 Collaboration changes in v1.0.66]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-06-30-pr-auto-now-starts-a-self-paced-loop-that-fixes-one-thing-per-run-and-paces-itse|/pr auto now starts a self-paced loop that fixes one thing per run and paces itself…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-30-3-interface-experience-changes-in-v1-0-66|3 Interface Experience changes in v1.0.66]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-30-9-apps-and-integrations-changes-in-v1-0-66|9 Apps and Integrations changes in v1.0.66]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-30-match-the-terminal-text-color-to-the-github-theme-canvas|Match the terminal text color to the GitHub theme canvas]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-06-30-21-developer-workflow-changes-in-v1-0-66|21 Developer Workflow changes in v1.0.66]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-30-6-account-and-access-changes-in-v1-0-66|6 Account and Access changes in v1.0.66]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-30-configure-subagent-concurrency-and-depth-limits-in-settings-usage-based-billing|Configure subagent concurrency and depth limits in /settings (usage-based billing users)]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-06-30-2-mobile-and-desktop-changes-in-v1-0-66|2 Mobile and Desktop changes in v1.0.66]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-06-30-3-safety-and-privacy-changes-in-v1-0-66|3 Safety and Privacy changes in v1.0.66]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-30-recover-corrupted-session-history-on-load|Recover corrupted session history on load]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-06-30-keep-session-store-searches-and-context-lookups-responsive|Keep session-store searches and context lookups responsive]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-30-5-model-support-changes-in-v1-0-66|5 Model Support changes in v1.0.66]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-30-33-other-changes-in-v1-0-66|33 other changes in v1.0.66]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-2-agent-mode-changes-in-v1-0-67|2 Agent Mode changes in v1.0.67]]
- Later: 2026-07-01 · Claude Code · [[Changes/Claude Code/2026-07-01-5-agent-mode-changes-in-v2-1-198|5 Agent Mode changes in v2.1.198]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-30-e8499c&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-30-8-agent-mode-changes-in-v1-0-66.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-30-e8499c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.66%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->