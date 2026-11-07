---
card_id: openclaw-2026-11-05-bf48ed
date: '2026-11-05'
description: 'OpenClaw · 2026-11-05 · Account and Access: 4 changes in v2026.11.1
  — Prevents turning off Tailscale exposure in the connected Mac app from deleting
  your…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2291
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2c65508a40795013c2f11825234e6df6a4de2bde30f4bf48d8fca630b52938ed
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-11-05-bf48ed
  comparison: ''
  date: '2026-11-05'
  description: 'OpenClaw — v2026.11.1: 4 Account and Access changes'
  evidence:
  - quote: Prevents turning off Tailscale exposure in the connected Mac app from deleting
      your Gateway authentication settings. Credentials already lost are not restored.
    source_release: https://docs.openclaw.ai/releases/2026.11.1
  - quote: Adds a workspace ID option to Anthropic API-key setup , and preserves incompatible
      existing profiles during setup-token sign-in.
    source_release: https://docs.openclaw.ai/releases/2026.11.1
  - quote: Prevents the in-process browser from writing Gateway authentication settings
      to your configuration at startup. Standalone browser clients using trusted-proxy
      authentication need an explicit Gateway password.
    source_release: https://docs.openclaw.ai/releases/2026.11.1
  - quote: Reuses a fresh shared OAuth token across concurrent MCP requests.
    source_release: https://docs.openclaw.ai/releases/2026.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-account-and-access-changes-in-v2026-11-1
  source_release: openclaw-2026-11-05-v2026-11-1-7d3de823
  source_type: openclaw_changelog
  theme: account-access
  title: 4 Account and Access changes in v2026.11.1
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-11-03-6-account-and-access-changes-in-v2026-10-10|6 Account
  and Access changes in v2026.10.10]]'
- '[[Changes/OpenHands/2026-11-03-ci-deps-bump-docker-login-action-from-4-6-0-to-4-7-0-in-the-actions-group-across|ci(deps):
  bump docker/login-action from 4.6.0 to 4.7.0 in the actions group across 1…]]'
- '[[Changes/Dify/2026-11-04-2-account-and-access-changes-in-1-19-0|2 Account and
  Access changes in 1.19.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-11-05-v2026-11-1-7d3de823|openclaw-2026-11-05-v2026-11-1-7d3de823]]'
source_type: openclaw_changelog
theme: account-access
title: 4 Account and Access changes in v2026.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Account and Access changes in v2026.11.1

**OpenClaw** · 2026-11-05 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.11.1) · from [[Releases/OpenClaw/openclaw-2026-11-05-v2026-11-1-7d3de823|v2026.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Prevents turning off Tailscale exposure in the connected Mac app from deleting your Gateway authentication settings. Credentials already lost are not restored.

> Adds a workspace ID option to Anthropic API-key setup , and preserves incompatible existing profiles during setup-token sign-in.

> Prevents the in-process browser from writing Gateway authentication settings to your configuration at startup. Standalone browser clients using trusted-proxy authentication need an explicit Gateway password.

> Reuses a fresh shared OAuth token across concurrent MCP requests.

Source: https://docs.openclaw.ai/releases/2026.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-11-05-reduces-prompt-cache-misses-across-completion-heartbeat-and-background-turns-by|Reduces prompt-cache misses across completion, heartbeat and background turns…]] · Editor Experience
- [[Changes/OpenClaw/2026-11-05-keeps-accepted-talk-work-running-when-you-end-talk-on-an-android-phone-connected|Keeps accepted Talk work running when you end Talk on an Android phone connected…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-11-05-5-apps-and-integrations-changes-in-v2026-11-1|5 Apps and Integrations changes in v2026.11.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-11-05-3-context-window-changes-in-v2026-11-1|3 Context Window changes in v2026.11.1]] · Context Window
- [[Changes/OpenClaw/2026-11-05-7-voice-and-audio-changes-in-v2026-11-1|7 Voice and Audio changes in v2026.11.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-11-05-5-memory-and-personalization-changes-in-v2026-11-1|5 Memory and Personalization changes in v2026.11.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-11-05-2-safety-and-privacy-changes-in-v2026-11-1|2 Safety and Privacy changes in v2026.11.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-11-05-prevents-oversized-mac-camera-clips-and-screen-recordings-from-disconnecting-the|Prevents oversized Mac camera clips and screen recordings from disconnecting…]] · Multimodal Input
- [[Changes/OpenClaw/2026-11-05-4-model-support-changes-in-v2026-11-1|4 Model Support changes in v2026.11.1]] · Model Support
- [[Changes/OpenClaw/2026-11-05-4-agent-mode-changes-in-v2026-11-1|4 Agent Mode changes in v2026.11.1]] · Agent Mode
- [[Changes/OpenClaw/2026-11-05-avoids-restoring-cold-archived-conversations-just-to-refresh-usage-and-cost-repo|Avoids restoring cold archived conversations just to refresh usage and cost reports…]] · Pricing Model
- [[Changes/OpenClaw/2026-11-05-allows-authorized-native-commands-to-restore-archived-source-sessions-and-report|Allows authorized native commands to restore archived source sessions, and reports…]] · Collaboration
- [[Changes/OpenClaw/2026-11-05-3-developer-workflow-changes-in-v2026-11-1|3 Developer Workflow changes in v2026.11.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-11-05-keeps-the-windows-scheduled-task-available-during-update-recovery-until-the-gate|Keeps the Windows scheduled task available during update recovery until the Gateway…]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-11-05-40-other-changes-in-v2026-11-1|40 other changes in v2026.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-11-04 · Dify · [[Changes/Dify/2026-11-04-2-account-and-access-changes-in-1-19-0|2 Account and Access changes in 1.19.0]]
- Later: 2026-11-05 · Qoder · [[Changes/Qoder/2026-11-05-ssh-and-wsl-improves-connection-management-and-workspace-creation-including-dire|SSH and WSL: Improves connection management and workspace creation, including…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-11-05-bf48ed&body=Card%3A%20Changes%2FOpenClaw%2F2026-11-05-4-account-and-access-changes-in-v2026-11-1.md%0ACard%20ID%3A%20openclaw-2026-11-05-bf48ed%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->