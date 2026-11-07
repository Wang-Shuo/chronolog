---
card_id: open-webui-2025-12-02-e129c4
date: '2025-12-02'
description: "Open WebUI · 2025-12-02 · Interface Experience: 11 changes in v0.6.41
  — \U0001F4AC Direct Message channels were introduced with a dedicated channel type
  selector and…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1058
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7a1a59c72455cda201ddfdcc538f9c2181ce4f9c1539517897bd2264ae9a1a21
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-02-e129c4
  comparison: ''
  date: '2025-12-02'
  description: 'Open WebUI — v0.6.41: 11 Interface Experience changes'
  evidence:
  - quote: "\U0001F4AC Direct Message channels were introduced with a dedicated channel
      type selector and multi-user member selection interface, enabling private conversations
      between specific users without requiring full channel visibility. [Commit](https://github.com/open-webui/open-webui/commit/64b4d5d9c280b926746584aaf92b447d09deb386)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F648 Users can now hide Direct Message channels from their sidebar
      while preserving message history, with automatic reactivation when new messages
      arrive from other participants, providing a cleaner interface for managing active
      conversations. [Commit](https://github.com/open-webui/open-webui/commit/acccb9afdd557274d6296c70258bb897bbb6652f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: ☑️ A comprehensive user selection component was added to the channel creation
      modal, featuring search functionality, sortable user lists, pagination support,
      and multi-select checkboxes for building Direct Message participant lists. [Commit](https://github.com/open-webui/open-webui/commit/acccb9afdd557274d6296c70258bb897bbb6652f)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F534 Channel unread message count tracking was implemented with
      visual badge indicators in the sidebar, automatically updating counts in real-time
      and marking messages as read when users view channels, with join/leave functionality
      to manage membership status. [Commit](https://github.com/open-webui/open-webui/commit/64b4d5d9c280b926746584aaf92b447d09deb386)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F7E2 Direct Message channels now display an active status indicator
      for one-on-one conversations, showing a green dot when the other participant
      is currently online or a gray dot when offline. [Commit](https://github.com/open-webui/open-webui/commit/4b6773885cd7527c5a56b963781dac5e95105eec),
      [Commit](https://github.com/open-webui/open-webui/commit/39645102d14f34e71b34e5ddce0625790be33f6f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: ⚡ Channel messages now appear instantly when sent using optimistic UI rendering,
      displaying with a pending state while the server confirms delivery, providing
      a more responsive messaging experience. [Commit](https://github.com/open-webui/open-webui/commit/25994dd3da90600401f53596d4e4fb067c1b8eaa)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F4AD Users can now set a custom status with an emoji and message
      that displays in profile previews, the sidebar user menu, and Direct Message
      channel items in the sidebar, with the ability to clear status at any time,
      providing visibility into availability or current focus similar to team communication
      platforms. [Commit](https://github.com/open-webui/open-webui/commit/51621ba91a982e52da168ce823abffd11ad3e4fa),
      [Commit](https://github.com/open-webui/open-webui/commit/f5e8d4d5a004115489c35725408b057e24dfe318)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F441️ The admin user list now displays an active status indicator
      next to each user, showing a visual green dot for users who have been active
      within the last three minutes. [Commit](https://github.com/open-webui/open-webui/commit/1b095d12ff2465b83afa94af89ded9593f8a8655)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: "\U0001F5BC️ User profile image display in preview contexts was fixed by
      resolving a Pydantic validation error that prevented proper rendering. [Commit](https://github.com/open-webui/open-webui/commit/c7eb7136893b0ddfdc5d55ffc7a05bd84a00f5d6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: ⏳ Chat history infinite loading was prevented by enhancing message data
      structure to properly track parent message relationships, resolving issues where
      missing parentId fields caused perpetual loading states. [#19225](https://github.com/open-webui/open-webui/issues/19225),
      [Commit](https://github.com/open-webui/open-webui/commit/ff4b1b9862d15adfa15eac17d2ce066c3d8ae38f)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  - quote: ➖ The active user count indicator was removed from the bottom-left user
      menu in the sidebar to streamline the interface. [Commit](https://github.com/open-webui/open-webui/commit/848f3fd4d86ca66656e0ff0335773945af8d7d8d)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 11-interface-experience-changes-in-v0-6-41
  source_release: open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25
  source_type: github_releases
  theme: interface-experience
  title: 11 Interface Experience changes in v0.6.41
  type: change
related_changes:
- '[[Changes/Lovable/2025-11-26-navigation-update|Navigation update]]'
- '[[Changes/Cline/2025-12-02-4-interface-experience-changes-in-v3-39-0|4 Interface
  Experience changes in v3.39.0]]'
- '[[Changes/Codex CLI/2025-12-02-chore-dedup-unified-exec-waited-rendering-by-jif-oai-in-7256|chore:
  dedup unified exec "waited" rendering by @jif-oai in ♯7256]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25]]'
source_type: github_releases
theme: interface-experience
title: 11 Interface Experience changes in v0.6.41
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Interface Experience changes in v0.6.41

**Open WebUI** · 2025-12-02 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.41) · from [[Releases/Open WebUI/open-webui-2025-12-02-v0-6-41-github-266904152-3dfc9f25|v0.6.41]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 💬 Direct Message channels were introduced with a dedicated channel type selector and multi-user member selection interface, enabling private conversations between specific users without requiring full channel visibility. [Commit](https://github.com/open-webui/open-webui/commit/64b4d5d9c280b926746584aaf92b447d09deb386)

> 🙈 Users can now hide Direct Message channels from their sidebar while preserving message history, with automatic reactivation when new messages arrive from other participants, providing a cleaner interface for managing active conversations. [Commit](https://github.com/open-webui/open-webui/commit/acccb9afdd557274d6296c70258bb897bbb6652f)

> ☑️ A comprehensive user selection component was added to the channel creation modal, featuring search functionality, sortable user lists, pagination support, and multi-select checkboxes for building Direct Message participant lists. [Commit](https://github.com/open-webui/open-webui/commit/acccb9afdd557274d6296c70258bb897bbb6652f)

> 🔴 Channel unread message count tracking was implemented with visual badge indicators in the sidebar, automatically updating counts in real-time and marking messages as read when users view channels, with join/leave functionality to manage membership status. [Commit](https://github.com/open-webui/open-webui/commit/64b4d5d9c280b926746584aaf92b447d09deb386)

> 🟢 Direct Message channels now display an active status indicator for one-on-one conversations, showing a green dot when the other participant is currently online or a gray dot when offline. [Commit](https://github.com/open-webui/open-webui/commit/4b6773885cd7527c5a56b963781dac5e95105eec), [Commit](https://github.com/open-webui/open-webui/commit/39645102d14f34e71b34e5ddce0625790be33f6f)

> ⚡ Channel messages now appear instantly when sent using optimistic UI rendering, displaying with a pending state while the server confirms delivery, providing a more responsive messaging experience. [Commit](https://github.com/open-webui/open-webui/commit/25994dd3da90600401f53596d4e4fb067c1b8eaa)

> 💭 Users can now set a custom status with an emoji and message that displays in profile previews, the sidebar user menu, and Direct Message channel items in the sidebar, with the ability to clear status at any time, providing visibility into availability or current focus similar to team communication platforms. [Commit](https://github.com/open-webui/open-webui/commit/51621ba91a982e52da168ce823abffd11ad3e4fa), [Commit](https://github.com/open-webui/open-webui/commit/f5e8d4d5a004115489c35725408b057e24dfe318)

> 👁️ The admin user list now displays an active status indicator next to each user, showing a visual green dot for users who have been active within the last three minutes. [Commit](https://github.com/open-webui/open-webui/commit/1b095d12ff2465b83afa94af89ded9593f8a8655)

> 🖼️ User profile image display in preview contexts was fixed by resolving a Pydantic validation error that prevented proper rendering. [Commit](https://github.com/open-webui/open-webui/commit/c7eb7136893b0ddfdc5d55ffc7a05bd84a00f5d6)

> ⏳ Chat history infinite loading was prevented by enhancing message data structure to properly track parent message relationships, resolving issues where missing parentId fields caused perpetual loading states. [#19225](https://github.com/open-webui/open-webui/issues/19225), [Commit](https://github.com/open-webui/open-webui/commit/ff4b1b9862d15adfa15eac17d2ce066c3d8ae38f)

> ➖ The active user count indicator was removed from the bottom-left user menu in the sidebar to streamline the interface. [Commit](https://github.com/open-webui/open-webui/commit/848f3fd4d86ca66656e0ff0335773945af8d7d8d)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.41
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-02-group-channels-were-introduced-as-a-new-channel-type-enabling-membership-based-c|👥 Group channels were introduced as a new channel type enabling membership-based…]] · Collaboration
- [[Changes/Open WebUI/2025-12-02-web-search-domain-filtering-was-corrected-to-properly-block-results-when-any-res|🛡️ Web search domain filtering was corrected to properly block results when any…]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-02-tool-call-response-token-duplication-was-fixed-by-removing-redundant-message-his|🔄 Tool call response token duplication was fixed by removing redundant message…]] · Context Window
- [[Changes/Open WebUI/2025-12-02-7-account-and-access-changes-in-v0-6-41|7 Account and Access changes in v0.6.41]] · Account and Access
- [[Changes/Open WebUI/2025-12-02-13-developer-workflow-changes-in-v0-6-41|13 Developer Workflow changes in v0.6.41]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-02-4-reliability-and-performance-changes-in-v0-6-41|4 Reliability and Performance changes in v0.6.41]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-02-2-safety-and-privacy-changes-in-v0-6-41|2 Safety and Privacy changes in v0.6.41]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-02-the-model-editor-interface-was-refined-with-access-control-settings-moved-to-a-d|🎨 The model editor interface was refined with access control settings moved…]] · Editor Experience
- [[Changes/Open WebUI/2025-12-02-9-model-support-changes-in-v0-6-41|9 Model Support changes in v0.6.41]] · Model Support
- [[Changes/Open WebUI/2025-12-02-image-generation-in-temporary-chats-was-fixed-by-correctly-handling-local-chat-s|🎨 Image generation in temporary chats was fixed by correctly handling local chat…]] · Image Generation
- [[Changes/Open WebUI/2025-12-02-2-enterprise-and-administration-changes-in-v0-6-41|2 Enterprise and Administration changes in v0.6.41]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-02-sentencetransformers-embedding-initialization-was-fixed-by-updating-the-transfor|🐍 SentenceTransformers embedding initialization was fixed by updating…]] · Files and Data
- [[Changes/Open WebUI/2025-12-02-2-apps-and-integrations-changes-in-v0-6-41|2 Apps and Integrations changes in v0.6.41]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-02-13-other-changes-in-v0-6-41|13 other changes in v0.6.41]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2025-12-02 · Codex CLI · [[Changes/Codex CLI/2025-12-02-chore-dedup-unified-exec-waited-rendering-by-jif-oai-in-7256|chore: dedup unified exec "waited" rendering by @jif-oai in ♯7256]]
- Later: 2025-12-02 · v0 · [[Changes/v0/2025-12-02-you-can-now-access-project-settings-in-v0-using-the-in-chat-sidebar|Project Settings in the Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-02-e129c4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-02-11-interface-experience-changes-in-v0-6-41.md%0ACard%20ID%3A%20open-webui-2025-12-02-e129c4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.41%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->