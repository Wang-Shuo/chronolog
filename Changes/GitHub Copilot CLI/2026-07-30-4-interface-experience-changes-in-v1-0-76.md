---
card_id: github-copilot-cli-2026-07-30-eb90c1
date: '2026-07-30'
description: 'GitHub Copilot CLI · 2026-07-30 · Interface Experience: 4 changes in
  1.0.76 — Split-view sidebar: hover-to-focus is now off by default (opt in with…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1298
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 81c7393d9bf267a513445eac828e9efb6ccc3316a945f807ef97affc67606b09
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-07-30-eb90c1
  comparison: ''
  date: '2026-07-30'
  description: 'GitHub Copilot CLI — 1.0.76: 4 Interface Experience changes'
  evidence:
  - quote: 'Split-view sidebar: hover-to-focus is now off by default (opt in with
      `sidebar.hoverFocus`), the active session card is accented by default (opt out
      with `sidebar.accentActiveSession`), and the closed-state `open sidebar` hint
      always renders in the neutral hint color'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: 'New Sessions sidebar for managing multiple concurrent sessions: switch
      between them, spawn new ones, and see their status at a glance. Turn it on with
      experimental mode (`/experimental on`).'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: The /instructions picker now respects --no-custom-instructions.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: Add configurable timed refreshes for custom status-line commands
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-interface-experience-changes-in-v1-0-76
  source_release: github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29
  source_type: github_releases
  theme: interface-experience
  title: 4 Interface Experience changes in v1.0.76
  type: change
related_changes:
- '[[Changes/Cursor/2026-07-28-existing-free-users-in-india-can-upgrade-their-plan-from-the-dashboard-new-users-aeb811|Existing
  Free users in India can upgrade their plan from the dashboard]]'
- '[[Changes/Dify/2026-07-28-10-interface-experience-changes-in-1-16-1|10 Interface
  Experience changes in 1.16.1]]'
- '[[Changes/Codex CLI/2026-07-29-8-interface-experience-changes-in-rust-v0-146-0|8
  Interface Experience changes in rust-v0.146.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29|github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29]]'
source_type: github_releases
theme: interface-experience
title: 4 Interface Experience changes in v1.0.76
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Interface Experience changes in v1.0.76

**GitHub Copilot CLI** · 2026-07-30 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.76) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29|1.0.76]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Split-view sidebar: hover-to-focus is now off by default (opt in with `sidebar.hoverFocus`), the active session card is accented by default (opt out with `sidebar.accentActiveSession`), and the closed-state `open sidebar` hint always renders in the neutral hint color

> New Sessions sidebar for managing multiple concurrent sessions: switch between them, spawn new ones, and see their status at a glance. Turn it on with experimental mode (`/experimental on`).

> The /instructions picker now respects --no-custom-instructions.

> Add configurable timed refreshes for custom status-line commands

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.76
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-07-30-5-safety-and-privacy-changes-in-v1-0-76|5 Safety and Privacy changes in v1.0.76]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-07-30-a-userpromptsubmitted-hook-returning-a-non-string-value-for-modifiedprompt-modif|A userPromptSubmitted hook returning a non-string value for modifiedPrompt…]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-07-30-diff-scrolls-and-syntax-highlights-large-multi-file-diffs-faster|/diff scrolls and syntax-highlights large multi-file diffs faster]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-07-30-2-developer-workflow-changes-in-v1-0-76|2 Developer Workflow changes in v1.0.76]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-07-30-2-apps-and-integrations-changes-in-v1-0-76|2 Apps and Integrations changes in v1.0.76]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-07-30-2-model-support-changes-in-v1-0-76|2 Model Support changes in v1.0.76]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-07-30-restore-the-early-warning-when-unreclaimable-system-and-tool-context-nears-the-l|Restore the early warning when unreclaimable system and tool context nears…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-07-30-voice-mode-pauses-playing-media-before-recording-and-resumes-it-afterward-where|Voice mode pauses playing media before recording and resumes it afterward, where…]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-07-30-2-agent-mode-changes-in-v1-0-76|2 Agent Mode changes in v1.0.76]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-07-30-2-editor-experience-changes-in-v1-0-76|2 Editor Experience changes in v1.0.76]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-07-30-10-other-changes-in-v1-0-76|10 other changes in v1.0.76]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-07-29 · Codex CLI · [[Changes/Codex CLI/2026-07-29-8-interface-experience-changes-in-rust-v0-146-0|8 Interface Experience changes in rust-v0.146.0]]
- Later: 2026-07-31 · v0 · [[Changes/v0/2026-07-31-3-interface-experience-changes-in-claude-opus-5-direct-figma-inspection|3 Interface Experience changes in Claude Opus 5, direct Figma inspection…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-07-30-eb90c1&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-07-30-4-interface-experience-changes-in-v1-0-76.md%0ACard%20ID%3A%20github-copilot-cli-2026-07-30-eb90c1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.76%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->