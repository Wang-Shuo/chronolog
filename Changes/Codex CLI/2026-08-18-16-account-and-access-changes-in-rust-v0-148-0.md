---
card_id: codex-cli-2026-08-18-a1d455
date: '2026-08-18'
description: 'Codex CLI · 2026-08-18 · Account and Access: 16 changes in 0.148.0 —
  Turns reconnect through temporary provider outages, and MCP servers recover after
  OAuth…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2212
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6a02ef38d493b3eda54a964b32012be1ae53f2538acbe5404dca7b10c2de2134
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-18-a1d455
  comparison: ''
  date: '2026-08-18'
  description: 'Codex CLI — 0.148.0: 16 Account and Access changes'
  evidence:
  - quote: 'Turns reconnect through temporary provider outages, and MCP servers recover
      after OAuth reauthentication without restarting Codex. (#37337, #37485, #38418)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: 'TUI startup no longer lets buffered terminal input activate prompts accidentally,
      and onboarding appears when authentication is missing. (#38641, #38643, #38644)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37337 Recover MCP servers after OAuth reauthentication @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37842 Speed up MCP OAuth credential reads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37860 Speed up MCP OAuth credential reads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37866 Add MCP OAuth credential contention regression tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38052 Add per-login MCP OAuth client registration selection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38054 Add configuration-backed external authentication @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38089 Add CIMD support to MCP OAuth registration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38188 Integrate workload identity with Codex authentication @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38258 Unify external authentication provider handling @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38418 Clarify MCP OAuth reauthentication errors @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38429 Route curated plugin catalogs by authentication mode @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38448 Support per-server MCP OAuth callback ports @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38643 Delay the startup composer until first-login onboarding @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38644 Show onboarding when Codex home lacks authentication state @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 16-account-and-access-changes-in-rust-v0-148-0
  source_release: codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae
  source_type: github_releases
  theme: account-access
  title: 16 Account and Access changes in rust-v0.148.0
  type: change
related_changes:
- '[[Changes/Replit/2026-08-14-migrate-to-clerk-auth|Migrate to Clerk Auth]]'
- '[[Changes/v0/2026-08-14-expired-sessions-recover-instead-of-dropping-you-into-a-personal-only-or-logged|Expired
  sessions recover instead of dropping you into a personal-only or logged-out…]]'
- '[[Changes/Claude Code/2026-08-17-2-account-and-access-changes-in-v2-1-234|2 Account
  and Access changes in v2.1.234]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae|codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae]]'
source_type: github_releases
theme: account-access
title: 16 Account and Access changes in rust-v0.148.0
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Account and Access changes in rust-v0.148.0

**Codex CLI** · 2026-08-18 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.148.0) · from [[Releases/Codex CLI/codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae|0.148.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Turns reconnect through temporary provider outages, and MCP servers recover after OAuth reauthentication without restarting Codex. (#37337, #37485, #38418)

> TUI startup no longer lets buffered terminal input activate prompts accidentally, and onboarding appears when authentication is missing. (#38641, #38643, #38644)

> #37337 Recover MCP servers after OAuth reauthentication @copyberry

> #37842 Speed up MCP OAuth credential reads @copyberry

> #37860 Speed up MCP OAuth credential reads @copyberry

> #37866 Add MCP OAuth credential contention regression tests @copyberry

> #38052 Add per-login MCP OAuth client registration selection @copyberry

> #38054 Add configuration-backed external authentication @copyberry

> #38089 Add CIMD support to MCP OAuth registration @copyberry

> #38188 Integrate workload identity with Codex authentication @copyberry

> #38258 Unify external authentication provider handling @copyberry

> #38418 Clarify MCP OAuth reauthentication errors @copyberry

> #38429 Route curated plugin catalogs by authentication mode @copyberry

> #38448 Support per-server MCP OAuth callback ports @copyberry

> #38643 Delay the startup composer until first-login onboarding @copyberry

> #38644 Show onboarding when Codex home lacks authentication state @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.148.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-18-57-apps-and-integrations-changes-in-rust-v0-148-0|57 Apps and Integrations changes in rust-v0.148.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-18-13-interface-experience-changes-in-rust-v0-148-0|13 Interface Experience changes in rust-v0.148.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-18-18-model-support-changes-in-rust-v0-148-0|18 Model Support changes in rust-v0.148.0]] · Model Support
- [[Changes/Codex CLI/2026-08-18-3-mobile-and-desktop-changes-in-rust-v0-148-0|3 Mobile and Desktop changes in rust-v0.148.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-18-5-developer-workflow-changes-in-rust-v0-148-0|5 Developer Workflow changes in rust-v0.148.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-18-38650-canonicalize-default-namespaces-in-grpc-subscription-filters-copyberry|♯38650 Canonicalize default namespaces in gRPC subscription filters @copyberry]] · Pricing Model
- [[Changes/Codex CLI/2026-08-18-37828-track-running-unified-exec-processes-at-turn-completion-copyberry|♯37828 Track running unified exec processes at turn completion @copyberry]] · Editor Experience
- [[Changes/Codex CLI/2026-08-18-17-safety-and-privacy-changes-in-rust-v0-148-0|17 Safety and Privacy changes in rust-v0.148.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-18-13-context-window-changes-in-rust-v0-148-0|13 Context Window changes in rust-v0.148.0]] · Context Window
- [[Changes/Codex CLI/2026-08-18-12-agent-mode-changes-in-rust-v0-148-0|12 Agent Mode changes in rust-v0.148.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-18-38024-expose-image-generation-usage-limit-failures-copyberry|♯38024 Expose image generation usage-limit failures @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-18-5-collaboration-changes-in-rust-v0-148-0|5 Collaboration changes in rust-v0.148.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-18-231-other-changes-in-rust-v0-148-0|231 other changes in rust-v0.148.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-08-17 · Claude Code · [[Changes/Claude Code/2026-08-17-2-account-and-access-changes-in-v2-1-234|2 Account and Access changes in v2.1.234]]
- Later: 2026-08-20 · Codex CLI · [[Changes/Codex CLI/2026-08-20-8-account-and-access-changes-in-rust-v0-149-0|8 Account and Access changes in rust-v0.149.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-18-a1d455&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-18-16-account-and-access-changes-in-rust-v0-148-0.md%0ACard%20ID%3A%20codex-cli-2026-08-18-a1d455%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.148.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->