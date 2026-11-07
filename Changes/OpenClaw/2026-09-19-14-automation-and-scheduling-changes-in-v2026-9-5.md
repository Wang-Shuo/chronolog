---
card_id: openclaw-2026-09-19-480f80
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Automation and Scheduling: 14 changes in v2026.9.5
  — The existing openclaw setup-and-repair helper is now discoverable in the tool…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change
    gain, with volume automation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2558
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1a6ae7cb8716b69ef180ad9f900a060226d56c305a11f26257d48333b83563ec
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-480f80
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 14 Automation and Scheduling changes'
  evidence:
  - quote: The existing openclaw setup-and-repair helper is now discoverable in the
      tool list. It also belongs to group:automation and group:openclaw , so denying
      either group blocks the helper even if you explicitly allow it. To use it, narrow
      or remove a conflicting group deny. Restricted profiles still need an explicit
      selection through tools.alsoAllow , subject to the remaining restrictions.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Read-only viewers can read cached recaps without requesting model work.
      Incognito, subagent, and scheduled-job sessions are excluded. Scheduled jobs
      keep their scheduler-owned summaries.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: When an update launched inside a supported managed Gateway service hands
      work to a background helper, the initiating command now exits with 75 . This
      means accepted and still in progress. Automation must check openclaw update
      status --json or openclaw update history --json , then follow the printed health
      guidance before treating the update as complete. Do not retry merely because
      this acknowledgment is nonzero; other nonzero exits remain failures. An older
      updater performing the first upgrade keeps its existing exit behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: In Workshop auto mode, weekly reviews now pause visibly when every configured
      runtime is known to lack support for keeping the review inside the Workshop
      directory. Inspect paused jobs with openclaw cron list --all --json , configure
      a supported runtime or fallback, then reload configuration or restart the Gateway.
      The same jobs become enabled again with their history intact.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: This does not add Codex support for these reviews or a separate review-only
      runtime selector. An enabled job still has to pass the checks when it runs,
      and automatic reviews still require cron to be enabled.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Automation can close an OpenClaw window without crashing the app or its
      other windows. Update or rebuild OpenClaw.app to receive this fix; updating
      the Peekaboo CLI alone is insufficient. Native plugin panels such as Workboard
      can load their stylesheets over a direct local HTTP connection. Cookies still
      share a hostname across ports, so do not put mutually untrusted services on
      that same hostname.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: After a plugin reload, script automations can refresh stale tools once
      before starting. Repeated failures stay grouped, and confirmed successful completion
      sends a recovery notice. Setup recovery never replays a script or tool action
      that has already started.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Before downgrading, let affected edited runs finish and let the scheduler
      finish reconciling their results on the current version. A completed task alone
      is not enough to preserve those edits when returning to an older version. Stream
      sources stopped by matching overload or timeout need you to check the expression
      or server load and explicitly re-enable them; disabling or changing an exit
      watch cancels its pending exit.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Administrator tasks can keep managing existing automations after waiting
      for subagents, without another user message. That access belongs only to the
      exact resumed task and covers management of existing jobs. Cancellation, a session
      reset or archive, a new direct user turn, or a Gateway restart ends the handoff.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Click Automation attached in a session hovercard to open its automation
      editor. If several automations match, you get a list filtered to that session,
      with Show all automations to return to the full list. Your existing viewing
      and editing permissions still apply. In the CLI, an ambiguous job name now shows
      matching jobs so you can retry by ID; scripts using duplicate names must use
      an ID too.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Choose View transcript in Tasks or automation run history to read the specific
      completed run, even after its temporary session has been cleaned up. The CLI
      also makes it easier to investigate a run, with searchable, paged history and
      separate filters for execution and delivery results. Transcript access still
      depends on retained history and your permissions. Existing text-block limits
      remain, so this does not recover deleted history or text that was omitted from
      the stored view.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Explicitly configured owners can now manage existing automations across
      sessions directly from chat. Eligibility comes from individual entries in commands.ownerAllowFrom
      , not channel allowlists or wildcards, and management does not transfer the
      creator's execution permissions. If Doctor can identify who created an older
      automation, openclaw doctor --fix restores their ability to edit its prompt
      without changing tool permissions. Jobs stop before execution when a required
      creator account is unavailable. Restore that account or recreate the automation
      under the intended account; changing its delivery account does not transfer
      ownership. A missing execution agent also leaves a reason in run history.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Doctor also warns when some automatically captured tool lists may be missing
      file, command or web capabilities. The restrictions may be intentional, so even
      --fix leaves them unchanged. To add tools, an authorized session must review
      and replace the complete list, including every tool the job should keep. Agents
      are instructed to ask an authorized administrator to check a known automation
      after a restricted lookup fails, before creating a replacement.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: If Chrome loses a tab's internal automation target, the extension relay
      can restore control for clients that remain subscribed, provided the tab is
      still accessible. Take a fresh snapshot before continuing; failed actions are
      not replayed. Explicit detach and Chrome's Cancel still stop control.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 14-automation-and-scheduling-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: automation-scheduling
  title: 14 Automation and Scheduling changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Descript/2026-09-17-record-in-a-scheduled-room-without-the-host|Record
  in a scheduled Room without the host]]'
- '[[Changes/Lovable/2026-09-17-automate-your-workspace-with-the-lovable-api|Automate
  your workspace with the Lovable API]]'
- '[[Changes/OpenHands/2026-09-17-feat-automations-select-saved-agent-profiles-by-neubig-in-https-github-com-openh|feat(automations):
  select saved agent profiles]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: automation-scheduling
title: 14 Automation and Scheduling changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Automation and Scheduling changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The existing openclaw setup-and-repair helper is now discoverable in the tool list. It also belongs to group:automation and group:openclaw , so denying either group blocks the helper even if you explicitly allow it. To use it, narrow or remove a conflicting group deny. Restricted profiles still need an explicit selection through tools.alsoAllow , subject to the remaining restrictions.

> Read-only viewers can read cached recaps without requesting model work. Incognito, subagent, and scheduled-job sessions are excluded. Scheduled jobs keep their scheduler-owned summaries.

> When an update launched inside a supported managed Gateway service hands work to a background helper, the initiating command now exits with 75 . This means accepted and still in progress. Automation must check openclaw update status --json or openclaw update history --json , then follow the printed health guidance before treating the update as complete. Do not retry merely because this acknowledgment is nonzero; other nonzero exits remain failures. An older updater performing the first upgrade keeps its existing exit behavior.

> In Workshop auto mode, weekly reviews now pause visibly when every configured runtime is known to lack support for keeping the review inside the Workshop directory. Inspect paused jobs with openclaw cron list --all --json , configure a supported runtime or fallback, then reload configuration or restart the Gateway. The same jobs become enabled again with their history intact.

> This does not add Codex support for these reviews or a separate review-only runtime selector. An enabled job still has to pass the checks when it runs, and automatic reviews still require cron to be enabled.

> Automation can close an OpenClaw window without crashing the app or its other windows. Update or rebuild OpenClaw.app to receive this fix; updating the Peekaboo CLI alone is insufficient. Native plugin panels such as Workboard can load their stylesheets over a direct local HTTP connection. Cookies still share a hostname across ports, so do not put mutually untrusted services on that same hostname.

> After a plugin reload, script automations can refresh stale tools once before starting. Repeated failures stay grouped, and confirmed successful completion sends a recovery notice. Setup recovery never replays a script or tool action that has already started.

> Before downgrading, let affected edited runs finish and let the scheduler finish reconciling their results on the current version. A completed task alone is not enough to preserve those edits when returning to an older version. Stream sources stopped by matching overload or timeout need you to check the expression or server load and explicitly re-enable them; disabling or changing an exit watch cancels its pending exit.

> Administrator tasks can keep managing existing automations after waiting for subagents, without another user message. That access belongs only to the exact resumed task and covers management of existing jobs. Cancellation, a session reset or archive, a new direct user turn, or a Gateway restart ends the handoff.

> Click Automation attached in a session hovercard to open its automation editor. If several automations match, you get a list filtered to that session, with Show all automations to return to the full list. Your existing viewing and editing permissions still apply. In the CLI, an ambiguous job name now shows matching jobs so you can retry by ID; scripts using duplicate names must use an ID too.

> Choose View transcript in Tasks or automation run history to read the specific completed run, even after its temporary session has been cleaned up. The CLI also makes it easier to investigate a run, with searchable, paged history and separate filters for execution and delivery results. Transcript access still depends on retained history and your permissions. Existing text-block limits remain, so this does not recover deleted history or text that was omitted from the stored view.

> Explicitly configured owners can now manage existing automations across sessions directly from chat. Eligibility comes from individual entries in commands.ownerAllowFrom , not channel allowlists or wildcards, and management does not transfer the creator's execution permissions. If Doctor can identify who created an older automation, openclaw doctor --fix restores their ability to edit its prompt without changing tool permissions. Jobs stop before execution when a required creator account is unavailable. Restore that account or recreate the automation under the intended account; changing its delivery account does not transfer ownership. A missing execution agent also leaves a reason in run history.

> Doctor also warns when some automatically captured tool lists may be missing file, command or web capabilities. The restrictions may be intentional, so even --fix leaves them unchanged. To add tools, an authorized session must review and replace the complete list, including every tool the job should keep. Agents are instructed to ask an authorized administrator to check a known automation after a restricted lookup fails, before creating a replacement.

> If Chrome loses a tab's internal automation target, the extension relay can restore control for clients that remain subscribed, provided the tab is still accessible. Take a fresh snapshot before continuing; failed actions are not replayed. Explicit detach and Chrome's Cancel still stop control.

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
- [[Changes/OpenClaw/2026-09-19-21-editor-experience-changes-in-v2026-9-5|21 Editor Experience changes in v2026.9.5]] · Editor Experience
- [[Changes/OpenClaw/2026-09-19-28-model-support-changes-in-v2026-9-5|28 Model Support changes in v2026.9.5]] · Model Support
- [[Changes/OpenClaw/2026-09-19-39-safety-and-privacy-changes-in-v2026-9-5|39 Safety and Privacy changes in v2026.9.5]] · Safety and Privacy
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
## Nearby in Automation and Scheduling

- Earlier: 2026-09-17 · OpenHands · [[Changes/OpenHands/2026-09-17-feat-automations-select-saved-agent-profiles-by-neubig-in-https-github-com-openh|feat(automations): select saved agent profiles]]
- Later: 2026-09-21 · Devin · [[Changes/Devin/2026-09-21-simpler-create-automation-menu|Simpler Create Automation Menu]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-480f80&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-14-automation-and-scheduling-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-480f80%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->