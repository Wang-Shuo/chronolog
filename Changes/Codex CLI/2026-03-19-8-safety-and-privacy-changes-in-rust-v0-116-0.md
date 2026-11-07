---
card_id: codex-cli-2026-03-19-701657
date: '2026-03-19'
description: 'Codex CLI · 2026-03-19 · Safety and Privacy: 8 changes in 0.116.0 —
  Improved Linux sandbox startup on symlinked checkouts, missing writable roots, and…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2060
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8d436dfa82d7f679fc954598756678bd61eec9f745d1a119a73c6e4fd5e74ed4
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-19-701657
  comparison: ''
  date: '2026-03-19'
  description: 'Codex CLI — 0.116.0: 8 Safety and Privacy changes'
  evidence:
  - quote: 'Improved Linux sandbox startup on symlinked checkouts, missing writable
      roots, and Ubuntu/AppArmor hosts by preferring system `bwrap` when available.
      (#14849, #14890, #14963)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14665 Use request permission profile in app server @mousseau-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14139 windows-sandbox: add runner IPC foundation for future unified_exec
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14849 fix: canonicalize symlinked Linux sandbox cwd @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14890 fix(linux-sandbox): ignore missing writable roots @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14963 fix(linux-sandbox): prefer system /usr/bin/bwrap when available
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14293 fix: honor active permission profiles in sandbox debug @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  - quote: '#14610 feat: support restricted ReadOnlyAccess in elevated Windows sandbox
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.116.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-safety-and-privacy-changes-in-rust-v0-116-0
  source_release: codex-cli-2026-03-19-rust-v0-116-0-github-299083035-eb74e2fd
  source_type: github_releases
  theme: safety-privacy
  title: 8 Safety and Privacy changes in rust-v0.116.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-03-17-3-safety-and-privacy-changes-in-v0-34-0|3 Safety
  and Privacy changes in v0.34.0]]'
- '[[Changes/Ollama/2026-03-17-ci-cd-generate-code-reviews-security-checks-and-other-tasks-within-your-ci|CI/CD:
  Generate code reviews, security checks, and other tasks within your CI]]'
- '[[Changes/Claude Code/2026-03-18-fixed-custom-status-line-showing-nothing-when-workspace-trust-is-blocking-it|Fixed
  custom status line showing nothing when workspace trust is blocking it]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-19-rust-v0-116-0-github-299083035-eb74e2fd|codex-cli-2026-03-19-rust-v0-116-0-github-299083035-eb74e2fd]]'
source_type: github_releases
theme: safety-privacy
title: 8 Safety and Privacy changes in rust-v0.116.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Safety and Privacy changes in rust-v0.116.0

**Codex CLI** · 2026-03-19 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.116.0) · from [[Releases/Codex CLI/codex-cli-2026-03-19-rust-v0-116-0-github-299083035-eb74e2fd|0.116.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved Linux sandbox startup on symlinked checkouts, missing writable roots, and Ubuntu/AppArmor hosts by preferring system `bwrap` when available. (#14849, #14890, #14963)

> #14665 Use request permission profile in app server @mousseau-oai

> #14139 windows-sandbox: add runner IPC foundation for future unified_exec @iceweasel-oai

> #14849 fix: canonicalize symlinked Linux sandbox cwd @viyatb-oai

> #14890 fix(linux-sandbox): ignore missing writable roots @viyatb-oai

> #14963 fix(linux-sandbox): prefer system /usr/bin/bwrap when available @viyatb-oai

> #14293 fix: honor active permission profiles in sandbox debug @viyatb-oai

> #14610 feat: support restricted ReadOnlyAccess in elevated Windows sandbox @viyatb-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.116.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-19-2-model-support-changes-in-rust-v0-116-0|2 Model Support changes in rust-v0.116.0]] · Model Support
- [[Changes/Codex CLI/2026-03-19-10-apps-and-integrations-changes-in-rust-v0-116-0|10 Apps and Integrations changes in rust-v0.116.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-19-2-voice-and-audio-changes-in-rust-v0-116-0|2 Voice and Audio changes in rust-v0.116.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-19-14986-temporarily-disable-private-desktop-until-it-works-with-elevated-ipc-path|♯14986 temporarily disable private desktop until it works with elevated IPC path…]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-19-14829-stack-3-4-add-current-thread-context-to-realtime-startup-aibrahim-oai|♯14829 stack 3/4 Add current thread context to realtime startup @aibrahim-oai]] · Context Window
- [[Changes/Codex CLI/2026-03-19-app-server-tui-now-supports-device-code-chatgpt-sign-in-during-onboarding-and-ca|App-server TUI now supports device-code ChatGPT sign-in during onboarding and can…]] · Account and Access
- [[Changes/Codex CLI/2026-03-19-5-agent-mode-changes-in-rust-v0-116-0|5 Agent Mode changes in rust-v0.116.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-19-2-interface-experience-changes-in-rust-v0-116-0|2 Interface Experience changes in rust-v0.116.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-19-4-memory-and-personalization-changes-in-rust-v0-116-0|4 Memory and Personalization changes in rust-v0.116.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-19-5-developer-workflow-changes-in-rust-v0-116-0|5 Developer Workflow changes in rust-v0.116.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-19-34-other-changes-in-rust-v0-116-0|34 other changes in rust-v0.116.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-18 · Claude Code · [[Changes/Claude Code/2026-03-18-fixed-custom-status-line-showing-nothing-when-workspace-trust-is-blocking-it|Fixed custom status line showing nothing when workspace trust is blocking it]]
- Later: 2026-03-20 · Claude Code · [[Changes/Claude Code/2026-03-20-2-safety-and-privacy-changes-in-v2-1-81|2 Safety and Privacy changes in v2.1.81]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-19-701657&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-19-8-safety-and-privacy-changes-in-rust-v0-116-0.md%0ACard%20ID%3A%20codex-cli-2026-03-19-701657%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.116.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->