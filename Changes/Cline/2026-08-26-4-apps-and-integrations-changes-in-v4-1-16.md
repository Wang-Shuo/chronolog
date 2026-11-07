---
card_id: cline-2026-08-26-83b071
date: '2026-08-26'
description: 'Cline · 2026-08-26 · Apps and Integrations: 4 changes in v4.1.16 — Everything
  here lands through the SDK bundle, so it applies to windows running that bundle.'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2812
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bf1440342c936f375e248a67c90b93b3b4142d11293d68b97e7f3e96e94aa5ba
product: cline
product_name: Cline
record:
  card_id: cline-2026-08-26-83b071
  comparison: ''
  date: '2026-08-26'
  description: 'Cline — v4.1.16: 4 Apps and Integrations changes'
  evidence:
  - quote: Everything here lands through the SDK bundle, so it applies to windows
      running that bundle.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.16
  - quote: Hooks now resolve their workspace from the VS Code window instead of shared
      global state in `~/.cline`. With a second window open on another project, a
      workspace's `.clinerules/hooks` scripts were never discovered, and hook cwd
      and the workspace paths passed to hook scripts resolved against whatever project
      some other or older Cline instance last recorded.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.16
  - quote: Installing an MCP server from the marketplace no longer misreads the catalog's
      `--` separator as part of the server command.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.16
  - quote: The per-tool MCP auto-approve checkboxes are hidden. MCP auto-approval
      is governed solely by the global "Use MCP servers" toggle — the per-tool checkboxes
      were no-ops that implied granularity the approval path does not have.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.16
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 4-apps-and-integrations-changes-in-v4-1-16
  source_release: cline-2026-08-26-v4-1-16-github-376988707-45a7fae8
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v4.1.16
  type: change
related_changes:
- '[[Changes/Raycast/2026-08-25-ai-added-support-for-mentioning-ai-extensions-when-replying-to-a-question-asked|AI
  : Added support for mentioning AI extensions when replying to a question asked…]]'
- '[[Changes/Raycast/2026-08-25-2-apps-and-integrations-changes-in-raycast-windows-2-0|2
  Apps and Integrations changes in Raycast windows 2.0]]'
- '[[Changes/Claude Code/2026-08-26-2-apps-and-integrations-changes-in-v2-1-247|2
  Apps and Integrations changes in v2.1.247]]'
source_release: '[[Releases/Cline/cline-2026-08-26-v4-1-16-github-376988707-45a7fae8|cline-2026-08-26-v4-1-16-github-376988707-45a7fae8]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v4.1.16
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v4.1.16

**Cline** · 2026-08-26 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.16) · from [[Releases/Cline/cline-2026-08-26-v4-1-16-github-376988707-45a7fae8|v4.1.16]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Everything here lands through the SDK bundle, so it applies to windows running that bundle.

> Hooks now resolve their workspace from the VS Code window instead of shared global state in `~/.cline`. With a second window open on another project, a workspace's `.clinerules/hooks` scripts were never discovered, and hook cwd and the workspace paths passed to hook scripts resolved against whatever project some other or older Cline instance last recorded.

> Installing an MCP server from the marketplace no longer misreads the catalog's `--` separator as part of the server command.

> The per-tool MCP auto-approve checkboxes are hidden. MCP auto-approval is governed solely by the global "Use MCP servers" toggle — the per-tool checkboxes were no-ops that implied granularity the approval path does not have.

Source: https://github.com/cline/cline/releases/tag/v4.1.16
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-08-26-cost-estimates-are-no-longer-shown-for-providers-billed-by-a-flat-rate-subscript|Cost estimates are no longer shown for providers billed by a flat-rate subscription…]] · Pricing Model
- [[Changes/Cline/2026-08-26-credentials-embedded-in-git-remote-urls-are-now-redacted-from-the-workspace-info|Credentials embedded in git remote URLs are now redacted from the workspace…]] · Model Support
- [[Changes/Cline/2026-08-26-3-other-changes-in-v4-1-16|3 other changes in v4.1.16]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-08-26 · Claude Code · [[Changes/Claude Code/2026-08-26-2-apps-and-integrations-changes-in-v2-1-247|2 Apps and Integrations changes in v2.1.247]]
- Later: 2026-08-26 · Codex CLI · [[Changes/Codex CLI/2026-08-26-24-apps-and-integrations-changes-in-rust-v0-150-0|24 Apps and Integrations changes in rust-v0.150.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-08-26-83b071&body=Card%3A%20Changes%2FCline%2F2026-08-26-4-apps-and-integrations-changes-in-v4-1-16.md%0ACard%20ID%3A%20cline-2026-08-26-83b071%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.16%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->