---
card_id: github-copilot-cli-2026-08-10-51fd46
date: '2026-08-10'
description: 'GitHub Copilot CLI · 2026-08-10 · Mobile and Desktop: 2 changes in 1.0.79
  — The `/app` command now opens the current session in the GitHub Copilot desktop
  app…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1245
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 48aed57e11e64ae0dffd512410f3d135c3bc09e3012d9be2c54ee4fad93ae192
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-08-10-51fd46
  comparison: ''
  date: '2026-08-10'
  description: 'GitHub Copilot CLI — 1.0.79: 2 Mobile and Desktop changes'
  evidence:
  - quote: The `/app` command now opens the current session in the GitHub Copilot
      desktop app instead of landing on Home with the wrong folder (requires GitHub
      Copilot app 1.1.3 or later)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: On macOS, sandboxed commands can use UNIX-domain sockets again, so tools
      that talk over a local IPC pipe (tsx, vite, esbuild, jest workers) no longer
      fail with `listen EPERM`
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 2-mobile-and-desktop-changes-in-v1-0-79
  source_release: github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a
  source_type: github_releases
  theme: mobile-desktop
  title: 2 Mobile and Desktop changes in v1.0.79
  type: change
related_changes:
- '[[Changes/Cline/2026-08-09-fall-back-to-the-session-cwd-or-desktop-for-mention-file-search-in-empty-windows|Fall
  back to the session cwd or Desktop for @-mention file search in empty windows]]'
- '[[Changes/ChatGPT/2026-08-10-chatgpt-can-now-help-you-find-available-restaurant-reservations-with-opentable-r|Restaurant
  reservations in ChatGPT]]'
- '[[Changes/ElevenLabs/2026-08-10-android-sdk|Android SDK]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a|github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a]]'
source_type: github_releases
theme: mobile-desktop
title: 2 Mobile and Desktop changes in v1.0.79
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Mobile and Desktop changes in v1.0.79

**GitHub Copilot CLI** · 2026-08-10 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.79) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a|1.0.79]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The `/app` command now opens the current session in the GitHub Copilot desktop app instead of landing on Home with the wrong folder (requires GitHub Copilot app 1.1.3 or later)

> On macOS, sandboxed commands can use UNIX-domain sockets again, so tools that talk over a local IPC pipe (tsx, vite, esbuild, jest workers) no longer fail with `listen EPERM`

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.79
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-08-10-a-failed-session-history-load-no-longer-leaves-the-timeline-permanently-empty-th|A failed session-history load no longer leaves the timeline permanently empty]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-08-10-2-interface-experience-changes-in-v1-0-79|2 Interface Experience changes in v1.0.79]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-08-10-improve-teleported-subagent-tasks-navigation-with-nested-tree-browsing-current-a|Improve teleported subagent /tasks navigation with nested tree browsing, current/all…]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-08-10-2-editor-experience-changes-in-v1-0-79|2 Editor Experience changes in v1.0.79]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-08-10-3-apps-and-integrations-changes-in-v1-0-79|3 Apps and Integrations changes in v1.0.79]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-08-10-compute-context-attribution-against-the-auto-resolved-model-so-token-totals-are|Compute /context attribution against the Auto-resolved model so token totals…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-08-10-11-safety-and-privacy-changes-in-v1-0-79|11 Safety and Privacy changes in v1.0.79]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-08-10-3-model-support-changes-in-v1-0-79|3 Model Support changes in v1.0.79]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-08-10-login-links-are-clickable-during-web-and-device-code-sign-in|Login links are clickable during web and device-code sign-in]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-08-10-4-developer-workflow-changes-in-v1-0-79|4 Developer Workflow changes in v1.0.79]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-08-10-2-enterprise-and-administration-changes-in-v1-0-79|2 Enterprise and Administration changes in v1.0.79]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-08-10-11-other-changes-in-v1-0-79|11 other changes in v1.0.79]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-08-10 · ElevenLabs · [[Changes/ElevenLabs/2026-08-10-android-sdk|Android SDK]]
- Later: 2026-08-10 · Windsurf · [[Changes/Windsurf/2026-08-10-devin-desktop|Devin Desktop]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-08-10-51fd46&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-08-10-2-mobile-and-desktop-changes-in-v1-0-79.md%0ACard%20ID%3A%20github-copilot-cli-2026-08-10-51fd46%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.79%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->