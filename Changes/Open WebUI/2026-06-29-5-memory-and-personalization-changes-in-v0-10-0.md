---
card_id: open-webui-2026-06-29-0909ae
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Memory and Personalization: 5 changes in v0.10.0
  — \U0001F9E0 **Reworked memory system.** Memory has been overhauled with distinct
  memory…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1075
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: feb7eeac33ee01f751c7fc28d2aa486c2baf802b6a2c5946ec46da04b3ca9b4b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-0909ae
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 5 Memory and Personalization changes'
  evidence:
  - quote: "\U0001F9E0 **Reworked memory system.** Memory has been overhauled with
      distinct memory types — long-lived personal memories and per-conversation context
      — managed through a structured add, update, and delete flow, giving models a
      more reliable way to remember and apply what they've learned about you. [Commit](https://github.com/open-webui/open-webui/commit/dbdcfd8c6080c284024052a482e589de226dbf05),
      [Commit](https://github.com/open-webui/open-webui/commit/7e13fd7ad19c28ba34502bde6c709665f7a6808c),
      [Commit](https://github.com/open-webui/open-webui/commit/2560533c1a8a2b2a0f7b47becf3703031053ad30),
      [Commit](https://github.com/open-webui/open-webui/commit/8977a10a2b1e150393635dc5c24e59660d0f2da9),
      [Commit](https://github.com/open-webui/open-webui/commit/260f3c3a22c55f15ca8f06c5314b23f2a9eb1739),
      [Commit](https://github.com/open-webui/open-webui/commit/b0487dd6dd942a757828a25aba92e9feef685275),
      [Commit](https://github.com/open-webui/open-webui/commit/a285a390c12e27e614d1ba9ffb92d1a0e49e7dfa),
      [Commit](https://github.com/open-webui/open-webui/commit/70e4ffcc6526c1bc90dbfdc0287283574b12c18b),
      [Commit](https://github.com/open-webui/open-webui/commit/2c4e1fce8f40b0cb5028f1afcb184b6e58c33041),
      [Commit](https://github.com/open-webui/open-webui/commit/c7e634776d7e77556d149b6cc884ed64363648a9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F7E2 **Loaded-model indicator for llama.cpp.** Models served through
      llama.cpp now report whether they're currently loaded in memory, including the
      sleeping state, so the loaded indicator works for them too. [Commit](https://github.com/open-webui/open-webui/commit/b696c5deff15d4c85c84c5bac244f062b1bc879a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F9E0 **Memory toggle follows the server default.** When a user hasn't
      set their own memory preference, it now follows the admin's global memory setting
      instead of defaulting to off. [#25909](https://github.com/open-webui/open-webui/pull/25909)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F3AF **Ejecting a workspace model unloads the right model.** Unloading
      a workspace model now resolves to its underlying base model, so the correct
      model is freed from memory. [Commit](https://github.com/open-webui/open-webui/commit/464e703e4716812d015966582152ddd8a2c71572),
      [#26269](https://github.com/open-webui/open-webui/pull/26269)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F393 **Several features are no longer beta.** Memories, Notes, Channels,
      and High Contrast Mode have graduated out of beta and no longer carry a beta
      label. [Commit](https://github.com/open-webui/open-webui/commit/7b55a63fc7ee323e9114713ce1d2f3f688aa37e6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-memory-and-personalization-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: memory
  title: 5 Memory and Personalization changes in v0.10.0
  type: change
related_changes:
- '[[Changes/Cursor/2026-06-18-you-can-now-delete-memory-files-in-the-ui-or-prompt-your-automation-to-delete-ou|Delete
  memory files in the UI, or prompt your automation to delete outdated memories…]]'
- '[[Changes/Claude Code/2026-06-22-improved-memory-the-agent-is-now-reminded-to-compact-its-memory-md-index-when-ne|Improved
  memory: the agent is now reminded to compact its MEMORY.md index…]]'
- '[[Changes/Kimi Code/2026-06-24-read-large-text-files-in-bounded-memory-and-read-tail-lines-without-scanning-who|Read
  large text files in bounded memory and read tail lines without scanning whole files]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: memory
title: 5 Memory and Personalization changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Memory and Personalization changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧠 **Reworked memory system.** Memory has been overhauled with distinct memory types — long-lived personal memories and per-conversation context — managed through a structured add, update, and delete flow, giving models a more reliable way to remember and apply what they've learned about you. [Commit](https://github.com/open-webui/open-webui/commit/dbdcfd8c6080c284024052a482e589de226dbf05), [Commit](https://github.com/open-webui/open-webui/commit/7e13fd7ad19c28ba34502bde6c709665f7a6808c), [Commit](https://github.com/open-webui/open-webui/commit/2560533c1a8a2b2a0f7b47becf3703031053ad30), [Commit](https://github.com/open-webui/open-webui/commit/8977a10a2b1e150393635dc5c24e59660d0f2da9), [Commit](https://github.com/open-webui/open-webui/commit/260f3c3a22c55f15ca8f06c5314b23f2a9eb1739), [Commit](https://github.com/open-webui/open-webui/commit/b0487dd6dd942a757828a25aba92e9feef685275), [Commit](https://github.com/open-webui/open-webui/commit/a285a390c12e27e614d1ba9ffb92d1a0e49e7dfa), [Commit](https://github.com/open-webui/open-webui/commit/70e4ffcc6526c1bc90dbfdc0287283574b12c18b), [Commit](https://github.com/open-webui/open-webui/commit/2c4e1fce8f40b0cb5028f1afcb184b6e58c33041), [Commit](https://github.com/open-webui/open-webui/commit/c7e634776d7e77556d149b6cc884ed64363648a9)

> 🟢 **Loaded-model indicator for llama.cpp.** Models served through llama.cpp now report whether they're currently loaded in memory, including the sleeping state, so the loaded indicator works for them too. [Commit](https://github.com/open-webui/open-webui/commit/b696c5deff15d4c85c84c5bac244f062b1bc879a)

> 🧠 **Memory toggle follows the server default.** When a user hasn't set their own memory preference, it now follows the admin's global memory setting instead of defaulting to off. [#25909](https://github.com/open-webui/open-webui/pull/25909)

> 🎯 **Ejecting a workspace model unloads the right model.** Unloading a workspace model now resolves to its underlying base model, so the correct model is freed from memory. [Commit](https://github.com/open-webui/open-webui/commit/464e703e4716812d015966582152ddd8a2c71572), [#26269](https://github.com/open-webui/open-webui/pull/26269)

> 🎓 **Several features are no longer beta.** Memories, Notes, Channels, and High Contrast Mode have graduated out of beta and no longer carry a beta label. [Commit](https://github.com/open-webui/open-webui/commit/7b55a63fc7ee323e9114713ce1d2f3f688aa37e6)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-29-5-files-and-data-changes-in-v0-10-0|5 Files and Data changes in v0.10.0]] · Files and Data
- [[Changes/Open WebUI/2026-06-29-3-voice-and-audio-changes-in-v0-10-0|3 Voice and Audio changes in v0.10.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-29-14-interface-experience-changes-in-v0-10-0|14 Interface Experience changes in v0.10.0]] · Interface Experience
- [[Changes/Open WebUI/2026-06-29-4-collaboration-changes-in-v0-10-0|4 Collaboration changes in v0.10.0]] · Collaboration
- [[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|🪪 Client User-Agent forwarded to model backends. The browser's User-Agent is now…]] · Agent Mode
- [[Changes/Open WebUI/2026-06-29-scim-sync-can-t-demote-an-admin-a-scim-provisioning-sync-that-marks-a-user-inact|🛟 SCIM sync can't demote an admin. A SCIM provisioning sync that marks a user…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-29-8-search-and-browsing-changes-in-v0-10-0|8 Search and Browsing changes in v0.10.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-29-25-model-support-changes-in-v0-10-0|25 Model Support changes in v0.10.0]] · Model Support
- [[Changes/Open WebUI/2026-06-29-6-reliability-and-performance-changes-in-v0-10-0|6 Reliability and Performance changes in v0.10.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-29-4-mobile-and-desktop-changes-in-v0-10-0|4 Mobile and Desktop changes in v0.10.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-29-better-screen-reader-labels-on-toggles-integration-and-switch-toggles-now-expose|♿ Better screen-reader labels on toggles. Integration and switch toggles now…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-29-16-safety-and-privacy-changes-in-v0-10-0|16 Safety and Privacy changes in v0.10.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-29-2-pricing-model-changes-in-v0-10-0|2 Pricing Model changes in v0.10.0]] · Pricing Model
- [[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-29-9-account-and-access-changes-in-v0-10-0|9 Account and Access changes in v0.10.0]] · Account and Access
- [[Changes/Open WebUI/2026-06-29-usable-chat-input-on-mobile-with-many-tools-when-skills-tools-terminal-web-searc|📱 Usable chat input on mobile with many tools. When skills, tools, terminal, web…]] · Image Generation
- [[Changes/Open WebUI/2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0|6 Automation and Scheduling changes in v0.10.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-29-3-context-window-changes-in-v0-10-0|3 Context Window changes in v0.10.0]] · Context Window
- [[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer Workflow changes in v0.10.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-29-10-editor-experience-changes-in-v0-10-0|10 Editor Experience changes in v0.10.0]] · Editor Experience
- [[Changes/Open WebUI/2026-06-29-29-other-changes-in-v0-10-0|29 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-06-24 · Kimi Code · [[Changes/Kimi Code/2026-06-24-read-large-text-files-in-bounded-memory-and-read-tail-lines-without-scanning-who|Read large text files in bounded memory and read tail lines without scanning whole files]]
- Later: 2026-06-30 · OpenClaw · [[Changes/OpenClaw/2026-06-30-26-memory-and-personalization-changes-in-v2026-6-11|26 Memory and Personalization changes in v2026.6.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-0909ae&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-5-memory-and-personalization-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-0909ae%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->