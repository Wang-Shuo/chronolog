---
card_id: open-webui-2026-10-10-89d137
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Context Window: 5 changes in v0.12.0 — \U0001F9E0
  **Compaction during long tool runs.** With context compaction on and native function…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1255
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 31129205c1200d869c6816ddd693e8e9f5903ed0b5909fb2df09ac742fcc2127
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-89d137
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 5 Context Window changes'
  evidence:
  - quote: "\U0001F9E0 **Compaction during long tool runs.** With context compaction
      on and native function calling, a reply that runs many tool calls in a row is
      now compacted between tool rounds once its context passes the token threshold,
      keeping each tool call together with its results and giving the summary the
      tool names and arguments, where compaction only ran before the reply started
      and a long tool run could grow past the model's context. [Commit](https://github.com/open-webui/open-webui/commit/67cfa917c12004d4e662d0f8879779b75ad6629a),
      [#27599](https://github.com/open-webui/open-webui/issues/27599)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FA99 **Input and output tokens in analytics.** Hovering, focusing
      or clicking the token total on the admin Analytics dashboard now shows how many
      of those tokens were input and how many were output. [Commit](https://github.com/open-webui/open-webui/commit/7e317fbada4acc5c48f326aa5935b3928275ea78),
      [#31646](https://github.com/open-webui/open-webui/issues/31646)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F41A **Prompt cache friendly terminal settings.** Open Terminal
      connections now have a Working Directory Context switch to leave the current
      folder out of the tool instructions, and a User Shell Tools option set to Always
      Include keeps the tools for your shell in the request while the shell is closed,
      so opening folders, reloading the page or losing the shell no longer change
      the start of the request and break the provider's prompt cache. [Commit](https://github.com/open-webui/open-webui/commit/a20b622ba808d46b28843e5d4ec0b996369f6a8b),
      [#32026](https://github.com/open-webui/open-webui/issues/32026), [#31590](https://github.com/open-webui/open-webui/issues/31590)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4CC **Attached files after context compaction.** With native function
      calling, files attached to a message now stay tied to that message after older
      messages are compacted and after a tool approval, where the model could be handed
      an older file's reference or none at all for a new upload. [Commit](https://github.com/open-webui/open-webui/commit/af6b82a18cc058b43ca1dc13ccf970f242e39a78),
      [#31411](https://github.com/open-webui/open-webui/issues/31411)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5DC️ **Images inside a chat no longer trigger compaction.** Images
      stored inside the chat itself, such as in chats from older versions or temporary
      chats, are no longer counted as text when estimating how full the context is,
      so a single image no longer pushes a chat over the compaction threshold or makes
      the context usage indicator jump. [#31915](https://github.com/open-webui/open-webui/pull/31915),
      [#31913](https://github.com/open-webui/open-webui/issues/31913)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-context-window-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: context-window
  title: 5 Context Window changes in v0.12.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-09-2-context-window-changes-in-v2-1-296|2 Context
  Window changes in v2.1.296]]'
- '[[Changes/GitHub Copilot CLI/2026-10-09-context-now-applies-to-new-and-resumed-acp-sessions-instead-of-silently-using-th|--context
  now applies to new and resumed ACP sessions instead of silently using…]]'
- '[[Changes/Replit/2026-10-09-work-across-projects-from-a-chat|Work across projects
  from a chat]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: context-window
title: 5 Context Window changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Context Window changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧠 **Compaction during long tool runs.** With context compaction on and native function calling, a reply that runs many tool calls in a row is now compacted between tool rounds once its context passes the token threshold, keeping each tool call together with its results and giving the summary the tool names and arguments, where compaction only ran before the reply started and a long tool run could grow past the model's context. [Commit](https://github.com/open-webui/open-webui/commit/67cfa917c12004d4e662d0f8879779b75ad6629a), [#27599](https://github.com/open-webui/open-webui/issues/27599)

> 🪙 **Input and output tokens in analytics.** Hovering, focusing or clicking the token total on the admin Analytics dashboard now shows how many of those tokens were input and how many were output. [Commit](https://github.com/open-webui/open-webui/commit/7e317fbada4acc5c48f326aa5935b3928275ea78), [#31646](https://github.com/open-webui/open-webui/issues/31646)

> 🐚 **Prompt cache friendly terminal settings.** Open Terminal connections now have a Working Directory Context switch to leave the current folder out of the tool instructions, and a User Shell Tools option set to Always Include keeps the tools for your shell in the request while the shell is closed, so opening folders, reloading the page or losing the shell no longer change the start of the request and break the provider's prompt cache. [Commit](https://github.com/open-webui/open-webui/commit/a20b622ba808d46b28843e5d4ec0b996369f6a8b), [#32026](https://github.com/open-webui/open-webui/issues/32026), [#31590](https://github.com/open-webui/open-webui/issues/31590)

> 📌 **Attached files after context compaction.** With native function calling, files attached to a message now stay tied to that message after older messages are compacted and after a tool approval, where the model could be handed an older file's reference or none at all for a new upload. [Commit](https://github.com/open-webui/open-webui/commit/af6b82a18cc058b43ca1dc13ccf970f242e39a78), [#31411](https://github.com/open-webui/open-webui/issues/31411)

> 🗜️ **Images inside a chat no longer trigger compaction.** Images stored inside the chat itself, such as in chats from older versions or temporary chats, are no longer counted as text when estimating how full the context is, so a single image no longer pushes a chat over the compaction threshold or makes the context usage indicator jump. [#31915](https://github.com/open-webui/open-webui/pull/31915), [#31913](https://github.com/open-webui/open-webui/issues/31913)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-reliability-and-performance-changes-in-v0-12-0|5 Reliability and Performance changes in v0.12.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5 Enterprise and Administration changes in v0.12.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-10-27-developer-workflow-changes-in-v0-12-0|27 Developer Workflow changes in v0.12.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-10-5-image-generation-changes-in-v0-12-0|5 Image Generation changes in v0.12.0]] · Image Generation
- [[Changes/Open WebUI/2026-10-10-49-model-support-changes-in-v0-12-0|49 Model Support changes in v0.12.0]] · Model Support
- [[Changes/Open WebUI/2026-10-10-19-account-and-access-changes-in-v0-12-0|19 Account and Access changes in v0.12.0]] · Account and Access
- [[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10 Automation and Scheduling changes in v0.12.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile and Desktop changes in v0.12.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-10-10-6-files-and-data-changes-in-v0-12-0|6 Files and Data changes in v0.12.0]] · Files and Data
- [[Changes/Open WebUI/2026-10-10-13-collaboration-changes-in-v0-12-0|13 Collaboration changes in v0.12.0]] · Collaboration
- [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]] · Interface Experience
- [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Agent Mode
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-10-09 · Replit · [[Changes/Replit/2026-10-09-work-across-projects-from-a-chat|Work across projects from a chat]]
- Later: 2026-10-13 · Cline · [[Changes/Cline/2026-10-13-2-context-window-changes-in-v4-1-24|2 Context Window changes in v4.1.24]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-89d137&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-5-context-window-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-89d137%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->