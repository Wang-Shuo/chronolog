---
card_id: cline-2026-09-17-e59cdb
date: '2026-09-17'
description: 'Cline · 2026-09-17 · Apps and Integrations: Terminal commands that succeed
  without printing anything (`git add -A` on a clean tree, for example) are now…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1274
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 931a8155a1987990b1ceaa415a036c8cb4b14e88a50f9e0331e980bdf18d3c16
product: cline
product_name: Cline
record:
  ai_generated: true
  card_id: cline-2026-09-17-e59cdb
  comparison: ''
  confidence: low
  date: '2026-09-17'
  description: 'Cline — v4.1.19: Terminal commands that succeed without printing anything
    (`git add -A` on a clean tree, for example) are now reported as empty output.
    They were treated as a shell-integration failure, which fed the model a snapshot
    of unrelated terminal scrollback prefixed with a warning that the output could
    not be captured, so silent commands intermittently looked like failures.'
  evidence:
  - quote: Terminal commands that succeed without printing anything (`git add -A`
      on a clean tree, for example) are now reported as empty output. They were treated
      as a shell-integration failure, which fed the model a snapshot of unrelated
      terminal scrollback prefixed with a warning that the output could not be captured,
      so silent commands intermittently looked like failures.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: cline
  product_name: Cline
  slug: terminal-commands-that-succeed-without-printing-anything-git-add-a-on-a-clean-tr
  source_release: cline-2026-09-17-v4-1-19-github-390521944-270e9514
  source_type: github_releases
  theme: apps-integrations
  theme_matches:
  - matched_terms:
    - integration
    score: 50
    theme: apps-integrations
  - matched_terms:
    - terminal
    score: 50
    theme: developer-workflow
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: Terminal commands that succeed without printing anything…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-17-10-apps-and-integrations-changes-in-v2-1-274|10
  Apps and Integrations changes in v2.1.274]]'
- '[[Changes/Claude Code/2026-09-17-6-apps-and-integrations-changes-in-v2-1-275|6
  Apps and Integrations changes in v2.1.275]]'
- '[[Changes/Claude Code/2026-09-17-added-plugin-install-plugin-marketplace-source-which-offers-to-add-the-marketpla|Added
  /plugin install plugin --marketplace source, which offers to add…]]'
source_release: '[[Releases/Cline/cline-2026-09-17-v4-1-19-github-390521944-270e9514|cline-2026-09-17-v4-1-19-github-390521944-270e9514]]'
source_type: github_releases
theme: apps-integrations
title: Terminal commands that succeed without printing anything…
type: change
---

<!-- chronolog:begin region="header" -->
# Terminal commands that succeed without printing anything…

**Cline** · 2026-09-17 · [[Themes/apps-integrations|Apps and Integrations]] · [Official source](https://github.com/cline/cline/releases/tag/v4.1.19) · from [[Releases/Cline/cline-2026-09-17-v4-1-19-github-390521944-270e9514|v4.1.19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Terminal commands that succeed without printing anything (`git add -A` on a clean tree, for example) are now reported as empty output. They were treated as a shell-integration failure, which fed the model a snapshot of unrelated terminal scrollback prefixed with a warning that the output could not be captured, so silent commands intermittently looked like failures.
>
> Source: https://github.com/cline/cline/releases/tag/v4.1.19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-09-17-on-windows-opening-a-repository-that-contains-a-file-named-rg-exe-git-exe-or-pow|On Windows, opening a repository that contains a file named rg.exe, git.exe…]] · Mobile and Desktop
- [[Changes/Cline/2026-09-17-13-model-support-changes-in-v4-1-19|13 Model Support changes in v4.1.19]] · Model Support
- [[Changes/Cline/2026-09-17-2-developer-workflow-changes-in-v4-1-19|2 Developer Workflow changes in v4.1.19]] · Developer Workflow
- [[Changes/Cline/2026-09-17-task-history-no-longer-goes-blank-when-a-task-spawns-many-subagents-subagent-row|Task history no longer goes blank when a task spawns many subagents]] · Agent Mode
- [[Changes/Cline/2026-09-17-long-tasks-now-compact-when-they-actually-need-to-rather-than-running-out-of-roo|Long tasks now compact when they actually need to rather than running out of room]] · Context Window
- [[Changes/Cline/2026-09-17-cline-pass-now-defaults-to-a-model-from-your-subscription-rather-than-a-free-one|Cline Pass now defaults to a model from your subscription rather than a free one]] · Pricing Model
- [[Changes/Cline/2026-09-17-web-search-is-now-enabled-by-default-on-models-that-support-it-outside-yolo-mode|Web search is now enabled by default on models that support it, outside YOLO mode]] · Search and Browsing
- [[Changes/Cline/2026-09-17-cline-s-logo-and-icons-have-been-refreshed-throughout-the-extension-including-th|Cline's logo and icons have been refreshed throughout the extension, including…]] · Interface Experience
- [[Changes/Cline/2026-09-17-5-other-changes-in-v4-1-19|5 other changes in v4.1.19]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-added-plugin-install-plugin-marketplace-source-which-offers-to-add-the-marketpla|Added /plugin install plugin --marketplace source, which offers to add…]]
- Later: 2026-09-17 · Codex CLI · [[Changes/Codex CLI/2026-09-17-24-apps-and-integrations-changes-in-rust-v0-155-0|24 Apps and Integrations changes in rust-v0.155.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-09-17-e59cdb&body=Card%3A%20Changes%2FCline%2F2026-09-17-terminal-commands-that-succeed-without-printing-anything-git-add-a-on-a-clean-tr.md%0ACard%20ID%3A%20cline-2026-09-17-e59cdb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->