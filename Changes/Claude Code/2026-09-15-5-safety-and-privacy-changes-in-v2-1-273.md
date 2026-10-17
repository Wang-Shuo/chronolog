---
card_id: claude-code-2026-09-15-2cb9c6
date: '2026-09-15'
description: 'Claude Code · 2026-09-15 · Safety and Privacy: 5 changes in v2.1.273
  — Fixed Bash commands the permission checker cannot fully analyze skipping the prompt…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1248
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2399621ce3f50ab10c581fd5a8ed341a12611827ff8961af3ae2fbfb6c6a1473
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-15-2cb9c6
  comparison: ''
  date: '2026-09-15'
  description: 'Claude Code — v2.1.273: 5 Safety and Privacy changes'
  evidence:
  - quote: Fixed Bash commands the permission checker cannot fully analyze skipping
      the prompt under `permissions.blockReadsOutsideWorkingDirectories`, and a subshell
      hiding a dangerous `rm` in bypass mode
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: Fixed Read on macOS refusing a dragged-in screenshot, or any file the system
      reports under a second path, with "symlink resolution changed after permission
      was checked"
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: Reverted a 2.1.268 change that checked Read and Edit deny rules on Bash
      lines the permission checker can't analyze (`eval`, `env -C`); commands like
      `time -p make build` prompt again instead of being denied
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: 'Windows: Improved the network-path permission check for UNC paths when
      a mapped network drive was added with `--add-dir`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: '[Claude Code on the web] Changed the admin "Share cloud sessions" setting
      to live under Data and privacy instead of the Claude Code page, where Data and
      privacy admins can also manage it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-safety-and-privacy-changes-in-v2-1-273
  source_release: claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in v2.1.273
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-12-fixed-read-only-git-commands-in-bash-unexpectedly-asking-for-permission-after-a|Fixed
  read-only git commands in Bash unexpectedly asking for permission after…]]'
- '[[Changes/ChatGPT/2026-09-14-if-you-make-no-changes-to-your-plugins-settings-the-default-permission-setting-i|If
  you make no changes to your Plugins settings, the default permission setting…]]'
- '[[Changes/Claude Code/2026-09-14-7-safety-and-privacy-changes-in-v2-1-271|7 Safety
  and Privacy changes in v2.1.271]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in v2.1.273
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in v2.1.273

**Claude Code** · 2026-09-15 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.273) · from [[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|v2.1.273]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed Bash commands the permission checker cannot fully analyze skipping the prompt under `permissions.blockReadsOutsideWorkingDirectories`, and a subshell hiding a dangerous `rm` in bypass mode

> Fixed Read on macOS refusing a dragged-in screenshot, or any file the system reports under a second path, with "symlink resolution changed after permission was checked"

> Reverted a 2.1.268 change that checked Read and Edit deny rules on Bash lines the permission checker can't analyze (`eval`, `env -C`); commands like `time -p make build` prompt again instead of being denied

> Windows: Improved the network-path permission check for UNC paths when a mapped network drive was added with `--add-dir`

> [Claude Code on the web] Changed the admin "Share cloud sessions" setting to live under Data and privacy instead of the Claude Code page, where Data and privacy admins can also manage it

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-improved-the-routine-detail-page-menu-and-rename-in-the-b|Claude Code on the web Improved the routine detail page]] · Interface Experience
- [[Changes/Claude Code/2026-09-15-improved-artifact-database-writes-an-update-can-now-remove-a-single-field-instea|Improved artifact database writes]] · Files and Data
- [[Changes/Claude Code/2026-09-15-3-apps-and-integrations-changes-in-v2-1-273|3 Apps and Integrations changes in v2.1.273]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-15-changed-auto-mode-on-bedrock-vertex-and-foundry-to-use-the-local-classifier-by-d|Changed auto mode on Bedrock, Vertex and Foundry to use the local classifier…]] · Agent Mode
- [[Changes/Claude Code/2026-09-15-changed-bug-and-feedback-reports-to-include-only-model-behavior-params-model-sys|Changed /bug and /feedback reports to include only model-behavior params…]] · Model Support
- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-added-a-discard-unsaved-changes-confirmation-before-the-n|Claude Code on the web Added a "Discard unsaved changes?" confirmation before…]] · Editor Experience
- [[Changes/Claude Code/2026-09-15-4-account-and-access-changes-in-v2-1-273|4 Account and Access changes in v2.1.273]] · Account and Access
- [[Changes/Claude Code/2026-09-15-improved-responsiveness-in-long-sessions-hook-progress-and-sub-agent-activity-no|Improved responsiveness in long sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-15-added-x-claude-code-request-class-x-claude-code-agent-type-x-claude-code-prev-to|Added x-claude-code-request-class, x-claude-code-agent-type…]] · Context Window
- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-removed-the-full-page-desktop-app-download-screen-that-ne|Claude Code on the web Removed the full-page desktop-app download screen that new…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-15-3-developer-workflow-changes-in-v2-1-273|3 Developer Workflow changes in v2.1.273]] · Developer Workflow
- [[Changes/Claude Code/2026-09-15-8-other-changes-in-v2-1-273|8 other changes in v2.1.273]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-14 · Claude Code · [[Changes/Claude Code/2026-09-14-7-safety-and-privacy-changes-in-v2-1-271|7 Safety and Privacy changes in v2.1.271]]
- Later: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-7-safety-and-privacy-changes-in-v2-1-275|7 Safety and Privacy changes in v2.1.275]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-15-2cb9c6&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-15-5-safety-and-privacy-changes-in-v2-1-273.md%0ACard%20ID%3A%20claude-code-2026-09-15-2cb9c6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.273%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->