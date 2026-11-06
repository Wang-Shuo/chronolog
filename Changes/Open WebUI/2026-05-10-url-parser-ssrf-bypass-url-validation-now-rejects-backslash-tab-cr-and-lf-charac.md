---
card_id: open-webui-2026-05-10-1009f2
date: '2026-05-10'
description: "Open WebUI · 2026-05-10 · Editor Experience: \U0001F6E1️ **URL parser
  SSRF bypass.** URL validation now rejects backslash, tab, CR, and LF characters
  that cause urllib…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1153
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 81f54e92ca751f1113bb3d471da08951f051f2b5713facfbd2a4c63012964f60
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-10-1009f2
  comparison: ''
  date: '2026-05-10'
  description: "Open WebUI — v0.9.5: \U0001F6E1️ **URL parser SSRF bypass.** URL validation
    now rejects backslash, tab, CR, and LF characters that cause urllib and requests/aiohttp
    to disagree on the target host, closing a parser-confusion SSRF bypass. [#24534](https://github.com/open-webui/open-webui/pull/24534)"
  evidence:
  - quote: "\U0001F6E1️ **URL parser SSRF bypass.** URL validation now rejects backslash,
      tab, CR, and LF characters that cause urllib and requests/aiohttp to disagree
      on the target host, closing a parser-confusion SSRF bypass. [#24534](https://github.com/open-webui/open-webui/pull/24534)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: url-parser-ssrf-bypass-url-validation-now-rejects-backslash-tab-cr-and-lf-charac
  source_release: open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2
  source_type: github_releases
  theme: editor-experience
  title: "\U0001F6E1️ **URL parser SSRF bypass.** URL validation now rejects backslash,
    tab, CR, and LF…"
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-08-2-editor-experience-changes-in-rust-v0-130-0|2 Editor
  Experience changes in rust-v0.130.0]]'
- '[[Changes/GitHub Copilot CLI/2026-05-08-2-editor-experience-changes-in-v1-0-44|2
  Editor Experience changes in v1.0.44]]'
- '[[Changes/Open WebUI/2026-05-09-5-editor-experience-changes-in-v0-9-3|5 Editor
  Experience changes in v0.9.3]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2]]'
source_type: github_releases
theme: editor-experience
title: "\U0001F6E1️ URL parser SSRF bypass. URL validation now rejects backslash,
  tab, CR, and LF…"
type: change
---

<!-- chronolog:begin region="header" -->
# 🛡️ **URL parser SSRF bypass.** URL validation now rejects backslash, tab, CR, and LF…

**Open WebUI** · 2026-05-10 · [[Themes/editor-experience|Editor Experience]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.5) · from [[Releases/Open WebUI/open-webui-2026-05-10-v0-9-5-github-320167431-c515d0a2|v0.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> 🛡️ **URL parser SSRF bypass.** URL validation now rejects backslash, tab, CR, and LF characters that cause urllib and requests/aiohttp to disagree on the target host, closing a parser-confusion SSRF bypass. [#24534](https://github.com/open-webui/open-webui/pull/24534)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-10-shared-chat-access-for-owners-and-admins-chat-owners-can-now-view-and-clone-thei|🔐 Shared chat access for owners and admins. Chat owners can now view and clone…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-05-10-2-image-generation-changes-in-v0-9-5|2 Image Generation changes in v0.9.5]] · Image Generation
- [[Changes/Open WebUI/2026-05-10-2-developer-workflow-changes-in-v0-9-5|2 Developer Workflow changes in v0.9.5]] · Developer Workflow
- [[Changes/Open WebUI/2026-05-10-6-safety-and-privacy-changes-in-v0-9-5|6 Safety and Privacy changes in v0.9.5]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-10-2-interface-experience-changes-in-v0-9-5|2 Interface Experience changes in v0.9.5]] · Interface Experience
- [[Changes/Open WebUI/2026-05-10-file-ownership-in-folder-and-knowledge-attachments-attaching-files-to-folders-or|🔐 File ownership in folder and knowledge attachments. Attaching files to folders…]] · Context Window
- [[Changes/Open WebUI/2026-05-10-3-model-support-changes-in-v0-9-5|3 Model Support changes in v0.9.5]] · Model Support
- [[Changes/Open WebUI/2026-05-10-redirect-based-ssrf-protection-all-outbound-http-requests-now-block-3xx-redirect|🛡️ Redirect-based SSRF protection. All outbound HTTP requests now block 3xx…]] · Account and Access
- [[Changes/Open WebUI/2026-05-10-6-other-changes-in-v0-9-5|6 other changes in v0.9.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-05-09 · Open WebUI · [[Changes/Open WebUI/2026-05-09-5-editor-experience-changes-in-v0-9-3|5 Editor Experience changes in v0.9.3]]
- Later: 2026-05-11 · Claude Code · [[Changes/Claude Code/2026-05-11-vscode-press-cmd-ctrl-shift-t-to-reopen-the-most-recently-closed-session-tab-con|VSCode Press Cmd/Ctrl+Shift+T to reopen the most recently closed session tab…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-10-1009f2&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-10-url-parser-ssrf-bypass-url-validation-now-rejects-backslash-tab-cr-and-lf-charac.md%0ACard%20ID%3A%20open-webui-2026-05-10-1009f2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->