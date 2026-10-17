---
card_id: claude-code-2026-03-07-913445
date: '2026-03-07'
description: 'Claude Code · 2026-03-07 · Apps and Integrations: 3 changes in v2.1.71
  — Improved `/plugin uninstall` to disable project-scoped plugins in…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1080
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2e4a414fa8e3b311e0ef988d2544180723094a388eda872975f8c6eb5258d165
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-07-913445
  comparison: ''
  date: '2026-03-07'
  description: 'Claude Code — v2.1.71: 3 Apps and Integrations changes'
  evidence:
  - quote: Improved `/plugin uninstall` to disable project-scoped plugins in `.claude/settings.local.json`
      instead of modifying `.claude/settings.json`, so changes don't affect teammates
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.71
  - quote: Improved plugin-provided MCP server deduplication — servers that duplicate
      a manually-configured server (same command/URL) are now skipped, preventing
      duplicate connections and tool sets. Suppressions are shown in the `/plugin`
      menu.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.71
  - quote: Removed startup notification noise for unauthenticated org-registered claude.ai
      connectors
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.71
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-apps-and-integrations-changes-in-v2-1-71
  source_release: claude-code-2026-03-07-v2-1-71-github-294146317-ab5a32e0
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v2.1.71
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-05-added-reload-plugins-command-to-activate-pending-plugin-changes-without-restarti|Added
  /reload-plugins command to activate pending plugin changes without restarting]]'
- '[[Changes/Claude Code/2026-03-05-7-apps-and-integrations-changes-in-v2-1-69|7 Apps
  and Integrations changes in v2.1.69]]'
- '[[Changes/Claude Code/2026-03-06-reduced-remote-control-poll-rate-to-once-per-10-minutes-while-connected-was-1-2s|Reduced
  Remote Control /poll rate to once per 10 minutes while connected…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-07-v2-1-71-github-294146317-ab5a32e0|claude-code-2026-03-07-v2-1-71-github-294146317-ab5a32e0]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v2.1.71
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v2.1.71

**Claude Code** · 2026-03-07 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.71) · from [[Releases/Claude Code/claude-code-2026-03-07-v2-1-71-github-294146317-ab5a32e0|v2.1.71]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved `/plugin uninstall` to disable project-scoped plugins in `.claude/settings.local.json` instead of modifying `.claude/settings.json`, so changes don't affect teammates

> Improved plugin-provided MCP server deduplication — servers that duplicate a manually-configured server (same command/URL) are now skipped, preventing duplicate connections and tool sets. Suppressions are shown in the `/plugin` menu.

> Removed startup notification noise for unauthenticated org-registered claude.ai connectors

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.71
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-07-added-cron-scheduling-tools-for-recurring-prompts-within-a-session|Added cron scheduling tools for recurring prompts within a session]] · Automation and Scheduling
- [[Changes/Claude Code/2026-03-07-added-loop-command-to-run-a-prompt-or-slash-command-on-a-recurring-interval-e-g|Added /loop command to run a prompt or slash command on a recurring interval…]] · Automation and Scheduling
- [[Changes/Claude Code/2026-03-07-fixed-false-positive-permission-prompts-for-compound-bash-commands-containing-he|Fixed false-positive permission prompts for compound bash commands containing…]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-07-added-voice-pushtotalk-keybinding-to-make-the-voice-activation-key-rebindable-in|Added voice:pushToTalk keybinding to make the voice activation key rebindable…]] · Voice and Audio
- [[Changes/Claude Code/2026-03-07-2-developer-workflow-changes-in-v2-1-71|2 Developer Workflow changes in v2.1.71]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-06 · Claude Code · [[Changes/Claude Code/2026-03-06-reduced-remote-control-poll-rate-to-once-per-10-minutes-while-connected-was-1-2s|Reduced Remote Control /poll rate to once per 10 minutes while connected…]]
- Later: 2026-03-10 · Claude Code · [[Changes/Claude Code/2026-03-10-3-apps-and-integrations-changes-in-v2-1-72|3 Apps and Integrations changes in v2.1.72]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-07-913445&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-07-3-apps-and-integrations-changes-in-v2-1-71.md%0ACard%20ID%3A%20claude-code-2026-03-07-913445%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.71%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->