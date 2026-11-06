---
card_id: codex-cli-2026-03-16-32d4bd
date: '2026-03-16'
description: 'Codex CLI · 2026-03-16 · Agent Mode: 16 changes in 0.115.0 — Smart Approvals
  can now route review requests through a guardian subagent in core, app-server, and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 984
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 13ce3cb78fb252fe073ec543cb9f932f730179e02a5e55c1ee4a67590a6da9c7
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-16-32d4bd
  comparison: ''
  date: '2026-03-16'
  description: 'Codex CLI — 0.115.0: 16 Agent Mode changes'
  evidence:
  - quote: 'Smart Approvals can now route review requests through a guardian subagent
      in core, app-server, and TUI, reducing repeated setup work on follow-up approvals.
      (#13860, #14668)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: 'The TUI no longer stalls on exit after creating subagents, and interrupting
      a turn no longer tears down background terminals by default. (#14816, #14602)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: The subagent wait tool is now consistently named `wait_agent`, aligning
      it with `spawn_agent` and `send_input`. (#14631)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14376 Keep agent-switch word-motion keys out of draft editing @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14432 Clarify spawn agent authorization @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14488 Handle malformed agent role definitions nonfatally @gabec-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14535 Split multi-agent handlers per tool @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14536 Add typed multi-agent tool outputs @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14603 Split multi-agent handler into dedicated files @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14618 Use subagents naming in the TUI @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14631 Rename multi-agent wait tool to wait_agent @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14622 Stabilize multi-agent feature flag @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14637 Fix wait_agent expectations in core tests @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14807 fix: sub-agent role when using profiles @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#13850 feat: make interrupt state not final for multi-agents @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14816 fix: tui freeze when sub-agents are present @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 16-agent-mode-changes-in-rust-v0-115-0
  source_release: codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db
  source_type: github_releases
  theme: agent-mode
  title: 16 Agent Mode changes in rust-v0.115.0
  type: change
related_changes:
- '[[Changes/Cline/2026-03-12-added-github-copilot-instructions-md-for-coding-agents|Added
  .github/copilot-instructions.md for coding agents]]'
- '[[Changes/GitHub Copilot CLI/2026-03-13-send-follow-up-messages-to-background-agents-with-the-write-agent-tool-for-multi|Send
  follow-up messages to background agents with the write_agent tool…]]'
- '[[Changes/Claude Code/2026-03-14-improved-background-agent-behavior-killing-a-background-agent-now-preserves-its|Improved
  background agent behavior]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db|codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db]]'
source_type: github_releases
theme: agent-mode
title: 16 Agent Mode changes in rust-v0.115.0
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Agent Mode changes in rust-v0.115.0

**Codex CLI** · 2026-03-16 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.115.0) · from [[Releases/Codex CLI/codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db|0.115.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Smart Approvals can now route review requests through a guardian subagent in core, app-server, and TUI, reducing repeated setup work on follow-up approvals. (#13860, #14668)

> The TUI no longer stalls on exit after creating subagents, and interrupting a turn no longer tears down background terminals by default. (#14816, #14602)

> The subagent wait tool is now consistently named `wait_agent`, aligning it with `spawn_agent` and `send_input`. (#14631)

> #14376 Keep agent-switch word-motion keys out of draft editing @joshka-oai

> #14432 Clarify spawn agent authorization @aibrahim-oai

> #14488 Handle malformed agent role definitions nonfatally @gabec-openai

> #14535 Split multi-agent handlers per tool @pakrym-oai

> #14536 Add typed multi-agent tool outputs @pakrym-oai

> #14603 Split multi-agent handler into dedicated files @pakrym-oai

> #14618 Use subagents naming in the TUI @aibrahim-oai

> #14631 Rename multi-agent wait tool to wait_agent @aibrahim-oai

> #14622 Stabilize multi-agent feature flag @aibrahim-oai

> #14637 Fix wait_agent expectations in core tests @charley-oai

> #14807 fix: sub-agent role when using profiles @jif-oai

> #13850 feat: make interrupt state not final for multi-agents @jif-oai

> #14816 fix: tui freeze when sub-agents are present @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.115.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-16-17-apps-and-integrations-changes-in-rust-v0-115-0|17 Apps and Integrations changes in rust-v0.115.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-16-2-context-window-changes-in-rust-v0-115-0|2 Context Window changes in rust-v0.115.0]] · Context Window
- [[Changes/Codex CLI/2026-03-16-2-mobile-and-desktop-changes-in-rust-v0-115-0|2 Mobile and Desktop changes in rust-v0.115.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-16-4-voice-and-audio-changes-in-rust-v0-115-0|4 Voice and Audio changes in rust-v0.115.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-16-14493-memories-focus-write-prompts-on-user-preferences-andi-oai|♯14493 memories: focus write prompts on user preferences @andi-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-16-9-safety-and-privacy-changes-in-rust-v0-115-0|9 Safety and Privacy changes in rust-v0.115.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-16-5-model-support-changes-in-rust-v0-115-0|5 Model Support changes in rust-v0.115.0]] · Model Support
- [[Changes/Codex CLI/2026-03-16-2-account-and-access-changes-in-rust-v0-115-0|2 Account and Access changes in rust-v0.115.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-16-2-developer-workflow-changes-in-rust-v0-115-0|2 Developer Workflow changes in rust-v0.115.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-16-14410-make-collab-model-metadata-accurate-on-completion-aibrahim-oai|♯14410 Make collab model metadata accurate on completion @aibrahim-oai]] · Interface Experience
- [[Changes/Codex CLI/2026-03-16-70-other-changes-in-rust-v0-115-0|70 other changes in rust-v0.115.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-03-14 · Claude Code · [[Changes/Claude Code/2026-03-14-improved-background-agent-behavior-killing-a-background-agent-now-preserves-its|Improved background agent behavior]]
- Later: 2026-03-16 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-16-5-agent-mode-changes-in-v1-0-6|5 Agent Mode changes in v1.0.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-16-32d4bd&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-16-16-agent-mode-changes-in-rust-v0-115-0.md%0ACard%20ID%3A%20codex-cli-2026-03-16-32d4bd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.115.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->