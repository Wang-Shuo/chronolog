---
card_id: cline-2026-09-17-2002a8
date: '2026-09-17'
description: 'Cline · 2026-09-17 · Mobile and Desktop: On Windows, opening a repository
  that contains a file named `rg.exe`, `git.exe`, or `powershell.exe` no longer runs…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1283
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 702d481c275db6f72d7eddaa62b1a73475a811b507ee9585adb1c76cad371ddb
product: cline
product_name: Cline
record:
  card_id: cline-2026-09-17-2002a8
  comparison: ''
  date: '2026-09-17'
  description: 'Cline — v4.1.19: On Windows, opening a repository that contains a
    file named `rg.exe`, `git.exe`, or `powershell.exe` no longer runs that file in
    place of the real program. Bare program names were resolved through the workspace
    directory before PATH, so a planted executable ran with your privileges as soon
    as the workspace was indexed. Cline now sets Windows'' `NoDefaultCurrentDirectoryInExePath`
    opt-out at startup, in both the VS Code extension and the JetBrains core. Processes
    Cline launches inherit it, so inside a Command Prompt shell a program in the current
    directory now needs `.\` as it already does in PowerShell.'
  evidence:
  - quote: On Windows, opening a repository that contains a file named `rg.exe`, `git.exe`,
      or `powershell.exe` no longer runs that file in place of the real program. Bare
      program names were resolved through the workspace directory before PATH, so
      a planted executable ran with your privileges as soon as the workspace was indexed.
      Cline now sets Windows' `NoDefaultCurrentDirectoryInExePath` opt-out at startup,
      in both the VS Code extension and the JetBrains core. Processes Cline launches
      inherit it, so inside a Command Prompt shell a program in the current directory
      now needs `.\` as it already does in PowerShell.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: cline
  product_name: Cline
  slug: on-windows-opening-a-repository-that-contains-a-file-named-rg-exe-git-exe-or-pow
  source_release: cline-2026-09-17-v4-1-19-github-390521944-270e9514
  source_type: github_releases
  theme: mobile-desktop
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: On Windows, opening a repository that contains a file named `rg.exe`, `git.exe`…
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-17-you-can-now-connect-multiple-accounts-to-plugins-in-chatgpt-expanding-support-be|Connect
  multiple accounts to plugins in ChatGPT]]'
- '[[Changes/Claude Code/2026-09-17-added-enduser-sub-the-idp-subject-to-the-telemetry-claude-desktop-and-cowork-sen|Added
  enduser.sub, the IdP subject, to the telemetry Claude Desktop and Cowork…]]'
- '[[Changes/Claude Code/2026-09-17-improved-the-desktop-error-when-claude-desktop-does-not-open-it-now-says-why-and|Improved
  the /desktop error when Claude Desktop does not open]]'
source_release: '[[Releases/Cline/cline-2026-09-17-v4-1-19-github-390521944-270e9514|cline-2026-09-17-v4-1-19-github-390521944-270e9514]]'
source_type: github_releases
theme: mobile-desktop
title: On Windows, opening a repository that contains a file named rg.exe, git.exe…
type: change
---

<!-- chronolog:begin region="header" -->
# On Windows, opening a repository that contains a file named `rg.exe`, `git.exe`…

**Cline** · 2026-09-17 · [[Themes/mobile-desktop|Mobile and Desktop]] · [Official source](https://github.com/cline/cline/releases/tag/v4.1.19) · from [[Releases/Cline/cline-2026-09-17-v4-1-19-github-390521944-270e9514|v4.1.19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> On Windows, opening a repository that contains a file named `rg.exe`, `git.exe`, or `powershell.exe` no longer runs that file in place of the real program. Bare program names were resolved through the workspace directory before PATH, so a planted executable ran with your privileges as soon as the workspace was indexed. Cline now sets Windows' `NoDefaultCurrentDirectoryInExePath` opt-out at startup, in both the VS Code extension and the JetBrains core. Processes Cline launches inherit it, so inside a Command Prompt shell a program in the current directory now needs `.\` as it already does in PowerShell.
>
> Source: https://github.com/cline/cline/releases/tag/v4.1.19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-09-17-13-model-support-changes-in-v4-1-19|13 Model Support changes in v4.1.19]] · Model Support
- [[Changes/Cline/2026-09-17-2-developer-workflow-changes-in-v4-1-19|2 Developer Workflow changes in v4.1.19]] · Developer Workflow
- [[Changes/Cline/2026-09-17-task-history-no-longer-goes-blank-when-a-task-spawns-many-subagents-subagent-row|Task history no longer goes blank when a task spawns many subagents]] · Agent Mode
- [[Changes/Cline/2026-09-17-long-tasks-now-compact-when-they-actually-need-to-rather-than-running-out-of-roo|Long tasks now compact when they actually need to rather than running out of room]] · Context Window
- [[Changes/Cline/2026-09-17-cline-pass-now-defaults-to-a-model-from-your-subscription-rather-than-a-free-one|Cline Pass now defaults to a model from your subscription rather than a free one]] · Pricing Model
- [[Changes/Cline/2026-09-17-web-search-is-now-enabled-by-default-on-models-that-support-it-outside-yolo-mode|Web search is now enabled by default on models that support it, outside YOLO mode]] · Search and Browsing
- [[Changes/Cline/2026-09-17-cline-s-logo-and-icons-have-been-refreshed-throughout-the-extension-including-th|Cline's logo and icons have been refreshed throughout the extension, including…]] · Interface Experience
- [[Changes/Cline/2026-09-17-terminal-commands-that-succeed-without-printing-anything-git-add-a-on-a-clean-tr|Terminal commands that succeed without printing anything…]] · Apps and Integrations
- [[Changes/Cline/2026-09-17-5-other-changes-in-v4-1-19|5 other changes in v4.1.19]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-improved-the-desktop-error-when-claude-desktop-does-not-open-it-now-says-why-and|Improved the /desktop error when Claude Desktop does not open]]
- Later: 2026-09-17 · Codex CLI · [[Changes/Codex CLI/2026-09-17-2-mobile-and-desktop-changes-in-rust-v0-155-0|2 Mobile and Desktop changes in rust-v0.155.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-09-17-2002a8&body=Card%3A%20Changes%2FCline%2F2026-09-17-on-windows-opening-a-repository-that-contains-a-file-named-rg-exe-git-exe-or-pow.md%0ACard%20ID%3A%20cline-2026-09-17-2002a8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->