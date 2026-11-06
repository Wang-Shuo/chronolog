---
card_id: codex-cli-2026-05-18-bb34ae
date: '2026-05-18'
description: 'Codex CLI · 2026-05-18 · Editor Experience: #21954 Fix goal update and
  add `/goal edit` command in TUI @etraut-openai'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1161
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: f91eda0f3c0bd2610f3a259ceae6af6d6409a2b7e3633e3ff80c4b05792819f4
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-18-bb34ae
  comparison: ''
  date: '2026-05-18'
  description: 'Codex CLI — 0.131.0: #21954 Fix goal update and add `/goal edit` command
    in TUI @etraut-openai'
  evidence:
  - quote: '#21954 Fix goal update and add `/goal edit` command in TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: 21954-fix-goal-update-and-add-goal-edit-command-in-tui-etraut-openai
  source_release: codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d
  source_type: github_releases
  theme: editor-experience
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: '#21954 Fix goal update and add `/goal edit` command in TUI @etraut-openai'
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-12-read-only-gh-cli-commands-list-view-status-diff-etc-are-auto-approved-without-pr|Read-only
  gh CLI commands (list, view, status, diff, etc.) are auto-approved without…]]'
- '[[Changes/Cursor/2026-05-13-improved-pr-tabs-by-adding-clearer-review-states-better-reviewer-thread-visibili|Improved
  PR tabs by adding clearer review states, better reviewer/thread visibility…]]'
- '[[Changes/Claude Code/2026-05-15-bg-and-detach-now-preserve-allow-dangerously-skip-permissions-so-the-forked-work|/bg
  and ←-detach now preserve --allow-dangerously-skip-permissions…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d]]'
source_type: github_releases
theme: editor-experience
title: ♯21954 Fix goal update and add /goal edit command in TUI @etraut-openai
type: change
---

<!-- chronolog:begin region="header" -->
# #21954 Fix goal update and add `/goal edit` command in TUI @etraut-openai

**Codex CLI** · 2026-05-18 · [[Themes/editor-experience|Editor Experience]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.131.0) · from [[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|0.131.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> #21954 Fix goal update and add `/goal edit` command in TUI @etraut-openai
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.131.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-18-5-account-and-access-changes-in-rust-v0-131-0|5 Account and Access changes in rust-v0.131.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-18-17-safety-and-privacy-changes-in-rust-v0-131-0|17 Safety and Privacy changes in rust-v0.131.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-18-9-agent-mode-changes-in-rust-v0-131-0|9 Agent Mode changes in rust-v0.131.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-18-4-memory-and-personalization-changes-in-rust-v0-131-0|4 Memory and Personalization changes in rust-v0.131.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-18-5-interface-experience-changes-in-rust-v0-131-0|5 Interface Experience changes in rust-v0.131.0]] · Interface Experience
- [[Changes/Codex CLI/2026-05-18-12-developer-workflow-changes-in-rust-v0-131-0|12 Developer Workflow changes in rust-v0.131.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-18-56-apps-and-integrations-changes-in-rust-v0-131-0|56 Apps and Integrations changes in rust-v0.131.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-18-10-mobile-and-desktop-changes-in-rust-v0-131-0|10 Mobile and Desktop changes in rust-v0.131.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-18-7-context-window-changes-in-rust-v0-131-0|7 Context Window changes in rust-v0.131.0]] · Context Window
- [[Changes/Codex CLI/2026-05-18-3-collaboration-changes-in-rust-v0-131-0|3 Collaboration changes in rust-v0.131.0]] · Collaboration
- [[Changes/Codex CLI/2026-05-18-4-model-support-changes-in-rust-v0-131-0|4 Model Support changes in rust-v0.131.0]] · Model Support
- [[Changes/Codex CLI/2026-05-18-155-other-changes-in-rust-v0-131-0|155 other changes in rust-v0.131.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-05-15 · Claude Code · [[Changes/Claude Code/2026-05-15-bg-and-detach-now-preserve-allow-dangerously-skip-permissions-so-the-forked-work|/bg and ←-detach now preserve --allow-dangerously-skip-permissions…]]
- Later: 2026-05-19 · Claude Code · [[Changes/Claude Code/2026-05-19-fewer-spurious-tool-errors-during-search-head-tail-file-views-now-satisfy-the-re|Fewer spurious tool errors during search]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-18-bb34ae&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-18-21954-fix-goal-update-and-add-goal-edit-command-in-tui-etraut-openai.md%0ACard%20ID%3A%20codex-cli-2026-05-18-bb34ae%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.131.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->