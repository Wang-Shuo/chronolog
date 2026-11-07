---
card_id: open-webui-2026-10-14-89e00e
date: '2026-10-14'
description: "Open WebUI · 2026-10-14 · Model Support: 9 changes in v0.12.1 — \U0001F4E3
  **Typed mentions in channels.** Writing @ name or #channel in a channel message
  without…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1374
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4ecdf547669f1a4c774c5e8583d7f212555404b27dfcb810ab0c649339744b1b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-14-89e00e
  comparison: ''
  date: '2026-10-14'
  description: 'Open WebUI — v0.12.1: 9 Model Support changes'
  evidence:
  - quote: "\U0001F4E3 **Typed mentions in channels.** Writing @ name or #channel
      in a channel message without picking from the list now turns it into a real
      mention when the name matches a member, model, app or channel, and mentions
      pasted from another message keep pointing at the same person. [Commit](https://github.com/open-webui/open-webui/commit/f9c524d31d7737239aa990751cca4705e3872cb8),
      [Commit](https://github.com/open-webui/open-webui/commit/ba3e2273586850f3c69f61d70bfa7e603f32634b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F46F **Message pairs for every model.** Generate Message Pair, Ctrl+Shift+Enter,
      now adds a placeholder reply for each selected model side by side, where only
      the first model got one, and the side-by-side view stays after a reload. [#32309](https://github.com/open-webui/open-webui/pull/32309)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F4CA **Input and output tokens in analytics.** The Analytics dashboard
      now shows model usage and user activity in one table with a Models and Users
      switch, and both lists show input, output and total tokens as separate columns
      that can each be sorted, where they showed a single Tokens column. [Commit](https://github.com/open-webui/open-webui/commit/00f12c0e47fb47b1318a20e97bacc753e769612b),
      [Commit](https://github.com/open-webui/open-webui/commit/21322d9cb192060b51857769c0ad9f9f14e1185d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001FA9F **Side-by-side replies after Regenerate.** Adding a second
      model and pressing Regenerate now keeps both replies side by side after a reload,
      where the second reply showed as another version of the first. [#32326](https://github.com/open-webui/open-webui/pull/32326),
      [#32325](https://github.com/open-webui/open-webui/issues/32325)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F5D2️ **Production versions with notes.** Setting an older model
      version as production now works when the model has a note attached as knowledge,
      where it failed with \"Referenced knowledge is unavailable\". [#32317](https://github.com/open-webui/open-webui/pull/32317),
      [#32316](https://github.com/open-webui/open-webui/issues/32316)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F441️ **Re-enabled models stay on.** In Admin Settings > Models,
      turning a model back on or showing it again now stays after a reload and the
      model appears in the chat model picker, where for a model never edited before
      the second change looked saved but was lost. [#32354](https://github.com/open-webui/open-webui/pull/32354),
      [#32353](https://github.com/open-webui/open-webui/issues/32353), [#32368](https://github.com/open-webui/open-webui/pull/32368),
      [#32365](https://github.com/open-webui/open-webui/issues/32365)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F50E **Clearer Top K descriptions.** The Top K and Top K Reranker
      descriptions in Admin Settings > Documents now say that Top K Reranker is the
      number of chunks the reranker passes to the model and that with hybrid search
      Top K is the number of candidates sent to the reranker, where the old text led
      admins to give the model far fewer chunks than intended. [#32225](https://github.com/open-webui/open-webui/pull/32225),
      [#32221](https://github.com/open-webui/open-webui/issues/32221)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F4C4 **Files from saved temporary chats.** After a temporary chat
      is saved, the model no longer tries to open a file attached in it and gets \"File
      not found\", since such a file was never stored and its text is already in the
      prompt. [Commit](https://github.com/open-webui/open-webui/commit/97a66ef73e84f9ebb4aa4324b8eac9aadeaca22e),
      [#32351](https://github.com/open-webui/open-webui/issues/32351)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: ✂️ **Deleting a message mid-chat.** Deleting a message in the middle of
      a chat no longer makes the model forget every earlier message while the chat
      still shows them. [#32332](https://github.com/open-webui/open-webui/pull/32332),
      [Commit](https://github.com/open-webui/open-webui/commit/29289f5ba67d39255837a6385e5394192733a12e),
      [#32331](https://github.com/open-webui/open-webui/issues/32331)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 9-model-support-changes-in-v0-12-1
  source_release: open-webui-2026-10-14-v0-12-1-github-412917560-ae297772
  source_type: github_releases
  theme: model-support
  title: 9 Model Support changes in v0.12.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-14-improved-the-note-claude-3-models-get-about-an-mentioned-pdf-so-they-less-often|Improved
  the note Claude 3 models get about an @-mentioned PDF, so they less often…]]'
- '[[Changes/GitHub Copilot CLI/2026-10-14-add-support-for-gemini-4-argon|Add support
  for Gemini 4 Argon]]'
- '[[Changes/Ollama/2026-10-14-decision-models-are-now-available-on-cloud-use-clef-cloud-and-clef-flash-cloud-t|Decision
  models are now available on cloud]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|open-webui-2026-10-14-v0-12-1-github-412917560-ae297772]]'
source_type: github_releases
theme: model-support
title: 9 Model Support changes in v0.12.1
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Model Support changes in v0.12.1

**Open WebUI** · 2026-10-14 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.1) · from [[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|v0.12.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📣 **Typed mentions in channels.** Writing @ name or #channel in a channel message without picking from the list now turns it into a real mention when the name matches a member, model, app or channel, and mentions pasted from another message keep pointing at the same person. [Commit](https://github.com/open-webui/open-webui/commit/f9c524d31d7737239aa990751cca4705e3872cb8), [Commit](https://github.com/open-webui/open-webui/commit/ba3e2273586850f3c69f61d70bfa7e603f32634b)

> 👯 **Message pairs for every model.** Generate Message Pair, Ctrl+Shift+Enter, now adds a placeholder reply for each selected model side by side, where only the first model got one, and the side-by-side view stays after a reload. [#32309](https://github.com/open-webui/open-webui/pull/32309)

> 📊 **Input and output tokens in analytics.** The Analytics dashboard now shows model usage and user activity in one table with a Models and Users switch, and both lists show input, output and total tokens as separate columns that can each be sorted, where they showed a single Tokens column. [Commit](https://github.com/open-webui/open-webui/commit/00f12c0e47fb47b1318a20e97bacc753e769612b), [Commit](https://github.com/open-webui/open-webui/commit/21322d9cb192060b51857769c0ad9f9f14e1185d)

> 🪟 **Side-by-side replies after Regenerate.** Adding a second model and pressing Regenerate now keeps both replies side by side after a reload, where the second reply showed as another version of the first. [#32326](https://github.com/open-webui/open-webui/pull/32326), [#32325](https://github.com/open-webui/open-webui/issues/32325)

> 🗒️ **Production versions with notes.** Setting an older model version as production now works when the model has a note attached as knowledge, where it failed with "Referenced knowledge is unavailable". [#32317](https://github.com/open-webui/open-webui/pull/32317), [#32316](https://github.com/open-webui/open-webui/issues/32316)

> 👁️ **Re-enabled models stay on.** In Admin Settings > Models, turning a model back on or showing it again now stays after a reload and the model appears in the chat model picker, where for a model never edited before the second change looked saved but was lost. [#32354](https://github.com/open-webui/open-webui/pull/32354), [#32353](https://github.com/open-webui/open-webui/issues/32353), [#32368](https://github.com/open-webui/open-webui/pull/32368), [#32365](https://github.com/open-webui/open-webui/issues/32365)

> 🔎 **Clearer Top K descriptions.** The Top K and Top K Reranker descriptions in Admin Settings > Documents now say that Top K Reranker is the number of chunks the reranker passes to the model and that with hybrid search Top K is the number of candidates sent to the reranker, where the old text led admins to give the model far fewer chunks than intended. [#32225](https://github.com/open-webui/open-webui/pull/32225), [#32221](https://github.com/open-webui/open-webui/issues/32221)

> 📄 **Files from saved temporary chats.** After a temporary chat is saved, the model no longer tries to open a file attached in it and gets "File not found", since such a file was never stored and its text is already in the prompt. [Commit](https://github.com/open-webui/open-webui/commit/97a66ef73e84f9ebb4aa4324b8eac9aadeaca22e), [#32351](https://github.com/open-webui/open-webui/issues/32351)

> ✂️ **Deleting a message mid-chat.** Deleting a message in the middle of a chat no longer makes the model forget every earlier message while the chat still shows them. [#32332](https://github.com/open-webui/open-webui/pull/32332), [Commit](https://github.com/open-webui/open-webui/commit/29289f5ba67d39255837a6385e5394192733a12e), [#32331](https://github.com/open-webui/open-webui/issues/32331)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-14-rich-ui-embed-console-errors-rich-ui-tool-embeds-no-longer-log-a-security-error|🧩 Rich UI embed console errors. Rich UI tool embeds no longer log a security…]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-14-6-developer-workflow-changes-in-v0-12-1|6 Developer Workflow changes in v0.12.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-14-translated-model-prompt-suggestions-editing-the-prompt-suggestions-of-a-model-th|💬 Translated model prompt suggestions. Editing the prompt suggestions of a model…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-14-tools-picked-in-new-chats-tools-picked-from-the-integrations-menu-the-web-search|🧰 Tools picked in new chats. Tools picked from the Integrations menu, the Web…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-14-2-context-window-changes-in-v0-12-1|2 Context Window changes in v0.12.1]] · Context Window
- [[Changes/Open WebUI/2026-10-14-3-account-and-access-changes-in-v0-12-1|3 Account and Access changes in v0.12.1]] · Account and Access
- [[Changes/Open WebUI/2026-10-14-save-hidden-on-others-messages-in-a-chat-shared-with-allow-replies-editing-a-mes|💾 Save hidden on others' messages. In a chat shared with Allow replies, editing…]] · Collaboration
- [[Changes/Open WebUI/2026-10-14-7-interface-experience-changes-in-v0-12-1|7 Interface Experience changes in v0.12.1]] · Interface Experience
- [[Changes/Open WebUI/2026-10-14-recurring-automations-run-once-automations-set-with-the-daily-weekly-or-monthly|📅 Recurring automations run once. Automations set with the Daily, Weekly…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-14-2-apps-and-integrations-changes-in-v0-12-1|2 Apps and Integrations changes in v0.12.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-14-4-editor-experience-changes-in-v0-12-1|4 Editor Experience changes in v0.12.1]] · Editor Experience
- [[Changes/Open WebUI/2026-10-14-memory-in-automations-automations-now-get-the-memory-tools-when-the-user-has-mem|🧠 Memory in automations. Automations now get the memory tools when the user has…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-14-2-reliability-and-performance-changes-in-v0-12-1|2 Reliability and Performance changes in v0.12.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-14-10-voice-and-audio-changes-in-v0-12-1|10 Voice and Audio changes in v0.12.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-14-11-other-changes-in-v0-12-1|11 other changes in v0.12.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-14 · Ollama · [[Changes/Ollama/2026-10-14-decision-models-are-now-available-on-cloud-use-clef-cloud-and-clef-flash-cloud-t|Decision models are now available on cloud]]
- Later: 2026-10-14 · Open WebUI · [[Changes/Open WebUI/2026-10-14-4-model-support-changes-in-v0-12-2|4 Model Support changes in v0.12.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-14-89e00e&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-14-9-model-support-changes-in-v0-12-1.md%0ACard%20ID%3A%20open-webui-2026-10-14-89e00e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->