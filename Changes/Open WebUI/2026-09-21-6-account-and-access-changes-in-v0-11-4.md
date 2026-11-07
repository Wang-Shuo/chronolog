---
card_id: open-webui-2026-09-21-254fc7
date: '2026-09-21'
description: "Open WebUI · 2026-09-21 · Account and Access: 6 changes in v0.11.4 —
  \U0001F513 **Turning off the sign-in form.** The box asking for an email address
  and a password can…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2246
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 77bd2835368e7ef2ae4b9f9a1bfbc48ee00623ad42fcc42b00f09c87e9d557e1
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-254fc7
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 6 Account and Access changes'
  evidence:
  - quote: "\U0001F513 **Turning off the sign-in form.** The box asking for an email
      address and a password can now be taken off the sign-in page from the authentication
      settings, where until now it could only be set before the server started, leaving
      single sign-on or a directory to sign people in. [Commit](https://github.com/open-webui/open-webui/commit/c4a349651e34bf5d0920bb5e26707ae9961ac39f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FAAA **Authentication type header.** A request to an OpenAI or Ollama
      connection now carries \"X-OpenWebUI-Auth-Type\", saying whether the person
      behind it signed in through the browser or called with an API key; its name
      is set with \"FORWARD_USER_INFO_HEADER_AUTH_TYPE\" and \"{{AUTH_TYPE}}\" works
      in custom headers. [Commit](https://github.com/open-webui/open-webui/commit/ee46e2664ab23bacc536fed21c06ab19067d695b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F510 **Sign-in role mapping.** Roles sent by an identity provider
      were in some setups not applied, leaving an account at the default role, and
      a sign-in whose roles cannot be read is now refused rather than let through.
      [Commit](https://github.com/open-webui/open-webui/commit/10d1cfe6375f207acaa531e857edb575ded2cfc3)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6AB **Blocked sign-in groups saved.** Comma-separated group names
      typed into the blocked groups field now take effect once saved, where the save
      stored the text as written and the sign-in check then read it as nothing; a
      group name carrying a comma of its own survives a save too. [Commit](https://github.com/open-webui/open-webui/commit/3fc1146c13d7b4b7a67c7fd058014436f80e0dfd)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F40C **Sign-in rate limiting.** Counting sign-in attempts through
      Redis no longer stops the whole worker until Redis answers, so a slow Redis
      stops freezing every other request with it. [#29977](https://github.com/open-webui/open-webui/pull/29977)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F58C️ **Editing an image you uploaded.** An image already held by
      Open WebUI can now be used with image editing, where fetching its own link back
      over the network could fail on a private network or without a sign-in. [Commit](https://github.com/open-webui/open-webui/commit/50413f34824ea49d5b94d3a97f3fe4bb2e881e38)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-account-and-access-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: account-access
  title: 6 Account and Access changes in v0.11.4
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-19-28-account-and-access-changes-in-v2026-9-5|28 Account
  and Access changes in v2026.9.5]]'
- '[[Changes/Devin/2026-09-21-link-your-bitbucket-data-center-account|Link Your Bitbucket
  Data Center Account]]'
- '[[Changes/GitHub Copilot CLI/2026-09-21-managed-plugin-commands-load-organization-marketplace-policy-with-environment-gi|Managed
  plugin commands load organization marketplace policy with environment…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: account-access
title: 6 Account and Access changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Account and Access changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔓 **Turning off the sign-in form.** The box asking for an email address and a password can now be taken off the sign-in page from the authentication settings, where until now it could only be set before the server started, leaving single sign-on or a directory to sign people in. [Commit](https://github.com/open-webui/open-webui/commit/c4a349651e34bf5d0920bb5e26707ae9961ac39f)

> 🪪 **Authentication type header.** A request to an OpenAI or Ollama connection now carries "X-OpenWebUI-Auth-Type", saying whether the person behind it signed in through the browser or called with an API key; its name is set with "FORWARD_USER_INFO_HEADER_AUTH_TYPE" and "{{AUTH_TYPE}}" works in custom headers. [Commit](https://github.com/open-webui/open-webui/commit/ee46e2664ab23bacc536fed21c06ab19067d695b)

> 🔐 **Sign-in role mapping.** Roles sent by an identity provider were in some setups not applied, leaving an account at the default role, and a sign-in whose roles cannot be read is now refused rather than let through. [Commit](https://github.com/open-webui/open-webui/commit/10d1cfe6375f207acaa531e857edb575ded2cfc3)

> 🚫 **Blocked sign-in groups saved.** Comma-separated group names typed into the blocked groups field now take effect once saved, where the save stored the text as written and the sign-in check then read it as nothing; a group name carrying a comma of its own survives a save too. [Commit](https://github.com/open-webui/open-webui/commit/3fc1146c13d7b4b7a67c7fd058014436f80e0dfd)

> 🐌 **Sign-in rate limiting.** Counting sign-in attempts through Redis no longer stops the whole worker until Redis answers, so a slow Redis stops freezing every other request with it. [#29977](https://github.com/open-webui/open-webui/pull/29977)

> 🖌️ **Editing an image you uploaded.** An image already held by Open WebUI can now be used with image editing, where fetching its own link back over the network could fail on a private network or without a sign-in. [Commit](https://github.com/open-webui/open-webui/commit/50413f34824ea49d5b94d3a97f3fe4bb2e881e38)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety and Privacy changes in v0.11.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-09-21-3-context-window-changes-in-v0-11-4|3 Context Window changes in v0.11.4]] · Context Window
- [[Changes/Open WebUI/2026-09-21-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-09-21-39-developer-workflow-changes-in-v0-11-4|39 Developer Workflow changes in v0.11.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-09-21-2-image-generation-changes-in-v0-11-4|2 Image Generation changes in v0.11.4]] · Image Generation
- [[Changes/Open WebUI/2026-09-21-4-collaboration-changes-in-v0-11-4|4 Collaboration changes in v0.11.4]] · Collaboration
- [[Changes/Open WebUI/2026-09-21-5-voice-and-audio-changes-in-v0-11-4|5 Voice and Audio changes in v0.11.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-09-21-10-files-and-data-changes-in-v0-11-4|10 Files and Data changes in v0.11.4]] · Files and Data
- [[Changes/Open WebUI/2026-09-21-21-editor-experience-changes-in-v0-11-4|21 Editor Experience changes in v0.11.4]] · Editor Experience
- [[Changes/Open WebUI/2026-09-21-6-memory-and-personalization-changes-in-v0-11-4|6 Memory and Personalization changes in v0.11.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-09-21-apple-device-replies-an-assistant-reply-no-longer-comes-up-blank-in-a-home-scree|📱 Apple device replies. An assistant reply no longer comes up blank in a home…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps and Integrations changes in v0.11.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-09-21-6-search-and-browsing-changes-in-v0-11-4|6 Search and Browsing changes in v0.11.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-09-21-13-interface-experience-changes-in-v0-11-4|13 Interface Experience changes in v0.11.4]] · Interface Experience
- [[Changes/Open WebUI/2026-09-21-4-automation-and-scheduling-changes-in-v0-11-4|4 Automation and Scheduling changes in v0.11.4]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-09-21-41-model-support-changes-in-v0-11-4|41 Model Support changes in v0.11.4]] · Model Support
- [[Changes/Open WebUI/2026-09-21-5-enterprise-and-administration-changes-in-v0-11-4|5 Enterprise and Administration changes in v0.11.4]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-09-21-61-other-changes-in-v0-11-4|61 other changes in v0.11.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-managed-plugin-commands-load-organization-marketplace-policy-with-environment-gi|Managed plugin commands load organization marketplace policy with environment…]]
- Later: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-claude-tag-improved-the-github-banner-in-claude-tag-admin-settings-to-say-why-gi|Claude Tag Improved the GitHub banner in Claude Tag admin settings to say why…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-254fc7&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-6-account-and-access-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-254fc7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->