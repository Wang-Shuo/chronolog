---
card_id: open-webui-2026-05-10-c40288
date: '2026-05-10'
description: "Open WebUI · 2026-05-10 · Other changes: 6 changes in v0.9.5 — \U0001F510
  **Feedback user attribution spoofing.** Submitting evaluation feedback can no longer
  forge the…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 22e2e4d868063b849e24812e9755890e2e344ad0838d5357a1e06379c9e4360b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-10-c40288
  comparison: ''
  date: '2026-05-10'
  description: 'Open WebUI — v0.9.5: 6 other changes'
  evidence:
  - quote: "\U0001F510 **Feedback user attribution spoofing.** Submitting evaluation
      feedback can no longer forge the `user_id` field through mass-assignment, preventing
      authenticated users from attributing ratings to other users and corrupting Elo
      leaderboard rankings and admin feedback exports. [#24508](https://github.com/open-webui/open-webui/pull/24508)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  - quote: "\U0001F6E1️ **Image URL redirect-based SSRF.** Chat messages containing
      image URLs no longer follow 3xx redirects to internal addresses during base64
      conversion, closing the most reachable redirect-based SSRF variant that required
      no special permissions or feature flags. [#24524](https://github.com/open-webui/open-webui/pull/24524)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  - quote: "\U0001F6E1️ **Collection write access on file processing.** The `process_file`
      and `process_files_batch` retrieval endpoints now enforce collection write-access
      checks before embedding content, preventing authenticated users from injecting
      file content into another user's knowledge-base collection. [#24524](https://github.com/open-webui/open-webui/pull/24524)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  - quote: "\U0001F510 **Channel message ownership enforcement.** Updating or deleting
      messages in group and DM channels now requires message ownership, preventing
      channel members from tampering with or silently removing other members' messages.
      [#24506](https://github.com/open-webui/open-webui/pull/24506)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  - quote: "\U0001F310 **Portuguese (Brazil) translation updates.** Translations for
      newly added UI items were added along with a consistency pass across existing
      entries. [#24503](https://github.com/open-webui/open-webui/pull/24503)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  - quote: "\U0001F9F9 **Removed unauthenticated retrieval status endpoint.** The
      unauthenticated `GET /api/v1/retrieval/` status endpoint has been removed as
      dead code — retrieval configuration is already available through authenticated
      admin endpoints. [#24497](https://github.com/open-webui/open-webui/pull/24497)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-other-changes-in-v0-9-5
  source_release: open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2
  source_type: github_releases
  theme: uncategorized
  title: 6 other changes in v0.9.5
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2]]'
source_type: github_releases
theme: uncategorized
title: 6 other changes in v0.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 6 other changes in v0.9.5

**Open WebUI** · 2026-05-10 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.5) · from [[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|v0.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 **Feedback user attribution spoofing.** Submitting evaluation feedback can no longer forge the `user_id` field through mass-assignment, preventing authenticated users from attributing ratings to other users and corrupting Elo leaderboard rankings and admin feedback exports. [#24508](https://github.com/open-webui/open-webui/pull/24508)

> 🛡️ **Image URL redirect-based SSRF.** Chat messages containing image URLs no longer follow 3xx redirects to internal addresses during base64 conversion, closing the most reachable redirect-based SSRF variant that required no special permissions or feature flags. [#24524](https://github.com/open-webui/open-webui/pull/24524)

> 🛡️ **Collection write access on file processing.** The `process_file` and `process_files_batch` retrieval endpoints now enforce collection write-access checks before embedding content, preventing authenticated users from injecting file content into another user's knowledge-base collection. [#24524](https://github.com/open-webui/open-webui/pull/24524)

> 🔐 **Channel message ownership enforcement.** Updating or deleting messages in group and DM channels now requires message ownership, preventing channel members from tampering with or silently removing other members' messages. [#24506](https://github.com/open-webui/open-webui/pull/24506)

> 🌐 **Portuguese (Brazil) translation updates.** Translations for newly added UI items were added along with a consistency pass across existing entries. [#24503](https://github.com/open-webui/open-webui/pull/24503)

> 🧹 **Removed unauthenticated retrieval status endpoint.** The unauthenticated `GET /api/v1/retrieval/` status endpoint has been removed as dead code — retrieval configuration is already available through authenticated admin endpoints. [#24497](https://github.com/open-webui/open-webui/pull/24497)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
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
- [[Changes/Open WebUI/2026-05-10-redirect-based-ssrf-protection-all-outbound-http-requests-now-block-3xx-redirect|🛡️ Redirect-based SSRF protection. All outbound HTTP requests now block 3xx…]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-10-c40288&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-10-6-other-changes-in-v0-9-5.md%0ACard%20ID%3A%20open-webui-2026-05-10-c40288%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->