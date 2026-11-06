---
card_id: open-webui-2026-10-14-6ee8a3
date: '2026-10-14'
description: "Open WebUI · 2026-10-14 · Context Window: 2 changes in v0.12.1 — \U0001F5DC️
  **Compaction during long tool runs.** Context compaction now also runs during a
  long series…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1259
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dc8026d598193e7ebbe2335b02aecb77826bc781e2ef24e2b74c1509828790dd
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-14-6ee8a3
  comparison: ''
  date: '2026-10-14'
  description: 'Open WebUI — v0.12.1: 2 Context Window changes'
  evidence:
  - quote: "\U0001F5DC️ **Compaction during long tool runs.** Context compaction now
      also runs during a long series of tool calls based on the token usage the provider
      reports, and the compacted summary is kept with the reply so the next message
      continues from it, where long tool runs could hit the model's context limit.
      [Commit](https://github.com/open-webui/open-webui/commit/bcf540a98935566537b05911a6bb4ace03c5648d),
      [#32306](https://github.com/open-webui/open-webui/issues/32306)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F4D6 **Large skills load as a preview.** With the Skills builtin
      tools on, a skill whose SKILL.md is longer than 20,000 characters now reaches
      the model as a 5,000 character opening preview, and the model reads on from
      where the preview ends with read_skill_file, which now returns up to 20,000
      characters per call instead of 100,000, and the new grep_skill_files tool lets
      the model search a skill's files for a word or pattern, keeping long skills
      from filling the context. [Commit](https://github.com/open-webui/open-webui/commit/200b9514917a070c88d112e3c0aba9df3322c5e1),
      [Commit](https://github.com/open-webui/open-webui/commit/d34f73066d837428ab198e14f285c09ad1ce2450),
      [Commit](https://github.com/open-webui/open-webui/commit/c314239558cdb47e4d1eaddf011bb4178e0742c2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-context-window-changes-in-v0-12-1
  source_release: open-webui-2026-10-14-v0-12-1-github-412917560-ae297772
  source_type: github_releases
  theme: context-window
  title: 2 Context Window changes in v0.12.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-14-2-context-window-changes-in-v2-1-299|2 Context
  Window changes in v2.1.299]]'
- '[[Changes/Claude Code/2026-10-14-added-usage-warnings-for-max-effort-workflows-always-on-context-and-large-tool-r|Added
  /usage warnings for max effort, workflows, always-on context and large tool…]]'
- '[[Changes/Ollama/2026-10-14-nvidia-nemotron-3-5-super-https-ollama-com-library-nemotron-3-5-super-is-a-visio|NVIDIA
  Nemotron 3.5 Super((source link)]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|open-webui-2026-10-14-v0-12-1-github-412917560-ae297772]]'
source_type: github_releases
theme: context-window
title: 2 Context Window changes in v0.12.1
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Context Window changes in v0.12.1

**Open WebUI** · 2026-10-14 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.1) · from [[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|v0.12.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗜️ **Compaction during long tool runs.** Context compaction now also runs during a long series of tool calls based on the token usage the provider reports, and the compacted summary is kept with the reply so the next message continues from it, where long tool runs could hit the model's context limit. [Commit](https://github.com/open-webui/open-webui/commit/bcf540a98935566537b05911a6bb4ace03c5648d), [#32306](https://github.com/open-webui/open-webui/issues/32306)

> 📖 **Large skills load as a preview.** With the Skills builtin tools on, a skill whose SKILL.md is longer than 20,000 characters now reaches the model as a 5,000 character opening preview, and the model reads on from where the preview ends with read_skill_file, which now returns up to 20,000 characters per call instead of 100,000, and the new grep_skill_files tool lets the model search a skill's files for a word or pattern, keeping long skills from filling the context. [Commit](https://github.com/open-webui/open-webui/commit/200b9514917a070c88d112e3c0aba9df3322c5e1), [Commit](https://github.com/open-webui/open-webui/commit/d34f73066d837428ab198e14f285c09ad1ce2450), [Commit](https://github.com/open-webui/open-webui/commit/c314239558cdb47e4d1eaddf011bb4178e0742c2)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-14-rich-ui-embed-console-errors-rich-ui-tool-embeds-no-longer-log-a-security-error|🧩 Rich UI embed console errors. Rich UI tool embeds no longer log a security…]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-14-6-developer-workflow-changes-in-v0-12-1|6 Developer Workflow changes in v0.12.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-14-translated-model-prompt-suggestions-editing-the-prompt-suggestions-of-a-model-th|💬 Translated model prompt suggestions. Editing the prompt suggestions of a model…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-14-tools-picked-in-new-chats-tools-picked-from-the-integrations-menu-the-web-search|🧰 Tools picked in new chats. Tools picked from the Integrations menu, the Web…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-14-3-account-and-access-changes-in-v0-12-1|3 Account and Access changes in v0.12.1]] · Account and Access
- [[Changes/Open WebUI/2026-10-14-save-hidden-on-others-messages-in-a-chat-shared-with-allow-replies-editing-a-mes|💾 Save hidden on others' messages. In a chat shared with Allow replies, editing…]] · Collaboration
- [[Changes/Open WebUI/2026-10-14-9-model-support-changes-in-v0-12-1|9 Model Support changes in v0.12.1]] · Model Support
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
## Nearby in Context Window

- Earlier: 2026-10-14 · Ollama · [[Changes/Ollama/2026-10-14-nvidia-nemotron-3-5-super-https-ollama-com-library-nemotron-3-5-super-is-a-visio|NVIDIA Nemotron 3.5 Super((source link)]]
- Later: 2026-10-14 · Open WebUI · [[Changes/Open WebUI/2026-10-14-per-chat-terminal-file-actions-with-the-open-terminal-chat-context-set-to-per-ch|🖥️ Per chat terminal file actions. With the Open Terminal chat context set…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-14-6ee8a3&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-14-2-context-window-changes-in-v0-12-1.md%0ACard%20ID%3A%20open-webui-2026-10-14-6ee8a3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->