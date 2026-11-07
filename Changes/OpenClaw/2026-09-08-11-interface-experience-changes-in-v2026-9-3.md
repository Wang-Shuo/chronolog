---
card_id: openclaw-2026-09-08-d11d38
date: '2026-09-08'
description: 'OpenClaw · 2026-09-08 · Interface Experience: 11 changes in v2026.9.3
  — Failed steer or redirect attempts restore their text and attachments without…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2704
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6a0d8e207348621da5e6a872cb7550a37e121bc93b6f3315ed061d6c4b976928
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-08-d11d38
  comparison: ''
  date: '2026-09-08'
  description: 'OpenClaw — v2026.9.3: 11 Interface Experience changes'
  evidence:
  - quote: Failed steer or redirect attempts restore their text and attachments without
      overwriting a newer draft, and delayed rewind completion preserves newer text,
      attachments and Goal mode. Documents attached during an active run retain extracted
      text and supported rendered pages, while uploaded images remain visible as a
      new workspace finishes loading.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Dashboards keep a themed loading presentation until their widgets are ready,
      and loaded dashboards retain notes, scroll position and chat drafts across navigation
      and Settings within the existing per-pane cache. Moving to another Gateway or
      user clears that cache.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Phone-width and embedded settings keep usable navigation, and Gateway switching
      shows the destinations clearly. Saved unavailable execution-device bindings
      stay visibly selected as unavailable, rather than implying that another device
      was chosen. Profile headers show the connected person's identity when known.
      Devices also supports editable aliases, and remote configuration-file opens
      confirm that the file opened on the Gateway host. Unsaved device-alias edits
      are dismissed on reconnect.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: The command palette keeps chat-search failures visible alongside usable
      navigation and catalog results, and model results follow the selected agent's
      current catalog. Model entries take you to Models rather than silently selecting
      one. Model-picker search stays applied through refresh, with Escape clearing
      the query before closing.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Long updates retain their progress watcher until completion, and update
      history keeps terminal failures, restart outcomes and current update availability
      distinct. Abandoned records can be recovered without stopping a healthy matching
      Gateway when no post-update work remains, with conservative checks for active
      drivers and explicit recovery for records lacking driver identity.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Matrix leaves archived state out of active-account selection and Doctor
      scans. Explicit replies keep their selected quoted message inside the intended
      thread, and wording-only edits avoid repeating mention alerts when the required
      history can be read.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Android keeps content clear of separating hinges, and on suitable book
      folds it keeps navigation beside the content. In tabletop posture, the conversation
      sits above the fold and the composer below it, with the layout falling back
      when the available panes are too small.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Local and CLI-backed model views now preserve the selected agent and canonical
      provider, and managed Codex conversations use a newly selected model on subsequent
      turns. Native-owned sessions retain their own selection rules.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Direct agent-hook callers can opt in to waitForCompletion and receive bounded
      status that distinguishes a reply, intentional silence and delivery outcomes.
      The completion response contains status rather than the model’s response text.
      The default remains acknowledgement of admission, and mapped or fan-out calls
      keep that existing behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Links opened in the Mac app now appear as native WebKit tabs in the Browser
      panel, replacing the separate link sidebar. They stay with that window when
      you switch conversations, with a URL bar, navigation controls and the option
      to open the page in your default browser.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Workboard can refresh pinned navigation names without discarding an open
      card draft, while Logbook timestamps stay clear of the activity stripe.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 11-interface-experience-changes-in-v2026-9-3
  source_release: openclaw-2026-09-08-v2026-9-3-dfcfef48
  source_type: openclaw_changelog
  theme: interface-experience
  title: 11 Interface Experience changes in v2026.9.3
  type: change
related_changes:
- '[[Changes/Lovable/2026-09-04-new-ways-to-open-project-settings|New ways to open
  project settings]]'
- '[[Changes/OpenClaw/2026-09-05-21-interface-experience-changes-in-v2026-9-2|21 Interface
  Experience changes in v2026.9.2]]'
- '[[Changes/ChatGPT/2026-09-08-edit-and-comment-on-mobile-open-a-generated-image-full-screen-to-edit-it-or-add|Edit
  and comment]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|openclaw-2026-09-08-v2026-9-3-dfcfef48]]'
source_type: openclaw_changelog
theme: interface-experience
title: 11 Interface Experience changes in v2026.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Interface Experience changes in v2026.9.3

**OpenClaw** · 2026-09-08 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.3) · from [[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Failed steer or redirect attempts restore their text and attachments without overwriting a newer draft, and delayed rewind completion preserves newer text, attachments and Goal mode. Documents attached during an active run retain extracted text and supported rendered pages, while uploaded images remain visible as a new workspace finishes loading.

> Dashboards keep a themed loading presentation until their widgets are ready, and loaded dashboards retain notes, scroll position and chat drafts across navigation and Settings within the existing per-pane cache. Moving to another Gateway or user clears that cache.

> Phone-width and embedded settings keep usable navigation, and Gateway switching shows the destinations clearly. Saved unavailable execution-device bindings stay visibly selected as unavailable, rather than implying that another device was chosen. Profile headers show the connected person's identity when known. Devices also supports editable aliases, and remote configuration-file opens confirm that the file opened on the Gateway host. Unsaved device-alias edits are dismissed on reconnect.

> The command palette keeps chat-search failures visible alongside usable navigation and catalog results, and model results follow the selected agent's current catalog. Model entries take you to Models rather than silently selecting one. Model-picker search stays applied through refresh, with Escape clearing the query before closing.

> Long updates retain their progress watcher until completion, and update history keeps terminal failures, restart outcomes and current update availability distinct. Abandoned records can be recovered without stopping a healthy matching Gateway when no post-update work remains, with conservative checks for active drivers and explicit recovery for records lacking driver identity.

> Matrix leaves archived state out of active-account selection and Doctor scans. Explicit replies keep their selected quoted message inside the intended thread, and wording-only edits avoid repeating mention alerts when the required history can be read.

> Android keeps content clear of separating hinges, and on suitable book folds it keeps navigation beside the content. In tabletop posture, the conversation sits above the fold and the composer below it, with the layout falling back when the available panes are too small.

> Local and CLI-backed model views now preserve the selected agent and canonical provider, and managed Codex conversations use a newly selected model on subsequent turns. Native-owned sessions retain their own selection rules.

> Direct agent-hook callers can opt in to waitForCompletion and receive bounded status that distinguishes a reply, intentional silence and delivery outcomes. The completion response contains status rather than the model’s response text. The default remains acknowledgement of admission, and mapped or fan-out calls keep that existing behavior.

> Links opened in the Mac app now appear as native WebKit tabs in the Browser panel, replacing the separate link sidebar. They stay with that window when you switch conversations, with a URL bar, navigation controls and the option to open the page in your default browser.

> Workboard can refresh pinned navigation names without discarding an open card draft, while Logbook timestamps stay clear of the activity stripe.

Source: https://docs.openclaw.ai/releases/2026.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-08-7-automation-and-scheduling-changes-in-v2026-9-3|7 Automation and Scheduling changes in v2026.9.3]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-08-10-memory-and-personalization-changes-in-v2026-9-3|10 Memory and Personalization changes in v2026.9.3]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-08-2-files-and-data-changes-in-v2026-9-3|2 Files and Data changes in v2026.9.3]] · Files and Data
- [[Changes/OpenClaw/2026-09-08-12-context-window-changes-in-v2026-9-3|12 Context Window changes in v2026.9.3]] · Context Window
- [[Changes/OpenClaw/2026-09-08-23-apps-and-integrations-changes-in-v2026-9-3|23 Apps and Integrations changes in v2026.9.3]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-08-ordinary-model-changes-now-apply-to-the-current-chat-by-default-including-admini|Ordinary model changes now apply to the current chat by default, including…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-08-10-mobile-and-desktop-changes-in-v2026-9-3|10 Mobile and Desktop changes in v2026.9.3]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-08-4-reliability-and-performance-changes-in-v2026-9-3|4 Reliability and Performance changes in v2026.9.3]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-08-provider-adapters-preserve-initial-anthropic-text-and-thinking-keep-images-with|Provider adapters preserve initial Anthropic text and thinking, keep images…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-08-8-editor-experience-changes-in-v2026-9-3|8 Editor Experience changes in v2026.9.3]] · Editor Experience
- [[Changes/OpenClaw/2026-09-08-8-voice-and-audio-changes-in-v2026-9-3|8 Voice and Audio changes in v2026.9.3]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-08-15-model-support-changes-in-v2026-9-3|15 Model Support changes in v2026.9.3]] · Model Support
- [[Changes/OpenClaw/2026-09-08-3-search-and-browsing-changes-in-v2026-9-3|3 Search and Browsing changes in v2026.9.3]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-08-16-agent-mode-changes-in-v2026-9-3|16 Agent Mode changes in v2026.9.3]] · Agent Mode
- [[Changes/OpenClaw/2026-09-08-slack-delivers-valid-structured-sections-intact-even-when-their-accessibility-te|Slack delivers valid structured sections intact even when their accessibility text…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-08-4-collaboration-changes-in-v2026-9-3|4 Collaboration changes in v2026.9.3]] · Collaboration
- [[Changes/OpenClaw/2026-09-08-14-safety-and-privacy-changes-in-v2026-9-3|14 Safety and Privacy changes in v2026.9.3]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-08-4-pricing-model-changes-in-v2026-9-3|4 Pricing Model changes in v2026.9.3]] · Pricing Model
- [[Changes/OpenClaw/2026-09-08-8-account-and-access-changes-in-v2026-9-3|8 Account and Access changes in v2026.9.3]] · Account and Access
- [[Changes/OpenClaw/2026-09-08-22-developer-workflow-changes-in-v2026-9-3|22 Developer Workflow changes in v2026.9.3]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-08-77-other-changes-in-v2026-9-3|77 other changes in v2026.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-09-08 · ChatGPT · [[Changes/ChatGPT/2026-09-08-edit-and-comment-on-mobile-open-a-generated-image-full-screen-to-edit-it-or-add|Edit and comment]]
- Later: 2026-09-09 · Claude Code · [[Changes/Claude Code/2026-09-09-improved-the-diff-panel-it-no-longer-flashes-0-files-changed-and-a-spinner-befor|Improved the /diff panel]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-08-d11d38&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-08-11-interface-experience-changes-in-v2026-9-3.md%0ACard%20ID%3A%20openclaw-2026-09-08-d11d38%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->