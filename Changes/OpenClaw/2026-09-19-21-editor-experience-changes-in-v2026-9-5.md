---
card_id: openclaw-2026-09-19-3874f4
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Editor Experience: 21 changes in v2026.9.5 —
  The browser-tab icon now shows when the selected agent is working, needs an answer
  or…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2869
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 10262d77bf4649bfab37b7eaa3178f2dc32bb613bba2316052d2562ee58be74b
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-3874f4
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 21 Editor Experience changes'
  evidence:
  - quote: The browser-tab icon now shows when the selected agent is working, needs
      an answer or approval, has finished while you were away, or has disconnected.
      The completion indicator clears when you return to the tab. Failed or interrupted
      runs do not appear as completed work.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Discard removes the local pending copy; it cannot cancel a message OpenClaw
      has already received. Most commands still need the conversation to finish loading.
      If saving a queued correction fails because of browser storage, keep the tab
      open and copy the affected text before freeing storage. For saved drafts that
      fail to load, reload without clearing site data, after copying any unsaved correction;
      clearing site data would delete local drafts.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Unfinished queued-message corrections survive switching conversations and
      block automatic update reloads until you save or cancel them. An explicit browser
      reload still discards those corrections. Incognito New Session drafts survive
      destination changes and Back within the same tab, but disappear on reload or
      closure; turning Incognito off resumes ordinary autosave for the existing draft.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: 'In Chat and New Session, type an emoji name such as :smi to see suggestions,
      then choose one with the arrow keys and Enter, Tab, or a click. Completing a
      recognized shortcode such as :smile: also inserts its emoji. This edits the
      draft without sending it, while code, URLs, and unknown names stay literal.'
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Mentions leaves more room for the entries you came to read. Notification
      settings now sit in the shared Inbox header, so you can reach them from any
      Inbox tab.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Reopen a file from chat, a tool card, or the Files list to refresh its
      saved contents in the existing tab. Simply selecting its tab keeps the current
      preview. Unsaved edits and newer saves stay protected from delayed reads, including
      when you switch sessions or connections.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Partial-clone Git updates can work with intentionally omitted historical
      objects while still requiring the complete files for the proposed version. If
      transfer fails, the error distinguishes missing-object recovery guidance from
      verified corruption. Local edits still stop an update before installation or
      service shutdown, now with a failure result and instructions to commit the changes
      and retry or use triage.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Package updates save supported local edits for recovery, and --reapply-local-overrides
      lets you explicitly replay trusted changes against matching original files.
      Fresh-profile updates now honor that choice too. Back up your edits and data
      before the first upgrade from an older updater. Recovery bundles are separate
      from data backups, remain on disk until you remove them, and keep conflicting
      changes available for manual recovery.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: After a stale write is rejected, choose Reload to retrieve current settings,
      then explicitly retry your change. The rejected write preserves external edits;
      reloading does not automatically replay it.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: With the corrected updater, a qualifying slow-starting Gateway can remain
      running after readiness checks expire, with its backups retained. The result
      stays gateway-readiness-unverified , not completed success or a promise to finish
      in the background. Keep the backups and check openclaw gateway status --deep
      . An already-running 2026.9.3 or 2026.9.4 updater keeps its older completion
      behavior and can still disable Windows autostart after this unverified result.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Temporary save failures no longer immediately discard completed Codex or
      Copilot child-task results. Codex retries saving results and delivery status
      without repeating an announcement just because its status write failed. Copilot
      retains the original outcome for a later event or cleanup to retry. Pending
      unsaved outcomes still depend on that OpenClaw process staying alive.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Scheduled work keeps your latest edits and gives you clearer ways to follow
      what ran, what failed, and what needs attention. You can also see whether delegated
      work is running, waiting or finished, and whether its result has returned.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Changes you save to a running schedule or watcher now survive completion
      and crash recovery. Manual runs report that they are queued only after the queue
      accepts them. That acknowledgement means the run was accepted, not that it has
      finished; use its run ID to check the outcome.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The explicit sessions_send mode resume can continue an eligible paused
      native child while preserving its original task and completion recipient. It
      requires current authority over that child and returns acceptance, not the final
      answer. Omit watch and use no positive wait timeout. Ordinary follow-up messages
      keep their existing behavior, and previously stranded tasks are not automatically
      repaired.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Scheduled jobs wait for delegated work and its result delivery before choosing
      a final response, within their existing deadline. Repeated wait checks now leave
      time to process completion. Managed Lobster approval flows can also resume from
      a saved checkpoint with the flow ID, current revision, owning session and the
      user's decision.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: After a rapid hide/show of the embedded Desktop, a later disconnect keeps
      its reason and Reconnect control visible. Repeated Stop requests on paired desktops
      now wait for cleanup already underway. Cloud Desktop shutdown cancels queued
      app launches and waits for its local work, including work from a replaced worker.
      Local cleanup completion does not confirm that the cloud provider has released
      the machine.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Browser access is required. Remote profiles, paired-node browsers, and
      attached personal browsers are unsupported, and the page does not use your phone
      or laptop's cookies. Stop closes the tab and loses unsaved page state. Resume
      opens the saved URL.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Reference saves wait for acknowledgment. Canceling a rejected edit preserves
      other changes, but a lost acknowledgment can leave the draft and error visible
      until you reload. Saving a reference does not rotate the secret or verify the
      provider connection.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Bash completion stops suggesting options after -- . If you use a cached
      completion script, refresh it with openclaw completion --shell bash --write-state
      and reload your shell.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Large ignored dependency folders and untracked directory trees no longer
      cause the filename-buffer overflow that prevented eligible cleanup; local edits
      and untracked child files remain restorable. A directory replacing a deleted
      file in a merge conflict can also be saved and restored, though the conflict
      itself still needs resolution. Existing retention rules and protection for nested
      repositories remain in place.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: In the Control UI, choosing Goal with Tab, Enter, or a click opens the
      existing objective form , as does submitting /goal or an empty /goal start ,
      /goal set , or /goal create command. Slashes and spacing in the objective stay
      literal. Empty objectives cannot be sent, and a rejected submission keeps your
      draft. Complete and management commands still work as text commands.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 21-editor-experience-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: editor-experience
  title: 21 Editor Experience changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Descript/2026-09-17-a-heads-up-about-grammarly|A heads-up about Grammarly]]'
- '[[Changes/GitHub Copilot CLI/2026-09-17-2-editor-experience-changes-in-v1-0-86|2
  Editor Experience changes in v1.0.86]]'
- '[[Changes/Claude Code/2026-09-18-2-editor-experience-changes-in-v2-1-277|2 Editor
  Experience changes in v2.1.277]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: editor-experience
title: 21 Editor Experience changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 21 Editor Experience changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The browser-tab icon now shows when the selected agent is working, needs an answer or approval, has finished while you were away, or has disconnected. The completion indicator clears when you return to the tab. Failed or interrupted runs do not appear as completed work.

> Discard removes the local pending copy; it cannot cancel a message OpenClaw has already received. Most commands still need the conversation to finish loading. If saving a queued correction fails because of browser storage, keep the tab open and copy the affected text before freeing storage. For saved drafts that fail to load, reload without clearing site data, after copying any unsaved correction; clearing site data would delete local drafts.

> Unfinished queued-message corrections survive switching conversations and block automatic update reloads until you save or cancel them. An explicit browser reload still discards those corrections. Incognito New Session drafts survive destination changes and Back within the same tab, but disappear on reload or closure; turning Incognito off resumes ordinary autosave for the existing draft.

> In Chat and New Session, type an emoji name such as :smi to see suggestions, then choose one with the arrow keys and Enter, Tab, or a click. Completing a recognized shortcode such as :smile: also inserts its emoji. This edits the draft without sending it, while code, URLs, and unknown names stay literal.

> Mentions leaves more room for the entries you came to read. Notification settings now sit in the shared Inbox header, so you can reach them from any Inbox tab.

> Reopen a file from chat, a tool card, or the Files list to refresh its saved contents in the existing tab. Simply selecting its tab keeps the current preview. Unsaved edits and newer saves stay protected from delayed reads, including when you switch sessions or connections.

> Partial-clone Git updates can work with intentionally omitted historical objects while still requiring the complete files for the proposed version. If transfer fails, the error distinguishes missing-object recovery guidance from verified corruption. Local edits still stop an update before installation or service shutdown, now with a failure result and instructions to commit the changes and retry or use triage.

> Package updates save supported local edits for recovery, and --reapply-local-overrides lets you explicitly replay trusted changes against matching original files. Fresh-profile updates now honor that choice too. Back up your edits and data before the first upgrade from an older updater. Recovery bundles are separate from data backups, remain on disk until you remove them, and keep conflicting changes available for manual recovery.

> After a stale write is rejected, choose Reload to retrieve current settings, then explicitly retry your change. The rejected write preserves external edits; reloading does not automatically replay it.

> With the corrected updater, a qualifying slow-starting Gateway can remain running after readiness checks expire, with its backups retained. The result stays gateway-readiness-unverified , not completed success or a promise to finish in the background. Keep the backups and check openclaw gateway status --deep . An already-running 2026.9.3 or 2026.9.4 updater keeps its older completion behavior and can still disable Windows autostart after this unverified result.

> Temporary save failures no longer immediately discard completed Codex or Copilot child-task results. Codex retries saving results and delivery status without repeating an announcement just because its status write failed. Copilot retains the original outcome for a later event or cleanup to retry. Pending unsaved outcomes still depend on that OpenClaw process staying alive.

> Scheduled work keeps your latest edits and gives you clearer ways to follow what ran, what failed, and what needs attention. You can also see whether delegated work is running, waiting or finished, and whether its result has returned.

> Changes you save to a running schedule or watcher now survive completion and crash recovery. Manual runs report that they are queued only after the queue accepts them. That acknowledgement means the run was accepted, not that it has finished; use its run ID to check the outcome.

> The explicit sessions_send mode resume can continue an eligible paused native child while preserving its original task and completion recipient. It requires current authority over that child and returns acceptance, not the final answer. Omit watch and use no positive wait timeout. Ordinary follow-up messages keep their existing behavior, and previously stranded tasks are not automatically repaired.

> Scheduled jobs wait for delegated work and its result delivery before choosing a final response, within their existing deadline. Repeated wait checks now leave time to process completion. Managed Lobster approval flows can also resume from a saved checkpoint with the flow ID, current revision, owning session and the user's decision.

> After a rapid hide/show of the embedded Desktop, a later disconnect keeps its reason and Reconnect control visible. Repeated Stop requests on paired desktops now wait for cleanup already underway. Cloud Desktop shutdown cancels queued app launches and waits for its local work, including work from a replaced worker. Local cleanup completion does not confirm that the cloud provider has released the machine.

> Browser access is required. Remote profiles, paired-node browsers, and attached personal browsers are unsupported, and the page does not use your phone or laptop's cookies. Stop closes the tab and loses unsaved page state. Resume opens the saved URL.

> Reference saves wait for acknowledgment. Canceling a rejected edit preserves other changes, but a lost acknowledgment can leave the draft and error visible until you reload. Saving a reference does not rotate the secret or verify the provider connection.

> Bash completion stops suggesting options after -- . If you use a cached completion script, refresh it with openclaw completion --shell bash --write-state and reload your shell.

> Large ignored dependency folders and untracked directory trees no longer cause the filename-buffer overflow that prevented eligible cleanup; local edits and untracked child files remain restorable. A directory replacing a deleted file in a merge conflict can also be saved and restored, though the conflict itself still needs resolution. Existing retention rules and protection for nested repositories remain in place.

> In the Control UI, choosing Goal with Tab, Enter, or a click opens the existing objective form , as does submitting /goal or an empty /goal start , /goal set , or /goal create command. Slashes and spacing in the objective stay literal. Empty objectives cannot be sent, and a rejected submission keeps your draft. Complete and management commands still work as text commands.

Source: https://docs.openclaw.ai/releases/2026.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-19-20-context-window-changes-in-v2026-9-5|20 Context Window changes in v2026.9.5]] · Context Window
- [[Changes/OpenClaw/2026-09-19-14-collaboration-changes-in-v2026-9-5|14 Collaboration changes in v2026.9.5]] · Collaboration
- [[Changes/OpenClaw/2026-09-19-the-browser-sidebar-gains-a-download-file-button-for-the-image-video-or-document|The Browser sidebar gains a Download file button for the image, video, or document…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-19-29-developer-workflow-changes-in-v2026-9-5|29 Developer Workflow changes in v2026.9.5]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-19-5-reliability-and-performance-changes-in-v2026-9-5|5 Reliability and Performance changes in v2026.9.5]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-19-retained-conversation-history-continues-to-follow-current-sharing-permissions-af|Retained conversation history continues to follow current sharing permissions after…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-19-2-enterprise-and-administration-changes-in-v2026-9-5|2 Enterprise and Administration changes in v2026.9.5]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-19-72-agent-mode-changes-in-v2026-9-5|72 Agent Mode changes in v2026.9.5]] · Agent Mode
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
## Nearby in Editor Experience

- Earlier: 2026-09-18 · Claude Code · [[Changes/Claude Code/2026-09-18-2-editor-experience-changes-in-v2-1-277|2 Editor Experience changes in v2.1.277]]
- Later: 2026-09-20 · Lovable · [[Changes/Lovable/2026-09-20-organize-project-files-into-collections|Organize project files into collections]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-3874f4&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-21-editor-experience-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-3874f4%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->