---
card_id: open-webui-2026-10-25-104f10
date: '2026-10-25'
description: "Open WebUI · 2026-10-25 · Model Support: 16 changes in v0.12.4 — \U0001F3AF
  **Load selected skills on demand.** Administrators can turn on \"Load selected skills
  on…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1385
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cf67027adfee06f10af983700ee147a650a656ec3c2d14aa7ae0292403202b4a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-25-104f10
  comparison: ''
  date: '2026-10-25'
  description: 'Open WebUI — v0.12.4: 16 Model Support changes'
  evidence:
  - quote: "\U0001F3AF **Load selected skills on demand.** Administrators can turn
      on \"Load selected skills on demand\" under Admin Settings > General or set
      \"ENABLE_SKILL_LAZY_LOADING\", so skills selected in the chat or attached to
      a model are only listed for the model to load when it needs them instead of
      sending their full instructions with every message, while skills mentioned in
      the message still load right away, and it is off by default and needs the built-in
      Skills tool. [Commit](https://github.com/open-webui/open-webui/commit/079fb19e75f8be4b44fada0c755cf383b21a625b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001FAAA **Profile cards across the workspace.** Hovering an owner's
      name in the workspace lists of models, knowledge, prompts, skills and tools
      and in admin Functions now opens their profile card instead of an email tooltip,
      with their profile picture next to the name, profile pictures in access settings,
      version history and the Analytics user list open the card too and the Notes
      list shows each owner's profile picture. [Commit](https://github.com/open-webui/open-webui/commit/02974f41e9b7c9d34f2cd7c664c2a04fd6ac12ae),
      [Commit](https://github.com/open-webui/open-webui/commit/72cc79b8f336a753b6e75e0f3415630601b14759),
      [Commit](https://github.com/open-webui/open-webui/commit/ba34b1c47c1d054d2f9c498d0aed862ec06da41a),
      [Commit](https://github.com/open-webui/open-webui/commit/4491e60a296c89b11f22a43f416ea04770fd687f),
      [Commit](https://github.com/open-webui/open-webui/commit/0de8d03c625739ed3fe5e5f2a33de79a760238bd),
      [Commit](https://github.com/open-webui/open-webui/commit/0628670f56133d2cdc20c59b06fbb9de36932eb9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: ✍️ **Note edits by text.** The model can now edit a note by finding and
      replacing exact text instead of only by character offsets, picking one match
      or all of them and getting the positions and surrounding text back when a match
      is ambiguous. [Commit](https://github.com/open-webui/open-webui/commit/243ef36c496714d9dd855de9fd261daa43caddb9),
      [#32752](https://github.com/open-webui/open-webui/issues/32752)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4C8 **Analytics by tokens.** The Admin Analytics dashboard now
      ranks models and users by tokens by default with a switch back to messages,
      and its usage chart adds volume and activity views, a single model view, a comparison
      with the previous period, a choice of time steps and Year to date and Last 12
      months ranges. [Commit](https://github.com/open-webui/open-webui/commit/131ddc32ecaeb06f9aa8740ff004710bacef72e0),
      [Commit](https://github.com/open-webui/open-webui/commit/06c17834ee3168b922f1b8a935b9dd76884b8fda),
      [Commit](https://github.com/open-webui/open-webui/commit/dc2ac86060e583f7374dd86f32f374a0b956bb8b),
      [Commit](https://github.com/open-webui/open-webui/commit/3539ad63213d13865a87a4db64a9829fd7d3b1b4),
      [Commit](https://github.com/open-webui/open-webui/commit/08bfaa4be67f6f87878b2209d568a648818506a7),
      [Commit](https://github.com/open-webui/open-webui/commit/06c382e5d223ba1b35dc0b1306c71da489c632b0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001FAA1 **More Concise and Add Details.** Choosing More Concise or
      Add Details or typing a suggestion under a reply now rewrites that reply, where
      the model got the instruction without the reply and answered it on its own,
      for example with \"OK, I'll keep answers shorter\". [#33084](https://github.com/open-webui/open-webui/pull/33084),
      [Commit](https://github.com/open-webui/open-webui/commit/c69e5a73c0de43691e502bfaa03285e4e8cec05d),
      [#33083](https://github.com/open-webui/open-webui/issues/33083)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F3A8 **Images after tool approval.** Images the model generates
      after you answer its question or approve or reject a tool call now appear in
      the reply, where they were created but never shown and the model kept retrying
      with more hidden images. [#32680](https://github.com/open-webui/open-webui/pull/32680),
      [Commit](https://github.com/open-webui/open-webui/commit/93ba628f3a3cf7f275892f3f3e0375d5984b51a7),
      [#32678](https://github.com/open-webui/open-webui/issues/32678)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F9EC **Embeddings with Prefix ID.** The embeddings API now works
      with models from a connection that has a Prefix ID, where the provider rejected
      the prefixed model name as unknown. [#32724](https://github.com/open-webui/open-webui/pull/32724),
      [Commit](https://github.com/open-webui/open-webui/commit/c901bc39d31eb85af289743850f92848529d422b),
      [#32715](https://github.com/open-webui/open-webui/issues/32715)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F6E0️ **Same-named tool functions.** When two attached tools have
      a function with the same name, the model can now call both, where only the first
      one could be called. [#32670](https://github.com/open-webui/open-webui/pull/32670),
      [Commit](https://github.com/open-webui/open-webui/commit/ab6976b5bf6b1f18149a4f6c8ec4e2d90adec643),
      [#32669](https://github.com/open-webui/open-webui/issues/32669)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4D6 **Reading files in pages.** The model's file reading tools
      now return every part of a file or knowledge base file read in pages with line
      numbers on, where some text between pages was skipped, and asking for only an
      end line now reads from the first line up to it, where the model got the same
      opening part back and kept retrying. [#33155](https://github.com/open-webui/open-webui/pull/33155),
      [Commit](https://github.com/open-webui/open-webui/commit/a01b36afe80983ca878b2c4dcdc25f8559a25308),
      [#33099](https://github.com/open-webui/open-webui/issues/33099), [#33154](https://github.com/open-webui/open-webui/pull/33154),
      [Commit](https://github.com/open-webui/open-webui/commit/d378fe81cb7e6bde2e4766cc5be1e0a45a320d3b),
      [#33100](https://github.com/open-webui/open-webui/issues/33100)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F648 **Base models after publishing.** Hiding, toggling or editing
      a base model right after making it public in Admin Settings > Models is now
      saved. [#32655](https://github.com/open-webui/open-webui/pull/32655), [Commit](https://github.com/open-webui/open-webui/commit/d8bef1ef90391647d2d34dffade63484f70e5c83),
      [#32654](https://github.com/open-webui/open-webui/issues/32654)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: ❓ **Clearer Ask User error.** When a model sends the Ask User questions
      as something other than a list, such as a JSON string, it now gets an error
      saying they must be an array of question objects instead of "ask_user requires
      1-3 questions", which made models repeat the same call. [#32727](https://github.com/open-webui/open-webui/pull/32727),
      [Commit](https://github.com/open-webui/open-webui/commit/794e57cf7ed29e0bf00a66a825c1d0b9682845b4),
      [#32662](https://github.com/open-webui/open-webui/issues/32662)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F501 **FastMCP list results sent once.** List results from tools
      on servers built with the standalone FastMCP package now reach the model once
      instead of twice, as text and as structured data. [#32726](https://github.com/open-webui/open-webui/pull/32726),
      [Commit](https://github.com/open-webui/open-webui/commit/217766ed0f53bde167cb80b115f7eb79664ffe5a),
      [#32719](https://github.com/open-webui/open-webui/issues/32719)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F9E0 **Reasoning replay with Azure.** Reasoning models on Azure
      OpenAI through the Responses API no longer fail with an \"Unknown parameter\"
      error on the request after they think and then call a tool. [Commit](https://github.com/open-webui/open-webui/commit/d1705c10788242b4d1a49042318a577877042469),
      [#32805](https://github.com/open-webui/open-webui/issues/32805)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F6AB **Model import reports taken IDs.** Importing models on the
      Workspace Models page now stops with an error at a model whose ID belongs to
      another user's model the importer cannot edit or, for non-admins, to a connection
      model, where that model was skipped without a message. [#32866](https://github.com/open-webui/open-webui/pull/32866),
      [Commit](https://github.com/open-webui/open-webui/commit/cb7d7e851d160bfc866aca9385c8a8013dd10192)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001FAE5 **Multi-model hover previews.** Sidebar hover previews of a
      chat with replies from several models now show one reply at full width, where
      every reply was squeezed into the card. [Commit](https://github.com/open-webui/open-webui/commit/35b51e09eab0942470cb9dce8f97fb00b9b96f2c),
      [#32858](https://github.com/open-webui/open-webui/issues/32858)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F579️ **Model controls for all users.** Anyone with access to a
      model can now pick its model control options, such as a Thinking level, and
      parameters saved to an account are no longer filtered by the Allow Chat Controls
      and Allow Chat Params permissions, which now only hide the Chat Controls and
      Advanced Parameters panels. [#32860](https://github.com/open-webui/open-webui/pull/32860),
      [Commit](https://github.com/open-webui/open-webui/commit/db5b8749448c5cb2a1e42f1bd0c01213bc2c31d1),
      [#32626](https://github.com/open-webui/open-webui/issues/32626)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 16-model-support-changes-in-v0-12-4
  source_release: open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79
  source_type: github_releases
  theme: model-support
  title: 16 Model Support changes in v0.12.4
  type: change
related_changes:
- '[[Changes/Qoder/2026-10-23-2-model-support-changes-in-qoder-0-4-11|2 Model Support
  changes in Qoder 0.4.11]]'
- '[[Changes/Ollama/2026-10-24-d3-https-ollama-com-library-d3-brings-vllm-semantic-router-s-decision-models-to|d3((source
  link) brings vLLM Semantic Router''s decision models…]]'
- '[[Changes/OpenClaw/2026-10-24-2-model-support-changes-in-v2026-10-7|2 Model Support
  changes in v2026.10.7]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79]]'
source_type: github_releases
theme: model-support
title: 16 Model Support changes in v0.12.4
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Model Support changes in v0.12.4

**Open WebUI** · 2026-10-25 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.4) · from [[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|v0.12.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎯 **Load selected skills on demand.** Administrators can turn on "Load selected skills on demand" under Admin Settings > General or set "ENABLE_SKILL_LAZY_LOADING", so skills selected in the chat or attached to a model are only listed for the model to load when it needs them instead of sending their full instructions with every message, while skills mentioned in the message still load right away, and it is off by default and needs the built-in Skills tool. [Commit](https://github.com/open-webui/open-webui/commit/079fb19e75f8be4b44fada0c755cf383b21a625b)

> 🪪 **Profile cards across the workspace.** Hovering an owner's name in the workspace lists of models, knowledge, prompts, skills and tools and in admin Functions now opens their profile card instead of an email tooltip, with their profile picture next to the name, profile pictures in access settings, version history and the Analytics user list open the card too and the Notes list shows each owner's profile picture. [Commit](https://github.com/open-webui/open-webui/commit/02974f41e9b7c9d34f2cd7c664c2a04fd6ac12ae), [Commit](https://github.com/open-webui/open-webui/commit/72cc79b8f336a753b6e75e0f3415630601b14759), [Commit](https://github.com/open-webui/open-webui/commit/ba34b1c47c1d054d2f9c498d0aed862ec06da41a), [Commit](https://github.com/open-webui/open-webui/commit/4491e60a296c89b11f22a43f416ea04770fd687f), [Commit](https://github.com/open-webui/open-webui/commit/0de8d03c625739ed3fe5e5f2a33de79a760238bd), [Commit](https://github.com/open-webui/open-webui/commit/0628670f56133d2cdc20c59b06fbb9de36932eb9)

> ✍️ **Note edits by text.** The model can now edit a note by finding and replacing exact text instead of only by character offsets, picking one match or all of them and getting the positions and surrounding text back when a match is ambiguous. [Commit](https://github.com/open-webui/open-webui/commit/243ef36c496714d9dd855de9fd261daa43caddb9), [#32752](https://github.com/open-webui/open-webui/issues/32752)

> 📈 **Analytics by tokens.** The Admin Analytics dashboard now ranks models and users by tokens by default with a switch back to messages, and its usage chart adds volume and activity views, a single model view, a comparison with the previous period, a choice of time steps and Year to date and Last 12 months ranges. [Commit](https://github.com/open-webui/open-webui/commit/131ddc32ecaeb06f9aa8740ff004710bacef72e0), [Commit](https://github.com/open-webui/open-webui/commit/06c17834ee3168b922f1b8a935b9dd76884b8fda), [Commit](https://github.com/open-webui/open-webui/commit/dc2ac86060e583f7374dd86f32f374a0b956bb8b), [Commit](https://github.com/open-webui/open-webui/commit/3539ad63213d13865a87a4db64a9829fd7d3b1b4), [Commit](https://github.com/open-webui/open-webui/commit/08bfaa4be67f6f87878b2209d568a648818506a7), [Commit](https://github.com/open-webui/open-webui/commit/06c382e5d223ba1b35dc0b1306c71da489c632b0)

> 🪡 **More Concise and Add Details.** Choosing More Concise or Add Details or typing a suggestion under a reply now rewrites that reply, where the model got the instruction without the reply and answered it on its own, for example with "OK, I'll keep answers shorter". [#33084](https://github.com/open-webui/open-webui/pull/33084), [Commit](https://github.com/open-webui/open-webui/commit/c69e5a73c0de43691e502bfaa03285e4e8cec05d), [#33083](https://github.com/open-webui/open-webui/issues/33083)

> 🎨 **Images after tool approval.** Images the model generates after you answer its question or approve or reject a tool call now appear in the reply, where they were created but never shown and the model kept retrying with more hidden images. [#32680](https://github.com/open-webui/open-webui/pull/32680), [Commit](https://github.com/open-webui/open-webui/commit/93ba628f3a3cf7f275892f3f3e0375d5984b51a7), [#32678](https://github.com/open-webui/open-webui/issues/32678)

> 🧬 **Embeddings with Prefix ID.** The embeddings API now works with models from a connection that has a Prefix ID, where the provider rejected the prefixed model name as unknown. [#32724](https://github.com/open-webui/open-webui/pull/32724), [Commit](https://github.com/open-webui/open-webui/commit/c901bc39d31eb85af289743850f92848529d422b), [#32715](https://github.com/open-webui/open-webui/issues/32715)

> 🛠️ **Same-named tool functions.** When two attached tools have a function with the same name, the model can now call both, where only the first one could be called. [#32670](https://github.com/open-webui/open-webui/pull/32670), [Commit](https://github.com/open-webui/open-webui/commit/ab6976b5bf6b1f18149a4f6c8ec4e2d90adec643), [#32669](https://github.com/open-webui/open-webui/issues/32669)

> 📖 **Reading files in pages.** The model's file reading tools now return every part of a file or knowledge base file read in pages with line numbers on, where some text between pages was skipped, and asking for only an end line now reads from the first line up to it, where the model got the same opening part back and kept retrying. [#33155](https://github.com/open-webui/open-webui/pull/33155), [Commit](https://github.com/open-webui/open-webui/commit/a01b36afe80983ca878b2c4dcdc25f8559a25308), [#33099](https://github.com/open-webui/open-webui/issues/33099), [#33154](https://github.com/open-webui/open-webui/pull/33154), [Commit](https://github.com/open-webui/open-webui/commit/d378fe81cb7e6bde2e4766cc5be1e0a45a320d3b), [#33100](https://github.com/open-webui/open-webui/issues/33100)

> 🙈 **Base models after publishing.** Hiding, toggling or editing a base model right after making it public in Admin Settings > Models is now saved. [#32655](https://github.com/open-webui/open-webui/pull/32655), [Commit](https://github.com/open-webui/open-webui/commit/d8bef1ef90391647d2d34dffade63484f70e5c83), [#32654](https://github.com/open-webui/open-webui/issues/32654)

> ❓ **Clearer Ask User error.** When a model sends the Ask User questions as something other than a list, such as a JSON string, it now gets an error saying they must be an array of question objects instead of "ask_user requires 1-3 questions", which made models repeat the same call. [#32727](https://github.com/open-webui/open-webui/pull/32727), [Commit](https://github.com/open-webui/open-webui/commit/794e57cf7ed29e0bf00a66a825c1d0b9682845b4), [#32662](https://github.com/open-webui/open-webui/issues/32662)

> 🔁 **FastMCP list results sent once.** List results from tools on servers built with the standalone FastMCP package now reach the model once instead of twice, as text and as structured data. [#32726](https://github.com/open-webui/open-webui/pull/32726), [Commit](https://github.com/open-webui/open-webui/commit/217766ed0f53bde167cb80b115f7eb79664ffe5a), [#32719](https://github.com/open-webui/open-webui/issues/32719)

> 🧠 **Reasoning replay with Azure.** Reasoning models on Azure OpenAI through the Responses API no longer fail with an "Unknown parameter" error on the request after they think and then call a tool. [Commit](https://github.com/open-webui/open-webui/commit/d1705c10788242b4d1a49042318a577877042469), [#32805](https://github.com/open-webui/open-webui/issues/32805)

> 🚫 **Model import reports taken IDs.** Importing models on the Workspace Models page now stops with an error at a model whose ID belongs to another user's model the importer cannot edit or, for non-admins, to a connection model, where that model was skipped without a message. [#32866](https://github.com/open-webui/open-webui/pull/32866), [Commit](https://github.com/open-webui/open-webui/commit/cb7d7e851d160bfc866aca9385c8a8013dd10192)

> 🫥 **Multi-model hover previews.** Sidebar hover previews of a chat with replies from several models now show one reply at full width, where every reply was squeezed into the card. [Commit](https://github.com/open-webui/open-webui/commit/35b51e09eab0942470cb9dce8f97fb00b9b96f2c), [#32858](https://github.com/open-webui/open-webui/issues/32858)

> 🕹️ **Model controls for all users.** Anyone with access to a model can now pick its model control options, such as a Thinking level, and parameters saved to an account are no longer filtered by the Allow Chat Controls and Allow Chat Params permissions, which now only hide the Chat Controls and Advanced Parameters panels. [#32860](https://github.com/open-webui/open-webui/pull/32860), [Commit](https://github.com/open-webui/open-webui/commit/db5b8749448c5cb2a1e42f1bd0c01213bc2c31d1), [#32626](https://github.com/open-webui/open-webui/issues/32626)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-25-10-safety-and-privacy-changes-in-v0-12-4|10 Safety and Privacy changes in v0.12.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-25-13-interface-experience-changes-in-v0-12-4|13 Interface Experience changes in v0.12.4]] · Interface Experience
- [[Changes/Open WebUI/2026-10-25-images-settings-save-admins-can-now-save-images-settings-while-image-generation|🖌️ Images settings save. Admins can now save Images settings while Image…]] · Image Generation
- [[Changes/Open WebUI/2026-10-25-4-voice-and-audio-changes-in-v0-12-4|4 Voice and Audio changes in v0.12.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-25-4-context-window-changes-in-v0-12-4|4 Context Window changes in v0.12.4]] · Context Window
- [[Changes/Open WebUI/2026-10-25-5-apps-and-integrations-changes-in-v0-12-4|5 Apps and Integrations changes in v0.12.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-25-49-developer-workflow-changes-in-v0-12-4|49 Developer Workflow changes in v0.12.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-25-4-editor-experience-changes-in-v0-12-4|4 Editor Experience changes in v0.12.4]] · Editor Experience
- [[Changes/Open WebUI/2026-10-25-3-reliability-and-performance-changes-in-v0-12-4|3 Reliability and Performance changes in v0.12.4]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-25-5-account-and-access-changes-in-v0-12-4|5 Account and Access changes in v0.12.4]] · Account and Access
- [[Changes/Open WebUI/2026-10-25-3-files-and-data-changes-in-v0-12-4|3 Files and Data changes in v0.12.4]] · Files and Data
- [[Changes/Open WebUI/2026-10-25-shared-chat-pages-load-once-chats-opened-under-s-through-a-share-link-or-by-an-a|🔗 Shared chat pages load once. Chats opened under /s/, through a share link…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-25-web-search-settings-save-admins-can-now-save-web-search-settings-such-as-the-web|🌍 Web Search settings save. Admins can now save Web Search settings such…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-25-translation-updates-translations-for-korean-cebuano-thai-german-japanese-vietnam|🌐 Translation updates. Translations for Korean, Cebuano, Thai, German, Japanese…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-24 · OpenClaw · [[Changes/OpenClaw/2026-10-24-2-model-support-changes-in-v2026-10-7|2 Model Support changes in v2026.10.7]]
- Later: 2026-10-26 · ChatGPT · [[Changes/ChatGPT/2026-10-26-gpt-6-1-terra-is-rolling-out-in-chatgpt-work-and-codex-it-supports-a-range-of-ta|GPT-6.1 Terra]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-25-104f10&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-25-16-model-support-changes-in-v0-12-4.md%0ACard%20ID%3A%20open-webui-2026-10-25-104f10%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->