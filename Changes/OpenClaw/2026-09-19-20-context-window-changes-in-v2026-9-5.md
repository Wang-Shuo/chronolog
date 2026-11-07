---
card_id: openclaw-2026-09-19-025c61
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Context Window: 20 changes in v2026.9.5 — In
  shared sessions, each person’s live draft now appears in a softer chat bubble labeled…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2558
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3c5423b2dcb280d7c33b0350626b746d8f4efc967f0ad959e0ea505bdc4a98cb
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-025c61
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 20 Context Window changes'
  evidence:
  - quote: In shared sessions, each person’s live draft now appears in a softer chat
      bubble labeled Typing · not sent , or as their own typing dots. These temporary
      previews disappear after inactivity or sending. They are not saved in the conversation
      or included in model context.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: 'Synthetic example: Review a launch draft in context, without losing the
      conversation.'
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: If an interactive update fails, AI repair starts only after you choose
      Yes, because it uses your account and tokens. Enter, No, cancellation, or a
      30-second timeout skips repair and leaves diagnostics and manual recovery instructions
      . An older updater already running may still use its old prompt.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Typed commands retain replied-to photos, quotes, and topic context and
      now run in the chat session. Codex-backed credential requests also deliver their
      protected form links again, including in side questions. Enter the credential
      in the masked Control UI form, not in Telegram. Messages interrupted by shutdown
      before the agent takes ownership return to the queue for restart recovery; already-adopted
      turns are not replayed, avoiding repeated tool work.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Mattermost keeps a thread's original participation expiry after a restart,
      so an expired conversation requires a mention again. It can also recover permitted
      recent thread context after a restart or reset, including DMs with threading
      enabled. Recovery respects historyLimit , reads at most one 200-post page per
      attempt, and has a five-second deadline. A reset can therefore be followed by
      earlier server-held messages returning as context; flat DMs are unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Regular chat still needs a separately selected primary model. Apple's smaller
      context and output quality limit its suitability for long prompts and complex
      tasks. Model Setup offers Recheck & repair if the helper is missing. Before
      upgrading, keep a verified archive of your current installation state. Returning
      to the older package requires restoring that archive; downgrading the package
      alone is insufficient.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Codex previews keep their opening text, and completed reasoning remains
      visible even when it did not arrive piece by piece. Asynchronous messages stay
      separate from the final answer instead of being repeated there. Native conversation
      history also carries recorded speaker identities through compaction, helping
      preserve who said what; missing historical identities are not guessed.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Copilot saves the connection between your OpenClaw conversation and its
      native session without blocking the host's main processing thread. Reset and
      shutdown wait for pending saves and cleanup, and a late compaction result no
      longer removes a different replacement session.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: If you downgrade, older OpenClaw versions can discard saved model-budget
      information during recovery, leaving context engines to use their fallback limits.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Budget-triggered compaction on public OpenAI Responses now uses its compact
      endpoint by default. Set params.responsesCompactEndpoint to false to opt out.
      Manual compaction keeps its previous default, and confirmed overflow or endpoint
      failure uses client-side recovery. This new default does not extend to ChatGPT,
      Azure or custom Responses endpoints. See compaction for the available controls.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Restored Codex screenshots now stay beside their original messages instead
      of appearing attached to a later request. If a whole historical message no longer
      fits in the model's context, its images are left out of that request but remain
      saved.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Multi-agent conversations hide raw worker reports and automatic coordination
      replies while keeping useful parent answers and task results visible. Child
      reports no longer start reciprocal reply loops, and a requested late result
      can produce one visible parent answer. Human follow-ups still get their own
      visible replies. Coordination remains in raw transcripts and model context,
      and older messages without enough sender information remain visible. This display
      behavior is separate from opting into private parent review before an announcement.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Managed Codex conversations can continue with changed tools, carrying completed
      results and accepted follow-up input within bounded conversation context. This
      stops the current native turn and background terminals. Imported or supervised
      Codex sessions need a new managed conversation for changed tools.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Workboard card details now organize task information, activity and recent
      session context into tabs, with common fields editable in place. You can also
      rename a board and choose or reset its icon and color. Closing changed cards
      or comments asks before discarding your draft, and failed saves keep your edits
      available. Dragging cards preserves neighboring status changes, while attachments
      on a recreated card survive cleanup of its predecessor.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Stopping a reply now keeps an established coding-app conversation available
      with its earlier context for the next turn. The partial reply stays visible,
      and the interrupted turn remains unsuccessful, so you can continue without treating
      unfinished work as complete.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Messaging topic changes and sends follow the configured cross-context rules,
      including when the source service is known but its conversation address is missing.
      Omitted cross-provider settings now permit otherwise allowed actions across
      services. Set tools.message.crossContext.allowAcrossProviders=false to preserve
      service isolation, and set allowWithinProvider=false as well to keep a bound
      conversation within its current chat. Pending sends stop before new provider
      requests after their caller closes, including Discord queue retries. Rejected
      unsent messages stay out of recovery once that rejection is saved; already dispatched
      messages cannot be recalled.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Side chat questions and cached answers now follow current conversation
      visibility, including private drafts in deployments with Gateway roles. Access
      is checked again before later embedded model requests, including requests delayed
      by credential or media preparation. Revoking access can stop the next request,
      but cannot retract context already sent to a provider.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: History pages with a byte limit and context preparation for large messages
      also do less unnecessary work. Small, empty, and full-page reads can still take
      longer.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Ordinary subagents can use completed tool results before pausing. When
      they resume and finish, the parent conversation can continue with their complete
      retained answers. Larger answers use more of the parent's context, and results
      removed by retention fall back to a marked, shortened copy. Later parent turns
      can find retained child results still awaiting delivery or continuation. A child
      you explicitly stop stays cancelled. If the parent finishes its work but misses
      a required channel reply, the result stays blocked for explicit retry or dismissal
      instead of automatically repeating its tools. Check completed actions before
      retrying.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Regression tests have less repeated setup and more coverage of the code
      that runs in production, including resource ownership during queued conversation
      compaction.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 20-context-window-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: context-window
  title: 20 Context Window changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Cline/2026-09-17-long-tasks-now-compact-when-they-actually-need-to-rather-than-running-out-of-roo|Long
  tasks now compact when they actually need to rather than running out of room]]'
- '[[Changes/Codex CLI/2026-09-17-20-context-window-changes-in-rust-v0-155-0|20 Context
  Window changes in rust-v0.155.0]]'
- '[[Changes/Lovable/2026-09-18-type-or-to-add-context-and-skills-where-you-type|Type
  @ or / to add context and skills where you type]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: context-window
title: 20 Context Window changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Context Window changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> In shared sessions, each person’s live draft now appears in a softer chat bubble labeled Typing · not sent , or as their own typing dots. These temporary previews disappear after inactivity or sending. They are not saved in the conversation or included in model context.

> Synthetic example: Review a launch draft in context, without losing the conversation.

> If an interactive update fails, AI repair starts only after you choose Yes, because it uses your account and tokens. Enter, No, cancellation, or a 30-second timeout skips repair and leaves diagnostics and manual recovery instructions . An older updater already running may still use its old prompt.

> Typed commands retain replied-to photos, quotes, and topic context and now run in the chat session. Codex-backed credential requests also deliver their protected form links again, including in side questions. Enter the credential in the masked Control UI form, not in Telegram. Messages interrupted by shutdown before the agent takes ownership return to the queue for restart recovery; already-adopted turns are not replayed, avoiding repeated tool work.

> Mattermost keeps a thread's original participation expiry after a restart, so an expired conversation requires a mention again. It can also recover permitted recent thread context after a restart or reset, including DMs with threading enabled. Recovery respects historyLimit , reads at most one 200-post page per attempt, and has a five-second deadline. A reset can therefore be followed by earlier server-held messages returning as context; flat DMs are unchanged.

> Regular chat still needs a separately selected primary model. Apple's smaller context and output quality limit its suitability for long prompts and complex tasks. Model Setup offers Recheck & repair if the helper is missing. Before upgrading, keep a verified archive of your current installation state. Returning to the older package requires restoring that archive; downgrading the package alone is insufficient.

> Codex previews keep their opening text, and completed reasoning remains visible even when it did not arrive piece by piece. Asynchronous messages stay separate from the final answer instead of being repeated there. Native conversation history also carries recorded speaker identities through compaction, helping preserve who said what; missing historical identities are not guessed.

> Copilot saves the connection between your OpenClaw conversation and its native session without blocking the host's main processing thread. Reset and shutdown wait for pending saves and cleanup, and a late compaction result no longer removes a different replacement session.

> If you downgrade, older OpenClaw versions can discard saved model-budget information during recovery, leaving context engines to use their fallback limits.

> Budget-triggered compaction on public OpenAI Responses now uses its compact endpoint by default. Set params.responsesCompactEndpoint to false to opt out. Manual compaction keeps its previous default, and confirmed overflow or endpoint failure uses client-side recovery. This new default does not extend to ChatGPT, Azure or custom Responses endpoints. See compaction for the available controls.

> Restored Codex screenshots now stay beside their original messages instead of appearing attached to a later request. If a whole historical message no longer fits in the model's context, its images are left out of that request but remain saved.

> Multi-agent conversations hide raw worker reports and automatic coordination replies while keeping useful parent answers and task results visible. Child reports no longer start reciprocal reply loops, and a requested late result can produce one visible parent answer. Human follow-ups still get their own visible replies. Coordination remains in raw transcripts and model context, and older messages without enough sender information remain visible. This display behavior is separate from opting into private parent review before an announcement.

> Managed Codex conversations can continue with changed tools, carrying completed results and accepted follow-up input within bounded conversation context. This stops the current native turn and background terminals. Imported or supervised Codex sessions need a new managed conversation for changed tools.

> Workboard card details now organize task information, activity and recent session context into tabs, with common fields editable in place. You can also rename a board and choose or reset its icon and color. Closing changed cards or comments asks before discarding your draft, and failed saves keep your edits available. Dragging cards preserves neighboring status changes, while attachments on a recreated card survive cleanup of its predecessor.

> Stopping a reply now keeps an established coding-app conversation available with its earlier context for the next turn. The partial reply stays visible, and the interrupted turn remains unsuccessful, so you can continue without treating unfinished work as complete.

> Messaging topic changes and sends follow the configured cross-context rules, including when the source service is known but its conversation address is missing. Omitted cross-provider settings now permit otherwise allowed actions across services. Set tools.message.crossContext.allowAcrossProviders=false to preserve service isolation, and set allowWithinProvider=false as well to keep a bound conversation within its current chat. Pending sends stop before new provider requests after their caller closes, including Discord queue retries. Rejected unsent messages stay out of recovery once that rejection is saved; already dispatched messages cannot be recalled.

> Side chat questions and cached answers now follow current conversation visibility, including private drafts in deployments with Gateway roles. Access is checked again before later embedded model requests, including requests delayed by credential or media preparation. Revoking access can stop the next request, but cannot retract context already sent to a provider.

> History pages with a byte limit and context preparation for large messages also do less unnecessary work. Small, empty, and full-page reads can still take longer.

> Ordinary subagents can use completed tool results before pausing. When they resume and finish, the parent conversation can continue with their complete retained answers. Larger answers use more of the parent's context, and results removed by retention fall back to a marked, shortened copy. Later parent turns can find retained child results still awaiting delivery or continuation. A child you explicitly stop stays cancelled. If the parent finishes its work but misses a required channel reply, the result stays blocked for explicit retry or dismissal instead of automatically repeating its tools. Check completed actions before retrying.

> Regression tests have less repeated setup and more coverage of the code that runs in production, including resource ownership during queued conversation compaction.

Source: https://docs.openclaw.ai/releases/2026.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

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
## Nearby in Context Window

- Earlier: 2026-09-18 · Lovable · [[Changes/Lovable/2026-09-18-type-or-to-add-context-and-skills-where-you-type|Type @ or / to add context and skills where you type]]
- Later: 2026-09-21 · Open WebUI · [[Changes/Open WebUI/2026-09-21-3-context-window-changes-in-v0-11-4|3 Context Window changes in v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-025c61&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-20-context-window-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-025c61%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->