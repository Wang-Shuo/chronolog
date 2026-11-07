---
card_id: openclaw-2026-09-03-268a3b
date: '2026-09-03'
description: 'OpenClaw · 2026-09-03 · Collaboration: 7 changes in v2026.9.1 — Skills
  are becoming something a team can own without turning the host into a ticket queue…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create
    a team here: (source link)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2792
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 33543aedfae85926d433b5c3fdc6216b42d326418a39972017fa32f2fc5ef532
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-03-268a3b
  comparison: ''
  date: '2026-09-03'
  description: 'OpenClaw — v2026.9.1: 7 Collaboration changes'
  evidence:
  - quote: Skills are becoming something a team can own without turning the host into
      a ticket queue. People sharing a Gateway can keep their own libraries, share
      work deliberately, and carry the exact selected revision into the session that
      needs it, while overwrites, policy failures, and optional runtime dependencies
      leave clearer recovery paths.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Signed-in teammates on a shared Gateway can create, import, update, and
      reuse skills without host access. A library starts private, sharing does not
      hand over edit rights, and ownership can move to a team when the skill itself
      becomes shared work, so routine authoring no longer has to pass through an administrator.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The real library distinguishes private, shared, and team-owned Harbor skills.
      Published 2026.9.1 interface with fictional Harbor data; no live task execution.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Long-running Codex work no longer ends just because its progress is quiet,
      and finite time limits follow elapsed time without throwing away useful partial
      output. Idle Codex chats can resume while other chats and catalog reads share
      the same app server, and prompt-hook changes either take effect safely on the
      next persistent turn or stop before inference with a recovery path instead of
      silently keeping stale instructions.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: First-party catalog entries use artwork already bundled with OpenClaw when
      it is available, avoiding fallback letter tiles and unnecessary remote icon
      requests when the CDN is blocked, while third-party artwork retains the authenticated
      proxy path. The Workshop tab also lines up with the shared Plugins content column
      on wide screens without changing its narrow layout.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Managed worktrees can now live on another chosen disk or folder without
      moving the rest of OpenClaw's state, and existing worktrees keep using the locations
      already recorded for them. This release first raised the shared checkout target
      to 100, then removed the hard admission ceiling entirely, so sufficient disk
      space governs new worktrees and restores while 100 remains the automatic cleanup
      target. Manual and protected worktrees keep their existing safeguards.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Removed or replaced sessions no longer leave an obsolete observer scheduling
      utility-model work that cannot be saved. A subagent settlement wake that reaches
      its deadline also cancels the exact accepted run and releases the requester's
      single-concurrency lane, letting later messages continue instead of piling up
      behind stale retries. That cancellation is scoped to settlement wakes and the
      shared direct-announcement deadline path.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 7-collaboration-changes-in-v2026-9-1
  source_release: openclaw-2026-09-03-v2026-9-1-281124fc
  source_type: openclaw_changelog
  theme: collaboration
  title: 7 Collaboration changes in v2026.9.1
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-01-4-collaboration-changes-in-v2026-8-2|4 Collaboration
  changes in v2026.8.2]]'
- '[[Changes/ChatGPT/2026-09-03-eligible-site-owners-can-now-share-a-live-chatgpt-site-with-named-people-outside|Share
  Sites with people outside your workspace]]'
- '[[Changes/Codex CLI/2026-09-03-6-collaboration-changes-in-rust-v0-153-0|6 Collaboration
  changes in rust-v0.153.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|openclaw-2026-09-03-v2026-9-1-281124fc]]'
source_type: openclaw_changelog
theme: collaboration
title: 7 Collaboration changes in v2026.9.1
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Collaboration changes in v2026.9.1

**OpenClaw** · 2026-09-03 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.1) · from [[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|v2026.9.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Skills are becoming something a team can own without turning the host into a ticket queue. People sharing a Gateway can keep their own libraries, share work deliberately, and carry the exact selected revision into the session that needs it, while overwrites, policy failures, and optional runtime dependencies leave clearer recovery paths.

> Signed-in teammates on a shared Gateway can create, import, update, and reuse skills without host access. A library starts private, sharing does not hand over edit rights, and ownership can move to a team when the skill itself becomes shared work, so routine authoring no longer has to pass through an administrator.

> The real library distinguishes private, shared, and team-owned Harbor skills. Published 2026.9.1 interface with fictional Harbor data; no live task execution.

> Long-running Codex work no longer ends just because its progress is quiet, and finite time limits follow elapsed time without throwing away useful partial output. Idle Codex chats can resume while other chats and catalog reads share the same app server, and prompt-hook changes either take effect safely on the next persistent turn or stop before inference with a recovery path instead of silently keeping stale instructions.

> First-party catalog entries use artwork already bundled with OpenClaw when it is available, avoiding fallback letter tiles and unnecessary remote icon requests when the CDN is blocked, while third-party artwork retains the authenticated proxy path. The Workshop tab also lines up with the shared Plugins content column on wide screens without changing its narrow layout.

> Managed worktrees can now live on another chosen disk or folder without moving the rest of OpenClaw's state, and existing worktrees keep using the locations already recorded for them. This release first raised the shared checkout target to 100, then removed the hard admission ceiling entirely, so sufficient disk space governs new worktrees and restores while 100 remains the automatic cleanup target. Manual and protected worktrees keep their existing safeguards.

> Removed or replaced sessions no longer leave an obsolete observer scheduling utility-model work that cannot be saved. A subagent settlement wake that reaches its deadline also cancels the exact accepted run and releases the requester's single-concurrency lane, letting later messages continue instead of piling up behind stale retries. That cancellation is scoped to settlement wakes and the shared direct-announcement deadline path.

Source: https://docs.openclaw.ai/releases/2026.9.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-03-14-agent-mode-changes-in-v2026-9-1|14 Agent Mode changes in v2026.9.1]] · Agent Mode
- [[Changes/OpenClaw/2026-09-03-12-voice-and-audio-changes-in-v2026-9-1|12 Voice and Audio changes in v2026.9.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-03-2-files-and-data-changes-in-v2026-9-1|2 Files and Data changes in v2026.9.1]] · Files and Data
- [[Changes/OpenClaw/2026-09-03-10-mobile-and-desktop-changes-in-v2026-9-1|10 Mobile and Desktop changes in v2026.9.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-03-19-memory-and-personalization-changes-in-v2026-9-1|19 Memory and Personalization changes in v2026.9.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-03-3-editor-experience-changes-in-v2026-9-1|3 Editor Experience changes in v2026.9.1]] · Editor Experience
- [[Changes/OpenClaw/2026-09-03-2-search-and-browsing-changes-in-v2026-9-1|2 Search and Browsing changes in v2026.9.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-03-12-account-and-access-changes-in-v2026-9-1|12 Account and Access changes in v2026.9.1]] · Account and Access
- [[Changes/OpenClaw/2026-09-03-several-less-visible-repairs-keep-the-apps-from-failing-around-dependencies-and|Several less visible repairs keep the apps from failing around dependencies…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-03-13-automation-and-scheduling-changes-in-v2026-9-1|13 Automation and Scheduling changes in v2026.9.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-03-an-update-or-doctor-repair-now-does-more-to-preserve-the-setup-you-already-autho|An update or Doctor repair now does more to preserve the setup you already authored…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-03-11-developer-workflow-changes-in-v2026-9-1|11 Developer Workflow changes in v2026.9.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-03-3-accessibility-and-localization-changes-in-v2026-9-1|3 Accessibility and Localization changes in v2026.9.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-03-26-apps-and-integrations-changes-in-v2026-9-1|26 Apps and Integrations changes in v2026.9.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-03-10-safety-and-privacy-changes-in-v2026-9-1|10 Safety and Privacy changes in v2026.9.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-03-11-context-window-changes-in-v2026-9-1|11 Context Window changes in v2026.9.1]] · Context Window
- [[Changes/OpenClaw/2026-09-03-12-model-support-changes-in-v2026-9-1|12 Model Support changes in v2026.9.1]] · Model Support
- [[Changes/OpenClaw/2026-09-03-14-interface-experience-changes-in-v2026-9-1|14 Interface Experience changes in v2026.9.1]] · Interface Experience
- [[Changes/OpenClaw/2026-09-03-on-linux-managed-local-model-and-embedding-services-are-preferred-as-the-out-of|On Linux, managed local model and embedding services are preferred…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-03-32-other-changes-in-v2026-9-1|32 other changes in v2026.9.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Collaboration

- Earlier: 2026-09-03 · Codex CLI · [[Changes/Codex CLI/2026-09-03-6-collaboration-changes-in-rust-v0-153-0|6 Collaboration changes in rust-v0.153.0]]
- Later: 2026-09-04 · Devin · [[Changes/Devin/2026-09-04-microsoft-teams-improvements|Microsoft Teams Improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-01-11 · Descript · [[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create a team here: (source link)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-03-268a3b&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-03-7-collaboration-changes-in-v2026-9-1.md%0ACard%20ID%3A%20openclaw-2026-09-03-268a3b%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->