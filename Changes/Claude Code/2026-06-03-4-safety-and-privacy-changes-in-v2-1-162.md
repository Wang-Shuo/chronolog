---
card_id: claude-code-2026-06-03-f896ae
date: '2026-06-03'
description: 'Claude Code · 2026-06-03 · Safety and Privacy: 4 changes in v2.1.162
  — `claude agents --json` now includes `waitingFor` showing what a waiting session
  is…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1144
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e97ab09a549abb302acdfb195543b14d5ad3db87b40e4e1cdb8acae2b4327e01
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-03-f896ae
  comparison: ''
  date: '2026-06-03'
  description: 'Claude Code — v2.1.162: 4 Safety and Privacy changes'
  evidence:
  - quote: '`claude agents --json` now includes `waitingFor` showing what a waiting
      session is blocked on (e.g. permission prompt)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.162
  - quote: Fixed WebFetch permission rules not being applied to built-in preapproved
      domains; explicit `WebFetch(domain:...)` deny/ask/allow rules now take precedence
      over the preapproved-host auto-allow
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.162
  - quote: Fixed Windows permission rules never matching when spelled with backslashes
      (`~\`, `\\server\share`) or case-variant paths, and Read deny rules not hiding
      files from Glob/Grep results
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.162
  - quote: Improved background service startup and `claude update` verification to
      wait out endpoint-security scanning of new binaries instead of failing after
      5 seconds
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.162
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-safety-and-privacy-changes-in-v2-1-162
  source_release: claude-code-2026-06-03-v2-1-162-github-333906405-cdc7c67c
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v2.1.162
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-28-2-safety-and-privacy-changes-in-v2-1-153|2 Safety
  and Privacy changes in v2.1.153]]'
- '[[Changes/Claude Code/2026-05-29-2-safety-and-privacy-changes-in-v2-1-157|2 Safety
  and Privacy changes in v2.1.157]]'
- '[[Changes/ChatGPT/2026-06-02-we-re-rolling-out-active-sessions-a-new-security-feature-in-chatgpt-that-helps-u-51e977|ChatGPT
  rolls out Active sessions, a new security feature that helps users review…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-03-v2-1-162-github-333906405-cdc7c67c|claude-code-2026-06-03-v2-1-162-github-333906405-cdc7c67c]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v2.1.162
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v2.1.162

**Claude Code** · 2026-06-03 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.162) · from [[Releases/Claude Code/claude-code-2026-06-03-v2-1-162-github-333906405-cdc7c67c|v2.1.162]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `claude agents --json` now includes `waitingFor` showing what a waiting session is blocked on (e.g. permission prompt)

> Fixed WebFetch permission rules not being applied to built-in preapproved domains; explicit `WebFetch(domain:...)` deny/ask/allow rules now take precedence over the preapproved-host auto-allow

> Fixed Windows permission rules never matching when spelled with backslashes (`~\`, `\\server\share`) or case-variant paths, and Read deny rules not hiding files from Glob/Grep results

> Improved background service startup and `claude update` verification to wait out endpoint-security scanning of new binaries instead of failing after 5 seconds

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.162
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-03-2-interface-experience-changes-in-v2-1-162|2 Interface Experience changes in v2.1.162]] · Interface Experience
- [[Changes/Claude Code/2026-06-03-tools-explicitly-listing-grep-glob-now-provides-the-dedicated-search-tools-on-na|--tools: explicitly listing Grep/Glob now provides the dedicated search tools…]] · Developer Workflow
- [[Changes/Claude Code/2026-06-03-quieter-startup-notices-group-by-severity-and-session-info-and-announcements-sha|Quieter startup: notices group by severity, and session info and announcements share…]] · Collaboration
- [[Changes/Claude Code/2026-06-03-renamed-windsurf-to-devin-desktop-in-the-ide-menu-terminal-setup-and-scroll-spee|Renamed Windsurf to Devin Desktop in the /ide menu, /terminal-setup…]] · Editor Experience
- [[Changes/Claude Code/2026-06-03-remote-control-now-shows-as-a-persistent-footer-pill-with-a-link-to-the-session|Remote Control now shows as a persistent footer pill (with a link to the session)…]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-03-effort-now-confirms-when-your-chosen-level-will-persist-as-the-default-for-new-s|/effort now confirms when your chosen level will persist as the default for new sessions]] · Model Support
- [[Changes/Claude Code/2026-06-03-4-other-changes-in-v2-1-162|4 other changes in v2.1.162]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-02 · ChatGPT · [[Changes/ChatGPT/2026-06-02-we-re-rolling-out-active-sessions-a-new-security-feature-in-chatgpt-that-helps-u-51e977|ChatGPT rolls out Active sessions, a new security feature that helps users review…]]
- Later: 2026-06-03 · Cursor · [[Changes/Cursor/2026-06-03-enterprise-customers-can-now-manage-multiple-cursor-teams-from-one-place-with-di|Enterprise customers can now manage multiple Cursor teams from one place…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-03-f896ae&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-03-4-safety-and-privacy-changes-in-v2-1-162.md%0ACard%20ID%3A%20claude-code-2026-06-03-f896ae%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.162%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->