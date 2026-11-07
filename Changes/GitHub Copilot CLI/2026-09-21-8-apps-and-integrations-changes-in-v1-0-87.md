---
card_id: github-copilot-cli-2026-09-21-55d6c8
date: '2026-09-21'
description: 'GitHub Copilot CLI · 2026-09-21 · Apps and Integrations: 8 changes in
  1.0.87 — Empty strictKnownMarketplaces allowlists now hide and block built-in plugin…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2838
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d7db44a9bd5f7d622e6621639597e8098390d4a80eb6034724864ad4c3df6ccc
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-21-55d6c8
  comparison: ''
  date: '2026-09-21'
  description: 'GitHub Copilot CLI — 1.0.87: 8 Apps and Integrations changes'
  evidence:
  - quote: Empty strictKnownMarketplaces allowlists now hide and block built-in plugin
      marketplaces.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.87
  - quote: Mouse-selected text is visibly highlighted in /help and /mcp show screens
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.87
  - quote: MCP auth status warnings stay accurate during reconnects and startup refreshes
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.87
  - quote: A failing MCP server no longer removes other servers' tools
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.87
  - quote: '`copilot mcp list` and `copilot mcp get` now report the built-in `github-mcp-server`
      when you are signed in, instead of showing it only in the interactive `/mcp`
      view'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.87
  - quote: MCP servers that advertise list-change capabilities but do not implement
      subscriptions now connect instead of failing
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.87
  - quote: Session resume no longer hangs while reconnecting MCP servers
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.87
  - quote: Configure per-server MCP slow-connection warning thresholds with slowConnectionThresholdMs
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.87
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 8-apps-and-integrations-changes-in-v1-0-87
  source_release: github-copilot-cli-2026-09-21-v1-0-87-github-393077593-9fe949ec
  source_type: github_releases
  theme: apps-integrations
  title: 8 Apps and Integrations changes in v1.0.87
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-19-you-can-now-ask-btw-side-questions-about-photos-attached-to-the-current-message|Ask
  /btw side questions about photos attached to the current message when using…]]'
- '[[Changes/OpenClaw/2026-09-19-52-apps-and-integrations-changes-in-v2026-9-5|52
  Apps and Integrations changes in v2026.9.5]]'
- '[[Changes/ElevenLabs/2026-09-21-sdk-releases|SDK releases]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-21-v1-0-87-github-393077593-9fe949ec|github-copilot-cli-2026-09-21-v1-0-87-github-393077593-9fe949ec]]'
source_type: github_releases
theme: apps-integrations
title: 8 Apps and Integrations changes in v1.0.87
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Apps and Integrations changes in v1.0.87

**GitHub Copilot CLI** · 2026-09-21 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.87) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-21-v1-0-87-github-393077593-9fe949ec|1.0.87]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Empty strictKnownMarketplaces allowlists now hide and block built-in plugin marketplaces.

> Mouse-selected text is visibly highlighted in /help and /mcp show screens

> MCP auth status warnings stay accurate during reconnects and startup refreshes

> A failing MCP server no longer removes other servers' tools

> `copilot mcp list` and `copilot mcp get` now report the built-in `github-mcp-server` when you are signed in, instead of showing it only in the interactive `/mcp` view

> MCP servers that advertise list-change capabilities but do not implement subscriptions now connect instead of failing

> Session resume no longer hangs while reconnecting MCP servers

> Configure per-server MCP slow-connection warning thresholds with slowConnectionThresholdMs

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.87
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-21-tear-down-the-processes-an-internal-git-command-started-when-it-times-out-so-a-s|Tear down the processes an internal git command started when it times out, so a slow…]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-09-21-consecutive-steering-prompts-in-the-same-mode-combine-into-one-pending-message-p|Consecutive steering prompts in the same mode combine into one pending message]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-09-21-show-live-elapsed-time-for-execution-subagents-in-timeline-entries|Show live elapsed time for execution subagents in timeline entries]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-21-managed-plugin-commands-load-organization-marketplace-policy-with-environment-gi|Managed plugin commands load organization marketplace policy with environment…]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-21-5-developer-workflow-changes-in-v1-0-87|5 Developer Workflow changes in v1.0.87]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-09-21-enable-the-rubber-duck-agent-for-every-model-family-and-for-low-cost-tier-sessio|Enable the rubber-duck agent for every model family and for low-cost-tier session models]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-09-21-2-safety-and-privacy-changes-in-v1-0-87|2 Safety and Privacy changes in v1.0.87]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-09-21-number-key-selection-in-the-question-dialog-works-for-choices-10-and-beyond|Number-key selection in the question dialog works for choices 10 and beyond]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-09-21-4-other-changes-in-v1-0-87|4 other changes in v1.0.87]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-21 · ElevenLabs · [[Changes/ElevenLabs/2026-09-21-sdk-releases|SDK releases]]
- Later: 2026-09-21 · Open WebUI · [[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps and Integrations changes in v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-21-55d6c8&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-21-8-apps-and-integrations-changes-in-v1-0-87.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-21-55d6c8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.87%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->