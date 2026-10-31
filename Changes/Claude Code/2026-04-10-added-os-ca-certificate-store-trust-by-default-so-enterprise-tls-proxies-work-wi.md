---
card_id: claude-code-2026-04-10-efc05f
date: '2026-04-10'
description: 'Claude Code · 2026-04-10 · Enterprise and Administration: Added OS CA
  certificate store trust by default, so enterprise TLS proxies work without extra
  setup…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2024-03-20-admin-improvements-team-admins-can-now-mark-themselves-as-unpaid-users-and-can-s|Admin
    improvements: Team admins can now mark themselves as unpaid users and can see…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 751
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: ec14e7f9597df65db88fd212827e3bf0a5d56cd8637c3e8ca7af53e10b853cae
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-10-efc05f
  comparison: ''
  date: '2026-04-10'
  description: 'Claude Code — v2.1.101: Added OS CA certificate store trust by default,
    so enterprise TLS proxies work without extra setup (set `CLAUDE_CODE_CERT_STORE=bundled`
    to use only bundled CAs)'
  evidence:
  - quote: Added OS CA certificate store trust by default, so enterprise TLS proxies
      work without extra setup (set `CLAUDE_CODE_CERT_STORE=bundled` to use only bundled
      CAs)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.101
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-os-ca-certificate-store-trust-by-default-so-enterprise-tls-proxies-work-wi
  source_release: claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642
  source_type: github_releases
  theme: enterprise-admin
  title: Added OS CA certificate store trust by default, so enterprise TLS proxies
    work…
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-02-added-an-enterprise-admin-control-for-disabling-made-with-cursor-code-attributio|Added
  an Enterprise Admin control for disabling "Made with Cursor" code attribution…]]'
- '[[Changes/Claude Code/2026-04-04-added-forceremotesettingsrefresh-policy-setting-when-set-the-cli-blocks-startup|Added
  forceRemoteSettingsRefresh policy setting]]'
- '[[Changes/Claude Code/2026-04-07-changed-default-effort-level-from-medium-to-high-for-api-key-bedrock-vertex-foun|Changed
  default effort level from medium to high for API-key…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642|claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642]]'
source_type: github_releases
theme: enterprise-admin
title: Added OS CA certificate store trust by default, so enterprise TLS proxies work…
type: change
---

<!-- chronolog:begin region="header" -->
# Added OS CA certificate store trust by default, so enterprise TLS proxies work…

**Claude Code** · 2026-04-10 · [[Themes/enterprise-admin|Enterprise and Administration]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.101) · from [[Releases/Claude Code/claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642|v2.1.101]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added OS CA certificate store trust by default, so enterprise TLS proxies work without extra setup (set `CLAUDE_CODE_CERT_STORE=bundled` to use only bundled CAs)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.101
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-10-improved-focus-mode-claude-now-writes-more-self-contained-summaries-since-it-kno|Improved focus mode]] · Interface Experience
- [[Changes/Claude Code/2026-04-10-fixed-a-command-injection-vulnerability-in-the-posix-which-fallback-used-by-lsp|Fixed a command injection vulnerability in the POSIX which fallback used by LSP…]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-10-improved-tool-not-available-errors-to-explain-why-and-how-to-proceed-when-the-mo|Improved tool-not-available errors to explain why and how to proceed when the model…]] · Context Window
- [[Changes/Claude Code/2026-04-10-added-team-onboarding-command-to-generate-a-teammate-ramp-up-guide-from-your-loc|Added /team-onboarding command to generate a teammate ramp-up guide…]] · Collaboration
- [[Changes/Claude Code/2026-04-10-ultraplan-and-other-remote-session-features-now-auto-create-a-default-cloud-envi|/ultraplan and other remote-session features now auto-create a default cloud…]] · Agent Mode
- [[Changes/Claude Code/2026-04-10-improved-brief-mode-to-retry-once-when-claude-responds-with-plain-text-instead-o|Improved brief mode to retry once when Claude responds with plain text instead…]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-10-4-apps-and-integrations-changes-in-v2-1-101|4 Apps and Integrations changes in v2.1.101]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-10-5-other-changes-in-v2-1-101|5 other changes in v2.1.101]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-04-07 · Claude Code · [[Changes/Claude Code/2026-04-07-changed-default-effort-level-from-medium-to-high-for-api-key-bedrock-vertex-foun|Changed default effort level from medium to high for API-key…]]
- Later: 2026-04-16 · ChatGPT · [[Changes/ChatGPT/2026-04-16-we-re-beginning-to-roll-out-ads-for-users-on-free-and-go-plans-in-australia-new|Rolling out ads in Australia, New Zealand, and Canada]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-03-20 · Cursor · [[Changes/Cursor/2024-03-20-admin-improvements-team-admins-can-now-mark-themselves-as-unpaid-users-and-can-s|Admin improvements: Team admins can now mark themselves as unpaid users and can see…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-10-efc05f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-10-added-os-ca-certificate-store-trust-by-default-so-enterprise-tls-proxies-work-wi.md%0ACard%20ID%3A%20claude-code-2026-04-10-efc05f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.101%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->