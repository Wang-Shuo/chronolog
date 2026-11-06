---
card_id: github-copilot-cli-2026-08-10-80d242
date: '2026-08-10'
description: 'GitHub Copilot CLI · 2026-08-10 · Other changes: 11 changes in 1.0.79
  — Large monorepos now use tgrep ([trigram-indexed grep for fast regex search in
  large…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0bd22d635bce7f3342149bed615c84afaf154906403ae6b74ef31c35e686aceb
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-08-10-80d242
  comparison: ''
  date: '2026-08-10'
  description: 'GitHub Copilot CLI — 1.0.79: 11 other changes'
  evidence:
  - quote: Large monorepos now use tgrep ([trigram-indexed grep for fast regex search
      in large codebases](https://github.com/microsoft/tgrep)) instead of ripgrep
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: Combine `--plan` with `--mode autopilot` to plan first and then implement
      without waiting for approval
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: Sandboxed commands work when the working directory lives on a Windows Dev
      Drive
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: Ask user multi-select prompts include an Other option for free-text answers
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: A rare internal delay no longer prints a diagnostic warning on top of the
      interactive UI
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: Sandboxed wrapper builds (make and friends) get the dev tool caches their
      recipes need, based on the build manifests in the working directory
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: Prompt pinning is off by default; set pinnedPrompts to true to enable it.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: Sandboxed commands can reach the network again on recent Windows builds,
      where every outbound connection was blocked even with outbound access enabled
      and no proxy configured
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: Leave the pinned prompt off by default on terminals under 30 rows, where
      it would crowd the output; set pinnedPrompts explicitly to override at any size
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: A prompt stashed with ctrl+s now stays with the session it was typed for,
      so switching away and back and pressing ctrl+s restores it instead of finding
      it gone
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: Show "pending · ctrl+c to cancel" for in-flight steering prompts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 11-other-changes-in-v1-0-79
  source_release: github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a
  source_type: github_releases
  theme: uncategorized
  title: 11 other changes in v1.0.79
  type: change
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a|github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a]]'
source_type: github_releases
theme: uncategorized
title: 11 other changes in v1.0.79
type: change
---

<!-- chronolog:begin region="header" -->
# 11 other changes in v1.0.79

**GitHub Copilot CLI** · 2026-08-10 · Other changes · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.79) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a|1.0.79]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Large monorepos now use tgrep ([trigram-indexed grep for fast regex search in large codebases](https://github.com/microsoft/tgrep)) instead of ripgrep

> Combine `--plan` with `--mode autopilot` to plan first and then implement without waiting for approval

> Sandboxed commands work when the working directory lives on a Windows Dev Drive

> Ask user multi-select prompts include an Other option for free-text answers

> A rare internal delay no longer prints a diagnostic warning on top of the interactive UI

> Sandboxed wrapper builds (make and friends) get the dev tool caches their recipes need, based on the build manifests in the working directory

> Prompt pinning is off by default; set pinnedPrompts to true to enable it.

> Sandboxed commands can reach the network again on recent Windows builds, where every outbound connection was blocked even with outbound access enabled and no proxy configured

> Leave the pinned prompt off by default on terminals under 30 rows, where it would crowd the output; set pinnedPrompts explicitly to override at any size

> A prompt stashed with ctrl+s now stays with the session it was typed for, so switching away and back and pressing ctrl+s restores it instead of finding it gone

> Show "pending · ctrl+c to cancel" for in-flight steering prompts

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.79
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-08-10-a-failed-session-history-load-no-longer-leaves-the-timeline-permanently-empty-th|A failed session-history load no longer leaves the timeline permanently empty]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-08-10-2-interface-experience-changes-in-v1-0-79|2 Interface Experience changes in v1.0.79]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-08-10-improve-teleported-subagent-tasks-navigation-with-nested-tree-browsing-current-a|Improve teleported subagent /tasks navigation with nested tree browsing, current/all…]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-08-10-2-editor-experience-changes-in-v1-0-79|2 Editor Experience changes in v1.0.79]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-08-10-2-mobile-and-desktop-changes-in-v1-0-79|2 Mobile and Desktop changes in v1.0.79]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-08-10-3-apps-and-integrations-changes-in-v1-0-79|3 Apps and Integrations changes in v1.0.79]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-08-10-compute-context-attribution-against-the-auto-resolved-model-so-token-totals-are|Compute /context attribution against the Auto-resolved model so token totals…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-08-10-11-safety-and-privacy-changes-in-v1-0-79|11 Safety and Privacy changes in v1.0.79]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-08-10-3-model-support-changes-in-v1-0-79|3 Model Support changes in v1.0.79]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-08-10-login-links-are-clickable-during-web-and-device-code-sign-in|Login links are clickable during web and device-code sign-in]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-08-10-4-developer-workflow-changes-in-v1-0-79|4 Developer Workflow changes in v1.0.79]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-08-10-2-enterprise-and-administration-changes-in-v1-0-79|2 Enterprise and Administration changes in v1.0.79]] · Enterprise and Administration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-08-10-80d242&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-08-10-11-other-changes-in-v1-0-79.md%0ACard%20ID%3A%20github-copilot-cli-2026-08-10-80d242%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.79%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->