---
card_id: openclaw-2026-10-22-15b257
date: '2026-10-22'
description: 'OpenClaw · 2026-10-22 · Model Support: 4 changes in v2026.10.6 — Windows
  now waits for local-model shutdown helpers to finish before moving on.'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1382
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6eae95ee8f3941bf85625bb413979978e731001fc6a5cdd985410bd42a69aa5f
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-22-15b257
  comparison: ''
  date: '2026-10-22'
  description: 'OpenClaw — v2026.10.6: 4 Model Support changes'
  evidence:
  - quote: Windows now waits for local-model shutdown helpers to finish before moving
      on.
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: A scheduled command pinned to the Gateway now refuses a prompt that asks
      it to run on another machine. If a saved job reports this conflict, fix its
      prompt or ask the operator to change the job’s saved machine. See CLI-backed
      model and scheduled-command guidance .
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: Logbook now tells you when a missing model is blocking queued work.
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  - quote: API clients can now get a saved session’s available commands without waiting
      for model information they didn’t ask for.
    source_release: https://docs.openclaw.ai/releases/2026.10.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-model-support-changes-in-v2026-10-6
  source_release: openclaw-2026-10-22-v2026-10-6-56379f53
  source_type: openclaw_changelog
  theme: model-support
  title: 4 Model Support changes in v2026.10.6
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-10-21-switching-models-mid-session-now-shows-a-confirmation-dialog-start-a-new-session|Switching
  models mid-session now shows a confirmation dialog]]'
- '[[Changes/GitHub Copilot CLI/2026-10-22-3-model-support-changes-in-v1-0-103|3 Model
  Support changes in v1.0.103]]'
- '[[Changes/Lovable/2026-10-22-gemini-2-5-chat-models-are-retired-for-your-app-s-ai-features|Gemini
  2.5 chat models are retired for your app''s AI features]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-22-v2026-10-6-56379f53|openclaw-2026-10-22-v2026-10-6-56379f53]]'
source_type: openclaw_changelog
theme: model-support
title: 4 Model Support changes in v2026.10.6
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v2026.10.6

**OpenClaw** · 2026-10-22 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.6) · from [[Releases/OpenClaw/openclaw-2026-10-22-v2026-10-6-56379f53|v2026.10.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Windows now waits for local-model shutdown helpers to finish before moving on.

> A scheduled command pinned to the Gateway now refuses a prompt that asks it to run on another machine. If a saved job reports this conflict, fix its prompt or ask the operator to change the job’s saved machine. See CLI-backed model and scheduled-command guidance .

> Logbook now tells you when a missing model is blocking queued work.

> API clients can now get a saved session’s available commands without waiting for model information they didn’t ask for.

Source: https://docs.openclaw.ai/releases/2026.10.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-22-shell-completion-now-finds-global-flags-after-subcommands-regenerate-your-saved|Shell completion now finds global flags after subcommands]] · Editor Experience
- [[Changes/OpenClaw/2026-10-22-5-automation-and-scheduling-changes-in-v2026-10-6|5 Automation and Scheduling changes in v2026.10.6]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-22-3-agent-mode-changes-in-v2026-10-6|3 Agent Mode changes in v2026.10.6]] · Agent Mode
- [[Changes/OpenClaw/2026-10-22-security-release-v2026-10-6-adds-remediations-for-the-emudhra-certificate-compro|Security release: v2026.10.6 adds remediations for the eMudhra certificate compromise]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-22-restarting-the-same-official-docker-container-no-longer-copies-all-its-saved-sta|Restarting the same official Docker container no longer copies all its saved state…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-10-22-7-developer-workflow-changes-in-v2026-10-6|7 Developer Workflow changes in v2026.10.6]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-22-linux-camera-discovery-now-reports-an-unreadable-device-folder-as-an-error-inste|Linux camera discovery now reports an unreadable device folder as an error instead…]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-22-web-search-timeout-errors-now-tell-you-the-request-s-actual-time-limit-see-web-t|Web search timeout errors now tell you the request’s actual time limit]] · Search and Browsing
- [[Changes/OpenClaw/2026-10-22-3-voice-and-audio-changes-in-v2026-10-6|3 Voice and Audio changes in v2026.10.6]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-22-session-share-now-shows-an-error-when-it-can-t-discover-receivers-instead-of-an|Session Share now shows an error when it can’t discover receivers, instead…]] · Collaboration
- [[Changes/OpenClaw/2026-10-22-2-mobile-and-desktop-changes-in-v2026-10-6|2 Mobile and Desktop changes in v2026.10.6]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-22-10-apps-and-integrations-changes-in-v2026-10-6|10 Apps and Integrations changes in v2026.10.6]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-22-2-enterprise-and-administration-changes-in-v2026-10-6|2 Enterprise and Administration changes in v2026.10.6]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-22-4-context-window-changes-in-v2026-10-6|4 Context Window changes in v2026.10.6]] · Context Window
- [[Changes/OpenClaw/2026-10-22-mcp-sign-in-errors-now-give-a-safe-reason-and-tell-you-how-to-sign-in-or-fix-you|MCP sign-in errors now give a safe reason and tell you how to sign in or fix…]] · Account and Access
- [[Changes/OpenClaw/2026-10-22-4-memory-and-personalization-changes-in-v2026-10-6|4 Memory and Personalization changes in v2026.10.6]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-22-you-can-now-stop-a-gateway-that-has-been-stuck-starting-for-more-than-five-minut|Stop a Gateway that has been stuck starting for more than five minutes without ever…]] · Other changes
- [[Changes/OpenClaw/2026-10-22-you-can-now-find-a-claude-code-conversation-by-its-exact-session-id-even-when-th|Find a Claude Code conversation by its exact session ID even when the normal search…]] · Other changes
- [[Changes/OpenClaw/2026-10-22-60-other-changes-in-v2026-10-6|60 other changes in v2026.10.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-22 · Lovable · [[Changes/Lovable/2026-10-22-gemini-2-5-chat-models-are-retired-for-your-app-s-ai-features|Gemini 2.5 chat models are retired for your app's AI features]]
- Later: 2026-10-22 · Raycast · [[Changes/Raycast/2026-10-22-ai-newly-installed-extension-provided-models-are-now-searchable-in-model-pickers|AI : Newly installed Extension-provided models are now searchable in model pickers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-22-15b257&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-22-4-model-support-changes-in-v2026-10-6.md%0ACard%20ID%3A%20openclaw-2026-10-22-15b257%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->