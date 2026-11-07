---
card_id: openclaw-2026-09-05-b2f534
date: '2026-09-05'
description: 'OpenClaw · 2026-09-05 · Interface Experience: 21 changes in v2026.9.2
  — Setting up a local model now starts with the computer that will run it, and OpenClaw…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1335
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e5fef3aaeb000bd82badd38428090726ca2731fdb80ba5fb9c343e550ad933f7
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-05-b2f534
  comparison: ''
  date: '2026-09-05'
  description: 'OpenClaw — v2026.9.2: 21 Interface Experience changes'
  evidence:
  - quote: Setting up a local model now starts with the computer that will run it,
      and OpenClaw checks that the model can use a tool before making it your default.
      The rest of setup gets several practical repairs too, from preserving complete
      workspace instructions after a failed write to choosing the intended agent,
      opening a hosted dashboard, and recovering shell completion when a profile cannot
      be changed.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Opening a long conversation now puts the recent messages you selected ahead
      of background chats and a restored Home pane, with smaller initial transfers
      and reusable avatar previews. Valid prefetched history stays available through
      unrelated sidebar updates, and completed messages avoid repeated redraws while
      a new reply streams. Older messages remain available by scrolling upward.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Choosing a command argument now submits the completed command from New
      Session, and the execution-host picker inserts valid settings while preserving
      the rest of a chat draft. Sending a message, submitting a chat command, or choosing
      Scroll to latest brings the newest output into view through composer resizing,
      while later manual scrolling and keys inside text or media controls remain under
      your control.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The model control can now tell you which fallback model is actually serving
      the conversation while the open picker keeps your preferred model selected.
      When the session returns to that preference, the old fallback label clears.
      Known model names stay visible while switching chats and loading their options,
      including in locked chats, without enabling controls before their availability
      is known.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: An Actions menu keeps copying IDs, pairing controls, and available desktops
      together, while an available Desktop opens in its own window. New Session and
      Move Session distinguish commands that are missing, waiting for pairing approval,
      or blocked by policy, so the next step matches the problem. The device guidance
      covers setup and reapproval, and Connection and System busyness show eligible
      mounted local disks separately.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The workspace sidebar makes the existing Discord community easier to find
      with a dismissible invitation that waits until sidebar interaction finishes
      before appearing. Joining opens the community in another tab, while closing
      the card saves a dismissal for that browser origin. If saving fails, the card
      can still stay dismissed for the current page with a warning.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: A valid diagram should not send you back to rewriting its source because
      the renderer could not load. Mermaid errors now distinguish unavailable rendering,
      invalid diagram source, and an image that could not display, with the appropriate
      reload or correction guidance and the source still readable and copyable.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: New Session makes the choice between Current checkout and New worktree
      explicit, with the starting branch and worktree name in the Checkout control.
      Device and cloud sessions continue to require a managed worktree, and local
      sessions can choose Current checkout when a worktree choice is unavailable.
      Recent Windows folders use readable short names, and the sidebar's familiar
      controls and nested-session loading placeholders keep their spacing through
      supported layouts.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The brief and workspace picker stay together before starting the session.
      Published 2026.9.2 interface with fictional Harbor data; no live task execution.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Expanded chat tables keep the same supported file previews and session
      links as their inline version, including keyboard activation. Following a link
      dismisses the expanded view so you can use its destination, closing it returns
      focus to Expand table, and changing conversations no longer leaves a hidden
      chat's table over the active one. The table guide also explains the existing,
      narrower navigation support in Ask OpenClaw.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Updated delegation guidance carries the requested outcome through child
      completion messages, so agents are instructed to continue authorized work after
      an intermediate review or check and verify the final result. For a request to
      land a pull request, that includes checking that GitHub reports it as merged.
      The instructions still allow a specific blocker when the remaining work needs
      new authority, credentials, or an external decision.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: iPhone conversations keep the current reply and working indicator visible
      as the assistant moves through tool calls, with streaming tables growing without
      repeatedly shifting earlier text. Opening the keyboard preserves the latest
      messages when you were already following them, while a deliberate scroll or
      selected search result keeps your chosen position. Scrolling near the left edge
      also takes a more clearly horizontal gesture before it opens the sidebar.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: When you use several Gateways, chat commands, widgets, approvals, settings,
      and status stay with the window or connection that owns them. Primary dashboards
      follow a changed Primary, independent saved-profile windows keep their own connection,
      and older replies cannot replace the selected Gateway's current settings. Switching
      Primary clears the old configuration draft, while reconnecting to the same Gateway
      preserves valid edits. A save already sent can still reach the previous Gateway,
      so changing selection does not undo an in-flight change.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Renewing the same account preserves its browser preferences, chat history,
      and queued messages. Signing in as someone else closes the previous account's
      native chat windows and uses separate history and queues, leaving earlier pending
      messages with their original account. Removing the saved Gateway clears its
      credentials and dashboard browser data.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Mac AI setup now shows confirmed connection-test rejection reasons and
      lets you explicitly retry or choose another connection without an old response
      wiping newer input. Uncertain outcomes keep their verification step, and older
      Gateways may still require the existing wait. Other daily controls receive focused
      repairs too, with scheduled-job lists retaining recent edits and deletions,
      and the browser sidebar resizing and remembering its width even with only one
      or two tabs.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The animated menu-bar icon keeps its existing motion with less CPU work
      in the measured idle scenarios. This is a focused reduction in background activity
      and animation cost; battery-life gains and the cleanup of separately detached
      provider processes are outside these changes.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: People sharing a Gateway can now connect their own supported model accounts
      in Settings → Profile → Connected accounts , choose a default for new chats,
      and use Account for this chat to make a separate choice for an existing conversation.
      Changing the default leaves existing chats alone, and collaborators and forks
      keep the account already selected for that chat. Model availability, status
      labels, fallback checks, and retry estimates now follow that personal selection.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Eligible interrupted subagent tasks can resume after a restart without
      another prompt, keeping the original task and conversation while showing progress
      from the replacement run. Already completed tasks recover their saved result
      and completion time. Restored follow-ups run through a limited queue so a large
      backlog does not start all at once, which can make that backlog take longer
      to clear. Resumption notices are separate from final replies and depend on a
      supported original destination and bounded retries.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Stopping a group of subagents sends stop requests to siblings without waiting
      for one sibling's cleanup, and includes new child branches discovered during
      the stop. A child launch still being prepared is also rejected if its parent
      loses authority before acceptance. Once accepted, children keep their independence
      after ordinary parent completion; a stop acknowledgment does not mean every
      underlying process has already finished cleaning up.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Command results give your agent more useful clues about what happened.
      A foreground command that exits unsuccessfully without printing anything now
      explicitly says (no output) beside its exit code, and background process lists
      distinguish an overall timeout from a command that stopped producing output.
      Polling a completed job clears its pending completion notice only after confirmed
      chat delivery or successful saving of the tool result, keeping that notice available
      when delivery or persistence fails.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Test cleanup, fixture isolation, and clearer failure reports make repository
      checks easier to diagnose. CI changes reduce repeated preparation and combine
      compatible jobs while retaining their checks. Internal refactors reduce repeated
      work in parsing, rendering, and database access without establishing a general
      user-facing speedup. The paired Vitest benchmark supports comparison of candidate
      versions; it does not establish acceptance of a Vitest upgrade.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 21-interface-experience-changes-in-v2026-9-2
  source_release: openclaw-2026-09-05-v2026-9-2-377f6d77
  source_type: openclaw_changelog
  theme: interface-experience
  title: 21 Interface Experience changes in v2026.9.2
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-04-42874-0-153-hotfix-show-astra-in-bundled-model-picker-rhan-oai|♯42874
  0.153 hotfix Show Astra in bundled model picker @rhan-oai]]'
- '[[Changes/GitHub Copilot CLI/2026-09-04-add-recent-created-name-and-classic-none-sorting-to-the-split-sessions-sidebar-w|Add
  Recent, Created, Name, and classic None sorting to the split Sessions sidebar…]]'
- '[[Changes/Lovable/2026-09-04-new-ways-to-open-project-settings|New ways to open
  project settings]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|openclaw-2026-09-05-v2026-9-2-377f6d77]]'
source_type: openclaw_changelog
theme: interface-experience
title: 21 Interface Experience changes in v2026.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 21 Interface Experience changes in v2026.9.2

**OpenClaw** · 2026-09-05 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.2) · from [[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Setting up a local model now starts with the computer that will run it, and OpenClaw checks that the model can use a tool before making it your default. The rest of setup gets several practical repairs too, from preserving complete workspace instructions after a failed write to choosing the intended agent, opening a hosted dashboard, and recovering shell completion when a profile cannot be changed.

> Opening a long conversation now puts the recent messages you selected ahead of background chats and a restored Home pane, with smaller initial transfers and reusable avatar previews. Valid prefetched history stays available through unrelated sidebar updates, and completed messages avoid repeated redraws while a new reply streams. Older messages remain available by scrolling upward.

> Choosing a command argument now submits the completed command from New Session, and the execution-host picker inserts valid settings while preserving the rest of a chat draft. Sending a message, submitting a chat command, or choosing Scroll to latest brings the newest output into view through composer resizing, while later manual scrolling and keys inside text or media controls remain under your control.

> The model control can now tell you which fallback model is actually serving the conversation while the open picker keeps your preferred model selected. When the session returns to that preference, the old fallback label clears. Known model names stay visible while switching chats and loading their options, including in locked chats, without enabling controls before their availability is known.

> An Actions menu keeps copying IDs, pairing controls, and available desktops together, while an available Desktop opens in its own window. New Session and Move Session distinguish commands that are missing, waiting for pairing approval, or blocked by policy, so the next step matches the problem. The device guidance covers setup and reapproval, and Connection and System busyness show eligible mounted local disks separately.

> The workspace sidebar makes the existing Discord community easier to find with a dismissible invitation that waits until sidebar interaction finishes before appearing. Joining opens the community in another tab, while closing the card saves a dismissal for that browser origin. If saving fails, the card can still stay dismissed for the current page with a warning.

> A valid diagram should not send you back to rewriting its source because the renderer could not load. Mermaid errors now distinguish unavailable rendering, invalid diagram source, and an image that could not display, with the appropriate reload or correction guidance and the source still readable and copyable.

> New Session makes the choice between Current checkout and New worktree explicit, with the starting branch and worktree name in the Checkout control. Device and cloud sessions continue to require a managed worktree, and local sessions can choose Current checkout when a worktree choice is unavailable. Recent Windows folders use readable short names, and the sidebar's familiar controls and nested-session loading placeholders keep their spacing through supported layouts.

> The brief and workspace picker stay together before starting the session. Published 2026.9.2 interface with fictional Harbor data; no live task execution.

> Expanded chat tables keep the same supported file previews and session links as their inline version, including keyboard activation. Following a link dismisses the expanded view so you can use its destination, closing it returns focus to Expand table, and changing conversations no longer leaves a hidden chat's table over the active one. The table guide also explains the existing, narrower navigation support in Ask OpenClaw.

> Updated delegation guidance carries the requested outcome through child completion messages, so agents are instructed to continue authorized work after an intermediate review or check and verify the final result. For a request to land a pull request, that includes checking that GitHub reports it as merged. The instructions still allow a specific blocker when the remaining work needs new authority, credentials, or an external decision.

> iPhone conversations keep the current reply and working indicator visible as the assistant moves through tool calls, with streaming tables growing without repeatedly shifting earlier text. Opening the keyboard preserves the latest messages when you were already following them, while a deliberate scroll or selected search result keeps your chosen position. Scrolling near the left edge also takes a more clearly horizontal gesture before it opens the sidebar.

> When you use several Gateways, chat commands, widgets, approvals, settings, and status stay with the window or connection that owns them. Primary dashboards follow a changed Primary, independent saved-profile windows keep their own connection, and older replies cannot replace the selected Gateway's current settings. Switching Primary clears the old configuration draft, while reconnecting to the same Gateway preserves valid edits. A save already sent can still reach the previous Gateway, so changing selection does not undo an in-flight change.

> Renewing the same account preserves its browser preferences, chat history, and queued messages. Signing in as someone else closes the previous account's native chat windows and uses separate history and queues, leaving earlier pending messages with their original account. Removing the saved Gateway clears its credentials and dashboard browser data.

> Mac AI setup now shows confirmed connection-test rejection reasons and lets you explicitly retry or choose another connection without an old response wiping newer input. Uncertain outcomes keep their verification step, and older Gateways may still require the existing wait. Other daily controls receive focused repairs too, with scheduled-job lists retaining recent edits and deletions, and the browser sidebar resizing and remembering its width even with only one or two tabs.

> The animated menu-bar icon keeps its existing motion with less CPU work in the measured idle scenarios. This is a focused reduction in background activity and animation cost; battery-life gains and the cleanup of separately detached provider processes are outside these changes.

> People sharing a Gateway can now connect their own supported model accounts in Settings → Profile → Connected accounts , choose a default for new chats, and use Account for this chat to make a separate choice for an existing conversation. Changing the default leaves existing chats alone, and collaborators and forks keep the account already selected for that chat. Model availability, status labels, fallback checks, and retry estimates now follow that personal selection.

> Eligible interrupted subagent tasks can resume after a restart without another prompt, keeping the original task and conversation while showing progress from the replacement run. Already completed tasks recover their saved result and completion time. Restored follow-ups run through a limited queue so a large backlog does not start all at once, which can make that backlog take longer to clear. Resumption notices are separate from final replies and depend on a supported original destination and bounded retries.

> Stopping a group of subagents sends stop requests to siblings without waiting for one sibling's cleanup, and includes new child branches discovered during the stop. A child launch still being prepared is also rejected if its parent loses authority before acceptance. Once accepted, children keep their independence after ordinary parent completion; a stop acknowledgment does not mean every underlying process has already finished cleaning up.

> Command results give your agent more useful clues about what happened. A foreground command that exits unsuccessfully without printing anything now explicitly says (no output) beside its exit code, and background process lists distinguish an overall timeout from a command that stopped producing output. Polling a completed job clears its pending completion notice only after confirmed chat delivery or successful saving of the tool result, keeping that notice available when delivery or persistence fails.

> Test cleanup, fixture isolation, and clearer failure reports make repository checks easier to diagnose. CI changes reduce repeated preparation and combine compatible jobs while retaining their checks. Internal refactors reduce repeated work in parsing, rendering, and database access without establishing a general user-facing speedup. The paired Vitest benchmark supports comparison of candidate versions; it does not establish acceptance of a Vitest upgrade.

Source: https://docs.openclaw.ai/releases/2026.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-05-24-safety-and-privacy-changes-in-v2026-9-2|24 Safety and Privacy changes in v2026.9.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-05-3-pricing-model-changes-in-v2026-9-2|3 Pricing Model changes in v2026.9.2]] · Pricing Model
- [[Changes/OpenClaw/2026-09-05-8-editor-experience-changes-in-v2026-9-2|8 Editor Experience changes in v2026.9.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-05-progress-mode-can-stay-quiet-about-routine-tool-calls-while-keeping-the-updates|Progress mode can stay quiet about routine tool calls while keeping the updates…]] · Presentation Creation
- [[Changes/OpenClaw/2026-09-05-swarm-is-now-available-to-eligible-agents-without-a-separate-enablement-step-so|Swarm is now available to eligible agents without a separate enablement step…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-a-rejected-send-can-keep-its-original-attachments-and-retry-action-when-you-leav|A rejected send can keep its original attachments and Retry action when you leave…]] · Files and Data
- [[Changes/OpenClaw/2026-09-05-20-account-and-access-changes-in-v2026-9-2|20 Account and Access changes in v2026.9.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-05-17-model-support-changes-in-v2026-9-2|17 Model Support changes in v2026.9.2]] · Model Support
- [[Changes/OpenClaw/2026-09-05-16-developer-workflow-changes-in-v2026-9-2|16 Developer Workflow changes in v2026.9.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2|21 Memory and Personalization changes in v2026.9.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-05-4-enterprise-and-administration-changes-in-v2026-9-2|4 Enterprise and Administration changes in v2026.9.2]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-05-if-background-image-video-or-music-generation-finishes-but-final-delivery-fails|If background image, video or music generation finishes but final delivery fails…]] · Music Generation
- [[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode changes in v2026.9.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2|35 Apps and Integrations changes in v2026.9.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2|8 Automation and Scheduling changes in v2026.9.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-05-9-collaboration-changes-in-v2026-9-2|9 Collaboration changes in v2026.9.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-05-10-mobile-and-desktop-changes-in-v2026-9-2|10 Mobile and Desktop changes in v2026.9.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-05-15-context-window-changes-in-v2026-9-2|15 Context Window changes in v2026.9.2]] · Context Window
- [[Changes/OpenClaw/2026-09-05-4-search-and-browsing-changes-in-v2026-9-2|4 Search and Browsing changes in v2026.9.2]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-05-17-voice-and-audio-changes-in-v2026-9-2|17 Voice and Audio changes in v2026.9.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-05-3-reliability-and-performance-changes-in-v2026-9-2|3 Reliability and Performance changes in v2026.9.2]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-05-you-can-now-put-the-part-of-a-task-you-are-working-on-in-the-main-view-and-keep|Put the part of a task you are working on in the main view and keep the conversation…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-72-other-changes-in-v2026-9-2|72 other changes in v2026.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-09-04 · Lovable · [[Changes/Lovable/2026-09-04-new-ways-to-open-project-settings|New ways to open project settings]]
- Later: 2026-09-08 · ChatGPT · [[Changes/ChatGPT/2026-09-08-edit-and-comment-on-mobile-open-a-generated-image-full-screen-to-edit-it-or-add|Edit and comment]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-05-b2f534&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-05-21-interface-experience-changes-in-v2026-9-2.md%0ACard%20ID%3A%20openclaw-2026-09-05-b2f534%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->