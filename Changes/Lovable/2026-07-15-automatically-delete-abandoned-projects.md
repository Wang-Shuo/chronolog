---
card_id: lovable-2026-07-15-42cd9a
date: '2026-07-15'
description: 'Lovable · 2026-07-15 · Safety and Privacy: Enterprise workspaces can
  now [clean up abandoned projects…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1186
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: d7638f56b186f3c88f013415288cd7ce1f9d4a7699ef47013c1d5723928429ba
product: lovable
product_name: Lovable
record:
  card_id: lovable-2026-07-15-42cd9a
  comparison: ''
  date: '2026-07-15'
  description: 'Lovable — Lovable updates — 2026-07-15: Enterprise workspaces can
    now [clean up abandoned projects automatically](https://docs.lovable.dev/features/privacy-and-security-settings.md#abandoned-projects),
    published and unpublished alike. Workspace admins and owners configure it under
    **Settings → Security → Privacy & security → Abandoned projects**: choose when
    a project counts as abandoned and how long after that it is deleted. Auto-delete
    is off by default. A project stays active while someone works on it in the editor,
    visitors use the published app, or its backend functions run; just opening or
    previewing it does not count.'
  evidence:
  - quote: 'Enterprise workspaces can now [clean up abandoned projects automatically](https://docs.lovable.dev/features/privacy-and-security-settings.md#abandoned-projects),
      published and unpublished alike. Workspace admins and owners configure it under
      **Settings → Security → Privacy & security → Abandoned projects**: choose when
      a project counts as abandoned and how long after that it is deleted. Auto-delete
      is off by default. A project stays active while someone works on it in the editor,
      visitors use the published app, or its backend functions run; just opening or
      previewing it does not count.'
    source_release: https://docs.lovable.dev/changelog
  - quote: Before a project is deleted, its owner and members with edit access receive
      warning emails and see an in-project banner 5 days and 1 day ahead. Editing
      the project, sending it a message, or selecting **Keep it** cancels the deletion.
      Lovable keeps a deleted project for 60 days, and support can bring it back within
      that window.
    source_release: https://docs.lovable.dev/changelog
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: lovable
  product_name: Lovable
  slug: automatically-delete-abandoned-projects
  source_release: lovable-2026-07-15-2026-07-15-41bc4811
  source_type: lovable_changelog
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - admins
    - enterprise
    score: 100
    theme: enterprise-admin
  - matched_terms:
    - privacy
    - security
    score: 100
    theme: safety-privacy
  - matched_terms:
    - editor
    score: 50
    theme: editor-experience
  theme_resolution: manual-semantic-rule-v2
  title: Automatically delete abandoned projects
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-14-fixed-multi-second-per-turn-slowdowns-in-sessions-with-many-permission-deny-ask|Fixed
  multi-second per-turn slowdowns in sessions with many permission deny/ask rules]]'
- '[[Changes/OpenCode/2026-07-14-desktop-kept-permission-auto-accept-state-separate-for-each-server|Desktop
  Kept permission auto-accept state separate for each server]]'
- '[[Changes/Claude Code/2026-07-15-2-safety-and-privacy-changes-in-v2-1-211|2 Safety
  and Privacy changes in v2.1.211]]'
source_release: '[[Releases/Lovable/lovable-2026-07-15-2026-07-15-41bc4811|lovable-2026-07-15-2026-07-15-41bc4811]]'
source_type: lovable_changelog
theme: safety-privacy
title: Automatically delete abandoned projects
type: change
---

<!-- chronolog:begin region="header" -->
# Automatically delete abandoned projects

**Lovable** · 2026-07-15 · [[Themes/safety-privacy|Safety and Privacy]] · Launch · [Official source](https://docs.lovable.dev/changelog) · from [[Releases/Lovable/lovable-2026-07-15-2026-07-15-41bc4811|Lovable updates — 2026-07-15]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Enterprise workspaces can now [clean up abandoned projects automatically](https://docs.lovable.dev/features/privacy-and-security-settings.md#abandoned-projects), published and unpublished alike. Workspace admins and owners configure it under **Settings → Security → Privacy & security → Abandoned projects**: choose when a project counts as abandoned and how long after that it is deleted. Auto-delete is off by default. A project stays active while someone works on it in the editor, visitors use the published app, or its backend functions run; just opening or previewing it does not count.
>
> Before a project is deleted, its owner and members with edit access receive warning emails and see an in-project banner 5 days and 1 day ahead. Editing the project, sending it a message, or selecting **Keep it** cancels the deletion. Lovable keeps a deleted project for 60 days, and support can bring it back within that window.
>
> Source: https://docs.lovable.dev/changelog
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Lovable/2026-07-15-gpt-5-6-and-gemini-text-to-speech-models-for-your-app-s-ai-features|GPT-5.6 and Gemini text-to-speech models for your app's AI features]] · Model Support
- [[Changes/Lovable/2026-07-15-let-ai-assistants-use-your-published-app|Let AI assistants use your published app]] · Agent Mode
- [[Changes/Lovable/2026-07-15-email-alerts-for-sign-ins-from-a-new-device-and-country|Email alerts for sign-ins from a new device and country]] · Account and Access
- [[Changes/Lovable/2026-07-15-password-reset-is-unavailable-for-accounts-without-a-password|Password reset is unavailable for accounts without a password]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-15 · Claude Code · [[Changes/Claude Code/2026-07-15-2-safety-and-privacy-changes-in-v2-1-211|2 Safety and Privacy changes in v2.1.211]]
- Later: 2026-07-16 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-16-2-safety-and-privacy-changes-in-v1-0-71|2 Safety and Privacy changes in v1.0.71]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20lovable-2026-07-15-42cd9a&body=Card%3A%20Changes%2FLovable%2F2026-07-15-automatically-delete-abandoned-projects.md%0ACard%20ID%3A%20lovable-2026-07-15-42cd9a%0ASource%3A%20https%3A%2F%2Fdocs.lovable.dev%2Fchangelog%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->