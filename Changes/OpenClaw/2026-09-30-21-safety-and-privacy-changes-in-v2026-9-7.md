---
card_id: openclaw-2026-09-30-8850dd
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Safety and Privacy: 21 changes in v2026.9.7
  — Guests with session-write access can create and control their own chats. Full
  permission…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2255
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bb66aba2709ed9e17ef6b3ca01441c7dba0b29e070d64e42742af39dc27b0f4c
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-8850dd
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 21 Safety and Privacy changes'
  evidence:
  - quote: Guests with session-write access can create and control their own chats.
      Full permission mode, sandbox changes, and changes to an existing chat’s context
      window still require an administrator.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Take photo opens a local camera preview so you can capture, retake, and
      confirm a photo before attaching it. Confirmation adds it to your draft without
      sending it. Live preview needs HTTPS or localhost and camera permission; if
      permission is denied, choose Retry or Upload photo.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Skill security scans now correctly count matches left out of a long report,
      fixing inflated totals when detection rules overlap. The checks themselves are
      unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Android setup groups optional permissions under a shorter initial list
      and Additional features . You can skip all of them. Camera and Location still
      need to be enabled separately after permission is granted. If your account allows
      it, you can approve the phone's requested access directly during setup.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Android has a full-width writing field with compact controls underneath.
      Use + → Camera to add a photo or video to your draft; camera permission is required,
      plus microphone permission for video. Completed replies stay visible when you
      collapse the tool activity, with counts of failed or blocked tools.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Android Talk keeps error messages open until you dismiss them, giving you
      time to read what needs fixing. Granting microphone permission can now start
      Listening on the first attempt. Missing providers or invalid credentials still
      need to be corrected in Gateway setup.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The Wear OS companion shows its full startup icon and keeps the watch background
      black in Light appearance. Voice controls and permission guidance can scroll
      when translated text or larger text sizes need more room. The watch still needs
      a paired Android phone running OpenClaw and connected to the Gateway.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: OpenAI setup makes Codex login, Sign in with ChatGPT (Beta), and API keys
      easier to distinguish, with model choices tied to the selected account. ChatGPT
      sign-in requires registration and consent to share tokens. It does not cover
      every model or media tool, and OpenClaw cannot show its quota or set per-app
      limits. The authentication comparison explains which credentials you need.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Local Codex can read full uploaded documents beyond their shortened previews
      when running without a sandbox and with read permission. Optional plugin tools
      already granted to the agent remain available. You can opt into Ultrafast with
      appServer.enableUltrafast ; it is off by default and requires account and model
      support.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Scheduled jobs can launch workers with their already-approved permissions
      without a mistaken administrator-permission error. Configured channel owners
      can also manage automations again after delegated work finishes. Existing restrictions
      still apply, and explicitly requesting Full Access still requires administrator
      permission.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Session browser dashboards also let people with conversation write access
      interact without browser administrator access. They start without your saved
      sign-ins and require Playwright with local managed Chromium. Conversation access
      limits still apply, and read-only, sandbox-required, or locked-model sessions
      are excluded. Stopping the dashboard, resetting the conversation, or restarting
      OpenClaw loses its page state.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: After you sign in or finish a manual step on a conversation-attached or
      cloud-session desktop , you can ask the agent to continue without separately
      releasing control in the viewer. It uses its existing permission, takes a fresh
      screenshot, and does not replay interrupted input. You can take control back
      at any time. This handoff is limited to attached and cloud-session desktops.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: You can open interactive application previews on a conversation's dedicated
      attached secondary worker when your write and tool permissions allow it. Sessions
      that require a sandbox or lock model selection are excluded. Anyone with the
      preview link can use it while it is open, even if the person who created it
      loses access. Close the preview to withdraw the link.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: When MXC cannot prepare a command, it removes the temporary sandbox directory
      instead of leaving it behind. The original error remains available to help diagnose
      the failure.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Native Codex apps keep their configured approval settings, and permitted
      reads can ask for consent. Check explicit tool exceptions separately. Do not
      rely on the interactive destructive-action setting alone to disable explicitly
      enabled native tools.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Back up your data before upgrading, including SQLite's write-ahead log.
      This change upgrades shared state from schema 18 to 19. Downgrading requires
      a matching pre-upgrade backup in a separate state directory and can lose later
      permission revocations and receipts. Never lower schema markers to force a downgrade.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Memory reads stay within their authorized folder when retrying, and canceled
      delegated work stops starting new workspace transfers. Required sandboxing now
      applies from the first request through the OpenAI-compatible APIs. If the required
      sandbox is unavailable, the run is refused.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Podman follows your selected connection and SSH identity. If an existing
      sandbox stops working after upgrading, follow the Podman recovery guide . Restore
      its original connection and save needed container data before recreating it.
      Mounted workspace files remain, but data inside the old container is not transferred.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Plugin commands are now rejected if their permission declarations are invalid.
      Public commands also cannot pass along the private permission used to author
      skills. Valid plugin commands keep their existing behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: 'With operator.write permission, you can also ask the agent to archive,
      restore, or stop sessions you can access and created or were assigned to. Stop
      normally clears queued follow-ups, so request clearQueued: false if you want
      to keep them.'
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Agents also get guidance to avoid repeatedly asking permission for work
      you already requested. Existing approvals still apply, and verified human contributor
      credit can follow new delegations with the person's consent.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 21-safety-and-privacy-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: safety-privacy
  title: 21 Safety and Privacy changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/Devin/2026-09-30-hardware-accelerated-emulators-in-sessions|Hardware-Accelerated
  Emulators in Sessions]]'
- '[[Changes/GitHub Copilot CLI/2026-09-30-permission-prompts-remain-answerable-after-resuming-interrupted-sessions|Permission
  prompts remain answerable after resuming interrupted sessions]]'
- '[[Changes/Lovable/2026-09-30-rotate-your-cloud-database-password-from-chat|Rotate
  your Cloud database password from chat]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: safety-privacy
title: 21 Safety and Privacy changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 21 Safety and Privacy changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Guests with session-write access can create and control their own chats. Full permission mode, sandbox changes, and changes to an existing chat’s context window still require an administrator.

> Take photo opens a local camera preview so you can capture, retake, and confirm a photo before attaching it. Confirmation adds it to your draft without sending it. Live preview needs HTTPS or localhost and camera permission; if permission is denied, choose Retry or Upload photo.

> Skill security scans now correctly count matches left out of a long report, fixing inflated totals when detection rules overlap. The checks themselves are unchanged.

> Android setup groups optional permissions under a shorter initial list and Additional features . You can skip all of them. Camera and Location still need to be enabled separately after permission is granted. If your account allows it, you can approve the phone's requested access directly during setup.

> Android has a full-width writing field with compact controls underneath. Use + → Camera to add a photo or video to your draft; camera permission is required, plus microphone permission for video. Completed replies stay visible when you collapse the tool activity, with counts of failed or blocked tools.

> Android Talk keeps error messages open until you dismiss them, giving you time to read what needs fixing. Granting microphone permission can now start Listening on the first attempt. Missing providers or invalid credentials still need to be corrected in Gateway setup.

> The Wear OS companion shows its full startup icon and keeps the watch background black in Light appearance. Voice controls and permission guidance can scroll when translated text or larger text sizes need more room. The watch still needs a paired Android phone running OpenClaw and connected to the Gateway.

> OpenAI setup makes Codex login, Sign in with ChatGPT (Beta), and API keys easier to distinguish, with model choices tied to the selected account. ChatGPT sign-in requires registration and consent to share tokens. It does not cover every model or media tool, and OpenClaw cannot show its quota or set per-app limits. The authentication comparison explains which credentials you need.

> Local Codex can read full uploaded documents beyond their shortened previews when running without a sandbox and with read permission. Optional plugin tools already granted to the agent remain available. You can opt into Ultrafast with appServer.enableUltrafast ; it is off by default and requires account and model support.

> Scheduled jobs can launch workers with their already-approved permissions without a mistaken administrator-permission error. Configured channel owners can also manage automations again after delegated work finishes. Existing restrictions still apply, and explicitly requesting Full Access still requires administrator permission.

> Session browser dashboards also let people with conversation write access interact without browser administrator access. They start without your saved sign-ins and require Playwright with local managed Chromium. Conversation access limits still apply, and read-only, sandbox-required, or locked-model sessions are excluded. Stopping the dashboard, resetting the conversation, or restarting OpenClaw loses its page state.

> After you sign in or finish a manual step on a conversation-attached or cloud-session desktop , you can ask the agent to continue without separately releasing control in the viewer. It uses its existing permission, takes a fresh screenshot, and does not replay interrupted input. You can take control back at any time. This handoff is limited to attached and cloud-session desktops.

> You can open interactive application previews on a conversation's dedicated attached secondary worker when your write and tool permissions allow it. Sessions that require a sandbox or lock model selection are excluded. Anyone with the preview link can use it while it is open, even if the person who created it loses access. Close the preview to withdraw the link.

> When MXC cannot prepare a command, it removes the temporary sandbox directory instead of leaving it behind. The original error remains available to help diagnose the failure.

> Native Codex apps keep their configured approval settings, and permitted reads can ask for consent. Check explicit tool exceptions separately. Do not rely on the interactive destructive-action setting alone to disable explicitly enabled native tools.

> Back up your data before upgrading, including SQLite's write-ahead log. This change upgrades shared state from schema 18 to 19. Downgrading requires a matching pre-upgrade backup in a separate state directory and can lose later permission revocations and receipts. Never lower schema markers to force a downgrade.

> Memory reads stay within their authorized folder when retrying, and canceled delegated work stops starting new workspace transfers. Required sandboxing now applies from the first request through the OpenAI-compatible APIs. If the required sandbox is unavailable, the run is refused.

> Podman follows your selected connection and SSH identity. If an existing sandbox stops working after upgrading, follow the Podman recovery guide . Restore its original connection and save needed container data before recreating it. Mounted workspace files remain, but data inside the old container is not transferred.

> Plugin commands are now rejected if their permission declarations are invalid. Public commands also cannot pass along the private permission used to author skills. Valid plugin commands keep their existing behavior.

> With operator.write permission, you can also ask the agent to archive, restore, or stop sessions you can access and created or were assigned to. Stop normally clears queued follow-ups, so request clearQueued: false if you want to keep them.

> Agents also get guidance to avoid repeatedly asking permission for work you already requested. Existing approvals still apply, and verified human contributor credit can follow new delegations with the person's consent.

Source: https://docs.openclaw.ai/releases/2026.9.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-30-4-context-window-changes-in-v2026-9-7|4 Context Window changes in v2026.9.7]] · Context Window
- [[Changes/OpenClaw/2026-09-30-13-developer-workflow-changes-in-v2026-9-7|13 Developer Workflow changes in v2026.9.7]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-30-3-files-and-data-changes-in-v2026-9-7|3 Files and Data changes in v2026.9.7]] · Files and Data
- [[Changes/OpenClaw/2026-09-30-13-account-and-access-changes-in-v2026-9-7|13 Account and Access changes in v2026.9.7]] · Account and Access
- [[Changes/OpenClaw/2026-09-30-2-enterprise-and-administration-changes-in-v2026-9-7|2 Enterprise and Administration changes in v2026.9.7]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-30-15-memory-and-personalization-changes-in-v2026-9-7|15 Memory and Personalization changes in v2026.9.7]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-30-33-agent-mode-changes-in-v2026-9-7|33 Agent Mode changes in v2026.9.7]] · Agent Mode
- [[Changes/OpenClaw/2026-09-30-17-interface-experience-changes-in-v2026-9-7|17 Interface Experience changes in v2026.9.7]] · Interface Experience
- [[Changes/OpenClaw/2026-09-30-36-apps-and-integrations-changes-in-v2026-9-7|36 Apps and Integrations changes in v2026.9.7]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-30-2-video-generation-changes-in-v2026-9-7|2 Video Generation changes in v2026.9.7]] · Video Generation
- [[Changes/OpenClaw/2026-09-30-12-voice-and-audio-changes-in-v2026-9-7|12 Voice and Audio changes in v2026.9.7]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-30-administrators-can-opt-into-heap-snapshots-to-investigate-memory-growth-a-snapsh|Administrators can opt into heap snapshots to investigate memory growth]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-30-14-mobile-and-desktop-changes-in-v2026-9-7|14 Mobile and Desktop changes in v2026.9.7]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-30-9-editor-experience-changes-in-v2026-9-7|9 Editor Experience changes in v2026.9.7]] · Editor Experience
- [[Changes/OpenClaw/2026-09-30-22-model-support-changes-in-v2026-9-7|22 Model Support changes in v2026.9.7]] · Model Support
- [[Changes/OpenClaw/2026-09-30-11-automation-and-scheduling-changes-in-v2026-9-7|11 Automation and Scheduling changes in v2026.9.7]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-30-4-search-and-browsing-changes-in-v2026-9-7|4 Search and Browsing changes in v2026.9.7]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-30-3-pricing-model-changes-in-v2026-9-7|3 Pricing Model changes in v2026.9.7]] · Pricing Model
- [[Changes/OpenClaw/2026-09-30-10-collaboration-changes-in-v2026-9-7|10 Collaboration changes in v2026.9.7]] · Collaboration
- [[Changes/OpenClaw/2026-09-30-4-multimodal-input-changes-in-v2026-9-7|4 Multimodal Input changes in v2026.9.7]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-30-72-other-changes-in-v2026-9-7|72 other changes in v2026.9.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-30 · Lovable · [[Changes/Lovable/2026-09-30-rotate-your-cloud-database-password-from-chat|Rotate your Cloud database password from chat]]
- Later: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety and Privacy changes in v2.1.287]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-8850dd&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-21-safety-and-privacy-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-8850dd%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->