---
card_id: open-webui-2026-10-29-617e16
date: '2026-10-29'
description: "Open WebUI · 2026-10-29 · Model Support: 7 changes in v0.12.5 — \U0001F4BE
  **Chat model choice saved.** Changing the model in a chat is now saved with the
  chat right…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1389
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 51a8d11c2fd34b95fc2ab2b71dd4591fd8b6027b067fe1cbedd37705664ef2f7
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-29-617e16
  comparison: ''
  date: '2026-10-29'
  description: 'Open WebUI — v0.12.5: 7 Model Support changes'
  evidence:
  - quote: "\U0001F4BE **Chat model choice saved.** Changing the model in a chat is
      now saved with the chat right away, so the chat reopens with that model even
      when no message was sent after the change. [Commit](https://github.com/open-webui/open-webui/commit/3aaecdd0e99f6407187732f2fb117841ce2cc013)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F58C️ **Responses API images shown.** Images that a model creates
      through the Responses API, such as Gemini image models through OpenRouter, now
      show in the chat, where they were saved but not displayed. [#33320](https://github.com/open-webui/open-webui/issues/33320),
      [Commit](https://github.com/open-webui/open-webui/commit/ef29fb12f1f641bf1d83b434a37298846d211deb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F6DD **Playground Controls applied.** Settings chosen under Controls
      in the Playground, such as Temperature and Seed, now reach Ollama models, where
      they were dropped and every run gave a different reply. [#33286](https://github.com/open-webui/open-webui/pull/33286),
      [#33285](https://github.com/open-webui/open-webui/issues/33285), [Commit](https://github.com/open-webui/open-webui/commit/f58fdf9b9531c27d18f449485eccd985490a86c0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F9F5 **Thread replies while loading.** A thread reply or model answer
      that arrives while the thread is still loading now shows up in full, and a reply
      no longer shows twice. [#33346](https://github.com/open-webui/open-webui/issues/33346),
      [Commit](https://github.com/open-webui/open-webui/commit/d14d8788af6626bffc3717c7ef5bcbc4f441a5cc),
      [Commit](https://github.com/open-webui/open-webui/commit/be8ebed78428bde77a369c5cb4ed1c1bca720592)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F500 **Model switch keeps your picks.** Switching models in a chat
      now applies the new model's default tools, skills, filters and features while
      keeping the ones you turned on or off yourself, where every switch cleared your
      picks, and chats with several models now get the default tools and skills of
      every selected model. [Commit](https://github.com/open-webui/open-webui/commit/3aaecdd0e99f6407187732f2fb117841ce2cc013),
      [Commit](https://github.com/open-webui/open-webui/commit/1c572c49bc5103b78c812e069872015d7fcb7391)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F4E3 **Model mentions switch chats.** Sending a message to a model
      picked with @ now switches the chat to that model, where the mention stayed
      above the input and the chat kept its own model. [Commit](https://github.com/open-webui/open-webui/commit/3aaecdd0e99f6407187732f2fb117841ce2cc013)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  - quote: "\U0001F501 **Regenerate uses current models.** Regenerating a response
      in a chat with several models now uses the model currently picked for that column,
      where it reused the model that first wrote the response. [Commit](https://github.com/open-webui/open-webui/commit/3aaecdd0e99f6407187732f2fb117841ce2cc013)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-model-support-changes-in-v0-12-5
  source_release: open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e
  source_type: github_releases
  theme: model-support
  title: 7 Model Support changes in v0.12.5
  type: change
related_changes:
- '[[Changes/OpenCode/2026-10-27-add-configurable-prompt-cache-ttls-per-provider-model|Add
  configurable prompt cache TTLs per provider/model]]'
- '[[Changes/OpenHands/2026-10-27-refactor-settings-use-existing-model-profile-theme-aliases-by-enyst-in-https-git|refactor(settings):
  use existing model-profile theme aliases]]'
- '[[Changes/Codex CLI/2026-10-29-10-model-support-changes-in-rust-v0-166-0|10 Model
  Support changes in rust-v0.166.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e|open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e]]'
source_type: github_releases
theme: model-support
title: 7 Model Support changes in v0.12.5
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Model Support changes in v0.12.5

**Open WebUI** · 2026-10-29 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.5) · from [[Releases/Open WebUI/open-webui-2026-10-29-v0-12-5-github-427647877-d6957e2e|v0.12.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 💾 **Chat model choice saved.** Changing the model in a chat is now saved with the chat right away, so the chat reopens with that model even when no message was sent after the change. [Commit](https://github.com/open-webui/open-webui/commit/3aaecdd0e99f6407187732f2fb117841ce2cc013)

> 🖌️ **Responses API images shown.** Images that a model creates through the Responses API, such as Gemini image models through OpenRouter, now show in the chat, where they were saved but not displayed. [#33320](https://github.com/open-webui/open-webui/issues/33320), [Commit](https://github.com/open-webui/open-webui/commit/ef29fb12f1f641bf1d83b434a37298846d211deb)

> 🛝 **Playground Controls applied.** Settings chosen under Controls in the Playground, such as Temperature and Seed, now reach Ollama models, where they were dropped and every run gave a different reply. [#33286](https://github.com/open-webui/open-webui/pull/33286), [#33285](https://github.com/open-webui/open-webui/issues/33285), [Commit](https://github.com/open-webui/open-webui/commit/f58fdf9b9531c27d18f449485eccd985490a86c0)

> 🧵 **Thread replies while loading.** A thread reply or model answer that arrives while the thread is still loading now shows up in full, and a reply no longer shows twice. [#33346](https://github.com/open-webui/open-webui/issues/33346), [Commit](https://github.com/open-webui/open-webui/commit/d14d8788af6626bffc3717c7ef5bcbc4f441a5cc), [Commit](https://github.com/open-webui/open-webui/commit/be8ebed78428bde77a369c5cb4ed1c1bca720592)

> 🔀 **Model switch keeps your picks.** Switching models in a chat now applies the new model's default tools, skills, filters and features while keeping the ones you turned on or off yourself, where every switch cleared your picks, and chats with several models now get the default tools and skills of every selected model. [Commit](https://github.com/open-webui/open-webui/commit/3aaecdd0e99f6407187732f2fb117841ce2cc013), [Commit](https://github.com/open-webui/open-webui/commit/1c572c49bc5103b78c812e069872015d7fcb7391)

> 📣 **Model mentions switch chats.** Sending a message to a model picked with @ now switches the chat to that model, where the mention stayed above the input and the chat kept its own model. [Commit](https://github.com/open-webui/open-webui/commit/3aaecdd0e99f6407187732f2fb117841ce2cc013)

> 🔁 **Regenerate uses current models.** Regenerating a response in a chat with several models now uses the model currently picked for that column, where it reused the model that first wrote the response. [Commit](https://github.com/open-webui/open-webui/commit/3aaecdd0e99f6407187732f2fb117841ce2cc013)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-29-improved-ui-accessibility-screen-reader-and-keyboard-users-can-now-move-through|♿ Improved UI accessibility. Screen reader and keyboard users can now move…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-10-29-provider-details-for-models-administrators-editing-a-model-now-see-a-provider-de|📇 Provider details for models. Administrators editing a model now see a Provider…]] · Context Window
- [[Changes/Open WebUI/2026-10-29-2-memory-and-personalization-changes-in-v0-12-5|2 Memory and Personalization changes in v0.12.5]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-29-2-automation-and-scheduling-changes-in-v0-12-5|2 Automation and Scheduling changes in v0.12.5]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-29-photos-for-sub-agents-models-can-now-hand-a-photo-attached-in-the-chat-to-a-sub|🤖 Photos for sub-agents. Models can now hand a photo attached in the chat…]] · Agent Mode
- [[Changes/Open WebUI/2026-10-29-knowledge-base-api-responses-trimmed-adding-updating-or-removing-knowledge-base|📃 Knowledge base API responses trimmed. Adding, updating or removing knowledge…]] · Collaboration
- [[Changes/Open WebUI/2026-10-29-2-reliability-and-performance-changes-in-v0-12-5|2 Reliability and Performance changes in v0.12.5]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-29-35-developer-workflow-changes-in-v0-12-5|35 Developer Workflow changes in v0.12.5]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-29-admins-manage-user-api-keys-administrators-can-now-rotate-or-delete-a-user-s-api|🗝️ Admins manage user API keys. Administrators can now rotate or delete a user's…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-29-2-image-generation-changes-in-v0-12-5|2 Image Generation changes in v0.12.5]] · Image Generation
- [[Changes/Open WebUI/2026-10-29-2-files-and-data-changes-in-v0-12-5|2 Files and Data changes in v0.12.5]] · Files and Data
- [[Changes/Open WebUI/2026-10-29-2-apps-and-integrations-changes-in-v0-12-5|2 Apps and Integrations changes in v0.12.5]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-29-security-advisory-this-release-contains-security-fixes-we-strongly-recommend-upd|🛡️ Security Advisory: This release contains security fixes]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-29-2-interface-experience-changes-in-v0-12-5|2 Interface Experience changes in v0.12.5]] · Interface Experience
- [[Changes/Open WebUI/2026-10-29-read-aloud-with-kokoro-js-read-aloud-now-speaks-with-the-chosen-kokoro-voice-whe|🔊 Read Aloud with Kokoro.js. Read Aloud now speaks with the chosen Kokoro voice…]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-29-6-editor-experience-changes-in-v0-12-5|6 Editor Experience changes in v0.12.5]] · Editor Experience
- [[Changes/Open WebUI/2026-10-29-translation-updates-translations-for-portuguese-brazil-catalan-italian-azerbaija|🌐 Translation updates. Translations for Portuguese (Brazil), Catalan, Italian…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-29 · Codex CLI · [[Changes/Codex CLI/2026-10-29-10-model-support-changes-in-rust-v0-166-0|10 Model Support changes in rust-v0.166.0]]
- Later: 2026-10-29 · OpenCode · [[Changes/OpenCode/2026-10-29-new-default-model-picker|New Default Model Picker]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-29-617e16&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-29-7-model-support-changes-in-v0-12-5.md%0ACard%20ID%3A%20open-webui-2026-10-29-617e16%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->