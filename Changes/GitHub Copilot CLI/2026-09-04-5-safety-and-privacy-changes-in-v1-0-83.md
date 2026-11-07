---
card_id: github-copilot-cli-2026-09-04-afb7e1
date: '2026-09-04'
description: 'GitHub Copilot CLI · 2026-09-04 · Safety and Privacy: 5 changes in 1.0.83
  — Sandboxed file tools now read the same developer-tool paths as sandboxed shell…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2229
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f9c30dcbb10551ddeb7d123cd8a768b32e2f4c3061bea2c847e63d237c699f8c
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-04-afb7e1
  comparison: ''
  date: '2026-09-04'
  description: 'GitHub Copilot CLI — 1.0.83: 5 Safety and Privacy changes'
  evidence:
  - quote: Sandboxed file tools now read the same developer-tool paths as sandboxed
      shell commands, including token-bearing registry config such as ~/.npmrc; set
      sandbox.allowDevToolAccess to false to turn these grants off
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: Host-provided plugin customizations can be read without redundant path
      permission prompts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: On macOS and Linux, sandboxed commands can no longer reach services running
      on your machine. On macOS this also blocks a server the command itself starts
      on 127.0.0.1, so test suites that bind a local port will fail; turn on Allow
      local network in /sandbox to reach localhost again.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: Improve sandboxed Bazel and Bazelisk runs by granting required cache and
      output paths; macOS requires a future Bazel release or additional sandbox capabilities
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  - quote: Improve /sandbox policy by grouping path grants by source and showing detected
      developer tools
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.83
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 5-safety-and-privacy-changes-in-v1-0-83
  source_release: github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in v1.0.83
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-03-6-safety-and-privacy-changes-in-rust-v0-153-0|6
  Safety and Privacy changes in rust-v0.153.0]]'
- '[[Changes/OpenClaw/2026-09-03-10-safety-and-privacy-changes-in-v2026-9-1|10 Safety
  and Privacy changes in v2026.9.1]]'
- '[[Changes/Claude Code/2026-09-04-4-safety-and-privacy-changes-in-v2-1-261|4 Safety
  and Privacy changes in v2.1.261]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c|github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in v1.0.83
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in v1.0.83

**GitHub Copilot CLI** · 2026-09-04 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.83) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-04-v1-0-83-github-382838246-6f996d9c|1.0.83]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Sandboxed file tools now read the same developer-tool paths as sandboxed shell commands, including token-bearing registry config such as ~/.npmrc; set sandbox.allowDevToolAccess to false to turn these grants off

> Host-provided plugin customizations can be read without redundant path permission prompts

> On macOS and Linux, sandboxed commands can no longer reach services running on your machine. On macOS this also blocks a server the command itself starts on 127.0.0.1, so test suites that bind a local port will fail; turn on Allow local network in /sandbox to reach localhost again.

> Improve sandboxed Bazel and Bazelisk runs by granting required cache and output paths; macOS requires a future Bazel release or additional sandbox capabilities

> Improve /sandbox policy by grouping path grants by source and showing detected developer tools

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
- [[Changes/GitHub Copilot CLI/2026-09-04-stopping-a-timed-out-shell-command-now-lets-queued-messages-run-and-sessions-ret|Stopping a timed-out shell command now lets queued messages run and sessions return…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-04-add-recent-created-name-and-classic-none-sorting-to-the-split-sessions-sidebar-w|Add Recent, Created, Name, and classic None sorting to the split Sessions sidebar…]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-09-04-3-account-and-access-changes-in-v1-0-83|3 Account and Access changes in v1.0.83]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-04-11-other-changes-in-v1-0-83|11 other changes in v1.0.83]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-04 · Claude Code · [[Changes/Claude Code/2026-09-04-4-safety-and-privacy-changes-in-v2-1-261|4 Safety and Privacy changes in v2.1.261]]
- Later: 2026-09-04 · HeyGen · [[Changes/HeyGen/2026-09-04-identity-verification-ui-update|Identity verification UI update]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-04-afb7e1&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-04-5-safety-and-privacy-changes-in-v1-0-83.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-04-afb7e1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.83%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->