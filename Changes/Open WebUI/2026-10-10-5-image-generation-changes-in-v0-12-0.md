---
card_id: open-webui-2026-10-10-5c30dc
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Image Generation: 5 changes in v0.12.0 — \U0001F39B️
  **Redesigned model editor.** The model editor has a new layout: the background image
  now…"
diffusion:
  first_in_tracked: "[[Changes/Open WebUI/2024-03-10-dall-e-integration-introduced-dall-e-integration-for-image-generation-alongside|\U0001F3A8
    DALL-E Integration]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 944
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: image-generation
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 032535ee9ff808c9bbc516bacb85f3a79bedf569e9949d88464482b144485f53
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-5c30dc
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 5 Image Generation changes'
  evidence:
  - quote: "\U0001F39B️ **Redesigned model editor.** The model editor has a new layout:
      the background image now fills a banner at the top with the model's picture,
      name and ID set over it and buttons to add, change or remove it on hover, a
      long system prompt opens folded to a short preview with Show more, and Capabilities,
      Default Features, Builtin Tools, Knowledge, Tools, Skills, Filters, Actions,
      Prompts, Voice and Terminal each fold into one row that summarizes what is set,
      such as \"Web Search, Image Generation +2\", \"3 of 9 enabled\" or \"Custom
      · 4\", and opens into switches with descriptions or a searchable picker with
      Enable all, Clear and a Manage link. Advanced Params shows how many parameters
      are changed, every setting name explains itself in a tooltip, Save & Update
      with the change note stays at the bottom of the editor, default features now
      sit with Capabilities and only list the capabilities that are on, default filters
      are switched on per filter inside the Filters picker, Knowledge has its own
      picker with Upload Files, empty lists point to the workspace where items are
      added, and the admin Model Defaults panel uses the same rows. [Commit](https://github.com/open-webui/open-webui/commit/d4879a98bc99e6a80ef13df3772ee1529d657509),
      [Commit](https://github.com/open-webui/open-webui/commit/255f88eff0a0c94e7a99bd95a7fc185aa398ec59),
      [Commit](https://github.com/open-webui/open-webui/commit/8d0ff76f2b8e21ae719a4b9338779b92b8778d98),
      [Commit](https://github.com/open-webui/open-webui/commit/44b71f87ab0433db9f9376d685653ff516c4e7e5),
      [Commit](https://github.com/open-webui/open-webui/commit/d54aa9836eb7cf23e50b6f9ecd35316f09874f1b),
      [Commit](https://github.com/open-webui/open-webui/commit/558fe57ca00ac1f74d9a565e353acc43379644bf),
      [Commit](https://github.com/open-webui/open-webui/commit/90496c28aed961d154143cf22b132caa6b8a52c5),
      [Commit](https://github.com/open-webui/open-webui/commit/76ad6f97c52db1e3b02926132fd6ea9c1176f40a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9F1 **Safety checks for generated image downloads.** When an image
      generation backend returns a link instead of the image, the download now goes
      through the same safety checks as other external image downloads, while links
      on the configured ComfyUI address stay trusted. [#31623](https://github.com/open-webui/open-webui/pull/31623)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9E9 **Default features when comparing models.** Adding a second
      model to a chat keeps web search, image generation and code interpreter on when
      every selected model has them as default features, and the web search toggle
      now always matches what is actually sent. [#30383](https://github.com/open-webui/open-webui/pull/30383),
      [#30310](https://github.com/open-webui/open-webui/issues/30310)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9EA **Code Interpreter when switching chats.** Opening another
      chat from the sidebar now turns Code Interpreter off like web search and image
      generation, where it stayed on and was saved into the next chat's draft; a chat's
      own draft and a model's default features still decide. [#31500](https://github.com/open-webui/open-webui/pull/31500),
      [#31472](https://github.com/open-webui/open-webui/issues/31472)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3A8 **Generated image formats.** Generated images that come back
      as JPEG or WebP are now saved, downloaded and served as what they are, where
      they were always labelled as PNG. [#30359](https://github.com/open-webui/open-webui/pull/30359),
      [#29948](https://github.com/open-webui/open-webui/issues/29948)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-image-generation-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: image-generation
  title: 5 Image Generation changes in v0.12.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-25-47327-preserve-image-generation-request-ids-on-failure-chrisdong-oai|♯47327
  Preserve image generation request IDs on failure @chrisdong-oai]]'
- '[[Changes/Codex CLI/2026-09-28-3-image-generation-changes-in-rust-v0-158-0|3 Image
  Generation changes in rust-v0.158.0]]'
- '[[Changes/ElevenLabs/2026-09-28-flows|Flows]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: image-generation
title: 5 Image Generation changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Image Generation changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/image-generation|Image Generation]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎛️ **Redesigned model editor.** The model editor has a new layout: the background image now fills a banner at the top with the model's picture, name and ID set over it and buttons to add, change or remove it on hover, a long system prompt opens folded to a short preview with Show more, and Capabilities, Default Features, Builtin Tools, Knowledge, Tools, Skills, Filters, Actions, Prompts, Voice and Terminal each fold into one row that summarizes what is set, such as "Web Search, Image Generation +2", "3 of 9 enabled" or "Custom · 4", and opens into switches with descriptions or a searchable picker with Enable all, Clear and a Manage link. Advanced Params shows how many parameters are changed, every setting name explains itself in a tooltip, Save & Update with the change note stays at the bottom of the editor, default features now sit with Capabilities and only list the capabilities that are on, default filters are switched on per filter inside the Filters picker, Knowledge has its own picker with Upload Files, empty lists point to the workspace where items are added, and the admin Model Defaults panel uses the same rows. [Commit](https://github.com/open-webui/open-webui/commit/d4879a98bc99e6a80ef13df3772ee1529d657509), [Commit](https://github.com/open-webui/open-webui/commit/255f88eff0a0c94e7a99bd95a7fc185aa398ec59), [Commit](https://github.com/open-webui/open-webui/commit/8d0ff76f2b8e21ae719a4b9338779b92b8778d98), [Commit](https://github.com/open-webui/open-webui/commit/44b71f87ab0433db9f9376d685653ff516c4e7e5), [Commit](https://github.com/open-webui/open-webui/commit/d54aa9836eb7cf23e50b6f9ecd35316f09874f1b), [Commit](https://github.com/open-webui/open-webui/commit/558fe57ca00ac1f74d9a565e353acc43379644bf), [Commit](https://github.com/open-webui/open-webui/commit/90496c28aed961d154143cf22b132caa6b8a52c5), [Commit](https://github.com/open-webui/open-webui/commit/76ad6f97c52db1e3b02926132fd6ea9c1176f40a)

> 🧱 **Safety checks for generated image downloads.** When an image generation backend returns a link instead of the image, the download now goes through the same safety checks as other external image downloads, while links on the configured ComfyUI address stay trusted. [#31623](https://github.com/open-webui/open-webui/pull/31623)

> 🧩 **Default features when comparing models.** Adding a second model to a chat keeps web search, image generation and code interpreter on when every selected model has them as default features, and the web search toggle now always matches what is actually sent. [#30383](https://github.com/open-webui/open-webui/pull/30383), [#30310](https://github.com/open-webui/open-webui/issues/30310)

> 🧪 **Code Interpreter when switching chats.** Opening another chat from the sidebar now turns Code Interpreter off like web search and image generation, where it stayed on and was saved into the next chat's draft; a chat's own draft and a model's default features still decide. [#31500](https://github.com/open-webui/open-webui/pull/31500), [#31472](https://github.com/open-webui/open-webui/issues/31472)

> 🎨 **Generated image formats.** Generated images that come back as JPEG or WebP are now saved, downloaded and served as what they are, where they were always labelled as PNG. [#30359](https://github.com/open-webui/open-webui/pull/30359), [#29948](https://github.com/open-webui/open-webui/issues/29948)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-reliability-and-performance-changes-in-v0-12-0|5 Reliability and Performance changes in v0.12.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5 Enterprise and Administration changes in v0.12.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-10-27-developer-workflow-changes-in-v0-12-0|27 Developer Workflow changes in v0.12.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-10-49-model-support-changes-in-v0-12-0|49 Model Support changes in v0.12.0]] · Model Support
- [[Changes/Open WebUI/2026-10-10-19-account-and-access-changes-in-v0-12-0|19 Account and Access changes in v0.12.0]] · Account and Access
- [[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10 Automation and Scheduling changes in v0.12.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile and Desktop changes in v0.12.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-10-10-6-files-and-data-changes-in-v0-12-0|6 Files and Data changes in v0.12.0]] · Files and Data
- [[Changes/Open WebUI/2026-10-10-13-collaboration-changes-in-v0-12-0|13 Collaboration changes in v0.12.0]] · Collaboration
- [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-10-5-context-window-changes-in-v0-12-0|5 Context Window changes in v0.12.0]] · Context Window
- [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]] · Interface Experience
- [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Agent Mode
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Image Generation

- Earlier: 2026-09-28 · ElevenLabs · [[Changes/ElevenLabs/2026-09-28-flows|Flows]]
- Later: 2026-10-16 · Open WebUI · [[Changes/Open WebUI/2026-10-16-clear-input-selections-shortcut-clearing-the-model-override-selected-tools-and-f|🧹 Clear Input Selections shortcut. Clearing the model override, selected tools…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-03-10 · Open WebUI · [[Changes/Open WebUI/2024-03-10-dall-e-integration-introduced-dall-e-integration-for-image-generation-alongside|🎨 DALL-E Integration]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-5c30dc&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-5-image-generation-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-5c30dc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->