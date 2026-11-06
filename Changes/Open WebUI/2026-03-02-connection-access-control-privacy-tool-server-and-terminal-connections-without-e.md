---
card_id: open-webui-2026-03-02-70fb4b
date: '2026-03-02'
description: "Open WebUI · 2026-03-02 · Safety and Privacy: \U0001F512 **Connection
  access control privacy.** Tool server and terminal connections without explicit
  access grants are…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1051
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 4ec690d84231d7ad90f56946e06ba9539a83898b27e0d0a168c00bb8296f109c
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-02-70fb4b
  comparison: ''
  date: '2026-03-02'
  description: "Open WebUI — v0.8.7: \U0001F512 **Connection access control privacy.**
    Tool server and terminal connections without explicit access grants are now private
    (admin-only) by default, fixing a bug where connections configured with no access
    grants were visible to all users instead of being restricted. [Commit](https://github.com/open-webui/open-webui/commit/2751a0f0b)"
  evidence:
  - quote: "\U0001F512 **Connection access control privacy.** Tool server and terminal
      connections without explicit access grants are now private (admin-only) by default,
      fixing a bug where connections configured with no access grants were visible
      to all users instead of being restricted. [Commit](https://github.com/open-webui/open-webui/commit/2751a0f0b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.7
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: connection-access-control-privacy-tool-server-and-terminal-connections-without-e
  source_release: open-webui-2026-03-02-v0-8-7-github-291874841-d7aad0b1
  source_type: github_releases
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - terminal
    score: 50
    theme: developer-workflow
  - matched_terms:
    - privacy
    score: 50
    theme: safety-privacy
  theme_resolution: manual-semantic-rule-v2
  title: "\U0001F512 **Connection access control privacy.** Tool server and terminal
    connections…"
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-28-fixed-listener-leak-in-interactive-permission-handler-during-auto-approvals|Fixed
  listener leak in interactive permission handler during auto-approvals]]'
- '[[Changes/Open WebUI/2026-03-01-4-safety-and-privacy-changes-in-v0-8-6|4 Safety
  and Privacy changes in v0.8.6]]'
- '[[Changes/Codex CLI/2026-03-02-8-safety-and-privacy-changes-in-rust-v0-107-0|8
  Safety and Privacy changes in rust-v0.107.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-02-v0-8-7-github-291874841-d7aad0b1|open-webui-2026-03-02-v0-8-7-github-291874841-d7aad0b1]]'
source_type: github_releases
theme: safety-privacy
title: "\U0001F512 Connection access control privacy. Tool server and terminal connections…"
type: change
---

<!-- chronolog:begin region="header" -->
# 🔒 **Connection access control privacy.** Tool server and terminal connections…

**Open WebUI** · 2026-03-02 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.7) · from [[Releases/Open WebUI/open-webui-2026-03-02-v0-8-7-github-291874841-d7aad0b1|v0.8.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> 🔒 **Connection access control privacy.** Tool server and terminal connections without explicit access grants are now private (admin-only) by default, fixing a bug where connections configured with no access grants were visible to all users instead of being restricted. [Commit](https://github.com/open-webui/open-webui/commit/2751a0f0b)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-02-chatcontrols-memory-leak-the-chatcontrols-panel-no-longer-leaks-event-listeners|🧠 ChatControls memory leak. The ChatControls panel no longer leaks event…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-02-temporary-chat-params-preservation-model-parameters-are-now-correctly-saved-when|💾 Temporary chat params preservation. Model parameters are now correctly saved…]] · Model Support
- [[Changes/Open WebUI/2026-03-02-faster-artifact-content-updates-artifact-content-extraction-during-streaming-is|⚡ Faster artifact content updates. Artifact content extraction during streaming…]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-02 · Codex CLI · [[Changes/Codex CLI/2026-03-02-8-safety-and-privacy-changes-in-rust-v0-107-0|8 Safety and Privacy changes in rust-v0.107.0]]
- Later: 2026-03-03 · Cursor · [[Changes/Cursor/2026-03-03-fixed-team-permission-and-access-control-inconsistencies-across-organization-set|Fixed team permission and access control inconsistencies across organization setups]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-02-70fb4b&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-02-connection-access-control-privacy-tool-server-and-terminal-connections-without-e.md%0ACard%20ID%3A%20open-webui-2026-03-02-70fb4b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->