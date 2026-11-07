---
card_id: openclaw-2026-07-13-f3013e
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Collaboration: 20 changes in v2026.7.1 — The
  Control UI Usage page now makes recent estimated costs, daily values, and each provider…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create
    a team here: (source link)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2740
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 67e8c76dff4a2e06eb41b09ac4d72c960748927075e33a7e95f9f3509a078cf6
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-f3013e
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 20 Collaboration changes'
  evidence:
  - quote: 'The Control UI Usage page now makes recent estimated costs, daily values,
      and each provider, model, agent, or channel''s share easier to compare without
      repeated reloads or hovering. #100432'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Browser control is easier to use across machines: operators can pair the
      bundled Chrome extension with a remote Gateway, share only selected signed-in
      tabs, diagnose Windows and WSL2 connection details, and revoke access by removing
      a tab from the OpenClaw group. Agents can also wait for delayed downloads and
      save the finished file to a guarded local path with its final URL and suggested
      name.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Microsoft Teams file delivery and chat lookup now cap large Microsoft
      Graph responses and return a labeled error instead of risking a process crash.
      #97784 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Microsoft Teams personal-chat welcome card now displays its greeting
      with the intended bold, medium emphasis. #96290 Thanks @ly-wang19, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Microsoft Teams feedback on long responses now carries intact emoji into
      reflection processing, preventing a cutoff from corrupting prompts, logs, or
      encoding. #96578 Thanks @llagy007, @weeli-009.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Mattermost teams with more than 200 members can now discover and address
      valid peers beyond the first page of the team directory. #98877 Related #98871
      . Thanks @qingminglong.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Feishu Drive can now list files beyond the first page of a large shared
      folder by accepting its returned next_page_token , with invalid page sizes rejected
      clearly before the request. #101572 Thanks @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Chinese, Japanese, and Korean bold labels followed immediately by text
      now render as bold instead of exposing literal ** markers in Telegram and other
      shared-Markdown channels. #101230 Thanks @nicknmorty.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'MiniMax and other shared provider usage checks now fail safely on oversized
      or malformed replies instead of buffering them without limit. #97659 Thanks
      @cxbasdev, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Shared Codex app-server clients now keep usage limits, auth cooldowns,
      thread subscriptions, and resumed connections tied to the account and conversation
      that actually owns them. #101376'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Standalone ACP clients now close the shared SQLite state database during
      shutdown so hot reloads and immediate restarts can reopen it without stale locks
      or callbacks. #100691 Thanks @lzy3538.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Refreshed native language packs now cover workspace files, sharing actions,
      folder states, Android SMS guidance, message delivery states, and related branding.
      a9b0a9a
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Session tools now display the correct absolute path for projects beside
      the home directory instead of turning a shared text prefix into a misleading
      ~... path. #96562 Thanks @he-yufeng.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Browser screenshots used privately for visual inspection are no longer
      attached automatically to channel replies and are shared only when explicitly
      requested. #101434'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Brought additional Docker checks into the shared QA inventory, improving
      release coverage and reducing duplicated validation work. #97708 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made QA credential requests fail cleanly when a shared broker returns
      an unexpectedly large response. #98619 Thanks @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Established a shared internal foundation for loading runtime modules consistently
      without changing behavior. #99261 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Strengthened lint protection against accidentally sharing one mutable
      value across multiple array entries. #100122'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored compilation of shared Apple-platform tests covering pairing setup
      results. #100355'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored compilation of shared Apple platform tests used for local validation.
      #101372'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 20-collaboration-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: collaboration
  title: 20 Collaboration changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-07-09-31587-stabilize-shared-rollout-budget-test-jif-oai|♯31587
  Stabilize shared rollout budget test @jif-oai]]'
- '[[Changes/Notion/2026-07-09-you-can-now-share-your-notion-workers|Share your Notion
  Workers]]'
- '[[Changes/ElevenLabs/2026-07-13-workspaces|Workspaces]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: collaboration
title: 20 Collaboration changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Collaboration changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The Control UI Usage page now makes recent estimated costs, daily values, and each provider, model, agent, or channel's share easier to compare without repeated reloads or hovering. #100432

> Browser control is easier to use across machines: operators can pair the bundled Chrome extension with a remote Gateway, share only selected signed-in tabs, diagnose Windows and WSL2 connection details, and revoke access by removing a tab from the OpenClaw group. Agents can also wait for delayed downloads and save the finished file to a guarded local path with its final URL and suggested name.

> Microsoft Teams file delivery and chat lookup now cap large Microsoft Graph responses and return a labeled error instead of risking a process crash. #97784 Thanks @alix-007.

> The Microsoft Teams personal-chat welcome card now displays its greeting with the intended bold, medium emphasis. #96290 Thanks @ly-wang19, @vincentkoc.

> Microsoft Teams feedback on long responses now carries intact emoji into reflection processing, preventing a cutoff from corrupting prompts, logs, or encoding. #96578 Thanks @llagy007, @weeli-009.

> Mattermost teams with more than 200 members can now discover and address valid peers beyond the first page of the team directory. #98877 Related #98871 . Thanks @qingminglong.

> Feishu Drive can now list files beyond the first page of a large shared folder by accepting its returned next_page_token , with invalid page sizes rejected clearly before the request. #101572 Thanks @zhangguiping-xydt.

> Chinese, Japanese, and Korean bold labels followed immediately by text now render as bold instead of exposing literal ** markers in Telegram and other shared-Markdown channels. #101230 Thanks @nicknmorty.

> MiniMax and other shared provider usage checks now fail safely on oversized or malformed replies instead of buffering them without limit. #97659 Thanks @cxbasdev, @vincentkoc.

> Shared Codex app-server clients now keep usage limits, auth cooldowns, thread subscriptions, and resumed connections tied to the account and conversation that actually owns them. #101376

> Standalone ACP clients now close the shared SQLite state database during shutdown so hot reloads and immediate restarts can reopen it without stale locks or callbacks. #100691 Thanks @lzy3538.

> Refreshed native language packs now cover workspace files, sharing actions, folder states, Android SMS guidance, message delivery states, and related branding. a9b0a9a

> Session tools now display the correct absolute path for projects beside the home directory instead of turning a shared text prefix into a misleading ~... path. #96562 Thanks @he-yufeng.

> Browser screenshots used privately for visual inspection are no longer attached automatically to channel replies and are shared only when explicitly requested. #101434

> Brought additional Docker checks into the shared QA inventory, improving release coverage and reducing duplicated validation work. #97708 Thanks @romneyda.

> Made QA credential requests fail cleanly when a shared broker returns an unexpectedly large response. #98619 Thanks @zengwen-dt.

> Established a shared internal foundation for loading runtime modules consistently without changing behavior. #99261 Thanks @romneyda.

> Strengthened lint protection against accidentally sharing one mutable value across multiple array entries. #100122

> Restored compilation of shared Apple-platform tests covering pairing setup results. #100355

> Restored compilation of shared Apple platform tests used for local validation. #101372

Source: https://docs.openclaw.ai/releases/2026.7.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-07-13-5-projects-and-workspaces-changes-in-v2026-7-1|5 Projects and Workspaces changes in v2026.7.1]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-07-13-99-developer-workflow-changes-in-v2026-7-1|99 Developer Workflow changes in v2026.7.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-07-13-69-context-window-changes-in-v2026-7-1|69 Context Window changes in v2026.7.1]] · Context Window
- [[Changes/OpenClaw/2026-07-13-10-accessibility-and-localization-changes-in-v2026-7-1|10 Accessibility and Localization changes in v2026.7.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-07-13-64-interface-experience-changes-in-v2026-7-1|64 Interface Experience changes in v2026.7.1]] · Interface Experience
- [[Changes/OpenClaw/2026-07-13-whatsapp-and-telegram-default-account-routing-warnings-are-now-available-through|WhatsApp and Telegram default-account routing warnings are now available through…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-07-13-132-agent-mode-changes-in-v2026-7-1|132 Agent Mode changes in v2026.7.1]] · Agent Mode
- [[Changes/OpenClaw/2026-07-13-after-one-generated-video-clip-is-ready-a-different-next-clip-can-start-immediat|After one generated video clip is ready, a different next clip can start immediately…]] · Video Generation
- [[Changes/OpenClaw/2026-07-13-79-automation-and-scheduling-changes-in-v2026-7-1|79 Automation and Scheduling changes in v2026.7.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-07-13-130-model-support-changes-in-v2026-7-1|130 Model Support changes in v2026.7.1]] · Model Support
- [[Changes/OpenClaw/2026-07-13-69-account-and-access-changes-in-v2026-7-1|69 Account and Access changes in v2026.7.1]] · Account and Access
- [[Changes/OpenClaw/2026-07-13-59-safety-and-privacy-changes-in-v2026-7-1|59 Safety and Privacy changes in v2026.7.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-07-13-224-mobile-and-desktop-changes-in-v2026-7-1|224 Mobile and Desktop changes in v2026.7.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-07-13-83-voice-and-audio-changes-in-v2026-7-1|83 Voice and Audio changes in v2026.7.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-07-13-18-pricing-model-changes-in-v2026-7-1|18 Pricing Model changes in v2026.7.1]] · Pricing Model
- [[Changes/OpenClaw/2026-07-13-21-editor-experience-changes-in-v2026-7-1|21 Editor Experience changes in v2026.7.1]] · Editor Experience
- [[Changes/OpenClaw/2026-07-13-7-image-generation-changes-in-v2026-7-1|7 Image Generation changes in v2026.7.1]] · Image Generation
- [[Changes/OpenClaw/2026-07-13-channel-setup-warnings-are-now-available-as-structured-doctor-lint-findings-with|Channel setup warnings are now available as structured Doctor lint findings…]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-07-13-4-enterprise-and-administration-changes-in-v2026-7-1|4 Enterprise and Administration changes in v2026.7.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-07-13-2-presentation-creation-changes-in-v2026-7-1|2 Presentation Creation changes in v2026.7.1]] · Presentation Creation
- [[Changes/OpenClaw/2026-07-13-136-memory-and-personalization-changes-in-v2026-7-1|136 Memory and Personalization changes in v2026.7.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-07-13-213-apps-and-integrations-changes-in-v2026-7-1|213 Apps and Integrations changes in v2026.7.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-07-13-8-search-and-browsing-changes-in-v2026-7-1|8 Search and Browsing changes in v2026.7.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-07-13-13-files-and-data-changes-in-v2026-7-1|13 Files and Data changes in v2026.7.1]] · Files and Data
- [[Changes/OpenClaw/2026-07-13-19-multimodal-input-changes-in-v2026-7-1|19 Multimodal Input changes in v2026.7.1]] · Multimodal Input
- [[Changes/OpenClaw/2026-07-13-38-reliability-and-performance-changes-in-v2026-7-1|38 Reliability and Performance changes in v2026.7.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-07-13-686-other-changes-in-v2026-7-1|686 other changes in v2026.7.1]] · Other changes
- [[Changes/OpenClaw/2026-07-13-official-openclaw-container-images-are-now-available-from-docker-hub-as-well-as|Official OpenClaw container images are now available from Docker Hub as well…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Collaboration

- Earlier: 2026-07-13 · ElevenLabs · [[Changes/ElevenLabs/2026-07-13-workspaces|Workspaces]]
- Later: 2026-07-16 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-16-2-collaboration-changes-in-v1-0-71|2 Collaboration changes in v1.0.71]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-01-11 · Descript · [[Changes/Descript/2019-01-11-create-a-team-here-https-web-descript-com-drive-new-teams|Create a team here: (source link)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-f3013e&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-20-collaboration-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-f3013e%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->