---
card_id: open-webui-2026-08-31-da0ccf
date: '2026-08-31'
description: "Open WebUI · 2026-08-31 · Model Support: 10 changes in v0.11.2 — \U0001F3CE️
  **Lighter model list refreshes.** On deployments running several workers, a refresh
  that…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1330
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dfbef114e44e3507b05ea64889d6ed350a5462fbc2c127a80a858d95887b6712
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-31-da0ccf
  comparison: ''
  date: '2026-08-31'
  description: 'Open WebUI — v0.11.2: 10 Model Support changes'
  evidence:
  - quote: "\U0001F3CE️ **Lighter model list refreshes.** On deployments running several
      workers, a refresh that finds the model list unchanged no longer has every worker
      rewrite the whole list to the shared cache, cutting the work and the traffic
      each refresh costs. [#29264](https://github.com/open-webui/open-webui/pull/29264)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F9F0 **A new request filter step.** Filter authors can now use `request`
      to adjust the payload right before each model call, including follow-up calls
      after tool use, while existing `inlet`, `stream`, and `outlet` filters keep
      working as before. [Commit](https://github.com/open-webui/open-webui/commit/2daa610cba514dfe2eae008b1fc440d4ddb0e470),
      [Commit](https://github.com/open-webui/open-webui/commit/2a4ef46ac86ada3447eb6d6c50fd4c1241eebd4d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F9CA **Streaming no longer stalls on reasoning models.** A reply
      from a reasoning model now streams through to the end instead of showing its
      first few words and then freezing until generation finishes. [#29053](https://github.com/open-webui/open-webui/pull/29053),
      [#29035](https://github.com/open-webui/open-webui/issues/29035)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F4AD **Thinking stays in Thoughts.** After a model uses a tool,
      its reasoning for the next step now appears in the collapsed Thoughts section
      instead of being written into the reply as ordinary text. [#29052](https://github.com/open-webui/open-webui/pull/29052),
      [#29040](https://github.com/open-webui/open-webui/issues/29040)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F9F0 **Pinned models start with their own tools.** Starting a chat
      from a pinned model in the sidebar now applies that model's tools and skills
      instead of carrying over the ones from the model you used last. [#29058](https://github.com/open-webui/open-webui/pull/29058),
      [#29050](https://github.com/open-webui/open-webui/issues/29050)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: ❓ **Rejected ask_user calls no longer kill the reply.** If a model asks
      the user a question in a way Open WebUI refuses, the model now receives that
      error and can continue or retry, instead of leaving the chat stopped with no
      answer. [#29252](https://github.com/open-webui/open-webui/pull/29252), [#29077](https://github.com/open-webui/open-webui/issues/29077)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F6AB **Disabled models no longer vanish.** Turning a model off in
      the admin Models list now keeps it in view so you can turn it back on, instead
      of it disappearing with no way to recover it. [#29037](https://github.com/open-webui/open-webui/pull/29037),
      [#29036](https://github.com/open-webui/open-webui/issues/29036)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: ✂️ **Message text kept intact.** Text containing angle brackets and a dollar
      sign is no longer mistaken for a skill mention and silently removed before your
      message reaches the model. [#29051](https://github.com/open-webui/open-webui/pull/29051),
      [#29041](https://github.com/open-webui/open-webui/issues/29041)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F4F1 **Readable model list on small screens.** The model identifier
      and timestamp in the workspace model list no longer overlap the model name on
      narrow displays. [#29084](https://github.com/open-webui/open-webui/pull/29084),
      [#29083](https://github.com/open-webui/open-webui/issues/29083)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F9ED **Model defaults panels stay usable.** The model capabilities
      and prompt suggestion sections in admin settings now scroll inside their panels
      instead of growing past the available space. [#29235](https://github.com/open-webui/open-webui/pull/29235)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 10-model-support-changes-in-v0-11-2
  source_release: open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b
  source_type: github_releases
  theme: model-support
  title: 10 Model Support changes in v0.11.2
  type: change
related_changes:
- '[[Changes/Midjourney/2026-08-29-we-ve-updated-our-v8-2-edit-model-for-better-image-quality-if-you-ve-had-any-iss|Edit
  Image Quality Update]]'
- '[[Changes/ChatGPT/2026-08-31-site-tools-use-webmcp-and-require-a-supported-account-model-and-webpage-they-are|Site
  tools use WebMCP and require a supported account, model, and webpage]]'
- '[[Changes/Lovable/2026-08-31-priority-processing-now-works-with-gemini-chat-models|Priority
  processing now works with Gemini chat models]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b|open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b]]'
source_type: github_releases
theme: model-support
title: 10 Model Support changes in v0.11.2
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Model Support changes in v0.11.2

**Open WebUI** · 2026-08-31 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.2) · from [[Releases/Open WebUI/open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b|v0.11.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🏎️ **Lighter model list refreshes.** On deployments running several workers, a refresh that finds the model list unchanged no longer has every worker rewrite the whole list to the shared cache, cutting the work and the traffic each refresh costs. [#29264](https://github.com/open-webui/open-webui/pull/29264)

> 🧰 **A new request filter step.** Filter authors can now use `request` to adjust the payload right before each model call, including follow-up calls after tool use, while existing `inlet`, `stream`, and `outlet` filters keep working as before. [Commit](https://github.com/open-webui/open-webui/commit/2daa610cba514dfe2eae008b1fc440d4ddb0e470), [Commit](https://github.com/open-webui/open-webui/commit/2a4ef46ac86ada3447eb6d6c50fd4c1241eebd4d)

> 🧊 **Streaming no longer stalls on reasoning models.** A reply from a reasoning model now streams through to the end instead of showing its first few words and then freezing until generation finishes. [#29053](https://github.com/open-webui/open-webui/pull/29053), [#29035](https://github.com/open-webui/open-webui/issues/29035)

> 💭 **Thinking stays in Thoughts.** After a model uses a tool, its reasoning for the next step now appears in the collapsed Thoughts section instead of being written into the reply as ordinary text. [#29052](https://github.com/open-webui/open-webui/pull/29052), [#29040](https://github.com/open-webui/open-webui/issues/29040)

> 🧰 **Pinned models start with their own tools.** Starting a chat from a pinned model in the sidebar now applies that model's tools and skills instead of carrying over the ones from the model you used last. [#29058](https://github.com/open-webui/open-webui/pull/29058), [#29050](https://github.com/open-webui/open-webui/issues/29050)

> ❓ **Rejected ask_user calls no longer kill the reply.** If a model asks the user a question in a way Open WebUI refuses, the model now receives that error and can continue or retry, instead of leaving the chat stopped with no answer. [#29252](https://github.com/open-webui/open-webui/pull/29252), [#29077](https://github.com/open-webui/open-webui/issues/29077)

> 🚫 **Disabled models no longer vanish.** Turning a model off in the admin Models list now keeps it in view so you can turn it back on, instead of it disappearing with no way to recover it. [#29037](https://github.com/open-webui/open-webui/pull/29037), [#29036](https://github.com/open-webui/open-webui/issues/29036)

> ✂️ **Message text kept intact.** Text containing angle brackets and a dollar sign is no longer mistaken for a skill mention and silently removed before your message reaches the model. [#29051](https://github.com/open-webui/open-webui/pull/29051), [#29041](https://github.com/open-webui/open-webui/issues/29041)

> 📱 **Readable model list on small screens.** The model identifier and timestamp in the workspace model list no longer overlap the model name on narrow displays. [#29084](https://github.com/open-webui/open-webui/pull/29084), [#29083](https://github.com/open-webui/open-webui/issues/29083)

> 🧭 **Model defaults panels stay usable.** The model capabilities and prompt suggestion sections in admin settings now scroll inside their panels instead of growing past the available space. [#29235](https://github.com/open-webui/open-webui/pull/29235)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-31-large-tool-calls-stream-faster-through-anthropic-compatible-clients-when-a-strea|🧠 Large tool calls stream faster through Anthropic-compatible…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-08-31-3-automation-and-scheduling-changes-in-v0-11-2|3 Automation and Scheduling changes in v0.11.2]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-08-31-3-interface-experience-changes-in-v0-11-2|3 Interface Experience changes in v0.11.2]] · Interface Experience
- [[Changes/Open WebUI/2026-08-31-code-interpreter-starts-on-windows-the-built-in-code-interpreter-now-serves-its|🐍 Code interpreter starts on Windows. The built-in code interpreter now serves…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-08-31-security-advisory-this-release-includes-security-and-access-control-fixes-we-rec|🛡️ Security Advisory: This release includes security and access-control fixes]] · Safety and Privacy
- [[Changes/Open WebUI/2026-08-31-high-contrast-mode-is-now-accessibility-mode-the-interface-setting-previously-ca|🏷️ High Contrast Mode is now Accessibility Mode. The interface setting…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-08-31-9-developer-workflow-changes-in-v0-11-2|9 Developer Workflow changes in v0.11.2]] · Developer Workflow
- [[Changes/Open WebUI/2026-08-31-2-files-and-data-changes-in-v0-11-2|2 Files and Data changes in v0.11.2]] · Files and Data
- [[Changes/Open WebUI/2026-08-31-2-collaboration-changes-in-v0-11-2|2 Collaboration changes in v0.11.2]] · Collaboration
- [[Changes/Open WebUI/2026-08-31-12-other-changes-in-v0-11-2|12 other changes in v0.11.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-08-31 · Lovable · [[Changes/Lovable/2026-08-31-priority-processing-now-works-with-gemini-chat-models|Priority processing now works with Gemini chat models]]
- Later: 2026-08-31 · OpenClaw · [[Changes/OpenClaw/2026-08-31-models-and-providers-chat-and-the-models-page-open-from-the-catalog-openclaw-alr|Models and Providers - Chat and the Models page open from the catalog OpenClaw…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-31-da0ccf&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-31-10-model-support-changes-in-v0-11-2.md%0ACard%20ID%3A%20open-webui-2026-08-31-da0ccf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->