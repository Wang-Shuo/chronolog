---
card_id: claude-code-2026-04-13-9f4dbb
date: '2026-04-13'
description: 'Claude Code · 2026-04-13 · Apps and Integrations: 3 changes in v2.1.105
  — Added PreCompact hook support: hooks can now block compaction by exiting with
  code 2…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1117
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dc75a440f0181a4837a11f0dd09e5b3ef075732e3c4a3eb8ad15f359d0521488
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-13-9f4dbb
  comparison: ''
  date: '2026-04-13'
  description: 'Claude Code — v2.1.105: 3 Apps and Integrations changes'
  evidence:
  - quote: 'Added PreCompact hook support: hooks can now block compaction by exiting
      with code 2 or returning `{"decision":"block"}`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.105
  - quote: Added background monitor support for plugins via a top-level `monitors`
      manifest key that auto-arms at session start or on skill invoke
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.105
  - quote: Improved MCP large-output truncation prompt to give format-specific recipes
      (e.g. `jq` for JSON, computed Read chunk sizes for text)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.105
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-apps-and-integrations-changes-in-v2-1-105
  source_release: claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v2.1.105
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-08-this-release-introduces-updates-to-bugbot-including-the-ability-to-self-improve|Cursor
  introduces updates to Bugbot including the ability to self-improve in real…]]'
- '[[Changes/Claude Code/2026-04-09-2-apps-and-integrations-changes-in-v2-1-98|2 Apps
  and Integrations changes in v2.1.98]]'
- '[[Changes/Claude Code/2026-04-10-4-apps-and-integrations-changes-in-v2-1-101|4
  Apps and Integrations changes in v2.1.101]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3|claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v2.1.105
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v2.1.105

**Claude Code** · 2026-04-13 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.105) · from [[Releases/Claude Code/claude-code-2026-04-13-v2-1-105-github-308569432-65a12cd3|v2.1.105]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added PreCompact hook support: hooks can now block compaction by exiting with code 2 or returning `{"decision":"block"}`

> Added background monitor support for plugins via a top-level `monitors` manifest key that auto-arms at session start or on skill invoke

> Improved MCP large-output truncation prompt to give format-specific recipes (e.g. `jq` for JSON, computed Read chunk sizes for text)

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.105
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-13-fixed-bash-tool-suggesting-acceptedits-permission-mode-when-exiting-plan-mode-wo|Fixed Bash tool suggesting acceptEdits permission mode when exiting plan mode…]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-13-improved-network-error-messages-connection-errors-now-show-a-retry-message-immed|Improved network error messages]] · Interface Experience
- [[Changes/Claude Code/2026-04-13-improved-stalled-api-stream-handling-streams-now-abort-after-5-minutes-of-no-dat|Improved stalled API stream handling]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-13-2-developer-workflow-changes-in-v2-1-105|2 Developer Workflow changes in v2.1.105]] · Developer Workflow
- [[Changes/Claude Code/2026-04-13-proactive-is-now-an-alias-for-loop|/proactive is now an alias for /loop]] · Automation and Scheduling
- [[Changes/Claude Code/2026-04-13-5-other-changes-in-v2-1-105|5 other changes in v2.1.105]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-10 · Claude Code · [[Changes/Claude Code/2026-04-10-4-apps-and-integrations-changes-in-v2-1-101|4 Apps and Integrations changes in v2.1.101]]
- Later: 2026-04-15 · Claude Code · [[Changes/Claude Code/2026-04-15-4-apps-and-integrations-changes-in-v2-1-110|4 Apps and Integrations changes in v2.1.110]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-13-9f4dbb&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-13-3-apps-and-integrations-changes-in-v2-1-105.md%0ACard%20ID%3A%20claude-code-2026-04-13-9f4dbb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.105%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->