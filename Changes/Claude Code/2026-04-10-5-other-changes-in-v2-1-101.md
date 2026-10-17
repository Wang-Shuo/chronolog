---
card_id: claude-code-2026-04-10-f193cf
date: '2026-04-10'
description: 'Claude Code · 2026-04-10 · Other changes: 5 changes in v2.1.101 — Improved
  rate-limit retry messages to show which limit was hit and when it resets instead
  of…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 35ee754f73aa08f2d0fbc79c28259a408c66ba1735146fc9b4c909f757501613
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-10-f193cf
  comparison: ''
  date: '2026-04-10'
  description: 'Claude Code — v2.1.101: 5 other changes'
  evidence:
  - quote: Improved rate-limit retry messages to show which limit was hit and when
      it resets instead of an opaque seconds countdown
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.101
  - quote: Improved refusal error messages to include the API-provided explanation
      when available
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.101
  - quote: Improved `claude -p --resume <name>` to accept session titles set via `/rename`
      or `--name`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.101
  - quote: Improved plan mode to hide the "Refine with Ultraplan" option when the
      user's org or auth setup can't reach Claude Code on the web
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.101
  - quote: Improved beta tracing to honor `OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_TOOL_DETAILS`,
      and `OTEL_LOG_TOOL_CONTENT`; sensitive span attributes are no longer emitted
      unless opted in
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.101
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-other-changes-in-v2-1-101
  source_release: claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642
  source_type: github_releases
  theme: uncategorized
  title: 5 other changes in v2.1.101
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642|claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642]]'
source_type: github_releases
theme: uncategorized
title: 5 other changes in v2.1.101
type: change
---

<!-- chronolog:begin region="header" -->
# 5 other changes in v2.1.101

**Claude Code** · 2026-04-10 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.101) · from [[Releases/Claude Code/claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642|v2.1.101]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved rate-limit retry messages to show which limit was hit and when it resets instead of an opaque seconds countdown

> Improved refusal error messages to include the API-provided explanation when available

> Improved `claude -p --resume <name>` to accept session titles set via `/rename` or `--name`

> Improved plan mode to hide the "Refine with Ultraplan" option when the user's org or auth setup can't reach Claude Code on the web

> Improved beta tracing to honor `OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_TOOL_DETAILS`, and `OTEL_LOG_TOOL_CONTENT`; sensitive span attributes are no longer emitted unless opted in

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
- [[Changes/Claude Code/2026-04-10-4-apps-and-integrations-changes-in-v2-1-101|4 Apps and Integrations changes in v2.1.101]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-10-added-os-ca-certificate-store-trust-by-default-so-enterprise-tls-proxies-work-wi|Added OS CA certificate store trust by default, so enterprise TLS proxies work…]] · Enterprise and Administration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-10-f193cf&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-10-5-other-changes-in-v2-1-101.md%0ACard%20ID%3A%20claude-code-2026-04-10-f193cf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.101%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->