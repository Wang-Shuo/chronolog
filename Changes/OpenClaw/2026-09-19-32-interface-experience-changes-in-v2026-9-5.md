---
card_id: openclaw-2026-09-19-4a3a04
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Interface Experience: 32 changes in v2026.9.5
  — Choose whether empty sidebar groups hide When filtering , Always , or Never ,
  with…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2715
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d78fb75033ca98cfdd8237e3a2eb59c9dd6f9f8c7b6bb4bc6d46e65811eb1412
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-4a3a04
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 32 Interface Experience changes'
  evidence:
  - quote: Choose whether empty sidebar groups hide When filtering , Always , or Never
      , with separate choices for each user and Gateway in this browser.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: New Session puts your devices in a searchable picker, with capacity details
      and an Any available device choice when you have several. Cloud options sit
      beside their provider, and suggested tasks can start in the current conversation,
      a new session, or a separate Git worktree .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: You can submit text and attachments while chat history loads and start
      your next draft immediately. Delivery waits until the conversation is ready.
      During a reconnect, a message OpenClaw has tried to send appears once in the
      conversation; messages it has not tried to send stay editable in the queue.
      If the connection drops while you correct one of those waiting messages, you
      can still save the correction. It keeps the message’s delivery choice and queue
      position, even if the main composer now uses Steer or Interrupt . Attachments
      show when they are being prepared, and removal controls name the file.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Loading earlier messages now keeps you on the message you were reading,
      including when you choose Show earlier . Completed answers stay visible after
      later tool activity, and Japanese, Chinese, and Korean bold text and multiline
      table cells display as intended. Desktop navigation groups loaded assistant
      responses by run, while long user messages have visible Show more and Show less
      controls.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Activity summaries sit closer to their replies without shrinking touch
      controls, and hidden panes remember your reading position. Large plain-text
      replies, including text shown when Markdown rendering fails, take less work
      to display while retaining the existing HTML sanitization.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Dashboard editors can use Layout → Use current view as default to save
      a shared fullscreen or split starting view, and agents can save it too. A viewer’s
      personal layout takes priority, and saving a default never rearranges active
      viewers. Fullscreen fills the task area, rather than the browser screen.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Desktop pages outside Chat now place titles or hub tabs and page actions
      in a shared toolbar. The layout also keeps Arabic and Persian page actions clear
      of the fixed sidebar controls. Chat, Settings takeover views, and mobile headers
      keep their existing layouts.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The new Systems workspace brings searchable machines, their reported resource
      readings, and an available remote desktop into the main workspace. Desktop viewing
      starts in view-only mode; taking control remains an explicit action subject
      to your permissions. If you customized your pinned navigation, add Systems through
      Edit pinned items .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Sorting a large session sidebar by People does less repeated work, especially
      when many different people own sessions. The ordering, selected session, and
      familiar controls stay the same.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Cancel preserves pending work, and a failed recovery move does not trigger
      removal. For a batch, recover each affected session individually before retrying
      the selection. CLI and native clients do not gain this interactive recovery
      flow.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Managed Gateway and node services can stay on the exact Node or Bun executable
      you select with --runtime-path , including a version-manager path. Use an absolute
      executable path; reinstall and repair preserve it, and an invalid pin produces
      an error instead of silently choosing another runtime. Set a different path
      to replace the pin, or explicitly use --runtime node without a path to return
      to automatic selection. See the Gateway service guide .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Chat can propose settings edits that were previously refused, including
      runtime pins and model or provider settings. After a validation failure, the
      assistant can offer one correction with a separate approval under your session's
      policy. A notice saying completion is unconfirmed means you should inspect current
      settings before retrying. Saving settings does not test whether an API key or
      model route works.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Reading a Discord message with --message-id or messageId now returns that
      message or an error, instead of unrelated recent history. Commands, autocomplete,
      and model selection also keep the intended channel or thread when Discord supplies
      only its ID. Authorized actions in your current DM accept equivalent native-channel
      targets while retaining the existing account and conversation restrictions.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Message scripts must omit --channel when they want automatic selection.
      An empty value now stops the command instead of silently choosing a channel;
      see message commands .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Switching keeps each experience's loaded windows and drafts available when
      you return. Drafts stay with their own experience, Gateway address and signed-in
      account, including the address used by an SSH tunnel. Settings opens on the
      web, while Connection, About and Quick Chat remain native. Command-N opens the
      Gateway-window picker, and Shift-Command-N creates a new thread.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: You can run a Gateway on your Mac alongside a remote primary , with separate
      chat and dashboard windows. Enable “Also run a Gateway on this Mac” in Connection
      settings. It is off by default, and your remote primary keeps its existing Talk,
      menu-bar and node role. Connection settings also offers install, update and
      repair actions for app-managed local Gateways, even after you dismiss setup.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Open Chat actions → Review changes to inspect uncommitted code and add
      a selection to your existing draft without sending it. The viewer is read-only
      and appears when your Gateway supports change review. The Chat actions menu
      also stops closing unexpectedly on affected phones.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The sidebar also keeps a stable width while opening and dragging, in both
      left-to-right and right-to-left layouts.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Ending Talk on Wear OS starts microphone and speaker shutdown before waiting
      for the phone, while “Ending call…” keeps the conversation visible. Model choices
      now follow the chat selected on your watch, with available choices retained
      during a partial refresh. Update the phone app and Gateway if the picker reports
      missing support.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The native Mac chat sidebar now groups conversations under named agents
      and keeps a text draft for each conversation. Activity and attention indicators
      help you find work that needs you, while timestamps and cached message previews
      make threads easier to recognize. The indicators cover loaded sessions and local
      history. Finish handling pending attachments before switching conversations.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: With multiple Gateways saved, the iOS sidebar now offers a picker so you
      can switch without opening Connection settings. Unavailable Gateways stay listed,
      and the selected connection shows its current status. Before switching, send
      or clear your draft, finish recording, remove attachments and wait for pending
      delivery. Drafts do not move between Gateways or restore separately for each
      one.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Tap a question or approval icon in the iOS, Android or native Mac sidebar
      to inspect what needs your attention without leaving the current conversation,
      even in collapsed groups. The count follows the oldest request's kind. Previewing
      does not approve anything, and iOS administration approvals still open the Dashboard
      review page. Resolved requests and requests from a previous Gateway or account
      stop contributing attention.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: WebChat shows the model actually generating a reply, including observed
      fallback changes in local, worker and native Codex runs. The picker keeps your
      saved choice. Until OpenClaw has an execution observation, the label says Model
      pending instead of reusing a previous turn's model.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Archiving an independent cloud session no longer waits for unrelated setup
      maintenance. Its sidebar row hides immediately and returns with an error if
      the request is rejected. An already-failed worker with no live turn can stay
      archived while cleanup is retried separately. Undo restores the row while the
      retained checkout is intact; it does not restart the worker.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Session Share lets you share selected conversation groups with teammates
      on another paired OpenClaw installation, giving them read-only access without
      handing over control of the conversation. Both sides must enable sharing, and
      an empty group selection shares nothing. Recipients see conversation text and
      eligible user-created forks, without subagents, tool activity or reasoning.
      They can read the conversation but cannot continue it, archive it or use its
      terminal.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Choose which installed coding apps supply sidebar conversations in Settings
      → Appearance → Session sources. Claude Code, Codex, OpenCode and Pi now have
      one place for these controls. Updated paired nodes can show native Codex conversations
      without a matching Gateway agent, and empty catalogs stay hidden while discovery
      continues. Large CLI history imports preserve more conversation text and visible
      results within the response size limit.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Bundled code-navigation tools process large, fragmented language-server
      replies with less copying. Stopping a turn during language-server startup now
      stops further launches and cleans up the servers that turn acquired. Canceling
      an individual tool request still leaves its shared server available for later
      requests.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Confirming a Beam deletion immediately hides its sidebar row while the
      request runs. If deletion fails, the current row returns with an error. Successful
      deletion is permanent and leaves independent continuations intact; uploading
      the same Beam later can recreate its row.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: UI customization now lives under Plugins → Customize UI, replacing the
      floating button. The Plugins page always opens the built-in workspace so you
      can reach these controls even when a custom workspace hides navigation. Open
      /plugins under your Control UI base URL and choose Built-in to return to the
      standard workspace.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Log views and exports now mask recognized credentials and private-key fragments
      across selected portions of stored logs while keeping JSON readable. The stored
      files remain unchanged, and reading a selection can take longer because masking
      may scan earlier history. Secret detection remains limited to recognized patterns
      and registered values, and the tool-result change does not cover native Codex.
      Previously shortened message text cannot be restored.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: If you use protected egress, Git commands launched by the Gateway now receive
      the proxy's trusted certificate bundle. This fixes the resulting HTTPS certificate
      error while keeping certificate verification enabled, with no new settings required.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Goals retain multiline instructions and meaningful spacing, so a carefully
      written objective reaches the agent intact. Goals can also be created without
      a token budget, and reconfirming completion keeps the original finish time.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 32-interface-experience-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: interface-experience
  title: 32 Interface Experience changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-09-18-custom-agent-controls-and-keyboard-navigation|Custom
  agent controls and keyboard navigation]]'
- '[[Changes/Google Antigravity/2026-09-18-3-interface-experience-changes-in-hub-v2-15-0-custom-agent-controls|3
  Interface Experience changes in HUB v2.15.0 — Custom agent controls…]]'
- '[[Changes/Lovable/2026-09-18-redesigned-project-cards|Redesigned project cards]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: interface-experience
title: 32 Interface Experience changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 32 Interface Experience changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Choose whether empty sidebar groups hide When filtering , Always , or Never , with separate choices for each user and Gateway in this browser.

> New Session puts your devices in a searchable picker, with capacity details and an Any available device choice when you have several. Cloud options sit beside their provider, and suggested tasks can start in the current conversation, a new session, or a separate Git worktree .

> You can submit text and attachments while chat history loads and start your next draft immediately. Delivery waits until the conversation is ready. During a reconnect, a message OpenClaw has tried to send appears once in the conversation; messages it has not tried to send stay editable in the queue. If the connection drops while you correct one of those waiting messages, you can still save the correction. It keeps the message’s delivery choice and queue position, even if the main composer now uses Steer or Interrupt . Attachments show when they are being prepared, and removal controls name the file.

> Loading earlier messages now keeps you on the message you were reading, including when you choose Show earlier . Completed answers stay visible after later tool activity, and Japanese, Chinese, and Korean bold text and multiline table cells display as intended. Desktop navigation groups loaded assistant responses by run, while long user messages have visible Show more and Show less controls.

> Activity summaries sit closer to their replies without shrinking touch controls, and hidden panes remember your reading position. Large plain-text replies, including text shown when Markdown rendering fails, take less work to display while retaining the existing HTML sanitization.

> Dashboard editors can use Layout → Use current view as default to save a shared fullscreen or split starting view, and agents can save it too. A viewer’s personal layout takes priority, and saving a default never rearranges active viewers. Fullscreen fills the task area, rather than the browser screen.

> Desktop pages outside Chat now place titles or hub tabs and page actions in a shared toolbar. The layout also keeps Arabic and Persian page actions clear of the fixed sidebar controls. Chat, Settings takeover views, and mobile headers keep their existing layouts.

> The new Systems workspace brings searchable machines, their reported resource readings, and an available remote desktop into the main workspace. Desktop viewing starts in view-only mode; taking control remains an explicit action subject to your permissions. If you customized your pinned navigation, add Systems through Edit pinned items .

> Sorting a large session sidebar by People does less repeated work, especially when many different people own sessions. The ordering, selected session, and familiar controls stay the same.

> Cancel preserves pending work, and a failed recovery move does not trigger removal. For a batch, recover each affected session individually before retrying the selection. CLI and native clients do not gain this interactive recovery flow.

> Managed Gateway and node services can stay on the exact Node or Bun executable you select with --runtime-path , including a version-manager path. Use an absolute executable path; reinstall and repair preserve it, and an invalid pin produces an error instead of silently choosing another runtime. Set a different path to replace the pin, or explicitly use --runtime node without a path to return to automatic selection. See the Gateway service guide .

> Chat can propose settings edits that were previously refused, including runtime pins and model or provider settings. After a validation failure, the assistant can offer one correction with a separate approval under your session's policy. A notice saying completion is unconfirmed means you should inspect current settings before retrying. Saving settings does not test whether an API key or model route works.

> Reading a Discord message with --message-id or messageId now returns that message or an error, instead of unrelated recent history. Commands, autocomplete, and model selection also keep the intended channel or thread when Discord supplies only its ID. Authorized actions in your current DM accept equivalent native-channel targets while retaining the existing account and conversation restrictions.

> Message scripts must omit --channel when they want automatic selection. An empty value now stops the command instead of silently choosing a channel; see message commands .

> Switching keeps each experience's loaded windows and drafts available when you return. Drafts stay with their own experience, Gateway address and signed-in account, including the address used by an SSH tunnel. Settings opens on the web, while Connection, About and Quick Chat remain native. Command-N opens the Gateway-window picker, and Shift-Command-N creates a new thread.

> You can run a Gateway on your Mac alongside a remote primary , with separate chat and dashboard windows. Enable “Also run a Gateway on this Mac” in Connection settings. It is off by default, and your remote primary keeps its existing Talk, menu-bar and node role. Connection settings also offers install, update and repair actions for app-managed local Gateways, even after you dismiss setup.

> Open Chat actions → Review changes to inspect uncommitted code and add a selection to your existing draft without sending it. The viewer is read-only and appears when your Gateway supports change review. The Chat actions menu also stops closing unexpectedly on affected phones.

> The sidebar also keeps a stable width while opening and dragging, in both left-to-right and right-to-left layouts.

> Ending Talk on Wear OS starts microphone and speaker shutdown before waiting for the phone, while “Ending call…” keeps the conversation visible. Model choices now follow the chat selected on your watch, with available choices retained during a partial refresh. Update the phone app and Gateway if the picker reports missing support.

> The native Mac chat sidebar now groups conversations under named agents and keeps a text draft for each conversation. Activity and attention indicators help you find work that needs you, while timestamps and cached message previews make threads easier to recognize. The indicators cover loaded sessions and local history. Finish handling pending attachments before switching conversations.

> With multiple Gateways saved, the iOS sidebar now offers a picker so you can switch without opening Connection settings. Unavailable Gateways stay listed, and the selected connection shows its current status. Before switching, send or clear your draft, finish recording, remove attachments and wait for pending delivery. Drafts do not move between Gateways or restore separately for each one.

> Tap a question or approval icon in the iOS, Android or native Mac sidebar to inspect what needs your attention without leaving the current conversation, even in collapsed groups. The count follows the oldest request's kind. Previewing does not approve anything, and iOS administration approvals still open the Dashboard review page. Resolved requests and requests from a previous Gateway or account stop contributing attention.

> WebChat shows the model actually generating a reply, including observed fallback changes in local, worker and native Codex runs. The picker keeps your saved choice. Until OpenClaw has an execution observation, the label says Model pending instead of reusing a previous turn's model.

> Archiving an independent cloud session no longer waits for unrelated setup maintenance. Its sidebar row hides immediately and returns with an error if the request is rejected. An already-failed worker with no live turn can stay archived while cleanup is retried separately. Undo restores the row while the retained checkout is intact; it does not restart the worker.

> Session Share lets you share selected conversation groups with teammates on another paired OpenClaw installation, giving them read-only access without handing over control of the conversation. Both sides must enable sharing, and an empty group selection shares nothing. Recipients see conversation text and eligible user-created forks, without subagents, tool activity or reasoning. They can read the conversation but cannot continue it, archive it or use its terminal.

> Choose which installed coding apps supply sidebar conversations in Settings → Appearance → Session sources. Claude Code, Codex, OpenCode and Pi now have one place for these controls. Updated paired nodes can show native Codex conversations without a matching Gateway agent, and empty catalogs stay hidden while discovery continues. Large CLI history imports preserve more conversation text and visible results within the response size limit.

> Bundled code-navigation tools process large, fragmented language-server replies with less copying. Stopping a turn during language-server startup now stops further launches and cleans up the servers that turn acquired. Canceling an individual tool request still leaves its shared server available for later requests.

> Confirming a Beam deletion immediately hides its sidebar row while the request runs. If deletion fails, the current row returns with an error. Successful deletion is permanent and leaves independent continuations intact; uploading the same Beam later can recreate its row.

> UI customization now lives under Plugins → Customize UI, replacing the floating button. The Plugins page always opens the built-in workspace so you can reach these controls even when a custom workspace hides navigation. Open /plugins under your Control UI base URL and choose Built-in to return to the standard workspace.

> Log views and exports now mask recognized credentials and private-key fragments across selected portions of stored logs while keeping JSON readable. The stored files remain unchanged, and reading a selection can take longer because masking may scan earlier history. Secret detection remains limited to recognized patterns and registered values, and the tool-result change does not cover native Codex. Previously shortened message text cannot be restored.

> If you use protected egress, Git commands launched by the Gateway now receive the proxy's trusted certificate bundle. This fixes the resulting HTTPS certificate error while keeping certificate verification enabled, with no new settings required.

> Goals retain multiline instructions and meaningful spacing, so a carefully written objective reaches the agent intact. Goals can also be created without a token budget, and reconfirming completion keeps the original finish time.

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
- [[Changes/OpenClaw/2026-09-19-14-automation-and-scheduling-changes-in-v2026-9-5|14 Automation and Scheduling changes in v2026.9.5]] · Automation and Scheduling
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
## Nearby in Interface Experience

- Earlier: 2026-09-18 · Lovable · [[Changes/Lovable/2026-09-18-redesigned-project-cards|Redesigned project cards]]
- Later: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-number-key-selection-in-the-question-dialog-works-for-choices-10-and-beyond|Number-key selection in the question dialog works for choices 10 and beyond]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-4a3a04&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-32-interface-experience-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-4a3a04%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->