---
card_id: open-webui-2026-10-14-c992e2
date: '2026-10-14'
description: "Open WebUI · 2026-10-14 · Other changes: 11 changes in v0.12.1 — \U0001F310
  **Translation updates.** Translations for Portuguese (Brazil), Italian, Czech, Romanian…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 53d1f69f54bce3a0d2127c53178ebe3099caa5a1efd0dc95ede94f3002db8441
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-14-c992e2
  comparison: ''
  date: '2026-10-14'
  description: 'Open WebUI — v0.12.1: 11 other changes'
  evidence:
  - quote: "\U0001F310 **Translation updates.** Translations for Portuguese (Brazil),
      Italian, Czech, Romanian, Dutch, Ukrainian, Polish, Thai, Spanish, Malay, Persian,
      Korean, Arabic, Japanese, Indonesian, Russian, Vietnamese, Turkish, Hindi, German,
      Greek, Hungarian, Hebrew, Bulgarian, Swedish, Estonian, Norwegian Bokmål, Lithuanian,
      Croatian, Slovak, Bosnian, Danish, Slovenian, Galician, Latvian, Tibetan, Serbian,
      Bengali, Cebuano, Azerbaijani, Basque, Irish, Georgian, Kabyle, Punjabi, Faroese,
      Tamil, Uyghur, Urdu, Filipino and Turkmen were enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F4D1 **Page titles for external knowledge citations.** Citations
      from external knowledge bases such as Qdrant, Milvus or pgvector whose source
      is a web address now show the page title in the source list below the answer,
      matching the numbered markers in the text, where the full address was shown.
      [#32232](https://github.com/open-webui/open-webui/pull/32232), [#32231](https://github.com/open-webui/open-webui/issues/32231)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F9ED **Redis Sentinel master names with capital letters.** With
      Redis Sentinel, a master name with capital letters in \"REDIS_URL\", such as
      myMaster, the default of the OT-Container-Kit redis-operator, now works, where
      it was lowercased and every Redis call failed with \"No master found\". [#32234](https://github.com/open-webui/open-webui/pull/32234),
      [#31918](https://github.com/open-webui/open-webui/issues/31918)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F510 **Redis Sentinels with a password.** Redis Sentinels protected
      with a password now work, as the credentials in \"REDIS_URL\" and \"WEBSOCKET_REDIS_URL\"
      are also used for the Sentinels, where every Redis call failed with \"No master
      found\"; Sentinel credentials set in \"WEBSOCKET_REDIS_OPTIONS\" still take
      precedence. [#32241](https://github.com/open-webui/open-webui/pull/32241), [#32240](https://github.com/open-webui/open-webui/issues/32240)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F517 **External knowledge citation links.** Clicking the title or
      Content link of a citation from an external knowledge base such as Qdrant, Milvus
      or pgvector now opens the cited web page, or shows the title as plain text when
      the source is not a web address, where it led to a not found error. [#32233](https://github.com/open-webui/open-webui/pull/32233),
      [#32231](https://github.com/open-webui/open-webui/issues/32231)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F44E **Rating reason and comment kept.** The reason and comment
      saved in the rating form are no longer wiped a few seconds later when the generated
      tags arrive, both on the reply and in Admin Panel > Evaluations > Feedback.
      [#32334](https://github.com/open-webui/open-webui/pull/32334), [#32333](https://github.com/open-webui/open-webui/issues/32333)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F419 **GitHub skill imports with symlinks.** Importing a skill from
      a GitHub link now works when the repository has symlinks outside the skill folder,
      such as a CLAUDE.md link at the root, where it failed with \"Archives cannot
      contain links or special files\". [#32313](https://github.com/open-webui/open-webui/pull/32313),
      [#32312](https://github.com/open-webui/open-webui/issues/32312)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F4C2 **Open knowledge file stays open.** Deleting a folder in a
      knowledge base no longer closes the file open in the viewer unless the delete
      removed that file. [#32319](https://github.com/open-webui/open-webui/pull/32319),
      [#32318](https://github.com/open-webui/open-webui/issues/32318)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F4B2 **Dollar signs in Ask and Explain.** Ask and Explain on selected
      text now keep dollar signs such as \"$5\" or \"$&\" in the selected text and
      in your question, where they were dropped or replaced with other text. [#32356](https://github.com/open-webui/open-webui/pull/32356),
      [#32355](https://github.com/open-webui/open-webui/issues/32355)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F514 **Reminders for moved calendar events.** A calendar event moved
      to a new time after its reminder went out now reminds you again before the new
      start, where it never reminded again. [#32358](https://github.com/open-webui/open-webui/pull/32358),
      [#32357](https://github.com/open-webui/open-webui/issues/32357)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: '⚠️ **Database Migrations**: This release includes database schema changes;
      we strongly recommend backing up your database and all associated data before
      upgrading in production environments. If you are running a multi-worker, multi-server,
      or load-balanced deployment, all instances must be updated simultaneously, rolling
      updates are not supported and will cause application failures due to schema
      incompatibility.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 11-other-changes-in-v0-12-1
  source_release: open-webui-2026-10-14-v0-12-1-github-412917560-ae297772
  source_type: github_releases
  theme: uncategorized
  title: 11 other changes in v0.12.1
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|open-webui-2026-10-14-v0-12-1-github-412917560-ae297772]]'
source_type: github_releases
theme: uncategorized
title: 11 other changes in v0.12.1
type: change
---

<!-- chronolog:begin region="header" -->
# 11 other changes in v0.12.1

**Open WebUI** · 2026-10-14 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.1) · from [[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|v0.12.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🌐 **Translation updates.** Translations for Portuguese (Brazil), Italian, Czech, Romanian, Dutch, Ukrainian, Polish, Thai, Spanish, Malay, Persian, Korean, Arabic, Japanese, Indonesian, Russian, Vietnamese, Turkish, Hindi, German, Greek, Hungarian, Hebrew, Bulgarian, Swedish, Estonian, Norwegian Bokmål, Lithuanian, Croatian, Slovak, Bosnian, Danish, Slovenian, Galician, Latvian, Tibetan, Serbian, Bengali, Cebuano, Azerbaijani, Basque, Irish, Georgian, Kabyle, Punjabi, Faroese, Tamil, Uyghur, Urdu, Filipino and Turkmen were enhanced and expanded.

> 📑 **Page titles for external knowledge citations.** Citations from external knowledge bases such as Qdrant, Milvus or pgvector whose source is a web address now show the page title in the source list below the answer, matching the numbered markers in the text, where the full address was shown. [#32232](https://github.com/open-webui/open-webui/pull/32232), [#32231](https://github.com/open-webui/open-webui/issues/32231)

> 🧭 **Redis Sentinel master names with capital letters.** With Redis Sentinel, a master name with capital letters in "REDIS_URL", such as myMaster, the default of the OT-Container-Kit redis-operator, now works, where it was lowercased and every Redis call failed with "No master found". [#32234](https://github.com/open-webui/open-webui/pull/32234), [#31918](https://github.com/open-webui/open-webui/issues/31918)

> 🔐 **Redis Sentinels with a password.** Redis Sentinels protected with a password now work, as the credentials in "REDIS_URL" and "WEBSOCKET_REDIS_URL" are also used for the Sentinels, where every Redis call failed with "No master found"; Sentinel credentials set in "WEBSOCKET_REDIS_OPTIONS" still take precedence. [#32241](https://github.com/open-webui/open-webui/pull/32241), [#32240](https://github.com/open-webui/open-webui/issues/32240)

> 🔗 **External knowledge citation links.** Clicking the title or Content link of a citation from an external knowledge base such as Qdrant, Milvus or pgvector now opens the cited web page, or shows the title as plain text when the source is not a web address, where it led to a not found error. [#32233](https://github.com/open-webui/open-webui/pull/32233), [#32231](https://github.com/open-webui/open-webui/issues/32231)

> 👎 **Rating reason and comment kept.** The reason and comment saved in the rating form are no longer wiped a few seconds later when the generated tags arrive, both on the reply and in Admin Panel > Evaluations > Feedback. [#32334](https://github.com/open-webui/open-webui/pull/32334), [#32333](https://github.com/open-webui/open-webui/issues/32333)

> 🐙 **GitHub skill imports with symlinks.** Importing a skill from a GitHub link now works when the repository has symlinks outside the skill folder, such as a CLAUDE.md link at the root, where it failed with "Archives cannot contain links or special files". [#32313](https://github.com/open-webui/open-webui/pull/32313), [#32312](https://github.com/open-webui/open-webui/issues/32312)

> 📂 **Open knowledge file stays open.** Deleting a folder in a knowledge base no longer closes the file open in the viewer unless the delete removed that file. [#32319](https://github.com/open-webui/open-webui/pull/32319), [#32318](https://github.com/open-webui/open-webui/issues/32318)

> 💲 **Dollar signs in Ask and Explain.** Ask and Explain on selected text now keep dollar signs such as "$5" or "$&" in the selected text and in your question, where they were dropped or replaced with other text. [#32356](https://github.com/open-webui/open-webui/pull/32356), [#32355](https://github.com/open-webui/open-webui/issues/32355)

> 🔔 **Reminders for moved calendar events.** A calendar event moved to a new time after its reminder went out now reminds you again before the new start, where it never reminded again. [#32358](https://github.com/open-webui/open-webui/pull/32358), [#32357](https://github.com/open-webui/open-webui/issues/32357)

> ⚠️ **Database Migrations**: This release includes database schema changes; we strongly recommend backing up your database and all associated data before upgrading in production environments. If you are running a multi-worker, multi-server, or load-balanced deployment, all instances must be updated simultaneously, rolling updates are not supported and will cause application failures due to schema incompatibility.

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
- [[Changes/Open WebUI/2026-10-14-2-apps-and-integrations-changes-in-v0-12-1|2 Apps and Integrations changes in v0.12.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-14-4-editor-experience-changes-in-v0-12-1|4 Editor Experience changes in v0.12.1]] · Editor Experience
- [[Changes/Open WebUI/2026-10-14-memory-in-automations-automations-now-get-the-memory-tools-when-the-user-has-mem|🧠 Memory in automations. Automations now get the memory tools when the user has…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-14-2-reliability-and-performance-changes-in-v0-12-1|2 Reliability and Performance changes in v0.12.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-14-10-voice-and-audio-changes-in-v0-12-1|10 Voice and Audio changes in v0.12.1]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-14-c992e2&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-14-11-other-changes-in-v0-12-1.md%0ACard%20ID%3A%20open-webui-2026-10-14-c992e2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->