---
card_id: claude-code-2026-04-16-1512c7
date: '2026-04-16'
description: 'Claude Code · 2026-04-16 · Apps and Integrations: 2 changes in v2.1.111
  — Headless `--output-format stream-json` now includes `plugin_errors` on the init
  event…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2680
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f43168a30bb43b85225cea3d3ec12352784b75f4be15602dc834bb1123007d2b
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-16-1512c7
  comparison: ''
  date: '2026-04-16'
  description: 'Claude Code — v2.1.111: 2 Apps and Integrations changes'
  evidence:
  - quote: Headless `--output-format stream-json` now includes `plugin_errors` on
      the init event when plugins are demoted for unsatisfied dependencies
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.111
  - quote: 'Improved plugin error handling: dependency errors now distinguish conflicting,
      invalid, and overly complex version requirements; fixed stale resolved versions
      after `plugin update`; `plugin install` now recovers from interrupted prior
      installs'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.111
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-apps-and-integrations-changes-in-v2-1-111
  source_release: claude-code-2026-04-16-v2-1-111-github-309911692-a3025e78
  source_type: github_releases
  theme: apps-integrations
  title: 2 Apps and Integrations changes in v2.1.111
  type: change
related_changes:
- '[[Changes/OpenCode/2026-04-15-export-ai-sdk-telemetry-spans-to-otlp-trace-backends|Export
  AI SDK telemetry spans to OTLP trace backends]]'
- '[[Changes/OpenCode/2026-04-15-4-apps-and-integrations-changes-in-v1-4-4|4 Apps
  and Integrations changes in v1.4.4]]'
- '[[Changes/Windsurf/2026-04-15-additional-changes|Additional Changes]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-16-v2-1-111-github-309911692-a3025e78|claude-code-2026-04-16-v2-1-111-github-309911692-a3025e78]]'
source_type: github_releases
theme: apps-integrations
title: 2 Apps and Integrations changes in v2.1.111
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Apps and Integrations changes in v2.1.111

**Claude Code** · 2026-04-16 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.111) · from [[Releases/Claude Code/claude-code-2026-04-16-v2-1-111-github-309911692-a3025e78|v2.1.111]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Headless `--output-format stream-json` now includes `plugin_errors` on the init event when plugins are demoted for unsatisfied dependencies

> Improved plugin error handling: dependency errors now distinguish conflicting, invalid, and overly complex version requirements; fixed stale resolved versions after `plugin update`; `plugin install` now recovers from interrupted prior installs

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.111
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-16-transcript-view-footer-now-shows-dump-to-scrollback-and-v-open-in-editor-shortcu|Transcript view footer now shows  (dump to scrollback) and v (open in editor)…]] · Editor Experience
- [[Changes/Claude Code/2026-04-16-3-model-support-changes-in-v2-1-111|3 Model Support changes in v2.1.111]] · Model Support
- [[Changes/Claude Code/2026-04-16-auto-mode-is-now-available-for-max-subscribers-when-using-opus-4-7|Auto mode is now available for Max subscribers when using Opus 4.7]] · Model Support
- [[Changes/Claude Code/2026-04-16-windows-powershell-tool-is-progressively-rolling-out-opt-in-or-out-with-claude-c|Windows: PowerShell tool is progressively rolling out]] · Mobile and Desktop
- [[Changes/Claude Code/2026-04-16-3-interface-experience-changes-in-v2-1-111|3 Interface Experience changes in v2.1.111]] · Interface Experience
- [[Changes/Claude Code/2026-04-16-added-less-permission-prompts-skill-scans-transcripts-for-common-read-only-bash|Added /less-permission-prompts skill]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-16-2-developer-workflow-changes-in-v2-1-111|2 Developer Workflow changes in v2.1.111]] · Developer Workflow
- [[Changes/Claude Code/2026-04-16-added-ultrareview-for-running-comprehensive-code-review-in-the-cloud-using-paral|Added /ultrareview for running comprehensive code review in the cloud using…]] · Developer Workflow
- [[Changes/Claude Code/2026-04-16-2-safety-and-privacy-changes-in-v2-1-111|2 Safety and Privacy changes in v2.1.111]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-16-auto-mode-no-longer-requires-enable-auto-mode|Auto mode no longer requires --enable-auto-mode]] · Agent Mode
- [[Changes/Claude Code/2026-04-16-6-other-changes-in-v2-1-111|6 other changes in v2.1.111]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-15 · Windsurf · [[Changes/Windsurf/2026-04-15-additional-changes|Additional Changes]]
- Later: 2026-04-16 · Descript · [[Changes/Descript/2026-04-16-the-api-also-supports-model-context-protocol-mcp-connections-so-you-can-take-act|The API also supports Model Context Protocol (MCP) connections so you can take…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-16-1512c7&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-16-2-apps-and-integrations-changes-in-v2-1-111.md%0ACard%20ID%3A%20claude-code-2026-04-16-1512c7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.111%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->