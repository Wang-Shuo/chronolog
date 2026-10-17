---
card_id: claude-code-2026-04-22-26e19a
date: '2026-04-22'
description: 'Claude Code · 2026-04-22 · Apps and Integrations: 4 changes in v2.1.117
  — Faster startup when both local and claude.ai MCP servers are configured (concurrent…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1126
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a244586e10e4e719fef1bc175319535f2a914661685bf9a448d554d1fd0a3fd7
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-22-26e19a
  comparison: ''
  date: '2026-04-22'
  description: 'Claude Code — v2.1.117: 4 Apps and Integrations changes'
  evidence:
  - quote: Faster startup when both local and claude.ai MCP servers are configured
      (concurrent connect now default)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.117
  - quote: '`plugin install` on an already-installed plugin now installs any missing
      dependencies instead of stopping at "already installed"'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.117
  - quote: Plugin dependency errors now say "not installed" with an install hint,
      and `claude plugin marketplace add` now auto-resolves missing dependencies from
      configured marketplaces
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.117
  - quote: Managed-settings `blockedMarketplaces` and `strictKnownMarketplaces` are
      now enforced on plugin install, update, refresh, and autoupdate
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.117
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-apps-and-integrations-changes-in-v2-1-117
  source_release: claude-code-2026-04-22-v2-1-117-github-311984967-1d917373
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v2.1.117
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-15-4-apps-and-integrations-changes-in-v2-1-110|4
  Apps and Integrations changes in v2.1.110]]'
- '[[Changes/Claude Code/2026-04-16-2-apps-and-integrations-changes-in-v2-1-111|2
  Apps and Integrations changes in v2.1.111]]'
- '[[Changes/Claude Code/2026-04-20-2-apps-and-integrations-changes-in-v2-1-116|2
  Apps and Integrations changes in v2.1.116]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-22-v2-1-117-github-311984967-1d917373|claude-code-2026-04-22-v2-1-117-github-311984967-1d917373]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v2.1.117
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v2.1.117

**Claude Code** · 2026-04-22 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.117) · from [[Releases/Claude Code/claude-code-2026-04-22-v2-1-117-github-311984967-1d917373|v2.1.117]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Faster startup when both local and claude.ai MCP servers are configured (concurrent connect now default)

> `plugin install` on an already-installed plugin now installs any missing dependencies instead of stopping at "already installed"

> Plugin dependency errors now say "not installed" with an install hint, and `claude plugin marketplace add` now auto-resolves missing dependencies from configured marketplaces

> Managed-settings `blockedMarketplaces` and `strictKnownMarketplaces` are now enforced on plugin install, update, refresh, and autoupdate

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.117
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-22-native-builds-on-macos-and-linux-the-glob-and-grep-tools-are-replaced-by-embedde|Native builds on macOS and Linux]] · Mobile and Desktop
- [[Changes/Claude Code/2026-04-22-2-developer-workflow-changes-in-v2-1-117|2 Developer Workflow changes in v2.1.117]] · Developer Workflow
- [[Changes/Claude Code/2026-04-22-windows-cached-where-exe-executable-lookups-per-process-for-faster-subprocess-la|Windows: cached where.exe executable lookups per process for faster subprocess launches]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-22-2-model-support-changes-in-v2-1-117|2 Model Support changes in v2.1.117]] · Model Support
- [[Changes/Claude Code/2026-04-22-opentelemetry-user-prompt-events-now-include-command-name-and-command-source-for|OpenTelemetry: user_prompt events now include command_name and command_source…]] · Pricing Model
- [[Changes/Claude Code/2026-04-22-2-agent-mode-changes-in-v2-1-117|2 Agent Mode changes in v2.1.117]] · Agent Mode
- [[Changes/Claude Code/2026-04-22-advisor-tool-experimental-dialog-now-carries-an-experimental-label-learn-more-li|Advisor Tool (experimental)]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-20 · Claude Code · [[Changes/Claude Code/2026-04-20-2-apps-and-integrations-changes-in-v2-1-116|2 Apps and Integrations changes in v2.1.116]]
- Later: 2026-04-23 · Claude Code · [[Changes/Claude Code/2026-04-23-3-apps-and-integrations-changes-in-v2-1-119|3 Apps and Integrations changes in v2.1.119]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-22-26e19a&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-22-4-apps-and-integrations-changes-in-v2-1-117.md%0ACard%20ID%3A%20claude-code-2026-04-22-26e19a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.117%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->