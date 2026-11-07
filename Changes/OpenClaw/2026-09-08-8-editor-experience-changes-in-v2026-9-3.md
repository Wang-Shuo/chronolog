---
card_id: openclaw-2026-09-08-609ce2
date: '2026-09-08'
description: 'OpenClaw · 2026-09-08 · Editor Experience: 8 changes in v2026.9.3 —
  Completed Swarms retain their child counts after cleanup and reload, with fully
  successful…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2858
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a4194b125e3bf5aaf7ffd2d3f151311c906d0990dc382f2146b412859991cc43
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-08-609ce2
  comparison: ''
  date: '2026-09-08'
  description: 'OpenClaw — v2026.9.3: 8 Editor Experience changes'
  evidence:
  - quote: Completed Swarms retain their child counts after cleanup and reload, with
      fully successful groups collapsing into expandable rows. Child completion still
      does not mean the parent's final synthesis has been delivered.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Review keeps delayed results attached to the latest selected task or file,
      and activity rows preserve readable labels without presenting edit-operation
      totals as checkout diffs. Reopened chats refresh their pending approvals rather
      than reusing an old set.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Panels retain their loaded data during connection interruptions and refresh
      when the connection returns, with offline and restart status in the footer.
      Suspended tabs can recover missed update notices while keeping their route and
      stored draft; unsaved settings still need to be saved or discarded before recovery.
      A tab already stranded by an earlier missed update may need one manual reload.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Supported same-origin text attachments can be read and selected directly
      in Files, with a literal UTF-8 preview up to 256 KiB. Unsupported or external
      documents remain download-only. File references with line ranges open at the
      first line, and leaving an agent-file preview through Edit restores focus to
      the editor.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Empty repositories explain that an initial commit is required, and placement
      failures keep their specific, readable diagnostics. Cancelled placement dialogs
      stay closed after delayed loading, while pending commands can show instructions
      before completion.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Configuration edits and Doctor repairs keep authored settings, explicit
      defaults and supported include-file ownership intact. An eligible nested change
      is written into the fragment that owns it, while unsafe shared-file or mixed-array
      changes remain refused rather than being flattened into a different configuration.
      Failed prefix recovery preserves the original file, and audit history retains
      the writer label supplied with a change.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Other conversations can save edits while cleanup checks a database's integrity.
      Deletion still waits for the complete verification.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Slow-operation logs distinguish queue, work and completion delays and identify
      the process or worker that emitted them. Connection diagnostics retain close
      causes, duration, local ping-write state and last-pong age, helping operators
      distinguish observations without treating a completed local write as proof that
      the remote side received it.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 8-editor-experience-changes-in-v2026-9-3
  source_release: openclaw-2026-09-08-v2026-9-3-dfcfef48
  source_type: openclaw_changelog
  theme: editor-experience
  title: 8 Editor Experience changes in v2026.9.3
  type: change
related_changes:
- '[[Changes/OpenCode/2026-09-04-core-send-the-session-id-as-github-copilot-s-interaction-header-to-improve-reque|Core
  Send the session ID as GitHub Copilot''s interaction header to improve request…]]'
- '[[Changes/OpenClaw/2026-09-05-8-editor-experience-changes-in-v2026-9-2|8 Editor
  Experience changes in v2026.9.2]]'
- '[[Changes/Lovable/2026-09-08-project-files-no-longer-copy-automatically-during-a-remix|Project
  files no longer copy automatically during a remix]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|openclaw-2026-09-08-v2026-9-3-dfcfef48]]'
source_type: openclaw_changelog
theme: editor-experience
title: 8 Editor Experience changes in v2026.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Editor Experience changes in v2026.9.3

**OpenClaw** · 2026-09-08 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.3) · from [[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Completed Swarms retain their child counts after cleanup and reload, with fully successful groups collapsing into expandable rows. Child completion still does not mean the parent's final synthesis has been delivered.

> Review keeps delayed results attached to the latest selected task or file, and activity rows preserve readable labels without presenting edit-operation totals as checkout diffs. Reopened chats refresh their pending approvals rather than reusing an old set.

> Panels retain their loaded data during connection interruptions and refresh when the connection returns, with offline and restart status in the footer. Suspended tabs can recover missed update notices while keeping their route and stored draft; unsaved settings still need to be saved or discarded before recovery. A tab already stranded by an earlier missed update may need one manual reload.

> Supported same-origin text attachments can be read and selected directly in Files, with a literal UTF-8 preview up to 256 KiB. Unsupported or external documents remain download-only. File references with line ranges open at the first line, and leaving an agent-file preview through Edit restores focus to the editor.

> Empty repositories explain that an initial commit is required, and placement failures keep their specific, readable diagnostics. Cancelled placement dialogs stay closed after delayed loading, while pending commands can show instructions before completion.

> Configuration edits and Doctor repairs keep authored settings, explicit defaults and supported include-file ownership intact. An eligible nested change is written into the fragment that owns it, while unsafe shared-file or mixed-array changes remain refused rather than being flattened into a different configuration. Failed prefix recovery preserves the original file, and audit history retains the writer label supplied with a change.

> Other conversations can save edits while cleanup checks a database's integrity. Deletion still waits for the complete verification.

> Slow-operation logs distinguish queue, work and completion delays and identify the process or worker that emitted them. Connection diagnostics retain close causes, duration, local ping-write state and last-pong age, helping operators distinguish observations without treating a completed local write as proof that the remote side received it.

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
- [[Changes/OpenClaw/2026-09-08-8-voice-and-audio-changes-in-v2026-9-3|8 Voice and Audio changes in v2026.9.3]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-08-15-model-support-changes-in-v2026-9-3|15 Model Support changes in v2026.9.3]] · Model Support
- [[Changes/OpenClaw/2026-09-08-3-search-and-browsing-changes-in-v2026-9-3|3 Search and Browsing changes in v2026.9.3]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-08-16-agent-mode-changes-in-v2026-9-3|16 Agent Mode changes in v2026.9.3]] · Agent Mode
- [[Changes/OpenClaw/2026-09-08-11-interface-experience-changes-in-v2026-9-3|11 Interface Experience changes in v2026.9.3]] · Interface Experience
- [[Changes/OpenClaw/2026-09-08-slack-delivers-valid-structured-sections-intact-even-when-their-accessibility-te|Slack delivers valid structured sections intact even when their accessibility text…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-08-4-collaboration-changes-in-v2026-9-3|4 Collaboration changes in v2026.9.3]] · Collaboration
- [[Changes/OpenClaw/2026-09-08-14-safety-and-privacy-changes-in-v2026-9-3|14 Safety and Privacy changes in v2026.9.3]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-08-4-pricing-model-changes-in-v2026-9-3|4 Pricing Model changes in v2026.9.3]] · Pricing Model
- [[Changes/OpenClaw/2026-09-08-8-account-and-access-changes-in-v2026-9-3|8 Account and Access changes in v2026.9.3]] · Account and Access
- [[Changes/OpenClaw/2026-09-08-22-developer-workflow-changes-in-v2026-9-3|22 Developer Workflow changes in v2026.9.3]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-08-77-other-changes-in-v2026-9-3|77 other changes in v2026.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-09-08 · Lovable · [[Changes/Lovable/2026-09-08-project-files-no-longer-copy-automatically-during-a-remix|Project files no longer copy automatically during a remix]]
- Later: 2026-09-08 · Raycast · [[Changes/Raycast/2026-09-08-window-management-added-create-layout-from-current-windows-command-allowing-for|Window Management : Added Create Layout From Current Windows command allowing…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-08-609ce2&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-08-8-editor-experience-changes-in-v2026-9-3.md%0ACard%20ID%3A%20openclaw-2026-09-08-609ce2%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->