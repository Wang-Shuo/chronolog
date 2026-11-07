---
card_id: openclaw-2026-10-10-f98adc
date: '2026-10-10'
description: 'OpenClaw · 2026-10-10 · Interface Experience: 20 changes in v2026.10.1
  — App panels fill the available space in fullscreen and split layouts, and transparent…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2736
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 45470e1e951898e0d2b0100821301ba2d9a8eef12d0bd5706aee56ebbca9d991
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-10-f98adc
  comparison: ''
  date: '2026-10-10'
  description: 'OpenClaw — v2026.10.1: 20 Interface Experience changes'
  evidence:
  - quote: App panels fill the available space in fullscreen and split layouts, and
      transparent apps that follow the host theme match light and dark dashboards.
      File views update after edits, and dashboard content reflects accepted board
      changes.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: You can snooze an eligible conversation in the web Control UI to clear
      it from the Active sidebar while its work continues. Find it in Snoozed or All
      and wake it yourself, or let it return at the chosen time or earlier after interaction,
      completion or pinning. Archived, child and protected conversations are excluded.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Nested board links and removable, reorderable sidebar pins make boards
      easier to reach. #164604 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: The Online sidebar lets you focus on people with running work and sort
      by presence, running work, open-chat count or name. These choices are temporary,
      and counts cover accessible open chats.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Sidebar pencil markers help you find saved drafts after reload or in a
      fresh tab, including attachments, replies and goals. Queued messages show an
      image preview, and their attachments leave the composer without clearing newer
      input. Incognito is excluded; without browser storage, drafts stay only in the
      current tab, and changes do not sync live to already-open tabs.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Consecutive updates from the same outside conversation share a compact
      row you can expand to read the original messages, times and available source
      links. Search and reply navigation open the relevant messages for you.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Agent identity editing brings related fields together and adds a searchable
      emoji picker alongside direct entry. Text and emoji avatars appear larger when
      starting chat, and name or avatar changes show the latest saved result. Clearing
      a saved emoji remains unsupported. If you still use an unmigrated browser-wide
      avatar, set each agent's avatar again in Overview under Identity.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Quiet Hours keeps its time window and timezone together, with a menu for
      choosing the zone. Saved aliases remain available, but you cannot type an unsaved
      zone missing from the browser's catalog. Some browsers offer only the local
      zone, UTC and the saved zone.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: The experimental native Mac sidebar adds groups, colors and owners to help
      you organize conversations and find the one you need. You can copy transcripts
      or links and open a selected conversation in another window. Group defaults
      can start new conversations in selected folders or eligible separate Git working
      copies; editor shortcuts need a local working copy.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: You can load older conversations for the selected agent and search names,
      details and messages from the Mac sidebar. Search combines immediate local matches
      with Gateway results and explains when indexing or archived transcripts leave
      results incomplete. View options remembers your filters, grouping and display
      choices for each Gateway profile.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Expandable follow-up trees and Pages across agents keep related conversations
      within reach. Hover over or keyboard-focus a conversation to preview available
      people, workspace and progress details without opening it. Pull-request cards
      identify last-known status when a refresh fails. The Mac chat guide covers navigation
      and keyboard access.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: You can choose Ultrafast on supported embedded OpenAI Responses routes
      with an API-key profile or a direct key. Codex requires an explicit Ultrafast
      choice and native account support for the selected model. If you relied on Fast
      or Auto upgrading automatically, select Ultrafast in the picker or with /fast
      ultrafast . See the shared speed controls .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: The model picker retains the provider you selected even when providers
      share a model ID, and the CLI catches misspelled thinking levels before saving
      an agent job. To remove a thinking override, use --clear-thinking ; a blank
      value does not clear it.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Support feedback and selection checkpoints, corrected JSON or schema answers,
      successive pauses and explicit cancellation. The installed Lobster runtime owns
      saved progress and validation. #162003 Thanks @miguelbranco80 , @Patrick-Erichsen
      and @Alix-007 .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Visitor access lists and revocation use the current verified GitHub identity
      to avoid matching someone else with the same handle. Explicit email selection
      takes priority, with exact-email fallback when identity is missing or ambiguous.
      #160497 . Thanks @shakkernerd .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Import needs a reachable source and copies text, leaving native files and
      native-tool resumption with the source. Large conversations retain only the
      newest portion within provider and import limits, with incomplete copies reported.
      Use consistent source-home selection to avoid duplicate copies; identical items
      without stable IDs can be skipped once the import window fills.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Hidden native child agents can use separate managed Git checkouts and report
      back without adding persistent sidebar sessions. Keeping a child retains its
      checkout; deleting it saves a snapshot first. These options do not support ACP
      or hidden cloud placement.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Organizing chats keeps the list in step with your actions. Custom groups
      survive /new and /reset , marking a chat read does not move it up the list,
      and confirmed Archive, Restore or Undo appears immediately. Sidebar Reset restores
      Display settings as well as Filters, and titles drop outdated decorations when
      the profile or connection changes.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Opening and navigating long chats requires less repeated download, history
      and layout work, while keeping your reading position and Stop available. After
      a restart, normal agent preparation shows Starting up and loads chat and sidebar
      data when ready. Reconnect bursts prioritize establishing connections, so initial
      session lists can take longer. Older tabs whose retained files were pruned need
      to reload. Restricted container deployments need a repaired image installed
      or built to apply the whole-UI 503 repair.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Conversation controls preserve other agents' replies and queued work when
      short session keys overlap. Files, images and usage reports stay with the selected
      conversation, and clearing export search restores the sidebar. See session controls
      .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 20-interface-experience-changes-in-v2026-10-1
  source_release: openclaw-2026-10-10-v2026-10-1-d64e4e93
  source_type: openclaw_changelog
  theme: interface-experience
  title: 20 Interface Experience changes in v2026.10.1
  type: change
related_changes:
- '[[Changes/OpenHands/2026-10-08-test-e2e-open-commits-from-the-tabs-pane-s-own-menu-by-enyst-in-https-github-com|test(e2e):
  open Commits from the tabs pane''s own menu]]'
- '[[Changes/Claude Code/2026-10-09-improved-fullscreen-mode-the-link-under-the-mouse-pointer-is-now-underlined-to-s|Improved
  fullscreen mode]]'
- '[[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface
  Experience changes in v0.12.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|openclaw-2026-10-10-v2026-10-1-d64e4e93]]'
source_type: openclaw_changelog
theme: interface-experience
title: 20 Interface Experience changes in v2026.10.1
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Interface Experience changes in v2026.10.1

**OpenClaw** · 2026-10-10 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.1) · from [[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App panels fill the available space in fullscreen and split layouts, and transparent apps that follow the host theme match light and dark dashboards. File views update after edits, and dashboard content reflects accepted board changes.

> You can snooze an eligible conversation in the web Control UI to clear it from the Active sidebar while its work continues. Find it in Snoozed or All and wake it yourself, or let it return at the chosen time or earlier after interaction, completion or pinning. Archived, child and protected conversations are excluded.

> Nested board links and removable, reorderable sidebar pins make boards easier to reach. #164604 . Thanks @steipete .

> The Online sidebar lets you focus on people with running work and sort by presence, running work, open-chat count or name. These choices are temporary, and counts cover accessible open chats.

> Sidebar pencil markers help you find saved drafts after reload or in a fresh tab, including attachments, replies and goals. Queued messages show an image preview, and their attachments leave the composer without clearing newer input. Incognito is excluded; without browser storage, drafts stay only in the current tab, and changes do not sync live to already-open tabs.

> Consecutive updates from the same outside conversation share a compact row you can expand to read the original messages, times and available source links. Search and reply navigation open the relevant messages for you.

> Agent identity editing brings related fields together and adds a searchable emoji picker alongside direct entry. Text and emoji avatars appear larger when starting chat, and name or avatar changes show the latest saved result. Clearing a saved emoji remains unsupported. If you still use an unmigrated browser-wide avatar, set each agent's avatar again in Overview under Identity.

> Quiet Hours keeps its time window and timezone together, with a menu for choosing the zone. Saved aliases remain available, but you cannot type an unsaved zone missing from the browser's catalog. Some browsers offer only the local zone, UTC and the saved zone.

> The experimental native Mac sidebar adds groups, colors and owners to help you organize conversations and find the one you need. You can copy transcripts or links and open a selected conversation in another window. Group defaults can start new conversations in selected folders or eligible separate Git working copies; editor shortcuts need a local working copy.

> You can load older conversations for the selected agent and search names, details and messages from the Mac sidebar. Search combines immediate local matches with Gateway results and explains when indexing or archived transcripts leave results incomplete. View options remembers your filters, grouping and display choices for each Gateway profile.

> Expandable follow-up trees and Pages across agents keep related conversations within reach. Hover over or keyboard-focus a conversation to preview available people, workspace and progress details without opening it. Pull-request cards identify last-known status when a refresh fails. The Mac chat guide covers navigation and keyboard access.

> You can choose Ultrafast on supported embedded OpenAI Responses routes with an API-key profile or a direct key. Codex requires an explicit Ultrafast choice and native account support for the selected model. If you relied on Fast or Auto upgrading automatically, select Ultrafast in the picker or with /fast ultrafast . See the shared speed controls .

> The model picker retains the provider you selected even when providers share a model ID, and the CLI catches misspelled thinking levels before saving an agent job. To remove a thinking override, use --clear-thinking ; a blank value does not clear it.

> Support feedback and selection checkpoints, corrected JSON or schema answers, successive pauses and explicit cancellation. The installed Lobster runtime owns saved progress and validation. #162003 Thanks @miguelbranco80 , @Patrick-Erichsen and @Alix-007 .

> Visitor access lists and revocation use the current verified GitHub identity to avoid matching someone else with the same handle. Explicit email selection takes priority, with exact-email fallback when identity is missing or ambiguous. #160497 . Thanks @shakkernerd .

> Import needs a reachable source and copies text, leaving native files and native-tool resumption with the source. Large conversations retain only the newest portion within provider and import limits, with incomplete copies reported. Use consistent source-home selection to avoid duplicate copies; identical items without stable IDs can be skipped once the import window fills.

> Hidden native child agents can use separate managed Git checkouts and report back without adding persistent sidebar sessions. Keeping a child retains its checkout; deleting it saves a snapshot first. These options do not support ACP or hidden cloud placement.

> Organizing chats keeps the list in step with your actions. Custom groups survive /new and /reset , marking a chat read does not move it up the list, and confirmed Archive, Restore or Undo appears immediately. Sidebar Reset restores Display settings as well as Filters, and titles drop outdated decorations when the profile or connection changes.

> Opening and navigating long chats requires less repeated download, history and layout work, while keeping your reading position and Stop available. After a restart, normal agent preparation shows Starting up and loads chat and sidebar data when ready. Reconnect bursts prioritize establishing connections, so initial session lists can take longer. Older tabs whose retained files were pruned need to reload. Restricted container deployments need a repaired image installed or built to apply the whole-UI 503 repair.

> Conversation controls preserve other agents' replies and queued work when short session keys overlap. Files, images and usage reports stay with the selected conversation, and clearing export search restores the sidebar. See session controls .

Source: https://docs.openclaw.ai/releases/2026.10.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-10-2-reliability-and-performance-changes-in-v2026-10-1|2 Reliability and Performance changes in v2026.10.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1|13 Memory and Personalization changes in v2026.10.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-10-96-apps-and-integrations-changes-in-v2026-10-1|96 Apps and Integrations changes in v2026.10.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-10-15-mobile-and-desktop-changes-in-v2026-10-1|15 Mobile and Desktop changes in v2026.10.1]] · Mobile and Desktop
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
- [[Changes/OpenClaw/2026-10-10-10-automation-and-scheduling-changes-in-v2026-10-1|10 Automation and Scheduling changes in v2026.10.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-10-112-other-changes-in-v2026-10-1|112 other changes in v2026.10.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-10-10 · Open WebUI · [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]]
- Later: 2026-10-12 · Google Antigravity · [[Changes/Google Antigravity/2026-10-12-3-interface-experience-changes-in-hub-v2-23-0-permissions-picker|3 Interface Experience changes in HUB v2.23.0 — Permissions picker…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-10-f98adc&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-10-20-interface-experience-changes-in-v2026-10-1.md%0ACard%20ID%3A%20openclaw-2026-10-10-f98adc%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->