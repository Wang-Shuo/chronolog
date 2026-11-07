---
card_id: open-webui-2026-05-10-80f226
date: '2026-05-10'
description: "Open WebUI · 2026-05-10 · Safety and Privacy: 6 changes in v0.9.5 —
  \U0001F6E1️ **Iframe content security policy.** Administrators can now configure
  a…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1120
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ee449481d439fce09addc7ce69aca0e9e821246d093d0e0bab89c614119bfafa
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-10-80f226
  comparison: ''
  date: '2026-05-10'
  description: 'Open WebUI — v0.9.5: 6 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F6E1️ **Iframe content security policy.** Administrators can now
      configure a Content-Security-Policy for all srcdoc iframes (Artifacts, tool
      embeds, file previews, citation modals) via the `IFRAME_CSP` environment variable,
      restricting what LLM-generated or user-uploaded HTML can load and execute inside
      previews. [Commit](https://github.com/open-webui/open-webui/commit/3bba1c227059a44c7eeefa97b8c69a63bf4f3454)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  - quote: "\U0001F527 **Terminal proxy response headers.** Administrators can now
      inject custom response headers into terminal proxy responses via the `TERMINAL_PROXY_HEADERS`
      environment variable (JSON object), enabling deployment-specific security headers
      like sandbox policies for proxied content. [Commit](https://github.com/open-webui/open-webui/commit/8d3133fe2835122bffaa4f2ce584730bc9c78981)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  - quote: "\U0001F510 **Skill public sharing permission enforcement.** Creating or
      updating skills now filters access grants through the `sharing.public_skills`
      permission, preventing non-admin users from making skills publicly accessible
      without the required permission. [#24494](https://github.com/open-webui/open-webui/pull/24494)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  - quote: "\U0001F510 **Calendar public sharing permission enforcement.** Creating
      or updating calendars now filters access grants through a new `sharing.public_calendars`
      permission, preventing users from making calendars publicly readable or writable
      without explicit admin-granted sharing permission. [#24493](https://github.com/open-webui/open-webui/pull/24493)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  - quote: "\U0001F510 **Tool source code update authorization.** Updating a tool's
      Python source code now requires `workspace.tools` or `workspace.tools_import`
      permission, preventing users with only a write-access grant from overwriting
      executable tool code while still allowing metadata edits. [#24513](https://github.com/open-webui/open-webui/pull/24513)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  - quote: "\U0001F510 **Channel pin write permission.** Pinning and unpinning messages
      on standard channels now requires write permission instead of read permission,
      preventing read-only users from modifying pinned content. [#24521](https://github.com/open-webui/open-webui/pull/24521)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-safety-and-privacy-changes-in-v0-9-5
  source_release: open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v0.9.5
  type: change
related_changes:
- '[[Changes/Replit/2026-05-08-workspace-security-center-2-0|Workspace Security Center
  2.0]]'
- '[[Changes/Open WebUI/2026-05-09-3-safety-and-privacy-changes-in-v0-9-3|3 Safety
  and Privacy changes in v0.9.3]]'
- '[[Changes/OpenCode/2026-05-09-core-rejected-invalid-permission-and-question-ids-in-the-http-api|Core
  Rejected invalid permission and question IDs in the HTTP API]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v0.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v0.9.5

**Open WebUI** · 2026-05-10 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.5) · from [[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|v0.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🛡️ **Iframe content security policy.** Administrators can now configure a Content-Security-Policy for all srcdoc iframes (Artifacts, tool embeds, file previews, citation modals) via the `IFRAME_CSP` environment variable, restricting what LLM-generated or user-uploaded HTML can load and execute inside previews. [Commit](https://github.com/open-webui/open-webui/commit/3bba1c227059a44c7eeefa97b8c69a63bf4f3454)

> 🔧 **Terminal proxy response headers.** Administrators can now inject custom response headers into terminal proxy responses via the `TERMINAL_PROXY_HEADERS` environment variable (JSON object), enabling deployment-specific security headers like sandbox policies for proxied content. [Commit](https://github.com/open-webui/open-webui/commit/8d3133fe2835122bffaa4f2ce584730bc9c78981)

> 🔐 **Skill public sharing permission enforcement.** Creating or updating skills now filters access grants through the `sharing.public_skills` permission, preventing non-admin users from making skills publicly accessible without the required permission. [#24494](https://github.com/open-webui/open-webui/pull/24494)

> 🔐 **Calendar public sharing permission enforcement.** Creating or updating calendars now filters access grants through a new `sharing.public_calendars` permission, preventing users from making calendars publicly readable or writable without explicit admin-granted sharing permission. [#24493](https://github.com/open-webui/open-webui/pull/24493)

> 🔐 **Tool source code update authorization.** Updating a tool's Python source code now requires `workspace.tools` or `workspace.tools_import` permission, preventing users with only a write-access grant from overwriting executable tool code while still allowing metadata edits. [#24513](https://github.com/open-webui/open-webui/pull/24513)

> 🔐 **Channel pin write permission.** Pinning and unpinning messages on standard channels now requires write permission instead of read permission, preventing read-only users from modifying pinned content. [#24521](https://github.com/open-webui/open-webui/pull/24521)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-10-url-parser-ssrf-bypass-url-validation-now-rejects-backslash-tab-cr-and-lf-charac|🛡️ URL parser SSRF bypass. URL validation now rejects backslash, tab, CR, and LF…]] · Editor Experience
- [[Changes/Open WebUI/2026-05-10-shared-chat-access-for-owners-and-admins-chat-owners-can-now-view-and-clone-thei|🔐 Shared chat access for owners and admins. Chat owners can now view and clone…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-05-10-2-image-generation-changes-in-v0-9-5|2 Image Generation changes in v0.9.5]] · Image Generation
- [[Changes/Open WebUI/2026-05-10-2-developer-workflow-changes-in-v0-9-5|2 Developer Workflow changes in v0.9.5]] · Developer Workflow
- [[Changes/Open WebUI/2026-05-10-2-interface-experience-changes-in-v0-9-5|2 Interface Experience changes in v0.9.5]] · Interface Experience
- [[Changes/Open WebUI/2026-05-10-file-ownership-in-folder-and-knowledge-attachments-attaching-files-to-folders-or|🔐 File ownership in folder and knowledge attachments. Attaching files to folders…]] · Context Window
- [[Changes/Open WebUI/2026-05-10-3-model-support-changes-in-v0-9-5|3 Model Support changes in v0.9.5]] · Model Support
- [[Changes/Open WebUI/2026-05-10-redirect-based-ssrf-protection-all-outbound-http-requests-now-block-3xx-redirect|🛡️ Redirect-based SSRF protection. All outbound HTTP requests now block 3xx…]] · Account and Access
- [[Changes/Open WebUI/2026-05-10-6-other-changes-in-v0-9-5|6 other changes in v0.9.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-09 · OpenCode · [[Changes/OpenCode/2026-05-09-core-rejected-invalid-permission-and-question-ids-in-the-http-api|Core Rejected invalid permission and question IDs in the HTTP API]]
- Later: 2026-05-10 · OpenCode · [[Changes/OpenCode/2026-05-10-core-read-tool-permission-rules-now-match-worktree-relative-paths-so-read-allowl|Core Read tool permission rules now match worktree-relative paths, so read…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-10-80f226&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-10-6-safety-and-privacy-changes-in-v0-9-5.md%0ACard%20ID%3A%20open-webui-2026-05-10-80f226%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->