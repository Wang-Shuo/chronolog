---
card_id: open-webui-2026-10-14-796135
date: '2026-10-14'
description: "Open WebUI · 2026-10-14 · Account and Access: 3 changes in v0.12.1 —
  \U0001F501 **No reconnect loop after sign-in.** A tab where you signed in without
  reloading the…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2269
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 037d6f9c2229aa784272ca504e241d4caf7bc4c3cec92b1b78ab136c3a8cc00b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-14-796135
  comparison: ''
  date: '2026-10-14'
  description: 'Open WebUI — v0.12.1: 3 Account and Access changes'
  evidence:
  - quote: "\U0001F501 **No reconnect loop after sign-in.** A tab where you signed
      in without reloading the page now reconnects signed in after a connection drop,
      such as sleep, a network change or a server restart, where since 0.12.0 it reconnected
      several times per second until the page was reloaded and put heavy load on the
      server. [#32341](https://github.com/open-webui/open-webui/pull/32341), [#32338](https://github.com/open-webui/open-webui/issues/32338)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F329️ **MCP OAuth behind Cloudflare.** Connecting an OAuth MCP tool
      server such as Canva now works when the provider's sign-in page is behind Cloudflare
      bot protection, where it failed with \"OAuth client registration is still invalid
      after re-registration\". [#32364](https://github.com/open-webui/open-webui/pull/32364),
      [#32363](https://github.com/open-webui/open-webui/issues/32363)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  - quote: "\U0001F511 **SSO sign in for SCIM users.** Users created through SCIM
      can sign in with SSO again, where they got \"401 Invalid authentication request\"
      since 0.12.0 because no sign-in record was created for them; a database migration
      adds the missing record for existing accounts without giving them a usable password,
      SCIM email changes now also update the sign-in email and deleting a user through
      SCIM removes the sign-in record as well. [Commit](https://github.com/open-webui/open-webui/commit/00f12c0e47fb47b1318a20e97bacc753e769612b),
      [#32347](https://github.com/open-webui/open-webui/issues/32347)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-account-and-access-changes-in-v0-12-1
  source_release: open-webui-2026-10-14-v0-12-1-github-412917560-ae297772
  source_type: github_releases
  theme: account-access
  title: 3 Account and Access changes in v0.12.1
  type: change
related_changes:
- '[[Changes/Lovable/2026-10-14-connect-your-apps-to-lovable-with-oauth|Connect your
  apps to Lovable with OAuth]]'
- '[[Changes/Lovable/2026-10-14-add-sign-in-with-lovable-to-any-website|Add Sign in
  with Lovable to any website]]'
- '[[Changes/Ollama/2026-10-14-clearer-error-messages-when-cloud-access-fails-sign-in-problems-payment-issues-i|Clearer
  error messages when cloud access fails]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|open-webui-2026-10-14-v0-12-1-github-412917560-ae297772]]'
source_type: github_releases
theme: account-access
title: 3 Account and Access changes in v0.12.1
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Account and Access changes in v0.12.1

**Open WebUI** · 2026-10-14 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.1) · from [[Releases/Open WebUI/open-webui-2026-10-14-v0-12-1-github-412917560-ae297772|v0.12.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔁 **No reconnect loop after sign-in.** A tab where you signed in without reloading the page now reconnects signed in after a connection drop, such as sleep, a network change or a server restart, where since 0.12.0 it reconnected several times per second until the page was reloaded and put heavy load on the server. [#32341](https://github.com/open-webui/open-webui/pull/32341), [#32338](https://github.com/open-webui/open-webui/issues/32338)

> 🌩️ **MCP OAuth behind Cloudflare.** Connecting an OAuth MCP tool server such as Canva now works when the provider's sign-in page is behind Cloudflare bot protection, where it failed with "OAuth client registration is still invalid after re-registration". [#32364](https://github.com/open-webui/open-webui/pull/32364), [#32363](https://github.com/open-webui/open-webui/issues/32363)

> 🔑 **SSO sign in for SCIM users.** Users created through SCIM can sign in with SSO again, where they got "401 Invalid authentication request" since 0.12.0 because no sign-in record was created for them; a database migration adds the missing record for existing accounts without giving them a usable password, SCIM email changes now also update the sign-in email and deleting a user through SCIM removes the sign-in record as well. [Commit](https://github.com/open-webui/open-webui/commit/00f12c0e47fb47b1318a20e97bacc753e769612b), [#32347](https://github.com/open-webui/open-webui/issues/32347)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-14-rich-ui-embed-console-errors-rich-ui-tool-embeds-no-longer-log-a-security-error|🧩 Rich UI embed console errors. Rich UI tool embeds no longer log a security…]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-14-6-developer-workflow-changes-in-v0-12-1|6 Developer Workflow changes in v0.12.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-14-translated-model-prompt-suggestions-editing-the-prompt-suggestions-of-a-model-th|💬 Translated model prompt suggestions. Editing the prompt suggestions of a model…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-14-tools-picked-in-new-chats-tools-picked-from-the-integrations-menu-the-web-search|🧰 Tools picked in new chats. Tools picked from the Integrations menu, the Web…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-14-2-context-window-changes-in-v0-12-1|2 Context Window changes in v0.12.1]] · Context Window
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
## Nearby in Account and Access

- Earlier: 2026-10-14 · Ollama · [[Changes/Ollama/2026-10-14-clearer-error-messages-when-cloud-access-fails-sign-in-problems-payment-issues-i|Clearer error messages when cloud access fails]]
- Later: 2026-10-15 · Codex CLI · [[Changes/Codex CLI/2026-10-15-53389-use-cached-login-credentials-for-guardian-decisions-swastik-oai|♯53389 Use cached login credentials for Guardian decisions @swastik-oai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-14-796135&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-14-3-account-and-access-changes-in-v0-12-1.md%0ACard%20ID%3A%20open-webui-2026-10-14-796135%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->