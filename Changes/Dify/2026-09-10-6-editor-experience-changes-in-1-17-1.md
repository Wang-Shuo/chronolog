---
card_id: dify-2026-09-10-d7f1bd
date: '2026-09-10'
description: 'Dify · 2026-09-10 · Editor Experience: 6 changes in v1.17.1 - Bug Fixes
  and Improvements — **Human Input could not be placed inside Iteration or Loop nodes**…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2860
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 97755b6cbd49d7af05bf1e330791ba595c7189de369f3ab385535173220de2d6
product: dify
product_name: Dify
record:
  card_id: dify-2026-09-10-d7f1bd
  comparison: ''
  date: '2026-09-10'
  description: 'Dify — v1.17.1 - Bug Fixes and Improvements: 6 Editor Experience changes'
  evidence:
  - quote: '**Human Input could not be placed inside Iteration or Loop nodes**, even
      though 1.17.0 shipped the runtime support for it — two stale editor guards still
      blocked selecting, connecting, and pasting the node inside a container. (#40061)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**The Human Input timeout edge could fire the wrong branch.** The editor
      writes the timeout edge as `__timeout`, but the backend compared against `__timeout__`,
      so at runtime a timeout could take a user-action branch instead of the timeout
      branch the author drew. (#40746)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: Object editor values are stringified before Monaco creates a model, instead
      of failing on non-string input (#41719)
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: Revert your temporary image edits, then continue with the normal upgrade
      steps below.
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: Open a large workflow in the editor and confirm it no longer reconnect-loops.
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'refactor(web): remove obsolete agent v2 scaffolding and editor state by
      @lyzno1 in https://github.com/langgenius/dify/pull/41931'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 6-editor-experience-changes-in-1-17-1
  source_release: dify-2026-09-10-1-17-1-github-386157159-e472b6fe
  source_type: github_releases
  theme: editor-experience
  title: 6 Editor Experience changes in 1.17.1
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-09-09-2-editor-experience-changes-in-hub-v2-13-0-introducing-new-documents|2
  Editor Experience changes in HUB v2.13.0 — Introducing new Documents…]]'
- '[[Changes/Lovable/2026-09-09-explore-changes-with-drafts|Explore changes with drafts]]'
- '[[Changes/Claude Code/2026-09-10-added-browser-tab-icons-for-published-artifacts-chosen-by-claude-to-match-each-p|Added
  browser-tab icons for published artifacts, chosen by Claude to match each page]]'
source_release: '[[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|dify-2026-09-10-1-17-1-github-386157159-e472b6fe]]'
source_type: github_releases
theme: editor-experience
title: 6 Editor Experience changes in 1.17.1
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Editor Experience changes in 1.17.1

**Dify** · 2026-09-10 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.1) · from [[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|v1.17.1 - Bug Fixes and Improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Human Input could not be placed inside Iteration or Loop nodes**, even though 1.17.0 shipped the runtime support for it — two stale editor guards still blocked selecting, connecting, and pasting the node inside a container. (#40061)

> **The Human Input timeout edge could fire the wrong branch.** The editor writes the timeout edge as `__timeout`, but the backend compared against `__timeout__`, so at runtime a timeout could take a user-action branch instead of the timeout branch the author drew. (#40746)

> Object editor values are stringified before Monaco creates a model, instead of failing on non-string input (#41719)

> Revert your temporary image edits, then continue with the normal upgrade steps below.

> Open a large workflow in the editor and confirm it no longer reconnect-loops.

> refactor(web): remove obsolete agent v2 scaffolding and editor state by @lyzno1 in https://github.com/langgenius/dify/pull/41931

Source: https://github.com/langgenius/dify/releases/tag/1.17.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-09-10-4-pricing-model-changes-in-1-17-1|4 Pricing Model changes in 1.17.1]] · Pricing Model
- [[Changes/Dify/2026-09-10-3-automation-and-scheduling-changes-in-1-17-1|3 Automation and Scheduling changes in 1.17.1]] · Automation and Scheduling
- [[Changes/Dify/2026-09-10-8-interface-experience-changes-in-1-17-1|8 Interface Experience changes in 1.17.1]] · Interface Experience
- [[Changes/Dify/2026-09-10-76-model-support-changes-in-1-17-1|76 Model Support changes in 1.17.1]] · Model Support
- [[Changes/Dify/2026-09-10-42-agent-mode-changes-in-1-17-1|42 Agent Mode changes in 1.17.1]] · Agent Mode
- [[Changes/Dify/2026-09-10-4-developer-workflow-changes-in-1-17-1|4 Developer Workflow changes in 1.17.1]] · Developer Workflow
- [[Changes/Dify/2026-09-10-3-collaboration-changes-in-1-17-1|3 Collaboration changes in 1.17.1]] · Collaboration
- [[Changes/Dify/2026-09-10-2-memory-and-personalization-changes-in-1-17-1|2 Memory and Personalization changes in 1.17.1]] · Memory and Personalization
- [[Changes/Dify/2026-09-10-16-safety-and-privacy-changes-in-1-17-1|16 Safety and Privacy changes in 1.17.1]] · Safety and Privacy
- [[Changes/Dify/2026-09-10-13-files-and-data-changes-in-1-17-1|13 Files and Data changes in 1.17.1]] · Files and Data
- [[Changes/Dify/2026-09-10-skill-packages-built-on-windows-failed-with-a-misleading-error-a-skill-md-using|Skill packages built on Windows failed with a misleading error. A SKILL.md…]] · Mobile and Desktop
- [[Changes/Dify/2026-09-10-12-apps-and-integrations-changes-in-1-17-1|12 Apps and Integrations changes in 1.17.1]] · Apps and Integrations
- [[Changes/Dify/2026-09-10-6-account-and-access-changes-in-1-17-1|6 Account and Access changes in 1.17.1]] · Account and Access
- [[Changes/Dify/2026-09-10-3-multimodal-input-changes-in-1-17-1|3 Multimodal Input changes in 1.17.1]] · Multimodal Input
- [[Changes/Dify/2026-09-10-3-accessibility-and-localization-changes-in-1-17-1|3 Accessibility and Localization changes in 1.17.1]] · Accessibility and Localization
- [[Changes/Dify/2026-09-10-a-plugin-could-exhaust-worker-memory-with-one-declared-number-the-blob-chunk-mer|A plugin could exhaust worker memory with one declared number. The blob chunk…]] · Reliability and Performance
- [[Changes/Dify/2026-09-10-6-context-window-changes-in-1-17-1|6 Context Window changes in 1.17.1]] · Context Window
- [[Changes/Dify/2026-09-10-205-other-changes-in-1-17-1|205 other changes in 1.17.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-09-10 · Claude Code · [[Changes/Claude Code/2026-09-10-added-browser-tab-icons-for-published-artifacts-chosen-by-claude-to-match-each-p|Added browser-tab icons for published artifacts, chosen by Claude to match each page]]
- Later: 2026-09-10 · Lovable · [[Changes/Lovable/2026-09-10-sync-your-project-with-bitbucket-cloud|Sync your project with Bitbucket Cloud]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-09-10-d7f1bd&body=Card%3A%20Changes%2FDify%2F2026-09-10-6-editor-experience-changes-in-1-17-1.md%0ACard%20ID%3A%20dify-2026-09-10-d7f1bd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->