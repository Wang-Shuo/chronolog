---
card_id: openclaw-2026-10-27-ecf896
date: '2026-10-27'
description: 'OpenClaw · 2026-10-27 · Apps and Integrations: 9 changes in v2026.10.8
  — Doctor now repairs stale plugin dependency links that could block a repair or
  update…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2874
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ab941410470418593efd14db8d89282569e2a0beff99ba2cccbee485b38c7b0b
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-27-ecf896
  comparison: ''
  date: '2026-10-27'
  description: 'OpenClaw — v2026.10.8: 9 Apps and Integrations changes'
  evidence:
  - quote: Doctor now repairs stale plugin dependency links that could block a repair
      or update, including dangling Windows junctions.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: A subsequent same-version repair can restart the managed Gateway after
      a post-plugin Doctor failure when it is safe to do so, including restoring Windows
      autostart. The failed repair is still reported.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: An unresponsive Slack relay connection can reconnect so incoming events
      can resume.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Local session, transcript and MCP cleanup failures now report their own
      error instead of silently switching the turn to another model or provider.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Doctor can load affected native plugins when the plugin files and OpenClaw
      state are on different filesystems.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Gateway startup repairs stale managed plugin links after an external OpenClaw
      reinstall, allowing affected plugins to load again.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: A failed remote MCP session deletion no longer blocks the next CLI-backend
      turn when local cleanup succeeds.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Gateway shutdown can finish after a timed-out plugin retirement once the
      plugin work and cleanup have settled.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Adds remediations for the eMudhra certificate compromise in the secret
      egress proxy and its exported trust bundle. Restart the Gateway to apply the
      change. Connections relying only on the excluded root will fail; apps with independent
      trust stores and bypass tunnels need their own updates.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 9-apps-and-integrations-changes-in-v2026-10-8
  source_release: openclaw-2026-10-27-v2026-10-8-9d674f40
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 9 Apps and Integrations changes in v2026.10.8
  type: change
related_changes:
- '[[Changes/Lovable/2026-10-27-connect-your-app-to-scrive|Connect your app to Scrive]]'
- '[[Changes/Microsoft 365 Copilot/2026-10-27-admins-can-create-and-deploy-custom-model-context-protocol-mcp-connectors-across|Admins
  can create and deploy custom Model Context Protocol (MCP) connectors across…]]'
- '[[Changes/Microsoft 365 Copilot/2026-10-27-user-can-use-canva-connector-in-researcher-web-microsoft-365-copilot-extensibili|User
  can use Canva Connector in Researcher Web (Microsoft 365 Copilot extensibility)]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-27-v2026-10-8-9d674f40|openclaw-2026-10-27-v2026-10-8-9d674f40]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 9 Apps and Integrations changes in v2026.10.8
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Apps and Integrations changes in v2026.10.8

**OpenClaw** · 2026-10-27 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.8) · from [[Releases/OpenClaw/openclaw-2026-10-27-v2026-10-8-9d674f40|v2026.10.8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Doctor now repairs stale plugin dependency links that could block a repair or update, including dangling Windows junctions.

> A subsequent same-version repair can restart the managed Gateway after a post-plugin Doctor failure when it is safe to do so, including restoring Windows autostart. The failed repair is still reported.

> An unresponsive Slack relay connection can reconnect so incoming events can resume.

> Local session, transcript and MCP cleanup failures now report their own error instead of silently switching the turn to another model or provider.

> Doctor can load affected native plugins when the plugin files and OpenClaw state are on different filesystems.

> Gateway startup repairs stale managed plugin links after an external OpenClaw reinstall, allowing affected plugins to load again.

> A failed remote MCP session deletion no longer blocks the next CLI-backend turn when local cleanup succeeds.

> Gateway shutdown can finish after a timed-out plugin retirement once the plugin work and cleanup have settled.

> Adds remediations for the eMudhra certificate compromise in the secret egress proxy and its exported trust bundle. Restart the Gateway to apply the change. Connections relying only on the excluded root will fail; apps with independent trust stores and bypass tunnels need their own updates.

Source: https://docs.openclaw.ai/releases/2026.10.8
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-27-6-voice-and-audio-changes-in-v2026-10-8|6 Voice and Audio changes in v2026.10.8]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-27-6-model-support-changes-in-v2026-10-8|6 Model Support changes in v2026.10.8]] · Model Support
- [[Changes/OpenClaw/2026-10-27-2-developer-workflow-changes-in-v2026-10-8|2 Developer Workflow changes in v2026.10.8]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-27-on-linux-doctor-can-repair-a-managed-gateway-that-is-using-an-unsupported-node-v|On Linux, Doctor can repair a managed Gateway that is using an unsupported Node…]] · Interface Experience
- [[Changes/OpenClaw/2026-10-27-4-automation-and-scheduling-changes-in-v2026-10-8|4 Automation and Scheduling changes in v2026.10.8]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-27-oversized-macos-camera-clips-and-screen-recordings-now-return-an-error-instead-o|Oversized macOS camera clips and screen recordings now return an error instead…]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-27-future-macos-updates-wait-for-the-serving-gateway-to-exit-and-release-its-databa|Future macOS updates wait for the serving Gateway to exit and release its databases…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-27-4-memory-and-personalization-changes-in-v2026-10-8|4 Memory and Personalization changes in v2026.10.8]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-27-5-account-and-access-changes-in-v2026-10-8|5 Account and Access changes in v2026.10.8]] · Account and Access
- [[Changes/OpenClaw/2026-10-27-2-safety-and-privacy-changes-in-v2026-10-8|2 Safety and Privacy changes in v2026.10.8]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-27-the-control-ui-now-reconnects-when-a-visible-tab-has-lost-contact-but-still-show|The Control UI now reconnects when a visible tab has lost contact but still shows…]] · Editor Experience
- [[Changes/OpenClaw/2026-10-27-7-agent-mode-changes-in-v2026-10-8|7 Agent Mode changes in v2026.10.8]] · Agent Mode
- [[Changes/OpenClaw/2026-10-27-malformed-microsoft-teams-message-html-no-longer-causes-the-parsing-stalls-that|Malformed Microsoft Teams message HTML no longer causes the parsing stalls…]] · Collaboration
- [[Changes/OpenClaw/2026-10-27-32-other-changes-in-v2026-10-8|32 other changes in v2026.10.8]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-27 · Microsoft 365 Copilot · [[Changes/Microsoft 365 Copilot/2026-10-27-user-can-use-canva-connector-in-researcher-web-microsoft-365-copilot-extensibili|User can use Canva Connector in Researcher Web (Microsoft 365 Copilot extensibility)]]
- Later: 2026-10-27 · OpenCode · [[Changes/OpenCode/2026-10-27-add-experimental-image-and-decision-generation-apis-to-plugins-and-sdk|Add experimental image and decision generation APIs to plugins and sdk]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-27-ecf896&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-27-9-apps-and-integrations-changes-in-v2026-10-8.md%0ACard%20ID%3A%20openclaw-2026-10-27-ecf896%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.8%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->