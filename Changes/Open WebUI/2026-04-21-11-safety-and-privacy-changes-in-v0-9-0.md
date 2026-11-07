---
card_id: open-webui-2026-04-21-a50a64
date: '2026-04-21'
description: "Open WebUI · 2026-04-21 · Safety and Privacy: 11 changes in v0.9.0 —
  \U0001F3C3 **Faster knowledge access updates.** Updating access grants for knowledge
  items now…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1101
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a795a2a79ca8d2e2fb74896940daf1e8f03a571c8f024b1e5229bde9a60897f2
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-a50a64
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 11 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F3C3 **Faster knowledge access updates.** Updating access grants
      for knowledge items now completes with less backend overhead, making permission
      changes apply more quickly. [#23799](https://github.com/open-webui/open-webui/pull/23799)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6E1️ **Expanded security header controls.** Administrators can
      now configure additional browser security headers, including \"CONTENT_SECURITY_POLICY_REPORT_ONLY\",
      \"CROSS_ORIGIN_EMBEDDER_POLICY\", \"CROSS_ORIGIN_OPENER_POLICY\", and \"CROSS_ORIGIN_RESOURCE_POLICY\",
      for stricter and more flexible deployment hardening. [Commit](https://github.com/open-webui/open-webui/commit/f246a66810fa4995d9494da3599c0fb297fb0213)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F512 **Rendered content safety.** Placeholder descriptions and the
      pending account notice now render markdown with safer sanitization ordering,
      reducing the risk of unsafe HTML appearing in these views. [Commit](https://github.com/open-webui/open-webui/commit/253f416de3f2d3a939a6feef2a56413fd61cc70b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F510 **Channel sharing permission enforcement.** Channel creation
      and updates now enforce allowed access grant rules for public sharing, preventing
      unauthorized wildcard sharing on group channels. [#23638](https://github.com/open-webui/open-webui/pull/23638)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6C2 **Tool server access checks.** Tool listing now correctly awaits
      server access checks, preventing users from seeing server-backed tools they
      do not have permission to use. [Commit](https://github.com/open-webui/open-webui/commit/d40f31982be3eed37e55e3f67b1eea9a5dc8c525)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: ✍️ **Collaborative document write checks.** Collaborative document updates
      now require proper write permission before changes are accepted. [Commit](https://github.com/open-webui/open-webui/commit/638c7ab80216452910bdc59a19eb90e6b7244c6c),
      [Commit](https://github.com/open-webui/open-webui/commit/3271b013a8b30a882364679dcb40ffc9a89f037e),
      [#23624](https://github.com/open-webui/open-webui/pull/23624)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F465 **Private channel member list access.** Standard channel member
      lists now require proper read permission, preventing unauthorized users from
      enumerating members of private channels by direct API calls. [#23625](https://github.com/open-webui/open-webui/pull/23625)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F300 **Tool server schema recursion safety.** Tool server OpenAPI
      conversion now handles circular request schema references safely, preventing
      conversion crashes and ensuring one bad tool server spec does not break the
      full tool server list. [#23588](https://github.com/open-webui/open-webui/pull/23588),
      [Commit](https://github.com/open-webui/open-webui/commit/d3df8f1f372411314be9121fbf61d107939fa258)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F9ED **Permission-aware built-in tools.** Built-in tools now consistently
      respect user feature permissions for memories, web search, image generation,
      code interpreter, notes, channels, and automations, preventing tools from being
      exposed to users without access. [Commit](https://github.com/open-webui/open-webui/commit/588b81eedaacbfd7394b707ae1600d9fb729b809..674695918e5e3e1811314ce2a082c5bbb42d76b2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6AA **Channel access checks.** Channel actions now verify the current
      user when checking access, improving permission enforcement across channel views
      and message actions. [Commit](https://github.com/open-webui/open-webui/commit/4632f200a9ac98c915aee412b34e86c3d3c58bb1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F6E1️ **Note edit permission enforcement.** Note saving now requires
      write access instead of read access, preventing unauthorized users from modifying
      notes while preserving expected collaboration permissions. [Commit](https://github.com/open-webui/open-webui/commit/584a9a0920d8c8c72fc89ccbac83c970b5a4bd4a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 11-safety-and-privacy-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: safety-privacy
  title: 11 Safety and Privacy changes in v0.9.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-18-fixed-a-crash-in-the-permission-dialog-when-an-agent-teams-teammate-requested-to|Fixed
  a crash in the permission dialog when an agent teams teammate requested tool…]]'
- '[[Changes/Claude Code/2026-04-20-security-sandbox-auto-allow-no-longer-bypasses-the-dangerous-path-safety-check-f|Security:
  sandbox auto-allow no longer bypasses the dangerous-path safety check…]]'
- '[[Changes/Codex CLI/2026-04-20-9-safety-and-privacy-changes-in-rust-v0-122-0|9
  Safety and Privacy changes in rust-v0.122.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: safety-privacy
title: 11 Safety and Privacy changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Safety and Privacy changes in v0.9.0

**Open WebUI** · 2026-04-21 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🏃 **Faster knowledge access updates.** Updating access grants for knowledge items now completes with less backend overhead, making permission changes apply more quickly. [#23799](https://github.com/open-webui/open-webui/pull/23799)

> 🛡️ **Expanded security header controls.** Administrators can now configure additional browser security headers, including "CONTENT_SECURITY_POLICY_REPORT_ONLY", "CROSS_ORIGIN_EMBEDDER_POLICY", "CROSS_ORIGIN_OPENER_POLICY", and "CROSS_ORIGIN_RESOURCE_POLICY", for stricter and more flexible deployment hardening. [Commit](https://github.com/open-webui/open-webui/commit/f246a66810fa4995d9494da3599c0fb297fb0213)

> 🔒 **Rendered content safety.** Placeholder descriptions and the pending account notice now render markdown with safer sanitization ordering, reducing the risk of unsafe HTML appearing in these views. [Commit](https://github.com/open-webui/open-webui/commit/253f416de3f2d3a939a6feef2a56413fd61cc70b)

> 🔐 **Channel sharing permission enforcement.** Channel creation and updates now enforce allowed access grant rules for public sharing, preventing unauthorized wildcard sharing on group channels. [#23638](https://github.com/open-webui/open-webui/pull/23638)

> 🛂 **Tool server access checks.** Tool listing now correctly awaits server access checks, preventing users from seeing server-backed tools they do not have permission to use. [Commit](https://github.com/open-webui/open-webui/commit/d40f31982be3eed37e55e3f67b1eea9a5dc8c525)

> ✍️ **Collaborative document write checks.** Collaborative document updates now require proper write permission before changes are accepted. [Commit](https://github.com/open-webui/open-webui/commit/638c7ab80216452910bdc59a19eb90e6b7244c6c), [Commit](https://github.com/open-webui/open-webui/commit/3271b013a8b30a882364679dcb40ffc9a89f037e), [#23624](https://github.com/open-webui/open-webui/pull/23624)

> 👥 **Private channel member list access.** Standard channel member lists now require proper read permission, preventing unauthorized users from enumerating members of private channels by direct API calls. [#23625](https://github.com/open-webui/open-webui/pull/23625)

> 🌀 **Tool server schema recursion safety.** Tool server OpenAPI conversion now handles circular request schema references safely, preventing conversion crashes and ensuring one bad tool server spec does not break the full tool server list. [#23588](https://github.com/open-webui/open-webui/pull/23588), [Commit](https://github.com/open-webui/open-webui/commit/d3df8f1f372411314be9121fbf61d107939fa258)

> 🧭 **Permission-aware built-in tools.** Built-in tools now consistently respect user feature permissions for memories, web search, image generation, code interpreter, notes, channels, and automations, preventing tools from being exposed to users without access. [Commit](https://github.com/open-webui/open-webui/commit/588b81eedaacbfd7394b707ae1600d9fb729b809..674695918e5e3e1811314ce2a082c5bbb42d76b2)

> 🚪 **Channel access checks.** Channel actions now verify the current user when checking access, improving permission enforcement across channel views and message actions. [Commit](https://github.com/open-webui/open-webui/commit/4632f200a9ac98c915aee412b34e86c3d3c58bb1)

> 🛡️ **Note edit permission enforcement.** Note saving now requires write access instead of read access, preventing unauthorized users from modifying notes while preserving expected collaboration permissions. [Commit](https://github.com/open-webui/open-webui/commit/584a9a0920d8c8c72fc89ccbac83c970b5a4bd4a)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-3-files-and-data-changes-in-v0-9-0|3 Files and Data changes in v0.9.0]] · Files and Data
- [[Changes/Open WebUI/2026-04-21-4-image-generation-changes-in-v0-9-0|4 Image Generation changes in v0.9.0]] · Image Generation
- [[Changes/Open WebUI/2026-04-21-28-model-support-changes-in-v0-9-0|28 Model Support changes in v0.9.0]] · Model Support
- [[Changes/Open WebUI/2026-04-21-5-editor-experience-changes-in-v0-9-0|5 Editor Experience changes in v0.9.0]] · Editor Experience
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-8-context-window-changes-in-v0-9-0|8 Context Window changes in v0.9.0]] · Context Window
- [[Changes/Open WebUI/2026-04-21-24-reliability-and-performance-changes-in-v0-9-0|24 Reliability and Performance changes in v0.9.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-21-4-apps-and-integrations-changes-in-v0-9-0|4 Apps and Integrations changes in v0.9.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-21-46-developer-workflow-changes-in-v0-9-0|46 Developer Workflow changes in v0.9.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-04-21-8-automation-and-scheduling-changes-in-v0-9-0|8 Automation and Scheduling changes in v0.9.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-21-7-memory-and-personalization-changes-in-v0-9-0|7 Memory and Personalization changes in v0.9.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-21-2-mobile-and-desktop-changes-in-v0-9-0|2 Mobile and Desktop changes in v0.9.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-04-21-17-interface-experience-changes-in-v0-9-0|17 Interface Experience changes in v0.9.0]] · Interface Experience
- [[Changes/Open WebUI/2026-04-21-4-search-and-browsing-changes-in-v0-9-0|4 Search and Browsing changes in v0.9.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-04-21-shared-chat-access-controls-you-can-now-control-who-has-access-to-a-shared-chat|🔗 Shared chat access controls. You can now control who has access to a shared…]] · Collaboration
- [[Changes/Open WebUI/2026-04-21-4-voice-and-audio-changes-in-v0-9-0|4 Voice and Audio changes in v0.9.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-04-21-17-account-and-access-changes-in-v0-9-0|17 Account and Access changes in v0.9.0]] · Account and Access
- [[Changes/Open WebUI/2026-04-21-21-other-changes-in-v0-9-0|21 other changes in v0.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-20 · Codex CLI · [[Changes/Codex CLI/2026-04-20-9-safety-and-privacy-changes-in-rust-v0-122-0|9 Safety and Privacy changes in rust-v0.122.0]]
- Later: 2026-04-21 · OpenCode · [[Changes/OpenCode/2026-04-21-terminal-fixed-permission-replies-using-remote-workspaces-so-they-are-sent-to-th|Terminal Fixed permission replies using remote workspaces so they are sent…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-a50a64&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-11-safety-and-privacy-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-a50a64%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->