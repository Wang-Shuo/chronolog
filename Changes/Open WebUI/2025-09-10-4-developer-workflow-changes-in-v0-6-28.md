---
card_id: open-webui-2025-09-10-b46484
date: '2025-09-10'
description: "Open WebUI · 2025-09-10 · Developer Workflow: 4 changes in v0.6.28 —
  \U0001F6E0️ External tool server data handling is now more robust, automatically
  attempting to…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2556
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 17676af829717fb612f0c10813ac60763996fd4946c6f8d9a31c4e6eb746989d
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-09-10-b46484
  comparison: ''
  date: '2025-09-10'
  description: 'Open WebUI — v0.6.28: 4 Developer Workflow changes'
  evidence:
  - quote: "\U0001F6E0️ External tool server data handling is now more robust, automatically
      attempting to parse specifications as JSON before falling back to YAML, regardless
      of the URL extension. [Commit](https://github.com/open-webui/open-webui/commit/774c0056bde88ed4831422efa81506488e3d6641)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.28
  - quote: "\U0001F3AF The \"Title\" field is now automatically focused when creating
      a new chat folder, streamlining the folder creation process. [#17315](https://github.com/open-webui/open-webui/issues/17315),
      [Commit](https://github.com/open-webui/open-webui/commit/c51a651a2d5e2a27546416666812e9b92205562d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.28
  - quote: "\U0001F50A A regression affecting Text-to-Speech for local providers using
      the OpenAI engine was fixed by reverting a URL joining change. [#17316](https://github.com/open-webui/open-webui/issues/17316),
      [Commit](https://github.com/open-webui/open-webui/commit/8339f59cdfc63f2d58c8e26933d1bf1438479d75)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.28
  - quote: "\U0001FAA7 A regression was fixed where the input modal for prompts with
      placeholders would not open, causing the raw prompt text to be pasted into the
      chat input field instead. [#17325](https://github.com/open-webui/open-webui/issues/17325),
      [Commit](https://github.com/open-webui/open-webui/commit/d5cb65527eaa4831459a4c7dbf187daa9c0525ae)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.28
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-developer-workflow-changes-in-v0-6-28
  source_release: open-webui-2025-09-10-v0-6-28-github-246132581-01492711
  source_type: github_releases
  theme: developer-workflow
  title: 4 Developer Workflow changes in v0.6.28
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-09-09-3-developer-workflow-changes-in-v0-4-0|3 Developer
  Workflow changes in v0.4.0]]'
- '[[Changes/Open WebUI/2025-09-09-14-developer-workflow-changes-in-v0-6-27|14 Developer
  Workflow changes in v0.6.27]]'
- '[[Changes/Codex CLI/2025-09-10-2-developer-workflow-changes-in-rust-v0-32-0|2 Developer
  Workflow changes in rust-v0.32.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-09-10-v0-6-28-github-246132581-01492711|open-webui-2025-09-10-v0-6-28-github-246132581-01492711]]'
source_type: github_releases
theme: developer-workflow
title: 4 Developer Workflow changes in v0.6.28
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Developer Workflow changes in v0.6.28

**Open WebUI** · 2025-09-10 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.28) · from [[Releases/Open WebUI/open-webui-2025-09-10-v0-6-28-github-246132581-01492711|v0.6.28]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🛠️ External tool server data handling is now more robust, automatically attempting to parse specifications as JSON before falling back to YAML, regardless of the URL extension. [Commit](https://github.com/open-webui/open-webui/commit/774c0056bde88ed4831422efa81506488e3d6641)

> 🎯 The "Title" field is now automatically focused when creating a new chat folder, streamlining the folder creation process. [#17315](https://github.com/open-webui/open-webui/issues/17315), [Commit](https://github.com/open-webui/open-webui/commit/c51a651a2d5e2a27546416666812e9b92205562d)

> 🔊 A regression affecting Text-to-Speech for local providers using the OpenAI engine was fixed by reverting a URL joining change. [#17316](https://github.com/open-webui/open-webui/issues/17316), [Commit](https://github.com/open-webui/open-webui/commit/8339f59cdfc63f2d58c8e26933d1bf1438479d75)

> 🪧 A regression was fixed where the input modal for prompts with placeholders would not open, causing the raw prompt text to be pasted into the chat input field instead. [#17325](https://github.com/open-webui/open-webui/issues/17325), [Commit](https://github.com/open-webui/open-webui/commit/d5cb65527eaa4831459a4c7dbf187daa9c0525ae)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.28
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-09-10-various-improvements-were-implemented-across-the-frontend-and-backend-to-enhance|🔄 Various improvements were implemented across the frontend and backend to enhance…]] · Reliability and Performance
- [[Changes/Open WebUI/2025-09-10-the-command-for-model-selection-now-supports-real-time-search-and-filtering-impr|🔍 The "@" command for model selection now supports real-time search and filtering…]] · Model Support
- [[Changes/Open WebUI/2025-09-10-2-other-changes-in-v0-6-28|2 other changes in v0.6.28]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2025-09-10 · Codex CLI · [[Changes/Codex CLI/2025-09-10-2-developer-workflow-changes-in-rust-v0-32-0|2 Developer Workflow changes in rust-v0.32.0]]
- Later: 2025-09-12 · Cursor · [[Changes/Cursor/2025-09-12-improved-terminal-for-agent|Improved terminal for Agent]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-09-10-b46484&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-09-10-4-developer-workflow-changes-in-v0-6-28.md%0ACard%20ID%3A%20open-webui-2025-09-10-b46484%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.28%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->