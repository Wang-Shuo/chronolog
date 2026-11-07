---
card_id: openclaw-2026-09-30-75633d
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Interface Experience: 17 changes in v2026.9.7
  — Onboarding starts sooner and explains invalid options and workspace paths more
  clearly…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1360
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fefe19f7e76a403a91a24341b5c0ba6751f029f699f23d5a158cf715eb3e9be0
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-75633d
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 17 Interface Experience changes'
  evidence:
  - quote: Onboarding starts sooner and explains invalid options and workspace paths
      more clearly. If you want a workspace without generated starter files, openclaw
      setup --baseline --skip-bootstrap now remembers that choice and preserves existing
      files.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The sidebar’s Filter & sort panel brings filtering and display choices
      together. Pinned chats stay in Pages across agents, and saved forks stay beneath
      their parent conversation after a restart. Unnamed heartbeat chats are hidden
      unless you choose Show system sessions.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Sidebar previews send fewer updates while your open chat keeps its full
      live reply stream. Hidden browser tabs also stop receiving sidebar-only activity.
      If you use a custom SDK client, update the Gateway alongside the SDK to keep
      live subscriptions working.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Agent commentary stays beside its tool activity, and work summaries distinguish
      skipped tools from failures or approval requests. During a run, the activity
      row keeps a readable tool purpose visible between calls, normally giving you
      three seconds to read it. Failures, blocks, and completion appear immediately.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The Online sidebar distinguishes recent interaction from simply being connected
      and now includes your own account. Compact rows show each person’s accessible
      open and running conversations. The expanded list orders Active, Idle, then
      unknown activity, with people running work first and names alphabetical within
      each group. Count sorting, the running-only filter, and aggregate totals have
      been removed. Quiet reading can show as Idle, and Running excludes queued work
      and work running only in child conversations.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: PR previews follow the chat’s working branch, so an incidental PR link
      no longer creates a banner. Branch and CI previews disappear on detached or
      default-branch checkouts. Sidebar badges may not appear until you open a chat,
      and mobile chat now shows the working branch before a PR exists.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: More menus, panels, and embedded apps follow your selected colors. Keyboard
      users get clearer focus and shortcut hints, with improved access to sidebar,
      file, and media controls. High-contrast indicators also improve in the affected
      controls; imported palettes still use their supplied colors.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Telegram keeps progress visible or shows a warning when a final answer
      fails to arrive. If delivery is uncertain, check OpenClaw chat history before
      retrying, since the answer may already have reached the chat. OpenClaw does
      not automatically resend uncertain answers, to avoid duplicates.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: More Android and Apple app controls, settings and error messages follow
      your chosen language. These updates refresh existing supported languages, including
      attachment controls, sidebar options and connection guidance.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The iPhone and iPad sidebar mascot pauses while hidden and resumes when
      you open the sidebar, avoiding animation work you cannot see.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Agents can use a configured Decision model to answer yes/no questions,
      choose between alternatives, or score supplied evidence. That evidence goes
      to your selected local or hosted provider, with its normal limits and charges.
      Results do not authorize actions, and the default-off Labs preference does not
      start automatic evaluations. Private or nightly setups using the old TypeSafe
      tool or model setting must move to the shared Decision selection.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Announcement setup suggests known conversations after you select a channel
      and enter its Account ID, with manual entry still available. Scheduled announcements
      receive the channel's formatting instructions, and command or script announcements
      sent to an explicit destination can appear in chat history for follow-up replies.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: QA Lab skips hidden sidebar controls when you navigate with the keyboard.
      Dashboard refreshes keep your selected tab, keyboard focus, and horizontal scroll
      position.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The Beam sidebar does less work when refreshing its session list. Local
      changes trigger a refresh, while changes from other processes are checked periodically.
      Ongoing uploads can still delay a fresh listing.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: 'By default, zero-wait messages to an agent’s own running child now try
      to guide its current work. Choose mode: "followup" when you need a separate
      turn and completion. Acceptance does not confirm the child has read it, and
      queued guidance can be lost on restart.'
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The terminal model picker opens while choices load and keeps your search
      as it refreshes. Startup and session refreshes also preserve the conversation
      you selected. Text submitted while a conversation loads stays editable until
      you press Enter again; a startup --message that was not sent is reported and
      is not retried automatically.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Release pages and plain-Markdown copies link to each other, so you can
      choose the format you prefer. Documentation navigation includes existing Persian
      and Thai translations, and old docs Showcase links point to the website Showcase
      . Contributors can also preview edits with the current website renderer.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 17-interface-experience-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: interface-experience
  title: 17 Interface Experience changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-30-4-interface-experience-changes-in-v2-1-286|4 Interface
  Experience changes in v2.1.286]]'
- '[[Changes/GitHub Copilot CLI/2026-09-30-2-interface-experience-changes-in-v1-0-90|2
  Interface Experience changes in v1.0.90]]'
- '[[Changes/Google Antigravity/2026-09-30-rendered-markdown-in-artifacts-and-in-files-opened-in-the-side-pane-can-now-be-e|Rendered
  Markdown in artifacts and in files opened in the side pane can now…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: interface-experience
title: 17 Interface Experience changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Interface Experience changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Onboarding starts sooner and explains invalid options and workspace paths more clearly. If you want a workspace without generated starter files, openclaw setup --baseline --skip-bootstrap now remembers that choice and preserves existing files.

> The sidebar’s Filter & sort panel brings filtering and display choices together. Pinned chats stay in Pages across agents, and saved forks stay beneath their parent conversation after a restart. Unnamed heartbeat chats are hidden unless you choose Show system sessions.

> Sidebar previews send fewer updates while your open chat keeps its full live reply stream. Hidden browser tabs also stop receiving sidebar-only activity. If you use a custom SDK client, update the Gateway alongside the SDK to keep live subscriptions working.

> Agent commentary stays beside its tool activity, and work summaries distinguish skipped tools from failures or approval requests. During a run, the activity row keeps a readable tool purpose visible between calls, normally giving you three seconds to read it. Failures, blocks, and completion appear immediately.

> The Online sidebar distinguishes recent interaction from simply being connected and now includes your own account. Compact rows show each person’s accessible open and running conversations. The expanded list orders Active, Idle, then unknown activity, with people running work first and names alphabetical within each group. Count sorting, the running-only filter, and aggregate totals have been removed. Quiet reading can show as Idle, and Running excludes queued work and work running only in child conversations.

> PR previews follow the chat’s working branch, so an incidental PR link no longer creates a banner. Branch and CI previews disappear on detached or default-branch checkouts. Sidebar badges may not appear until you open a chat, and mobile chat now shows the working branch before a PR exists.

> More menus, panels, and embedded apps follow your selected colors. Keyboard users get clearer focus and shortcut hints, with improved access to sidebar, file, and media controls. High-contrast indicators also improve in the affected controls; imported palettes still use their supplied colors.

> Telegram keeps progress visible or shows a warning when a final answer fails to arrive. If delivery is uncertain, check OpenClaw chat history before retrying, since the answer may already have reached the chat. OpenClaw does not automatically resend uncertain answers, to avoid duplicates.

> More Android and Apple app controls, settings and error messages follow your chosen language. These updates refresh existing supported languages, including attachment controls, sidebar options and connection guidance.

> The iPhone and iPad sidebar mascot pauses while hidden and resumes when you open the sidebar, avoiding animation work you cannot see.

> Agents can use a configured Decision model to answer yes/no questions, choose between alternatives, or score supplied evidence. That evidence goes to your selected local or hosted provider, with its normal limits and charges. Results do not authorize actions, and the default-off Labs preference does not start automatic evaluations. Private or nightly setups using the old TypeSafe tool or model setting must move to the shared Decision selection.

> Announcement setup suggests known conversations after you select a channel and enter its Account ID, with manual entry still available. Scheduled announcements receive the channel's formatting instructions, and command or script announcements sent to an explicit destination can appear in chat history for follow-up replies.

> QA Lab skips hidden sidebar controls when you navigate with the keyboard. Dashboard refreshes keep your selected tab, keyboard focus, and horizontal scroll position.

> The Beam sidebar does less work when refreshing its session list. Local changes trigger a refresh, while changes from other processes are checked periodically. Ongoing uploads can still delay a fresh listing.

> By default, zero-wait messages to an agent’s own running child now try to guide its current work. Choose mode: "followup" when you need a separate turn and completion. Acceptance does not confirm the child has read it, and queued guidance can be lost on restart.

> The terminal model picker opens while choices load and keeps your search as it refreshes. Startup and session refreshes also preserve the conversation you selected. Text submitted while a conversation loads stays editable until you press Enter again; a startup --message that was not sent is reported and is not retried automatically.

> Release pages and plain-Markdown copies link to each other, so you can choose the format you prefer. Documentation navigation includes existing Persian and Thai translations, and old docs Showcase links point to the website Showcase . Contributors can also preview edits with the current website renderer.

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
- [[Changes/OpenClaw/2026-09-30-36-apps-and-integrations-changes-in-v2026-9-7|36 Apps and Integrations changes in v2026.9.7]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-30-2-video-generation-changes-in-v2026-9-7|2 Video Generation changes in v2026.9.7]] · Video Generation
- [[Changes/OpenClaw/2026-09-30-12-voice-and-audio-changes-in-v2026-9-7|12 Voice and Audio changes in v2026.9.7]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-30-21-safety-and-privacy-changes-in-v2026-9-7|21 Safety and Privacy changes in v2026.9.7]] · Safety and Privacy
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
## Nearby in Interface Experience

- Earlier: 2026-09-30 · Google Antigravity · [[Changes/Google Antigravity/2026-09-30-rendered-markdown-in-artifacts-and-in-files-opened-in-the-side-pane-can-now-be-e|Rendered Markdown in artifacts and in files opened in the side pane can now…]]
- Later: 2026-10-01 · Codex CLI · [[Changes/Codex CLI/2026-10-01-2-interface-experience-changes-in-rust-v0-160-0|2 Interface Experience changes in rust-v0.160.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-75633d&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-17-interface-experience-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-75633d%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->