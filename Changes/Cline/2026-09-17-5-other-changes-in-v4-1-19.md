---
card_id: cline-2026-09-17-de7dc4
date: '2026-09-17'
description: 'Cline · 2026-09-17 · Other changes: 5 changes in v4.1.19 — The W&B Inference
  provider is now listed as CoreWeave, with its sign-up and API-key links updated
  to…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 352eec959856e7d84b165f27b48907245f8fc071ea393d7f7ac6957412a263ab
product: cline
product_name: Cline
record:
  card_id: cline-2026-09-17-de7dc4
  comparison: ''
  date: '2026-09-17'
  description: 'Cline — v4.1.19: 5 other changes'
  evidence:
  - quote: The W&B Inference provider is now listed as CoreWeave, with its sign-up
      and API-key links updated to match CoreWeave's current documentation.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: Opening your home directory as a workspace no longer drives the extension
      host to exhaustion. Typing an `@` mention indexed every file beneath it and
      re-ranked the whole index on each keystroke.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: Credentials are now stripped of invisible characters when saved, not only
      when pasted, and the cleanup covers AWS, GCP, and SAP fields and custom header
      values in addition to API keys.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: Claude Code and OpenCode no longer ask for an API key they never read.
      Both authenticate from their own local CLI's credentials, but they were treated
      as key-based providers; the workaround was storing a dummy key. A missing CLI
      on `PATH` now warns rather than blocking, since a configured path or bundled
      binary also works.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: Langfuse tracing, when configured, is now limited to the Cline and Cline
      Pass providers. The provider was ignored, so prompts and responses sent to third-party
      and bring-your-own-key providers were exported too.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 5-other-changes-in-v4-1-19
  source_release: cline-2026-09-17-v4-1-19-github-390521944-270e9514
  source_type: github_releases
  theme: uncategorized
  title: 5 other changes in v4.1.19
  type: change
source_release: '[[Releases/Cline/cline-2026-09-17-v4-1-19-github-390521944-270e9514|cline-2026-09-17-v4-1-19-github-390521944-270e9514]]'
source_type: github_releases
theme: uncategorized
title: 5 other changes in v4.1.19
type: change
---

<!-- chronolog:begin region="header" -->
# 5 other changes in v4.1.19

**Cline** · 2026-09-17 · Other changes · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.19) · from [[Releases/Cline/cline-2026-09-17-v4-1-19-github-390521944-270e9514|v4.1.19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The W&B Inference provider is now listed as CoreWeave, with its sign-up and API-key links updated to match CoreWeave's current documentation.

> Opening your home directory as a workspace no longer drives the extension host to exhaustion. Typing an `@` mention indexed every file beneath it and re-ranked the whole index on each keystroke.

> Credentials are now stripped of invisible characters when saved, not only when pasted, and the cleanup covers AWS, GCP, and SAP fields and custom header values in addition to API keys.

> Claude Code and OpenCode no longer ask for an API key they never read. Both authenticate from their own local CLI's credentials, but they were treated as key-based providers; the workaround was storing a dummy key. A missing CLI on `PATH` now warns rather than blocking, since a configured path or bundled binary also works.

> Langfuse tracing, when configured, is now limited to the Cline and Cline Pass providers. The provider was ignored, so prompts and responses sent to third-party and bring-your-own-key providers were exported too.

Source: https://github.com/cline/cline/releases/tag/v4.1.19
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
- [[Changes/Cline/2026-09-17-terminal-commands-that-succeed-without-printing-anything-git-add-a-on-a-clean-tr|Terminal commands that succeed without printing anything…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-09-17-de7dc4&body=Card%3A%20Changes%2FCline%2F2026-09-17-5-other-changes-in-v4-1-19.md%0ACard%20ID%3A%20cline-2026-09-17-de7dc4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->