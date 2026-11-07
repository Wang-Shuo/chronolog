---
card_id: claude-code-2026-04-10-b7d6fe
date: '2026-04-10'
description: 'Claude Code · 2026-04-10 · Apps and Integrations: 4 changes in v2.1.101
  — Improved settings resilience: an unrecognized hook event name in `settings.json`
  no…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2674
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 54daaaacd8f763f3ee916b31187db175d1641eb479f1a3ebd9572019a71b4d8b
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
- '[[Changes/Claude Code/2026-04-09-2-apps-and-integrations-changes-in-v2-1-98|2 Apps
  and Integrations changes in v2.1.98]]'
- '[[Changes/GitHub Copilot CLI/2026-04-09-7-apps-and-integrations-changes-in-v1-0-22|7
  Apps and Integrations changes in v1.0.22]]'
- '[[Changes/OpenCode/2026-04-09-sdk-fix-the-generated-sdk-and-openapi-types-for-providers-and-session-shell-resp|SDK
  Fix the generated SDK and OpenAPI types for /providers and session shell responses]]'
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

- Earlier: 2026-04-09 · OpenCode · [[Changes/OpenCode/2026-04-09-sdk-fix-the-generated-sdk-and-openapi-types-for-providers-and-session-shell-resp|SDK Fix the generated SDK and OpenAPI types for /providers and session shell responses]]
- Later: 2026-04-10 · Codex CLI · [[Changes/Codex CLI/2026-04-10-19-apps-and-integrations-changes-in-rust-v0-119-0|19 Apps and Integrations changes in rust-v0.119.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-10-b7d6fe&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-10-4-apps-and-integrations-changes-in-v2-1-101.md%0ACard%20ID%3A%20claude-code-2026-04-10-b7d6fe%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.101%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->