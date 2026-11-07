---
card_id: openclaw-2026-10-13-e791eb
date: '2026-10-13'
description: 'OpenClaw · 2026-10-13 · Safety and Privacy: 3 changes in v2026.10.3
  — Updates requested in chat. Fixed a Doctor cleanup check that falsely refused permission…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2268
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 373c9352f413eb5db902fbc657c56d8b18de42ec78606fc595ec3857a9d7169c
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-13-e791eb
  comparison: ''
  date: '2026-10-13'
  description: 'OpenClaw — v2026.10.3: 3 Safety and Privacy changes'
  evidence:
  - quote: 'Updates requested in chat. Fixed a Doctor cleanup check that falsely refused
      permission and rolled back chat-requested updates, sometimes leaving plugin
      upgrades unfinished. #170218 , thanks to @RomneyDa , @hannesrudolph , @ezimerman
      , @yoyo837 , @aia007731-lab , @justinforsound and @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.3
  - quote: 'Codex follow-up messages. Compatible follow-ups can continue after failed
      conversation preparation while an existing background command keeps running.
      Incompatible permission or policy changes remain refused while protected work
      runs. #169431 , thanks to @jjjhenriksen and @RomneyDa .'
    source_release: https://docs.openclaw.ai/releases/2026.10.3
  - quote: 'IPv6 provider fallback. Guarded model requests can try a working IPv6
      address when IPv4 is unreachable and Node address-family autoselection is enabled.
      Configured network security checks still apply. See connectivity troubleshooting
      . #168973 , thanks to @steipete , @an2in , @georgenaz , @motookoyama and @orthogonalistic
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 3-safety-and-privacy-changes-in-v2026-10-3
  source_release: openclaw-2026-10-13-v2026-10-3-54cedb60
  source_type: openclaw_changelog
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v2026.10.3
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-13-3-safety-and-privacy-changes-in-v1-0-97|3
  Safety and Privacy changes in v1.0.97]]'
- '[[Changes/HeyGen/2026-10-13-admin-billing-and-security|Admin, billing and security]]'
- '[[Changes/HeyGen/2026-10-13-sso-join-controls|SSO join controls]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-13-v2026-10-3-54cedb60|openclaw-2026-10-13-v2026-10-3-54cedb60]]'
source_type: openclaw_changelog
theme: safety-privacy
title: 3 Safety and Privacy changes in v2026.10.3
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v2026.10.3

**OpenClaw** · 2026-10-13 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.3) · from [[Releases/OpenClaw/openclaw-2026-10-13-v2026-10-3-54cedb60|v2026.10.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Updates requested in chat. Fixed a Doctor cleanup check that falsely refused permission and rolled back chat-requested updates, sometimes leaving plugin upgrades unfinished. #170218 , thanks to @RomneyDa , @hannesrudolph , @ezimerman , @yoyo837 , @aia007731-lab , @justinforsound and @steipete .

> Codex follow-up messages. Compatible follow-ups can continue after failed conversation preparation while an existing background command keeps running. Incompatible permission or policy changes remain refused while protected work runs. #169431 , thanks to @jjjhenriksen and @RomneyDa .

> IPv6 provider fallback. Guarded model requests can try a working IPv6 address when IPv4 is unreachable and Node address-family autoselection is enabled. Configured network security checks still apply. See connectivity troubleshooting . #168973 , thanks to @steipete , @an2in , @georgenaz , @motookoyama and @orthogonalistic .

Source: https://docs.openclaw.ai/releases/2026.10.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-13-2-account-and-access-changes-in-v2026-10-3|2 Account and Access changes in v2026.10.3]] · Account and Access
- [[Changes/OpenClaw/2026-10-13-replies-after-native-compaction-the-next-message-waits-for-saved-conversation-hi|Replies after native compaction]] · Context Window
- [[Changes/OpenClaw/2026-10-13-5-memory-and-personalization-changes-in-v2026-10-3|5 Memory and Personalization changes in v2026.10.3]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-13-claude-cli-session-tools-later-turns-keep-their-authorized-session-history-and-a|Claude CLI session tools]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-13-7-apps-and-integrations-changes-in-v2026-10-3|7 Apps and Integrations changes in v2026.10.3]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-13-muse-wonder-meta-users-can-select-muse-wonder-with-text-and-image-input-and-max|Muse Wonder. Meta users can select Muse Wonder with text and image input and max thinking]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-13-5-developer-workflow-changes-in-v2026-10-3|5 Developer Workflow changes in v2026.10.3]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-13-windows-service-accounts-updates-recognize-different-task-scheduler-names-for-th|Windows service accounts]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-13-3-model-support-changes-in-v2026-10-3|3 Model Support changes in v2026.10.3]] · Model Support
- [[Changes/OpenClaw/2026-10-13-24-other-changes-in-v2026-10-3|24 other changes in v2026.10.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-13 · HeyGen · [[Changes/HeyGen/2026-10-13-sso-join-controls|SSO join controls]]
- Later: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-2-safety-and-privacy-changes-in-v2-1-300|2 Safety and Privacy changes in v2.1.300]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-13-e791eb&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-13-3-safety-and-privacy-changes-in-v2026-10-3.md%0ACard%20ID%3A%20openclaw-2026-10-13-e791eb%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->