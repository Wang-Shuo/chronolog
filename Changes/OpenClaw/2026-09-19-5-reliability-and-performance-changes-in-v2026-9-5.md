---
card_id: openclaw-2026-09-19-1a57c2
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Reliability and Performance: 5 changes in v2026.9.5
  — Session refreshes also release old versions of session-list data that were being…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1374
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1f5c66a9fb1a0e39e08747c6006676ce22cf92dbfa21901d2f698fdcc699c947
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-1a57c2
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 5 Reliability and Performance changes'
  evidence:
  - quote: Session refreshes also release old versions of session-list data that were
      being kept in memory, fixing a leak that could exhaust Gateway memory and interrupt
      work.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Shutdown failures now retain the failed step and redacted exception details
      after exit, with bounded time for pending logs to flush. Inspect them with openclaw
      gateway stability --bundle latest --json . This helps diagnose failures once
      the fixed Gateway is running; it does not repair the original exception or recover
      details already lost.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Long Codex sessions load a bounded amount of mirrored history for prompt
      preparation and compaction, reducing memory allocation along that path while
      keeping full transcripts and native resume state. If required recent context
      cannot fit, preparation fails explicitly. An authorized standalone /reset or
      /new can recover by clearing active context, which loses conversation continuity;
      /reset soft is insufficient. OpenClaw does not reset or resume interrupted work
      automatically.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: File checks for large workspaces are also faster when preparing node and
      cloud sessions. Stop can cancel preparation before a worker is allocated, though
      file reads already underway must finish before cleanup. Upgrade the Gateway
      to receive this fix; updating only the node is not enough.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: More simultaneous turns can use more memory and put more pressure on providers.
      Existing agents.defaults.maxConcurrent settings still take precedence. Set a
      lower explicit limit for a constrained machine or resource-heavy work.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 5-reliability-and-performance-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: reliability-performance
  title: 5 Reliability and Performance changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-09-15-removed-a-redundant-scan-of-your-skills-rules-and-other-customization-files-that|Removed
  a redundant scan of your skills, rules, and other customization files…]]'
- '[[Changes/GitHub Copilot CLI/2026-09-16-speed-up-startup-when-resuming-an-existing-local-session-by-its-exact-uuid-with|Speed
  up startup when resuming an existing local session by its exact UUID with --resume]]'
- '[[Changes/Claude Code/2026-09-17-added-a-visible-warning-when-memory-usage-is-critical-with-steps-to-free-memory|Added
  a visible warning when memory usage is critical, with steps to free memory…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: reliability-performance
title: 5 Reliability and Performance changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Reliability and Performance changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Session refreshes also release old versions of session-list data that were being kept in memory, fixing a leak that could exhaust Gateway memory and interrupt work.

> Shutdown failures now retain the failed step and redacted exception details after exit, with bounded time for pending logs to flush. Inspect them with openclaw gateway stability --bundle latest --json . This helps diagnose failures once the fixed Gateway is running; it does not repair the original exception or recover details already lost.

> Long Codex sessions load a bounded amount of mirrored history for prompt preparation and compaction, reducing memory allocation along that path while keeping full transcripts and native resume state. If required recent context cannot fit, preparation fails explicitly. An authorized standalone /reset or /new can recover by clearing active context, which loses conversation continuity; /reset soft is insufficient. OpenClaw does not reset or resume interrupted work automatically.

> File checks for large workspaces are also faster when preparing node and cloud sessions. Stop can cancel preparation before a worker is allocated, though file reads already underway must finish before cleanup. Upgrade the Gateway to receive this fix; updating only the node is not enough.

> More simultaneous turns can use more memory and put more pressure on providers. Existing agents.defaults.maxConcurrent settings still take precedence. Set a lower explicit limit for a constrained machine or resource-heavy work.

Source: https://docs.openclaw.ai/releases/2026.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-19-20-context-window-changes-in-v2026-9-5|20 Context Window changes in v2026.9.5]] · Context Window
- [[Changes/OpenClaw/2026-09-19-14-collaboration-changes-in-v2026-9-5|14 Collaboration changes in v2026.9.5]] · Collaboration
- [[Changes/OpenClaw/2026-09-19-the-browser-sidebar-gains-a-download-file-button-for-the-image-video-or-document|The Browser sidebar gains a Download file button for the image, video, or document…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-19-29-developer-workflow-changes-in-v2026-9-5|29 Developer Workflow changes in v2026.9.5]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-19-retained-conversation-history-continues-to-follow-current-sharing-permissions-af|Retained conversation history continues to follow current sharing permissions after…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-19-2-enterprise-and-administration-changes-in-v2026-9-5|2 Enterprise and Administration changes in v2026.9.5]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-19-72-agent-mode-changes-in-v2026-9-5|72 Agent Mode changes in v2026.9.5]] · Agent Mode
- [[Changes/OpenClaw/2026-09-19-21-editor-experience-changes-in-v2026-9-5|21 Editor Experience changes in v2026.9.5]] · Editor Experience
- [[Changes/OpenClaw/2026-09-19-28-model-support-changes-in-v2026-9-5|28 Model Support changes in v2026.9.5]] · Model Support
- [[Changes/OpenClaw/2026-09-19-39-safety-and-privacy-changes-in-v2026-9-5|39 Safety and Privacy changes in v2026.9.5]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-19-14-automation-and-scheduling-changes-in-v2026-9-5|14 Automation and Scheduling changes in v2026.9.5]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-19-32-interface-experience-changes-in-v2026-9-5|32 Interface Experience changes in v2026.9.5]] · Interface Experience
- [[Changes/OpenClaw/2026-09-19-you-can-now-set-the-approval-reviewer-s-reasoning-and-optional-fast-mode-indepen|Set the approval reviewer's reasoning and optional Fast mode independently…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-19-you-can-now-install-the-cli-on-freebsd-with-install-cli-sh-using-system-node-and|Install the CLI on FreeBSD with install-cli.sh using system Node and npm]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-19-6-pricing-model-changes-in-v2026-9-5|6 Pricing Model changes in v2026.9.5]] · Pricing Model
- [[Changes/OpenClaw/2026-09-19-28-account-and-access-changes-in-v2026-9-5|28 Account and Access changes in v2026.9.5]] · Account and Access
- [[Changes/OpenClaw/2026-09-19-31-memory-and-personalization-changes-in-v2026-9-5|31 Memory and Personalization changes in v2026.9.5]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-19-you-can-now-ask-btw-side-questions-about-photos-attached-to-the-current-message|Ask /btw side questions about photos attached to the current message when using…]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-19-52-apps-and-integrations-changes-in-v2026-9-5|52 Apps and Integrations changes in v2026.9.5]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-19-23-mobile-and-desktop-changes-in-v2026-9-5|23 Mobile and Desktop changes in v2026.9.5]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-19-6-search-and-browsing-changes-in-v2026-9-5|6 Search and Browsing changes in v2026.9.5]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-19-video-generation-preserves-repeated-reference-positions-so-the-same-image-can-se|Video generation preserves repeated reference positions, so the same image can serve…]] · Music Generation
- [[Changes/OpenClaw/2026-09-19-browser-pages-appear-directly-in-the-chat-panel-header-leaving-more-room-for-the|Browser pages appear directly in the Chat panel header, leaving more room for the page]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-19-7-files-and-data-changes-in-v2026-9-5|7 Files and Data changes in v2026.9.5]] · Files and Data
- [[Changes/OpenClaw/2026-09-19-15-voice-and-audio-changes-in-v2026-9-5|15 Voice and Audio changes in v2026.9.5]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-19-shared-helpers-consolidate-repeated-implementation-including-preparation-and-res|Shared helpers consolidate repeated implementation, including preparation…]] · Video Generation
- [[Changes/OpenClaw/2026-09-19-171-other-changes-in-v2026-9-5|171 other changes in v2026.9.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-added-a-visible-warning-when-memory-usage-is-critical-with-steps-to-free-memory|Added a visible warning when memory usage is critical, with steps to free memory…]]
- Later: 2026-09-21 · Open WebUI · [[Changes/Open WebUI/2026-09-21-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-1a57c2&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-5-reliability-and-performance-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-1a57c2%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->