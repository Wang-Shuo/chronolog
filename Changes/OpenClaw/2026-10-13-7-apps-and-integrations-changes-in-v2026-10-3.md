---
card_id: openclaw-2026-10-13-4c8280
date: '2026-10-13'
description: 'OpenClaw · 2026-10-13 · Apps and Integrations: 7 changes in v2026.10.3
  — Migration warnings and verification timers. Completed plugin migrations stop showing…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2860
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d1dfa245a4ee9c96f1b2f2031360a87b2b525a930503a1304425ff57100dd04c
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-13-4c8280
  comparison: ''
  date: '2026-10-13'
  description: 'OpenClaw — v2026.10.3: 7 Apps and Integrations changes'
  evidence:
  - quote: 'Migration warnings and verification timers. Completed plugin migrations
      stop showing obsolete unfinished warnings. Package verification also keeps its
      deadline when the system clock changes. Genuine pending migrations still need
      attention; see the repair guide . #169004 , thanks to @steipete , @adenzhou1350
      and @wg-mojo .'
    source_release: https://docs.openclaw.ai/releases/2026.10.3
  - quote: 'Switching back to OpenAI. OpenAI models can use the existing built-in
      runtime when Codex is disabled and that runtime can run them. An explicitly
      configured Codex runtime still needs the Codex plugin enabled. #169412 , thanks
      to @obviyus .'
    source_release: https://docs.openclaw.ai/releases/2026.10.3
  - quote: 'Blocked local plugin settings. Doctor and updates preserve enablement,
      settings and policy for installed or linked plugins blocked by a path safety
      check. The plugin stays blocked until its path is repaired; see blocked-plugin
      guidance . #168111 , thanks to @obviyus .'
    source_release: https://docs.openclaw.ai/releases/2026.10.3
  - quote: 'oc-path file edits. The opt-in oc-path plugin refuses openclaw path set
      edits on invalid UTF-8 before rewriting the file, preserving the original bytes.
      Back up and repair or convert the file before retrying. #168491 , thanks to
      @wangmiao0668000666 , @yetval and @Takhoffman .'
    source_release: https://docs.openclaw.ai/releases/2026.10.3
  - quote: 'Webhook callbacks during upgrades. Existing official webhook-channel callbacks
      can be preserved before a deferred plugin replacement is activated, including
      the affected Microsoft Teams path. Authored callbacks and opt-outs remain respected;
      see webhook migration guidance . #169035 , thanks to @steipete and @sirius1024
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.3
  - quote: 'Codex plugin compatibility. Official external Codex packages older than
      2026.9.7 are reported unavailable before they break replies. Eligible official
      updates follow the core release, and failures show useful reasons. Use openclaw
      update repair or openclaw plugins update codex ; linked copies need their source
      updated or load-path override removed. Finish Doctor before restarting when
      migrations are pending. See plugin update guidance . #170306 , thanks to @RomneyDa
      , @steipete and @ezimerman .'
    source_release: https://docs.openclaw.ai/releases/2026.10.3
  - quote: 'Plugin package repairs. A replacement package can be saved while its data
      migration is unfinished, allowing Doctor to continue. Finish openclaw doctor
      --fix before restarting or reloading the replacement. Unavailable automatically
      selected official ClawHub versions can use trusted same-version npm packages,
      or keep compatible installed code with a retry warning. Removing the plugin''s
      entry preserves its backup and pending migration obligations. See the updating
      guide . #170339 , thanks to @RomneyDa , @steipete , @h6y3 , @CodeForcer , @waynegault
      and @rauf543 .'
    source_release: https://docs.openclaw.ai/releases/2026.10.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 7-apps-and-integrations-changes-in-v2026-10-3
  source_release: openclaw-2026-10-13-v2026-10-3-54cedb60
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 7 Apps and Integrations changes in v2026.10.3
  type: change
related_changes:
- '[[Changes/Gemini/2026-10-13-an-easier-way-to-customize-how-gemini-works-for-you-and-more-connected-apps|An
  easier way to customize how Gemini works for you and more connected apps]]'
- '[[Changes/GitHub Copilot CLI/2026-10-13-4-apps-and-integrations-changes-in-v1-0-97|4
  Apps and Integrations changes in v1.0.97]]'
- '[[Changes/Lovable/2026-10-13-approve-every-tool-from-a-chat-connector-at-once|Approve
  every tool from a chat connector at once]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-13-v2026-10-3-54cedb60|openclaw-2026-10-13-v2026-10-3-54cedb60]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 7 Apps and Integrations changes in v2026.10.3
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Apps and Integrations changes in v2026.10.3

**OpenClaw** · 2026-10-13 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.3) · from [[Releases/OpenClaw/openclaw-2026-10-13-v2026-10-3-54cedb60|v2026.10.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Migration warnings and verification timers. Completed plugin migrations stop showing obsolete unfinished warnings. Package verification also keeps its deadline when the system clock changes. Genuine pending migrations still need attention; see the repair guide . #169004 , thanks to @steipete , @adenzhou1350 and @wg-mojo .

> Switching back to OpenAI. OpenAI models can use the existing built-in runtime when Codex is disabled and that runtime can run them. An explicitly configured Codex runtime still needs the Codex plugin enabled. #169412 , thanks to @obviyus .

> Blocked local plugin settings. Doctor and updates preserve enablement, settings and policy for installed or linked plugins blocked by a path safety check. The plugin stays blocked until its path is repaired; see blocked-plugin guidance . #168111 , thanks to @obviyus .

> oc-path file edits. The opt-in oc-path plugin refuses openclaw path set edits on invalid UTF-8 before rewriting the file, preserving the original bytes. Back up and repair or convert the file before retrying. #168491 , thanks to @wangmiao0668000666 , @yetval and @Takhoffman .

> Webhook callbacks during upgrades. Existing official webhook-channel callbacks can be preserved before a deferred plugin replacement is activated, including the affected Microsoft Teams path. Authored callbacks and opt-outs remain respected; see webhook migration guidance . #169035 , thanks to @steipete and @sirius1024 .

> Codex plugin compatibility. Official external Codex packages older than 2026.9.7 are reported unavailable before they break replies. Eligible official updates follow the core release, and failures show useful reasons. Use openclaw update repair or openclaw plugins update codex ; linked copies need their source updated or load-path override removed. Finish Doctor before restarting when migrations are pending. See plugin update guidance . #170306 , thanks to @RomneyDa , @steipete and @ezimerman .

> Plugin package repairs. A replacement package can be saved while its data migration is unfinished, allowing Doctor to continue. Finish openclaw doctor --fix before restarting or reloading the replacement. Unavailable automatically selected official ClawHub versions can use trusted same-version npm packages, or keep compatible installed code with a retry warning. Removing the plugin's entry preserves its backup and pending migration obligations. See the updating guide . #170339 , thanks to @RomneyDa , @steipete , @h6y3 , @CodeForcer , @waynegault and @rauf543 .

Source: https://docs.openclaw.ai/releases/2026.10.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-13-2-account-and-access-changes-in-v2026-10-3|2 Account and Access changes in v2026.10.3]] · Account and Access
- [[Changes/OpenClaw/2026-10-13-replies-after-native-compaction-the-next-message-waits-for-saved-conversation-hi|Replies after native compaction]] · Context Window
- [[Changes/OpenClaw/2026-10-13-5-memory-and-personalization-changes-in-v2026-10-3|5 Memory and Personalization changes in v2026.10.3]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-13-claude-cli-session-tools-later-turns-keep-their-authorized-session-history-and-a|Claude CLI session tools]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-13-muse-wonder-meta-users-can-select-muse-wonder-with-text-and-image-input-and-max|Muse Wonder. Meta users can select Muse Wonder with text and image input and max thinking]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-13-5-developer-workflow-changes-in-v2026-10-3|5 Developer Workflow changes in v2026.10.3]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-13-windows-service-accounts-updates-recognize-different-task-scheduler-names-for-th|Windows service accounts]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-13-3-safety-and-privacy-changes-in-v2026-10-3|3 Safety and Privacy changes in v2026.10.3]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-13-3-model-support-changes-in-v2026-10-3|3 Model Support changes in v2026.10.3]] · Model Support
- [[Changes/OpenClaw/2026-10-13-24-other-changes-in-v2026-10-3|24 other changes in v2026.10.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-13 · Lovable · [[Changes/Lovable/2026-10-13-approve-every-tool-from-a-chat-connector-at-once|Approve every tool from a chat connector at once]]
- Later: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-7-apps-and-integrations-changes-in-v2-1-300|7 Apps and Integrations changes in v2.1.300]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-13-4c8280&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-13-7-apps-and-integrations-changes-in-v2026-10-3.md%0ACard%20ID%3A%20openclaw-2026-10-13-4c8280%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->