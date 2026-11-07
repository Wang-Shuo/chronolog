---
card_id: open-webui-2026-10-16-2807d6
date: '2026-10-16'
description: "Open WebUI · 2026-10-16 · Model Support: 3 changes in v0.12.3 — \U0001F4CF
  **Skill read limits.** Administrators can set how many characters of a skill the
  model reads…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1376
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 53d59a7ba84ed241703c806baa71aa5f4b86a8e10048716aa9bf26debd265e48
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-16-2807d6
  comparison: ''
  date: '2026-10-16'
  description: 'Open WebUI — v0.12.3: 3 Model Support changes'
  evidence:
  - quote: "\U0001F4CF **Skill read limits.** Administrators can set how many characters
      of a skill the model reads at once and how long the preview of longer instructions
      is, under Admin Settings > General with \"Skill Read Limit\" and \"Skill Preview
      Length\" or the \"SKILL_CONTENT_MAX_CHARS\" and \"SKILL_PREVIEW_MAX_CHARS\"
      environment variables, which default to 20000 and 5000. [Commit](https://github.com/open-webui/open-webui/commit/92e64c1d59cdd99b5f33a108186a1d368daab964)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: ⏩ **Continue Response with several models.** Continue Response now continues
      the reply it was clicked under, where in a chat with several models it could
      extend another model's reply. [#32456](https://github.com/open-webui/open-webui/pull/32456),
      [Commit](https://github.com/open-webui/open-webui/commit/3c82fda4e813e00d33ca16a8ddd61596296a2066),
      [#32455](https://github.com/open-webui/open-webui/issues/32455)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F3AF **Model skills now load their full instructions.** With the
      Skills builtin tool on, skills attached to a model in the model editor, which
      every new chat pre-selects, and skills picked from the chat input menu now send
      their full instructions with each message, where they were only listed by name
      and description for the model to load with view_skill; deployments that attached
      skills to models only to make them available should remove them from the model
      to avoid the extra prompt length, since every skill the user can read is listed
      for the model anyway. [Commit](https://github.com/open-webui/open-webui/commit/5cf7c03332ad3fd68ddba276b94a87f8cea25c7a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-model-support-changes-in-v0-12-3
  source_release: open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v0.12.3
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-10-16-gpt-6-pro-in-the-chat-tab-now-offers|GPT-6 Pro in
  the chat tab now offers]]'
- '[[Changes/Claude Code/2026-10-16-improved-the-message-when-a-background-session-reopened-from-another-folder-has|Improved
  the message when a background session reopened from another folder has no…]]'
- '[[Changes/Cline/2026-10-16-4-model-support-changes-in-v4-1-25|4 Model Support changes
  in v4.1.25]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d|open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v0.12.3
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v0.12.3

**Open WebUI** · 2026-10-16 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.3) · from [[Releases/Open WebUI/open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d|v0.12.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📏 **Skill read limits.** Administrators can set how many characters of a skill the model reads at once and how long the preview of longer instructions is, under Admin Settings > General with "Skill Read Limit" and "Skill Preview Length" or the "SKILL_CONTENT_MAX_CHARS" and "SKILL_PREVIEW_MAX_CHARS" environment variables, which default to 20000 and 5000. [Commit](https://github.com/open-webui/open-webui/commit/92e64c1d59cdd99b5f33a108186a1d368daab964)

> ⏩ **Continue Response with several models.** Continue Response now continues the reply it was clicked under, where in a chat with several models it could extend another model's reply. [#32456](https://github.com/open-webui/open-webui/pull/32456), [Commit](https://github.com/open-webui/open-webui/commit/3c82fda4e813e00d33ca16a8ddd61596296a2066), [#32455](https://github.com/open-webui/open-webui/issues/32455)

> 🎯 **Model skills now load their full instructions.** With the Skills builtin tool on, skills attached to a model in the model editor, which every new chat pre-selects, and skills picked from the chat input menu now send their full instructions with each message, where they were only listed by name and description for the model to load with view_skill; deployments that attached skills to models only to make them available should remove them from the model to avoid the extra prompt length, since every skill the user can read is listed for the model anyway. [Commit](https://github.com/open-webui/open-webui/commit/5cf7c03332ad3fd68ddba276b94a87f8cea25c7a)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-16-built-in-tools-turned-back-on-stay-on-a-built-in-tool-such-as-memory-that-is-off|🧰 Built-in tools turned back on stay on. A built-in tool such as Memory…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-16-20-developer-workflow-changes-in-v0-12-3|20 Developer Workflow changes in v0.12.3]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-16-4-files-and-data-changes-in-v0-12-3|4 Files and Data changes in v0.12.3]] · Files and Data
- [[Changes/Open WebUI/2026-10-16-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-16-2-account-and-access-changes-in-v0-12-3|2 Account and Access changes in v0.12.3]] · Account and Access
- [[Changes/Open WebUI/2026-10-16-2-enterprise-and-administration-changes-in-v0-12-3|2 Enterprise and Administration changes in v0.12.3]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-16-2-context-window-changes-in-v0-12-3|2 Context Window changes in v0.12.3]] · Context Window
- [[Changes/Open WebUI/2026-10-16-clear-input-selections-shortcut-clearing-the-model-override-selected-tools-and-f|🧹 Clear Input Selections shortcut. Clearing the model override, selected tools…]] · Image Generation
- [[Changes/Open WebUI/2026-10-16-built-in-tools-with-a-custom-tools-parameter-a-model-with-a-custom-parameter-nam|🧩 Built-in tools with a custom tools parameter. A model with a custom parameter…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-16-4-interface-experience-changes-in-v0-12-3|4 Interface Experience changes in v0.12.3]] · Interface Experience
- [[Changes/Open WebUI/2026-10-16-2-editor-experience-changes-in-v0-12-3|2 Editor Experience changes in v0.12.3]] · Editor Experience
- [[Changes/Open WebUI/2026-10-16-2-safety-and-privacy-changes-in-v0-12-3|2 Safety and Privacy changes in v0.12.3]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-16-2-collaboration-changes-in-v0-12-3|2 Collaboration changes in v0.12.3]] · Collaboration
- [[Changes/Open WebUI/2026-10-16-translation-updates-translations-for-portuguese-brazil-chinese-traditional-arabi|🌐 Translation updates. Translations for Portuguese (Brazil), Chinese…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-16 · Cline · [[Changes/Cline/2026-10-16-4-model-support-changes-in-v4-1-25|4 Model Support changes in v4.1.25]]
- Later: 2026-10-16 · OpenClaw · [[Changes/OpenClaw/2026-10-16-openai-reasoning-with-tools-fixed-tool-call-failures-and-reasoning-being-switche|OpenAI reasoning with tools]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-16-2807d6&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-16-3-model-support-changes-in-v0-12-3.md%0ACard%20ID%3A%20open-webui-2026-10-16-2807d6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->