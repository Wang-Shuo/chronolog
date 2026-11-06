---
card_id: open-webui-2026-08-25-7c76fe
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Context Window: 4 changes in v0.11.1 — \U0001F9F7
  **Replies not carried into the next turn.** With providers that skip parts of the
  streaming…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1209
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 62db251c968f66d054cad311953666888cf0b8bed096a0fc21a1275b89aaa5f9
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-7c76fe
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 4 Context Window changes'
  evidence:
  - quote: "\U0001F9F7 **Replies not carried into the next turn.** With providers
      that skip parts of the streaming sequence, the finished reply is now taken from
      the completed message, so it stays available as context for your next question
      and the citations that arrived with it are no longer dropped. [#28310](https://github.com/open-webui/open-webui/pull/28310)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F233 **Conversations compacted too early on llama.cpp.** A conversation
      served by llama.cpp is no longer shortened at roughly half the size you configured,
      where its cached input was counted twice, so a chat showing 39,000 tokens was
      treated as 77,000 against a 70,000 limit. [#28590](https://github.com/open-webui/open-webui/issues/28590),
      [Commit](https://github.com/open-webui/open-webui/commit/0b27fa5e873c9f3cff7b14e4eeab8321bdd8970c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F529 **A new chat shown as nearly full.** The indicator of how full
      a conversation is now counts tokens the same way the shortening does, where
      the two read different figures from providers that report both and a fresh chat
      could appear close to its limit. [#27620](https://github.com/open-webui/open-webui/pull/27620),
      [#27608](https://github.com/open-webui/open-webui/issues/27608), [Commit](https://github.com/open-webui/open-webui/commit/978d2572140e4fe31ebbc33274f699c71b8cdc29)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F47B **Messages disappearing from a conversation.** Two things saving
      the same conversation at once no longer discard each other's changes, where
      a message could vanish from the screen while still counting toward the model's
      context and a file attached during a reply was lost on the next save. [Commit](https://github.com/open-webui/open-webui/commit/1c13fedb16e74c5888c52ccd928a5eb5bbb1068d),
      [#28742](https://github.com/open-webui/open-webui/issues/28742)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-context-window-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: context-window
  title: 4 Context Window changes in v0.11.1
  type: change
related_changes:
- '[[Changes/Replit/2026-08-21-start-with-conversations|Start with Conversations]]'
- '[[Changes/Dify/2026-08-25-8-context-window-changes-in-1-17-0|8 Context Window changes
  in 1.17.0]]'
- '[[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-19239-update-clear-command-docs-to-include-context-reset-by|SSR
  Agent Issue Fix (19239): Update /clear command docs to include context reset]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: context-window
title: 4 Context Window changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Context Window changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧷 **Replies not carried into the next turn.** With providers that skip parts of the streaming sequence, the finished reply is now taken from the completed message, so it stays available as context for your next question and the citations that arrived with it are no longer dropped. [#28310](https://github.com/open-webui/open-webui/pull/28310)

> 🈳 **Conversations compacted too early on llama.cpp.** A conversation served by llama.cpp is no longer shortened at roughly half the size you configured, where its cached input was counted twice, so a chat showing 39,000 tokens was treated as 77,000 against a 70,000 limit. [#28590](https://github.com/open-webui/open-webui/issues/28590), [Commit](https://github.com/open-webui/open-webui/commit/0b27fa5e873c9f3cff7b14e4eeab8321bdd8970c)

> 🔩 **A new chat shown as nearly full.** The indicator of how full a conversation is now counts tokens the same way the shortening does, where the two read different figures from providers that report both and a fresh chat could appear close to its limit. [#27620](https://github.com/open-webui/open-webui/pull/27620), [#27608](https://github.com/open-webui/open-webui/issues/27608), [Commit](https://github.com/open-webui/open-webui/commit/978d2572140e4fe31ebbc33274f699c71b8cdc29)

> 👻 **Messages disappearing from a conversation.** Two things saving the same conversation at once no longer discard each other's changes, where a message could vanish from the screen while still counting toward the model's context and a file attached during a reply was lost on the next save. [Commit](https://github.com/open-webui/open-webui/commit/1c13fedb16e74c5888c52ccd928a5eb5bbb1068d), [#28742](https://github.com/open-webui/open-webui/issues/28742)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-25-9-files-and-data-changes-in-v0-11-1|9 Files and Data changes in v0.11.1]] · Files and Data
- [[Changes/Open WebUI/2026-08-25-image-generation-and-web-search-staying-switched-off-turning-either-off-now-take|🎨 Image generation and web search staying switched off. Turning either off now…]] · Image Generation
- [[Changes/Open WebUI/2026-08-25-7-safety-and-privacy-changes-in-v0-11-1|7 Safety and Privacy changes in v0.11.1]] · Safety and Privacy
- [[Changes/Open WebUI/2026-08-25-improved-ui-accessibility-a-closed-sidebar-is-no-longer-reachable-by-keyboard-or|♿ Improved UI accessibility. A closed sidebar is no longer reachable by keyboard…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-08-25-2-pricing-model-changes-in-v0-11-1|2 Pricing Model changes in v0.11.1]] · Pricing Model
- [[Changes/Open WebUI/2026-08-25-11-automation-and-scheduling-changes-in-v0-11-1|11 Automation and Scheduling changes in v0.11.1]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-08-25-10-reliability-and-performance-changes-in-v0-11-1|10 Reliability and Performance changes in v0.11.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-08-25-6-collaboration-changes-in-v0-11-1|6 Collaboration changes in v0.11.1]] · Collaboration
- [[Changes/Open WebUI/2026-08-25-13-account-and-access-changes-in-v0-11-1|13 Account and Access changes in v0.11.1]] · Account and Access
- [[Changes/Open WebUI/2026-08-25-starting-up-on-windows-the-windows-start-script-now-creates-the-secret-key-it-ne|🪟 Starting up on Windows. The Windows start script now creates the secret key…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-08-25-2-multimodal-input-changes-in-v0-11-1|2 Multimodal Input changes in v0.11.1]] · Multimodal Input
- [[Changes/Open WebUI/2026-08-25-12-editor-experience-changes-in-v0-11-1|12 Editor Experience changes in v0.11.1]] · Editor Experience
- [[Changes/Open WebUI/2026-08-25-4-apps-and-integrations-changes-in-v0-11-1|4 Apps and Integrations changes in v0.11.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-08-25-73-developer-workflow-changes-in-v0-11-1|73 Developer Workflow changes in v0.11.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-08-25-8-memory-and-personalization-changes-in-v0-11-1|8 Memory and Personalization changes in v0.11.1]] · Memory and Personalization
- [[Changes/Open WebUI/2026-08-25-files-for-delegated-tasks-a-task-handed-to-a-sub-agent-can-now-carry-the-attachm|🤝 Files for delegated tasks. A task handed to a sub-agent can now carry…]] · Agent Mode
- [[Changes/Open WebUI/2026-08-25-4-enterprise-and-administration-changes-in-v0-11-1|4 Enterprise and Administration changes in v0.11.1]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-08-25-24-interface-experience-changes-in-v0-11-1|24 Interface Experience changes in v0.11.1]] · Interface Experience
- [[Changes/Open WebUI/2026-08-25-5-search-and-browsing-changes-in-v0-11-1|5 Search and Browsing changes in v0.11.1]] · Search and Browsing
- [[Changes/Open WebUI/2026-08-25-4-voice-and-audio-changes-in-v0-11-1|4 Voice and Audio changes in v0.11.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-08-25-56-model-support-changes-in-v0-11-1|56 Model Support changes in v0.11.1]] · Model Support
- [[Changes/Open WebUI/2026-08-25-39-other-changes-in-v0-11-1|39 other changes in v0.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-08-25 · Gemini CLI · [[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-19239-update-clear-command-docs-to-include-context-reset-by|SSR Agent Issue Fix (19239): Update /clear command docs to include context reset]]
- Later: 2026-08-26 · Claude Code · [[Changes/Claude Code/2026-08-26-changed-sonnet-5-s-default-auto-compact-window-to-its-full-1m-context-so-session|Changed Sonnet 5's default auto-compact window to its full 1M context, so sessions…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-7c76fe&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-4-context-window-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-7c76fe%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->