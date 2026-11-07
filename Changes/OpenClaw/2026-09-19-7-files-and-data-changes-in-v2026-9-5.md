---
card_id: openclaw-2026-09-19-bbe0e5
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Files and Data: 7 changes in v2026.9.5 — Markdown
  attachments open as formatted documents beside the conversation, with headings…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode
    offset]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2558
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7e8abc25bb9ae3a780ad76b7350ebbb7aafbb8a8c909f8165b2f759dddb0642f
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-bbe0e5
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 7 Files and Data changes'
  evidence:
  - quote: Markdown attachments open as formatted documents beside the conversation,
      with headings, tables, and working code controls. Chat menus can copy available
      message Markdown, complete code, tables ready for a spreadsheet, or an attachment’s
      download link or name. New generated images stay with their completion reply
      without adding a duplicate image-only message. Uploaded image frames now align
      with their prompts, including in Safari, and user image galleries sit closer
      to the text that explains them.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Keep several chat files open in tabs and switch between them without losing
      your reading position. HTML files offer Preview and Source , and reopened editable
      drafts can save or resolve conflicts directly from Preview. Strict mode keeps
      document scripts disabled and applies the guarded preview’s resource restrictions.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Requests already submitted may finish. Cancellation does not recall delivered
      messages or files, undo accepted changes, or stop remote tasks already accepted.
      A file upload alone also does not establish delivery to a conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Image and PDF inspection, along with local generation references, now follow
      the active task's worktree and relative directory. A screenshot created in that
      checkout can be read without moving it to the agent's default workspace. Local
      media access still respects approved roots and symlink boundaries, and sandboxed
      tools retain their filesystem isolation.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Canceling PDF extraction no longer aborts Node through the repaired PNG-compression
      initialization failure. Cancellation during that encoding step waits for it
      and the worker to finish; rendering remains immediately cancellable. A stuck
      protected native operation can still delay cancellation beyond the task deadline.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Preparing Feishu documents with several tables or longer cell text needs
      less local processing while preserving table widths and Unicode text. Smaller
      inputs and some batches may not benefit, and Feishu network requests are unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: PDF access now follows media and OpenClaw group restrictions, so an explicit
      PDF allow cannot override a conflicting group deny. Narrow that deny if PDF
      access is intended. Doctor also stops copying LINE direct-message senders into
      group permissions. Review existing groupAllowFrom entries if you ran an earlier
      repair, since previously copied entries remain in place.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 7-files-and-data-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: file-data
  title: 7 Files and Data changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Claude/2026-09-16-create-designs-decks-and-docs-in-any-conversation|Create
  designs, decks, and docs in any conversation]]'
- '[[Changes/OpenHands/2026-09-16-feat-track-authenticated-canvas-arrivals-by-neubig-in-https-github-com-openhands|feat:
  track authenticated Canvas arrivals]]'
- '[[Changes/Claude Code/2026-09-17-claude-tag-removed-the-repeated-guest-attribution-note-claude-appended-to-a-slac|Claude
  Tag Removed the repeated guest-attribution note Claude appended to a Slack…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: file-data
title: 7 Files and Data changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Files and Data changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Markdown attachments open as formatted documents beside the conversation, with headings, tables, and working code controls. Chat menus can copy available message Markdown, complete code, tables ready for a spreadsheet, or an attachment’s download link or name. New generated images stay with their completion reply without adding a duplicate image-only message. Uploaded image frames now align with their prompts, including in Safari, and user image galleries sit closer to the text that explains them.

> Keep several chat files open in tabs and switch between them without losing your reading position. HTML files offer Preview and Source , and reopened editable drafts can save or resolve conflicts directly from Preview. Strict mode keeps document scripts disabled and applies the guarded preview’s resource restrictions.

> Requests already submitted may finish. Cancellation does not recall delivered messages or files, undo accepted changes, or stop remote tasks already accepted. A file upload alone also does not establish delivery to a conversation.

> Image and PDF inspection, along with local generation references, now follow the active task's worktree and relative directory. A screenshot created in that checkout can be read without moving it to the agent's default workspace. Local media access still respects approved roots and symlink boundaries, and sandboxed tools retain their filesystem isolation.

> Canceling PDF extraction no longer aborts Node through the repaired PNG-compression initialization failure. Cancellation during that encoding step waits for it and the worker to finish; rendering remains immediately cancellable. A stuck protected native operation can still delay cancellation beyond the task deadline.

> Preparing Feishu documents with several tables or longer cell text needs less local processing while preserving table widths and Unicode text. Smaller inputs and some batches may not benefit, and Feishu network requests are unchanged.

> PDF access now follows media and OpenClaw group restrictions, so an explicit PDF allow cannot override a conflicting group deny. Narrow that deny if PDF access is intended. Doctor also stops copying LINE direct-message senders into group permissions. Review existing groupAllowFrom entries if you ran an earlier repair, since previously copied entries remain in place.

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
- [[Changes/OpenClaw/2026-09-19-15-voice-and-audio-changes-in-v2026-9-5|15 Voice and Audio changes in v2026.9.5]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-19-shared-helpers-consolidate-repeated-implementation-including-preparation-and-res|Shared helpers consolidate repeated implementation, including preparation…]] · Video Generation
- [[Changes/OpenClaw/2026-09-19-171-other-changes-in-v2026-9-5|171 other changes in v2026.9.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-claude-tag-removed-the-repeated-guest-attribution-note-claude-appended-to-a-slac|Claude Tag Removed the repeated guest-attribution note Claude appended to a Slack…]]
- Later: 2026-09-21 · Open WebUI · [[Changes/Open WebUI/2026-09-21-10-files-and-data-changes-in-v0-11-4|10 Files and Data changes in v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode offset]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-bbe0e5&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-7-files-and-data-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-bbe0e5%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->