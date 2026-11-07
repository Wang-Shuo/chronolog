---
card_id: codex-cli-2026-05-26-bf78b8
date: '2026-05-26'
description: 'Codex CLI · 2026-05-26 · Safety and Privacy: 7 changes in 0.134.0 —
  Made `--profile` the primary profile selector across CLI, TUI permissions, and sandbox…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2128
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9885c638828d88e713894e70f5ffa41687750d9c48b0f1d178c986c70a516e66
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-26-bf78b8
  comparison: ''
  date: '2026-05-26'
  description: 'Codex CLI — 0.134.0: 7 Safety and Privacy changes'
  evidence:
  - quote: 'Made `--profile` the primary profile selector across CLI, TUI permissions,
      and sandbox flows, with legacy profile configs rejected through migration guidance.
      (#23708, #23883, #23890, #24051, #24055, #24059, #24067, #24110)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: Preserved active permission profile metadata when syncing auto-review runtime
      settings. (#23956)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23708 tui: plumb permission profile selection @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23956 Fix auto-review permission profile override @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24102 cli: infer host sandbox backend @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24117 [codex] Use rolling files for Windows sandbox logs @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24110 cli: support --profile for codex sandbox @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-safety-and-privacy-changes-in-rust-v0-134-0
  source_release: codex-cli-2026-05-26-rust-v0-134-0-github-329640454-7be6059e
  source_type: github_releases
  theme: safety-privacy
  title: 7 Safety and Privacy changes in rust-v0.134.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-05-22-docs-add-vi-mode-shortcuts-and-clarify-mcp-custom-sandbox-setup-by-chrisjcthomas|docs:
  add vi mode shortcuts and clarify MCP/custom sandbox setup]]'
- '[[Changes/GitHub Copilot CLI/2026-05-23-2-safety-and-privacy-changes-in-v1-0-52|2
  Safety and Privacy changes in v1.0.52]]'
- '[[Changes/AnythingLLM/2026-05-26-this-is-we-believe-a-fundamental-shift-in-how-ai-assistants-work-for-the-first-t|This
  is, we believe, a fundamental shift in how AI assistants work]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-26-rust-v0-134-0-github-329640454-7be6059e|codex-cli-2026-05-26-rust-v0-134-0-github-329640454-7be6059e]]'
source_type: github_releases
theme: safety-privacy
title: 7 Safety and Privacy changes in rust-v0.134.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in rust-v0.134.0

**Codex CLI** · 2026-05-26 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.134.0) · from [[Releases/Codex CLI/codex-cli-2026-05-26-rust-v0-134-0-github-329640454-7be6059e|0.134.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Made `--profile` the primary profile selector across CLI, TUI permissions, and sandbox flows, with legacy profile configs rejected through migration guidance. (#23708, #23883, #23890, #24051, #24055, #24059, #24067, #24110)

> Preserved active permission profile metadata when syncing auto-review runtime settings. (#23956)

> #23708 tui: plumb permission profile selection @viyatb-oai

> #23956 Fix auto-review permission profile override @etraut-openai

> #24102 cli: infer host sandbox backend @bolinfest

> #24117 [codex] Use rolling files for Windows sandbox logs @iceweasel-oai

> #24110 cli: support --profile for codex sandbox @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.134.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-26-3-agent-mode-changes-in-rust-v0-134-0|3 Agent Mode changes in rust-v0.134.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-26-11-apps-and-integrations-changes-in-rust-v0-134-0|11 Apps and Integrations changes in rust-v0.134.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-26-22915-3-of-4-tui-route-feature-and-memory-toggles-through-app-server-etraut-open|♯22915 3 of 4 tui: route feature and memory toggles through app server @etraut-openai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-26-23736-add-new-enterprise-requirement-gate-adams-oai|♯23736 Add new enterprise requirement gate @adams-oai]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-05-26-5-context-window-changes-in-rust-v0-134-0|5 Context Window changes in rust-v0.134.0]] · Context Window
- [[Changes/Codex CLI/2026-05-26-2-account-and-access-changes-in-rust-v0-134-0|2 Account and Access changes in rust-v0.134.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-26-2-mobile-and-desktop-changes-in-rust-v0-134-0|2 Mobile and Desktop changes in rust-v0.134.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-26-47-other-changes-in-rust-v0-134-0|47 other changes in rust-v0.134.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-26 · AnythingLLM · [[Changes/AnythingLLM/2026-05-26-this-is-we-believe-a-fundamental-shift-in-how-ai-assistants-work-for-the-first-t|This is, we believe, a fundamental shift in how AI assistants work]]
- Later: 2026-05-27 · Claude Code · [[Changes/Claude Code/2026-05-27-2-safety-and-privacy-changes-in-v2-1-152|2 Safety and Privacy changes in v2.1.152]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-26-bf78b8&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-26-7-safety-and-privacy-changes-in-rust-v0-134-0.md%0ACard%20ID%3A%20codex-cli-2026-05-26-bf78b8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.134.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->