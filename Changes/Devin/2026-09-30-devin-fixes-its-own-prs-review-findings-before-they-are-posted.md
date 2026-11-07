---
card_id: devin-2026-09-30-dd9be9
date: '2026-09-30'
description: 'Devin · 2026-09-30 · Developer Workflow: When Devin Review reviews a
  pull request that a running Devin session opened, the findings are no longer posted
  as…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2941
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 8ff32716651389fa3557dec101456d89d385fc54dd69ad7dd83e1ce2604332e2
product: devin
product_name: Devin
record:
  card_id: devin-2026-09-30-dd9be9
  comparison: ''
  date: '2026-09-30'
  description: 'Devin — Devin updates — 2026-09-30: When Devin Review reviews a pull
    request that a running Devin session opened, the findings are no longer posted
    as review comments right away. They go to that session first: with Auto-fix on
    Devin fixes what it can, with Auto-fix off it only reports back. While this happens
    the PR shows a "Devin is addressing Devin Review findings" status. Once Devin
    is done, only the findings it could not fix are posted as review comments, and
    the status lists what was fixed; the Devin Review badge and "No Issues Found"
    summary still appear as before, and code-quality findings stay on the Devin Review
    page. PRs that no running session owns are reviewed exactly as today.'
  evidence:
  - quote: 'When Devin Review reviews a pull request that a running Devin session
      opened, the findings are no longer posted as review comments right away. They
      go to that session first: with Auto-fix on Devin fixes what it can, with Auto-fix
      off it only reports back. While this happens the PR shows a "Devin is addressing
      Devin Review findings" status. Once Devin is done, only the findings it could
      not fix are posted as review comments, and the status lists what was fixed;
      the Devin Review badge and "No Issues Found" summary still appear as before,
      and code-quality findings stay on the Devin Review page. PRs that no running
      session owns are reviewed exactly as today.'
    source_release: https://docs.devin.ai/release-notes/2026
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: devin
  product_name: Devin
  slug: devin-fixes-its-own-prs-review-findings-before-they-are-posted
  source_release: devin-2026-09-30-2026-09-30-863545c9
  source_type: devin_changelog
  theme: developer-workflow
  title: Devin Fixes Its Own PRs' Review Findings Before They Are Posted
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-29-5-developer-workflow-changes-in-rust-v0-159-0|5
  Developer Workflow changes in rust-v0.159.0]]'
- '[[Changes/Claude Code/2026-09-30-3-developer-workflow-changes-in-v2-1-286|3 Developer
  Workflow changes in v2.1.286]]'
- '[[Changes/Devin/2026-09-30-read-only-live-shell-preview|Read-Only Live Shell Preview]]'
source_release: '[[Releases/Devin/devin-2026-09-30-2026-09-30-863545c9|devin-2026-09-30-2026-09-30-863545c9]]'
source_type: devin_changelog
theme: developer-workflow
title: Devin Fixes Its Own PRs' Review Findings Before They Are Posted
type: change
---

<!-- chronolog:begin region="header" -->
# Devin Fixes Its Own PRs' Review Findings Before They Are Posted

**Devin** · 2026-09-30 · [[Themes/developer-workflow|Developer Workflow]] · Launch · [Official source](https://docs.devin.ai/release-notes/2026) · from [[Releases/Devin/devin-2026-09-30-2026-09-30-863545c9|Devin updates — 2026-09-30]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> When Devin Review reviews a pull request that a running Devin session opened, the findings are no longer posted as review comments right away. They go to that session first: with Auto-fix on Devin fixes what it can, with Auto-fix off it only reports back. While this happens the PR shows a "Devin is addressing Devin Review findings" status. Once Devin is done, only the findings it could not fix are posted as review comments, and the status lists what was fixed; the Devin Review badge and "No Issues Found" summary still appear as before, and code-quality findings stay on the Devin Review page. PRs that no running session owns are reviewed exactly as today.
>
> Source: https://docs.devin.ai/release-notes/2026
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Devin/2026-09-30-session-menu-polish|Session Menu Polish]] · Interface Experience
- [[Changes/Devin/2026-09-30-ask-devin-recognizes-commented-out-code|Ask Devin Recognizes Commented-Out Code]] · Search and Browsing
- [[Changes/Devin/2026-09-30-oncall-lists-and-settings|Oncall Lists and Settings]] · Context Window
- [[Changes/Devin/2026-09-30-read-only-live-shell-preview|Read-Only Live Shell Preview]] · Developer Workflow
- [[Changes/Devin/2026-09-30-skills-only-repositories-install-as-plugins|Skills-Only Repositories Install as Plugins]] · Apps and Integrations
- [[Changes/Devin/2026-09-30-microsoft-teams-sync-from-the-session-menu-and-clearer-setup-messaging|Microsoft Teams: Sync from the Session Menu and Clearer Setup Messaging]] · Interface Experience
- [[Changes/Devin/2026-09-30-github-team-sync-managed-repository-access|GitHub Team Sync: Managed Repository Access]] · Collaboration
- [[Changes/Devin/2026-09-30-preflight-checks-for-automations|Preflight Checks for Automations]] · Automation and Scheduling
- [[Changes/Devin/2026-09-30-environments-and-analytics|Environments and Analytics]] · Enterprise and Administration
- [[Changes/Devin/2026-09-30-context-tab|Context Tab]] · Memory and Personalization
- [[Changes/Devin/2026-09-30-messages-are-no-longer-lost-when-the-connection-drops|Messages Are No Longer Lost When the Connection Drops]] · Editor Experience
- [[Changes/Devin/2026-09-30-slack-buttons-work-across-organizations|Slack: Buttons Work Across Organizations]] · Apps and Integrations
- [[Changes/Devin/2026-09-30-hardware-accelerated-emulators-in-sessions|Hardware-Accelerated Emulators in Sessions]] · Safety and Privacy
- [[Changes/Devin/2026-09-30-voice-call-bar-follows-the-composer|Voice Call Bar Follows the Composer]] · Voice and Audio
- [[Changes/Devin/2026-09-30-devin-as-a-native-jira-agent|Devin as a Native Jira Agent]] · Agent Mode
- [[Changes/Devin/2026-09-30-session-preview-cards-in-the-sidebar|Session Preview Cards in the Sidebar]] · Interface Experience
- [[Changes/Devin/2026-09-30-devin-mono-for-code-and-terminals|Devin Mono for Code and Terminals]] · Editor Experience
- [[Changes/Devin/2026-09-30-reliability-and-navigation-fixes|Reliability and Navigation Fixes]] · Interface Experience
- [[Changes/Devin/2026-09-30-sidebar-and-command-palette|Sidebar and Command Palette]] · Interface Experience
- [[Changes/Devin/2026-09-30-outposts|Outposts]] · Enterprise and Administration
- [[Changes/Devin/2026-09-30-findings-that-devin-marks-as-resolved-keep-showing-the-original-finding-with-dev|Findings that Devin marks as resolved keep showing the original finding…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-30 · Claude Code · [[Changes/Claude Code/2026-09-30-3-developer-workflow-changes-in-v2-1-286|3 Developer Workflow changes in v2.1.286]]
- Later: 2026-09-30 · Google Antigravity · [[Changes/Google Antigravity/2026-09-30-pressing-cmd-a-or-ctrl-a-now-selects-only-the-content-pane-or-terminal-you-are-f|Pressing Cmd+A or Ctrl+A now selects only the content pane or terminal you…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20devin-2026-09-30-dd9be9&body=Card%3A%20Changes%2FDevin%2F2026-09-30-devin-fixes-its-own-prs-review-findings-before-they-are-posted.md%0ACard%20ID%3A%20devin-2026-09-30-dd9be9%0ASource%3A%20https%3A%2F%2Fdocs.devin.ai%2Frelease-notes%2F2026%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->