---
card_id: openclaw-2026-10-03-4c7bf7
date: '2026-10-03'
description: 'OpenClaw · 2026-10-03 · Pricing Model: 9 changes in v2026.9.8 — Starting
  OpenClaw. Starting directly or in a container now prevents two copies from using
  the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily
    limit: To ensure a high-quality experience for all ChatGPT users, we…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1388
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bf01f65067fc3158faef77b2815f819c322875f3a4766f138adea96709619fb1
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-03-4c7bf7
  comparison: ''
  date: '2026-10-03'
  description: 'OpenClaw — v2026.9.8: 9 Pricing Model changes'
  evidence:
  - quote: Starting OpenClaw. Starting directly or in a container now prevents two
      copies from using the same saved data at once. Windows startup also avoids getting
      stuck when a cache folder's path is too long. Sources and credits .
    source_release: https://docs.openclaw.ai/releases/2026.9.8
  - quote: Database maintenance. Maintenance retries when another operation briefly
      has the database busy. Update rehearsals avoid unnecessary database copies and
      keep each record's ID unchanged. Update recovery sources and credits , platform
      update sources and credits .
    source_release: https://docs.openclaw.ai/releases/2026.9.8
  - quote: Telegram cleanup. Doctor can move confirmed-empty files left over from
      old Telegram connections into an archive. It leaves nonempty or uncertain files
      for review and keeps the originals if the move fails. Sources and credits .
    source_release: https://docs.openclaw.ai/releases/2026.9.8
  - quote: Telegram previews. Fixed late edits to a Telegram reply preview from a
      task that had already been replaced. Sources and credits .
    source_release: https://docs.openclaw.ai/releases/2026.9.8
  - quote: Refreshing skills. On Unix-based systems, skills copied from a read-only
      installation can now be refreshed in sandboxed workspaces and Claude CLI sessions.
      The copied folders no longer block the refresh because they inherited the original's
      restrictions. Sources and credits .
    source_release: https://docs.openclaw.ai/releases/2026.9.8
  - quote: Codex memory use. Running many native Codex agents uses less duplicate
      memory. OpenClaw waits until an agent's conversation list is needed before starting
      the background process for that list, and shares settings where compatible.
      Memory used to track saved shell environments is also limited. Update recovery
      sources and credits , platform update sources and credits .
    source_release: https://docs.openclaw.ai/releases/2026.9.8
  - quote: Local connection checks. HTTPS checks that OpenClaw is running locally
      now follow the managed proxy settings and verify that the server's certificate
      matches the one you configured on every connection. Sources and credits .
    source_release: https://docs.openclaw.ai/releases/2026.9.8
  - quote: Secrets in logs. Fixed a case where secrets in long, unusually formatted
      log entries were not hidden when OpenClaw ran on Bun. Sources and credits .
    source_release: https://docs.openclaw.ai/releases/2026.9.8
  - quote: Repairing conversation history. Repair no longer crashes when it follows
      a long chain of linked conversations. It preserves the history and keeps each
      transcript attached to the right session. Sources and credits .
    source_release: https://docs.openclaw.ai/releases/2026.9.8
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 9-pricing-model-changes-in-v2026-9-8
  source_release: openclaw-2026-10-03-v2026-9-8-0844d8d3
  source_type: openclaw_changelog
  theme: pricing-model
  title: 9 Pricing Model changes in v2026.9.8
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-30-3-pricing-model-changes-in-v2026-9-7|3 Pricing Model
  changes in v2026.9.7]]'
- '[[Changes/Codex CLI/2026-10-01-49079-update-and-centralize-tui-subscription-labels-etraut-openai|♯49079
  Update and centralize TUI subscription labels @etraut-openai]]'
- '[[Changes/Claude Code/2026-10-02-improved-the-usage-credits-message-shown-to-team-and-enterprise-members-whose-or|Improved
  the /usage-credits message shown to Team and Enterprise members whose…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-03-v2026-9-8-0844d8d3|openclaw-2026-10-03-v2026-9-8-0844d8d3]]'
source_type: openclaw_changelog
theme: pricing-model
title: 9 Pricing Model changes in v2026.9.8
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Pricing Model changes in v2026.9.8

**OpenClaw** · 2026-10-03 · [[Themes/pricing-model|Pricing Model]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.8) · from [[Releases/OpenClaw/openclaw-2026-10-03-v2026-9-8-0844d8d3|v2026.9.8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Starting OpenClaw. Starting directly or in a container now prevents two copies from using the same saved data at once. Windows startup also avoids getting stuck when a cache folder's path is too long. Sources and credits .

> Database maintenance. Maintenance retries when another operation briefly has the database busy. Update rehearsals avoid unnecessary database copies and keep each record's ID unchanged. Update recovery sources and credits , platform update sources and credits .

> Telegram cleanup. Doctor can move confirmed-empty files left over from old Telegram connections into an archive. It leaves nonempty or uncertain files for review and keeps the originals if the move fails. Sources and credits .

> Telegram previews. Fixed late edits to a Telegram reply preview from a task that had already been replaced. Sources and credits .

> Refreshing skills. On Unix-based systems, skills copied from a read-only installation can now be refreshed in sandboxed workspaces and Claude CLI sessions. The copied folders no longer block the refresh because they inherited the original's restrictions. Sources and credits .

> Codex memory use. Running many native Codex agents uses less duplicate memory. OpenClaw waits until an agent's conversation list is needed before starting the background process for that list, and shares settings where compatible. Memory used to track saved shell environments is also limited. Update recovery sources and credits , platform update sources and credits .

> Local connection checks. HTTPS checks that OpenClaw is running locally now follow the managed proxy settings and verify that the server's certificate matches the one you configured on every connection. Sources and credits .

> Secrets in logs. Fixed a case where secrets in long, unusually formatted log entries were not hidden when OpenClaw ran on Bun. Sources and credits .

> Repairing conversation history. Repair no longer crashes when it follows a long chain of linked conversations. It preserves the history and keeps each transcript attached to the right session. Sources and credits .

Source: https://docs.openclaw.ai/releases/2026.9.8
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-03-2-mobile-and-desktop-changes-in-v2026-9-8|2 Mobile and Desktop changes in v2026.9.8]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-03-2-model-support-changes-in-v2026-9-8|2 Model Support changes in v2026.9.8]] · Model Support
- [[Changes/OpenClaw/2026-10-03-4-agent-mode-changes-in-v2026-9-8|4 Agent Mode changes in v2026.9.8]] · Agent Mode
- [[Changes/OpenClaw/2026-10-03-session-assignment-moving-the-pointer-over-assign-to-and-then-pressing-enter-now|Session assignment]] · Interface Experience
- [[Changes/OpenClaw/2026-10-03-2-memory-and-personalization-changes-in-v2026-9-8|2 Memory and Personalization changes in v2026.9.8]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-03-2-account-and-access-changes-in-v2026-9-8|2 Account and Access changes in v2026.9.8]] · Account and Access
- [[Changes/OpenClaw/2026-10-03-browser-tabs-after-updates-if-you-leave-openclaw-s-bundled-web-interface-open-du|Browser tabs after updates]] · Editor Experience
- [[Changes/OpenClaw/2026-10-03-3-other-changes-in-v2026-9-8|3 other changes in v2026.9.8]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-10-02 · Claude Code · [[Changes/Claude Code/2026-10-02-improved-the-usage-credits-message-shown-to-team-and-enterprise-members-whose-or|Improved the /usage-credits message shown to Team and Enterprise members whose…]]
- Later: 2026-10-05 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-05-plan-usage-reflects-the-current-billing-period-after-quota-resets|Plan usage reflects the current billing period after quota resets]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily limit: To ensure a high-quality experience for all ChatGPT users, we…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-03-4c7bf7&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-03-9-pricing-model-changes-in-v2026-9-8.md%0ACard%20ID%3A%20openclaw-2026-10-03-4c7bf7%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.8%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->