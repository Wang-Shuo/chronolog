---
card_id: open-webui-2026-06-01-ce37e6
date: '2026-06-01'
description: "Open WebUI · 2026-06-01 · Model Support: 12 changes in v0.9.6 — \U0001FA84
  **Per-chat skills toggle.** Skills can now be turned on or off for a conversation
  directly…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1239
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f00fba2595e76cca68e2a8394dc1a59dc14643f27bd116dffeff93604372c4a0
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-01-ce37e6
  comparison: ''
  date: '2026-06-01'
  description: 'Open WebUI — v0.9.6: 12 Model Support changes'
  evidence:
  - quote: "\U0001FA84 **Per-chat skills toggle.** Skills can now be turned on or
      off for a conversation directly from the chat Integrations menu, the same way
      tools and capabilities already work, instead of only through the model preset.
      [#25036](https://github.com/open-webui/open-webui/issues/25036), [#25037](https://github.com/open-webui/open-webui/pull/25037)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4BD **Fewer redundant model-list writes.** On multi-instance deployments
      backed by Redis, the model list is no longer rewritten when it hasn't changed,
      cutting a major source of redundant writes. [#25469](https://github.com/open-webui/open-webui/issues/25469),
      [#25474](https://github.com/open-webui/open-webui/pull/25474), [Commit](https://github.com/open-webui/open-webui/commit/fd76b51ab2ad4c4192f2c98153e47888712c2009)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4D0 **Profile image size limit.** Administrators can now cap the
      size of inline profile images via the new \"PROFILE_IMAGE_MAX_DATA_URI_SIZE\"
      setting, bounding how much database and cache space inline avatars and model
      icons can consume. [#25468](https://github.com/open-webui/open-webui/issues/25468),
      [#25476](https://github.com/open-webui/open-webui/pull/25476)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F6A7 **System prompt bypass via request parameter.** The flag that
      skips a model's configured system prompt can no longer be set by external clients
      through a request parameter, so admin-configured system prompts can't be bypassed
      from the API. [#25156](https://github.com/open-webui/open-webui/pull/25156)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F500 **Ollama backend selection access check.** Requests can no
      longer target an arbitrary Ollama backend by index; a caller-supplied backend
      selector is now verified against the backends that actually serve the requested
      model. [Commit](https://github.com/open-webui/open-webui/commit/7139797be04030b9d1016782f1dbb251c5fe68bb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F9FC **Model profile image script injection.** Model profile images
      are now validated on save and only served inline when they are a known-safe
      image type, preventing a crafted SVG profile image from running scripts in other
      users' browsers, while existing legacy images that fail validation are cleared
      gracefully instead of breaking the model list. [#25060](https://github.com/open-webui/open-webui/pull/25060),
      [#25173](https://github.com/open-webui/open-webui/pull/25173)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4AC **Chat title generation.** Automatically generated chat titles
      now use the model currently selected in the dropdown for the active chat and
      fall back to the model from the active message branch otherwise, and a clear
      message is shown if no model is available instead of an unhelpful error. [#24604](https://github.com/open-webui/open-webui/issues/24604),
      [#24745](https://github.com/open-webui/open-webui/issues/24745), [Commit](https://github.com/open-webui/open-webui/commit/e5c8f8110a88739e011d8ab23e5cb11b4768469f),
      [Commit](https://github.com/open-webui/open-webui/commit/3c5e7968f0b5130890e17f1f2a2a52297cb145a6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F9E0 **Clear error when no embedding model is configured.** Using
      knowledge or retrieval features without a loaded embedding model now returns
      a clear setup error explaining what to configure, instead of failing with a
      cryptic crash. [Commit](https://github.com/open-webui/open-webui/commit/55ca719bbf76306ed647424c728f730d0bef21f9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4AD **Advanced parameter settings.** Custom reasoning tags and
      custom model parameters are now saved correctly instead of being dropped, and
      the presence penalty and repeat penalty no longer save the frequency penalty's
      value instead of their own. [#25183](https://github.com/open-webui/open-webui/pull/25183),
      [#25200](https://github.com/open-webui/open-webui/pull/25200), [#25204](https://github.com/open-webui/open-webui/pull/25204)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F5B1️ **Focus-loss handling in editors.** Workspace and admin editors
      for models, tools, functions, and skills again respond correctly when the browser
      window loses focus, after the wrong event name was being listened for. [#25459](https://github.com/open-webui/open-webui/pull/25459)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F648 **Hidden models in channel mentions.** Models marked as hidden
      no longer appear in the channel message-input model mention selector, matching
      how hidden models are excluded elsewhere in the interface. [#24892](https://github.com/open-webui/open-webui/pull/24892)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F649 **Hidden models in default-model and automation pickers.**
      The admin pickers for default models and default pinned models, and the automation
      model dropdown, now filter out hidden models, consistent with how hidden models
      are treated elsewhere. [#24869](https://github.com/open-webui/open-webui/issues/24869),
      [Commit](https://github.com/open-webui/open-webui/commit/1fa3050f069a72de1daaaa29233b545c4deaea51),
      [Commit](https://github.com/open-webui/open-webui/commit/4705c2d98812c1189c2ae4960399bc8888d4861c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 12-model-support-changes-in-v0-9-6
  source_release: open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e
  source_type: github_releases
  theme: model-support
  title: 12 Model Support changes in v0.9.6
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-06-01-5-model-support-changes-in-rust-v0-136-0|5 Model
  Support changes in rust-v0.136.0]]'
- '[[Changes/ElevenLabs/2026-06-01-workspaces|Workspaces]]'
- '[[Changes/GitHub Copilot CLI/2026-06-01-new-reasoning-after-tool-calls-appears-at-the-bottom-of-the-timeline-instead-of|New
  reasoning after tool calls appears at the bottom of the timeline instead…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e]]'
source_type: github_releases
theme: model-support
title: 12 Model Support changes in v0.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Model Support changes in v0.9.6

**Open WebUI** · 2026-06-01 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.6) · from [[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🪄 **Per-chat skills toggle.** Skills can now be turned on or off for a conversation directly from the chat Integrations menu, the same way tools and capabilities already work, instead of only through the model preset. [#25036](https://github.com/open-webui/open-webui/issues/25036), [#25037](https://github.com/open-webui/open-webui/pull/25037)

> 💽 **Fewer redundant model-list writes.** On multi-instance deployments backed by Redis, the model list is no longer rewritten when it hasn't changed, cutting a major source of redundant writes. [#25469](https://github.com/open-webui/open-webui/issues/25469), [#25474](https://github.com/open-webui/open-webui/pull/25474), [Commit](https://github.com/open-webui/open-webui/commit/fd76b51ab2ad4c4192f2c98153e47888712c2009)

> 📐 **Profile image size limit.** Administrators can now cap the size of inline profile images via the new "PROFILE_IMAGE_MAX_DATA_URI_SIZE" setting, bounding how much database and cache space inline avatars and model icons can consume. [#25468](https://github.com/open-webui/open-webui/issues/25468), [#25476](https://github.com/open-webui/open-webui/pull/25476)

> 🚧 **System prompt bypass via request parameter.** The flag that skips a model's configured system prompt can no longer be set by external clients through a request parameter, so admin-configured system prompts can't be bypassed from the API. [#25156](https://github.com/open-webui/open-webui/pull/25156)

> 🔀 **Ollama backend selection access check.** Requests can no longer target an arbitrary Ollama backend by index; a caller-supplied backend selector is now verified against the backends that actually serve the requested model. [Commit](https://github.com/open-webui/open-webui/commit/7139797be04030b9d1016782f1dbb251c5fe68bb)

> 🧼 **Model profile image script injection.** Model profile images are now validated on save and only served inline when they are a known-safe image type, preventing a crafted SVG profile image from running scripts in other users' browsers, while existing legacy images that fail validation are cleared gracefully instead of breaking the model list. [#25060](https://github.com/open-webui/open-webui/pull/25060), [#25173](https://github.com/open-webui/open-webui/pull/25173)

> 💬 **Chat title generation.** Automatically generated chat titles now use the model currently selected in the dropdown for the active chat and fall back to the model from the active message branch otherwise, and a clear message is shown if no model is available instead of an unhelpful error. [#24604](https://github.com/open-webui/open-webui/issues/24604), [#24745](https://github.com/open-webui/open-webui/issues/24745), [Commit](https://github.com/open-webui/open-webui/commit/e5c8f8110a88739e011d8ab23e5cb11b4768469f), [Commit](https://github.com/open-webui/open-webui/commit/3c5e7968f0b5130890e17f1f2a2a52297cb145a6)

> 🧠 **Clear error when no embedding model is configured.** Using knowledge or retrieval features without a loaded embedding model now returns a clear setup error explaining what to configure, instead of failing with a cryptic crash. [Commit](https://github.com/open-webui/open-webui/commit/55ca719bbf76306ed647424c728f730d0bef21f9)

> 💭 **Advanced parameter settings.** Custom reasoning tags and custom model parameters are now saved correctly instead of being dropped, and the presence penalty and repeat penalty no longer save the frequency penalty's value instead of their own. [#25183](https://github.com/open-webui/open-webui/pull/25183), [#25200](https://github.com/open-webui/open-webui/pull/25200), [#25204](https://github.com/open-webui/open-webui/pull/25204)

> 🖱️ **Focus-loss handling in editors.** Workspace and admin editors for models, tools, functions, and skills again respond correctly when the browser window loses focus, after the wrong event name was being listened for. [#25459](https://github.com/open-webui/open-webui/pull/25459)

> 🙈 **Hidden models in channel mentions.** Models marked as hidden no longer appear in the channel message-input model mention selector, matching how hidden models are excluded elsewhere in the interface. [#24892](https://github.com/open-webui/open-webui/pull/24892)

> 🙉 **Hidden models in default-model and automation pickers.** The admin pickers for default models and default pinned models, and the automation model dropdown, now filter out hidden models, consistent with how hidden models are treated elsewhere. [#24869](https://github.com/open-webui/open-webui/issues/24869), [Commit](https://github.com/open-webui/open-webui/commit/1fa3050f069a72de1daaaa29233b545c4deaea51), [Commit](https://github.com/open-webui/open-webui/commit/4705c2d98812c1189c2ae4960399bc8888d4861c)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-01-bulk-enable-or-disable-automations-automations-can-now-be-enabled-or-disabled-in|🔘 Bulk enable or disable automations. Automations can now be enabled or disabled…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-01-4-context-window-changes-in-v0-9-6|4 Context Window changes in v0.9.6]] · Context Window
- [[Changes/Open WebUI/2026-06-01-2-memory-and-personalization-changes-in-v0-9-6|2 Memory and Personalization changes in v0.9.6]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-01-keyboard-and-screen-reader-access-to-menus-the-integrations-more-options-and-use|♿ Keyboard and screen reader access to menus. The integrations, more-options…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-01-27-developer-workflow-changes-in-v0-9-6|27 Developer Workflow changes in v0.9.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-01-4-interface-experience-changes-in-v0-9-6|4 Interface Experience changes in v0.9.6]] · Interface Experience
- [[Changes/Open WebUI/2026-06-01-4-editor-experience-changes-in-v0-9-6|4 Editor Experience changes in v0.9.6]] · Editor Experience
- [[Changes/Open WebUI/2026-06-01-5-files-and-data-changes-in-v0-9-6|5 Files and Data changes in v0.9.6]] · Files and Data
- [[Changes/Open WebUI/2026-06-01-7-safety-and-privacy-changes-in-v0-9-6|7 Safety and Privacy changes in v0.9.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-01-startup-on-non-unicode-consoles-open-webui-no-longer-crashes-at-startup-when-the|🥾 Startup on non-Unicode consoles. Open WebUI no longer crashes at startup…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-01-youtube-short-link-transcripts-pasting-a-youtu-be-short-link-into-a-chat-now-loa|📺 YouTube short link transcripts. Pasting a "youtu.be" short link into a chat…]] · Multimodal Input
- [[Changes/Open WebUI/2026-06-01-9-search-and-browsing-changes-in-v0-9-6|9 Search and Browsing changes in v0.9.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-01-shared-chat-file-write-protection-access-to-a-file-through-a-shared-chat-now-onl|🔐 Shared-chat file write protection. Access to a file through a shared chat now…]] · Collaboration
- [[Changes/Open WebUI/2026-06-01-2-enterprise-and-administration-changes-in-v0-9-6|2 Enterprise and Administration changes in v0.9.6]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-01-image-generation-with-non-standard-response-headers-image-generation-now-works-w|🖌️ Image generation with non-standard response headers. Image generation now…]] · Image Generation
- [[Changes/Open WebUI/2026-06-01-6-account-and-access-changes-in-v0-9-6|6 Account and Access changes in v0.9.6]] · Account and Access
- [[Changes/Open WebUI/2026-06-01-4-apps-and-integrations-changes-in-v0-9-6|4 Apps and Integrations changes in v0.9.6]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-01-5-reliability-and-performance-changes-in-v0-9-6|5 Reliability and Performance changes in v0.9.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-01-4-voice-and-audio-changes-in-v0-9-6|4 Voice and Audio changes in v0.9.6]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-01-20-other-changes-in-v0-9-6|20 other changes in v0.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-06-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-01-new-reasoning-after-tool-calls-appears-at-the-bottom-of-the-timeline-instead-of|New reasoning after tool calls appears at the bottom of the timeline instead…]]
- Later: 2026-06-02 · Claude Code · [[Changes/Claude Code/2026-06-02-removed-claude-code-opus-4-6-fast-mode-override-the-environment-variable-is-now|Removed CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE; the environment variable is now a no-op]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-01-ce37e6&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-01-12-model-support-changes-in-v0-9-6.md%0ACard%20ID%3A%20open-webui-2026-06-01-ce37e6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->