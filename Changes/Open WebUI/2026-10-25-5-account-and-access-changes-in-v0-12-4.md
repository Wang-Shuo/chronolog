---
card_id: open-webui-2026-10-25-cb11d0
date: '2026-10-25'
description: "Open WebUI · 2026-10-25 · Account and Access: 5 changes in v0.12.4 —
  \U0001F4E7 **LDAP default email domain.** Administrators can now set a default email
  domain in the…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2280
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8ca90083def65587c1ad9fff939a6d8cbd5148e8731a26eb2ae605b810d28278
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-25-cb11d0
  comparison: ''
  date: '2026-10-25'
  description: 'Open WebUI — v0.12.4: 5 Account and Access changes'
  evidence:
  - quote: "\U0001F4E7 **LDAP default email domain.** Administrators can now set a
      default email domain in the LDAP settings or with \"LDAP_DEFAULT_EMAIL_DOMAIN\",
      so LDAP users without a mail attribute sign in with their username at that domain
      as their email address and into any existing account with that address, which
      is why the domain should be one you control. [Commit](https://github.com/open-webui/open-webui/commit/74fb7a8c56bd92e6603e71e74917a99597228d10),
      [#33001](https://github.com/open-webui/open-webui/issues/33001)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F510 **OAuth connections over the API.** Connections set to OAuth
      authentication now also send the user's OAuth token when the user calls the
      API with an API key or bearer token, like tool servers already did. [#32826](https://github.com/open-webui/open-webui/pull/32826),
      [Commit](https://github.com/open-webui/open-webui/commit/6367a3cc406b3417d1a2eb2bfde9f1b841d43150),
      [#32820](https://github.com/open-webui/open-webui/issues/32820)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4E3 **Faster channel posts.** Posting a message in a channel with
      many members online now returns in a fraction of a second, where it waited for
      every online member's login to be checked again first. [#32889](https://github.com/open-webui/open-webui/pull/32889),
      [Commit](https://github.com/open-webui/open-webui/commit/a9adb2b78ebccdd51543a47c285309e9b016a71c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F4F1 **Sign-in page on small screens.** The sign-in page can now
      be scrolled when it is taller than the screen, such as on phones with the keyboard
      open, where parts of the form could be out of reach. [Commit](https://github.com/open-webui/open-webui/commit/ffbe0ac12da8ca5af9da12f8f00c43e382300b4f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - quote: "\U0001F511 **OAuth 2.1 static MCP secrets.** MCP connections using OAuth
      2.1 (Static) now send the client secret through HTTP Basic authentication when
      the server does not take it as a form field, where servers such as X Ads that
      list the public client method first got no secret and rejected the sign-in.
      [#32818](https://github.com/open-webui/open-webui/pull/32818), [Commit](https://github.com/open-webui/open-webui/commit/21f770fb731ff24245bc9ca8c3c82bb4171e24cf),
      [#32813](https://github.com/open-webui/open-webui/issues/32813)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-account-and-access-changes-in-v0-12-4
  source_release: open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79
  source_type: github_releases
  theme: account-access
  title: 5 Account and Access changes in v0.12.4
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-23-the-amazon-bedrock-setup-wizard-is-now-enabled-by-default-with-api-key-entry-gro|The
  Amazon Bedrock setup wizard is now enabled by default, with API key entry…]]'
- '[[Changes/Dify/2026-10-23-6-account-and-access-changes-in-1-18-0|6 Account and
  Access changes in 1.18.0]]'
- '[[Changes/Windsurf/2026-10-24-a-saved-sign-in-keeps-working-after-updating-on-machines-where-the-editor-s-own|A
  saved sign-in keeps working after updating on machines where the editor''s own…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79]]'
source_type: github_releases
theme: account-access
title: 5 Account and Access changes in v0.12.4
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Account and Access changes in v0.12.4

**Open WebUI** · 2026-10-25 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.4) · from [[Releases/Open WebUI/open-webui-2026-10-25-v0-12-4-github-423239437-ffa84a79|v0.12.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📧 **LDAP default email domain.** Administrators can now set a default email domain in the LDAP settings or with "LDAP_DEFAULT_EMAIL_DOMAIN", so LDAP users without a mail attribute sign in with their username at that domain as their email address and into any existing account with that address, which is why the domain should be one you control. [Commit](https://github.com/open-webui/open-webui/commit/74fb7a8c56bd92e6603e71e74917a99597228d10), [#33001](https://github.com/open-webui/open-webui/issues/33001)

> 🔐 **OAuth connections over the API.** Connections set to OAuth authentication now also send the user's OAuth token when the user calls the API with an API key or bearer token, like tool servers already did. [#32826](https://github.com/open-webui/open-webui/pull/32826), [Commit](https://github.com/open-webui/open-webui/commit/6367a3cc406b3417d1a2eb2bfde9f1b841d43150), [#32820](https://github.com/open-webui/open-webui/issues/32820)

> 📣 **Faster channel posts.** Posting a message in a channel with many members online now returns in a fraction of a second, where it waited for every online member's login to be checked again first. [#32889](https://github.com/open-webui/open-webui/pull/32889), [Commit](https://github.com/open-webui/open-webui/commit/a9adb2b78ebccdd51543a47c285309e9b016a71c)

> 📱 **Sign-in page on small screens.** The sign-in page can now be scrolled when it is taller than the screen, such as on phones with the keyboard open, where parts of the form could be out of reach. [Commit](https://github.com/open-webui/open-webui/commit/ffbe0ac12da8ca5af9da12f8f00c43e382300b4f)

> 🔑 **OAuth 2.1 static MCP secrets.** MCP connections using OAuth 2.1 (Static) now send the client secret through HTTP Basic authentication when the server does not take it as a form field, where servers such as X Ads that list the public client method first got no secret and rejected the sign-in. [#32818](https://github.com/open-webui/open-webui/pull/32818), [Commit](https://github.com/open-webui/open-webui/commit/21f770fb731ff24245bc9ca8c3c82bb4171e24cf), [#32813](https://github.com/open-webui/open-webui/issues/32813)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-25-16-model-support-changes-in-v0-12-4|16 Model Support changes in v0.12.4]] · Model Support
- [[Changes/Open WebUI/2026-10-25-10-safety-and-privacy-changes-in-v0-12-4|10 Safety and Privacy changes in v0.12.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-25-13-interface-experience-changes-in-v0-12-4|13 Interface Experience changes in v0.12.4]] · Interface Experience
- [[Changes/Open WebUI/2026-10-25-images-settings-save-admins-can-now-save-images-settings-while-image-generation|🖌️ Images settings save. Admins can now save Images settings while Image…]] · Image Generation
- [[Changes/Open WebUI/2026-10-25-4-voice-and-audio-changes-in-v0-12-4|4 Voice and Audio changes in v0.12.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-25-4-context-window-changes-in-v0-12-4|4 Context Window changes in v0.12.4]] · Context Window
- [[Changes/Open WebUI/2026-10-25-5-apps-and-integrations-changes-in-v0-12-4|5 Apps and Integrations changes in v0.12.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-25-49-developer-workflow-changes-in-v0-12-4|49 Developer Workflow changes in v0.12.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-25-4-editor-experience-changes-in-v0-12-4|4 Editor Experience changes in v0.12.4]] · Editor Experience
- [[Changes/Open WebUI/2026-10-25-3-reliability-and-performance-changes-in-v0-12-4|3 Reliability and Performance changes in v0.12.4]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-25-3-files-and-data-changes-in-v0-12-4|3 Files and Data changes in v0.12.4]] · Files and Data
- [[Changes/Open WebUI/2026-10-25-shared-chat-pages-load-once-chats-opened-under-s-through-a-share-link-or-by-an-a|🔗 Shared chat pages load once. Chats opened under /s/, through a share link…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-25-web-search-settings-save-admins-can-now-save-web-search-settings-such-as-the-web|🌍 Web Search settings save. Admins can now save Web Search settings such…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-25-translation-updates-translations-for-korean-cebuano-thai-german-japanese-vietnam|🌐 Translation updates. Translations for Korean, Cebuano, Thai, German, Japanese…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-10-24 · Windsurf · [[Changes/Windsurf/2026-10-24-a-saved-sign-in-keeps-working-after-updating-on-machines-where-the-editor-s-own|A saved sign-in keeps working after updating on machines where the editor's own…]]
- Later: 2026-10-26 · Claude Code · [[Changes/Claude Code/2026-10-26-improved-the-message-shown-when-a-pasted-sign-in-code-is-refused-it-now-says-the|Improved the message shown when a pasted sign-in code is refused]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-25-cb11d0&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-25-5-account-and-access-changes-in-v0-12-4.md%0ACard%20ID%3A%20open-webui-2026-10-25-cb11d0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->