---
card_id: openclaw-2026-09-23-eb35f0
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Interface Experience: 19 changes in v2026.9.6
  — Conversations can be archived or restored directly from the sidebar with Undo,
  and…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2719
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e3dea9c3906502986390870297645ee7f681689678ed94aa90b7b92d94b80507
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-eb35f0
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 19 Interface Experience changes'
  evidence:
  - quote: Conversations can be archived or restored directly from the sidebar with
      Undo, and keyboard shortcuts open a New Session draft or archive the current
      eligible chat. Archiving keeps the conversation and its work, while group moves
      appear immediately and retain confirmed placement if the next refresh fails.
      New tabs keep the original draft in place and open with navigation expanded,
      and generated links retain the intended conversation. On desktop, right-click
      or Shift+F10 opens the full row menu, while touch keeps a menu button. If a
      group save is uncertain, refresh and check its placement before retrying.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The sidebar keeps loaded Codex conversations available while paired computers
      refresh, identifies linked messaging conversations from their recorded details,
      and keeps grouped agent-created chats searchable and reopenable. More room goes
      to conversation names by removing redundant owner avatars, duplicate Home entries
      and Worktree or Checkout row labels, with repository details still available
      on hover. Session lists and previews also reuse unchanged information more often,
      reducing repeated preparation as activity arrives.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Healthy session catalogs can also progress while another source is slow.
      Automatic list refreshes may wait for five idle seconds or briefly cool down
      after a slow read, while deliberate refreshes, navigation and reconnects bypass
      that delay.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Temporary child runs now belong in transcript activity and Tasks , leaving
      ordinary navigation for persistent conversations. Their parent conversation
      continues to show an activity ring during follow-up work, and the icon keeps
      its resting size when that ring starts. Use Tasks or transcript activity to
      inspect the work itself, since a failure tooltip is not a link to the child
      conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Search can find authorized conversations beyond the currently loaded sidebar,
      with avatars, owner badges, highlighted matches and All, Sessions or Messages
      filters to help recognize the result. Results remain a bounded set of matches,
      and cold archived history must first be restored by opening its conversation.
      Within a chat, Escape closes focused transcript search and returns focus without
      clearing your draft or pending reply.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Automatic naming can finish and update the sidebar after worktree setup
      stops waiting, while failed naming uses a neutral two-word name for a new session
      or worktree instead of copying the opening prompt. Setup can wait up to 30 seconds
      for a name, and a later title leaves an already-created branch unchanged. Manual
      names remain intact, and composing characters in the title editor no longer
      saves or discards a rename before composition ends.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Long chats load older history in fewer batches and keep navigation markers
      and reading position steadier as replies stream, the composer changes size or
      images finish loading. Expanded details and code-reading controls stay in place
      while the current part of a reply is still being written. Code controls now
      also survive a closing code fence and later paragraphs in that same live reply,
      though saved-history replacement or a source correction can still reset them.
      Code examples stay literal, reduced-motion preferences apply from startup, and
      opening a chat no longer slides the whole conversation into place. The initial
      history load stays small, while older-history batches can be larger.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: After rewinding and resending, the branch menu reveals the preserved conversations
      without a reload, and loaded history follows the branch you selected. Repeated
      branch listings and history reads also avoid some unnecessary transcript work.
      These are conversation branches, and returning to one does not undo earlier
      tool actions or file changes.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Reading older messages in a shared chat no longer gets interrupted by another
      person's message or typing, including when an automatic scroll was pending.
      Deliberate reader navigation remains active, and the active reply stays visible
      through queued sends and saved history. A message from your own account in another
      browser also counts as remote activity. Sending from the current pane or selecting
      Latest resumes following the conversation, while typing produces fewer repeated
      presence updates.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: You can keep editing a Side chat follow-up while its answer is pending,
      although sending still waits. Reloaded split panes also restore their own conversation's
      side panels instead of inheriting another pane's Files selection.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Multiline drafts remain readable during keyboard navigation and selection,
      while affected typing layouts avoid repeated resizing and unnecessary redraws
      around selected mentions.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Hover or keyboard-focus an ordinary public link to see page details before
      opening it, with an explicit Open in your browser action and a text fallback
      when images are unavailable. This sends the eligible URL, including its path
      and query, to the Gateway for an anonymous public-page fetch without your browser's
      site credentials. The existing automatic-favicon opt-out also disables this
      enrichment, and touch taps keep normal navigation.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Mobile web layouts keep message margins, galleries, session controls and
      sidebar tools within reach, with search available from the navigation drawer
      and placement choices stacked for smaller screens. On recognized iPhone and
      iPad Safari browsers, a single Attach entry opens the existing file chooser,
      with camera and source prompts still controlled by the operating system.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Telegram now selects the complete installed HTTP client under Bun, repairing
      the affected reply path and /models provider picker that could fail with dispatcher.compose
      is not a function . The live verification used a custom Bun build, so this scoped
      fix does not establish general stock-Bun support.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The Mac Dashboard follows the native window's appearance while loading,
      avoiding a white flash before the selected theme appears. The collapsed-sidebar
      Inbox also matches the other titlebar actions and leaves room for its unread
      badge.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: ACP-connected coding agents resolve model choices against the currently
      connected harness, including after reconnecting, and newly spawned child work
      appears once in the task list. Explicit model choices fail if they are unknown
      or ambiguous, so an unsupported selection cannot silently become another model.
      Failed ACPX starts also release unused session state while preserving queued
      retries.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Coding-agent and provider tests use more controlled startup, clocks and
      cleanup, helping failures point to the behavior under test. Shared fixtures
      retain coverage for model selection, streamed responses and credential preparation.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Command setup and diagnostic formatting avoid unused imports, repeated
      scans and temporary copies. Displayed results and selection behavior remain
      the same.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Control UI maintenance consolidates queued-message cleanup, session preferences
      and subscriptions under their existing owners. Rendering also reuses unchanged
      favicon colors.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 19-interface-experience-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: interface-experience
  title: 19 Interface Experience changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-09-23-3-interface-experience-changes-in-kimi-code-2-1-0|3
  Interface Experience changes in Kimi Code 2.1.0]]'
- '[[Changes/Lovable/2026-09-23-one-project-menu-on-your-phone|One project menu on
  your phone]]'
- '[[Changes/Lovable/2026-09-23-redesigned-projects-page|Redesigned Projects page]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: interface-experience
title: 19 Interface Experience changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 19 Interface Experience changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Conversations can be archived or restored directly from the sidebar with Undo, and keyboard shortcuts open a New Session draft or archive the current eligible chat. Archiving keeps the conversation and its work, while group moves appear immediately and retain confirmed placement if the next refresh fails. New tabs keep the original draft in place and open with navigation expanded, and generated links retain the intended conversation. On desktop, right-click or Shift+F10 opens the full row menu, while touch keeps a menu button. If a group save is uncertain, refresh and check its placement before retrying.

> The sidebar keeps loaded Codex conversations available while paired computers refresh, identifies linked messaging conversations from their recorded details, and keeps grouped agent-created chats searchable and reopenable. More room goes to conversation names by removing redundant owner avatars, duplicate Home entries and Worktree or Checkout row labels, with repository details still available on hover. Session lists and previews also reuse unchanged information more often, reducing repeated preparation as activity arrives.

> Healthy session catalogs can also progress while another source is slow. Automatic list refreshes may wait for five idle seconds or briefly cool down after a slow read, while deliberate refreshes, navigation and reconnects bypass that delay.

> Temporary child runs now belong in transcript activity and Tasks , leaving ordinary navigation for persistent conversations. Their parent conversation continues to show an activity ring during follow-up work, and the icon keeps its resting size when that ring starts. Use Tasks or transcript activity to inspect the work itself, since a failure tooltip is not a link to the child conversation.

> Search can find authorized conversations beyond the currently loaded sidebar, with avatars, owner badges, highlighted matches and All, Sessions or Messages filters to help recognize the result. Results remain a bounded set of matches, and cold archived history must first be restored by opening its conversation. Within a chat, Escape closes focused transcript search and returns focus without clearing your draft or pending reply.

> Automatic naming can finish and update the sidebar after worktree setup stops waiting, while failed naming uses a neutral two-word name for a new session or worktree instead of copying the opening prompt. Setup can wait up to 30 seconds for a name, and a later title leaves an already-created branch unchanged. Manual names remain intact, and composing characters in the title editor no longer saves or discards a rename before composition ends.

> Long chats load older history in fewer batches and keep navigation markers and reading position steadier as replies stream, the composer changes size or images finish loading. Expanded details and code-reading controls stay in place while the current part of a reply is still being written. Code controls now also survive a closing code fence and later paragraphs in that same live reply, though saved-history replacement or a source correction can still reset them. Code examples stay literal, reduced-motion preferences apply from startup, and opening a chat no longer slides the whole conversation into place. The initial history load stays small, while older-history batches can be larger.

> After rewinding and resending, the branch menu reveals the preserved conversations without a reload, and loaded history follows the branch you selected. Repeated branch listings and history reads also avoid some unnecessary transcript work. These are conversation branches, and returning to one does not undo earlier tool actions or file changes.

> Reading older messages in a shared chat no longer gets interrupted by another person's message or typing, including when an automatic scroll was pending. Deliberate reader navigation remains active, and the active reply stays visible through queued sends and saved history. A message from your own account in another browser also counts as remote activity. Sending from the current pane or selecting Latest resumes following the conversation, while typing produces fewer repeated presence updates.

> You can keep editing a Side chat follow-up while its answer is pending, although sending still waits. Reloaded split panes also restore their own conversation's side panels instead of inheriting another pane's Files selection.

> Multiline drafts remain readable during keyboard navigation and selection, while affected typing layouts avoid repeated resizing and unnecessary redraws around selected mentions.

> Hover or keyboard-focus an ordinary public link to see page details before opening it, with an explicit Open in your browser action and a text fallback when images are unavailable. This sends the eligible URL, including its path and query, to the Gateway for an anonymous public-page fetch without your browser's site credentials. The existing automatic-favicon opt-out also disables this enrichment, and touch taps keep normal navigation.

> Mobile web layouts keep message margins, galleries, session controls and sidebar tools within reach, with search available from the navigation drawer and placement choices stacked for smaller screens. On recognized iPhone and iPad Safari browsers, a single Attach entry opens the existing file chooser, with camera and source prompts still controlled by the operating system.

> Telegram now selects the complete installed HTTP client under Bun, repairing the affected reply path and /models provider picker that could fail with dispatcher.compose is not a function . The live verification used a custom Bun build, so this scoped fix does not establish general stock-Bun support.

> The Mac Dashboard follows the native window's appearance while loading, avoiding a white flash before the selected theme appears. The collapsed-sidebar Inbox also matches the other titlebar actions and leaves room for its unread badge.

> ACP-connected coding agents resolve model choices against the currently connected harness, including after reconnecting, and newly spawned child work appears once in the task list. Explicit model choices fail if they are unknown or ambiguous, so an unsupported selection cannot silently become another model. Failed ACPX starts also release unused session state while preserving queued retries.

> Coding-agent and provider tests use more controlled startup, clocks and cleanup, helping failures point to the behavior under test. Shared fixtures retain coverage for model selection, streamed responses and credential preparation.

> Command setup and diagnostic formatting avoid unused imports, repeated scans and temporary copies. Displayed results and selection behavior remain the same.

> Control UI maintenance consolidates queued-message cleanup, session preferences and subscriptions under their existing owners. Rendering also reuses unchanged favicon colors.

Source: https://docs.openclaw.ai/releases/2026.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-23-50-safety-and-privacy-changes-in-v2026-9-6|50 Safety and Privacy changes in v2026.9.6]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-23-localization-maintenance-removes-entries-whose-interface-text-has-already-been-r|Localization maintenance removes entries whose interface text has already been…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-23-5-reliability-and-performance-changes-in-v2026-9-6|5 Reliability and Performance changes in v2026.9.6]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-23-2-image-generation-changes-in-v2026-9-6|2 Image Generation changes in v2026.9.6]] · Image Generation
- [[Changes/OpenClaw/2026-09-23-18-voice-and-audio-changes-in-v2026-9-6|18 Voice and Audio changes in v2026.9.6]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-23-25-context-window-changes-in-v2026-9-6|25 Context Window changes in v2026.9.6]] · Context Window
- [[Changes/OpenClaw/2026-09-23-16-mobile-and-desktop-changes-in-v2026-9-6|16 Mobile and Desktop changes in v2026.9.6]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-23-41-agent-mode-changes-in-v2026-9-6|41 Agent Mode changes in v2026.9.6]] · Agent Mode
- [[Changes/OpenClaw/2026-09-23-16-collaboration-changes-in-v2026-9-6|16 Collaboration changes in v2026.9.6]] · Collaboration
- [[Changes/OpenClaw/2026-09-23-15-editor-experience-changes-in-v2026-9-6|15 Editor Experience changes in v2026.9.6]] · Editor Experience
- [[Changes/OpenClaw/2026-09-23-2-enterprise-and-administration-changes-in-v2026-9-6|2 Enterprise and Administration changes in v2026.9.6]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-23-31-developer-workflow-changes-in-v2026-9-6|31 Developer Workflow changes in v2026.9.6]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-23-8-pricing-model-changes-in-v2026-9-6|8 Pricing Model changes in v2026.9.6]] · Pricing Model
- [[Changes/OpenClaw/2026-09-23-plugin-requested-answer-revisions-wait-for-session-history-to-become-available-a|Plugin-requested answer revisions wait for session history to become available…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-23-6-files-and-data-changes-in-v2026-9-6|6 Files and Data changes in v2026.9.6]] · Files and Data
- [[Changes/OpenClaw/2026-09-23-58-apps-and-integrations-changes-in-v2026-9-6|58 Apps and Integrations changes in v2026.9.6]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-23-17-account-and-access-changes-in-v2026-9-6|17 Account and Access changes in v2026.9.6]] · Account and Access
- [[Changes/OpenClaw/2026-09-23-background-image-video-and-music-generation-can-complete-independently-of-the-re|Background image, video, and music generation can complete independently…]] · Music Generation
- [[Changes/OpenClaw/2026-09-23-23-memory-and-personalization-changes-in-v2026-9-6|23 Memory and Personalization changes in v2026.9.6]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-23-3-search-and-browsing-changes-in-v2026-9-6|3 Search and Browsing changes in v2026.9.6]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-23-9-automation-and-scheduling-changes-in-v2026-9-6|9 Automation and Scheduling changes in v2026.9.6]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-23-22-model-support-changes-in-v2026-9-6|22 Model Support changes in v2026.9.6]] · Model Support
- [[Changes/OpenClaw/2026-09-23-119-other-changes-in-v2026-9-6|119 other changes in v2026.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-09-23 · Lovable · [[Changes/Lovable/2026-09-23-redesigned-projects-page|Redesigned Projects page]]
- Later: 2026-09-24 · Claude Code · [[Changes/Claude Code/2026-09-24-4-interface-experience-changes-in-v2-1-282|4 Interface Experience changes in v2.1.282]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-eb35f0&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-19-interface-experience-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-eb35f0%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->