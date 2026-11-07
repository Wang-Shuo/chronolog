---
card_id: openclaw-2026-10-08-34dd0c
date: '2026-10-08'
description: 'OpenClaw · 2026-10-08 · Interface Experience: 4 changes in v2026.9.9
  — Channel conversation history. Messages sent from the dashboard into a channel
  keep their…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2734
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 106099758de6dd816bcf48add82004c145525f1ac8d5a87be729e59a2a18ac74
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-08-34dd0c
  comparison: ''
  date: '2026-10-08'
  description: 'OpenClaw — v2026.9.9: 4 Interface Experience changes'
  evidence:
  - quote: 'Channel conversation history. Messages sent from the dashboard into a
      channel keep their original conversation association. New messages from linked
      requesters also stop appearing twice in Claude CLI chat history, with internal
      requester instructions kept out of the displayed text. Existing records are
      not rewritten. #151786 by @Alix-007 , reported by @Rotocruz ; #161012 by @Marvinthebored
      and @Peetiegonzalez , with reports from @Oldrich333 , @holgergruenhagen and
      @obnoxious2011-cmd .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Update completion. Updating OpenClaw no longer fails just because it is
      saving data at the same time. Updates from affected older versions keep the
      files plugins need to finish their upgrades, and global npm installs avoid a
      false recovery-file check failure. Once required database work has finished,
      a stalled shutdown can also stop holding up the update result; that safeguard
      applies to subsequent updates run by the fixed installation. 30c180a , ecac0d3
      (original migration fix) , 55360c6 by @RomneyDa ; #161258 by @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Starting background jobs. Fixed a startup problem that could freeze chat
      or disconnect the web interface when a scheduled job or Skill Workshop review
      began. This applies to jobs using their agent''s configured workspace, including
      while older chat history is condensed. Their file access remains limited to
      the task folder . Scheduled jobs can also proceed using existing model information
      when a catalog refresh is slow. #164049 by @steipete ; #161132 by @jayzhou2309
      , reported by @Flakedict and verified by @obviyus .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Delegated task completion. Parents receive complete new CLI-backed subagent
      answers instead of a shortened prefix. Finished child trees release capacity
      even when their completion notification is suspended, and same-model retries
      retain permitted follow-up delegation. Older truncated answers are not repaired.
      #162843 by @zyz619963502zyz , with diagnosis by @holgergruenhagen ; #162368
      by @armstrongsam25 , reported by @davidcittadini , both verified by @obviyus
      ; #163032 by @stackingrockss .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-interface-experience-changes-in-v2026-9-9
  source_release: openclaw-2026-10-08-v2026-9-9-933614cc
  source_type: openclaw_changelog
  theme: interface-experience
  title: 4 Interface Experience changes in v2026.9.9
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-08-clicking-a-sessions-sidebar-row-now-reliably-switches-sessions-during-split-view|Clicking
  a Sessions sidebar row now reliably switches sessions during split-view…]]'
- '[[Changes/Google Antigravity/2026-10-08-sidebar-drag-and-drop-ui-extensions-and-localized-conversation-timestamps|Sidebar
  drag-and-drop, UI Extensions, and localized conversation timestamps]]'
- '[[Changes/Google Antigravity/2026-10-08-you-can-now-drag-and-drop-conversations-between-sections-in-the-sidebar-to-organ|Drag
  and drop conversations between sections in the sidebar to organize your projects]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|openclaw-2026-10-08-v2026-9-9-933614cc]]'
source_type: openclaw_changelog
theme: interface-experience
title: 4 Interface Experience changes in v2026.9.9
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Interface Experience changes in v2026.9.9

**OpenClaw** · 2026-10-08 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.9) · from [[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|v2026.9.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Channel conversation history. Messages sent from the dashboard into a channel keep their original conversation association. New messages from linked requesters also stop appearing twice in Claude CLI chat history, with internal requester instructions kept out of the displayed text. Existing records are not rewritten. #151786 by @Alix-007 , reported by @Rotocruz ; #161012 by @Marvinthebored and @Peetiegonzalez , with reports from @Oldrich333 , @holgergruenhagen and @obnoxious2011-cmd .

> Update completion. Updating OpenClaw no longer fails just because it is saving data at the same time. Updates from affected older versions keep the files plugins need to finish their upgrades, and global npm installs avoid a false recovery-file check failure. Once required database work has finished, a stalled shutdown can also stop holding up the update result; that safeguard applies to subsequent updates run by the fixed installation. 30c180a , ecac0d3 (original migration fix) , 55360c6 by @RomneyDa ; #161258 by @steipete .

> Starting background jobs. Fixed a startup problem that could freeze chat or disconnect the web interface when a scheduled job or Skill Workshop review began. This applies to jobs using their agent's configured workspace, including while older chat history is condensed. Their file access remains limited to the task folder . Scheduled jobs can also proceed using existing model information when a catalog refresh is slow. #164049 by @steipete ; #161132 by @jayzhou2309 , reported by @Flakedict and verified by @obviyus .

> Delegated task completion. Parents receive complete new CLI-backed subagent answers instead of a shortened prefix. Finished child trees release capacity even when their completion notification is suspended, and same-model retries retain permitted follow-up delegation. Older truncated answers are not repaired. #162843 by @zyz619963502zyz , with diagnosis by @holgergruenhagen ; #162368 by @armstrongsam25 , reported by @davidcittadini , both verified by @obviyus ; #163032 by @stackingrockss .

Source: https://docs.openclaw.ai/releases/2026.9.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-08-4-agent-mode-changes-in-v2026-9-9|4 Agent Mode changes in v2026.9.9]] · Agent Mode
- [[Changes/OpenClaw/2026-10-08-model-retries-and-context-one-shot-model-requests-through-the-gateway-retain-the|Model retries and context]] · Context Window
- [[Changes/OpenClaw/2026-10-08-2-voice-and-audio-changes-in-v2026-9-9|2 Voice and Audio changes in v2026.9.9]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-08-3-developer-workflow-changes-in-v2026-9-9|3 Developer Workflow changes in v2026.9.9]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-08-windows-mxc-sandbox-the-optional-mxc-sandbox-can-start-and-run-tools-on-compatib|Windows MXC sandbox]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-08-claude-haiku-5-5-you-can-select-haiku-5-5-through-the-anthropic-api-and-claude-c|Claude Haiku 5.5. You can select Haiku 5.5 through the Anthropic API and Claude CLI]] · Pricing Model
- [[Changes/OpenClaw/2026-10-08-10-apps-and-integrations-changes-in-v2026-9-9|10 Apps and Integrations changes in v2026.9.9]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-08-2-account-and-access-changes-in-v2026-9-9|2 Account and Access changes in v2026.9.9]] · Account and Access
- [[Changes/OpenClaw/2026-10-08-2-enterprise-and-administration-changes-in-v2026-9-9|2 Enterprise and Administration changes in v2026.9.9]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-08-4-model-support-changes-in-v2026-9-9|4 Model Support changes in v2026.9.9]] · Model Support
- [[Changes/OpenClaw/2026-10-08-3-mobile-and-desktop-changes-in-v2026-9-9|3 Mobile and Desktop changes in v2026.9.9]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-08-feishu-attachments-files-sent-with-captions-or-together-in-feishu-lark-posts-rea|Feishu attachments]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-08-2-memory-and-personalization-changes-in-v2026-9-9|2 Memory and Personalization changes in v2026.9.9]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-08-2-automation-and-scheduling-changes-in-v2026-9-9|2 Automation and Scheduling changes in v2026.9.9]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-08-september-database-compatibility-upgrading-from-september-stable-keeps-shared-da|September database compatibility]] · Collaboration
- [[Changes/OpenClaw/2026-10-08-24-other-changes-in-v2026-9-9|24 other changes in v2026.9.9]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-10-08 · Google Antigravity · [[Changes/Google Antigravity/2026-10-08-you-can-now-drag-and-drop-conversations-between-sections-in-the-sidebar-to-organ|Drag and drop conversations between sections in the sidebar to organize your projects]]
- Later: 2026-10-08 · OpenHands · [[Changes/OpenHands/2026-10-08-test-e2e-open-commits-from-the-tabs-pane-s-own-menu-by-enyst-in-https-github-com|test(e2e): open Commits from the tabs pane's own menu]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-08-34dd0c&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-08-4-interface-experience-changes-in-v2026-9-9.md%0ACard%20ID%3A%20openclaw-2026-10-08-34dd0c%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->