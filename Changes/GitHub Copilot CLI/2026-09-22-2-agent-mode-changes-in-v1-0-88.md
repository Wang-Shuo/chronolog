---
card_id: github-copilot-cli-2026-09-22-3c9f76
date: '2026-09-22'
description: 'GitHub Copilot CLI · 2026-09-22 · Agent Mode: 2 changes in 1.0.88 —
  Custom-agent startup now distinguishes model-list load failures from an empty catalog…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1174
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 70c5402953860afa7f46ad4ebff67b35ef013b24170233608dd4c36734d097c8
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-22-3c9f76
  comparison: ''
  date: '2026-09-22'
  description: 'GitHub Copilot CLI — 1.0.88: 2 Agent Mode changes'
  evidence:
  - quote: Custom-agent startup now distinguishes model-list load failures from an
      empty catalog, preventing false unavailable warnings and silent required-agent
      deselection
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  - quote: A custom agent's `reasoning-effort` now applies when the agent is selected,
      instead of only its model. An explicit `--reasoning-effort` still wins, and
      a level the selected model does not offer is reported and left unapplied
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.88
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 2-agent-mode-changes-in-v1-0-88
  source_release: github-copilot-cli-2026-09-22-v1-0-88-github-394076851-2894d283
  source_type: github_releases
  theme: agent-mode
  title: 2 Agent Mode changes in v1.0.88
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-22-2-agent-mode-changes-in-v2-1-280|2 Agent Mode
  changes in v2.1.280]]'
- '[[Changes/Cline/2026-09-22-2-agent-mode-changes-in-v4-1-20|2 Agent Mode changes
  in v4.1.20]]'
- '[[Changes/Codex CLI/2026-09-22-34-agent-mode-changes-in-rust-v0-156-0|34 Agent
  Mode changes in rust-v0.156.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-22-v1-0-88-github-394076851-2894d283|github-copilot-cli-2026-09-22-v1-0-88-github-394076851-2894d283]]'
source_type: github_releases
theme: agent-mode
title: 2 Agent Mode changes in v1.0.88
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Agent Mode changes in v1.0.88

**GitHub Copilot CLI** · 2026-09-22 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.88) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-22-v1-0-88-github-394076851-2894d283|1.0.88]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Custom-agent startup now distinguishes model-list load failures from an empty catalog, preventing false unavailable warnings and silent required-agent deselection

> A custom agent's `reasoning-effort` now applies when the agent is selected, instead of only its model. An explicit `--reasoning-effort` still wins, and a level the selected model does not offer is reported and left unapplied

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.88
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-22-in-the-sessions-tab-rows-you-can-dismiss-now-take-x-then-x-again-to-confirm-a-lo|In the Sessions tab, rows you can dismiss now take x then x again to confirm]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-09-22-add-optional-osc-777-terminal-notifications-for-direct-ghostty-and-wezterm-sessi|Add optional OSC 777 terminal notifications for direct Ghostty and WezTerm sessions]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-09-22-resuming-large-local-sessions-keeps-transcript-memory-bounded-for-smoother-cli-p|Resuming large local sessions keeps transcript memory bounded for smoother CLI performance]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-09-22-3-account-and-access-changes-in-v1-0-88|3 Account and Access changes in v1.0.88]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-22-session-resume-preserves-pending-conversation-events-when-saving-fails-and-expla|Session resume preserves pending conversation events when saving fails and explains…]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-09-22-2-safety-and-privacy-changes-in-v1-0-88|2 Safety and Privacy changes in v1.0.88]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-09-22-6-apps-and-integrations-changes-in-v1-0-88|6 Apps and Integrations changes in v1.0.88]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-09-22-8-other-changes-in-v1-0-88|8 other changes in v1.0.88]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-22 · Codex CLI · [[Changes/Codex CLI/2026-09-22-34-agent-mode-changes-in-rust-v0-156-0|34 Agent Mode changes in rust-v0.156.0]]
- Later: 2026-09-22 · OpenHands · [[Changes/OpenHands/2026-09-22-docs-refresh-agents-md-guidance-by-all-hands-bot-in-https-github-com-openhands-o|docs: refresh AGENTS.md guidance]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-22-3c9f76&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-22-2-agent-mode-changes-in-v1-0-88.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-22-3c9f76%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.88%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->