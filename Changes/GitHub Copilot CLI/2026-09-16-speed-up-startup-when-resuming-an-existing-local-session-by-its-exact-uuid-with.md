---
card_id: github-copilot-cli-2026-09-16-7350a7
date: '2026-09-16'
description: 'GitHub Copilot CLI · 2026-09-16 · Reliability and Performance: Speed
  up startup when resuming an existing local session by its exact UUID with `--resume`'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1371
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 38b134b5624320795ef9e3791a64182753901b05239672edf6d6cfc5a3fd91f5
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-16-7350a7
  comparison: ''
  date: '2026-09-16'
  description: 'GitHub Copilot CLI — 1.0.85: Speed up startup when resuming an existing
    local session by its exact UUID with `--resume`'
  evidence:
  - quote: Speed up startup when resuming an existing local session by its exact UUID
      with `--resume`
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: speed-up-startup-when-resuming-an-existing-local-session-by-its-exact-uuid-with
  source_release: github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9
  source_type: github_releases
  theme: reliability-performance
  title: Speed up startup when resuming an existing local session by its exact UUID
    with `--resume`
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-11-improved-responsiveness-in-long-sessions-transcript-updates-no-longer-re-process|Improved
  responsiveness in long sessions]]'
- '[[Changes/Claude Code/2026-09-14-improved-terminal-rendering-performance-large-diffs-and-long-transcripts-render|Improved
  terminal rendering performance]]'
- '[[Changes/Claude Code/2026-09-15-improved-responsiveness-in-long-sessions-hook-progress-and-sub-agent-activity-no|Improved
  responsiveness in long sessions]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9]]'
source_type: github_releases
theme: reliability-performance
title: Speed up startup when resuming an existing local session by its exact UUID
  with --resume
type: change
---

<!-- chronolog:begin region="header" -->
# Speed up startup when resuming an existing local session by its exact UUID with `--resume`

**GitHub Copilot CLI** · 2026-09-16 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.85) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|1.0.85]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Speed up startup when resuming an existing local session by its exact UUID with `--resume`
>
> Source: https://github.com/github/copilot-cli/releases/tag/v1.0.85
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-16-4-account-and-access-changes-in-v1-0-85|4 Account and Access changes in v1.0.85]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-16-6-developer-workflow-changes-in-v1-0-85|6 Developer Workflow changes in v1.0.85]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-09-16-9-editor-experience-changes-in-v1-0-85|9 Editor Experience changes in v1.0.85]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-09-16-17-safety-and-privacy-changes-in-v1-0-85|17 Safety and Privacy changes in v1.0.85]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-09-16-13-model-support-changes-in-v1-0-85|13 Model Support changes in v1.0.85]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-09-16-usage-shows-per-model-ai-credit-consumption-in-usage-breakdowns|/usage shows per-model AI Credit consumption in usage breakdowns]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-09-16-3-memory-and-personalization-changes-in-v1-0-85|3 Memory and Personalization changes in v1.0.85]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-09-16-4-mobile-and-desktop-changes-in-v1-0-85|4 Mobile and Desktop changes in v1.0.85]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-09-16-add-json-to-copilot-plugin-list-copilot-plugin-marketplace-list-and-copilot-plug|Add --json to copilot plugin list, copilot plugin marketplace list…]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-09-16-3-context-window-changes-in-v1-0-85|3 Context Window changes in v1.0.85]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-09-16-2-agent-mode-changes-in-v1-0-85|2 Agent Mode changes in v1.0.85]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-16-20-apps-and-integrations-changes-in-v1-0-85|20 Apps and Integrations changes in v1.0.85]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-09-16-share-notes-md-now-writes-the-exported-session-to-your-home-directory-instead-of|--share=~/notes.md now writes the exported session to your home directory instead…]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-09-16-when-session-history-is-truncated-or-compacted-just-as-a-turn-finishes-the-worki|When session history is truncated or compacted just as a turn finishes…]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-09-16-3-interface-experience-changes-in-v1-0-85|3 Interface Experience changes in v1.0.85]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-09-16-19-other-changes-in-v1-0-85|19 other changes in v1.0.85]] · Other changes
- [[Changes/GitHub Copilot CLI/2026-09-16-vim-mode-is-now-available-to-everyone-turn-it-on-with-vim-or-by-setting-editormo|Vim mode is now available to everyone]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-09-15 · Claude Code · [[Changes/Claude Code/2026-09-15-improved-responsiveness-in-long-sessions-hook-progress-and-sub-agent-activity-no|Improved responsiveness in long sessions]]
- Later: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-added-a-visible-warning-when-memory-usage-is-critical-with-steps-to-free-memory|Added a visible warning when memory usage is critical, with steps to free memory…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-16-7350a7&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-16-speed-up-startup-when-resuming-an-existing-local-session-by-its-exact-uuid-with.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-16-7350a7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.85%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->