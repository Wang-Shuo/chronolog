---
card_id: open-webui-2026-03-08-c65e72
date: '2026-03-08'
description: 'Open WebUI · 2026-03-08 · Automation and Scheduling: ♾️ **Artifacts
  reactive loop fix.** Fixed an infinite reactive loop in chat when artifacts are
  present by…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add
    data clean schedule]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 796
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 4748c12d50ac76cc5805b3d9780fa04c455fea832470c3df2290850dd70a5355
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-08-c65e72
  comparison: ''
  date: '2026-03-08'
  description: 'Open WebUI — v0.8.9: ♾️ **Artifacts reactive loop fix.** Fixed an
    infinite reactive loop in chat when artifacts are present by moving the animation
    frame logic outside the reactive block, preventing continuous re-rendering and
    CPU usage. [#22238](https://github.com/open-webui/open-webui/pull/22238), [Commit](https://github.com/open-webui/open-webui/commit/626fcff417afba642f4f71e0498267a21435c524)'
  evidence:
  - quote: ♾️ **Artifacts reactive loop fix.** Fixed an infinite reactive loop in
      chat when artifacts are present by moving the animation frame logic outside
      the reactive block, preventing continuous re-rendering and CPU usage. [#22238](https://github.com/open-webui/open-webui/pull/22238),
      [Commit](https://github.com/open-webui/open-webui/commit/626fcff417afba642f4f71e0498267a21435c524)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: artifacts-reactive-loop-fix-fixed-an-infinite-reactive-loop-in-chat-when-artifac
  source_release: open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb
  source_type: github_releases
  theme: automation-scheduling
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: ♾️ **Artifacts reactive loop fix.** Fixed an infinite reactive loop in chat…
  type: change
related_changes:
- '[[Changes/Cursor/2026-03-05-cursor-now-supports-automations-for-building-always-on-agents-that-run-based-on-fb3c5d|Cursor
  now supports automations for building always-on agents that run based…]]'
- '[[Changes/Claude Code/2026-03-07-added-cron-scheduling-tools-for-recurring-prompts-within-a-session|Added
  cron scheduling tools for recurring prompts within a session]]'
- '[[Changes/Claude Code/2026-03-07-added-loop-command-to-run-a-prompt-or-slash-command-on-a-recurring-interval-e-g|Added
  /loop command to run a prompt or slash command on a recurring interval…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb|open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb]]'
source_type: github_releases
theme: automation-scheduling
title: ♾️ Artifacts reactive loop fix. Fixed an infinite reactive loop in chat…
type: change
---

<!-- chronolog:begin region="header" -->
# ♾️ **Artifacts reactive loop fix.** Fixed an infinite reactive loop in chat…

**Open WebUI** · 2026-03-08 · [[Themes/automation-scheduling|Automation and Scheduling]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.9) · from [[Releases/Open WebUI/open-webui-2026-03-08-v0-8-9-github-294335564-7bdc11cb|v0.8.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> ♾️ **Artifacts reactive loop fix.** Fixed an infinite reactive loop in chat when artifacts are present by moving the animation frame logic outside the reactive block, preventing continuous re-rendering and CPU usage. [#22238](https://github.com/open-webui/open-webui/pull/22238), [Commit](https://github.com/open-webui/open-webui/commit/626fcff417afba642f4f71e0498267a21435c524)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-08-image-generation-in-temporary-chats-generated-images-now-display-correctly-in-te|🖌️ Image generation in temporary chats. Generated images now display correctly…]] · Image Generation
- [[Changes/Open WebUI/2026-03-08-2-context-window-changes-in-v0-8-9|2 Context Window changes in v0.8.9]] · Context Window
- [[Changes/Open WebUI/2026-03-08-microsoft-oauth-refresh-token-fix-fixed-a-bug-where-microsoft-oauth-refresh-toke|🔐 Microsoft OAuth refresh token fix. Fixed a bug where Microsoft OAuth refresh…]] · Account and Access
- [[Changes/Open WebUI/2026-03-08-17-developer-workflow-changes-in-v0-8-9|17 Developer Workflow changes in v0.8.9]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-08-5-interface-experience-changes-in-v0-8-9|5 Interface Experience changes in v0.8.9]] · Interface Experience
- [[Changes/Open WebUI/2026-03-08-2-voice-and-audio-changes-in-v0-8-9|2 Voice and Audio changes in v0.8.9]] · Voice and Audio
- [[Changes/Open WebUI/2026-03-08-android-photo-capture-fixed-an-issue-where-the-first-photo-taken-in-chat-appeare|📷 Android photo capture. Fixed an issue where the first photo taken in chat…]] · Files and Data
- [[Changes/Open WebUI/2026-03-08-2-search-and-browsing-changes-in-v0-8-9|2 Search and Browsing changes in v0.8.9]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-08-open-terminal-html-editing-users-can-now-edit-html-source-files-in-open-terminal|✏️ Open Terminal HTML editing. Users can now edit HTML source files in Open…]] · Editor Experience
- [[Changes/Open WebUI/2026-03-08-system-metrics-via-opentelemetry-administrators-can-now-monitor-python-runtime-a|📡 System metrics via OpenTelemetry. Administrators can now monitor Python…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-03-08-13-reliability-and-performance-changes-in-v0-8-9|13 Reliability and Performance changes in v0.8.9]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-08-9-model-support-changes-in-v0-8-9|9 Model Support changes in v0.8.9]] · Model Support
- [[Changes/Open WebUI/2026-03-08-open-terminal-permission-fix-open-terminal-is-now-visible-without-requiring-allo|🖥️ Open Terminal permission fix. Open Terminal is now visible without requiring…]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-08-14-other-changes-in-v0-8-9|14 other changes in v0.8.9]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-03-07 · Claude Code · [[Changes/Claude Code/2026-03-07-added-loop-command-to-run-a-prompt-or-slash-command-on-a-recurring-interval-e-g|Added /loop command to run a prompt or slash command on a recurring interval…]]
- Later: 2026-03-10 · Claude Code · [[Changes/Claude Code/2026-03-10-added-claude-code-disable-cron-environment-variable-to-immediately-stop-schedule|Added CLAUDE_CODE_DISABLE_CRON environment variable to immediately stop scheduled…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-08-c65e72&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-08-artifacts-reactive-loop-fix-fixed-an-infinite-reactive-loop-in-chat-when-artifac.md%0ACard%20ID%3A%20open-webui-2026-03-08-c65e72%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->