---
card_id: claude-code-2026-03-14-e348fd
date: '2026-03-14'
description: 'Claude Code · 2026-03-14 · Apps and Integrations: 4 changes in v2.1.76
  — Added MCP elicitation support — MCP servers can now request structured input mid-task…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1087
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3129222ecc5f42ca88949720f2c5cda1b9c75a6a44803ffadaaadfb840c3c57f
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-14-e348fd
  comparison: ''
  date: '2026-03-14'
  description: 'Claude Code — v2.1.76: 4 Apps and Integrations changes'
  evidence:
  - quote: Added MCP elicitation support — MCP servers can now request structured
      input mid-task via an interactive dialog (form fields or browser URL)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.76
  - quote: Added new `Elicitation` and `ElicitationResult` hooks to intercept and
      override responses before they're sent back
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.76
  - quote: Improved Remote Control session titles — now derived from your first prompt
      instead of showing "Interactive session"
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.76
  - quote: Updated `--plugin-dir` to only accept one path to support subcommands —
      use repeated `--plugin-dir` for multiple directories
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.76
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-apps-and-integrations-changes-in-v2-1-76
  source_release: claude-code-2026-03-14-v2-1-76-github-296929324-94cd2ffc
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v2.1.76
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-10-3-apps-and-integrations-changes-in-v2-1-72|3 Apps
  and Integrations changes in v2.1.72]]'
- '[[Changes/Cursor/2026-03-11-we-ve-added-more-than-30-new-plugins-from-partners-such-as-atlassian-datadog-git-901313|New
  Plugins on the Cursor Marketplace]]'
- '[[Changes/Claude Code/2026-03-12-changed-plugin-dir-so-local-dev-copies-now-override-installed-marketplace-plugin|Changed
  --plugin-dir so local dev copies now override installed marketplace…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-14-v2-1-76-github-296929324-94cd2ffc|claude-code-2026-03-14-v2-1-76-github-296929324-94cd2ffc]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v2.1.76
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v2.1.76

**Claude Code** · 2026-03-14 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.76) · from [[Releases/Claude Code/claude-code-2026-03-14-v2-1-76-github-296929324-94cd2ffc|v2.1.76]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added MCP elicitation support — MCP servers can now request structured input mid-task via an interactive dialog (form fields or browser URL)

> Added new `Elicitation` and `ElicitationResult` hooks to intercept and override responses before they're sent back

> Improved Remote Control session titles — now derived from your first prompt instead of showing "Interactive session"

> Updated `--plugin-dir` to only accept one path to support subcommands — use repeated `--plugin-dir` for multiple directories

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.76
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-14-added-session-quality-survey-enterprise-admins-can-configure-the-sample-rate-via|Added session quality survey]] · Enterprise and Administration
- [[Changes/Claude Code/2026-03-14-added-effort-slash-command-to-set-model-effort-level|Added /effort slash command to set model effort level]] · Model Support
- [[Changes/Claude Code/2026-03-14-3-safety-and-privacy-changes-in-v2-1-76|3 Safety and Privacy changes in v2.1.76]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-14-added-postcompact-hook-that-fires-after-compaction-completes|Added PostCompact hook that fires after compaction completes]] · Context Window
- [[Changes/Claude Code/2026-03-14-added-n-name-name-cli-flag-to-set-a-display-name-for-the-session-at-startup|Added -n / --name name CLI flag to set a display name for the session at startup]] · Projects and Workspaces
- [[Changes/Claude Code/2026-03-14-improved-voice-to-show-your-dictation-language-on-enable-and-warn-when-your-lang|Improved /voice to show your dictation language on enable and warn…]] · Voice and Audio
- [[Changes/Claude Code/2026-03-14-4-developer-workflow-changes-in-v2-1-76|4 Developer Workflow changes in v2.1.76]] · Developer Workflow
- [[Changes/Claude Code/2026-03-14-improved-background-agent-behavior-killing-a-background-agent-now-preserves-its|Improved background agent behavior]] · Agent Mode
- [[Changes/Claude Code/2026-03-14-improved-model-fallback-notifications-now-always-visible-instead-of-hidden-behin|Improved model fallback notifications]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-12 · Claude Code · [[Changes/Claude Code/2026-03-12-changed-plugin-dir-so-local-dev-copies-now-override-installed-marketplace-plugin|Changed --plugin-dir so local dev copies now override installed marketplace…]]
- Later: 2026-03-17 · Claude Code · [[Changes/Claude Code/2026-03-17-3-apps-and-integrations-changes-in-v2-1-78|3 Apps and Integrations changes in v2.1.78]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-14-e348fd&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-14-4-apps-and-integrations-changes-in-v2-1-76.md%0ACard%20ID%3A%20claude-code-2026-03-14-e348fd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.76%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->