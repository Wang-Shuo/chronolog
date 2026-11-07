---
card_id: github-copilot-cli-2026-06-01-b0521f
date: '2026-06-01'
description: 'GitHub Copilot CLI · 2026-06-01 · Agent Mode: Canceling a running shell
  command (Ctrl+C on a !command, or aborting an agent command — including in sandboxed…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1061
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: change
machine_hash: 1367a363266777b6bbdd8a184fd8d3273a023ee5bbc4939174ac6324563054d2
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  ai_generated: true
  card_id: github-copilot-cli-2026-06-01-b0521f
  comparison: ''
  confidence: low
  date: '2026-06-01'
  description: 'GitHub Copilot CLI — 1.0.57: Canceling a running shell command (Ctrl+C
    on a !command, or aborting an agent command — including in sandboxed and background-promoted
    shells) now terminates the whole process tree instead of leaving orphaned processes
    running'
  evidence:
  - quote: Canceling a running shell command (Ctrl+C on a !command, or aborting an
      agent command — including in sandboxed and background-promoted shells) now terminates
      the whole process tree instead of leaving orphaned processes running
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.57
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: change
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: canceling-a-running-shell-command-ctrl-c-on-a-command-or-aborting-an-agent-comma
  source_release: github-copilot-cli-2026-06-01-v1-0-57-github-332702409-1dd8346d
  source_type: github_releases
  theme: agent-mode
  title: Canceling a running shell command (Ctrl+C on a !command, or aborting an agent
    command
  type: change
related_changes:
- '[[Changes/Replit/2026-05-29-agent|Agent]]'
- '[[Changes/Replit/2026-05-29-agent-can-generate-music-sound-effects-and-speech|Agent
  can generate music, sound effects, and speech]]'
- '[[Changes/Codex CLI/2026-06-01-3-agent-mode-changes-in-rust-v0-136-0|3 Agent Mode
  changes in rust-v0.136.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-01-v1-0-57-github-332702409-1dd8346d|github-copilot-cli-2026-06-01-v1-0-57-github-332702409-1dd8346d]]'
source_type: github_releases
theme: agent-mode
title: Canceling a running shell command (Ctrl+C on a !command, or aborting an agent
  command
type: change
---

<!-- chronolog:begin region="header" -->
# Canceling a running shell command (Ctrl+C on a !command, or aborting an agent command

**GitHub Copilot CLI** · 2026-06-01 · [[Themes/agent-mode|Agent Mode]] · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.57) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-01-v1-0-57-github-332702409-1dd8346d|1.0.57]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Canceling a running shell command (Ctrl+C on a !command, or aborting an agent command — including in sandboxed and background-promoted shells) now terminates the whole process tree instead of leaving orphaned processes running
>
> Source: https://github.com/github/copilot-cli/releases/tag/v1.0.57
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-01-new-reasoning-after-tool-calls-appears-at-the-bottom-of-the-timeline-instead-of|New reasoning after tool calls appears at the bottom of the timeline instead…]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-01-surface-the-underlying-reason-e-g-github-api-rate-limit-when-sdk-auth-token-vali|Surface the underlying reason (e.g. GitHub API rate limit) when SDK auth-token…]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-01-canvas-providers-can-return-file-urls-in-open-results-for-local-file-previews|Canvas providers can return file:// URLs in open results for local file previews]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-06-01-2-search-and-browsing-changes-in-v1-0-57|2 Search and Browsing changes in v1.0.57]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-06-01-session-resume-works-correctly-after-a-crash-that-left-partial-data-in-the-sessi|Session resume works correctly after a crash that left partial data in the session log]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-06-01-5-apps-and-integrations-changes-in-v1-0-57|5 Apps and Integrations changes in v1.0.57]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-01-lsp-show-lsp-test-and-lsp-reload-correctly-discover-project-lsp-config-when-the|/lsp show, /lsp test, and /lsp reload correctly discover project LSP config…]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-01-9-editor-experience-changes-in-v1-0-57|9 Editor Experience changes in v1.0.57]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-01-9-other-changes-in-v1-0-57|9 other changes in v1.0.57]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-01 · Codex CLI · [[Changes/Codex CLI/2026-06-01-3-agent-mode-changes-in-rust-v0-136-0|3 Agent Mode changes in rust-v0.136.0]]
- Later: 2026-06-02 · Claude Code · [[Changes/Claude Code/2026-06-02-improved-performance-of-opening-recently-inactive-background-agent-sessions-in-c|Improved performance of opening recently-inactive background agent sessions…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-01-b0521f&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-01-canceling-a-running-shell-command-ctrl-c-on-a-command-or-aborting-an-agent-comma.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-01-b0521f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.57%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->