---
card_id: open-webui-2026-08-31-f1672f
date: '2026-08-31'
description: "Open WebUI · 2026-08-31 · Collaboration: 2 changes in v0.11.2 — \U0001F9F5
  **Smoother busy websocket servers.** Large Redis-backed websocket deployments now
  spend far…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create
    a team here: (source link)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2789
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6dc521150cefc793c5b101f65f3953c898d0f5e577087b51ec937b1199ce94b5
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-31-f1672f
  comparison: ''
  date: '2026-08-31'
  description: 'Open WebUI — v0.11.2: 2 Collaboration changes'
  evidence:
  - quote: "\U0001F9F5 **Smoother busy websocket servers.** Large Redis-backed websocket
      deployments now spend far less time sweeping old sessions, reading their own
      session data back from Redis, and checking every outgoing websocket message
      for file attachments Open WebUI does not send, so channel posts, collaboration
      updates, heartbeats, and live chat updates put less load on busy servers. [#28835](https://github.com/open-webui/open-webui/pull/28835),
      [#28180](https://github.com/open-webui/open-webui/pull/28180)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F9F9 **Shared chats search resets.** Reopening the shared chats
      dialog now starts with an empty search box and the full list, rather than a
      leftover search term above unfiltered results. [#29082](https://github.com/open-webui/open-webui/pull/29082),
      [#29081](https://github.com/open-webui/open-webui/issues/29081)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-collaboration-changes-in-v0-11-2
  source_release: open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b
  source_type: github_releases
  theme: collaboration
  title: 2 Collaboration changes in v0.11.2
  type: change
related_changes:
- '[[Changes/Qoder/2026-08-27-an-ecosystem-that-connects-with-70-plugins-20-000-skills-and-40-connectors-qoder|An
  ecosystem that connects]]'
- '[[Changes/Gamma/2026-08-28-we-ve-shipped-a-lot-since-our-last-update-here-are-five-highlights-that-make-it|We’ve
  shipped a lot since our last update]]'
- '[[Changes/v0/2026-08-28-4-collaboration-changes-in-gpt-5-6-sol-sign-in-inside-previews|4
  Collaboration changes in GPT-5.6 Sol, sign-in inside previews…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b|open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b]]'
source_type: github_releases
theme: collaboration
title: 2 Collaboration changes in v0.11.2
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Collaboration changes in v0.11.2

**Open WebUI** · 2026-08-31 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.2) · from [[Releases/Open WebUI/open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b|v0.11.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧵 **Smoother busy websocket servers.** Large Redis-backed websocket deployments now spend far less time sweeping old sessions, reading their own session data back from Redis, and checking every outgoing websocket message for file attachments Open WebUI does not send, so channel posts, collaboration updates, heartbeats, and live chat updates put less load on busy servers. [#28835](https://github.com/open-webui/open-webui/pull/28835), [#28180](https://github.com/open-webui/open-webui/pull/28180)

> 🧹 **Shared chats search resets.** Reopening the shared chats dialog now starts with an empty search box and the full list, rather than a leftover search term above unfiltered results. [#29082](https://github.com/open-webui/open-webui/pull/29082), [#29081](https://github.com/open-webui/open-webui/issues/29081)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-31-large-tool-calls-stream-faster-through-anthropic-compatible-clients-when-a-strea|🧠 Large tool calls stream faster through Anthropic-compatible…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-08-31-3-automation-and-scheduling-changes-in-v0-11-2|3 Automation and Scheduling changes in v0.11.2]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-08-31-3-interface-experience-changes-in-v0-11-2|3 Interface Experience changes in v0.11.2]] · Interface Experience
- [[Changes/Open WebUI/2026-08-31-code-interpreter-starts-on-windows-the-built-in-code-interpreter-now-serves-its|🐍 Code interpreter starts on Windows. The built-in code interpreter now serves…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-08-31-security-advisory-this-release-includes-security-and-access-control-fixes-we-rec|🛡️ Security Advisory: This release includes security and access-control fixes]] · Safety and Privacy
- [[Changes/Open WebUI/2026-08-31-high-contrast-mode-is-now-accessibility-mode-the-interface-setting-previously-ca|🏷️ High Contrast Mode is now Accessibility Mode. The interface setting…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-08-31-9-developer-workflow-changes-in-v0-11-2|9 Developer Workflow changes in v0.11.2]] · Developer Workflow
- [[Changes/Open WebUI/2026-08-31-2-files-and-data-changes-in-v0-11-2|2 Files and Data changes in v0.11.2]] · Files and Data
- [[Changes/Open WebUI/2026-08-31-10-model-support-changes-in-v0-11-2|10 Model Support changes in v0.11.2]] · Model Support
- [[Changes/Open WebUI/2026-08-31-12-other-changes-in-v0-11-2|12 other changes in v0.11.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Collaboration

- Earlier: 2026-08-28 · v0 · [[Changes/v0/2026-08-28-4-collaboration-changes-in-gpt-5-6-sol-sign-in-inside-previews|4 Collaboration changes in GPT-5.6 Sol, sign-in inside previews…]]
- Later: 2026-08-31 · OpenClaw · [[Changes/OpenClaw/2026-08-31-browser-and-computer-use-signed-in-browser-sessions-through-an-isolated-managed|Browser and Computer Use - Signed-in browser sessions through an isolated managed…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-01-11 · Descript · [[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create a team here: (source link)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-31-f1672f&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-31-2-collaboration-changes-in-v0-11-2.md%0ACard%20ID%3A%20open-webui-2026-08-31-f1672f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->