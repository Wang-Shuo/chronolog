---
card_id: open-webui-2026-10-10-a52a12
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Agent Mode: 7 changes in v0.12.0 — \U0001FAE5
  **Temporary chats leave no sub-agent chats.** Temporary chats no longer offer the
  model…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1192
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 15c4d8b18b26e19ec9efa780d10b419200e6667380b78a96bca30127d92ec36e
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-a52a12
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 7 Agent Mode changes'
  evidence:
  - quote: "\U0001FAE5 **Temporary chats leave no sub-agent chats.** Temporary chats
      no longer offer the model sub-agents or timers, whose conversations were saved
      on the server although a temporary chat should leave nothing behind. [#31573](https://github.com/open-webui/open-webui/pull/31573),
      [#31567](https://github.com/open-webui/open-webui/issues/31567)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6D1 **Sub-agent results after a role change.** A chat now only
      continues with a finished sub-agent's result while its owner still has an active
      role, the same check timers already make, so a deactivated or pending account
      no longer keeps generating replies. [#31451](https://github.com/open-webui/open-webui/pull/31451)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FA83 **Background replies show up live.** When a background sub-agent
      finishes or a timer goes off, its result and the model's follow-up reply now
      appear in the open chat right away, where they only showed after a page reload.
      [#31576](https://github.com/open-webui/open-webui/pull/31576), [#31566](https://github.com/open-webui/open-webui/issues/31566)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F33F **One branch with background sub-agents.** When a background
      sub-agent finishes while the answer that started it is still being written,
      its report now follows that answer, where the chat switched to another branch
      that hid the latest question and answer and the model replied without seeing
      them. [#31557](https://github.com/open-webui/open-webui/pull/31557), [#31507](https://github.com/open-webui/open-webui/issues/31507)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F30D **Attach Webpage user agent.** Attaching a webpage now sends
      the configured \"USER_AGENT\" from the first request, so sites such as Wikipedia
      that block the default agent no longer fail with 403 Forbidden. [#30385](https://github.com/open-webui/open-webui/pull/30385),
      [#29617](https://github.com/open-webui/open-webui/issues/29617)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5C2️ **Sub-agents in folder chats.** Sub-agents started from a
      chat in a folder with knowledge attached are now limited to that folder's knowledge
      like the chat itself, where they could list and search every knowledge base
      you can read. [#31574](https://github.com/open-webui/open-webui/pull/31574),
      [#31569](https://github.com/open-webui/open-webui/issues/31569)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F502 **Sub-agents and timers without repeated instructions.** Sub-agents,
      timers and the replies that follow a background sub-agent's result now rebuild
      their instructions from the original chat, where they reused the chat's finished
      system prompt, so the model received its system prompt, skills, knowledge list
      and tool and terminal instructions twice. Skills mentioned in the original message
      and the chat's variables now carry over as well. [#31568](https://github.com/open-webui/open-webui/issues/31568),
      [Commit](https://github.com/open-webui/open-webui/commit/ecbbff8afb3537d5e799e434a61a1134a97c6362)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-agent-mode-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: agent-mode
  title: 7 Agent Mode changes in v0.12.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-09-3-agent-mode-changes-in-v2-1-296|3 Agent Mode
  changes in v2.1.296]]'
- '[[Changes/Devin/2026-10-09-org-level-agent-capabilities|Org-level Agent capabilities]]'
- '[[Changes/Devin/2026-10-09-repository-agents-md-loaded-on-setup|Repository AGENTS.md
  loaded on setup]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: agent-mode
title: 7 Agent Mode changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Agent Mode changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🫥 **Temporary chats leave no sub-agent chats.** Temporary chats no longer offer the model sub-agents or timers, whose conversations were saved on the server although a temporary chat should leave nothing behind. [#31573](https://github.com/open-webui/open-webui/pull/31573), [#31567](https://github.com/open-webui/open-webui/issues/31567)

> 🛑 **Sub-agent results after a role change.** A chat now only continues with a finished sub-agent's result while its owner still has an active role, the same check timers already make, so a deactivated or pending account no longer keeps generating replies. [#31451](https://github.com/open-webui/open-webui/pull/31451)

> 🪃 **Background replies show up live.** When a background sub-agent finishes or a timer goes off, its result and the model's follow-up reply now appear in the open chat right away, where they only showed after a page reload. [#31576](https://github.com/open-webui/open-webui/pull/31576), [#31566](https://github.com/open-webui/open-webui/issues/31566)

> 🌿 **One branch with background sub-agents.** When a background sub-agent finishes while the answer that started it is still being written, its report now follows that answer, where the chat switched to another branch that hid the latest question and answer and the model replied without seeing them. [#31557](https://github.com/open-webui/open-webui/pull/31557), [#31507](https://github.com/open-webui/open-webui/issues/31507)

> 🌍 **Attach Webpage user agent.** Attaching a webpage now sends the configured "USER_AGENT" from the first request, so sites such as Wikipedia that block the default agent no longer fail with 403 Forbidden. [#30385](https://github.com/open-webui/open-webui/pull/30385), [#29617](https://github.com/open-webui/open-webui/issues/29617)

> 🗂️ **Sub-agents in folder chats.** Sub-agents started from a chat in a folder with knowledge attached are now limited to that folder's knowledge like the chat itself, where they could list and search every knowledge base you can read. [#31574](https://github.com/open-webui/open-webui/pull/31574), [#31569](https://github.com/open-webui/open-webui/issues/31569)

> 🔂 **Sub-agents and timers without repeated instructions.** Sub-agents, timers and the replies that follow a background sub-agent's result now rebuild their instructions from the original chat, where they reused the chat's finished system prompt, so the model received its system prompt, skills, knowledge list and tool and terminal instructions twice. Skills mentioned in the original message and the chat's variables now carry over as well. [#31568](https://github.com/open-webui/open-webui/issues/31568), [Commit](https://github.com/open-webui/open-webui/commit/ecbbff8afb3537d5e799e434a61a1134a97c6362)

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
- [[Changes/Open WebUI/2026-10-10-5-context-window-changes-in-v0-12-0|5 Context Window changes in v0.12.0]] · Context Window
- [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]] · Interface Experience
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-09 · Devin · [[Changes/Devin/2026-10-09-repository-agents-md-loaded-on-setup|Repository AGENTS.md loaded on setup]]
- Later: 2026-10-10 · OpenClaw · [[Changes/OpenClaw/2026-10-10-27-agent-mode-changes-in-v2026-10-1|27 Agent Mode changes in v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-a52a12&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-7-agent-mode-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-a52a12%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->