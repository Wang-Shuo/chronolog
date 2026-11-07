---
card_id: open-webui-2026-03-01-801faf
date: '2026-03-01'
description: "Open WebUI · 2026-03-01 · Interface Experience: 4 changes in v0.8.6
  — \U0001F4BE **Faster model and file operations.** Model selection, file preparation,
  and history…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1147
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a98cd9cfae011aa8491137dc45e5a5507351e5db2b5589656d5d531354e31522
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-01-801faf
  comparison: ''
  date: '2026-03-01'
  description: 'Open WebUI — v0.8.6: 4 Interface Experience changes'
  evidence:
  - quote: "\U0001F4BE **Faster model and file operations.** Model selection, file
      preparation, and history saving are now faster. [#22102](https://github.com/open-webui/open-webui/pull/22102)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F514 **Notification HTML escaping.** Notification messages now properly
      escape HTML content, matching the behavior in chat messages and ensuring consistent
      rendering across the interface. [#21860](https://github.com/open-webui/open-webui/issues/21860),
      [Commit](https://github.com/open-webui/open-webui/commit/e83f668107723fa90ba0efa76c340c8338f45431)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F3A8 **Sidebar user menu positioning.** The sidebar user menu no
      longer drifts rightward when the sidebar is resized, keeping the menu properly
      aligned with its trigger. [#21853](https://github.com/open-webui/open-webui/pull/21853)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F550 **Chat timestamp i18n fix.** Chat timestamps in the sidebar
      now display correctly, fixing an issue where the time ago format (e.g., \"5m\",
      \"2h\", \"3d\") was not being localized properly due to incorrect variable casing
      in the translation function. [Commit](https://github.com/open-webui/open-webui/commit/ae28e7d24530eb9f7909b293bcd0f33048a022a9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-interface-experience-changes-in-v0-8-6
  source_release: open-webui-2026-03-01-v0-8-6-github-291846033-263bca05
  source_type: github_releases
  theme: interface-experience
  title: 4 Interface Experience changes in v0.8.6
  type: change
related_changes:
- '[[Changes/Replit/2026-02-27-password-manager-keyboard-navigation|Password manager
  keyboard navigation]]'
- '[[Changes/Replit/2026-02-27-system-theme-support|System theme support]]'
- '[[Changes/Claude Code/2026-02-28-added-always-copy-full-response-option-to-the-copy-picker-when-selected-future-c|Added
  "Always copy full response" option to the /copy picker]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|open-webui-2026-03-01-v0-8-6-github-291846033-263bca05]]'
source_type: github_releases
theme: interface-experience
title: 4 Interface Experience changes in v0.8.6
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Interface Experience changes in v0.8.6

**Open WebUI** · 2026-03-01 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.6) · from [[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|v0.8.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 💾 **Faster model and file operations.** Model selection, file preparation, and history saving are now faster. [#22102](https://github.com/open-webui/open-webui/pull/22102)

> 🔔 **Notification HTML escaping.** Notification messages now properly escape HTML content, matching the behavior in chat messages and ensuring consistent rendering across the interface. [#21860](https://github.com/open-webui/open-webui/issues/21860), [Commit](https://github.com/open-webui/open-webui/commit/e83f668107723fa90ba0efa76c340c8338f45431)

> 🎨 **Sidebar user menu positioning.** The sidebar user menu no longer drifts rightward when the sidebar is resized, keeping the menu properly aligned with its trigger. [#21853](https://github.com/open-webui/open-webui/pull/21853)

> 🕐 **Chat timestamp i18n fix.** Chat timestamps in the sidebar now display correctly, fixing an issue where the time ago format (e.g., "5m", "2h", "3d") was not being localized properly due to incorrect variable casing in the translation function. [Commit](https://github.com/open-webui/open-webui/commit/ae28e7d24530eb9f7909b293bcd0f33048a022a9)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-01-21-reliability-and-performance-changes-in-v0-8-6|21 Reliability and Performance changes in v0.8.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-01-2-search-and-browsing-changes-in-v0-8-6|2 Search and Browsing changes in v0.8.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-01-oauth-session-token-decryption-oauth-sessions-are-now-properly-detached-from-the|🔓 OAuth session token decryption. OAuth sessions are now properly detached…]] · Context Window
- [[Changes/Open WebUI/2026-03-01-individual-user-sharing-control-administrators-can-now-disable-individual-user-s|🔐 Individual user sharing control. Administrators can now disable individual…]] · Collaboration
- [[Changes/Open WebUI/2026-03-01-3-account-and-access-changes-in-v0-8-6|3 Account and Access changes in v0.8.6]] · Account and Access
- [[Changes/Open WebUI/2026-03-01-4-safety-and-privacy-changes-in-v0-8-6|4 Safety and Privacy changes in v0.8.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-01-8-model-support-changes-in-v0-8-6|8 Model Support changes in v0.8.6]] · Model Support
- [[Changes/Open WebUI/2026-03-01-9-developer-workflow-changes-in-v0-8-6|9 Developer Workflow changes in v0.8.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-01-6-other-changes-in-v0-8-6|6 other changes in v0.8.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-02-28 · Claude Code · [[Changes/Claude Code/2026-02-28-added-always-copy-full-response-option-to-the-copy-picker-when-selected-future-c|Added "Always copy full response" option to the /copy picker]]
- Later: 2026-03-02 · ElevenLabs · [[Changes/ElevenLabs/2026-03-02-elevenagents|ElevenAgents]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-01-801faf&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-01-4-interface-experience-changes-in-v0-8-6.md%0ACard%20ID%3A%20open-webui-2026-03-01-801faf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->