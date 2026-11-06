---
card_id: open-webui-2026-08-31-1e320a
date: '2026-08-31'
description: "Open WebUI · 2026-08-31 · Automation and Scheduling: 3 changes in v0.11.2
  — \U0001F51F **Repeating automations keep their count.** An automation set to run
  a fixed…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add
    data clean schedule]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 972
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4c454a3e14638124658539026a25f1f039080fecdd8fafe423282aa17a50e0e2
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-31-1e320a
  comparison: ''
  date: '2026-08-31'
  description: 'Open WebUI — v0.11.2: 3 Automation and Scheduling changes'
  evidence:
  - quote: "\U0001F51F **Repeating automations keep their count.** An automation set
      to run a fixed number of times is no longer shown as running once and quietly
      rewritten to a single run the next time you open and save it. [#29261](https://github.com/open-webui/open-webui/pull/29261),
      [#29263](https://github.com/open-webui/open-webui/pull/29263)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F5D3️ **Schedules survive a save.** An automation carrying a start
      date now shows its real schedule in the list and keeps its weekly or monthly
      setting when saved, instead of showing raw rule text and falling back to daily.
      [#29263](https://github.com/open-webui/open-webui/pull/29263)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F9E9 **Custom automation schedules stay custom.** Reopening an automation
      with a custom repeat rule no longer loses the custom rule from the editor. [#29260](https://github.com/open-webui/open-webui/pull/29260)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-automation-and-scheduling-changes-in-v0-11-2
  source_release: open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b
  source_type: github_releases
  theme: automation-scheduling
  title: 3 Automation and Scheduling changes in v0.11.2
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-27-changed-loop-self-paced-dynamic-mode-and-the-no-prompt-autonomous-default-are-no|Changed
  /loop: self-paced dynamic mode and the no-prompt autonomous default…]]'
- '[[Changes/GitHub Copilot CLI/2026-08-27-use-x-to-remove-scheduled-every-and-after-prompts-in-schedule-manager|Use
  x to remove scheduled /every and /after prompts in Schedule Manager]]'
- '[[Changes/OpenHands/2026-08-27-2-automation-and-scheduling-changes-in-v1-16-0|2
  Automation and Scheduling changes in v1.16.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b|open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b]]'
source_type: github_releases
theme: automation-scheduling
title: 3 Automation and Scheduling changes in v0.11.2
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Automation and Scheduling changes in v0.11.2

**Open WebUI** · 2026-08-31 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.2) · from [[Releases/Open WebUI/open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b|v0.11.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔟 **Repeating automations keep their count.** An automation set to run a fixed number of times is no longer shown as running once and quietly rewritten to a single run the next time you open and save it. [#29261](https://github.com/open-webui/open-webui/pull/29261), [#29263](https://github.com/open-webui/open-webui/pull/29263)

> 🗓️ **Schedules survive a save.** An automation carrying a start date now shows its real schedule in the list and keeps its weekly or monthly setting when saved, instead of showing raw rule text and falling back to daily. [#29263](https://github.com/open-webui/open-webui/pull/29263)

> 🧩 **Custom automation schedules stay custom.** Reopening an automation with a custom repeat rule no longer loses the custom rule from the editor. [#29260](https://github.com/open-webui/open-webui/pull/29260)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-31-large-tool-calls-stream-faster-through-anthropic-compatible-clients-when-a-strea|🧠 Large tool calls stream faster through Anthropic-compatible…]] · Reliability and Performance
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
## Nearby in Automation and Scheduling

- Earlier: 2026-08-27 · OpenHands · [[Changes/OpenHands/2026-08-27-2-automation-and-scheduling-changes-in-v1-16-0|2 Automation and Scheduling changes in v1.16.0]]
- Later: 2026-09-01 · Codex CLI · [[Changes/Codex CLI/2026-09-01-41457-source-proactive-multi-agent-instructions-from-the-model-catalog-copyberry|♯41457 Source proactive multi-agent instructions from the model catalog @copyberry]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-31-1e320a&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-31-3-automation-and-scheduling-changes-in-v0-11-2.md%0ACard%20ID%3A%20open-webui-2026-08-31-1e320a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->