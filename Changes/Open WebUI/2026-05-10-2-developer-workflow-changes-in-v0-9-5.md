---
card_id: open-webui-2026-05-10-6fcac8
date: '2026-05-10'
description: "Open WebUI · 2026-05-10 · Developer Workflow: 2 changes in v0.9.5 —
  \U0001F6E1️ **Profile image MIME-type allowlist.** Serving profile images from data
  URIs now…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1149
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f51c91b8587d929a18fe051fbfbd58c0560731a52e326ca1e96e95c7e23ce529
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-10-6fcac8
  comparison: ''
  date: '2026-05-10'
  description: 'Open WebUI — v0.9.5: 2 Developer Workflow changes'
  evidence:
  - quote: "\U0001F6E1️ **Profile image MIME-type allowlist.** Serving profile images
      from data URIs now enforces a strict MIME-type allowlist (PNG, JPEG, GIF, WEBP
      by default, configurable via `PROFILE_IMAGE_ALLOWED_MIME_TYPES`) and sets `X-Content-Type-Options:
      nosniff`, preventing stored-XSS through SVG or other executable content types.
      [Commit](https://github.com/open-webui/open-webui/commit/15e696691cad98692c329de62ed8a5bdb3a26d4e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  - quote: "\U0001F4CB **PR template issue requirement.** Pull requests now require
      a linked Issue or Discussion reference, ensuring better traceability for all
      contributions. PRs without a linked issue or discussion may be closed without
      review."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-developer-workflow-changes-in-v0-9-5
  source_release: open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2
  source_type: github_releases
  theme: developer-workflow
  title: 2 Developer Workflow changes in v0.9.5
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-08-2-developer-workflow-changes-in-v1-0-44|2
  Developer Workflow changes in v1.0.44]]'
- '[[Changes/Open WebUI/2026-05-09-22-developer-workflow-changes-in-v0-9-3|22 Developer
  Workflow changes in v0.9.3]]'
- '[[Changes/OpenCode/2026-05-09-3-developer-workflow-changes-in-v1-14-44-2|3 Developer
  Workflow changes in v1.14.44 + 2]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2]]'
source_type: github_releases
theme: developer-workflow
title: 2 Developer Workflow changes in v0.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Developer Workflow changes in v0.9.5

**Open WebUI** · 2026-05-10 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.5) · from [[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|v0.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🛡️ **Profile image MIME-type allowlist.** Serving profile images from data URIs now enforces a strict MIME-type allowlist (PNG, JPEG, GIF, WEBP by default, configurable via `PROFILE_IMAGE_ALLOWED_MIME_TYPES`) and sets `X-Content-Type-Options: nosniff`, preventing stored-XSS through SVG or other executable content types. [Commit](https://github.com/open-webui/open-webui/commit/15e696691cad98692c329de62ed8a5bdb3a26d4e)

> 📋 **PR template issue requirement.** Pull requests now require a linked Issue or Discussion reference, ensuring better traceability for all contributions. PRs without a linked issue or discussion may be closed without review.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-10-url-parser-ssrf-bypass-url-validation-now-rejects-backslash-tab-cr-and-lf-charac|🛡️ URL parser SSRF bypass. URL validation now rejects backslash, tab, CR, and LF…]] · Editor Experience
- [[Changes/Open WebUI/2026-05-10-shared-chat-access-for-owners-and-admins-chat-owners-can-now-view-and-clone-thei|🔐 Shared chat access for owners and admins. Chat owners can now view and clone…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-05-10-2-image-generation-changes-in-v0-9-5|2 Image Generation changes in v0.9.5]] · Image Generation
- [[Changes/Open WebUI/2026-05-10-6-safety-and-privacy-changes-in-v0-9-5|6 Safety and Privacy changes in v0.9.5]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-10-2-interface-experience-changes-in-v0-9-5|2 Interface Experience changes in v0.9.5]] · Interface Experience
- [[Changes/Open WebUI/2026-05-10-file-ownership-in-folder-and-knowledge-attachments-attaching-files-to-folders-or|🔐 File ownership in folder and knowledge attachments. Attaching files to folders…]] · Context Window
- [[Changes/Open WebUI/2026-05-10-3-model-support-changes-in-v0-9-5|3 Model Support changes in v0.9.5]] · Model Support
- [[Changes/Open WebUI/2026-05-10-redirect-based-ssrf-protection-all-outbound-http-requests-now-block-3xx-redirect|🛡️ Redirect-based SSRF protection. All outbound HTTP requests now block 3xx…]] · Account and Access
- [[Changes/Open WebUI/2026-05-10-6-other-changes-in-v0-9-5|6 other changes in v0.9.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-05-09 · OpenCode · [[Changes/OpenCode/2026-05-09-3-developer-workflow-changes-in-v1-14-44-2|3 Developer Workflow changes in v1.14.44 + 2]]
- Later: 2026-05-10 · OpenCode · [[Changes/OpenCode/2026-05-10-2-developer-workflow-changes-in-v1-14-45|2 Developer Workflow changes in v1.14.45]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-10-6fcac8&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-10-2-developer-workflow-changes-in-v0-9-5.md%0ACard%20ID%3A%20open-webui-2026-05-10-6fcac8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->