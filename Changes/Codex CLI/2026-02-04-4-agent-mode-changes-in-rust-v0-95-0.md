---
card_id: codex-cli-2026-02-04-aca672
date: '2026-02-04'
description: 'Codex CLI · 2026-02-04 · Agent Mode: 4 changes in 0.95.0 — Added personal
  skill loading from `~/.agents/skills` (with `~/.codex/skills` compatibility), plus…'
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
machine_hash: b6b04e9dab3ff8ae8e326e49a02129142bab2c2157e85bd0b4e07ce154e4571e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-04-aca672
  comparison: ''
  date: '2026-02-04'
  description: 'Codex CLI — 0.95.0: 4 Agent Mode changes'
  evidence:
  - quote: 'Added personal skill loading from `~/.agents/skills` (with `~/.codex/skills`
      compatibility), plus app-server APIs/events to list and download public remote
      skills. (#10437, #10448)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10437 feat: Read personal skills from .agents/skills @gverma-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10447 Fix plan implementation prompt reappearing after /agent thread
      switch @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  - quote: '#10524 fix: make $PWD/.agents read-only like $PWD/.codex @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.95.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-agent-mode-changes-in-rust-v0-95-0
  source_release: codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b
  source_type: github_releases
  theme: agent-mode
  title: 4 Agent Mode changes in rust-v0.95.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-03-added-token-count-tool-uses-and-duration-metrics-to-task-tool-results|Added
  token count, tool uses, and duration metrics to Task tool results]]'
- '[[Changes/GitHub Copilot CLI/2026-02-03-4-agent-mode-changes-in-v0-0-402|4 Agent
  Mode changes in v0.0.402]]'
- '[[Changes/GitHub Copilot CLI/2026-02-03-support-agents-skills-directory-for-auto-loading-skills|Support
  .agents/skills directory for auto-loading skills]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b|codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b]]'
source_type: github_releases
theme: agent-mode
title: 4 Agent Mode changes in rust-v0.95.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in rust-v0.95.0

**Codex CLI** · 2026-02-04 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.95.0) · from [[Releases/Codex CLI/codex-cli-2026-02-04-rust-v0-95-0-github-282823276-932b0b6b|0.95.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added personal skill loading from `~/.agents/skills` (with `~/.codex/skills` compatibility), plus app-server APIs/events to list and download public remote skills. (#10437, #10448)

> #10437 feat: Read personal skills from .agents/skills @gverma-openai

> #10447 Fix plan implementation prompt reappearing after /agent thread switch @charley-oai

> #10524 fix: make $PWD/.agents read-only like $PWD/.codex @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.95.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-04-10-developer-workflow-changes-in-rust-v0-95-0|10 Developer Workflow changes in rust-v0.95.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-04-10340-session-picker-shows-thread-name-if-set-pap-openai|♯10340 Session picker shows thread_name if set @pap-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-02-04-2-context-window-changes-in-rust-v0-95-0|2 Context Window changes in rust-v0.95.0]] · Context Window
- [[Changes/Codex CLI/2026-02-04-10404-cleanup-collaboration-mode-variants-charley-oai|♯10404 Cleanup collaboration mode variants @charley-oai]] · Collaboration
- [[Changes/Codex CLI/2026-02-04-2-mobile-and-desktop-changes-in-rust-v0-95-0|2 Mobile and Desktop changes in rust-v0.95.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-04-2-model-support-changes-in-rust-v0-95-0|2 Model Support changes in rust-v0.95.0]] · Model Support
- [[Changes/Codex CLI/2026-02-04-10274-add-credits-tooltip-pakrym-oai|♯10274 Add credits tooltip @pakrym-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-02-04-6-safety-and-privacy-changes-in-rust-v0-95-0|6 Safety and Privacy changes in rust-v0.95.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-04-5-apps-and-integrations-changes-in-rust-v0-95-0|5 Apps and Integrations changes in rust-v0.95.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-04-2-search-and-browsing-changes-in-rust-v0-95-0|2 Search and Browsing changes in rust-v0.95.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-02-04-42-other-changes-in-rust-v0-95-0|42 other changes in rust-v0.95.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-02-03 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-03-support-agents-skills-directory-for-auto-loading-skills|Support .agents/skills directory for auto-loading skills]]
- Later: 2026-02-04 · Gemini CLI · [[Changes/Gemini CLI/2026-02-04-15-agent-mode-changes-in-v0-27-0|15 Agent Mode changes in v0.27.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-04-aca672&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-04-4-agent-mode-changes-in-rust-v0-95-0.md%0ACard%20ID%3A%20codex-cli-2026-02-04-aca672%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.95.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->