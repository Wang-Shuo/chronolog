---
card_id: open-webui-2026-05-10-f71b19
date: '2026-05-10'
description: "Open WebUI · 2026-05-10 · Account and Access: \U0001F6E1️ **Redirect-based
  SSRF protection.** All outbound HTTP requests now block 3xx redirects by default
  via a new…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2112
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 46678c257c8a040b696f2c9f3bd29b55649b58fe9639d083d1ec0f2372a0f5bf
product: open-webui
product_name: Open WebUI
record:
  ai_generated: true
  card_id: open-webui-2026-05-10-f71b19
  comparison: ''
  confidence: low
  date: '2026-05-10'
  description: "Open WebUI — v0.9.5: \U0001F6E1️ **Redirect-based SSRF protection.**
    All outbound HTTP requests now block 3xx redirects by default via a new `AIOHTTP_CLIENT_ALLOW_REDIRECTS`
    environment variable, preventing redirect-based SSRF where a public URL silently
    redirects to internal addresses (RFC 1918, loopback, cloud-metadata endpoints).
    Affected call sites include web fetch, image loading, OAuth discovery, tool server
    execution, and code interpreter login. [#24491](https://github.com/open-webui/open-webui/pull/24491)"
  evidence:
  - quote: "\U0001F6E1️ **Redirect-based SSRF protection.** All outbound HTTP requests
      now block 3xx redirects by default via a new `AIOHTTP_CLIENT_ALLOW_REDIRECTS`
      environment variable, preventing redirect-based SSRF where a public URL silently
      redirects to internal addresses (RFC 1918, loopback, cloud-metadata endpoints).
      Affected call sites include web fetch, image loading, OAuth discovery, tool
      server execution, and code interpreter login. [#24491](https://github.com/open-webui/open-webui/pull/24491)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: redirect-based-ssrf-protection-all-outbound-http-requests-now-block-3xx-redirect
  source_release: open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2
  source_type: github_releases
  theme: account-access
  title: "\U0001F6E1️ **Redirect-based SSRF protection.** All outbound HTTP requests
    now block 3xx…"
  type: change
related_changes:
- '[[Changes/Raycast/2026-05-08-general-faster-app-startup-and-a-more-reliable-launch-at-login-experience|General
  : Faster app startup and a more reliable launch-at-login experience]]'
- '[[Changes/Replit/2026-05-08-private-publishing-for-everyone|Private publishing
  for everyone]]'
- '[[Changes/Open WebUI/2026-05-09-4-account-and-access-changes-in-v0-9-3|4 Account
  and Access changes in v0.9.3]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2]]'
source_type: github_releases
theme: account-access
title: "\U0001F6E1️ Redirect-based SSRF protection. All outbound HTTP requests now
  block 3xx…"
type: change
---

<!-- chronolog:begin region="header" -->
# 🛡️ **Redirect-based SSRF protection.** All outbound HTTP requests now block 3xx…

**Open WebUI** · 2026-05-10 · [[Themes/account-access|Account and Access]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.5) · from [[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|v0.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> 🛡️ **Redirect-based SSRF protection.** All outbound HTTP requests now block 3xx redirects by default via a new `AIOHTTP_CLIENT_ALLOW_REDIRECTS` environment variable, preventing redirect-based SSRF where a public URL silently redirects to internal addresses (RFC 1918, loopback, cloud-metadata endpoints). Affected call sites include web fetch, image loading, OAuth discovery, tool server execution, and code interpreter login. [#24491](https://github.com/open-webui/open-webui/pull/24491)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-10-url-parser-ssrf-bypass-url-validation-now-rejects-backslash-tab-cr-and-lf-charac|🛡️ URL parser SSRF bypass. URL validation now rejects backslash, tab, CR, and LF…]] · Editor Experience
- [[Changes/Open WebUI/2026-05-10-shared-chat-access-for-owners-and-admins-chat-owners-can-now-view-and-clone-thei|🔐 Shared chat access for owners and admins. Chat owners can now view and clone…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-05-10-2-image-generation-changes-in-v0-9-5|2 Image Generation changes in v0.9.5]] · Image Generation
- [[Changes/Open WebUI/2026-05-10-2-developer-workflow-changes-in-v0-9-5|2 Developer Workflow changes in v0.9.5]] · Developer Workflow
- [[Changes/Open WebUI/2026-05-10-6-safety-and-privacy-changes-in-v0-9-5|6 Safety and Privacy changes in v0.9.5]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-10-2-interface-experience-changes-in-v0-9-5|2 Interface Experience changes in v0.9.5]] · Interface Experience
- [[Changes/Open WebUI/2026-05-10-file-ownership-in-folder-and-knowledge-attachments-attaching-files-to-folders-or|🔐 File ownership in folder and knowledge attachments. Attaching files to folders…]] · Context Window
- [[Changes/Open WebUI/2026-05-10-3-model-support-changes-in-v0-9-5|3 Model Support changes in v0.9.5]] · Model Support
- [[Changes/Open WebUI/2026-05-10-6-other-changes-in-v0-9-5|6 other changes in v0.9.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-05-09 · Open WebUI · [[Changes/Open WebUI/2026-05-09-4-account-and-access-changes-in-v0-9-3|4 Account and Access changes in v0.9.3]]
- Later: 2026-05-12 · Dify · [[Changes/Dify/2026-05-12-refactor-auth-update-oauth-button-and-settings-modal-for-improved-state-manageme|refactor(auth): update OAuth button and settings modal for improved state management…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-10-f71b19&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-10-redirect-based-ssrf-protection-all-outbound-http-requests-now-block-3xx-redirect.md%0ACard%20ID%3A%20open-webui-2026-05-10-f71b19%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->