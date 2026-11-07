---
card_id: openclaw-2026-09-19-0440ac
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Collaboration: 14 changes in v2026.9.5 — The
  UI screenshots below use a fictional Waypoint launch team and synthetic conversations…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1214
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 290b581e22c8d6f60cb1e298a62f9187af217a49e8c6541bb614d8638247b5d5
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-0440ac
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 14 Collaboration changes'
  evidence:
  - quote: The UI screenshots below use a fictional Waypoint launch team and synthetic
      conversations, research notes, and metrics. The feature explainers are conceptual
      illustrations, not live status screens.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Setup can help you create a specialist or a small team, choose an avatar,
      and get connected. Installation and recovery guidance also covers more of the
      places where setup can get stuck.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Panes showing the same conversation share history recovery, and activity
      elsewhere avoids unnecessary redraws.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: 'Synthetic example: Short recaps connect the research, writing, and review
      across your team.'
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Teams replies preserve mention names containing escaped brackets or backslashes
      and correctly separate raw tables from code blocks in lists when table conversion
      is off. Votes submitted while older poll data is being imported are also preserved.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Teams searches and member lookups now use the conversation you select,
      with existing access and membership restrictions still enforced. Channel lists
      and details also accept valid Teams team IDs when Slack is enabled. Lists still
      require teamId , and channel details require both teamId and channelId .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: A failed Codex turn no longer has to strand an otherwise eligible conversation
      when its instructions change. OpenClaw can resume the same saved thread after
      confirming that the old process has exited. Recovery still refuses cases where
      replacement would disrupt active or protected siblings, client-bound sessions
      or supervised work. Separately, one startup timeout no longer interrupts healthy
      turns sharing the process, and Linux process checks avoid waiting behind unrelated
      filesystem work. A native startup that never settles can still block new starts
      in the same Codex home until that process exits.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Before downgrading to a version without this recovery support, disable
      the backend and finish pending cloud allocation or cleanup using the current
      version. The shared SSH backend also now requires native no-replace directory
      renaming to create or recreate workspaces. Existing workspaces remain usable
      without being reseeded.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: 'Conceptual illustration: One page. A shared point of view.'
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Choose groups carefully, since text and metadata may contain private information
      and revocation cannot recall what someone already received. Keep the source
      node connected and restart it after configuration changes. Reload an older open
      shared view after updating, and restore cold history on the source before reading
      it remotely.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: 'Conceptual illustration: Share the conversation. Not the controls.'
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: These uploads wait until OpenClaw has collected the full body before sending.
      Shared capacity limits or the five-minute deadline can refuse a transfer. Larger
      uploads and those without a known length still send in chunks, which some destinations
      reject.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The first source template and each checkout's dependencies still need preparation.
      ReFS sharing can take longer than ordinary Git checkout; set worktreeAcceleration
      to false to opt out. Btrfs sharing requires the optional native package; unavailable
      or disabled native helpers use ordinary Git and its normal space checks. APFS
      uses ordinary Git when inherited permissions cannot be preserved or checked,
      and cancelling an already-started native clone waits for it to finish.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Source profiles use ordinary Git checkout. Enabling them can also make
      later full worktrees use Git instead of accelerated sharing, even after expanding
      the source selection, so allow extra disk space.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 14-collaboration-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: collaboration
  title: 14 Collaboration changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-09-16-share-notes-md-now-writes-the-exported-session-to-your-home-directory-instead-of|--share=~/notes.md
  now writes the exported session to your home directory instead…]]'
- '[[Changes/Codex CLI/2026-09-17-44354-extract-shared-footer-hint-wrapping-in-the-tui-copyberry|♯44354
  Extract shared footer hint wrapping in the TUI @copyberry]]'
- '[[Changes/Claude Code/2026-09-18-changed-ultrareview-in-non-interactive-sessions-to-refuse-when-the-repository-ha|Changed
  /ultrareview in non-interactive sessions to refuse when the repository has…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: collaboration
title: 14 Collaboration changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Collaboration changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The UI screenshots below use a fictional Waypoint launch team and synthetic conversations, research notes, and metrics. The feature explainers are conceptual illustrations, not live status screens.

> Setup can help you create a specialist or a small team, choose an avatar, and get connected. Installation and recovery guidance also covers more of the places where setup can get stuck.

> Panes showing the same conversation share history recovery, and activity elsewhere avoids unnecessary redraws.

> Synthetic example: Short recaps connect the research, writing, and review across your team.

> Teams replies preserve mention names containing escaped brackets or backslashes and correctly separate raw tables from code blocks in lists when table conversion is off. Votes submitted while older poll data is being imported are also preserved.

> Teams searches and member lookups now use the conversation you select, with existing access and membership restrictions still enforced. Channel lists and details also accept valid Teams team IDs when Slack is enabled. Lists still require teamId , and channel details require both teamId and channelId .

> A failed Codex turn no longer has to strand an otherwise eligible conversation when its instructions change. OpenClaw can resume the same saved thread after confirming that the old process has exited. Recovery still refuses cases where replacement would disrupt active or protected siblings, client-bound sessions or supervised work. Separately, one startup timeout no longer interrupts healthy turns sharing the process, and Linux process checks avoid waiting behind unrelated filesystem work. A native startup that never settles can still block new starts in the same Codex home until that process exits.

> Before downgrading to a version without this recovery support, disable the backend and finish pending cloud allocation or cleanup using the current version. The shared SSH backend also now requires native no-replace directory renaming to create or recreate workspaces. Existing workspaces remain usable without being reseeded.

> Conceptual illustration: One page. A shared point of view.

> Choose groups carefully, since text and metadata may contain private information and revocation cannot recall what someone already received. Keep the source node connected and restart it after configuration changes. Reload an older open shared view after updating, and restore cold history on the source before reading it remotely.

> Conceptual illustration: Share the conversation. Not the controls.

> These uploads wait until OpenClaw has collected the full body before sending. Shared capacity limits or the five-minute deadline can refuse a transfer. Larger uploads and those without a known length still send in chunks, which some destinations reject.

> The first source template and each checkout's dependencies still need preparation. ReFS sharing can take longer than ordinary Git checkout; set worktreeAcceleration to false to opt out. Btrfs sharing requires the optional native package; unavailable or disabled native helpers use ordinary Git and its normal space checks. APFS uses ordinary Git when inherited permissions cannot be preserved or checked, and cancelling an already-started native clone waits for it to finish.

> Source profiles use ordinary Git checkout. Enabling them can also make later full worktrees use Git instead of accelerated sharing, even after expanding the source selection, so allow extra disk space.

Source: https://docs.openclaw.ai/releases/2026.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-19-20-context-window-changes-in-v2026-9-5|20 Context Window changes in v2026.9.5]] · Context Window
- [[Changes/OpenClaw/2026-09-19-the-browser-sidebar-gains-a-download-file-button-for-the-image-video-or-document|The Browser sidebar gains a Download file button for the image, video, or document…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-19-29-developer-workflow-changes-in-v2026-9-5|29 Developer Workflow changes in v2026.9.5]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-19-5-reliability-and-performance-changes-in-v2026-9-5|5 Reliability and Performance changes in v2026.9.5]] · Reliability and Performance
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
## Nearby in Collaboration

- Earlier: 2026-09-18 · Claude Code · [[Changes/Claude Code/2026-09-18-changed-ultrareview-in-non-interactive-sessions-to-refuse-when-the-repository-ha|Changed /ultrareview in non-interactive sessions to refuse when the repository has…]]
- Later: 2026-09-21 · Open WebUI · [[Changes/Open WebUI/2026-09-21-4-collaboration-changes-in-v0-11-4|4 Collaboration changes in v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-24 · ChatGPT · [[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-0440ac&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-14-collaboration-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-0440ac%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->