---
card_id: claude-code-2026-04-10-b7d6fe
date: '2026-04-10'
description: 'Claude Code · 2026-04-10 · Apps and Integrations: 4 changes in v2.1.101
  — Improved settings resilience: an unrecognized hook event name in `settings.json`
  no…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1114
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7873712fe3b4edd1f2a86227b942c7b5a044e1896eddc74ee64fc309e5367467
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-10-b7d6fe
  comparison: ''
  date: '2026-04-10'
  description: 'Claude Code — v2.1.101: 4 Apps and Integrations changes'
  evidence:
  - quote: 'Improved settings resilience: an unrecognized hook event name in `settings.json`
      no longer causes the entire file to be ignored'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.101
  - quote: Improved plugin hooks from plugins force-enabled by managed settings to
      run when `allowManagedHooksOnly` is set
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.101
  - quote: Improved `/plugin` and `claude plugin update` to show a warning when the
      marketplace could not be refreshed, instead of silently reporting a stale version
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.101
  - quote: Improved SDK `query()` to clean up subprocess and temp files when consumers
      `break` from `for await` or use `await using`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.101
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-apps-and-integrations-changes-in-v2-1-101
  source_release: claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v2.1.101
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-08-give-bugbot-access-to-mcp-servers-for-additional-context-during-code-reviews-on|Bugbot
  MCP Support]]'
- '[[Changes/Cursor/2026-04-08-this-release-introduces-updates-to-bugbot-including-the-ability-to-self-improve|Cursor
  introduces updates to Bugbot including the ability to self-improve in real…]]'
- '[[Changes/Claude Code/2026-04-09-2-apps-and-integrations-changes-in-v2-1-98|2 Apps
  and Integrations changes in v2.1.98]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642|claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v2.1.101
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v2.1.101

**Claude Code** · 2026-04-10 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.101) · from [[Releases/Claude Code/claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642|v2.1.101]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved settings resilience: an unrecognized hook event name in `settings.json` no longer causes the entire file to be ignored

> Improved plugin hooks from plugins force-enabled by managed settings to run when `allowManagedHooksOnly` is set

> Improved `/plugin` and `claude plugin update` to show a warning when the marketplace could not be refreshed, instead of silently reporting a stale version

> Improved SDK `query()` to clean up subprocess and temp files when consumers `break` from `for await` or use `await using`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.101
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-10-improved-focus-mode-claude-now-writes-more-self-contained-summaries-since-it-kno|Improved focus mode]] · Interface Experience
- [[Changes/Claude Code/2026-04-10-fixed-a-command-injection-vulnerability-in-the-posix-which-fallback-used-by-lsp|Fixed a command injection vulnerability in the POSIX which fallback used by LSP…]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-10-improved-tool-not-available-errors-to-explain-why-and-how-to-proceed-when-the-mo|Improved tool-not-available errors to explain why and how to proceed when the model…]] · Context Window
- [[Changes/Claude Code/2026-04-10-added-team-onboarding-command-to-generate-a-teammate-ramp-up-guide-from-your-loc|Added /team-onboarding command to generate a teammate ramp-up guide…]] · Collaboration
- [[Changes/Claude Code/2026-04-10-ultraplan-and-other-remote-session-features-now-auto-create-a-default-cloud-envi|/ultraplan and other remote-session features now auto-create a default cloud…]] · Agent Mode
- [[Changes/Claude Code/2026-04-10-improved-brief-mode-to-retry-once-when-claude-responds-with-plain-text-instead-o|Improved brief mode to retry once when Claude responds with plain text instead…]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-10-added-os-ca-certificate-store-trust-by-default-so-enterprise-tls-proxies-work-wi|Added OS CA certificate store trust by default, so enterprise TLS proxies work…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-04-10-5-other-changes-in-v2-1-101|5 other changes in v2.1.101]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-09 · Claude Code · [[Changes/Claude Code/2026-04-09-2-apps-and-integrations-changes-in-v2-1-98|2 Apps and Integrations changes in v2.1.98]]
- Later: 2026-04-13 · Claude Code · [[Changes/Claude Code/2026-04-13-3-apps-and-integrations-changes-in-v2-1-105|3 Apps and Integrations changes in v2.1.105]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-10-b7d6fe&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-10-4-apps-and-integrations-changes-in-v2-1-101.md%0ACard%20ID%3A%20claude-code-2026-04-10-b7d6fe%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.101%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->