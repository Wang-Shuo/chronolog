---
card_id: open-webui-2026-10-14-c4f8be
date: '2026-10-14'
description: "Open WebUI · 2026-10-14 · Apps and Integrations: 2 changes in v0.12.1
  — \U0001F5C3️ **File list for pipes and tools without attachments.** Pipes and tools
  now get an…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1301
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 21dca0ea269ea9b08f2a62789ed1ed1db6e9600e8a3018161780b9899794197d
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-14-c4f8be
  comparison: ''
  date: '2026-10-14'
  description: 'Open WebUI — v0.12.1: 2 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F5C3️ **File list for pipes and tools without attachments.** Pipes
      and tools now get an empty file list on messages without attachments, where
      they got None and plugins that loop over the files failed. [#32380](https://github.com/open-webui/open-webui/pull/32380),
      [#32379](https://github.com/open-webui/open-webui/issues/32379)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F50C **MCP connection errors in the logs.** When an MCP server fails
      to connect during a chat, the reason, such as a refused connection or a 401
      from the server, is now logged as an error, where it was only logged at debug
      level and never reached the logs of a default install. [#32229](https://github.com/open-webui/open-webui/pull/32229),
      [#32213](https://github.com/open-webui/open-webui/issues/32213)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-apps-and-integrations-changes-in-v0-12-1
  source_release: open-webui-2026-10-14-v0-12-1-github-412917560-ae297772
  source_type: github_releases
  theme: apps-integrations
  title: 2 Apps and Integrations changes in v0.12.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-14-19-apps-and-integrations-changes-in-v2-1-299|19
  Apps and Integrations changes in v2.1.299]]'
- '[[Changes/GitHub Copilot CLI/2026-10-14-2-apps-and-integrations-changes-in-v1-0-98|2
  Apps and Integrations changes in v1.0.98]]'
- '[[Changes/Lovable/2026-10-14-connect-your-app-to-bing-webmaster-tools|Connect your
  app to Bing Webmaster Tools]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|open-webui-2026-10-14-v0-12-1-github-412917560-ae297772]]'
source_type: github_releases
theme: apps-integrations
title: 2 Apps and Integrations changes in v0.12.1
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Apps and Integrations changes in v0.12.1

**Open WebUI** · 2026-10-14 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.1) · from [[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|v0.12.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗃️ **File list for pipes and tools without attachments.** Pipes and tools now get an empty file list on messages without attachments, where they got None and plugins that loop over the files failed. [#32380](https://github.com/open-webui/open-webui/pull/32380), [#32379](https://github.com/open-webui/open-webui/issues/32379)

> 🔌 **MCP connection errors in the logs.** When an MCP server fails to connect during a chat, the reason, such as a refused connection or a 401 from the server, is now logged as an error, where it was only logged at debug level and never reached the logs of a default install. [#32229](https://github.com/open-webui/open-webui/pull/32229), [#32213](https://github.com/open-webui/open-webui/issues/32213)

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
- [[Changes/Open WebUI/2026-10-14-9-model-support-changes-in-v0-12-1|9 Model Support changes in v0.12.1]] · Model Support
- [[Changes/Open WebUI/2026-10-14-7-interface-experience-changes-in-v0-12-1|7 Interface Experience changes in v0.12.1]] · Interface Experience
- [[Changes/Open WebUI/2026-10-14-recurring-automations-run-once-automations-set-with-the-daily-weekly-or-monthly|📅 Recurring automations run once. Automations set with the Daily, Weekly…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-14-4-editor-experience-changes-in-v0-12-1|4 Editor Experience changes in v0.12.1]] · Editor Experience
- [[Changes/Open WebUI/2026-10-14-memory-in-automations-automations-now-get-the-memory-tools-when-the-user-has-mem|🧠 Memory in automations. Automations now get the memory tools when the user has…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-14-2-reliability-and-performance-changes-in-v0-12-1|2 Reliability and Performance changes in v0.12.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-14-10-voice-and-audio-changes-in-v0-12-1|10 Voice and Audio changes in v0.12.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-14-11-other-changes-in-v0-12-1|11 other changes in v0.12.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-14 · Lovable · [[Changes/Lovable/2026-10-14-connect-your-app-to-bing-webmaster-tools|Connect your app to Bing Webmaster Tools]]
- Later: 2026-10-15 · Codex CLI · [[Changes/Codex CLI/2026-10-15-15-apps-and-integrations-changes-in-rust-v0-163-0|15 Apps and Integrations changes in rust-v0.163.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-14-c4f8be&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-14-2-apps-and-integrations-changes-in-v0-12-1.md%0ACard%20ID%3A%20open-webui-2026-10-14-c4f8be%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->