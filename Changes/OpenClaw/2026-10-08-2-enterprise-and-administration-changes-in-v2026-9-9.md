---
card_id: openclaw-2026-10-08-54423f
date: '2026-10-08'
description: 'OpenClaw · 2026-10-08 · Enterprise and Administration: 2 changes in
  v2026.9.9 — Telegram Control UI. To open OpenClaw''s Mini App in Telegram, send
  /controlui…'
diffusion:
  first_in_tracked: '[[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export
    members as CSV (for Enterprise Plans) Quickly download a list of the people…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2459
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 47399eefed5046738c1c51ee3780de289a0244e5cfd650fd02170f42f6447495
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-08-54423f
  comparison: ''
  date: '2026-10-08'
  description: 'OpenClaw — v2026.9.9: 2 Enterprise and Administration changes'
  evidence:
  - quote: 'Telegram Control UI. To open OpenClaw''s Mini App in Telegram, send /controlui
      in a private chat with the bot. /dashboard now belongs to session dashboards.
      Follow the migration guide to replace old shortcuts and get a fresh button.
      Access requires your numeric Telegram ID in the bot''s owner settings; ask an
      administrator to add it if you relied on a wildcard or username. #161369 by
      @mmaps , with command separation by @joshavant .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Export approvals. Diagnostics and trajectory exports keep their designated
      approval device even when the prompt is delivered to a private chat. Other approval-only
      devices cannot approve the bound command; the administrator bypass remains.
      #125663 by @RomneyDa .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 2-enterprise-and-administration-changes-in-v2026-9-9
  source_release: openclaw-2026-10-08-v2026-9-9-933614cc
  source_type: openclaw_changelog
  theme: enterprise-admin
  title: 2 Enterprise and Administration changes in v2026.9.9
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-07-add-enterprise-permissions-limitto-to-enforce-managed-domain-boundaries-for-netw|Add
  enterprise permissions.limitTo to enforce managed domain boundaries for network…]]'
- '[[Changes/Claude Code/2026-10-08-claude-tag-changed-claude-s-notice-that-a-channel-shared-across-enterprise-grid|Claude
  Tag Changed Claude''s notice that a channel shared across Enterprise Grid…]]'
- '[[Changes/Lovable/2026-10-08-publish-to-invited-people-only-on-free-and-pro-plans|Publish
  to invited people only on Free and Pro plans]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|openclaw-2026-10-08-v2026-9-9-933614cc]]'
source_type: openclaw_changelog
theme: enterprise-admin
title: 2 Enterprise and Administration changes in v2026.9.9
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Enterprise and Administration changes in v2026.9.9

**OpenClaw** · 2026-10-08 · [[Themes/enterprise-admin|Enterprise and Administration]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.9) · from [[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|v2026.9.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Telegram Control UI. To open OpenClaw's Mini App in Telegram, send /controlui in a private chat with the bot. /dashboard now belongs to session dashboards. Follow the migration guide to replace old shortcuts and get a fresh button. Access requires your numeric Telegram ID in the bot's owner settings; ask an administrator to add it if you relied on a wildcard or username. #161369 by @mmaps , with command separation by @joshavant .

> Export approvals. Diagnostics and trajectory exports keep their designated approval device even when the prompt is delivered to a private chat. Other approval-only devices cannot approve the bound command; the administrator bypass remains. #125663 by @RomneyDa .

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
- [[Changes/OpenClaw/2026-10-08-4-interface-experience-changes-in-v2026-9-9|4 Interface Experience changes in v2026.9.9]] · Interface Experience
- [[Changes/OpenClaw/2026-10-08-10-apps-and-integrations-changes-in-v2026-9-9|10 Apps and Integrations changes in v2026.9.9]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-08-2-account-and-access-changes-in-v2026-9-9|2 Account and Access changes in v2026.9.9]] · Account and Access
- [[Changes/OpenClaw/2026-10-08-4-model-support-changes-in-v2026-9-9|4 Model Support changes in v2026.9.9]] · Model Support
- [[Changes/OpenClaw/2026-10-08-3-mobile-and-desktop-changes-in-v2026-9-9|3 Mobile and Desktop changes in v2026.9.9]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-08-feishu-attachments-files-sent-with-captions-or-together-in-feishu-lark-posts-rea|Feishu attachments]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-08-2-memory-and-personalization-changes-in-v2026-9-9|2 Memory and Personalization changes in v2026.9.9]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-08-2-automation-and-scheduling-changes-in-v2026-9-9|2 Automation and Scheduling changes in v2026.9.9]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-08-september-database-compatibility-upgrading-from-september-stable-keeps-shared-da|September database compatibility]] · Collaboration
- [[Changes/OpenClaw/2026-10-08-24-other-changes-in-v2026-9-9|24 other changes in v2026.9.9]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-10-08 · Lovable · [[Changes/Lovable/2026-10-08-publish-to-invited-people-only-on-free-and-pro-plans|Publish to invited people only on Free and Pro plans]]
- Later: 2026-10-08 · OpenHands · [[Changes/OpenHands/2026-10-08-feat-onboarding-show-the-super-admin-setup-guide-on-enterprise-backends-by-hiept|feat(onboarding): show the Super Admin setup guide on enterprise backends]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-01-14 · Notion · [[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export members as CSV (for Enterprise Plans) Quickly download a list of the people…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-08-54423f&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-08-2-enterprise-and-administration-changes-in-v2026-9-9.md%0ACard%20ID%3A%20openclaw-2026-10-08-54423f%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->