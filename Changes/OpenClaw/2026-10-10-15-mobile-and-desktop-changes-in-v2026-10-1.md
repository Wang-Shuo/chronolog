---
card_id: openclaw-2026-10-10-0ca27b
date: '2026-10-10'
description: 'OpenClaw · 2026-10-10 · Mobile and Desktop: 15 changes in v2026.10.1
  — Supported Bun-only installations on macOS and Linux can run the ordinary openclaw…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1306
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c349bc3b15f076f1c8b1639455d3f22375b7d4e2d827c6584432ec19dcc73efe
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-10-0ca27b
  comparison: ''
  date: '2026-10-10'
  description: 'OpenClaw — v2026.10.1: 15 Mobile and Desktop changes'
  evidence:
  - quote: Supported Bun-only installations on macOS and Linux can run the ordinary
      openclaw command without Node. Use the documented Bun 1.4 or newer launcher
      and keep the command on your PATH; reinstalling or approving its repair with
      doctor --fix refreshes it. Older installed updaters still need a supported upgrade
      route.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Reactions to supported channel-origin prompts can appear on the channel
      as the bot; reactions to assistant replies stay local. Local reactions survive
      a failed mirror. Telegram and WhatsApp can restore a remaining emoji after removal,
      but channel reactions can still be wrong when several people chose the same
      emoji.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: iOS and Android let you view and add emoji reactions to eligible saved
      messages in shared conversations, with counts, accessible pickers and live updates
      without extra notifications. Android includes media-only messages through long-press.
      Reaction controls follow conversation permissions and are unavailable for archived,
      source-catalog or unsaved messages.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: If iOS cannot identify you when first connecting, your own reactions may
      not highlight or be removable until you reconnect or switch conversations. See
      iOS reactions and shared-conversation reactions .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: You can paste a copied screenshot or supported image into an attachment-enabled
      iPhone or iPad chat without saving it to Photos first, then remove it before
      sending. Images take precedence over text in a mixed paste. File links copied
      from Files are not supported, and attachment limits still apply.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Mobile Settings links work with a custom web-interface path when pairing
      uses a new code. Affected clients need a new code and must re-pair. Setup also
      shows its fixed welcomes and choices in the selected Simplified or Traditional
      Chinese language.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: The optional macOS DNS guide explains what happens when Homebrew times
      out or is terminated. Fresh installs with no Matrix configuration or old Matrix
      data no longer receive an irrelevant migration warning. Configured installations
      and incomplete scans retain the migration checks .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Each WhatsApp named account uses its own group reply preference, falling
      back to its configured mention policy. If a group relied on the old shared setting,
      rerun /activation always or /activation mention in that group with the intended
      account. Doctor preserves configured accounts and warns about ambiguous unlinked
      defaults; review them yourself and preserve needed shared policy before removing
      an unwanted default.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Older skills and hooks need a manual metadata update to retain prerequisites,
      installation hints and hook events: rename metadata.clawdbot to metadata.openclaw
      , preserving existing canonical values if both blocks are present. Reconcile
      .clawdhub tracking into .clawhub without overwriting records. Where node clients
      are equally matched, select an exact node ID; the April 2026 macOS setup PATH-check
      exemption is also retired.'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Android group edits stay with their original Gateway: switching connections
      rejects stale rename and delete dialogs, and deleting a group leaves its conversations
      Ungrouped. iPhone and iPad demo captures hide real saved Gateway and credential
      controls. Android keeps current notification forwarding while removing older
      recent-app suggestions.'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Reading and searching skills on Android has translated labels in 21 existing
      non-English locales.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Desktop reconnects no longer accumulate repeated attempts to clean up a
      failed session. Reconnecting alone no longer retries a cleanup failure , even
      if it was transient. Inspect the reported process or filesystem error and perform
      lifecycle cleanup, such as turning Host Desktop off in Labs; a replacement starts
      only after cleanup succeeds. See desktop configuration .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Stopping Beam and Codex desktop watchers cancels polls and retries and
      waits for admitted work, preventing late generation publication. #163914 . Thanks
      @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'A healthy macOS Crabbox worker can re-enroll on a busy host without a
      false reprovisioning error. #162233 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Starting OpenClaw with its managed Bun runtime or the macOS bundled runtime
      no longer installs missing packages implicitly. Install dependencies explicitly;
      existing services receive the launch flag through normal reinstall or update,
      and direct stock-Bun launches should use --no-install . Private-network Matrix
      and Mattermost settings need Doctor repair on 2026.9.7 before upgrading; Tlon
      retains update-time migration, while direct replacement needs openclaw doctor
      --fix . See Bun installation and the configuration migration guide .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 15-mobile-and-desktop-changes-in-v2026-10-1
  source_release: openclaw-2026-10-10-v2026-10-1-d64e4e93
  source_type: openclaw_changelog
  theme: mobile-desktop
  title: 15 Mobile and Desktop changes in v2026.10.1
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-08-3-mobile-and-desktop-changes-in-v2026-9-9|3 Mobile
  and Desktop changes in v2026.9.9]]'
- '[[Changes/Replit/2026-10-09-replit-desktop-windows-preview-with-microsoft-and-nvidia|Replit
  Desktop Windows preview with Microsoft and NVIDIA]]'
- '[[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile
  and Desktop changes in v0.12.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|openclaw-2026-10-10-v2026-10-1-d64e4e93]]'
source_type: openclaw_changelog
theme: mobile-desktop
title: 15 Mobile and Desktop changes in v2026.10.1
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Mobile and Desktop changes in v2026.10.1

**OpenClaw** · 2026-10-10 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.1) · from [[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Supported Bun-only installations on macOS and Linux can run the ordinary openclaw command without Node. Use the documented Bun 1.4 or newer launcher and keep the command on your PATH; reinstalling or approving its repair with doctor --fix refreshes it. Older installed updaters still need a supported upgrade route.

> Reactions to supported channel-origin prompts can appear on the channel as the bot; reactions to assistant replies stay local. Local reactions survive a failed mirror. Telegram and WhatsApp can restore a remaining emoji after removal, but channel reactions can still be wrong when several people chose the same emoji.

> iOS and Android let you view and add emoji reactions to eligible saved messages in shared conversations, with counts, accessible pickers and live updates without extra notifications. Android includes media-only messages through long-press. Reaction controls follow conversation permissions and are unavailable for archived, source-catalog or unsaved messages.

> If iOS cannot identify you when first connecting, your own reactions may not highlight or be removable until you reconnect or switch conversations. See iOS reactions and shared-conversation reactions .

> You can paste a copied screenshot or supported image into an attachment-enabled iPhone or iPad chat without saving it to Photos first, then remove it before sending. Images take precedence over text in a mixed paste. File links copied from Files are not supported, and attachment limits still apply.

> Mobile Settings links work with a custom web-interface path when pairing uses a new code. Affected clients need a new code and must re-pair. Setup also shows its fixed welcomes and choices in the selected Simplified or Traditional Chinese language.

> The optional macOS DNS guide explains what happens when Homebrew times out or is terminated. Fresh installs with no Matrix configuration or old Matrix data no longer receive an irrelevant migration warning. Configured installations and incomplete scans retain the migration checks .

> Each WhatsApp named account uses its own group reply preference, falling back to its configured mention policy. If a group relied on the old shared setting, rerun /activation always or /activation mention in that group with the intended account. Doctor preserves configured accounts and warns about ambiguous unlinked defaults; review them yourself and preserve needed shared policy before removing an unwanted default.

> Older skills and hooks need a manual metadata update to retain prerequisites, installation hints and hook events: rename metadata.clawdbot to metadata.openclaw , preserving existing canonical values if both blocks are present. Reconcile .clawdhub tracking into .clawhub without overwriting records. Where node clients are equally matched, select an exact node ID; the April 2026 macOS setup PATH-check exemption is also retired.

> Android group edits stay with their original Gateway: switching connections rejects stale rename and delete dialogs, and deleting a group leaves its conversations Ungrouped. iPhone and iPad demo captures hide real saved Gateway and credential controls. Android keeps current notification forwarding while removing older recent-app suggestions.

> Reading and searching skills on Android has translated labels in 21 existing non-English locales.

> Desktop reconnects no longer accumulate repeated attempts to clean up a failed session. Reconnecting alone no longer retries a cleanup failure , even if it was transient. Inspect the reported process or filesystem error and perform lifecycle cleanup, such as turning Host Desktop off in Labs; a replacement starts only after cleanup succeeds. See desktop configuration .

> Stopping Beam and Codex desktop watchers cancels polls and retries and waits for admitted work, preventing late generation publication. #163914 . Thanks @steipete .

> A healthy macOS Crabbox worker can re-enroll on a busy host without a false reprovisioning error. #162233 . Thanks @steipete .

> Starting OpenClaw with its managed Bun runtime or the macOS bundled runtime no longer installs missing packages implicitly. Install dependencies explicitly; existing services receive the launch flag through normal reinstall or update, and direct stock-Bun launches should use --no-install . Private-network Matrix and Mattermost settings need Doctor repair on 2026.9.7 before upgrading; Tlon retains update-time migration, while direct replacement needs openclaw doctor --fix . See Bun installation and the configuration migration guide .

Source: https://docs.openclaw.ai/releases/2026.10.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-10-2-reliability-and-performance-changes-in-v2026-10-1|2 Reliability and Performance changes in v2026.10.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1|13 Memory and Personalization changes in v2026.10.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-10-96-apps-and-integrations-changes-in-v2026-10-1|96 Apps and Integrations changes in v2026.10.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-10-12-context-window-changes-in-v2026-10-1|12 Context Window changes in v2026.10.1]] · Context Window
- [[Changes/OpenClaw/2026-10-10-4-pricing-model-changes-in-v2026-10-1|4 Pricing Model changes in v2026.10.1]] · Pricing Model
- [[Changes/OpenClaw/2026-10-10-18-account-and-access-changes-in-v2026-10-1|18 Account and Access changes in v2026.10.1]] · Account and Access
- [[Changes/OpenClaw/2026-10-10-18-model-support-changes-in-v2026-10-1|18 Model Support changes in v2026.10.1]] · Model Support
- [[Changes/OpenClaw/2026-10-10-20-safety-and-privacy-changes-in-v2026-10-1|20 Safety and Privacy changes in v2026.10.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-10-3-search-and-browsing-changes-in-v2026-10-1|3 Search and Browsing changes in v2026.10.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-10-10-plugin-authors-can-await-session-history-extension-changes-and-replay-metadata-t|Plugin authors can await session history, extension changes and replay metadata]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-10-2-accessibility-and-localization-changes-in-v2026-10-1|2 Accessibility and Localization changes in v2026.10.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-10-10-image-generation-with-oauth-can-retry-using-a-supported-openai-chat-model-in-age|Image generation with OAuth can retry using a supported OpenAI chat model…]] · Image Generation
- [[Changes/OpenClaw/2026-10-10-10-editor-experience-changes-in-v2026-10-1|10 Editor Experience changes in v2026.10.1]] · Editor Experience
- [[Changes/OpenClaw/2026-10-10-2-files-and-data-changes-in-v2026-10-1|2 Files and Data changes in v2026.10.1]] · Files and Data
- [[Changes/OpenClaw/2026-10-10-8-voice-and-audio-changes-in-v2026-10-1|8 Voice and Audio changes in v2026.10.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-10-27-agent-mode-changes-in-v2026-10-1|27 Agent Mode changes in v2026.10.1]] · Agent Mode
- [[Changes/OpenClaw/2026-10-10-12-collaboration-changes-in-v2026-10-1|12 Collaboration changes in v2026.10.1]] · Collaboration
- [[Changes/OpenClaw/2026-10-10-video-previews-new-video-previews-can-download-media-before-play|Video previews: New video previews can download media before Play]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-10-11-developer-workflow-changes-in-v2026-10-1|11 Developer Workflow changes in v2026.10.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-10-5-enterprise-and-administration-changes-in-v2026-10-1|5 Enterprise and Administration changes in v2026.10.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-10-20-interface-experience-changes-in-v2026-10-1|20 Interface Experience changes in v2026.10.1]] · Interface Experience
- [[Changes/OpenClaw/2026-10-10-10-automation-and-scheduling-changes-in-v2026-10-1|10 Automation and Scheduling changes in v2026.10.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-10-112-other-changes-in-v2026-10-1|112 other changes in v2026.10.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-10-10 · Open WebUI · [[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile and Desktop changes in v0.12.0]]
- Later: 2026-10-12 · Google Antigravity · [[Changes/Google Antigravity/2026-10-12-2-mobile-and-desktop-changes-in-hub-v2-23-0-permissions-picker|2 Mobile and Desktop changes in HUB v2.23.0 — Permissions picker…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-10-0ca27b&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-10-15-mobile-and-desktop-changes-in-v2026-10-1.md%0ACard%20ID%3A%20openclaw-2026-10-10-0ca27b%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->