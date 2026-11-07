---
card_id: openclaw-2026-10-22-97b7d2
date: '2026-10-22'
description: 'OpenClaw · 2026-10-22 · Apps and Integrations: 10 changes in v2026.10.6
  — Plugin setup now lets you fix an invalid number without closing the prompt.'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1309
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f616ad410a7727f612844bab246f4d9dd151e68750b5059a762503cca82b7d51
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-22-97b7d2
  comparison: ''
  date: '2026-10-22'
  description: 'OpenClaw — v2026.10.6: 10 Apps and Integrations changes'
  evidence:
  - quote: Plugin setup now lets you fix an invalid number without closing the prompt.
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: Upgrades done from the apps now repair official plugins before checking
      migrations.
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: If an empty, retired plugin setting in a single-file configuration stops
      the Gateway from starting, Doctor can now back it up and remove it.
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: Slack now waits until incoming events are saved before continuing recovery,
      so events aren’t lost.
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: When an MCP integration sends the same result as both structured data and
      JSON text, the model now gets only one copy, even if the formatting differs.
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: Plugins now warn you when a CLI provider binding is missing. Using the
      CLI on its own still works. See CLI backend plugins .
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: When some plugins or channels fail to load, you now see the failures, and
      the alternatives that did load keep working.
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: Plugin removal now postpones cleanup instead of deleting files when it
      can’t read the marker that protects them.
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: Enabled ACP coding backends can now start without an unused default workspace.
      Add acpx to any plugin allowlist that applies, and use an absolute path for
      custom adapters.
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: The Gateway now stays up when a hook’s credential can’t be found, and only
      turns off the affected hooks. Add the secret to the service environment and
      reload or restart, or disable those hooks.
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 10-apps-and-integrations-changes-in-v2026-10-6
  source_release: openclaw-2026-10-22-v2026-10-6-56379f53
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 10 Apps and Integrations changes in v2026.10.6
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-22-2-apps-and-integrations-changes-in-v2-1-309|2
  Apps and Integrations changes in v2.1.309]]'
- '[[Changes/GitHub Copilot CLI/2026-10-22-reuse-cached-local-mcp-tool-snapshots-across-registered-git-worktrees-in-one-rep|Reuse
  cached local MCP tool snapshots across registered Git worktrees in one repository]]'
- '[[Changes/Google Antigravity/2026-10-22-3-apps-and-integrations-changes-in-hub-v2-26-0-notifications-settings|3
  Apps and Integrations changes in HUB v2.26.0 — Notifications settings…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-22-v2026-10-6-56379f53|openclaw-2026-10-22-v2026-10-6-56379f53]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 10 Apps and Integrations changes in v2026.10.6
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Apps and Integrations changes in v2026.10.6

**OpenClaw** · 2026-10-22 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.6) · from [[Releases/OpenClaw/openclaw-2026-10-22-v2026-10-6-56379f53|v2026.10.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Plugin setup now lets you fix an invalid number without closing the prompt.

> Upgrades done from the apps now repair official plugins before checking migrations.

> If an empty, retired plugin setting in a single-file configuration stops the Gateway from starting, Doctor can now back it up and remove it.

> Slack now waits until incoming events are saved before continuing recovery, so events aren’t lost.

> When an MCP integration sends the same result as both structured data and JSON text, the model now gets only one copy, even if the formatting differs.

> Plugins now warn you when a CLI provider binding is missing. Using the CLI on its own still works. See CLI backend plugins .

> When some plugins or channels fail to load, you now see the failures, and the alternatives that did load keep working.

> Plugin removal now postpones cleanup instead of deleting files when it can’t read the marker that protects them.

> Enabled ACP coding backends can now start without an unused default workspace. Add acpx to any plugin allowlist that applies, and use an absolute path for custom adapters.

> The Gateway now stays up when a hook’s credential can’t be found, and only turns off the affected hooks. Add the secret to the service environment and reload or restart, or disable those hooks.

Source: https://docs.openclaw.ai/releases/2026.10.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-22-shell-completion-now-finds-global-flags-after-subcommands-regenerate-your-saved|Shell completion now finds global flags after subcommands]] · Editor Experience
- [[Changes/OpenClaw/2026-10-22-5-automation-and-scheduling-changes-in-v2026-10-6|5 Automation and Scheduling changes in v2026.10.6]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-22-3-agent-mode-changes-in-v2026-10-6|3 Agent Mode changes in v2026.10.6]] · Agent Mode
- [[Changes/OpenClaw/2026-10-22-4-model-support-changes-in-v2026-10-6|4 Model Support changes in v2026.10.6]] · Model Support
- [[Changes/OpenClaw/2026-10-22-security-release-v2026-10-6-adds-remediations-for-the-emudhra-certificate-compro|Security release: v2026.10.6 adds remediations for the eMudhra certificate compromise]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-22-restarting-the-same-official-docker-container-no-longer-copies-all-its-saved-sta|Restarting the same official Docker container no longer copies all its saved state…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-10-22-7-developer-workflow-changes-in-v2026-10-6|7 Developer Workflow changes in v2026.10.6]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-22-linux-camera-discovery-now-reports-an-unreadable-device-folder-as-an-error-inste|Linux camera discovery now reports an unreadable device folder as an error instead…]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-22-web-search-timeout-errors-now-tell-you-the-request-s-actual-time-limit-see-web-t|Web search timeout errors now tell you the request’s actual time limit]] · Search and Browsing
- [[Changes/OpenClaw/2026-10-22-3-voice-and-audio-changes-in-v2026-10-6|3 Voice and Audio changes in v2026.10.6]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-22-session-share-now-shows-an-error-when-it-can-t-discover-receivers-instead-of-an|Session Share now shows an error when it can’t discover receivers, instead…]] · Collaboration
- [[Changes/OpenClaw/2026-10-22-2-mobile-and-desktop-changes-in-v2026-10-6|2 Mobile and Desktop changes in v2026.10.6]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-22-2-enterprise-and-administration-changes-in-v2026-10-6|2 Enterprise and Administration changes in v2026.10.6]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-22-4-context-window-changes-in-v2026-10-6|4 Context Window changes in v2026.10.6]] · Context Window
- [[Changes/OpenClaw/2026-10-22-mcp-sign-in-errors-now-give-a-safe-reason-and-tell-you-how-to-sign-in-or-fix-you|MCP sign-in errors now give a safe reason and tell you how to sign in or fix…]] · Account and Access
- [[Changes/OpenClaw/2026-10-22-4-memory-and-personalization-changes-in-v2026-10-6|4 Memory and Personalization changes in v2026.10.6]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-22-you-can-now-stop-a-gateway-that-has-been-stuck-starting-for-more-than-five-minut|Stop a Gateway that has been stuck starting for more than five minutes without ever…]] · Other changes
- [[Changes/OpenClaw/2026-10-22-you-can-now-find-a-claude-code-conversation-by-its-exact-session-id-even-when-th|Find a Claude Code conversation by its exact session ID even when the normal search…]] · Other changes
- [[Changes/OpenClaw/2026-10-22-60-other-changes-in-v2026-10-6|60 other changes in v2026.10.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-22 · Google Antigravity · [[Changes/Google Antigravity/2026-10-22-3-apps-and-integrations-changes-in-hub-v2-26-0-notifications-settings|3 Apps and Integrations changes in HUB v2.26.0 — Notifications settings…]]
- Later: 2026-10-22 · OpenHands · [[Changes/OpenHands/2026-10-22-chore-bump-openhands-extensions-to-0-33-0-by-neubig-in-https-github-com-openhand|chore: bump @openhands/extensions to 0.33.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-22-97b7d2&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-22-10-apps-and-integrations-changes-in-v2026-10-6.md%0ACard%20ID%3A%20openclaw-2026-10-22-97b7d2%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->