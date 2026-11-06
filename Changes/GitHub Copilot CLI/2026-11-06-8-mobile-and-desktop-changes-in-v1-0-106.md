---
card_id: github-copilot-cli-2026-11-06-64c459
date: '2026-11-06'
description: 'GitHub Copilot CLI · 2026-11-06 · Mobile and Desktop: 8 changes in 1.0.106
  — PowerShell commands work on Windows when the CLI is installed in a long directory…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1333
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 38c2ee34d7f0dee36f737ec539acfd16566583f229554ede213665d211027fa9
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-11-06-64c459
  comparison: ''
  date: '2026-11-06'
  description: 'GitHub Copilot CLI — 1.0.106: 8 Mobile and Desktop changes'
  evidence:
  - quote: PowerShell commands work on Windows when the CLI is installed in a long
      directory path
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: On Windows, sandboxed sessions in nested Git directories can change to
      and write at the repository root
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot help config` now says `copyOnSelect` is on by default on macOS,
      that `/keep-alive` changes only the current session, that `logLevel` is set
      in the /settings dialog or settings.json rather than `copilot config`, and that
      `trustedFolders` lives in config.json and is filled by the folder-trust prompt.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Sandboxed commands on macOS can read files inside the default Xcode.app
      bundle.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: PowerShell commands that clear the screen with `cls` or `Clear-Host` no
      longer fail on Windows or skip the rest of the command
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Pressing Ctrl+C during startup on Windows now exits cleanly and runs shutdown
      before the TUI mounts.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep winget launcher symlinks intact when running `copilot update` on Windows
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Sandboxed commands on macOS no longer create missing denied paths on disk
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 8-mobile-and-desktop-changes-in-v1-0-106
  source_release: github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4
  source_type: github_releases
  theme: mobile-desktop
  title: 8 Mobile and Desktop changes in v1.0.106
  type: change
related_changes:
- '[[Changes/OpenHands/2026-11-03-2-mobile-and-desktop-changes-in-v1-35-0|2 Mobile
  and Desktop changes in v1.35.0]]'
- '[[Changes/OpenHands/2026-11-05-2-mobile-and-desktop-changes-in-v1-36-0|2 Mobile
  and Desktop changes in v1.36.0]]'
- '[[Changes/Codex CLI/2026-11-06-2-mobile-and-desktop-changes-in-rust-v0-167-0|2
  Mobile and Desktop changes in rust-v0.167.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4]]'
source_type: github_releases
theme: mobile-desktop
title: 8 Mobile and Desktop changes in v1.0.106
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Mobile and Desktop changes in v1.0.106

**GitHub Copilot CLI** · 2026-11-06 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.106) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> PowerShell commands work on Windows when the CLI is installed in a long directory path

> On Windows, sandboxed sessions in nested Git directories can change to and write at the repository root

> `copilot help config` now says `copyOnSelect` is on by default on macOS, that `/keep-alive` changes only the current session, that `logLevel` is set in the /settings dialog or settings.json rather than `copilot config`, and that `trustedFolders` lives in config.json and is filled by the folder-trust prompt.

> Sandboxed commands on macOS can read files inside the default Xcode.app bundle.

> PowerShell commands that clear the screen with `cls` or `Clear-Host` no longer fail on Windows or skip the rest of the command

> Pressing Ctrl+C during startup on Windows now exits cleanly and runs shutdown before the TUI mounts.

> Keep winget launcher symlinks intact when running `copilot update` on Windows

> Sandboxed commands on macOS no longer create missing denied paths on disk

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.106
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-11-06-4-voice-and-audio-changes-in-v1-0-106|4 Voice and Audio changes in v1.0.106]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-11-06-2-files-and-data-changes-in-v1-0-106|2 Files and Data changes in v1.0.106]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-11-06-3-reliability-and-performance-changes-in-v1-0-106|3 Reliability and Performance changes in v1.0.106]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-11-06-34-agent-mode-changes-in-v1-0-106|34 Agent Mode changes in v1.0.106]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-11-06-10-memory-and-personalization-changes-in-v1-0-106|10 Memory and Personalization changes in v1.0.106]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-11-06-64-developer-workflow-changes-in-v1-0-106|64 Developer Workflow changes in v1.0.106]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-11-06-34-safety-and-privacy-changes-in-v1-0-106|34 Safety and Privacy changes in v1.0.106]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-11-06-9-collaboration-changes-in-v1-0-106|9 Collaboration changes in v1.0.106]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-11-06-4-projects-and-workspaces-changes-in-v1-0-106|4 Projects and Workspaces changes in v1.0.106]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-11-06-8-accessibility-and-localization-changes-in-v1-0-106|8 Accessibility and Localization changes in v1.0.106]] · Accessibility and Localization
- [[Changes/GitHub Copilot CLI/2026-11-06-17-context-window-changes-in-v1-0-106|17 Context Window changes in v1.0.106]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-11-06-57-editor-experience-changes-in-v1-0-106|57 Editor Experience changes in v1.0.106]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-33-model-support-changes-in-v1-0-106|33 Model Support changes in v1.0.106]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-11-06-89-apps-and-integrations-changes-in-v1-0-106|89 Apps and Integrations changes in v1.0.106]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-11-06-2-image-generation-changes-in-v1-0-106|2 Image Generation changes in v1.0.106]] · Image Generation
- [[Changes/GitHub Copilot CLI/2026-11-06-42-interface-experience-changes-in-v1-0-106|42 Interface Experience changes in v1.0.106]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-5-pricing-model-changes-in-v1-0-106|5 Pricing Model changes in v1.0.106]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-11-06-in-the-every-schedule-manager-x-now-removes-the-highlighted-schedule-even-after|In the /every schedule manager, x now removes the highlighted schedule even after…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-11-06-23-account-and-access-changes-in-v1-0-106|23 Account and Access changes in v1.0.106]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-11-06-172-other-changes-in-v1-0-106|172 other changes in v1.0.106]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-11-06 · Codex CLI · [[Changes/Codex CLI/2026-11-06-2-mobile-and-desktop-changes-in-rust-v0-167-0|2 Mobile and Desktop changes in rust-v0.167.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-11-06-64c459&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-11-06-8-mobile-and-desktop-changes-in-v1-0-106.md%0ACard%20ID%3A%20github-copilot-cli-2026-11-06-64c459%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.106%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->