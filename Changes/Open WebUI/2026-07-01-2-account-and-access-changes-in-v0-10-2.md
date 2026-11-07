---
card_id: open-webui-2026-07-01-cc7d80
date: '2026-07-01'
description: "Open WebUI · 2026-07-01 · Account and Access: 2 changes in v0.10.2 —
  \U0001F510 **Fewer unexpected logouts.** A single request returning an authorization
  error no…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2164
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 79f1185dd3c2da681c1f09486d80a95ce60df5c6a3d5e6da4f00cfa52aed4432
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-01-cc7d80
  comparison: ''
  date: '2026-07-01'
  description: 'Open WebUI — v0.10.2: 2 Account and Access changes'
  evidence:
  - quote: "\U0001F510 **Fewer unexpected logouts.** A single request returning an
      authorization error no longer signs you out while your session is still valid,
      since the app now confirms the session status before redirecting to login. [Commit](https://github.com/open-webui/open-webui/commit/56ee875e21cb3b137a5aa1eca6eb3c0731b14045)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
  - quote: "\U0001F5C4️ **Safer database upgrades.** Upgrading an existing SQLite
      database no longer crashes during the user-table migration or corrupts saved
      user settings, resolving failures that could block startup or break login after
      an upgrade. [#26403](https://github.com/open-webui/open-webui/issues/26403),
      [Commit](https://github.com/open-webui/open-webui/commit/c416c6cad69cc4ce44faacdad87cc65862625fb4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-account-and-access-changes-in-v0-10-2
  source_release: open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f
  source_type: github_releases
  theme: account-access
  title: 2 Account and Access changes in v0.10.2
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-06-30-2-account-and-access-changes-in-v2026-6-11|2 Account
  and Access changes in v2026.6.11]]'
- '[[Changes/OpenCode/2026-06-30-3-account-and-access-changes-in-v1-17-12|3 Account
  and Access changes in v1.17.12]]'
- '[[Changes/Claude Code/2026-07-01-login-now-opens-the-sign-in-dialog-from-the-claude-agents-view-instead-of-saying|/login
  now opens the sign-in dialog from the claude agents view instead…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f|open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f]]'
source_type: github_releases
theme: account-access
title: 2 Account and Access changes in v0.10.2
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Account and Access changes in v0.10.2

**Open WebUI** · 2026-07-01 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.2) · from [[Releases/Open WebUI/open-webui-2026-07-01-v0-10-2-github-347327188-9065e44f|v0.10.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 **Fewer unexpected logouts.** A single request returning an authorization error no longer signs you out while your session is still valid, since the app now confirms the session status before redirecting to login. [Commit](https://github.com/open-webui/open-webui/commit/56ee875e21cb3b137a5aa1eca6eb3c0731b14045)

> 🗄️ **Safer database upgrades.** Upgrading an existing SQLite database no longer crashes during the user-table migration or corrupts saved user settings, resolving failures that could block startup or break login after an upgrade. [#26403](https://github.com/open-webui/open-webui/issues/26403), [Commit](https://github.com/open-webui/open-webui/commit/c416c6cad69cc4ce44faacdad87cc65862625fb4)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.10.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-01-speech-to-text-request-format-openai-compatible-speech-to-text-can-now-send-audi|🎙️ Speech-to-text request format. OpenAI-compatible speech-to-text can now send…]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-01-web-search-domain-filtering-domain-allow-and-block-rules-for-web-search-results|🔒 Web search domain filtering. Domain allow and block rules for web search…]] · Search and Browsing
- [[Changes/Open WebUI/2026-07-01-2-interface-experience-changes-in-v0-10-2|2 Interface Experience changes in v0.10.2]] · Interface Experience
- [[Changes/Open WebUI/2026-07-01-5-model-support-changes-in-v0-10-2|5 Model Support changes in v0.10.2]] · Model Support
- [[Changes/Open WebUI/2026-07-01-2-memory-and-personalization-changes-in-v0-10-2|2 Memory and Personalization changes in v0.10.2]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-01-models-with-null-capabilities-chatting-with-a-model-whose-capabilities-are-unset|🤖 Models with null capabilities. Chatting with a model whose capabilities…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-01-5-developer-workflow-changes-in-v0-10-2|5 Developer Workflow changes in v0.10.2]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-01-2-editor-experience-changes-in-v0-10-2|2 Editor Experience changes in v0.10.2]] · Editor Experience
- [[Changes/Open WebUI/2026-07-01-3-safety-and-privacy-changes-in-v0-10-2|3 Safety and Privacy changes in v0.10.2]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-01-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-07-01-2-other-changes-in-v0-10-2|2 other changes in v0.10.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-07-01 · Claude Code · [[Changes/Claude Code/2026-07-01-login-now-opens-the-sign-in-dialog-from-the-claude-agents-view-instead-of-saying|/login now opens the sign-in dialog from the claude agents view instead…]]
- Later: 2026-07-06 · ChatGPT · [[Changes/ChatGPT/2026-07-06-chatgpt-for-powerpoint-is-now-generally-available-globally-from-a-sidebar-in-mic|ChatGPT for PowerPoint is now generally available]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-01-cc7d80&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-01-2-account-and-access-changes-in-v0-10-2.md%0ACard%20ID%3A%20open-webui-2026-07-01-cc7d80%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->