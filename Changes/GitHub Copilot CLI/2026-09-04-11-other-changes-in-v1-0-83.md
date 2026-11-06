---
card_id: github-copilot-cli-2026-09-04-a58988
date: '2026-09-04'
description: 'GitHub Copilot CLI · 2026-09-04 · Other changes: 11 changes in 1.0.83
  — Adding support for claude-fable-5.1'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c457d3a93fcba7667516a21c4aeffc6556d97eda77a1fce26ba548d1fd3ca30a
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-04-a58988
  comparison: ''
  date: '2026-09-04'
  description: 'GitHub Copilot CLI — 1.0.83: 11 other changes'
  evidence:
  - quote: Adding support for claude-fable-5.1
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: A session lock that is re-entered on the same thread now fails with a reported
      error instead of freezing the CLI.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: A follow-up prompt typed while autopilot is running no longer disappears
      from the timeline
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: Restart provides clearer update guidance when automatic restart cannot
      be completed
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: Anthropic sessions continue after temporary fallback instead of failing
      on invalid thinking signatures
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: The newest line of output stays visible above the input box instead of
      hiding behind it, except while a prompt is pinned to the top of the transcript
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: Linux sandboxing now needs slirp4netns, nsenter, iptables, ip6tables, iptables-restore
      and ip6tables-restore on PATH. Install them if sandboxed commands start failing
      to launch.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: CLI starts without the interrupted-session restore prompt by default.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: Resuming large sessions keeps the input prompt responsive sooner.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: Linux sandboxes now restrict network egress to the configured proxy; proxy
      mode requires slirp4netns, util-linux 2.35+, iptables, and /dev/net/tun access
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: The collapsed autopilot goal panel now reads as a single-line pinned prompt,
      keeping the frame it shares with a pinned prompt instead of compressing into
      a bare band wedged against the chrome above it
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 11-other-changes-in-v1-0-83
  source_release: github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c
  source_type: github_releases
  theme: uncategorized
  title: 11 other changes in v1.0.83
  type: change
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c|github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c]]'
source_type: github_releases
theme: uncategorized
title: 11 other changes in v1.0.83
type: change
---

<!-- chronolog:begin region="header" -->
# 11 other changes in v1.0.83

**GitHub Copilot CLI** · 2026-09-04 · Other changes · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.83) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c|1.0.83]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Adding support for claude-fable-5.1

> A session lock that is re-entered on the same thread now fails with a reported error instead of freezing the CLI.

> A follow-up prompt typed while autopilot is running no longer disappears from the timeline

> Restart provides clearer update guidance when automatic restart cannot be completed

> Anthropic sessions continue after temporary fallback instead of failing on invalid thinking signatures

> The newest line of output stays visible above the input box instead of hiding behind it, except while a prompt is pinned to the top of the transcript

> Linux sandboxing now needs slirp4netns, nsenter, iptables, ip6tables, iptables-restore and ip6tables-restore on PATH. Install them if sandboxed commands start failing to launch.

> CLI starts without the interrupted-session restore prompt by default.

> Resuming large sessions keeps the input prompt responsive sooner.

> Linux sandboxes now restrict network egress to the configured proxy; proxy mode requires slirp4netns, util-linux 2.35+, iptables, and /dev/net/tun access

> The collapsed autopilot goal panel now reads as a single-line pinned prompt, keeping the frame it shares with a pinned prompt instead of compressing into a bare band wedged against the chrome above it

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.83
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-04-long-running-sessions-on-linux-return-freed-memory-to-the-system-instead-of-hold|Long-running sessions on Linux return freed memory to the system instead of holding…]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-09-04-7-apps-and-integrations-changes-in-v1-0-83|7 Apps and Integrations changes in v1.0.83]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-09-04-enterprise-admins-can-pin-sign-in-to-approved-github-organizations-with-the-forc|Enterprise admins can pin sign-in to approved GitHub organizations…]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-09-04-2-editor-experience-changes-in-v1-0-83|2 Editor Experience changes in v1.0.83]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-09-04-3-model-support-changes-in-v1-0-83|3 Model Support changes in v1.0.83]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-09-04-detect-the-herdr-terminal-multiplexer-instead-of-mistaking-it-for-tmux-so-the-ki|Detect the herdr terminal multiplexer instead of mistaking it for tmux, so the Kitty…]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-09-04-exporting-a-resumed-session-with-share-or-share-gist-writes-the-whole-transcript|Exporting a resumed session with --share or --share-gist writes the whole transcript…]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-09-04-5-safety-and-privacy-changes-in-v1-0-83|5 Safety and Privacy changes in v1.0.83]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-09-04-stopping-a-timed-out-shell-command-now-lets-queued-messages-run-and-sessions-ret|Stopping a timed-out shell command now lets queued messages run and sessions return…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-04-add-recent-created-name-and-classic-none-sorting-to-the-split-sessions-sidebar-w|Add Recent, Created, Name, and classic None sorting to the split Sessions sidebar…]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-09-04-3-account-and-access-changes-in-v1-0-83|3 Account and Access changes in v1.0.83]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-04-a58988&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-04-11-other-changes-in-v1-0-83.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-04-a58988%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.83%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->