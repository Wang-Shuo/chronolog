---
card_id: open-webui-2026-08-31-08e8d0
date: '2026-08-31'
description: "Open WebUI · 2026-08-31 · Reliability and Performance: \U0001F9E0 **Large
  tool calls stream faster through Anthropic-compatible clients.** When a streamed
  tool call…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1355
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: e0fa210734b0de5f14653ee1fc39cc7da4e0c060973c94dcfb56d3f110cb52c4
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-31-08e8d0
  comparison: ''
  date: '2026-08-31'
  description: "Open WebUI — v0.11.2: \U0001F9E0 **Large tool calls stream faster
    through Anthropic-compatible clients.** When a streamed tool call sends a large
    block of arguments, Open WebUI now waits until that block can actually be complete
    before checking it, instead of doing the same expensive check again on every tiny
    piece. [#28858](https://github.com/open-webui/open-webui/pull/28858)"
  evidence:
  - quote: "\U0001F9E0 **Large tool calls stream faster through Anthropic-compatible
      clients.** When a streamed tool call sends a large block of arguments, Open
      WebUI now waits until that block can actually be complete before checking it,
      instead of doing the same expensive check again on every tiny piece. [#28858](https://github.com/open-webui/open-webui/pull/28858)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: large-tool-calls-stream-faster-through-anthropic-compatible-clients-when-a-strea
  source_release: open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b
  source_type: github_releases
  theme: reliability-performance
  title: "\U0001F9E0 **Large tool calls stream faster through Anthropic-compatible…"
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-08-25-10-reliability-and-performance-changes-in-v0-11-1|10
  Reliability and Performance changes in v0.11.1]]'
- '[[Changes/GitHub Copilot CLI/2026-08-27-resume-large-sessions-faster-by-showing-recent-history-first-while-older-message|Resume
  large sessions faster by showing recent history first while older messages load]]'
- '[[Changes/Lovable/2026-08-27-faster-command-palette|Faster command palette]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b|open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b]]'
source_type: github_releases
theme: reliability-performance
title: "\U0001F9E0 Large tool calls stream faster through Anthropic-compatible…"
type: change
---

<!-- chronolog:begin region="header" -->
# 🧠 **Large tool calls stream faster through Anthropic-compatible…

**Open WebUI** · 2026-08-31 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.2) · from [[Releases/Open WebUI/open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b|v0.11.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> 🧠 **Large tool calls stream faster through Anthropic-compatible clients.** When a streamed tool call sends a large block of arguments, Open WebUI now waits until that block can actually be complete before checking it, instead of doing the same expensive check again on every tiny piece. [#28858](https://github.com/open-webui/open-webui/pull/28858)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-31-3-automation-and-scheduling-changes-in-v0-11-2|3 Automation and Scheduling changes in v0.11.2]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-08-31-3-interface-experience-changes-in-v0-11-2|3 Interface Experience changes in v0.11.2]] · Interface Experience
- [[Changes/Open WebUI/2026-08-31-code-interpreter-starts-on-windows-the-built-in-code-interpreter-now-serves-its|🐍 Code interpreter starts on Windows. The built-in code interpreter now serves…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-08-31-security-advisory-this-release-includes-security-and-access-control-fixes-we-rec|🛡️ Security Advisory: This release includes security and access-control fixes]] · Safety and Privacy
- [[Changes/Open WebUI/2026-08-31-high-contrast-mode-is-now-accessibility-mode-the-interface-setting-previously-ca|🏷️ High Contrast Mode is now Accessibility Mode. The interface setting…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-08-31-9-developer-workflow-changes-in-v0-11-2|9 Developer Workflow changes in v0.11.2]] · Developer Workflow
- [[Changes/Open WebUI/2026-08-31-2-files-and-data-changes-in-v0-11-2|2 Files and Data changes in v0.11.2]] · Files and Data
- [[Changes/Open WebUI/2026-08-31-10-model-support-changes-in-v0-11-2|10 Model Support changes in v0.11.2]] · Model Support
- [[Changes/Open WebUI/2026-08-31-2-collaboration-changes-in-v0-11-2|2 Collaboration changes in v0.11.2]] · Collaboration
- [[Changes/Open WebUI/2026-08-31-12-other-changes-in-v0-11-2|12 other changes in v0.11.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-08-27 · Lovable · [[Changes/Lovable/2026-08-27-faster-command-palette|Faster command palette]]
- Later: 2026-08-31 · Open WebUI · [[Changes/Open WebUI/2026-08-31-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-31-08e8d0&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-31-large-tool-calls-stream-faster-through-anthropic-compatible-clients-when-a-strea.md%0ACard%20ID%3A%20open-webui-2026-08-31-08e8d0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->